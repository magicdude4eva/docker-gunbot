#!/bin/bash
set -e

# Paths
: "${GUNTHY_HOME:=/opt/gunthy}"
: "${GUNTHY_DATA:=/data}"

# Ensure required dirs exist in /data
mkdir -p "${GUNTHY_DATA}/backtesting" \
         "${GUNTHY_DATA}/backups" \
         "${GUNTHY_DATA}/customStrategies" \
         "${GUNTHY_DATA}/gunbot_logs" \
         "${GUNTHY_DATA}/json" \
         "${GUNTHY_DATA}/logs"

# Ensure a real config.js file lives in /data (no symlink)
if [ ! -f "${GUNTHY_DATA}/config.js" ]; then
  # seed from image example if present, else empty object
  if [ -f "${GUNTHY_HOME}/config-js-example.txt" ]; then
    cp -f "${GUNTHY_HOME}/config-js-example.txt" "${GUNTHY_DATA}/config.js"
  else
    echo '{}' > "${GUNTHY_DATA}/config.js"
  fi
fi

# Symlink read-only runtime assets into /data so the binary can resolve them relative to CWD.
# Newer Gunbot bundles ship only the binary, so link assets the image actually has and
# drop dangling links left behind by older images.
cd "${GUNTHY_DATA}"
for asset in cs tulind node_modules server.cert server.key; do
  if [ -e "${GUNTHY_HOME}/${asset}" ]; then
    [ -L "${asset}" ] || ln -s "${GUNTHY_HOME}/${asset}" "${asset}"
  elif [ -L "${asset}" ] && [ ! -e "${asset}" ]; then
    rm -f "${asset}"
  fi
done

# Gunbot writes into cs/ (e.g. cs/tables), so it must be a writable dir when not linked
if [ ! -e cs ]; then
  mkdir -p cs
  chown gunthy:gunthy cs || true
fi

# Make sure /data is writable by the runtime user
if [ ! -f "${GUNTHY_DATA}/.owned_by_gunthy" ]; then
  chown -R gunthy:gunthy "${GUNTHY_DATA}" || true
  touch "${GUNTHY_DATA}/.owned_by_gunthy"
fi

# Run Gunbot with CWD=/data so all relative writes (config.js etc.) happen inside /data
echo "Starting Gunbot with CWD=${GUNTHY_DATA} ..."
cd "${GUNTHY_DATA}"
exec gosu gunthy /opt/gunthy/gunthy-linux "$@"
