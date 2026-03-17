#!/usr/bin/env python3
"""
Flora-Workspace (Sage) auf VM102 deployen.

Voraussetzung: Skript und workspace-flora/ auf VM102 kopiert.

Auf VM105 (PowerShell):
  scp -r infrastructure/docker/workspace-flora infrastructure/docker/apply_flora_workspace.py user@docker-apps:/tmp/

Auf VM102 (nach SSH-Login):
  python3 /tmp/apply_flora_workspace.py

Optional: --template-dir /tmp/workspace-flora (falls anderer Pfad)
"""
import argparse
import os
import shutil

BASE = "/home/user/clawd"
DEFAULT_TEMPLATE_DIR = "/tmp/workspace-flora"
FILES = ["AGENTS.md", "SOUL.md", "USER.md", "WELCOME_MESSAGE.md", "HEARTBEAT.md", "CRON.md"]


def main():
    ap = argparse.ArgumentParser(description="Flora-Workspace (Sage) deployen")
    ap.add_argument("--template-dir", default=DEFAULT_TEMPLATE_DIR, help="Pfad zu workspace-flora Templates")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen, nicht schreiben")
    args = ap.parse_args()

    target = os.path.join(BASE, "workspace-flora")
    if not os.path.exists(target):
        print(f"Fehler: Zielverzeichnis {target} existiert nicht.", file=__import__("sys").stderr)
        exit(1)

    for f in FILES:
        src = os.path.join(args.template_dir, f)
        dst = os.path.join(target, f)
        if not os.path.exists(src):
            print(f"  Überspringe {f}: nicht gefunden in {args.template_dir}")
            continue
        if args.dry_run:
            print(f"  Würde kopieren: {src} -> {dst}")
        else:
            shutil.copy2(src, dst)
            print(f"  {f} -> deployed")

    if not args.dry_run:
        print("\nDone. Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")


if __name__ == "__main__":
    main()
