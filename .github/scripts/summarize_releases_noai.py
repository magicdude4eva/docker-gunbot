#!/usr/bin/env python3
"""
Deterministic release summary (no AI) for Gunbot Telegram data.

Input: JSON from fetch_telegram_releases.py
Output: Markdown:

### vX.Y.Z
- <post first line>
  - <post second line>
  - <post third line>

Rules:
- Ignore 'anchor' ("Gunbot vX.Y.Z") and 'download' posts.
- For each remaining post:
  * First non-empty line -> normalized as a single top-level bullet.
  * Subsequent non-empty lines -> normalized as sub-bullets (indented).
- Strip leading bullets, emojis, and @mentions before re-bulleting to avoid "- - ..." artifacts.
- De-duplicate case-insensitively while preserving order.
"""

import json
import sys
import re

# Detect a leading bullet we want to normalize away
LEADING_BULLET_RE = re.compile(r"^\s*([\-•–]\s+)")
# Strip common emoji prefix ranges
EMOJI_PREFIX_RE = re.compile(r"^[\u2600-\u26FF\u2700-\u27BF\U0001F300-\U0001FAFF]+\s*")
# Strip a leading @mention (e.g., @user:, @user )
MENTION_PREFIX_RE = re.compile(r"^@\w+[: ]\s*")

def _clean_line(s: str) -> str:
    s = s.strip()
    if not s:
        return ""
    # Remove obvious prefixes we don't want to duplicate
    s = EMOJI_PREFIX_RE.sub("", s)
    s = MENTION_PREFIX_RE.sub("", s)
    s = LEADING_BULLET_RE.sub("", s)  # drop any existing leading bullet
    # Collapse excessive spaces
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip()

def _normalize_post_to_markdown(text: str):
    """
    Turn a (possibly multi-line) post into:
      - First line (top-level bullet)
        - subsequent line
        - subsequent line
    """
    lines = [ln for ln in (text or "").splitlines()]
    # keep only non-empty after cleaning
    cleaned = [ _clean_line(ln) for ln in lines ]
    cleaned = [ ln for ln in cleaned if ln ]

    if not cleaned:
        return []

    first = f"- {cleaned[0]}"
    rest = [ f"  - {ln}" for ln in cleaned[1:] ]
    return [first] + rest

def summarize_release(rel: dict) -> str:
    version = rel.get("version", "").strip()
    posts = rel.get("posts", [])

    bullets = []
    seen = set()  # for de-dup (case-insensitive on the rendered lines)

    for p in posts:
        ptype = p.get("type")
        if ptype in ("anchor", "download"):
            continue  # skip these entirely

        text = (p.get("text") or "").strip()
        if not text:
            continue

        lines = _normalize_post_to_markdown(text)
        for ln in lines:
            key = ln.lower()
            if key in seen:
                continue
            seen.add(key)
            bullets.append(ln)

    if not bullets:
        return f"### {version}\n- (no granular changes posted)\n"

    return f"### {version}\n" + "\n".join(bullets) + "\n"

def main():
    data = json.load(sys.stdin)
    releases = data.get("releases", [])
    out = []
    for rel in releases:
        out.append(summarize_release(rel))
    print("\n".join(out).strip())

if __name__ == "__main__":
    main()
