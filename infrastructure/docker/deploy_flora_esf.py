#!/usr/bin/env python3
"""
Flora-Workspace inkl. learning/esf auf VM102 deployen + Hermes pilot sync.

Von VM105 (PowerShell, Repo-Root):
  python infrastructure/docker/deploy_flora_esf.py
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TEMPLATE = REPO / "infrastructure/docker/workspace-flora"
ESF = TEMPLATE / "learning/esf"
REMOTE = "user@docker-apps"
REMOTE_BASE = "/home/user/clawd/workspace-flora"
CORE_FILES = [
    "AGENTS.md",
    "SOUL.md",
    "USER.md",
    "WELCOME_MESSAGE.md",
    "HEARTBEAT.md",
    "CRON.md",
]


def run(cmd: list[str]) -> None:
    print(" ".join(cmd))
    subprocess.check_call(cmd)


def ssh(cmd: str) -> None:
    run(["ssh", REMOTE, cmd])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-hermes", action="store_true")
    ap.add_argument("--no-restart", action="store_true")
    args = ap.parse_args()

    if not ESF.exists():
        sys.exit(f"learning/esf fehlt: {ESF}")

    if args.dry_run:
        print(f"Deploy nach {REMOTE_BASE}: {CORE_FILES} + learning/esf/")
        return

    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp) / "stage"
        stage.mkdir()
        for f in CORE_FILES:
            src = TEMPLATE / f
            if src.exists():
                shutil.copy2(src, stage / f)
        shutil.copytree(
            ESF,
            stage / "learning" / "esf",
            ignore=shutil.ignore_patterns(".env", ".env.example"),
        )

        ssh(f"mkdir -p {REMOTE_BASE}")
        run(["scp", "-r", f"{stage}/.", f"{REMOTE}:{REMOTE_BASE}/"])

    if not args.no_hermes:
        files = " ".join(CORE_FILES)
        ssh(
            f"mkdir -p ~/.hermes/profiles/pilot/learning; "
            f"for f in {files}; do cp -a {REMOTE_BASE}/$f ~/.hermes/profiles/pilot/$f; done; "
            f"rm -rf ~/.hermes/profiles/pilot/learning/esf; "
            f"cp -a {REMOTE_BASE}/learning/esf ~/.hermes/profiles/pilot/learning/"
        )

    if not args.no_restart:
        ssh(
            "systemctl --user try-restart hermes-gateway-pilot 2>/dev/null; "
            "systemctl --user try-restart clawdbot-gateway-personal 2>/dev/null; true"
        )

    ssh(f"ls {REMOTE_BASE}/learning/esf; grep ESF {REMOTE_BASE}/AGENTS.md | head -3")
    print("Deploy fertig.")


if __name__ == "__main__":
    main()
