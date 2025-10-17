#!/usr/bin/env bash
set -euo pipefail

# ---------------------------------------------------------------------------
#  Gunbot Docker Quick Setup
#  Repo: https://github.com/magicdude4eva/docker-gunbot (branch: main)
#
#  Usage (one-liner):
#    curl -fsSL -H 'Cache-Control: no-cache' \
#      -o setup.sh https://raw.githubusercontent.com/magicdude4eva/docker-gunbot/refs/heads/main/setup.sh \
#      && bash setup.sh
#
# ---------------------------------------------------------------------------

# --- Banner ---------------------------------------------------------------
clear
cat <<'EOF'
───────────────────────────────────────────────
        _____             _           _   
       / ____|           | |         | |  
      | |  __ _   _ _ __ | |__   ___ | |_ 
      | | |_ | | | | '_ \| '_ \ / _ \| __|
      | |__| | |_| | | | | |_) | (_) | |_ 
       \_____|\__,_|_| |_|_.__/ \___/ \__|                                                                                                               
───────────────────────────────────────────────
  Gunbot Docker Setup Script by magicdude4eva
───────────────────────────────────────────────
EOF
echo

# --- Constants ------------------------------------------------------------
ZIP_URL="https://codeload.github.com/magicdude4eva/docker-gunbot/zip/refs/heads/main"

log()  { echo "[$(date +'%H:%M:%S')] $*"; }
fail() { echo "[x] $*" >&2; exit 1; }

# --- Pre-flight checks ----------------------------------------------------
command -v docker >/dev/null 2>&1 || fail "Docker is required but not installed."

if docker compose version >/dev/null 2>&1; then
  COMPOSE_CMD=(docker compose)
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE_CMD=(docker-compose)
else
  fail "Neither 'docker compose' nor 'docker-compose' found."
fi

# --- Ask for install directory -------------------------------------------
echo "Where should Gunbot be installed?"
echo "  1) Current directory: $(pwd)"
echo "  2) Create and use ./gunbot (recommended)"
read -r -p "Enter 1 or 2 [default: 2]: " CHOICE
CHOICE="${CHOICE:-2}"

case "$CHOICE" in
  1) TARGET_DIR="$(pwd)";;
  2) TARGET_DIR="$(pwd)/gunbot"; mkdir -p "$TARGET_DIR";;
  *) echo "Invalid choice. Using option 2 -> ./gunbot."; TARGET_DIR="$(pwd)/gunbot"; mkdir -p "$TARGET_DIR";;
esac

log "→ Installing into: $TARGET_DIR"

# --- Download and extract -------------------------------------------------
TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

command -v unzip >/dev/null 2>&1 || fail "unzip is required."
curl -fsSL "$ZIP_URL" -o "$TMPDIR/repo.zip"
unzip -q "$TMPDIR/repo.zip" -d "$TMPDIR"

# The extracted folder is always named docker-gunbot-main
ROOT="${TMPDIR}/docker-gunbot-main"
[[ -d "$ROOT" ]] || fail "Unexpected ZIP structure."

cp -a "${ROOT}/binance_data" "$TARGET_DIR/"
cp -a "${ROOT}/docker-compose.yml" "$TARGET_DIR/"

# --- Start Docker stack ---------------------------------------------------
log "Starting containers with ${COMPOSE_CMD[*]} up -d"
pushd "$TARGET_DIR" >/dev/null
"${COMPOSE_CMD[@]}" up -d
popd >/dev/null

echo
log "✅ Setup complete!"
log "Compose file: ${TARGET_DIR}/docker-compose.yml"
log "Data dir    : ${TARGET_DIR}/binance_data"
echo "───────────────────────────────────────────────"
echo "You can manage containers with:"
echo "  cd ${TARGET_DIR}"
echo "  ${COMPOSE_CMD[*]} ps"
echo
echo "🌐 Gunbot Web UI is available at:"
echo "   👉 http://localhost:5555/"
echo "───────────────────────────────────────────────"