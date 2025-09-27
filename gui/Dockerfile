FROM bitnami/minideb:latest

ARG GUI_INSTALL_URL="https://gunthy.org/downloads/beta/gui-linux.zip"
ARG DEBIAN_FRONTEND=noninteractive
ARG VCS_REF
ARG TARGETARCH=amd64
ARG CACHEBUST=1

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/magicdude4eva/docker-gunbot" \
      description="Gunbot GUI Docker Image using minimal GlibC image"

## Setup Environment
ENV TZ=Europe/Vienna \
  TERM=xterm-256color \
  NPM_CONFIG_COLOR=always \
  GUI_INSTALL_URL=${GUI_INSTALL_URL} \
  MOCHA_COLORS=true \
  FORCE_COLOR=true

# Use bash with strict mode for RUN lines
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Base packages
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends \
        apt-utils unzip curl fontconfig fonts-dejavu-extra ca-certificates && \
    apt-get -y upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates --fresh && \
    fc-cache -fv

WORKDIR /tmp

# Download & extract — tie cache to CACHEBUST so this layer is rebuilt when you change it
# Adding a dummy query '?cb=' is enough to change the command hash; server will ignore it.
RUN echo "CACHEBUST=${CACHEBUST}" >/dev/null && \
    curl -fsSL --retry 3 --retry-delay 2 \
      -H "Cache-Control: no-cache" \
      -o gui.zip "${GUI_INSTALL_URL}?cb=${CACHEBUST}" && \
    unzip -q gui.zip -d /gunbot-gui && \
    rm -f gui.zip

# Make executable
RUN chmod +x /gunbot-gui/gui-linux

WORKDIR /gunbot-gui
EXPOSE 5001

## Mount shared volume for bot data
VOLUME [ "/gunbot/config.js" ]

CMD ["/gunbot-gui/gui-linux"]
