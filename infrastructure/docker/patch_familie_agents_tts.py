#!/usr/bin/env python3
"""Familie-AGENTS.md um TTS-Regeln ergänzen – auf VM102 ausführen."""
import os

FILE = os.path.expanduser("~/clawd/workspace-familie/AGENTS.md")
RULES = """

## TTS-Regeln (Plattform übernimmt automatisch)
- Sprachausgabe wird von der Plattform übernommen – einfach normalen Text schreiben.
- Kein `<tool_call>` mit name "tts", kein [[tts]]-Tag.
- Keine Emojis (technische Einschränkung bei Sprachnachrichten).
"""

def main():
    if not os.path.isfile(FILE):
        print(f"Fehler: {FILE} nicht gefunden.")
        return 1
    with open(FILE) as f:
        content = f.read()
    if "TTS-Regeln" in content:
        print("TTS-Regeln bereits vorhanden.")
        return 0
    with open(FILE, "a") as f:
        f.write(RULES)
    print(f"TTS-Regeln zu {FILE} hinzugefügt.")
    print("Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")
    return 0

if __name__ == "__main__":
    exit(main())
