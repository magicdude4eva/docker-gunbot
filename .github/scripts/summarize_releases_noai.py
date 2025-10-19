#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
summarize_releases_noai.py

Read releases.json from stdin (produced by fetch_telegram_releases.py)
and print human-readable Markdown summaries.

- Preserves emojis (no ASCII stripping).
- Handles forwarded messages with a title + bullets.
- Applies committer attribution (from forwards or '@user commits:' markers).
- Splits multiline detail blocks into individual items.
- Classifies each item into simple buckets for grouping.

Usage:
  python .github/scripts/summarize_releases_noai.py < releases.json
"""

from __future__ import annotations

import json
import re
import sys
from typing import Dict, Iterable, List, Optional, Tuple

# ---------- classification helpers ----------

RE_FIX       = re.compile(r"\b(fix|fixed|bug|issue|patch|resolve[sd]?)\b", re.I)
RE_ADD       = re.compile(r"\b(add|added|introduc(e|ed)|enable[sd]?|new)\b", re.I)
RE_CHANGE    = re.compile(r"\b(change[sd]?|tweak[sd]?|adjust(ed)?|update[sd]?|upgrade[sd]?)\b", re.I)
RE_IMPROVE   = re.compile(r"\b(improv(e|ed|ement)|optimis(e|ed|ation)|optimiz(e|ed|ation)|performance)\b", re.I)
RE_SECURITY  = re.compile(r"\b(security|vuln|cve)\b", re.I)
RE_GUI       = re.compile(r"\b(gui|dashboard|chart|table|pagination|tabs?)\b", re.I)
RE_EXCHANGE  = re.compile(r"\b(binance|kraken|mexc|bitget|hyperliquid|orderbook|endpoint|pairs?)\b", re.I)
RE_STRATEGY  = re.compile(r"\b(athena|wick\s*magic|ghostrider|candle\s+analysis|quanta)\b", re.I)

BULLET_PREFIX_RE = re.compile(r"^\s*[-•–]\s*")
SECTION_HEAD_RE = re.compile(
    r"^\s*(changes\s+in\s+behavio[u]r|enhancements?|bug\s*fixes?)\s*:?$", re.I
)

def classify(text: str) -> str:
    t = text.lower()
    if RE_SECURITY.search(t):  return "Security"
    if RE_FIX.search(t):       return "Fixes"
    if RE_IMPROVE.search(t):   return "Improved"
    if RE_ADD.search(t):       return "Added"
    if RE_CHANGE.search(t):    return "Changed"
    if RE_GUI.search(t):       return "GUI"
    if RE_EXCHANGE.search(t):  return "Exchange"
    if RE_STRATEGY.search(t):  return "Strategy"
    return "Other"

def clean_bullet(line: str) -> str:
    # strip a single leading bullet marker if present
    return BULLET_PREFIX_RE.sub("", line).strip()

def split_detail_block(text: str) -> Tuple[Optional[str], List[str]]:
    """
    Split a post 'text' into (optional title, [items]).
    - For forwarded posts, the first non-empty line is the title.
    - Keep section blocks (Bug Fixes:, Enhancements:, etc.) as context bullets.
    - Return individual change items (one per bullet/line).
    """
    if not text:
        return None, []

    lines = [ln.rstrip() for ln in text.splitlines()]
    non_empty = [ln for ln in lines if ln.strip()]
    title: Optional[str] = None
    items: List[str] = []

    # Consider the first non-empty, non-section line without a leading bullet as a title
    if non_empty:
        first = non_empty[0].strip()
        if not BULLET_PREFIX_RE.match(first):
            title = first

    in_section = False
    last_section = None

    for raw in lines:
        l = raw.strip()
        if not l:
            in_section = False
            continue

        # section headers appear as plain lines
        if SECTION_HEAD_RE.match(l):
            in_section = True
            last_section = clean_bullet(l.rstrip(":"))
            # add a context marker as a pseudo-bullet to keep section grouping visible
            items.append(f"{last_section}:")
            continue

        # treat everything else as a bulletish item
        text_item = clean_bullet(l)

        # avoid duplicating the title if it reappears as a bullet
        if title and text_item == title:
            continue

        items.append(text_item)

    # final pass: remove duplicates while preserving order
    seen = set()
    deduped: List[str] = []
    for it in items:
        key = it.strip().lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(it.strip())

    # remove empty artifacts
    deduped = [x for x in deduped if x]

    return title, deduped

# ---------- rendering ----------

def render_release_md(rel: Dict) -> str:
    version = rel.get("version", "Unknown")
    date    = rel.get("anchor_time", "")
    posts   = rel.get("posts", [])

    # collect download text (first download)
    download_text = ""
    for p in posts:
        if p.get("type") == "download":
            download_text = p.get("text", "")
            break

    # normalize into items with category + committer
    buckets: Dict[str, List[str]] = {
        "Security": [], "Fixes": [], "Improved": [], "Added": [],
        "Changed": [], "GUI": [], "Exchange": [], "Strategy": [], "Other": []
    }

    for p in posts:
        if p.get("type") not in ("detail",):
            continue

        forwarded = bool(p.get("forwarded"))
        committer = p.get("committer")
        title, parts = split_detail_block(p.get("text", ""))

        # prepend title as context for forwarded posts if it looks meaningful
        context = []
        if forwarded and title:
            context.append(f"*{title}*")

        # Each line becomes an item
        for part in parts:
            if not part:
                continue
            # skip pure context markers like "Bug Fixes:" if they slipped through
            if SECTION_HEAD_RE.match(part):
                continue

            item_text = " - ".join(context + [part]) if context else part
            cat = classify(item_text)
            suffix = f"  _(by {committer})_" if committer else ""
            buckets[cat].append(f"- {item_text}{suffix}")

    # build markdown
    out: List[str] = []
    out.append(f"## Gunbot {version}")
    if date:
        out.append(f"_Released: {date}_")
    out.append("")

    # print non-empty buckets in a friendly order
    order = ["Security", "Fixes", "Improved", "Added", "Changed", "GUI", "Exchange", "Strategy", "Other"]
    for k in order:
        if buckets[k]:
            out.append(f"#### {k}")
            out.extend(buckets[k])
            out.append("")

    if download_text:
        # skip boilerplate “files are now available …” messages
        if not re.search(r"files\s+are\s+now\s+available", download_text, re.I):
            out.append(f"**Download:** {download_text}")
            out.append("")

    out.append("\n---\n")
    return "\n".join(out).rstrip() + "\n"

def main() -> None:
    data = json.load(sys.stdin)
    releases = data.get("releases", [])
    if not releases:
        print("No releases found.", file=sys.stderr)
        return

    # Newest first is fine as-is; if desired, reverse to oldest-first:
    # releases = list(reversed(releases))

    chunks = [render_release_md(r) for r in releases]
    sys.stdout.write("\n".join(chunks))

if __name__ == "__main__":
    main()
