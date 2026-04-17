#!/usr/bin/env python3
"""Einmal: Textdatei per clawdbot an Flora-Telegram senden (VM102)."""
import subprocess
import sys

MSG_FILE = "/tmp/sage_morning_trigger.txt"
TARGET = "665037248"
BOT = "/home/user/.clawdbot/bin/clawdbot"

def main():
    msg = open(MSG_FILE, encoding="utf-8").read().strip()
    cmd = [
        BOT,
        "--profile",
        "personal",
        "message",
        "send",
        "--channel",
        "telegram",
        "--target",
        TARGET,
        "--message",
        msg,
        "--json",
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
