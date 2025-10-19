#!/usr/bin/env python3
"""
fetch_telegram_releases.py

Scrape release notes for Gunbot from a Telegram "Announcements" channel and
emit a machine-readable JSON bundle for downstream processing.

Release window:
  - begins at a post like "Gunbot v<semver>"
  - ends at the first post that includes https://www.gunbot.com/downloads

Between those markers we:
  - store regular "detail" posts (lightly filtered for change-like lines)
  - treat Forwarded messages specially:
      * resolve the original author (user/channel) as the 'committer'
      * keep the forward's title line PLUS pruned change bullets
  - support "@user commits:" markers; subsequent change posts in the same
    release get "committer": "@user" until another commits marker or until
    the release ends (download link seen)

Env vars:
  TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_SESSION (Telethon StringSession)
  TG_CHANNEL   -> numeric id (e.g. -1001122850092) or @username
  SINCE_DAYS   -> default 14
  MAX_MESSAGES -> default 400
"""

from __future__ import annotations

import asyncio
import datetime as dt
import json
import os
import re
from typing import Dict, List, Optional, Tuple

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.patched import Message
from telethon.tl.types import PeerChannel, PeerUser

# ---------------------------- Config -----------------------------------------

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
SESSION = os.environ["TELEGRAM_SESSION"]

CHANNEL_INPUT_RAW = os.environ.get("TG_CHANNEL", "").strip()
if not CHANNEL_INPUT_RAW:
    raise SystemExit("Set TG_CHANNEL to the channel id (e.g. -100...) or @username.")

# Cast numeric channel ids to int so Telethon can resolve them
if re.fullmatch(r"-?\d+", CHANNEL_INPUT_RAW):
    CHANNEL_INPUT = int(CHANNEL_INPUT_RAW)
else:
    CHANNEL_INPUT = CHANNEL_INPUT_RAW  # @username

SINCE_DAYS = int(os.environ.get("SINCE_DAYS", "14"))
MAX_MESSAGES = int(os.environ.get("MAX_MESSAGES", "400"))

CUTOFF = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=SINCE_DAYS)

# ---------------------------- Regex ------------------------------------------

# Anchor allows optional leading "v" but we capture only the numeric part
ANCHOR_RE    = re.compile(r"^\s*Gunbot\s+v?(\d+\.\d+\.\d+)\b", re.I)
DOWNLOAD_RE  = re.compile(r"https?://www\.gunbot\.com/downloads/?", re.I)

# Keep headings like: Introducing..., In This Update, Changes in Behaviour, Enhancements, Bug Fixes
KEEP_HEADING_RE = re.compile(
    r"^\s*(introducing|in\s+this\s+update|changes\s+in\s+behavio[u]r|enhancements?|bug\s*fixes?)\b",
    re.I,
)

# Lines that are obviously change-like
KEEP_LINE_RE = re.compile(
    r"""
    ^\s*[-•–]\s+                                  |  # bullets
    \b(?:fix|fixed|bug|issue|patch|resolve[sd]?)\b|  # bugfixes
    \b(?:add|added|introduc(e|ed)|enable[sd]?|new)\b|# additions
    \b(?:change[sd]?|tweak[sd]?|adjust(ed)?|update[sd]?|upgrade[sd]?)\b|
    \b(?:improv(e|ed|ement)|optimis(e|ed|ation)|optimiz(e|ed|ation)|performance)\b|
    \b(?:security|safe\s*mode|stale\s*data)\b     |
    \b(?:gui|server|endpoint|orderbook|dashboard|athena|options?)\b
    """,
    re.I | re.VERBOSE,
)

# Section blocks like: "Changes in Behaviour:", "Enhancements:", "Bug Fixes:"
SECTION_HEAD_RE = re.compile(
    r"^\s*(changes\s+in\s+behavio[u]r|enhancements?|bug\s*fixes?)\s*:\s*$",
    re.I,
)

# Noise to drop
DROP_LINE_RE = re.compile(
    r"""
    ^\s*(telegram|request\s+to\s+join)\b   |
    \b(join\s+us\s+in\s+our\s+telegram)\b  |
    \binvites?\s+you\s+to\s+join\b         |
    \bcommunity\b                          |
    \bfiles\s+are\s+being\s+uploaded\b
    """,
    re.I | re.VERBOSE,
)

# "@username commits:" marker
COMMITS_LINE_RE = re.compile(r"^@\s?([A-Za-z0-9_]+)\s+commits?:\s*$", re.I)

# ---------------------------- Helpers -----------------------------------------

def normalize_text(t: Optional[str]) -> str:
    """Keep Unicode (incl. emojis). Only drop nulls and normalize newlines."""
    if not t:
        return ""
    t = t.replace("\x00", "")
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return t.strip()

def extract_change_lines(text: str) -> List[str]:
    """Return lines that are change-like, including section blocks."""
    lines = [ln.rstrip() for ln in (text or "").splitlines()]
    out: List[str] = []
    in_section = False

    for raw in lines:
        l = raw.strip()
        if not l:
            in_section = False
            continue

        if SECTION_HEAD_RE.match(l):
            out.append(f"- {l.rstrip(':')}:")
            in_section = True
            continue

        if in_section:
            out.append(l if l.startswith(("-", "•", "–")) else f"- {l}")
            continue

        if KEEP_HEADING_RE.search(l) or KEEP_LINE_RE.search(l):
            out.append(l if l.startswith(("-", "•", "–")) else f"- {l}")

    # de-dupe preserving order
    seen = set()
    cleaned: List[str] = []
    for line in out:
        key = line.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(line)
    return cleaned

