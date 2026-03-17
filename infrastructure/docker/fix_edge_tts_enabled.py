#!/usr/bin/env python3
"""messages.tts.edge.enabled auf True setzen.

tts.js prüft if (!config.edge.enabled) und überspringt mit 'edge: disabled'.
Config-Pfad: ~/.clawdbot-personal/clawdbot.json
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
    tts = cfg.setdefault("messages", {}).setdefault("tts", {})
    edge = tts.setdefault("edge", {})
    was = edge.get("enabled")
    edge["enabled"] = True
    # Sinnvolle Defaults falls nicht gesetzt
    edge.setdefault("lang", "de-DE")
    edge.setdefault("voice", "de-DE-KatjaNeural")
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)
    print(f"messages.tts.edge.enabled: {was} → True")
    print("Gateway neu starten: ~/.clawdbot/bin/clawdbot --profile personal gateway restart")
    return 0

if __name__ == "__main__":
    exit(main())
