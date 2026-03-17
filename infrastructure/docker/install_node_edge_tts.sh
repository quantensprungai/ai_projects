#!/bin/bash
# node-edge-tts in Clawdbot's node_modules installieren.
# Clawdbot sucht es dort – npx-Cache reicht nicht.
# Auf VM102 ausführen.
set -e
CLAWDBOT_DIR="${HOME}/.clawdbot/lib/node_modules/clawdbot"
if [ ! -d "$CLAWDBOT_DIR" ]; then
  echo "Clawdbot nicht gefunden: $CLAWDBOT_DIR"
  exit 1
fi
cd "$CLAWDBOT_DIR"
echo "Installiere node-edge-tts in $CLAWDBOT_DIR ..."
npm install node-edge-tts
if [ -d "node_modules/node-edge-tts" ]; then
  echo "OK. Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service"
else
  echo "Installation fehlgeschlagen."
  exit 1
fi
