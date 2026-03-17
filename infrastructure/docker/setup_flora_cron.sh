#!/bin/bash
# Sage Cron Jobs für Flora – auf VM102 ausführen
# Voraussetzung: clawdbot --profile personal, Flora gepaart (Signal)
# Nutze clawdbot oder openclaw je nach Installation

CMD="${CLAWDBOT_CMD:-clawdbot} --profile personal"
if ! command -v clawdbot &>/dev/null && command -v openclaw &>/dev/null; then
  CMD="openclaw"
fi

echo "Verwende: $CMD"
echo ""

# Job 1: Pflanze der Woche (Sonntag 18:00)
echo "Füge Cron-Job 1 hinzu: Pflanze der Woche..."
$CMD cron add \
  --name "Pflanze der Woche" \
  --cron "0 18 * * 0" \
  --tz "Europe/Berlin" \
  --session isolated \
  --agent flora \
  --announce \
  --message "Pick a medicinal plant or herb that fits the current season. Share 2-3 short sentences about something surprising about it – ideally with a bridge to physiotherapy, anatomy, or healing. Tone: like a friend who just discovered something cool. Use 1-2 fitting emojis. NO learning task, NO question at the end (unless it's a genuinely curious one). Write in German. Example: '🌿 Wusstest du, dass Rosmarin die Durchblutung so stark fördert, dass er in der Sportphysiotherapie als Badezusatz genutzt wird? Die alten Griechen haben ihn übrigens Studenten vor Prüfungen auf den Kopf gelegt – ob das hilft? 🤔'"

echo ""

# Job 2: Jahreszeitenimpuls (1. des Monats, 10:00)
echo "Füge Cron-Job 2 hinzu: Jahreszeitenimpuls..."
$CMD cron add \
  --name "Jahreszeitenimpuls" \
  --cron "0 10 1 * *" \
  --tz "Europe/Berlin" \
  --session isolated \
  --agent flora \
  --announce \
  --message "It's the 1st of a new month. Create a short (2-3 sentences), seasonal observation about nature – what's happening outside right now? Which herbs are growing, blooming, resting? Connect it – if it fits organically – to something from physiotherapy or health. Tone: poetic-casual, like glancing out the window. NO learning task. Write in German. Example: '🌸 März – die Birken fangen an zu weinen (Birkenwasser!). Wusstest du, dass Birkenwasser entzündungshemmend wirkt und traditionell bei Gelenkbeschwerden eingesetzt wurde? Die Natur macht schon ihr Ding, bevor wir überhaupt aufstehen.'"

echo ""
echo "Cron-Jobs hinzugefügt. Prüfen: $CMD cron list"
