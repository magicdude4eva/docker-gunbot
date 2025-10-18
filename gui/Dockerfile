# ---- builder (download + unpack) ----
FROM debian:bookworm-slim AS builder

ARG DEBIAN_FRONTEND=noninteractive
ARG GUI_INSTALL_URL="https://gunthy.org/downloads/beta/gui-linux.zip"
ARG CACHEBUST=1

RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl libarchive-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp/gui
# stream-extract, avoid storing zip
RUN echo "cb=${CACHEBUST}" >/dev/null \
 && curl -fsSL "${GUI_INSTALL_URL}?cb=${CACHEBUST}" | bsdtar -x -f -

# Ensure binary is executable
RUN chmod 0555 /tmp/gui/gui-linux

# ---- final (runtime only) ----
FROM debian:bookworm-slim

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Vienna \
    TERM=xterm-256color \
    NPM_CONFIG_COLOR=always \
    MOCHA_COLORS=true \
    FORCE_COLOR=true \
    GUI_HOME=/gunbot-gui

# runtime deps only; skip upgrade, skip apt-utils
# fonts: start with core; add -extra later only if you truly need more glyphs
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates \
      fontconfig fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# non-root user for Synology friendliness
RUN useradd -r -m -d /home/gunthy -s /usr/sbin/nologin gunthy

WORKDIR ${GUI_HOME}
COPY --from=builder --chown=gunthy:gunthy /tmp/gui/ ${GUI_HOME}/

# Make sure the binary has exec bit (belt-and-suspenders)
RUN chmod 0555 ${GUI_HOME}/gui-linux

# Expose as before
EXPOSE 5001

VOLUME [ "/gunbot/config.js" ]

USER gunthy
CMD ["/gunbot-gui/gui-linux"]
