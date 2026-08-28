#!/usr/bin/env python3
"""
Orchestriert Flora-PDF-Extraktion auf Spark (MinerU GPU).

Von VM105 / Windows (Repo-Root):
  python infrastructure/spark/scripts/flora/run_extract_on_spark.py ^
    --pdf path\\zu\\Neuro_Skript.pdf --subject neuro --max-pages 15 --compare

Kopiert PDF → Spark, läuft extract_lecture_pdf.py (mineru), holt Markdown zurück
nach infrastructure/docker/workspace-flora/learning/<subject>/source/
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DEFAULT_HOST = "sparkuser@100.96.115.1"
DEFAULT_PORT = "2222"
REMOTE_WORK = "~/flora_extract"
REMOTE_SCRIPT = (
    "~/ai_projects/infrastructure/spark/scripts/flora/extract_lecture_pdf.py"
)
MINERU_BIN = "~/srv/hd-worker/.venv/bin/mineru"
VENV_PY = "~/srv/hd-worker/.venv/bin/python"


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)


def scp_to(local: Path, remote_spec: str, port: str) -> None:
    run(["scp", "-P", port, "-o", "StrictHostKeyChecking=accept-new", str(local), remote_spec])


def scp_from(remote_spec: str, local: Path, port: str) -> None:
    local.parent.mkdir(parents=True, exist_ok=True)
    run(["scp", "-P", port, "-o", "StrictHostKeyChecking=accept-new", remote_spec, str(local)])


def ssh(host: str, port: str, remote_cmd: str) -> None:
    run(["ssh", "-p", port, "-o", "StrictHostKeyChecking=accept-new", host, remote_cmd])


def main() -> None:
    ap = argparse.ArgumentParser(description="Flora PDF extract via Spark MinerU")
    ap.add_argument("--pdf", type=Path, required=True)
    ap.add_argument("--subject", default="neuro", help="learning/<subject>/source/")
    ap.add_argument("--max-pages", type=int, default=None)
    ap.add_argument("--compare", action="store_true", help="Zusätzlich pypdf-Output")
    ap.add_argument("--host", default=DEFAULT_HOST)
    ap.add_argument("--port", default=DEFAULT_PORT)
    ap.add_argument("--backend", default="pipeline")
    ap.add_argument(
        "--device",
        default="cpu",
        help="cuda wenn GPU frei; default cpu (Spark teilt GPU oft mit SGLang)",
    )
    ap.add_argument("--lang", default="latin")
    ap.add_argument("--method", default="auto", choices=("auto", "txt", "ocr"))
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Override local output dir",
    )
    args = ap.parse_args()

    pdf = args.pdf.resolve()
    if not pdf.exists():
        sys.exit(f"PDF fehlt: {pdf}")

    out_dir = args.out_dir or (
        REPO
        / "infrastructure/docker/workspace-flora/learning"
        / args.subject
        / "source"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    remote_dir = f"{REMOTE_WORK}/{date.today().isoformat()}_{pdf.stem}"
    remote_pdf = f"{remote_dir}/{pdf.name}"
    remote_out = f"{remote_dir}/out"

    ssh(args.host, args.port, f"mkdir -p {remote_dir}/out")
    # Script mitkopieren (Spark-Repo kann hinterherhinken)
    script_local = Path(__file__).resolve().parent / "extract_lecture_pdf.py"
    scp_to(script_local, f"{args.host}:{remote_dir}/extract_lecture_pdf.py", args.port)
    scp_to(pdf, f"{args.host}:{remote_pdf}", args.port)

    max_pages = f"--max-pages {args.max_pages}" if args.max_pages else ""
    compare = "--compare" if args.compare else ""
    remote_cmd = (
        f"{VENV_PY} {remote_dir}/extract_lecture_pdf.py "
        f"--pdf {remote_pdf} --out {remote_out} --engine mineru "
        f"--mineru-bin {MINERU_BIN} --backend {args.backend} "
        f"--device {args.device} --lang {args.lang} --method {args.method} "
        f"{max_pages} {compare}"
    )
    ssh(args.host, args.port, remote_cmd)

    stem = pdf.stem
    scp_from(f"{args.host}:{remote_out}/{stem}.md", out_dir / f"{stem}.md", args.port)
    meta = out_dir / f"{stem}_mineru_meta.json"
    try:
        scp_from(f"{args.host}:{remote_out}/{stem}_mineru_meta.json", meta, args.port)
    except subprocess.CalledProcessError:
        print("Hinweis: Meta-JSON nicht geholt", flush=True)
    if args.compare:
        try:
            scp_from(
                f"{args.host}:{remote_out}/{stem}_pypdf.md",
                out_dir / f"{stem}_pypdf.md",
                args.port,
            )
        except subprocess.CalledProcessError:
            print("Hinweis: pypdf-Vergleich nicht geholt", flush=True)

    print(f"Fertig -> {out_dir}")


if __name__ == "__main__":
    main()
