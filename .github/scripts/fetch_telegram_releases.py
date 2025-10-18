#!/usr/bin/env python3
"""
Fetch grouped Gunbot releases from a private Telegram channel.

Grouping rules:
- Start at posts that begin with: "Gunbot vX.Y.Z"
- Collect all following posts until the first one containing: "https://www.gunbot.com/downloads"
- Skip obvious noise (resellers, community intros).
- Output JSON: {"releases":[{"version":"vX.Y.Z","anchor_id":...,"anchor_time":...,"posts":[...]}, ...]}

Env:
  TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_SESSION   # required (MTProto user session)
  TG_CHANNEL  # numeric private channel id, e.g. -10011
  SINCE_DAYS=7, MAX_MESSAGES=100   # tight defaults
"""
import os, re, json, datetime, sys
from typing import Dict, Any
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import PeerChannel

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
SESSION = os.environ["TELEGRAM_SESSION"]

# Use ONLY numeric private channel id (example: -1001122850092)
CHANNEL_INPUT = os.environ.get("TG_CHANNEL", "").strip()
if not CHANNEL_INPUT or not CHANNEL_INPUT.lstrip("-").isdigit():
    raise SystemExit("Set TG_CHANNEL to the numeric channel id, e.g. export TG_CHANNEL='-1001122850092'")

# Tight defaults as requested
SINCE_DAYS   = int(os.environ.get("SINCE_DAYS", "7"))     # at most 7 days back
MAX_MESSAGES = int(os.environ.get("MAX_MESSAGES", "100")) # last 100 messages

# Timezone-aware UTC (Python 3.11+)
cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=SINCE_DAYS)

ANCHOR_RE   = re.compile(r"^\s*Gunbot\s+v?(\d+\.\d+\.\d+)\b", re.I)
DOWNLOAD_RE = re.compile(r"https?://www\.gunbot\.com/downloads/?", re.I)

NOISE_HINTS = (
    "reseller", "resellers", "join our telegram", "community",
    "request to join", "introduction", "self-introduction", "support group"
)

def is_anchor(text: str):
    m = ANCHOR_RE.search(text or "")
    return (m is not None, f"v{m.group(1)}" if m else None)

def is_download_link(text: str):
    return bool(DOWNLOAD_RE.search(text or ""))

def is_noise(text: str):
    t = (text or "").lower()
    return any(h in t for h in NOISE_HINTS)

def msg_text(m) -> str:
    return (m.message or "").strip()

def resolve_channel(client: TelegramClient, ref: str):
    try:
        return client.get_entity(PeerChannel(int(ref)))
    except Exception as e:
        raise RuntimeError(
            f"Failed to resolve numeric channel ID {ref}. "
            "Ensure the Telegram account for this session is a member of the channel."
        ) from e

def main():
    result: Dict[str, Any] = {"releases": []}
    with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
        entity = resolve_channel(client, CHANNEL_INPUT)

        # Fetch newest → oldest with hard cap and cutoff
        collected = []
        for m in client.iter_messages(entity, reverse=False, limit=MAX_MESSAGES):
            if not m or not m.date:
                continue
            md_utc = m.date.astimezone(datetime.UTC)
            if md_utc < cutoff:
                break
            m._normalized_date = md_utc
            collected.append(m)
        # Chronological for grouping logic
        msgs = list(reversed(collected))

    if not msgs:
        print(json.dumps({"releases": []}, ensure_ascii=False, indent=2))
        return

    releases: Dict[str, Dict[str, Any]] = {}
    current_ver = None
    collecting = False

    for m in msgs:
        text = msg_text(m)
        if not text:
            continue

        # Start block on "Gunbot vX.Y.Z"
        anchor_flag, ver = is_anchor(text)
        if anchor_flag:
            current_ver = ver
            collecting = True
            if ver not in releases:
                releases[ver] = {
                    "version": ver,
                    "anchor_id": m.id,
                    "anchor_time": m._normalized_date.isoformat(),
                    "posts": []
                }
            releases[ver]["posts"].append({
                "id": m.id, "date": m._normalized_date.isoformat(),
                "text": text, "type": "anchor"
            })
            continue

        if not collecting or current_ver is None:
            continue

        # End block when download link appears
        if is_download_link(text):
            releases[current_ver]["posts"].append({
                "id": m.id, "date": m._normalized_date.isoformat(),
                "text": text, "type": "download"
            })
            current_ver = None
            collecting  = False
            continue

        # Skip obvious noise
        if is_noise(text):
            continue

        releases[current_ver]["posts"].append({
            "id": m.id, "date": m._normalized_date.isoformat(),
            "text": text, "type": "detail"
        })

    ordered = sorted(releases.values(), key=lambda r: r["anchor_time"], reverse=True)
    print(json.dumps({"releases": ordered}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
