#!/usr/bin/env python3
"""
Deterministic release summary from fetch_telegram_releases.py JSON.

- For each release.version, create a "### vX.Y.Z" section.
- Keep lines that look like bullets or contain fix/add/change/update/improve/feature/support.
- De-duplicate bullets, cap at ~12 lines per version.
- Print Markdown to stdout.
"""
import sys, json, re

data = json.load(sys.stdin)
releases = data.get("releases", [])
if not releases:
    print("NO-NEW-RELEASES")
    sys.exit(0)

# Simple heuristics: keep “- …” lines, lines with fix/add/change/update/feature,
# collapse whitespace, and ignore obvious noise.
KEEP_RE = re.compile(r"(^\s*[-•–]\s+)|\b(fix|fixed|add|added|change|changed|update|updated|improve|improved|feature|support)\b", re.I)

def clean(line: str) -> str:
    line = re.sub(r"\s+", " ", line).strip()
    return line

out = []
for rel in releases:
    out.append(f"### {rel['version']}")
    bullets = []
    for p in rel["posts"]:
        if p["type"] == "anchor" or p["type"] == "download":
            continue
        for raw_line in p["text"].splitlines():
            line = clean(raw_line)
            if not line: 
                continue
            if KEEP_RE.search(line):
                # Normalize to a single dash bullet
                if not line.startswith("- "):
                    line = "- " + line.lstrip("-•– ")
                bullets.append(line)
    # de-dup while keeping order
    seen = set()
    deduped = []
    for b in bullets:
        if b.lower() in seen: 
            continue
        seen.add(b.lower())
        deduped.append(b)
    # cap to a reasonable count
    deduped = deduped[:12] or ["- (no granular changes posted)"]
    out.extend(deduped)
    out.append("")  # blank line between versions

print("\n".join(out).rstrip())
