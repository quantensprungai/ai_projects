#!/usr/bin/env python3
"""
Pilot-PDFs: ESF als Geschichte (Flora + Sage).

  python infrastructure/spark/scripts/esf/build_flora_story_pdf.py
  python infrastructure/spark/scripts/esf/build_flora_story_pdf.py --zip
"""
from __future__ import annotations

import argparse
import html as html_lib
import re
import sys
import zipfile
from datetime import date
from io import BytesIO
from pathlib import Path

import markdown
from xhtml2pdf import pisa

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flora_pdf_utils import enhance_html_breaks, normalize_for_pdf

REPO = Path(__file__).resolve().parents[4]
ESF = REPO / "infrastructure/docker/workspace-flora/learning/esf"
STORY_DIR = ESF / "geschichte"
PDF_DIR = STORY_DIR / "pdf"

STORY_SOURCES: list[tuple[str, str, str]] = [
    ("test_a_deduktion.md", "Test_A_Der_Westfluegel.pdf", "ESF Geschichte · Test A"),
    ("test_b_pico_pwert.md", "Test_B_PICO_pWert.pdf", "ESF Geschichte · Test B"),
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8"/>
  <style>
    @page {{
      size: A4;
      margin: 2.6cm 2cm 2.2cm 2cm;
      @frame header {{
        -pdf-frame-content: chapterHeader;
        top: 0.5cm;
        margin-left: 2cm;
        margin-right: 2cm;
        height: 1.1cm;
      }}
      @frame footer {{
        -pdf-frame-content: footerContent;
        bottom: 0.55cm;
        margin-left: 2cm;
        margin-right: 2cm;
        height: 0.8cm;
      }}
    }}
    body {{
      font-family: DejaVu Sans, Helvetica, Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.5;
      color: #1a1a1a;
    }}
    #chapterHeader {{
      font-size: 8.5pt;
      color: #4a5568;
      border-bottom: 0.75pt solid #cbd5e0;
      padding-bottom: 3pt;
      font-weight: bold;
    }}
    h1 {{
      font-size: 17pt;
      color: #1e3a5f;
      margin: 0 0 4pt 0;
      page-break-after: avoid;
    }}
    em.subtitle {{
      font-style: italic;
      color: #4a5568;
      font-size: 9.5pt;
    }}
    p {{ margin: 0 0 8pt 0; orphans: 3; widows: 3; }}
    hr {{
      border: none;
      border-top: 1px solid #e2e8f0;
      margin: 14pt 0;
    }}
    strong {{ color: #2c5282; }}
    .merkblock-dezent {{
      margin-top: 16pt;
      padding: 10pt 12pt;
      background: #f7fafc;
      border-left: 3pt solid #718096;
      font-size: 9.5pt;
      page-break-inside: avoid;
    }}
    .merkblock-exam {{
      margin-top: 16pt;
      padding: 10pt 12pt;
      background: #edf2f7;
      border-left: 3pt solid #2c5282;
      font-size: 9pt;
      page-break-inside: avoid;
    }}
    .merkblock-dezent table,
    .merkblock-exam table {{
      width: 100%;
      border-collapse: collapse;
      margin: 8pt 0;
      font-size: 8.5pt;
      table-layout: fixed;
    }}
    .merkblock-exam th, .merkblock-exam td {{
      border: 1px solid #c5cdd8;
      padding: 4pt 5pt;
      vertical-align: top;
      word-wrap: break-word;
    }}
    .merkblock-exam th {{
      background: #e2e8f0;
      font-weight: bold;
    }}
    #footerContent {{
      font-size: 8pt;
      color: #718096;
      text-align: center;
    }}
  </style>
</head>
<body>
{body}
<div id="chapterHeader">{header}</div>
<div id="footerContent">{footer}</div>
</body>
</html>
"""


def md_to_html(md_text: str) -> str:
    md_text = normalize_for_pdf(md_text)
    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )
    return enhance_html_breaks(html)


def write_story_pdf(md_path: Path, pdf_path: Path, header: str) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    body = md_to_html(md_text)
    footer = pdf_path.stem.replace("_", " ")
    html = HTML_TEMPLATE.format(
        body=body,
        header=html_lib.escape(header),
        footer=html_lib.escape(footer),
    )
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    buf = BytesIO()
    status = pisa.CreatePDF(html, dest=buf, encoding="utf-8")
    if status.err:
        raise RuntimeError(f"PDF-Fehler {md_path.name}: {status.err}")
    pdf_path.write_bytes(buf.getvalue())


def build_zip() -> Path:
    zip_path = ESF / "flora_esf_geschichte_test.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for _, pdf_name, _ in STORY_SOURCES:
            src = PDF_DIR / pdf_name
            if src.exists():
                zf.write(src, arcname=f"ESF_Geschichte/{pdf_name}")
    return zip_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Flora ESF Story-Pilot-PDFs")
    parser.add_argument("--zip", action="store_true")
    args = parser.parse_args()

    print(f"ESF Story-PDF ({date.today().isoformat()})")
    for md_name, pdf_name, header in STORY_SOURCES:
        md_path = STORY_DIR / md_name
        pdf_path = PDF_DIR / pdf_name
        if not md_path.exists():
            print(f"  fehlt: {md_name}")
            continue
        write_story_pdf(md_path, pdf_path, header)
        size_kb = pdf_path.stat().st_size // 1024
        print(f"  OK  {pdf_name} ({size_kb} KB)")

    if args.zip:
        zip_path = build_zip()
        print(f"  ZIP {zip_path.name} ({zip_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
