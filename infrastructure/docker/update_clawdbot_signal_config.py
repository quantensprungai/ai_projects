#!/usr/bin/env python3
"""
Schritt 4+5: Signal-Channel aktivieren und Bindings mit echten E.164-Nummern.

Auf VM102 ausführen (nach SSH-Login):

  python3 update_clawdbot_signal_config.py \\
    --account "+49XXXXXXXXX" \\
    --heiko "+49..." \\
    --noah "+49..." \\
    --flora "+49..."

Optional: --familie "+49..." für Einzelperson statt Gruppe. Ohne --familie bleibt
das Gruppen-Binding mit Platzhalter (oder entferne es manuell).
"""
import argparse
import json
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"


def main():
    ap = argparse.ArgumentParser(description="Clawdbot Signal-Config und Bindings aktualisieren")
    ap.add_argument("--account", required=True, help="Bot-Signal-Nummer (E.164, z.B. +49...)")
    ap.add_argument("--heiko", required=True, help="Heikos Signal-Nummer (E.164)")
    ap.add_argument("--noah", required=True, help="Noahs Signal-Nummer (E.164)")
    ap.add_argument("--flora", required=True, help="Floras Signal-Nummer (E.164)")
    ap.add_argument("--familie", default=None, help="Familie: E.164 für DM oder base64 Gruppen-ID")
    ap.add_argument("--familie-allow-from", default=None, help="Gruppen-Zulassung: E.164 mit Komma (z.B. +49HEIKO,+49LILY). Ohne: Heiko/Noah/Flora")
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

    # Schritt 4: channels.signal
    if "channels" not in cfg:
        cfg["channels"] = {}
    signal_cfg = cfg.get("channels", {}).get("signal", {})
    signal_cfg.update({
        "enabled": True,
        "account": args.account,
        "cliPath": "signal-cli",
        "dmPolicy": "pairing",
        "allowFrom": [],
    })
    # Gruppen: groupAllowFrom (z.B. Heiko + Lily). Signal kennt kein "groups".
    if args.familie and not args.familie.startswith("+"):
        signal_cfg["groupPolicy"] = "allowlist"
        if args.familie_allow_from:
            signal_cfg["groupAllowFrom"] = [n.strip() for n in args.familie_allow_from.split(",") if n.strip()]
        else:
            signal_cfg["groupAllowFrom"] = [args.heiko, args.noah, args.flora]
    cfg["channels"]["signal"] = signal_cfg

    # Schritt 5: Bindings
    # peer.kind: "dm" für DMs, "group" für Gruppen (Clawdbot 2026.x Schema)
    bindings = [
        {"agentId": "heiko", "match": {"channel": "signal", "peer": {"kind": "dm", "id": args.heiko}}},
        {"agentId": "noah", "match": {"channel": "signal", "peer": {"kind": "dm", "id": args.noah}}},
        {"agentId": "flora", "match": {"channel": "signal", "peer": {"kind": "dm", "id": args.flora}}},
    ]

    if args.familie:
        kind = "dm" if args.familie.startswith("+") else "group"
        bindings.append({"agentId": "familie", "match": {"channel": "signal", "peer": {"kind": kind, "id": args.familie}}})
    else:
        bindings.append({"agentId": "familie", "match": {"channel": "signal", "peer": {"kind": "group", "id": "REPLACE_FAMILIE_GROUP"}}})

    bindings.append({"agentId": "main", "match": {"channel": "signal"}})
    cfg["bindings"] = bindings

    # Familie-Agent: mentionPatterns fuer Signal-Gruppen (Signal hat keine @mentions)
    # ".*" = jede Nachricht triggert (entspricht requireMention: false)
    if args.familie and not args.familie.startswith("+"):
        if "agents" not in cfg:
            cfg["agents"] = {}
        if "list" not in cfg["agents"]:
            cfg["agents"]["list"] = []
        # familie-Agent in list finden oder anlegen
        familie_agent = next((a for a in cfg["agents"]["list"] if a.get("id") == "familie"), None)
        if familie_agent is None:
            cfg["agents"]["list"].append({"id": "familie", "groupChat": {"mentionPatterns": [".*"]}})
        else:
            familie_agent["groupChat"] = familie_agent.get("groupChat") or {}
            familie_agent["groupChat"]["mentionPatterns"] = [".*"]

    if args.dry_run:
        print(json.dumps(cfg, indent=2))
        return

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print("Config aktualisiert. Nächster Schritt:")
    print("  systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
