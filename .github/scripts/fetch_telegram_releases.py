#!/usr/bin/env python3
import os, re, json, datetime
from typing import Dict, Any, List
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
SESSION = os.environ["TELEGRAM_SESSION"]
CHANNEL = os.environ.get("TG_CHANNEL", "GunthyAnnouncements")  # e.g. t.me/GunthyAnnouncements

SINCE_DAYS = int(os.environ.get("SINCE_DAYS", "14"))

cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=SINCE_DAYS)

ANCHOR_RE = re.compile(r"^\s*Gunbot\s+v?(\d+\.\d+\.\d+)\b", re.I)
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

def main():
    result: Dict[str, Any] = {"releases": []}

    with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
        entity = client.get_entity(CHANNEL)
        msgs = list(client.iter_messages(entity, reverse=True))  # chronological

    # filter by time
    msgs = [m for m in msgs if m.date and m.date.replace(tzinfo=None) >= cutoff]

    releases: Dict[str, Dict[str, Any]] = {}
    current_ver = None
    collecting = False

    for m in msgs:
        text = msg_text(m)
        if not text:
            continue

        # Start of a release block
        anchor_flag, ver = is_anchor(text)
        if anchor_flag:
            current_ver = ver
            collecting = True
            if ver not in releases:
                releases[ver] = {
                    "version": ver,
                    "anchor_id": m.id,
                    "anchor_time": m.date.isoformat(),
                    "posts": []
                }
            releases[ver]["posts"].append({"id": m.id, "date": m.date.isoformat(), "text": text, "type": "anchor"})
            continue

        if not collecting or current_ver is None:
            continue

        # End of block when download link appears
        if is_download_link(text):
            releases[current_ver]["posts"].append({"id": m.id, "date": m.date.isoformat(), "text": text, "type": "download"})
            # stop collecting until next anchor
            current_ver = None
            collecting = False
            continue

        # Skip obvious noise between anchor and download
        if is_noise(text):
            continue

        releases[current_ver]["posts"].append({"id": m.id, "date": m.date.isoformat(), "text": text, "type": "detail"})

    ordered = sorted(releases.values(), key=lambda r: r["anchor_time"], reverse=True)
    result["releases"] = ordered
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
