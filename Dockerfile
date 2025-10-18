# ---------------------------------------------------------------------------
#  Gunbot Docker Image (Colorised Edition)
#  Maintainer: https://github.com/magicdude4eva/docker-gunbot
#
#  Description:
#    Builds a minimal Debian-based Gunbot container with colorised terminal
#    output and sane defaults. Uses Bitnami's Minideb base for small footprint
#    and GlibC compatibility.
#
#  Features:
#    - Installs Gunthy binary from official source (https://gunthy.org)
#    - Supports persistent data in /data (mounted via volume)
#    - Adds color-friendly TERM and NPM config for better console readability
#    - Uses gosu for clean user privilege handling
#
#  Build Example:
#    docker build -t magicdude4eva/gunbot-colorised:latest .
#
#  Run Example:
#    docker run -d --name gunbot -v $(pwd)/data:/data -p 5555:5000 magicdude4eva/gunbot-colorised
#
# ---------------------------------------------------------------------------

 # ========== builder ==========
FROM debian:bookworm-slim AS builder

ARG DEBIAN_FRONTEND=noninteractive
ARG INSTALL_URL="https://gunthy.org/downloads/gunthy_linux.zip"
ARG CACHEBUST=1

RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl libarchive-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/gunthy

# Stream-extract to avoid keeping a large .zip layer
RUN echo "cb=${CACHEBUST}" >/dev/null \
 && curl -fsSL "${INSTALL_URL}?cb=${CACHEBUST}" | bsdtar -x -f - \
 && chmod 0555 /tmp/gunthy/gunthy-linux  

# prune non-linux native bindings
RUN find /tmp/gunthy -type f -name "index_osx.node" -delete \
 && find /tmp/gunthy -type f -name "index_win.node" -delete \
 && find /tmp/gunthy -type f -name "*.map" -delete \
 && rm -rf /tmp/gunthy/node_modules/@neon-exchange/nash-protocol-gunbot/docs || true \
 && rm -f /tmp/gunthy/node_modules/technicalindicators/dist/browser*.js \
          /tmp/gunthy/node_modules/technicalindicators/dist/*.map \
          /tmp/gunthy/node_modules/technicalindicators/images/* || true;

# ========== final ==========
FROM debian:bookworm-slim

ARG DEBIAN_FRONTEND=noninteractive
LABEL org.label-schema.vcs-url="https://github.com/magicdude4eva/docker-gunbot" \
      description="Gunbot Docker (Colorised Edition)"

ENV TZ=Europe/Vienna \
    TERM=xterm-256color \
    FORCE_COLOR=true \
    NPM_CONFIG_COLOR=always \
    GUNTHY_HOME=/opt/gunthy \
    GUNTHY_DATA=/data

# minimal runtime deps
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates gosu tzdata bash fontconfig fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# runtime user before COPY so --chown works
RUN useradd -r -m -d /home/gunthy -s /usr/sbin/nologin gunthy

# copy only what we need, with ownership set at copy time
COPY --from=builder --chown=gunthy:gunthy /tmp/gunthy/ ${GUNTHY_HOME}/

# entrypoint
COPY --chown=root:root docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 0555 /docker-entrypoint.sh

EXPOSE 3000 3001 5000 5001
WORKDIR ${GUNTHY_DATA}
VOLUME ["${GUNTHY_DATA}"]
ENTRYPOINT ["/docker-entrypoint.sh"]
