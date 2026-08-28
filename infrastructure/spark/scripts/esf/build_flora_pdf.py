#!/usr/bin/env python3
"""
Erzeugt lesbare PDFs für Flora (iPad: Dateien-App, AirDrop, iCloud).

  python infrastructure/spark/scripts/esf/build_flora_pdf.py
  python infrastructure/spark/scripts/esf/build_flora_pdf.py --zip

Fokus: Lesen und Übungen getrennt, PDF-sichere Zeichen, laufende Kapitel-Kopfzeile.
"""
from __future__ import annotations

import argparse
import html as html_lib
import sys
import zipfile
from datetime import date
from io import BytesIO
from pathlib import Path

import markdown
from pypdf import PdfReader, PdfWriter
from xhtml2pdf import pisa

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flora_pdf_utils import (
    enhance_html_breaks,
    preprocess_md_for_pdf,
    preprocess_section_md,
    split_pdf_sections,
)

REPO = Path(__file__).resolve().parents[4]
ESF = REPO / "infrastructure/docker/workspace-flora/learning/esf"
PDF_DIR = ESF / "reader/pdf"

# (rel_md, pdf_name, doc_title, exercises_mode)
PDF_SOURCES: list[tuple[str, str, str, bool]] = [
    ("FLORA_START_HIER.md", "00_Start_hier.pdf", "ESF Start", False),
    ("reader/FLORA_ESF_WOCHE1_LESEN.md", "01_Woche1_Inhalt.pdf", "ESF Woche 1", False),
    ("reader/FLORA_ESF_WOCHE1_UEBUNGEN.md", "01b_Woche1_Uebungen.pdf", "ESF Woche 1", True),
    ("reader/FLORA_ESF_WOCHE2_LESEN.md", "02_Woche2_Inhalt.pdf", "ESF Woche 2", False),
    ("reader/FLORA_ESF_WOCHE2_UEBUNGEN.md", "02b_Woche2_Uebungen.pdf", "ESF Woche 2", True),
    ("PICO_PICOT_SPIDER.md", "03_PICO_PICOT_SPIDER.pdf", "PICO PICOT", False),
    ("reader/PHYSIOPRAXIS_ESF_2TEILER.md", "03b_Physiopraxis_2teiler.pdf", "Physiopraxis", False),
    ("source/Altfragen_Klausur_Natalie.md", "04_Altfragen_Klausur.pdf", "Altfragen", False),
    ("pruefung_simulation.md", "05_Probeklausur.pdf", "Probeklausur", True),
    ("glossary.md", "06_Glossar.pdf", "Glossar", False),
]

