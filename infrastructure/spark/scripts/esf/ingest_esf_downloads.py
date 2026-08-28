#!/usr/bin/env python3
"""
Neue Quellen aus Downloads in den ESF-Stack übernehmen.

  python infrastructure/spark/scripts/esf/ingest_esf_downloads.py

Übernimmt (wenn vorhanden):
  - Physiopraxis 2-teiler (Pflicht-Ergänzung)
  - Aufgabe EP-dual (.bin = PDF)
  - optional/QUELLEN_BEWERTUNG.md für übrige Dateien
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[4]
ESF = REPO / "infrastructure/docker/workspace-flora/learning/esf"
SOURCE = ESF / "source"
OPTIONAL = SOURCE / "optional"
DOWNLOADS = Path.home() / "Downloads"

INGEST: list[tuple[Path, str]] = [
    (DOWNLOADS / "Von der Beobachtung zur Forschungsfrage.pdf", "Physiopraxis_Teil1_Beobachtung_zur_Forschungsfrage.md"),
    (DOWNLOADS / "Zufall oder nicht_2021.pdf", "Physiopraxis_Teil2_Zufall_oder_nicht.md"),
    (DOWNLOADS / "Aufgabe EP-dual_.bin", "Aufgabe_EP_dual_Gruppenpraesentation.md"),
]

SKIP_LINES = (
    "heruntergeladen von",
    "thieme. all rights",
    "wissenschaft | empirischer forschungsprozess",
    "bit.ly/glossar",
    "glossar_physio",
    "kostenlos zum download",
    "bakhtiarzein",
    "www.thieme-connect",
    "www.thieme",
)


def extract_pdf(pdf: Path, title: str) -> str:
    reader = PdfReader(str(pdf))
    parts = [f"# {title}\n", "_Quelle: physiopraxis (Thieme), Hochschule Osnabrück._\n"]
    for i, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").strip()
        if text:
            parts.append(f"\n## Seite {i}\n\n{text}\n")
    return "\n".join(parts)


def clean_physiopraxis(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    skip_block = False
    for line in lines:
        low = line.lower().strip()
        if any(s in low for s in SKIP_LINES):
            continue
        if re.match(r"^physiopraxis\s+\d", low):
            continue
        if re.match(r"^©\s", line.strip()):
            continue
        if low.startswith("erklärungen zu allen mit der lupe"):
            skip_block = True
            continue
        if skip_block and (low.startswith("a-z") or low == "10" or low == "11"):
            continue
        if skip_block and line.strip() and not low.startswith("→"):
            if len(line.strip()) > 40:
                skip_block = False
            else:
                continue
        if re.match(r"^\d{1,2}$", line.strip()):
            continue
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    SOURCE.mkdir(parents=True, exist_ok=True)
    OPTIONAL.mkdir(parents=True, exist_ok=True)

    for src, dest_name in INGEST:
        if not src.exists():
            print(f"  fehlt: {src.name}")
            continue
        if dest_name.startswith("Physiopraxis"):
            title = dest_name.replace(".md", "").replace("_", " ")
            raw = extract_pdf(src, title)
            md = clean_physiopraxis(raw)
        else:
            raw = extract_pdf(src, "Aufgabe EP-dual — Gruppenpräsentation")
            md = raw
        out = SOURCE / dest_name
        out.write_text(md, encoding="utf-8")
        print(f"  OK  {dest_name} ({len(md)} Zeichen)")

    bewertung = OPTIONAL / "QUELLEN_BEWERTUNG.md"
    bewertung.write_text(
        """# ESF — Bewertung weiterer Downloads

Stand: automatisch bei `ingest_esf_downloads.py`.

## Im Stack integriert (Pflicht-Leseergänzung)

| Datei | Rolle |
|-------|-------|
| `Physiopraxis_Teil1_Beobachtung_zur_Forschungsfrage.md` | Forschungsprozess, PICOT, H0/H1, Studiendesigns (RCT-Beispiel Schulter) |
| `Physiopraxis_Teil2_Zufall_oder_nicht.md` | Deskriptive/induktive Statistik, p-Wert, t-Test, Typ-1/2-Fehler — **gleiches RCT** |

→ Lesen als `reader/PHYSIOPRAXIS_ESF_2TEILER.md` (mit PICO-Schritt bzw. Woche 2).

## Referenz (nicht Klausur-Pflicht)

| Original (Downloads) | Einschätzung | Empfehlung |
|---------------------|--------------|------------|
| `Aufgabe EP-dual_.bin` | **Ist ein PDF** (falsche Endung). Aufgabenstellung **Gruppenpräsentation** (4 Artikel aus ILIAS, 15–20 Min) — **kein Klausurformat** | `source/Aufgabe_EP_dual_Gruppenpraesentation.md` für Sage; Flora nur wenn Gruppenauftrag ansteht |
| `Original Research … Knee Conditions.pdf` | Englischer **Volltext-RCT** (Digital-App vs. konventionelle PT, n=60). Gut zum **Artikel zerlegen** (Einleitung/Methode/Ergebnisse), **nicht** für Definitionen/Zuordnung in der ESF-Klausur | In `optional/` belassen; nutzen wenn einer der 4 ILIAS-Artikel für die Gruppenpräsentation |
| `Occupational Therapy_ALZHEIMER_2020.pdf` | **Ergotherapie**, Alzheimer/Demenz — anderes Fach, anderes Outcome. Für ESF-Klausur (PT, Methoden) **kaum relevant** | Ignorieren, außer explizit als ILIAS-Artikel vorgegeben |

## Kurzentscheidung

- **Klausur:** Physiopraxis-2teiler + Reader + Altfragen + PICO
- **Gruppenpräsentation EP-dual:** Aufgaben-PDF + einer der englischen Volltexte (falls in ILIAS)
- **Alzheimer/OT:** nur bei konkreter Vorgabe, sonst weglassen
""",
        encoding="utf-8",
    )
    print(f"  OK  optional/QUELLEN_BEWERTUNG.md")

    for tmp in SOURCE.glob("_preview_*"):
        tmp.unlink(missing_ok=True)
        print(f"  del {tmp.name}")


if __name__ == "__main__":
    main()
