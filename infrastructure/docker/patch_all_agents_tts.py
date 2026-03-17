#!/usr/bin/env python3
"""
TTS-Regeln zu allen Agent-Workspaces hinzufügen – auf VM102 ausführen.
Behebt: tool_call tts, [[tts:...]], Emojis, "Ich habe keine Sprachausgabe"
"""
import os

BASE = os.path.expanduser("~/clawd")
AGENTS = ["heiko", "noah", "flora", "familie"]

RULES = """

## TTS-Regeln (Plattform übernimmt automatisch)
- NUR normalen Text schreiben. Kein `<tool_call>` mit name "tts", kein [[tts:...]], kein Markup.
- Die Plattform wandelt Antworten bei Sprachnachricht-Inbound automatisch in Audio um.
- Keine Emojis (technische Einschränkung bei Sprachnachrichten).
"""

def main():
    for agent in AGENTS:
        path = os.path.join(BASE, f"workspace-{agent}", "AGENTS.md")
        if not os.path.isfile(path):
            print(f"  Überspringe {agent}: {path} nicht gefunden")
            continue
        with open(path) as f:
            content = f.read()
        if "TTS-Regeln" in content:
            print(f"  {agent}: TTS-Regeln bereits vorhanden")
            continue
        with open(path, "a") as f:
            f.write(RULES)
        print(f"  {agent}: TTS-Regeln hinzugefügt")
    print("\nGateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")
    print("Sessions zurücksetzen (falls Agent weiterhin tool_call nutzt):")
    print("  rm -rf ~/.clawdbot-personal/agents/heiko/sessions/*")
    print("  rm -rf ~/.clawdbot-personal/agents/flora/sessions/*")
    print("  rm -rf ~/.clawdbot-personal/agents/familie/sessions/*")
    return 0

if __name__ == "__main__":
    exit(main())