ZIP_FILES: list[str] = [
    "FLORA_START_HIER.md",
    "reader/FLORA_ESF_WOCHE1_LESEN.md",
    "reader/FLORA_ESF_WOCHE1_UEBUNGEN.md",
    "reader/FLORA_ESF_WOCHE2_LESEN.md",
    "reader/FLORA_ESF_WOCHE2_UEBUNGEN.md",
    "PICO_PICOT_SPIDER.md",
    "source/Altfragen_Klausur_Natalie.md",
    "pruefung_simulation.md",
    "glossary.md",
    "reader/pdf/00_Start_hier.pdf",
    "reader/pdf/01_Woche1_Inhalt.pdf",
    "reader/pdf/01b_Woche1_Uebungen.pdf",
    "reader/pdf/02_Woche2_Inhalt.pdf",
    "reader/pdf/02b_Woche2_Uebungen.pdf",
    "reader/pdf/03_PICO_PICOT_SPIDER.pdf",
    "reader/pdf/04_Altfragen_Klausur.pdf",
    "reader/pdf/05_Probeklausur.pdf",
    "reader/pdf/06_Glossar.pdf",
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8"/>
  <style>
    @page {{
      size: A4;
      margin: 2.9cm 2cm 2.5cm 2cm;
      @frame header {{
        -pdf-frame-content: chapterHeader;
        top: 0.55cm;
        margin-left: 2cm;
        margin-right: 2cm;
        height: 1.35cm;
      }}
      @frame footer {{
        -pdf-frame-content: footerContent;
        bottom: 0.65cm;
        margin-left: 2cm;
        margin-right: 2cm;
        height: 0.9cm;
      }}
    }}
    body {{
      font-family: DejaVu Sans, Helvetica, Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.45;
      color: #1a1a1a;
    }}
    #chapterHeader {{
      font-size: 8.5pt;
      color: #4a5568;
      border-bottom: 0.75pt solid #cbd5e0;
      padding-bottom: 3pt;
      font-weight: bold;
    }}
    h1.chapter-title {{
      font-size: 16pt;
      color: #1e3a5f;
      margin: 4pt 0 8pt 0;
      page-break-after: avoid;
      page-break-inside: avoid;
    }}
    h2.section-title {{
      font-size: 12.5pt;
      color: #2c5282;
      margin: 14pt 0 6pt 0;
      page-break-after: avoid;
      page-break-inside: avoid;
    }}
    h3.subsection-title {{
      font-size: 11pt;
      margin: 10pt 0 4pt 0;
      page-break-after: avoid;
      page-break-inside: avoid;
      -pdf-keep-with-next: true;
    }}
    h2.section-title + p,
    h2.section-title + ul,
    h2.section-title + ol,
    h2.section-title + table,
    h3.subsection-title + p,
    h3.subsection-title + ul,
    h3.subsection-title + ol,
    h3.subsection-title + table {{
      page-break-before: avoid;
    }}
    .section-block {{
      margin-bottom: 2pt;
    }}
    .section-vertiefung {{
      page-break-before: always;
    }}
    .subsection-block {{
      page-break-inside: avoid;
      margin-bottom: 6pt;
    }}
    .comparison-subsection {{
      page-break-before: always;
    }}
    .subsection-block > h3.subsection-title {{
      page-break-after: avoid;
      -pdf-keep-with-next: true;
    }}
    p, li {{ orphans: 3; widows: 3; }}
    p {{ margin: 0 0 6pt 0; }}
    ul, ol {{ margin: 4pt 0 8pt 0; padding-left: 16pt; }}
    ul.keep-together, ol.keep-together {{
      page-break-inside: avoid;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 8pt 0 12pt 0;
      font-size: 9pt;
      table-layout: fixed;
    }}
    table.compact-table,
    table.comparison-table {{
      page-break-inside: avoid;
    }}
    table.comparison-table tr {{
      page-break-inside: avoid;
    }}
    table.tall-table {{
      page-break-inside: auto;
    }}
    table.wide-table {{
      font-size: 7.5pt;
      page-break-inside: auto;
    }}
    th, td {{
      border: 1px solid #c5cdd8;
      padding: 4pt 5pt;
      vertical-align: top;
      word-wrap: break-word;
    }}
    table.wide-table th:first-child,
    table.wide-table td:first-child {{ width: 34%; }}
    th {{ background-color: #edf2f7; font-weight: bold; }}
    blockquote {{
      margin: 6pt 0 10pt 0;
      padding: 5pt 8pt;
      background: #edf2f7;
      border-left: 3pt solid #2c5282;
      font-size: 9.5pt;
      color: #2d3748;
      page-break-inside: avoid;
    }}
    blockquote.note {{
      background: #fffaf0;
      border-left-color: #dd6b20;
    }}
    pre {{
      background: #f4f6f8;
      padding: 8pt;
      border: 1px solid #e2e8f0;
      font-size: 9pt;
      white-space: pre-wrap;
      page-break-inside: avoid;
    }}
    hr {{ border: none; border-top: 1px solid #cbd5e0; margin: 10pt 0; }}
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


def md_to_html_body(section_md: str) -> str:
    section_md = preprocess_section_md(section_md)
    html = markdown.markdown(
        section_md,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )
    return enhance_html_breaks(html)


def render_section_pdf(header: str, section_md: str, footer: str) -> bytes:
    body = md_to_html_body(section_md)
    safe_header = html_lib.escape(header)
    safe_footer = html_lib.escape(footer)
    html = HTML_TEMPLATE.format(body=body, header=safe_header, footer=safe_footer)
    buf = BytesIO()
    status = pisa.CreatePDF(html, dest=buf, encoding="utf-8")
    if status.err:
        raise RuntimeError(f"PDF-Fehler Abschnitt «{header}»: {status.err}")
    return buf.getvalue()


def write_pdf(md_path: Path, pdf_path: Path, doc_title: str, exercises: bool) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    md_text = preprocess_md_for_pdf(md_text, doc_title, exercises=exercises)
    sections = split_pdf_sections(md_text, doc_title)
    footer = pdf_path.stem.replace("_", " ")

    writer = PdfWriter()
    for header, section_md in sections:
        chunk = render_section_pdf(header, section_md, footer)
        reader = PdfReader(BytesIO(chunk))
        for page in reader.pages:
            writer.add_page(page)

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with pdf_path.open("wb") as out:
        writer.write(out)


def build_zip() -> Path:
    zip_path = ESF / "flora_esf_ipad.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in ZIP_FILES:
            src = ESF / rel
            if not src.exists():
                print(f"  übersprungen (fehlt): {rel}")
                continue
            zf.write(src, arcname=f"ESF/{Path(rel).name}")
    return zip_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Flora ESF PDFs + optional ZIP")
    parser.add_argument("--zip", action="store_true", help="ZIP für iPad bauen")
    args = parser.parse_args()

    print(f"ESF PDF-Export ({date.today().isoformat()})")
    for rel_md, pdf_name, doc_title, exercises in PDF_SOURCES:
        md_path = ESF / rel_md
        pdf_path = PDF_DIR / pdf_name
        if not md_path.exists():
            print(f"  fehlt: {rel_md}")
            continue
        write_pdf(md_path, pdf_path, doc_title, exercises)
        size_kb = pdf_path.stat().st_size // 1024
        print(f"  OK  {pdf_name} ({size_kb} KB)")

    if args.zip:
        zip_path = build_zip()
        print(f"  ZIP {zip_path.name} ({zip_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
