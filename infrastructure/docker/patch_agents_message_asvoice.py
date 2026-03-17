#!/usr/bin/env python3
"""
Verhindert, dass Agents <tool_call> mit message + asVoice ausgeben.

Symptom: User erhält Rohtext wie:
  <tool_call>{"name": "message", "arguments": {"asVoice": true, ...}}</tool_call>

Ursache: Agent nutzt message-Tool statt normalen Text. tools.deny: ["tts"]
blockiert nur tts, nicht message. Die Plattform wandelt bei auto: "always"
normalen Text automatisch in Audio um – der Agent soll NUR Text schreiben.

Auf VM102 ausführen (Workspaces unter ~/clawd):
  python3 patch_agents_message_asvoice.py
"""
import os

BASE = os.path.expanduser("~/clawd")
AGENTS = ["heiko", "noah", "flora", "familie"]

# Regel, die ergänzt werden soll
MESSAGE_ASVOICE_RULE = (
    "- **NIEMALS** `<tool_call>` mit name \"message\" und asVoice verwenden – "
    "nur normalen Text schreiben, die Plattform wandelt automatisch um."
)

def main():
    for agent in AGENTS:
        path = os.path.join(BASE, f"workspace-{agent}", "AGENTS.md")
        if not os.path.isfile(path):
            print(f"  Überspringe {agent}: {path} nicht gefunden")
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()
        if "asVoice" in content and "message" in content and "NIEMALS" in content:
            print(f"  {agent}: Regel bereits vorhanden")
            continue
        if "message" in content and "asVoice" in content:
            print(f"  {agent}: Ähnliche Regel gefunden, prüfen")
        # In CRITICAL-Block einfügen (nach "NIEMALS [[tts" oder nach "Keine Tags")
        insert_markers = [
            "- **NIEMALS** `[[tts:...]]`",
            "- **NIEMALS** [[tts:...]]",
            "- Die Plattform wandelt deine Antwort automatisch in Sprachnachricht um.",
        ]
        inserted = False
        for marker in insert_markers:
            if marker in content and MESSAGE_ASVOICE_RULE not in content:
                content = content.replace(
                    marker,
                    marker + "\n" + MESSAGE_ASVOICE_RULE,
                    1
                )
                inserted = True
                break
        if not inserted:
            # Fallback: nach CRITICAL-Überschrift
            if "## CRITICAL" in content and MESSAGE_ASVOICE_RULE not in content:
                content = content.replace(
                    "## CRITICAL – Antwortformat (NIEMALS verletzen)\n",
                    "## CRITICAL – Antwortformat (NIEMALS verletzen)\n" + MESSAGE_ASVOICE_RULE + "\n",
                    1
                )
                inserted = True
        if inserted:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  {agent}: Regel eingefügt")
        else:
            print(f"  {agent}: Kein Einfügepunkt gefunden")
    print("\nSessions zurücksetzen (empfohlen):")
    print("  rm -rf ~/.clawdbot-personal/agents/*/sessions/*")
    print("Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")
    return 0

if __name__ == "__main__":
    exit(main())
