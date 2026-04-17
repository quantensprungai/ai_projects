#!/usr/bin/env python3
"""Notfall: messages.tts.mode auf gültigen Wert setzen (final|all), Gateway startet sonst nicht."""
import json
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"


def main():
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
    tts = cfg.setdefault("messages", {}).setdefault("tts", {})
    tts["mode"] = "final"
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)
    print("messages.tts.mode = final (gültig für Clawdbot)")


if __name__ == "__main__":
    main()
