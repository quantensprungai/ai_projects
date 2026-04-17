#!/usr/bin/env python3
"""
TTS / Sprachantworten (Voice-MP3) global deaktivieren — nur Text-Antworten.

Auf VM102:
  python3 update_clawdbot_voice_disable.py

STT (Sprachnachrichten transkribieren) bleibt unverändert (tools.media.audio), falls konfiguriert.
"""
import json
import os
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"
PREFS_PATH = "/home/user/.clawdbot-personal/settings/tts.json"


def main():
    try:
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print(f"Fehler: {CONFIG_PATH} nicht gefunden.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Fehler: JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if "messages" not in cfg:
        cfg["messages"] = {}
    if "tts" not in cfg["messages"]:
        cfg["messages"]["tts"] = {}

    tts = cfg["messages"]["tts"]
    tts["auto"] = "off"
    # Schema (Clawdbot 2026.1.x): mode nur "final" | "all" — "off" ist ungültig und killt das Gateway.
    # Mit auto=off + edge.enabled=false ist TTS aus; mode=final = weniger TTS-Anlässe als "all".
    tts["mode"] = "final"
    tts["edge"] = {**tts.get("edge", {}), "enabled": False}

    if os.path.isfile(PREFS_PATH):
        try:
            with open(PREFS_PATH) as f:
                prefs = json.load(f)
        except json.JSONDecodeError:
            prefs = {}
        inner = prefs.get("tts")
        if isinstance(inner, dict):
            inner["auto"] = "off"
            prefs["tts"] = inner
        else:
            prefs = {"tts": {"auto": "off", "summarize": False, "maxLength": 8000}}
        with open(PREFS_PATH, "w") as f:
            json.dump(prefs, f, indent=2)
        print("tts.json: auto=off")

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print("messages.tts: auto=off, edge.enabled=false")
    print("Nächster Schritt: systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
