#!/usr/bin/env python3
"""Run a single PDF through MinerU for comparison with Unlimited-OCR.

Creates an optional page-limited PDF subset, invokes the MinerU CLI, and
collects metadata for A/B benchmarking. Not wired into the IC worker.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path


def subset_pdf(pdf_path: Path, max_pages: int | None, work_dir: Path) -> Path:
    if max_pages is None:
        return pdf_path

    import fitz

    doc = fitz.open(pdf_path)
    out = work_dir / f"{pdf_path.stem}_first{max_pages}p.pdf"
    subset = fitz.open()
    for index in range(min(len(doc), max_pages)):
        subset.insert_pdf(doc, from_page=index, to_page=index)
    subset.save(out)
    subset.close()
    doc.close()
    return out


def find_markdown(output_dir: Path) -> Path | None:
    candidates = sorted(output_dir.rglob("*.md"))
    return candidates[0] if candidates else None


def main() -> None:
    parser = argparse.ArgumentParser(description="MinerU PDF spike runner")
    parser.add_argument("--pdf", required=True, type=Path, help="Input PDF")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory")
    parser.add_argument("--max-pages", default=None, type=int, help="Limit pages for smoke tests")
    parser.add_argument(
        "--mineru-bin",
        default=None,
        help="Path to mineru CLI (default: MINERU_BIN env or ~/srv/hd-worker/.venv/bin/mineru)",
    )
    parser.add_argument("--backend", default="hybrid-auto-engine")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--lang", default="latin")
    args = parser.parse_args()

    pdf_path = args.pdf.resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    output_dir = args.output_dir.resolve()
    work_dir = output_dir / ".work"
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    mineru_bin = Path(
        args.mineru_bin
        or __import__("os").environ.get("MINERU_BIN", "")
        or Path.home() / "srv/hd-worker/.venv/bin/mineru"
    )
    if not mineru_bin.exists():
        raise FileNotFoundError(f"MinerU CLI not found: {mineru_bin}")

    started = time.time()
    input_pdf = subset_pdf(pdf_path, args.max_pages, work_dir)

    cmd = [
        str(mineru_bin),
        "-p",
        str(input_pdf),
        "-o",
        str(work_dir),
        "-b",
        args.backend,
        "--device",
        args.device,
        "--lang",
        args.lang,
    ]
    print("Running:", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)

    md_path = find_markdown(work_dir)
    if md_path is None:
        raise RuntimeError(f"No markdown output found under {work_dir}")

    final_md = output_dir / "result.md"
    shutil.copy2(md_path, final_md)

    metadata = {
        "engine": "mineru",
        "mineru_bin": str(mineru_bin),
        "pdf": str(pdf_path),
        "input_pdf": str(input_pdf),
        "output_dir": str(output_dir),
        "backend": args.backend,
        "device": args.device,
        "lang": args.lang,
        "max_pages": args.max_pages,
        "result_md": str(final_md),
        "elapsed_seconds": round(time.time() - started, 2),
    }
    (output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
