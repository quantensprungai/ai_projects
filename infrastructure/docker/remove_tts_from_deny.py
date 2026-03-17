#!/usr/bin/env python3
"""tts aus tools.deny entfernen – Test ob tools.deny Auto-TTS blockiert.

Hypothese: tools.deny: ["tts"] blockiert die gesamte Auto-TTS-Pipeline,
nicht nur Agent-Tool-Calls. Wenn Audio danach funktioniert: CRITICAL-Block
in AGENTS.md beibehalten (verhindert [[tts:...]]-Output).
"""
import json
import os

CONFIG_PATH = os.path.expanduser("~/.clawdbot-personal/clawdbot.json")

def main():
    if not os.path.isfile(CONFIG_PATH):
        print(f"Config nicht gefunden: {CONFIG_PATH}")
        return 1
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
    deny = cfg.get("tools", {}).get("deny", [])
    print(f"Vorher: tools.deny = {deny}")
    if "tts" in deny:
        deny.remove("tts")
        cfg.setdefault("tools", {})["deny"] = deny
        with open(CONFIG_PATH, "w") as f:
            json.dump(cfg, f, indent=2)
        print("tts aus tools.deny ENTFERNT ✓")
        print("Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")
    else:
        print("tts war nicht in tools.deny")
    return 0

if __name__ == "__main__":
    exit(main())
