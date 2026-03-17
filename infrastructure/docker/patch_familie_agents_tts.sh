#!/bin/bash
# Familie-AGENTS.md um TTS-Regeln ergänzen – auf VM102 ausführen
# Verhindert: "Ich habe keine Sprachausgabe", tool_call tts, Emojis

FILE="$HOME/clawd/workspace-familie/AGENTS.md"
MARKER="## TTS-Regeln (Plattform übernimmt automatisch)"

if [ ! -f "$FILE" ]; then
  echo "Fehler: $FILE nicht gefunden."
  exit 1
fi

if grep -q "TTS-Regeln" "$FILE" 2>/dev/null; then
  echo "TTS-Regeln bereits vorhanden."
  exit 0
fi

cat >> "$FILE" << 'EOF'

## TTS-Regeln (Plattform übernimmt automatisch)
- Sprachausgabe wird von der Plattform übernommen – einfach normalen Text schreiben.
- Kein `<tool_call>` mit name "tts", kein [[tts]]-Tag.
- Keine Emojis (technische Einschränkung bei Sprachnachrichten).
EOF

echo "TTS-Regeln zu $FILE hinzugefügt. Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service"