def prune_lines(raw: str) -> str:
    """Filter out noise then return a joined block."""
    if not raw:
        return ""
    kept = []
    for l in extract_change_lines(raw):
        if DROP_LINE_RE.search(l):
            continue
        kept.append(l)
    return "\n".join(kept).strip()

async def fetch_messages(client: TelegramClient, channel):
    """Yield messages newer than cutoff (newest first from Telegram)."""
    async for m in client.iter_messages(entity=channel, limit=MAX_MESSAGES):
        if m.date and m.date.replace(tzinfo=dt.timezone.utc) < CUTOFF:
            break
        yield m

async def extract_forward_meta(client: TelegramClient, m: Message) -> Tuple[bool, dict]:
    """
    If message is forwarded, resolve the origin into a small 'committer' dict.
    Returns (is_forwarded, meta_dict)
    """
    fwd = getattr(m, "fwd_from", None)
    if not fwd:
        return False, {}

    name = None
    username = None
    ident = None

    if getattr(fwd, "from_name", None):
        name = fwd.from_name

    ent = None
    if getattr(fwd, "from_id", None):
        try:
            if isinstance(fwd.from_id, (PeerUser, PeerChannel)):
                ent = await client.get_entity(fwd.from_id)
        except Exception:
            ent = None

    if ent is not None:
        ident = getattr(ent, "id", None)
        username = getattr(ent, "username", None)
        if not name:
            name = getattr(ent, "title", None)
            if not name:
                fn = getattr(ent, "first_name", "") or ""
                ln = getattr(ent, "last_name", "") or ""
                name = (fn + " " + ln).strip() or None

    if not name:
        name = "Unknown"

    return True, {
        "committer": name,
        "committer_username": username,
        "committer_id": ident,
    }

def iso(ts: Optional[dt.datetime]) -> str:
    return (ts or dt.datetime.now(dt.timezone.utc)).astimezone(dt.timezone.utc).isoformat()

# ---------------------------- Core logic -------------------------------------

async def build_releases() -> Dict[str, dict]:
    async with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
        try:
            messages = [m async for m in fetch_messages(client, CHANNEL_INPUT)]
        except Exception as e:
            hint = (
                "Could not resolve TG channel. If you used a numeric id, make sure "
                "TG_CHANNEL is numeric (no quotes) or use @username. "
                "Also ensure the session account can view that channel."
            )
            raise SystemExit(f"Channel resolution failed: {e}\n{hint}")

        messages.sort(key=lambda x: x.date or dt.datetime.min.replace(tzinfo=dt.timezone.utc))

        releases: Dict[str, dict] = {}
        current_version: Optional[str] = None
        pending_committer: Optional[str] = None  # from "@user commits:"

        for m in messages:
            text_raw = normalize_text(m.message or m.text or "")
            if not text_raw:
                continue

            # anchor?
            ma = ANCHOR_RE.search(text_raw)
            if ma:
                numeric = ma.group(1)           # e.g. "30.6.7"
                ver = f"v{numeric}"             # store with leading "v"
                current_version = ver
                releases[current_version] = {
                    "version": ver,             # <-- always "vX.Y.Z"
                    "anchor_id": m.id,
                    "anchor_time": iso(m.date),
                    "posts": [
                        {"id": m.id, "date": iso(m.date), "type": "anchor", "text": f"Gunbot v{numeric}"}
                    ],
                }
                pending_committer = None
                continue

            if not current_version:
                continue  # chatter before the first anchor

            # commits marker?
            cm = COMMITS_LINE_RE.match(text_raw)
            if cm:
                pending_committer = f"@{cm.group(1)}"
                continue

            # end marker?
            if DOWNLOAD_RE.search(text_raw):
                releases[current_version]["posts"].append(
                    {"id": m.id, "date": iso(m.date), "type": "download", "text": text_raw}
                )
                current_version = None
                pending_committer = None
                continue

            # details: forwarded vs normal
            is_fwd, fmeta = await extract_forward_meta(client, m)
            if is_fwd:
                lines = [ln.strip() for ln in text_raw.splitlines() if ln.strip()]
                title = lines[0] if lines else ""
                bullets = prune_lines(text_raw)
                merged_text = title if not bullets else f"{title}\n{bullets}"
                if merged_text.strip():
                    post = {
                        "id": m.id,
                        "date": iso(m.date),
                        "type": "detail",
                        "forwarded": True,
                        "text": merged_text.strip(),
                        **fmeta,
                    }
                    releases[current_version]["posts"].append(post)
                continue

            # normal detail
            kept = prune_lines(text_raw)
            if kept:
                post = {
                    "id": m.id,
                    "date": iso(m.date),
                    "type": "detail",
                    "forwarded": False,
                    "text": kept,
                }
                if pending_committer:
                    post["committer"] = pending_committer
                releases[current_version]["posts"].append(post)

        ordered = sorted(releases.values(), key=lambda r: r["anchor_time"], reverse=True)
        return {"releases": ordered}

def main():
    data = asyncio.run(build_releases())
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
