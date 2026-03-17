#!/usr/bin/env python3
"""Entfernt channels.signal.tts aus clawdbot.json – auf VM102 ausführen.
Der Key ist ungültig und führt zu 'Config invalid'."""
import json
import os

CONFIG = os.path.expanduser("~/.clawdbot-personal/clawdbot.json")

def main():
    with open(CONFIG) as f:
        cfg = json.load(f)
    sig = cfg.get("channels", {}).get("signal", {})
    if "tts" in sig:
        del sig["tts"]
        with open(CONFIG, "w") as f:
            json.dump(cfg, f, indent=2)
        print("channels.signal.tts entfernt.")
    else:
        print("channels.signal.tts war nicht vorhanden.")
    print("Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")

if __name__ == "__main__":
    main()
