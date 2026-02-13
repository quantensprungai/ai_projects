#!/usr/bin/env python3
"""
Schritt 9: Spark (Qwen 32B auf Port 30001) als LLM-Backend für Clawdbot konfigurieren.

Auf VM102 ausführen (nach SSH-Login):

  python3 update_clawdbot_spark_config.py

Oder mit explizitem Spark-Host (falls spark-56d0 nicht auflöst):

  python3 update_clawdbot_spark_config.py --host 100.x.x.x

Vorher testen: curl -sf http://spark-56d0:30001/v1/models
"""
import argparse
import json
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"

SPARK_DEFAULT_HOST = "spark-56d0"
SPARK_PORT = 30001
MODEL_ID = "qwen3-32b-nvfp4"


def main():
    ap = argparse.ArgumentParser(description="Clawdbot Spark/Qwen-Model-Config hinzufügen")
    ap.add_argument("--host", default=SPARK_DEFAULT_HOST, help="Spark-Host (MagicDNS oder IP)")
    ap.add_argument("--port", type=int, default=SPARK_PORT, help="Spark-Port")
    ap.add_argument("--model", default=MODEL_ID, help="Modell-ID aus /v1/models")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen, nicht schreiben")
    args = ap.parse_args()

    base_url = f"http://{args.host}:{args.port}/v1"

    try:
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print(f"Fehler: {CONFIG_PATH} nicht gefunden.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Fehler: ungültiges JSON in {CONFIG_PATH}: {e}", file=sys.stderr)
        sys.exit(1)

    # models.providers.spark
    if "models" not in cfg:
        cfg["models"] = {}
    if "providers" not in cfg["models"]:
        cfg["models"]["providers"] = {}
    cfg["models"]["providers"]["spark"] = {
        "baseUrl": base_url,
        "apiKey": "dummy",
        "api": "openai-completions",
        "models": [
            {
                "id": args.model,
                "name": "Qwen 32B",
                "contextWindow": 32000,
                "maxTokens": 8192,
            }
        ],
    }

    # agents.defaults.model.primary
    if "agents" not in cfg:
        cfg["agents"] = {}
    if "defaults" not in cfg["agents"]:
        cfg["agents"]["defaults"] = {}
    if "model" not in cfg["agents"]["defaults"]:
        cfg["agents"]["defaults"]["model"] = {}
    if isinstance(cfg["agents"]["defaults"]["model"], dict):
        cfg["agents"]["defaults"]["model"]["primary"] = f"spark/{args.model}"
    else:
        cfg["agents"]["defaults"]["model"] = {"primary": f"spark/{args.model}"}

    if args.dry_run:
        print(json.dumps({"models": cfg["models"], "agents": cfg["agents"]}, indent=2))
        return

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print(f"Config aktualisiert. Spark: {base_url}, Model: spark/{args.model}")
    print("Nächster Schritt: systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
