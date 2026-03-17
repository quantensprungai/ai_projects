#!/usr/bin/env python3
"""
Entfernt messages.tts.audioAsVoice aus clawdbot.json – ungültiger Key führt zu Config invalid / Crash-Loop.

Auf VM102 ausführen:
  python3 remove_audio_as_voice_config.py

Alternative: ~/.clawdbot/bin/clawdbot --profile personal doctor --fix
"""
import json
import os
import sys

CONFIG_PATH = os.environ.get("CLAWDBOT_CONFIG", os.path.expanduser("~/.clawdbot-personal/clawdbot.json"))


def main():
    path = CONFIG_PATH
    if not os.path.isfile(path):
        print(f"Fehler: {path} nicht gefunden.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(path) as f:
            cfg = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Fehler: ungültiges JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if "messages" not in cfg:
        cfg["messages"] = {}
    if "tts" not in cfg["messages"]:
        cfg["messages"]["tts"] = {}
    tts = cfg["messages"]["tts"]

    if "audioAsVoice" in tts:
        del tts["audioAsVoice"]
        with open(path, "w") as f:
            json.dump(cfg, f, indent=2)
        print("audioAsVoice ENTFERNT.")
        print("Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")
    else:
        print("audioAsVoice war nicht in der Config.")
        print("Falls Gateway crasht: ~/.clawdbot/bin/clawdbot --profile personal doctor --fix")


if __name__ == "__main__":
    main()
