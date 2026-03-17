#!/usr/bin/env python3
"""
Web-Tools (web_search, web_fetch) aktivieren – mit Perplexity oder Brave.

Auf VM102 ausführen:

  # Perplexity (empfohlen: AI-synthetisierte Antworten mit Zitaten)
  python3 update_clawdbot_web_tools.py --provider perplexity --api-key "pplx-..."

  # Oder: API-Key per Umgebungsvariable
  PERPLEXITY_API_KEY=pplx-... python3 update_clawdbot_web_tools.py --provider perplexity

  # Brave (klassische Suchergebnisse, kostenloser Tier)
  BRAVE_API_KEY=... python3 update_clawdbot_web_tools.py --provider brave

Hinweis: API-Keys niemals ins Repo committen. Nutze Env oder --api-key zur Laufzeit.
"""
import argparse
import json
import os
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"


def main():
    ap = argparse.ArgumentParser(description="Clawdbot Web-Tools (web_search, web_fetch) aktivieren")
    ap.add_argument("--provider", choices=["perplexity", "brave"], default="perplexity",
                    help="Such-Provider (default: perplexity)")
    ap.add_argument("--api-key", default=None, help="API-Key (oder Env: PERPLEXITY_API_KEY / BRAVE_API_KEY)")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen, nicht schreiben")
    args = ap.parse_args()

    if args.api_key:
        api_key = args.api_key.strip()
    elif args.provider == "perplexity":
        api_key = os.environ.get("PERPLEXITY_API_KEY", "").strip()
    else:
        api_key = os.environ.get("BRAVE_API_KEY", "").strip()

    if not api_key and not args.dry_run:
        print("Fehler: API-Key fehlt. Setze --api-key oder PERPLEXITY_API_KEY / BRAVE_API_KEY.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print(f"Fehler: {CONFIG_PATH} nicht gefunden.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Fehler: ungültiges JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if "tools" not in cfg:
        cfg["tools"] = {}
    tools = cfg["tools"]

    # tools.allow: group:web hinzufügen (web_search, web_fetch)
    allow = list(tools.get("allow", []))
    if "group:web" not in allow and "web_search" not in allow:
        allow.append("group:web")
    tools["allow"] = allow

    # tools.web
    if "web" not in tools:
        tools["web"] = {}
    tools["web"]["fetch"] = tools["web"].get("fetch", {})
    tools["web"]["fetch"]["enabled"] = True

    tools["web"]["search"] = tools["web"].get("search", {})
    tools["web"]["search"]["enabled"] = True

    if args.provider == "perplexity":
        tools["web"]["search"]["provider"] = "perplexity"
        tools["web"]["search"]["perplexity"] = {
            "apiKey": api_key or "(setze PERPLEXITY_API_KEY)",
            "baseUrl": "https://api.perplexity.ai",
            "model": "sonar-pro",
        }
        print("Provider: Perplexity Sonar")
    else:
        tools["web"]["search"]["provider"] = "brave"
        if api_key:
            tools["web"]["search"]["apiKey"] = api_key
        print("Provider: Brave Search")

    if args.dry_run:
        c = json.loads(json.dumps(cfg))
        p = c.get("tools", {}).get("web", {}).get("search", {}).get("perplexity", {})
        if p and p.get("apiKey"):
            c["tools"]["web"]["search"]["perplexity"]["apiKey"] = "***"
        if c.get("tools", {}).get("web", {}).get("search", {}).get("apiKey"):
            c["tools"]["web"]["search"]["apiKey"] = "***"
        print(json.dumps(c, indent=2))
        return

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print("Web-Tools aktiviert. Gateway neu starten:")
    print("  systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
