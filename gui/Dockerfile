# -----------------------------------------------------------------------------
# Gunbot GUI Docker Image
# Maintainer: https://github.com/magicdude4eva/docker-gunbot
#
# Description:
#   Minimal Debian-based image for the Gunbot GUI. Uses a multi-stage build to
#   fetch and verify the official GUI bundle, keeps runtime deps tiny, and runs
#   as a non-root user. Synology-friendly (no recursive chown on start).
#
# Features:
#   - Fetches GUI bundle from gunthy.org (no .zip kept in layers)
#   - Optional sha256 verification of the bundle (INSTALL_SHA256)
#   - Read-only app in /gunbot-gui, config file mounted at /gunbot-gui/config.json
#   - Small font stack (fontconfig + DejaVu core) for UI text/charts
#   - Clean apt layers; no apt-get upgrade; no recursive chmod/chown
#
# Runtime config:
#   The GUI is an Express server that reads ./config.json (relative to
#   /gunbot-gui) and listens on config.port (default 3000). The browser talks
#   to the Gunbot core directly via api_url. Bind-mount a file such as:
#
#     { "api_url": "https://<core-host>", "port": 3000 }
#
#   docker run -p 3000:3000 \
#     -v /path/to/config.json:/gunbot-gui/config.json:ro magicdude4eva/gunbot-gui
#
# -----------------------------------------------------------------------------

# ---- builder: fetch & unpack GUI bundle -------------------------------------
FROM debian:bookworm-slim AS builder

ARG DEBIAN_FRONTEND=noninteractive
ARG GUI_INSTALL_URL="https://gunthy.org:3009/beta/gui-linux.zip"
# Optional: expected sha256 of the zip (pinned by CI); verified when set
ARG INSTALL_SHA256=""
ARG CACHEBUST=1
ARG TARGETPLATFORM
ARG TARGETARCH

RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl libarchive-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/gui

# Download, verify (if checksum given), extract only the binary, drop the zip
RUN echo "cb=${CACHEBUST}" >/dev/null \
 && curl -fsSL -o /tmp/gui.zip "${GUI_INSTALL_URL}?cb=${CACHEBUST}" \
 && if [ -n "${INSTALL_SHA256}" ]; then echo "${INSTALL_SHA256}  /tmp/gui.zip" | sha256sum -c -; fi \
 && bsdtar -x -f /tmp/gui.zip gui-linux \
 && rm -f /tmp/gui.zip \
 && chmod 0555 /tmp/gui/gui-linux

# ---- final: runtime only -----------------------------------------------------
FROM debian:bookworm-slim

ARG GUI_VERSION=""

# ----- OCI labels (filled by build args) -------------------------------------
LABEL org.opencontainers.image.title="Gunbot GUI" \
      org.opencontainers.image.description="Debian-based Gunbot GUI with slim layers and Synology-friendly defaults." \
      org.opencontainers.image.version="${GUI_VERSION}" \
      org.opencontainers.image.url="https://hub.docker.com/r/magicdude4eva/gunbot-gui" \
      org.opencontainers.image.source="https://github.com/magicdude4eva/docker-gunbot" \
      org.opencontainers.image.documentation="https://github.com/magicdude4eva/docker-gunbot" \
      maintainer="Gerd Naschenweng <https://github.com/magicdude4eva>"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Vienna \
    TERM=xterm-256color \
    NPM_CONFIG_COLOR=always \
    MOCHA_COLORS=true \
    FORCE_COLOR=true \
    GUI_HOME=/gunbot-gui

# Minimal runtime deps (fonts for UI; no apt upgrade)
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates fontconfig fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Non-root runtime user
RUN useradd -r -m -d /home/gunthy -s /usr/sbin/nologin gunthy

# App reads ./config.json, so the working dir must stay /gunbot-gui
WORKDIR ${GUI_HOME}
COPY --from=builder --chown=gunthy:gunthy --chmod=0555 /tmp/gui/gui-linux ${GUI_HOME}/gui-linux

# GUI server port (config.port, default 3000)
EXPOSE 3000

USER gunthy
CMD ["/gunbot-gui/gui-linux"]
