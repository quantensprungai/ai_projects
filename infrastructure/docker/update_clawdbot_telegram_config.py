#!/usr/bin/env python3
"""
Telegram-Channel aktivieren und Bindings hinzufügen (zusätzlich zu Signal).

Auf VM102 ausführen (nach SSH-Login):

  python3 update_clawdbot_telegram_config.py --bot-token "123456789:ABCdef..."

Optional – Agent-spezifische Bindings (Telegram-User-IDs nach Pairing):

  python3 update_clawdbot_telegram_config.py --bot-token "..." \\
    --heiko "123456789" \\
    --noah "987654321" \\
    --flora "111222333" \\
    --familie "444555666"

Telegram-User-ID ermitteln:
  - Nach Pairing: clawdbot pairing list telegram (zeigt ggf. User-Infos)
  - Oder: curl "https://api.telegram.org/bot<TOKEN>/getUpdates" (als User dem Bot schreiben)
  - Oder: openclaw logs --follow, dann dem Bot eine DM schicken

Hinweis: Bestehende Bindings (z.B. Signal) werden beibehalten – Telegram-Bindings werden ergänzt.
"""
import argparse
import json
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"


def normalize_telegram_id(raw: str) -> str:
    """Telegram-ID normalisieren: telegram:123 oder tg:123 → 123."""
    if not raw or not raw.strip():
        return ""
    s = raw.strip()
    for prefix in ("telegram:", "tg:"):
        if s.lower().startswith(prefix):
            s = s[len(prefix):].strip()
    return s if s.isdigit() else raw.strip()


def main():
    ap = argparse.ArgumentParser(
        description="Clawdbot Telegram-Channel aktivieren und Bindings ergänzen"
    )
    ap.add_argument("--bot-token", required=True, help="Bot-Token von @BotFather")
    ap.add_argument("--heiko", default=None, help="Heikos Telegram-User-ID (nach Pairing)")
    ap.add_argument("--noah", default=None, help="Noahs Telegram-User-ID")
    ap.add_argument("--flora", default=None, help="Floras Telegram-User-ID")
    ap.add_argument("--familie", default=None, help="Familie/Lumi Telegram-User-ID")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen, nicht schreiben")
    args = ap.parse_args()

    try:
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print(f"Fehler: {CONFIG_PATH} nicht gefunden.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Fehler: ungültiges JSON in {CONFIG_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    # channels.telegram
    if "channels" not in cfg:
        cfg["channels"] = {}
    cfg["channels"]["telegram"] = {
        "enabled": True,
        "botToken": args.bot_token.strip(),
        "dmPolicy": "pairing",
    }

    # Bindings: Bestehende behalten, Telegram-Bindings ergänzen
    bindings = list(cfg.get("bindings", []))

    # Entferne alte Telegram-Bindings (für saubere Neu-Konfiguration)
    bindings = [b for b in bindings if b.get("match", {}).get("channel") != "telegram"]

    def tg_binding(agent_id: str, user_id: str) -> dict:
        uid = normalize_telegram_id(user_id)
        if not uid:
            return None
        return {
            "agentId": agent_id,
            "match": {"channel": "telegram", "peer": {"kind": "dm", "id": uid}},
        }

    agent_ids = [
        ("heiko", args.heiko),
        ("noah", args.noah),
        ("flora", args.flora),
        ("familie", args.familie),
    ]
    for agent_id, uid in agent_ids:
        b = tg_binding(agent_id, uid) if uid else None
        if b:
            bindings.append(b)

    # main-Fallback für Telegram (wie bei Signal)
    bindings.append({"agentId": "main", "match": {"channel": "telegram"}})

    cfg["bindings"] = bindings

    if args.dry_run:
        print(json.dumps(cfg, indent=2))
        return

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print("Telegram-Config aktualisiert.")
    print("\nNächste Schritte:")
    print("  1. Gateway neu starten:")
    print("     systemctl --user restart clawdbot-gateway-personal.service")
    print("  2. Pairing durchführen:")
    print("     clawdbot --profile personal pairing list telegram")
    print("     clawdbot --profile personal pairing approve telegram <CODE>")
    print("  3. Telegram-User-IDs ermitteln (getUpdates oder Logs), dann Skript erneut mit --heiko/--noah/... ausführen.")


if __name__ == "__main__":
    main()
