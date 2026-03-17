#!/usr/bin/env python3
"""
Flora-Agent: Heartbeat-Config (4h, 09:00–20:00) setzen.

Auf VM102 ausführen (nach SSH-Login):

  python3 update_clawdbot_flora_config.py

Voraussetzung: Flora-Agent existiert bereits in agents.list (z.B. via update_clawdbot_signal_config.py).
"""
import json
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"

HEARTBEAT = {
    "every": "4h",
    "target": "last",
    "activeHours": {"start": "09:00", "end": "20:00"},
}


def main():
    try:
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print(f"Fehler: {CONFIG_PATH} nicht gefunden.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Fehler: ungültiges JSON in {CONFIG_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    agents = cfg.get("agents", {}).get("list", [])
    flora = next((a for a in agents if a.get("id") == "flora"), None)
    if not flora:
        print("Fehler: Flora-Agent nicht in agents.list gefunden.", file=sys.stderr)
        sys.exit(1)

    flora["heartbeat"] = HEARTBEAT
    print("Flora heartbeat:", json.dumps(HEARTBEAT, indent=2))

    # Cron global aktivieren (falls noch nicht)
    if "cron" not in cfg:
        cfg["cron"] = {}
    if cfg["cron"].get("enabled") is not True:
        cfg["cron"]["enabled"] = True
        print("Cron global aktiviert.")

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print("Config aktualisiert. Nächster Schritt:")
    print("  systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
