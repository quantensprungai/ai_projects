#!/usr/bin/env python3
"""Flora-Binding und Pairing prüfen – auf VM102 ausführen."""
import json
import os
import subprocess

CONFIG = os.path.expanduser("~/.clawdbot-personal/clawdbot.json")

print("=== 1. Flora-Bindings in Config ===")
try:
    with open(CONFIG) as f:
        cfg = json.load(f)
    for b in cfg.get("bindings", []):
        if b.get("agentId") == "flora":
            peer = b.get("match", {}).get("peer", {})
            print(f"  peer: {peer}")
except Exception as e:
    print(f"  Fehler: {e}")

print("\n=== 2. Pending Pairings ===")
try:
    r = subprocess.run(
        ["/home/user/.clawdbot/bin/clawdbot", "--profile", "personal", "pairing", "list", "signal"],
        capture_output=True, text=True, timeout=10
    )
    print(r.stdout or r.stderr or "Keine Ausgabe")
except Exception as e:
    print(f"  Fehler: {e}")

print("\n=== 3. Approve-Befehl (wenn Flora-Nummer im Pairing) ===")
print("  clawdbot --profile personal pairing approve signal <CODE>")
