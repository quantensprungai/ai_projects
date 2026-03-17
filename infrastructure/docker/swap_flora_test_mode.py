#!/usr/bin/env python3
"""
Flora-Testmodus: Deine Nummer (+4917641410414) vorübergehend auf Flora umbiegen.

Signal nutzt nach Pairing oft UUID statt E.164 – daher werden ALLE Heiko-Bindings
(E.164 + UUID) umgebogen, nicht nur die E.164.

Auf VM102 ausführen:
  python3 swap_flora_test_mode.py          # Testmodus: deine Nummer → Flora
  python3 swap_flora_test_mode.py --restore # Zurück: deine Nummer → Heiko
"""
import argparse
import json
import os
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"
BACKUP_PATH = "/tmp/flora_test_swap_backup.json"
TEST_NUMBER = "+4917641410414"


def main():
    ap = argparse.ArgumentParser(description="Flora-Testmodus: Nummer umbiegen")
    ap.add_argument("--restore", action="store_true", help="Zurück auf Heiko")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen")
    args = ap.parse_args()

    with open(CONFIG_PATH) as f:
        cfg = json.load(f)

    bindings = cfg.get("bindings", [])

    if args.restore:
        # Restore: Bindings aus Backup von flora zurück auf heiko
        if not os.path.exists(BACKUP_PATH):
            print("Fehler: Kein Backup gefunden. Erst Testmodus ausführen.", file=sys.stderr)
            sys.exit(1)
        with open(BACKUP_PATH) as f:
            peer_ids = json.load(f)
        target_bindings = [b for b in bindings if b.get("match", {}).get("peer", {}).get("id") in peer_ids]
        for b in target_bindings:
            b["agentId"] = "heiko"
            print(f"  Restore: {b['match']['peer']['id']} → heiko")
    else:
        # Testmodus: ALLE Heiko-Bindings (E.164 + UUID) auf flora
        target_bindings = [b for b in bindings if b.get("agentId") == "heiko" and b.get("match", {}).get("channel") == "signal"]
        if not target_bindings:
            print("Fehler: Keine Heiko-Bindings gefunden.", file=sys.stderr)
            sys.exit(1)
        peer_ids = [b["match"]["peer"]["id"] for b in target_bindings]
        with open(BACKUP_PATH, "w") as f:
            json.dump(peer_ids, f, indent=2)
        for b in target_bindings:
            pid = b["match"]["peer"]["id"]
            b["agentId"] = "flora"
            print(f"  {pid} → flora")

        # Session-Cache löschen, damit neues Routing greift (nicht alte Heiko-Session)
        sessions_dir = os.path.expanduser("~/.clawdbot-personal/agents/heiko/sessions")
        if os.path.isdir(sessions_dir):
            import glob
            removed = 0
            for f in glob.glob(os.path.join(sessions_dir, "*")):
                try:
                    if os.path.isfile(f):
                        os.remove(f)
                        removed += 1
                except OSError:
                    pass
            if removed:
                print("  Heiko-Sessions gelöscht – frisches Routing beim nächsten Chat.")

    if args.dry_run:
        print(json.dumps([b for b in bindings if b.get("agentId") in ("heiko", "flora")], indent=2))
        return

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    mode = "Restore" if args.restore else "Testmodus"
    print(f"{mode}: Deine Nummer → {'Heiko' if args.restore else 'Flora'}")
    print("Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
