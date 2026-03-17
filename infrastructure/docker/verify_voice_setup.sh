#!/bin/bash
# Voice-Setup (STT + TTS) auf VM102 prüfen – auf VM102 ausführen
# ssh user@docker-apps
# bash /tmp/verify_voice_setup.sh

echo "=== 1. System-Abhängigkeiten ==="
echo -n "ffmpeg: "; which ffmpeg && ffmpeg -version 2>/dev/null | head -1 || echo "FEHLT"
echo -n "whisper: "; (which whisper || test -f ~/.local/bin/whisper) && echo "OK" || echo "FEHLT"
echo -n "node: "; node -v 2>/dev/null || echo "FEHLT"
echo -n "node-edge-tts: "; npm list -g node-edge-tts 2>/dev/null | head -1 || echo "nicht global; prüfe npx"; npx node-edge-tts --help 2>/dev/null | head -1 || echo "FEHLT"

echo ""
echo "=== 2. Config (clawdbot.json) ==="
CONFIG=~/.clawdbot-personal/clawdbot.json
if [ -f "$CONFIG" ]; then
  echo "messages.tts.auto: $(jq -r '.messages.tts.auto // "nicht gesetzt"' $CONFIG)"
  echo "messages.tts.provider: $(jq -r '.messages.tts.provider // "nicht gesetzt"' $CONFIG)"
  echo "tools.deny: $(jq -r '.tools.deny // "[]"' $CONFIG)"
  echo "tools.media.audio.enabled: $(jq -r '.tools.media.audio.enabled // "nicht gesetzt"' $CONFIG)"
else
  echo "Config nicht gefunden: $CONFIG"
fi

echo ""
echo "=== 3. TTS-Prefs ==="
PREFS=~/.clawdbot-personal/settings/tts.json
if [ -f "$PREFS" ]; then
  cat "$PREFS"
else
  echo "tts.json nicht gefunden"
fi

echo ""
echo "=== 4. Edge TTS direkt testen ==="
echo "Test: edge-tts --voice de-DE-KatjaNeural --text 'Hallo Test' --write-media /tmp/tts_test.mp3"
edge-tts --voice de-DE-KatjaNeural --text "Hallo Test" --write-media /tmp/tts_test.mp3 2>&1 && echo "OK: /tmp/tts_test.mp3 erstellt" || echo "FEHLER"

echo ""
echo "=== 5. Gateway-Status ==="
systemctl --user is-active clawdbot-gateway-personal.service 2>/dev/null || echo "nicht aktiv"

echo ""
echo "=== 6. Letzte Gateway-Logs (TTS/tts/signal/voice) ==="
journalctl --user -u clawdbot-gateway-personal.service -n 30 --no-pager 2>/dev/null | grep -iE "tts|voice|signal|delivered|failed|error" | tail -15
