# -----------------------------------------------------------------------------
# Gunbot GUI Docker Image
# Maintainer: https://github.com/magicdude4eva/docker-gunbot
#
# Description:
#   Minimal Debian-based image for the Gunbot GUI. Uses a multi-stage build to
#   stream-extract the official GUI bundle, keeps runtime deps tiny, and runs
#   as a non-root user. Synology-friendly (no recursive chown on start).
#
# Features:
#   - Fetches GUI bundle from gunthy.org (no .zip kept in layers)
#   - Read-only app in /gunbot-gui, mounts config dir at /gunbot
#   - Small font stack (fontconfig + DejaVu core) for UI text/charts
#   - Clean apt layers; no apt-get upgrade; no recursive chmod/chown
#
# -----------------------------------------------------------------------------

# ---- builder: fetch & unpack GUI bundle -------------------------------------
FROM debian:bookworm-slim AS builder

ARG DEBIAN_FRONTEND=noninteractive
ARG GUI_INSTALL_URL="https://gunthy.org/downloads/beta/gui-linux.zip"
ARG CACHEBUST=1
ARG TARGETPLATFORM
ARG TARGETARCH

RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl libarchive-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/gui

# Stream-extract (avoid keeping the .zip in an image layer)
RUN echo "cb=${CACHEBUST}" >/dev/null \
 && curl -fsSL "${GUI_INSTALL_URL}?cb=${CACHEBUST}" | bsdtar -x -f - \
 && chmod 0555 /tmp/gui/gui-linux

# ---- final: runtime only -----------------------------------------------------
FROM debian:bookworm-slim

# ----- OCI labels (filled by build args) -------------------------------------
LABEL org.opencontainers.image.title="Gunbot GUI" \
      org.opencontainers.image.description="Debian-based Gunbot GUI with slim layers and Synology-friendly defaults." \
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

WORKDIR ${GUI_HOME}
COPY --from=builder --chown=gunthy:gunthy --chmod=0555 /tmp/gui/gui-linux ${GUI_HOME}/gui-linux

# Expose as before
EXPOSE 5001

VOLUME [ "/gunbot/config.js" ]

USER gunthy
CMD ["/gunbot-gui/gui-linux"]
