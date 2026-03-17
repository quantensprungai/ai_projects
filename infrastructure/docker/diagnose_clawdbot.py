#!/usr/bin/env python3
"""Schnelle Clawdbot-Diagnose – auf VM102 ausführen."""
import json
import os
import subprocess

CONFIG = os.path.expanduser("~/.clawdbot-personal/clawdbot.json")

def run(cmd, timeout=10):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip() + (r.stderr.strip() if r.stderr else "")
    except Exception as e:
        return str(e)

print("=== 1. Gateway-Status ===")
r = subprocess.run(["systemctl", "--user", "is-active", "clawdbot-gateway-personal.service"], capture_output=True, text=True)
print(r.stdout.strip() or "NICHT AKTIV")

print("\n=== 2. Letzte Gateway-Logs ===")
r = subprocess.run("journalctl --user -u clawdbot-gateway-personal.service -n 40 --no-pager".split(), capture_output=True, text=True)
for line in (r.stdout or "").split("\n")[-25:]:
    print(line[:120])

print("\n=== 3. signal-cli (Port 8081) ===")
r = subprocess.run("ss -tlnp 2>/dev/null | grep 8081", shell=True, capture_output=True, text=True)
print(r.stdout.strip() or "Nicht gefunden")

print("\n=== 4. Config JSON ===")
cfg = None
try:
    with open(CONFIG) as f:
        cfg = json.load(f)
    print("JSON OK")
    sig = cfg.get("channels", {}).get("signal", {})
    print("channels.signal keys:", list(sig.keys()) if sig else "leer/nicht vorhanden")
except Exception as e:
    print("FEHLER:", e)

print("\n=== 5. Spark/LLM erreichbar? ===")
try:
    base = (cfg or {}).get("models", {}).get("providers", {}).get("spark", {}).get("baseUrl", "http://spark-56d0:30001/v1")
    url = base.replace("/v1", "") + "/v1/models" if "/v1" in base else base + "/v1/models"
    r = subprocess.run(["curl", "-sf", "--connect-timeout", "5", url], capture_output=True, text=True)
    print("Spark:", "OK" if r.returncode == 0 else "NICHT ERREICHBAR")
except NameError:
    print("Config nicht geladen, Spark-Check übersprungen")

print("\n=== 6. Bindings ===")
if cfg:
    for b in cfg.get("bindings", [])[:6]:
        print(" ", b.get("agentId"), "->", str(b.get("match", {}).get("peer", {}).get("id", "?"))[:25])
else:
    print("Config nicht geladen")
