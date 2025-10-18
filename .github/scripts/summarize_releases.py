#!/usr/bin/env python3
import os, sys, json, requests

data = json.load(sys.stdin)  # {"releases":[...]}
releases = data.get("releases", [])
if not releases:
    print("NO-NEW-RELEASES")
    sys.exit(0)

def format_prompt(releases):
    blocks = []
    for rel in releases:
        lines = [f"## {rel['version']}"]
        for p in rel["posts"]:
            lines.append(p["text"])
        blocks.append("\n".join(lines))
    joined = "\n\n---\n\n".join(blocks)
    return f"""
You are a release-notes editor. From the Telegram posts grouped by version below, extract concise, actionable changelogs.

Rules:
- Output Markdown only.
- One section per version: '### vX.Y.Z'.
- 5-12 short bullets per version.
- Imperative style (Fix:, Add:, Change:).
- Keep strategy names (Athena, GhostRider, etc.). Skip community/reseller chatter.

Source posts:
{joined}
"""

prompt = format_prompt(releases)

resp = requests.post(
    "https://models.inference.ai.azure.com/v1/responses",
    headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Content-Type": "application/json"
    },
    json={"model":"gpt-4o-mini", "input":[{"role":"user","content":prompt}]}
)
resp.raise_for_status()
print(resp.json()["output_text"])
