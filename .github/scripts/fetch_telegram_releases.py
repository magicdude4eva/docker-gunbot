#!/usr/bin/env python3
"""
Fetch Gunbot release messages from a private Telegram channel and output structured JSON.

Grouping rules:
  • Start collecting when a post begins with:  "Gunbot vX.Y.Z"
  • Collect all following posts (incl. forwarded) until the first post that contains:
      https://www.gunbot.com/downloads
  • Keep only lines that look like change notes (bullets or fix/add/change/update/etc.).
    Strip promo/invite lines from forwarded messages instead of dropping the whole post.
  • Skip a post entirely only if it has no relevant lines after pruning.

Output JSON:
{
  "releases": [
    {
      "version": "v30.6.7",
      "anchor_id": 12345,
      "anchor_time": "2025-10-16T17:04:00+00:00",
      "posts": [
        {"id": 12345, "date": "...", "type": "anchor",  "text": "Gunbot v30.6.7"},
        {"id": 12346, "date": "...", "type": "detail",  "text": "- Fix ..."},
        {"id": 12347, "date": "...", "type": "download","text": "files are now available at https://www.gunbot.com/downloads"}
      ]
    }
  ]
}

Env:
  TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_SESSION  -> Telethon user session
  TG_CHANNEL  -> numeric private channel id (e.g., -1001122850092)
Optional:
  SINCE_DAYS=7, MAX_MESSAGES=100
"""

import os
import re
import sys
import json
import datetime
from typing import Dict, Any

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import PeerChannel

# --- Config -----------------------------------------------------------------

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
SESSION = os.environ["TELEGRAM_SESSION"]

CHANNEL_INPUT = os.environ.get("TG_CHANNEL", "").strip()
if not CHANNEL_INPUT or not CHANNEL_INPUT.lstrip("-").isdigit():
    raise SystemExit("Set TG_CHANNEL to the numeric channel id, e.g. export TG_CHANNEL='-1001122850092'")

SINCE_DAYS   = int(os.environ.get("SINCE_DAYS", "7"))
MAX_MESSAGES = int(os.environ.get("MAX_MESSAGES", "100"))

cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=SINCE_DAYS)

# --- Patterns ---------------------------------------------------------------

ANCHOR_RE    = re.compile(r"^\s*Gunbot\s+v?(\d+\.\d+\.\d+)\b", re.I)
DOWNLOAD_RE  = re.compile(r"https?://www\.gunbot\.com/downloads/?", re.I)

# Lines to KEEP inside a post (bullets or change-y phrases)
KEEP_LINE_RE = re.compile(
    r"""
    ^\s*[-•–]\s+                              |  # bullet lines
    ^\s*\#?                                   # optional leading '#'
    (?:fix|fixed|add|added|change|changed|
       update|updated|improve|improved|
       optimi[sz]e|bug|gui|server|performance|
       strategy|athena|ghostrider|wick)\b
    """,
    re.I | re.X,
)

# Lines to DROP if not useful (promo/noise)
DROP_LINE_RE = re.compile(
    r"(join (our|us) on telegram|request to join|t\.me/|invite|contact them|support group)",
    re.I,
)

NOISE_HINTS = (
    "reseller", "resellers", "community",
    "introduction", "self-introduction",
)

# --- Helpers ----------------------------------------------------------------

def is_anchor(text: str):
    m = ANCHOR_RE.search(text or "")
    return (m is not None, f"v{m.group(1)}" if m else None)

def is_download_link(text: str):
    return bool(DOWNLOAD_RE.search(text or ""))

def msg_text(m) -> str:
    return (m.message or "").strip()

def prune_message_text(raw: str) -> str:
    """
    Keep relevant lines from a post; drop pure promo lines.
    If nothing matches keep-criteria, return empty string.
    """
    out = []
    for ln in (raw or "").splitlines():
        l = ln.strip()
        if not l:
            continue
        if KEEP_LINE_RE.search(l):
            out.append(l if l.startswith(("-", "•", "–")) else f"- {l}")
            continue
        if DROP_LINE_RE.search(l):
            continue
        # Keep short technical fragments, drop chatter
        if len(l) >= 6 and not any(h in l.lower() for h in ("request to join", "telegram group")):
            out.append(l if l.startswith(("-", "•", "–")) else f"- {l}")
    # De-duplicate while preserving order (case-insensitive)
    seen = set()
    cleaned = []
    for line in out:
        key = line.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(line)
    return "\n".join(cleaned)

def is_noise(text: str):
    """Treat as noise only if there are *no* relevant lines after pruning."""
    if not text:
        return True
    if KEEP_LINE_RE.search(text):
        return False
    t = text.lower()
    return any(h in t for h in NOISE_HINTS)

def resolve_channel(client: TelegramClient, ref: str):
    try:
        return client.get_entity(PeerChannel(int(ref)))
    except Exception as e:
        raise RuntimeError(
            f"Failed to resolve numeric channel ID {ref}. "
            "Ensure the Telegram account for this session is a member of the channel."
        ) from e

# --- Main -------------------------------------------------------------------

def main():
    result: Dict[str, Any] = {"releases": []}

    with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
        entity = resolve_channel(client, CHANNEL_INPUT)

        # Fetch newest → oldest; stop at cutoff and cap to MAX_MESSAGES
        collected = []
        for m in client.iter_messages(entity, reverse=False, limit=MAX_MESSAGES):
            if not m or not m.date:
                continue
            md_utc = m.date.astimezone(datetime.UTC)
            if md_utc < cutoff:
                break
            m._normalized_date = md_utc
            collected.append(m)

        msgs = list(reversed(collected))  # chronological for parser

    if not msgs:
        print(json.dumps({"releases": []}, ensure_ascii=False, indent=2))
        return

    releases: Dict[str, Dict[str, Any]] = {}
    current_ver = None
    collecting = False

    for m in msgs:
        raw = msg_text(m)
        text = prune_message_text(raw)

        # Start block on exact opener; use raw so we don't miss "Gunbot vX.Y.Z"
        a_flag, ver = is_anchor(raw)
        if a_flag:
            current_ver = ver
            collecting = True
            if ver not in releases:
                releases[ver] = {
                    "version": ver,
                    "anchor_id": m.id,
                    "anchor_time": m._normalized_date.isoformat(),
                    "posts": [],
                }
            releases[ver]["posts"].append({
                "id": m.id,
                "date": m._normalized_date.isoformat(),
                "text": f"Gunbot {ver}",
                "type": "anchor",
            })
            continue

        if not collecting or current_ver is None:
            continue

        # End block on first download link (use raw to be safe)
        if is_download_link(raw):
            releases[current_ver]["posts"].append({
                "id": m.id,
                "date": m._normalized_date.isoformat(),
                "text": raw.strip(),
                "type": "download",
            })
            current_ver = None
            collecting = False
            continue

        # Skip truly empty/noisy details
        if is_noise(text):
            continue

        releases[current_ver]["posts"].append({
            "id": m.id,
            "date": m._normalized_date.isoformat(),
            "text": text,
            "type": "detail",
        })

    ordered = sorted(releases.values(), key=lambda r: r["anchor_time"], reverse=True)
    print(json.dumps({"releases": ordered}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
