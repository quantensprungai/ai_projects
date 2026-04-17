#!/usr/bin/env python3
"""
Flora-Agent: Primärmodell auf Anthropic Claude Sonnet 4.5 (API) setzen.

Auf VM102 ausführen (nach SSH-Login), wenn ~/.clawdbot-personal/clawdbot.json existiert:

  python3 update_clawdbot_flora_sonnet.py

Voraussetzungen:
  - Flora existiert in agents.list (z. B. update_clawdbot_signal_config.py).
  - Anthropic-Auth für diesen Agent / das Gateway (API-Key):
      openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
    Oder ANTHROPIC_API_KEY in der Umgebung des Gateway-Dienstes (systemd).
    OpenClaw: Auth ist pro Agent relevant — bei „no api key for provider anthropic“
    für flora: Onboarding für flora erneut oder models status prüfen.

Sonstige Agents (heiko, noah, familie) behalten agents.defaults.model, sofern nicht
anders gesetzt.

Rückgängig (Flora nutzt wieder nur das Default-Modell aus agents.defaults):

  python3 update_clawdbot_flora_sonnet.py --clear
"""
import argparse
import json
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"

# Mit Clawdbot 2026.1.24-x ist Sonnet 4-6 im eingebauten Katalog oft noch nicht registriert
# („unknown model: anthropic/claude-sonnet-4-6“) — 4-5 ist im Paket referenziert (live-model-filter).
DEFAULT_SONNET = "anthropic/claude-sonnet-4-5"


def main():
    ap = argparse.ArgumentParser(
        description="Flora: Modell auf Anthropic Claude Sonnet 4.5 setzen oder zurücksetzen"
    )
    ap.add_argument(
        "--primary",
        default=DEFAULT_SONNET,
        help=f"Modell-Primary (Default: {DEFAULT_SONNET})",
    )
    ap.add_argument(
        "--clear",
        action="store_true",
        help="flora.model entfernen — Flora erbt wieder agents.defaults.model",
    )
    ap.add_argument("--dry-run", action="store_true", help="Nur JSON-Ausschnitt ausgeben")
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

    agents = cfg.get("agents", {}).get("list", [])
    flora = next((a for a in agents if a.get("id") == "flora"), None)
    if not flora:
        print("Fehler: Flora-Agent nicht in agents.list gefunden.", file=sys.stderr)
        sys.exit(1)

    if args.clear:
        flora.pop("model", None)
        print("flora.model entfernt (Fallback auf agents.defaults.model).")
    else:
        flora["model"] = {"primary": args.primary}
        print("Flora model.primary:", args.primary)

    if args.dry_run:
        print(json.dumps({"id": "flora", "model": flora.get("model")}, indent=2))
        return

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print("Config geschrieben:", CONFIG_PATH)
    print("Nächste Schritte:")
    print("  1) Anthropic-Auth prüfen:  openclaw --profile personal models status")
    print("  2) Gateway neu starten:   systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
