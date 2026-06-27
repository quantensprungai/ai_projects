#!/usr/bin/env python3
"""Run a single PDF through baidu/Unlimited-OCR for comparison with MinerU.

This script is intentionally not wired into the IC worker. It is a Spark-side
benchmark helper: convert PDF pages to images, run Unlimited-OCR, and keep all
outputs in a local experiment directory.
"""

from __future__ import annotations

import argparse
import json
import tempfile
import time
from pathlib import Path

import fitz
import torch
from transformers import AutoModel, AutoTokenizer


MODEL_NAME = "baidu/Unlimited-OCR"


def pdf_to_images(pdf_path: Path, dpi: int, max_pages: int | None) -> list[Path]:
    doc = fitz.open(pdf_path)
    tmp_dir = Path(tempfile.mkdtemp(prefix="unlimited_ocr_pdf_"))
    matrix = fitz.Matrix(dpi / 72, dpi / 72)
    paths: list[Path] = []

    page_count = len(doc) if max_pages is None else min(len(doc), max_pages)
    for index in range(page_count):
        out = tmp_dir / f"page_{index + 1:04d}.png"
        doc[index].get_pixmap(matrix=matrix).save(out)
        paths.append(out)

    doc.close()
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description="Unlimited-OCR PDF spike runner")
    parser.add_argument("--pdf", required=True, type=Path, help="Input PDF")
    parser.add_argument("--output-dir", required=True, type=Path, help="Output directory")
    parser.add_argument("--dpi", default=300, type=int, help="PDF render DPI")
    parser.add_argument("--max-pages", default=None, type=int, help="Limit pages for smoke tests")
    parser.add_argument("--max-length", default=32768, type=int, help="Generation max length")
    parser.add_argument("--ngram-window", default=1024, type=int, help="No-repeat ngram window")
    args = parser.parse_args()

    pdf_path = args.pdf.resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    started = time.time()
    image_paths = pdf_to_images(pdf_path, dpi=args.dpi, max_pages=args.max_pages)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    model = AutoModel.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
        use_safetensors=True,
        torch_dtype=torch.bfloat16,
    )
    model = model.eval().cuda()

    model.infer_multi(
        tokenizer,
        prompt="<image>Multi page parsing.",
        image_files=[str(path) for path in image_paths],
        output_path=str(output_dir),
        image_size=1024,
        max_length=args.max_length,
        no_repeat_ngram_size=35,
        ngram_window=args.ngram_window,
        save_results=True,
    )

    metadata = {
        "model": MODEL_NAME,
        "pdf": str(pdf_path),
        "output_dir": str(output_dir),
        "dpi": args.dpi,
        "pages": len(image_paths),
        "max_pages": args.max_pages,
        "max_length": args.max_length,
        "ngram_window": args.ngram_window,
        "elapsed_seconds": round(time.time() - started, 2),
        "cuda_device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
    }
    (output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
