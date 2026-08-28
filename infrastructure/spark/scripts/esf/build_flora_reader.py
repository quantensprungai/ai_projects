#!/usr/bin/env python3
"""
Baut lesbare Dateien für Flora (Obsidian / PDF-Export).

  python infrastructure/spark/scripts/esf/build_flora_reader.py

Output:
  reader/FLORA_ESF_WOCHE1_LESEN.md      — nur Stoff
  reader/FLORA_ESF_WOCHE1_UEBUNGEN.md   — nur Übungen + Musterlösungen
  reader/FLORA_ESF_WOCHE2_LESEN.md
  reader/FLORA_ESF_WOCHE2_UEBUNGEN.md
  reader/FLORA_ESF_WOCHE1.md            — kombiniert (Obsidian, optional)
  reader/FLORA_ESF_WOCHE2.md
  reader/FLORA_ESF_KOMPAKT.md
  reader/PHYSIOPRAXIS_ESF_2TEILER.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flora_pdf_utils import dedupe_chapter_headings, strip_lernkontrolle

REPO = Path(__file__).resolve().parents[4]
ESF = REPO / "infrastructure/docker/workspace-flora/learning/esf"
READER = ESF / "reader"

WOCHE1_MODULES = [
    "02_kapitel_1_grundlagen_der_empirischen_soz",
    "03_kapitel_2_philosophische_grundlagen_und",
    "04_kapitel_3_theorien_hypothesen_und_variab",
    "06_kapitel_5_qualitative_forschungsmethoden",
    "07_kapitel_6_vergleich_quantitativ_qualitat",
    "08_kapitel_7_g_tekriterien_empirischer_fors",
    "11_kapitel_1_grundlagen_und_besonderheiten",
    "13_kapitel_3_formulierung_der_forschungsfra",
    "15_kapitel_5_datenanalyse_und_interpretatio",
]

WOCHE2_MODULES = [
    "19_2_forschungsdesigns_verstehen_und_unters",
    "20_3_variablen_operationalisierung_und_skal",
    "21_4_deskriptive_statistik_daten_zusammenfa",
    "22_5_bivariate_deskriptive_statistik_zusamm",
    "24_7_induktive_statistik_und_hypothesentest",
    "25_8_kritische_appraisal_und_interpretation",
]

PHYSIOPRAXIS_PARTS = [
    ("Teil 1 — Von der Beobachtung zur Forschungsfrage", "Physiopraxis_Teil1_Beobachtung_zur_Forschungsfrage.md"),
    ("Teil 2 — Zufall oder nicht", "Physiopraxis_Teil2_Zufall_oder_nicht.md"),
]

def chapter_title_from_module(text: str, stem: str) -> str:
    text = dedupe_chapter_headings(text)
    for line in text.splitlines():
        if not line.startswith("# "):
            continue
        title = line[2:].strip()
        if title.upper().startswith("KAPITEL "):
            return title  # „Kapitel 1: …"
        if title and title.lower() != "lernmodul":
            return title
    return stem.replace("_", " ")


def read_module_content(stem: str) -> str:
    mod = ESF / "modules" / f"{stem}.md"
    if not mod.exists():
        return ""
    text = mod.read_text(encoding="utf-8")
    text = dedupe_chapter_headings(text)
    text = strip_lernkontrolle(text).strip()
    return text


def read_exercises(stem: str) -> str:
    ex = ESF / "exercises" / f"{stem}.md"
    if not ex.exists():
        return ""
    text = ex.read_text(encoding="utf-8")
    # Einheitliche Überschrift: Kapitelname statt „3 ÜBUNGSAUFGABEN – …"
    mod = ESF / "modules" / f"{stem}.md"
    title = chapter_title_from_module(mod.read_text(encoding="utf-8"), stem) if mod.exists() else stem
    text = re.sub(
        r"^#\s+.*ÜBUNGSAUFGABEN.*$",
        f"# Übungen — {title}",
        text,
        count=1,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    return text.strip()


def build_lesen(title: str, stems: list[str], preamble: str) -> str:
    chunks = [f"# {title}\n", preamble, "\n---\n"]
    first = True
    for stem in stems:
        content = read_module_content(stem)
        if not content.strip():
            continue
        if not first:
            chunks.append("\n\n---\n\n")
        first = False
        chunks.append(content)
    return "\n".join(chunks)


def build_uebungen(title: str, stems: list[str]) -> str:
    chunks = [
        f"# {title} — Übungen\n",
        "Erst selbst versuchen, dann Musterlösung lesen. "
        "Bei „Erklär's zurück“-Fragen: Sage fragen oder laut erklären.\n",
        "\n---\n",
    ]
    first = True
    for stem in stems:
        content = read_exercises(stem)
        if not content.strip():
            continue
        if not first:
            chunks.append("\n\n---\n\n")
        first = False
        chunks.append(content)
    return "\n".join(chunks)


def build_combined(lesen: str, uebungen: str) -> str:
    return (
        lesen
        + "\n\n---\n\n# Übungen (dieses Paket)\n\n"
        + "Die Übungen stehen **am Ende jedes Kapitels** im PDF `*_Uebungen.pdf` "
        + "oder in der separaten Übungs-Datei — nicht nochmal hier doppelt.\n\n"
        + "---\n\n"
        + uebungen
    )


def build_physiopraxis() -> str:
    chunks = [
        "# Physiopraxis — Empirischer Forschungsprozess (2-teilig)\n",
        "Gleiches fiktives RCT (Schulterschmerz / Rotatorenmanschette). "
        "Optional — Woche 1/2 haben Vorrang.\n",
        "\n---\n",
    ]
    for part_title, rel in PHYSIOPRAXIS_PARTS:
        src = ESF / "source" / rel
        if not src.exists():
            continue
        chunks.append(f"\n\n---\n\n# {part_title}\n\n")
        chunks.append(src.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def main() -> None:
    READER.mkdir(parents=True, exist_ok=True)

    w1_lesen = build_lesen(
        "ESF Woche 1 — Grundlagen & Qualitativ (Lesen)",
        WOCHE1_MODULES,
        "Nur Stoff. Übungen: siehe `FLORA_ESF_WOCHE1_UEBUNGEN.md` oder PDF `01b_Woche1_Uebungen.pdf`.\n",
    )
    w1_ueb = build_uebungen("ESF Woche 1", WOCHE1_MODULES)
    w2_lesen = build_lesen(
        "ESF Woche 2 — Quantitativ (Lesen)",
        WOCHE2_MODULES,
        "Nur Stoff. Übungen: siehe `FLORA_ESF_WOCHE2_UEBUNGEN.md` oder PDF `02b_Woche2_Uebungen.pdf`.\n",
    )
    w2_ueb = build_uebungen("ESF Woche 2", WOCHE2_MODULES)

    (READER / "FLORA_ESF_WOCHE1_LESEN.md").write_text(w1_lesen, encoding="utf-8")
    (READER / "FLORA_ESF_WOCHE1_UEBUNGEN.md").write_text(w1_ueb, encoding="utf-8")
    (READER / "FLORA_ESF_WOCHE2_LESEN.md").write_text(w2_lesen, encoding="utf-8")
    (READER / "FLORA_ESF_WOCHE2_UEBUNGEN.md").write_text(w2_ueb, encoding="utf-8")

    # Kombiniert für Obsidian (Übungen separat angehängt, kein Modul+Übung-Mix pro Kapitel)
    (READER / "FLORA_ESF_WOCHE1.md").write_text(build_combined(w1_lesen, w1_ueb), encoding="utf-8")
    (READER / "FLORA_ESF_WOCHE2.md").write_text(build_combined(w2_lesen, w2_ueb), encoding="utf-8")

    physio = build_physiopraxis()
    if "Teil 1" in physio:
        (READER / "PHYSIOPRAXIS_ESF_2TEILER.md").write_text(physio, encoding="utf-8")

    glossar = ""
    g = ESF / "glossary.md"
    if g.exists():
        glossar = "\n\n---\n\n" + g.read_text(encoding="utf-8")

    pruef = ""
    p = ESF / "pruefung_simulation.md"
    if p.exists():
        pruef = "\n\n---\n\n# Anhang: Probeklausur\n\n" + p.read_text(encoding="utf-8")

    kompakt = (
        "# ESF — Flora Lesepaket (kompakt)\n\n"
        "Lesen und Übungen getrennt — siehe auch Einzel-PDFs.\n\n---\n\n"
        + w1_lesen
        + "\n\n---\n\n"
        + w1_ueb
        + "\n\n---\n\n"
        + w2_lesen
        + "\n\n---\n\n"
        + w2_ueb
        + glossar
        + pruef
    )
    (READER / "FLORA_ESF_KOMPAKT.md").write_text(kompakt, encoding="utf-8")

    print(f"Geschrieben: {READER}/")
    for name in (
        "FLORA_ESF_WOCHE1_LESEN.md",
        "FLORA_ESF_WOCHE1_UEBUNGEN.md",
        "FLORA_ESF_WOCHE2_LESEN.md",
        "FLORA_ESF_WOCHE2_UEBUNGEN.md",
        "FLORA_ESF_WOCHE1.md",
        "FLORA_ESF_WOCHE2.md",
        "FLORA_ESF_KOMPAKT.md",
    ):
        print(f"  {name}")
    if (READER / "PHYSIOPRAXIS_ESF_2TEILER.md").exists():
        print("  PHYSIOPRAXIS_ESF_2TEILER.md")


if __name__ == "__main__":
    main()
