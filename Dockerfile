FROM bitnami/minideb:stretch

#ARG INSTALL_URL="https://github.com/GuntharDeNiro/BTCT/releases/download/2046/lin.zip"
ARG INSTALL_URL="https://github.com/GuntharDeNiro/BTCT/releases/download/2100/lin_v14.zip"

ENV TZ=Europe/Vienna \
  TERM=xterm-256color \
  FORCE_COLOR=true \
  NPM_CONFIG_COLOR=always \
  MOCHA_COLORS=true \
  INSTALL_URL=${INSTALL_URL}

RUN apt-get -y update && \
 apt-get -y upgrade && \
 apt-get install -y unzip curl fontconfig && \
 apt-get clean -y && \
 apt-get autoclean -y && \
 apt-get autoremove -y

WORKDIR /tmp
RUN curl -Lo /tmp/lin.zip ${INSTALL_URL}

RUN unzip -q lin.zip \
 && rm -rf lin.zip \
 && rm -rf __MACOSX \
 && mv lin* /gunbot \
 && rm -f /gunbot/config.js \
 && rm -f /gunbot/tgconfig.json \
 && rm -f /gunbot/autoconfig.json \
 && chmod +x /gunbot/gunthy-linux

WORKDIR /gunbot

EXPOSE 5000
VOLUME [ "/gunbot/backups", "/gunbot/logs", "/gunbot/json", "/gunbot/config.js", "/gunbot/gunbotgui.db"]

CMD /gunbot/gunthy-linux
