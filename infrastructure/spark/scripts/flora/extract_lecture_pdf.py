#!/usr/bin/env python3
"""
Flora-Lernskripte: PDF → strukturiertes Markdown.

Engines:
  pypdf   — lokal, schnell, schwach bei Scans/Spalten/Tabellen
  mineru  — auf Spark (GPU), Layout + Tabellen + OCR

Beispiele (auf Spark):
  python extract_lecture_pdf.py --pdf Vorlesung.pdf --out source/ --engine mineru --max-pages 12
  python extract_lecture_pdf.py --pdf Vorlesung.pdf --out source/ --engine pypdf

Von Windows (orchestriert Spark):
  python run_extract_on_spark.py --pdf path\\zu\\skript.pdf --subject neuro --max-pages 12
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path


def extract_pypdf(pdf: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SystemExit("pip install pypdf") from exc

    reader = PdfReader(str(pdf))
    parts = [f"# {pdf.stem}\n", f"_Engine: pypdf · {len(reader.pages)} Seiten_\n"]
    for i, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").strip()
        if not text:
            text = "_(kein extrahierbarer Text — Folie ggf. bildlastig)_"
        parts.append(f"\n## Seite {i}\n\n{text}\n")
    return "\n".join(parts)


def subset_pdf(pdf: Path, max_pages: int | None, work: Path) -> Path:
    if max_pages is None:
        return pdf
    try:
        import fitz
    except ImportError as exc:
        raise SystemExit("MinerU-Subset braucht PyMuPDF (fitz): pip install pymupdf") from exc

    doc = fitz.open(pdf)
    out = work / f"{pdf.stem}_first{max_pages}p.pdf"
    subset = fitz.open()
    for i in range(min(len(doc), max_pages)):
        subset.insert_pdf(doc, from_page=i, to_page=i)
    subset.save(out)
    subset.close()
    doc.close()
    return out


def find_markdown(root: Path) -> Path | None:
    mds = sorted(root.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return mds[0] if mds else None


def extract_mineru(
    pdf: Path,
    *,
    work: Path,
    mineru_bin: Path,
    backend: str,
    device: str,
    lang: str,
    method: str,
    max_pages: int | None,
) -> tuple[str, dict]:
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True, exist_ok=True)

    started = time.time()
    input_pdf = subset_pdf(pdf, max_pages, work)
    out_dir = work / "mineru_out"
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(mineru_bin),
        "-p",
        str(input_pdf),
        "-o",
        str(out_dir),
        "-b",
        backend,
        "--device",
        device,
        "--lang",
        lang,
        "-m",
        method,
    ]
    print("Running:", " ".join(cmd), flush=True)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    err_snip = (proc.stderr or proc.stdout or "").strip()[:1500]
    if proc.returncode != 0:
        raise RuntimeError(f"MinerU failed (rc={proc.returncode}): {err_snip}")

    md_path = find_markdown(out_dir)
    if md_path is None:
        raise RuntimeError(
            f"Kein Markdown unter {out_dir}"
            + (f"\n\nstderr/stdout:\n{err_snip}" if err_snip else "")
        )

    text = md_path.read_text(encoding="utf-8")
    header = f"# {pdf.stem}\n\n_Engine: mineru · backend={backend} · lang={lang}_\n\n"
    meta = {
        "engine": "mineru",
        "mineru_bin": str(mineru_bin),
        "pdf": str(pdf),
        "input_pdf": str(input_pdf),
        "backend": backend,
        "device": device,
        "lang": lang,
        "method": method,
        "max_pages": max_pages,
        "chars": len(text),
        "elapsed_seconds": round(time.time() - started, 2),
        "source_md": str(md_path),
    }
    return header + text, meta


def default_mineru_bin() -> Path:
    import os

    env = os.environ.get("MINERU_BIN", "").strip()
    if env:
        return Path(env)
    home = Path.home() / "srv/hd-worker/.venv/bin/mineru"
    which = shutil.which("mineru")
    if home.exists():
        return home
    if which:
        return Path(which)
    return home


def main() -> None:
    ap = argparse.ArgumentParser(description="Flora lecture PDF → Markdown")
    ap.add_argument("--pdf", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True, help="Output directory for .md")
    ap.add_argument("--engine", choices=("pypdf", "mineru"), default="pypdf")
    ap.add_argument("--max-pages", type=int, default=None)
    ap.add_argument("--mineru-bin", type=Path, default=None)
    ap.add_argument("--backend", default="pipeline", help="MinerU backend (Spark: pipeline)")
    ap.add_argument("--device", default="cpu", help="cpu (sicher neben SGLang) oder cuda")
    ap.add_argument("--lang", default="latin")
    ap.add_argument("--method", default="auto", choices=("auto", "txt", "ocr"))
    ap.add_argument("--compare", action="store_true", help="Auch pypdf schreiben (*_pypdf.md)")
    args = ap.parse_args()

    pdf = args.pdf.resolve()
    if not pdf.exists():
        raise SystemExit(f"PDF fehlt: {pdf}")

    out_dir = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = pdf.stem

    if args.engine == "pypdf" or args.compare:
        md = extract_pypdf(pdf)
        if args.max_pages:
            # rough page trim by ## Seite markers
            chunks = md.split("\n## Seite ")
            keep = [chunks[0]] + [
                f"\n## Seite {c}" for c in chunks[1 : args.max_pages + 1]
            ]
            md = "".join(keep)
        name = f"{stem}_pypdf.md" if args.compare or args.engine != "pypdf" else f"{stem}.md"
        path = out_dir / name
        path.write_text(md, encoding="utf-8")
        print(f"OK pypdf → {path} ({len(md)} chars)")

    if args.engine == "mineru":
        bin_path = args.mineru_bin or default_mineru_bin()
        if not bin_path.exists():
            raise SystemExit(f"MinerU CLI fehlt: {bin_path}")
        work = out_dir / f".work_{stem}"
        text, meta = extract_mineru(
            pdf,
            work=work,
            mineru_bin=bin_path,
            backend=args.backend,
            device=args.device,
            lang=args.lang,
            method=args.method,
            max_pages=args.max_pages,
        )
        path = out_dir / f"{stem}.md"
        path.write_text(text, encoding="utf-8")
        (out_dir / f"{stem}_mineru_meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"OK mineru → {path} ({meta['chars']} chars, {meta['elapsed_seconds']}s)")
        print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
