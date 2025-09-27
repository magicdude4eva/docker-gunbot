FROM bitnami/minideb:latest

ARG INSTALL_URL="https://gunthy.org/downloads/gunthy_linux.zip"
ARG DEBIAN_FRONTEND=noninteractive
ARG VCS_REF
ARG TARGETARCH=amd64
ARG CACHEBUST=1

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/magicdude4eva/docker-gunbot" \
      description="Gunbot Docker Image Using minimal GlibC image with colorised output"

## Setup Environment
ENV TZ=Europe/Vienna \
  TERM=xterm-256color \
  FORCE_COLOR=true \
  NPM_CONFIG_COLOR=always \
  MOCHA_COLORS=true \
  INSTALL_URL=${INSTALL_URL} \
  GUNTHY_HOME=/opt/gunthy \
  GUNTHY_DATA=/data

# Safer RUN defaults
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Base deps
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get -y update && \
    apt-get -y install --no-install-recommends \
        apt-utils unzip curl wget fontconfig fonts-dejavu-extra ca-certificates && \
    apt-get -y upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates --fresh && \
    fc-cache -fv

# Create app dirs + user
RUN mkdir -p "${GUNTHY_HOME}" "${GUNTHY_DATA}" && \
    useradd -r -s /bin/false -d "${GUNTHY_HOME}" gunthy && \
    chown -R gunthy:gunthy "${GUNTHY_HOME}" "${GUNTHY_DATA}"

# Download and install Gunthy (cache-busted)
WORKDIR ${GUNTHY_HOME}
RUN echo "CACHEBUST=${CACHEBUST}" >/dev/null && \
    echo "Downloading latest Gunbot..." && \
    curl -fsSL --retry 3 --retry-delay 2 -o /tmp/gunthy_linux.zip \
      "${INSTALL_URL}?cb=${CACHEBUST}" && \
    unzip -q /tmp/gunthy_linux.zip && \
    chmod +x gunthy-linux && \
    rm -rf /tmp/gunthy_linux.zip config.js tgconfig.json autoconfig.json .DS_Store && \
    ls -la .

# Ensure ownership
RUN chown -R gunthy:gunthy "${GUNTHY_HOME}" "${GUNTHY_DATA}"

# Install gosu for proper user switching (quick sanity check)
RUN ARCH="$(dpkg --print-architecture)" && \
    wget -qO /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.17/gosu-${ARCH}" && \
    chmod +x /usr/local/bin/gosu && \
    gosu nobody true

# Entrypoint
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh && chown gunthy:gunthy /docker-entrypoint.sh

# Expose ports
EXPOSE 3000 3001 5000 5001

# Set working directory
WORKDIR ${GUNTHY_DATA}

# Volumes for persistent data
VOLUME ["${GUNTHY_DATA}"]

# Set entrypoint
ENTRYPOINT ["/docker-entrypoint.sh"] 
