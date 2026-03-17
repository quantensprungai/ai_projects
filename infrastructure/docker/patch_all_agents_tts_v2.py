#!/usr/bin/env python3
"""
TTS-Regeln in allen Agent-Workspaces ERSETZEN/VERSCHÄRFEN – auf VM102 ausführen.
Behebt: [[tts:...]], [[tts:text]]...[[/tts:text]], Emojis
"""
import os
import re

BASE = os.path.expanduser("~/clawd")
AGENTS = ["heiko", "noah", "flora", "familie"]

# Striktere Regeln – ganz oben in der Datei einfügen (nach der ersten #-Zeile)
CRITICAL_BLOCK = """

## CRITICAL – Antwortformat (NIEMALS verletzen)
- **NUR normalen Fließtext** schreiben. Keine Tags, kein Markup.
- **NIEMALS** [[tts:...]] oder [[tts:text]]...[[/tts:text]] – diese erscheinen als Rohtext und funktionieren nicht.
- **NIEMALS** <tool_call> mit name "message" und asVoice – nur normalen Text schreiben, die Plattform wandelt automatisch um.
- **NIEMALS** Emojis (😊 😄 🌿 etc.) – brechen den Signal-Versand.
- Die Plattform wandelt deine Antwort automatisch in Sprachnachricht um.
"""

def has_critical_block(content: str) -> bool:
    return "CRITICAL – Antwortformat" in content

def main():
    for agent in AGENTS:
        path = os.path.join(BASE, f"workspace-{agent}", "AGENTS.md")
        if not os.path.isfile(path):
            print(f"  Überspringe {agent}: {path} nicht gefunden")
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()
        if has_critical_block(content):
            print(f"  {agent}: CRITICAL-Block bereits vorhanden")
            continue
        # Alte TTS-Regeln-Sektion entfernen (falls vorhanden)
        content = re.sub(
            r'\n## TTS-Regeln \(Plattform übernimmt automatisch\)\n(?:- .*\n)*',
            '',
            content
        )
        # CRITICAL-Block nach der ersten #-Zeile einfügen
        first_line = content.find("\n")
        insert_pos = first_line + 1 if first_line >= 0 else 0
        content = content[:insert_pos] + CRITICAL_BLOCK + content[insert_pos:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  {agent}: CRITICAL-Block eingefügt")
    print("\nGateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")
    print("Sessions zurücksetzen: rm -rf ~/.clawdbot-personal/agents/heiko/sessions/* ~/.clawdbot-personal/agents/noah/sessions/* ~/.clawdbot-personal/agents/flora/sessions/* ~/.clawdbot-personal/agents/familie/sessions/*")
    return 0

if __name__ == "__main__":
    exit(main())
