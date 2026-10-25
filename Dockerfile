# -----------------------------------------------------------------------------
#  Gunbot Docker Image (Colorised Edition)
#  Maintainer: https://github.com/magicdude4eva/docker-gunbot
#
#  Description:
#   Minimal Debian-based Gunbot container with colourised terminal output,
#   sane defaults, and Synology-friendly permissions. Uses multi-stage
#   build to avoid shipping the archive and extra tooling.
#
#  Features:
#   - Fetches official Gunthy bundle and prunes non-Linux/dev artefacts
#   - Read-only app payload in /opt/gunthy, persistent runtime data in /data
#   - Non-root user by default; gosu for UID/GID handoff as needed
#   - Clean apt layers; no upgrade; zip streamed/extracted in builder
#
# -----------------------------------------------------------------------------

# ---- builder: fetch & unpack vendor bundle ----------------------------------
FROM debian:bookworm-slim AS builder

ARG DEBIAN_FRONTEND=noninteractive
# Must match the source of the version in checksums.json used by CI
# (the :3009/beta mirror lags behind and serves older builds)
ARG INSTALL_URL="https://gunthy.org/downloads/gunthy-linux-x64.zip"
# Optional: expected sha256 of the zip (from checksums.json); verified when set
ARG INSTALL_SHA256=""
ARG CACHEBUST=1
ARG TARGETPLATFORM
ARG TARGETARCH

# Tools only for build stage
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl libarchive-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/gunthy

# Download, verify (if checksum given), extract, drop the zip
RUN echo "cb=${CACHEBUST}" >/dev/null \
 && curl -fsSL -o /tmp/gunthy.zip "${INSTALL_URL}?cb=${CACHEBUST}" \
 && if [ -n "${INSTALL_SHA256}" ]; then echo "${INSTALL_SHA256}  /tmp/gunthy.zip" | sha256sum -c -; fi \
 && bsdtar -x -f /tmp/gunthy.zip \
 && rm -f /tmp/gunthy.zip \
 && chmod 0555 /tmp/gunthy/gunthy-linux

# Conservative pruning (keeps runtime intact)
RUN find /tmp/gunthy -type f -name "index_osx.node" -delete \
 && find /tmp/gunthy -type f -name "index_win.node" -delete \
 && find /tmp/gunthy -type f -name "*.map" -delete \
 && rm -rf /tmp/gunthy/node_modules/@neon-exchange/nash-protocol-gunbot/docs || true \
 && rm -f /tmp/gunthy/node_modules/technicalindicators/dist/browser*.js \
          /tmp/gunthy/node_modules/technicalindicators/dist/*.map \
          /tmp/gunthy/node_modules/technicalindicators/images/* || true

# ---- final: runtime only ----------------------------------------------------
FROM debian:bookworm-slim

# ----- OCI labels (populate via --build-arg) ---------------------------------
LABEL org.opencontainers.image.title="Gunbot (Colorised)" \
      org.opencontainers.image.description="Debian-based Gunbot with colourised console, slim layers, and Synology-friendly defaults." \
      org.opencontainers.image.url="https://hub.docker.com/r/magicdude4eva/gunbot-colorised" \
      org.opencontainers.image.source="https://github.com/magicdude4eva/docker-gunbot" \
      org.opencontainers.image.documentation="https://github.com/magicdude4eva/docker-gunbot" \
      maintainer="Gerd Naschenweng <https://github.com/magicdude4eva>"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Vienna \
    TERM=xterm-256color \
    FORCE_COLOR=true \
    NPM_CONFIG_COLOR=always \
    GUNTHY_HOME=/opt/gunthy \
    GUNTHY_DATA=/data

# Minimal runtime deps (no apt upgrade)
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates gosu tzdata bash fontconfig fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Non-root runtime user
RUN useradd -r -m -d /home/gunthy -s /usr/sbin/nologin gunthy

# App payload (ownership at copy time; no recursive chown layer)
COPY --from=builder --chown=gunthy:gunthy /tmp/gunthy/ ${GUNTHY_HOME}/

# Entrypoint (idempotent, keeps /data chown fast on Synology)
COPY --chown=root:root docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 0555 /docker-entrypoint.sh

# Ports exposed by Gunbot (API/UI etc.)
EXPOSE 3000 3001 5000 5001

# Persistent data volume (configs, logs, runtime artefacts)
WORKDIR ${GUNTHY_DATA}
VOLUME ["${GUNTHY_DATA}"]

ENTRYPOINT ["/docker-entrypoint.sh"]
