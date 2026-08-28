#!/usr/bin/env python3
"""
ESF Lernmaterial lokal erzeugen (ohne Spark): PDF → Markdown → LLM-Module.

Voraussetzungen:
  pip install anthropic pypdf python-dotenv

API-Key (nicht ins Repo committen):
  infrastructure/docker/workspace-flora/learning/esf/.env
  oder Umgebungsvariable ANTHROPIC_API_KEY

Beispiele:
  python esf_local_pipeline.py extract
  python esf_local_pipeline.py all --dry-run
  python esf_local_pipeline.py all
  python esf_local_pipeline.py pruefung
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("pip install pypdf", file=sys.stderr)
    raise

REPO_ROOT = Path(__file__).resolve().parents[4]
ESF_DIR = REPO_ROOT / "infrastructure/docker/workspace-flora/learning/esf"
SOURCE_DIR = ESF_DIR / "source"
MODULES_DIR = ESF_DIR / "modules"
EXERCISES_DIR = ESF_DIR / "exercises"
CARDS_DIR = ESF_DIR / "cards"
ENV_FILE = ESF_DIR / ".env"

DEFAULT_PDF_DIR = Path.home() / "Downloads"
# Langdock Python-SDK: base OHNE /v1 (SDK hängt /v1/messages selbst an)
# https://docs.langdock.com/en/developer/completion-api/anthropic
LANGDOCK_EU_BASE = "https://api.langdock.com/anthropic/eu"
# Direkt Anthropic (console.anthropic.com)
ANTHROPIC_HAIKU = "claude-haiku-4-5"
ANTHROPIC_SONNET = "claude-sonnet-4-6"
# Langdock
LANGDOCK_HAIKU = "claude-haiku-4-5-default"
LANGDOCK_SONNET = "claude-sonnet-4-6-default"
DEFAULT_HAIKU = ANTHROPIC_HAIKU
DEFAULT_SONNET = ANTHROPIC_SONNET

PDF_PATTERNS = ("*ESF*", "*METHODEN*")

EXAM_CONTEXT = """
Prüfungsformat (verbindlich für Übungen und Prüfungssimulation):
- Dauer: 60–90 Minuten
- Umfang: ca. 20–25 Aufgaben
- Davon nur 1–3 Rechenaufgaben — Kopfrechnen OHNE Taschenrechner
- Erlaubte Kopfrechnen: ganze Zahlen, einfache Brüche/Prozente, Mittelwert aus 3–5 Zahlen, SD grob nur wenn sehr einfach
- Schwerpunkt: Begriffe, Zuordnung, Forschungslogik, Interpretation (p-Wert, Gütekriterien, Design), qualitative Schritte
- Kein SPSS/R, keine komplexen Formeln auswendig
"""

# Stems im Flora-Reader (Woche 1 + 2) — für gezielte Neu-Generierung
READER_STEMS: frozenset[str] = frozenset({
    "02_kapitel_1_grundlagen_der_empirischen_soz",
    "03_kapitel_2_philosophische_grundlagen_und",
    "04_kapitel_3_theorien_hypothesen_und_variab",
    "06_kapitel_5_qualitative_forschungsmethoden",
    "07_kapitel_6_vergleich_quantitativ_qualitat",
    "08_kapitel_7_g_tekriterien_empirischer_fors",
    "11_kapitel_1_grundlagen_und_besonderheiten",
    "13_kapitel_3_formulierung_der_forschungsfra",
    "15_kapitel_5_datenanalyse_und_interpretatio",
    "19_2_forschungsdesigns_verstehen_und_unters",
    "20_3_variablen_operationalisierung_und_skal",
    "21_4_deskriptive_statistik_daten_zusammenfa",
    "22_5_bivariate_deskriptive_statistik_zusamm",
    "24_7_induktive_statistik_und_hypothesentest",
    "25_8_kritische_appraisal_und_interpretation",
})

MODULE_SYSTEM = (
    "Erstelle ein Lernmodul zum SELBSTLESEN (ohne Tutor). Deutsch, sachlich, kein Motivations-Ton. "
    "Keine Emojis. Keine Sonderzeichen H₀/H₁ — schreibe H0 (Nullhypothese) und H1 (Alternativhypothese). "
    "Statistik: Interpretation vor Formel."
    + EXAM_CONTEXT
)

MODULE_USER_TEMPLATE = """Kapitel: {title}

ZWINGENDE Struktur:
## Kurz erklärt
4–6 Sätze Alltagssprache (wie eine gute Tutor-Antwort).

## PT-Beispiel
Ein konkretes Physiotherapie-Beispiel.

## Für die Prüfung
Listen und Zuordnungen vollständig (z.B. Deduktion/Induktion je 5 Merkmale wenn im Stoff).

## Vertiefung
Bullets/Tabellen — kompakt.

Outline:
{outline}

Quelle ({src_name}):
---
{src_text}
---

Max. 1200 Wörter. KEINE „Lernkontrolle“ / „Erklär-es-zurück“ am Ende (kommt in Übungen).
Bei Rechenbeispielen: nur Kopfrechnen-Niveau."""

EXERCISE_SYSTEM = (
    "Übungsaufgaben mit Musterlösung. Deutsch. Prüfungsnah. Keine Emojis. "
    "Keine H₀/H₁ — nutze H0 (Nullhypothese), H1 (Alternativhypothese)."
    + EXAM_CONTEXT
)


def load_env() -> None:
    if ENV_FILE.exists():
        try:
            from dotenv import load_dotenv

            load_dotenv(ENV_FILE, override=True)
        except ImportError:
            for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

    api_key = (os.environ.get("ANTHROPIC_API_KEY") or "").strip()
    is_direct_anthropic = api_key.startswith("sk-ant-")

    # Direkt-Anthropic-Key → Langdock-Reste ignorieren (häufiger Konfig-Fehler)
    if is_direct_anthropic and not os.environ.get("LANGDOCK_FORCE"):
        os.environ.pop("LANGDOCK_REGION", None)
        os.environ.pop("ANTHROPIC_BASE_URL", None)
        os.environ.setdefault("ESF_MODEL_HAIKU", ANTHROPIC_HAIKU)
        os.environ.setdefault("ESF_MODEL_SONNET", ANTHROPIC_SONNET)
    else:
        if os.environ.get("LANGDOCK", "").lower() in ("1", "true", "yes"):
            os.environ.setdefault("ANTHROPIC_BASE_URL", LANGDOCK_EU_BASE)
        region = (os.environ.get("LANGDOCK_REGION") or "").strip().lower()
        if region in ("eu", "us"):
            os.environ.setdefault(
                "ANTHROPIC_BASE_URL",
                f"https://api.langdock.com/anthropic/{region}",
            )
            os.environ.setdefault("ESF_MODEL_HAIKU", LANGDOCK_HAIKU)
            os.environ.setdefault("ESF_MODEL_SONNET", LANGDOCK_SONNET)


def find_pdfs(pdf_dir: Path) -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for pat in PDF_PATTERNS:
        for p in sorted(pdf_dir.glob(pat)):
            if p.suffix.lower() != ".pdf" or p in seen:
                continue
            seen.add(p)
            out.append(p)
    return out


def extract_pdf(pdf: Path) -> str:
    reader = PdfReader(str(pdf))
    parts = [f"# {pdf.stem}\n"]
    for i, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").strip()
        if not text:
            text = "_(kein extrahierbarer Text — Folie ggf. bildlastig)_"
        parts.append(f"\n## Folie {i}\n\n{text}\n")
    return "\n".join(parts)


def cmd_extract(pdf_dir: Path) -> list[Path]:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    pdfs = find_pdfs(pdf_dir)
    if not pdfs:
        print(f"Keine PDFs in {pdf_dir}", file=sys.stderr)
        sys.exit(1)
    written: list[Path] = []
    for pdf in pdfs:
        md = extract_pdf(pdf)
        out = SOURCE_DIR / f"{pdf.stem}.md"
        out.write_text(md, encoding="utf-8")
        chars = len(md)
        pages = md.count("## Folie ")
        safe_print(f"  {pdf.name} -> {out.name} ({pages} Folien, {chars} Zeichen)")
        written.append(out)
    return written


def list_sources() -> list[Path]:
    if not SOURCE_DIR.exists():
        return []
    return sorted(SOURCE_DIR.glob("*.md"))


def truncate(text: str, max_chars: int = 90_000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n_(… gekürzt für API-Limit …)_\n"


def get_client():
    api_key = (os.environ.get("ANTHROPIC_API_KEY") or "").strip()
    if not api_key:
        print(
            f"ANTHROPIC_API_KEY fehlt. Lege {ENV_FILE} an (siehe .env.example).",
            file=sys.stderr,
        )
        sys.exit(1)
    try:
        from anthropic import Anthropic
    except ImportError:
        print("Fehlt: pip install anthropic python-dotenv", file=sys.stderr)
        print("Danach erneut (extract schon da): ... esf_local_pipeline.py all --skip-extract", file=sys.stderr)
        sys.exit(1)
    base_url = (os.environ.get("ANTHROPIC_BASE_URL") or "").strip() or None
    kwargs: dict = {"api_key": api_key}
    if base_url:
        base_url = base_url.rstrip("/")
        if base_url.endswith("/v1"):
            base_url = base_url[:-3]
        kwargs["base_url"] = base_url + "/"
        kwargs["default_headers"] = {"Authorization": f"Bearer {api_key}"}
    return Anthropic(**kwargs)


def cmd_list_models() -> None:
    """Verfügbare Langdock-Modelle auflisten (GET /anthropic/{region}/v1/models)."""
    import urllib.request

    api_key = (os.environ.get("ANTHROPIC_API_KEY") or "").strip()
    if not api_key:
        print("ANTHROPIC_API_KEY fehlt.", file=sys.stderr)
        sys.exit(1)
    if api_key.startswith("sk-ant-") and not os.environ.get("ANTHROPIC_BASE_URL"):
        print(
            "Direkt-Anthropic: list-models nicht nötig.\n"
            f"  Haiku: {os.environ.get('ESF_MODEL_HAIKU', ANTHROPIC_HAIKU)}\n"
            f"  Sonnet: {os.environ.get('ESF_MODEL_SONNET', ANTHROPIC_SONNET)}",
        )
        return
    base = (os.environ.get("ANTHROPIC_BASE_URL") or LANGDOCK_EU_BASE).rstrip("/")
    if base.endswith("/v1"):
        base = base[:-3]
    url = f"{base}/v1/models"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "anthropic-version": "2023-06-01",
        },
    )
    print(f"GET {url}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
    except Exception as e:
        print(f"Fehler: {e}", file=sys.stderr)
        sys.exit(1)
    try:
        data = json.loads(body)
        for m in data.get("data", data.get("models", [data])):
            if isinstance(m, dict):
                print(f"  {m.get('id', m)}")
            else:
                print(f"  {m}")
    except json.JSONDecodeError:
        print(body[:2000])


def cmd_test_auth(client, model: str) -> None:
    """Minimaler API-Test vor teurem Batch."""
    print(f"Auth-Test: model={model}")
    base = (os.environ.get("ANTHROPIC_BASE_URL") or "").strip()
    if base:
        base = base.rstrip("/")
        if base.endswith("/v1"):
            base = base[:-3]
        print(f"  base_url={base}/  (SDK -> {base}/v1/messages)")
    else:
        print("  base_url=https://api.anthropic.com (Direkt-Anthropic)")
    try:
        msg = client.messages.create(
            model=model,
            max_tokens=16,
            messages=[{"role": "user", "content": "Antworte nur: OK"}],
        )
        text = "".join(b.text for b in msg.content if hasattr(b, "text"))
        print(f"  OK — Antwort: {text.strip()!r}")
    except Exception as e:
        err = str(e)
        print(f"  FEHLER: {err}", file=sys.stderr)
        if "401" in err or "authentication" in err.lower():
            print(
                "\n401 = Key wird abgelehnt. Häufige Ursachen:\n"
                "  1) Langdock: LANGDOCK_REGION=eu + ANTHROPIC_BASE_URL (siehe .env.example)\n"
                "  2) Key abgelaufen/widerrufen — neuen Key erzeugen\n"
                "  3) Direkt-Anthropic braucht Key von console.anthropic.com (sk-ant-api03-...)\n"
                "  4) Modell-ID passt nicht zum Gateway (ESF_MODEL_HAIKU in .env prüfen)\n"
                "\nTest:\n"
                "  python esf_local_pipeline.py test-auth --haiku <deine-modell-id>\n",
                file=sys.stderr,
            )
        sys.exit(1)


def call_llm(
    client,
    model: str,
    system: str,
    user: str,
    max_tokens: int = 8192,
    dry_run: bool = False,
) -> str:
    if dry_run:
        preview = user[:400].replace("\n", " ")
        print(f"  [dry-run] {model}: {preview}…")
        return f"_(dry-run output for {model})_"
    msg = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in msg.content if hasattr(b, "text"))


def parse_chapters(outline_md: str) -> list[dict]:
    chapters: list[dict] = []
    current: dict | None = None
    for line in outline_md.splitlines():
        if line.startswith("## ") and not line.startswith("### "):
            if current:
                chapters.append(current)
            title = line[3:].strip()
            must = "[NICE]" not in title.upper() and "NICE" not in line.upper()
            if "[MUST]" in title.upper():
                must = True
                title = re.sub(r"\[MUST\]", "", title, flags=re.I).strip()
            if "[NICE]" in title.upper():
                must = False
                title = re.sub(r"\[NICE\]", "", title, flags=re.I).strip()
            current = {"title": title, "must": must, "body": []}
        elif current is not None:
            current["body"].append(line)
    if current:
        chapters.append(current)
    return chapters


def slugify(title: str, idx: int) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", title.lower())[:40].strip("_")
    return f"{idx:02d}_{s or 'kapitel'}"


def cmd_outline(client, model: str, sources: list[Path], dry_run: bool) -> dict[str, str]:
    outlines: dict[str, str] = {}
    system = (
        "Du strukturierst Vorlesungsfolien für ein 2-Wochen-Lernprogramm "
        "Empirische Sozialforschung (Physiotherapie-Studium). Deutsch, präzise."
        + EXAM_CONTEXT
    )
    for src in sources:
        text = truncate(src.read_text(encoding="utf-8"))
        user = f"""Gliedere dieses Deck in 5–8 Kapitel.

Pro Kapitel:
- ### Lernziele (2–4, Verben: erklären, unterscheiden, anwenden, beurteilen)
- Tag [MUST] oder [NICE] — MUST = für Prüfung + 2-Wochen-Plan nötig
- ### Prüfungsfallen (2–3 Bulletpoints)

Deck: {src.stem}

---
{text}
---

Format: ## Kapitel-Titel [MUST|NICE]"""
        print(f"Outline: {src.name} …")
        out = call_llm(client, model, system, user, dry_run=dry_run)
        out_path = ESF_DIR / f"outline_{src.stem}.md"
        out_path.write_text(out, encoding="utf-8")
        outlines[src.stem] = out
        print(f"  -> {out_path.name}")
        time.sleep(0.5)
    return outlines


def pick_source_for_chapter(title: str, sources: list[Path]) -> Path:
    t = title.lower()
    if any(w in t for w in ("quant", "statist", "skalen", "hypothes", "p-wert", "p wert")):
        for s in sources:
            if "QUANTITATIVE" in s.stem.upper():
                return s
    if any(w in t for w in ("qualit", "interview", "kodier", "fgd", "fokus")):
        for s in sources:
            if "QUALITATIVE" in s.stem.upper():
                return s
    for s in sources:
        if "EINF" in s.stem.upper() or "EINFÜHRUNG" in s.stem.upper():
            return s
    return sources[0]


def cmd_status() -> None:
    modules = list(MODULES_DIR.glob("*.md")) if MODULES_DIR.exists() else []
    cards = list(CARDS_DIR.glob("*.jsonl")) if CARDS_DIR.exists() else []
    exercises = list(EXERCISES_DIR.glob("*.md")) if EXERCISES_DIR.exists() else []
    safe_print(f"Outlines:     {len(list(ESF_DIR.glob('outline_*.md')))}")
    safe_print(f"Module:       {len(modules)}")
    safe_print(f"Karten:       {len(cards)}")
    safe_print(f"Uebungen:     {len(exercises)}")
    safe_print(f"Glossar:      {(ESF_DIR / 'glossary.md').exists()}")
    safe_print(f"Probeklausur: {(ESF_DIR / 'pruefung_simulation.md').exists()}")


def cmd_modules(
    client,
    haiku: str,
    sonnet: str,
    sources: list[Path],
    dry_run: bool,
    must_only: bool = True,
    skip_existing: bool = False,
    only_reader: bool = False,
) -> None:
    MODULES_DIR.mkdir(parents=True, exist_ok=True)
    outline_files = sorted(ESF_DIR.glob("outline_*.md"))
    if not outline_files:
        print("Keine outline_*.md — zuerst: esf_local_pipeline.py outline", file=sys.stderr)
        sys.exit(1)

    idx = 0
    for of in outline_files:
        outline_md = of.read_text(encoding="utf-8")
        chapters = parse_chapters(outline_md)
        for ch in chapters:
            if must_only and not ch["must"]:
                continue
            idx += 1
            title = ch["title"]
            slug = slugify(title, idx)
            src = pick_source_for_chapter(title, sources)
            src_text = truncate(src.read_text(encoding="utf-8"), 60_000)
            if only_reader and slug not in READER_STEMS:
                continue
            quant = "QUANTITATIVE" in src.stem.upper() or any(
                w in title.lower() for w in ("statist", "hypothes", "skalen", "quant")
            )
            model = sonnet if (quant or slug in READER_STEMS) else haiku
            user = MODULE_USER_TEMPLATE.format(
                title=title,
                outline="".join(ch["body"]),
                src_name=src.name,
                src_text=src_text,
            )
            out_path = MODULES_DIR / f"{slug}.md"
            if skip_existing and out_path.exists() and out_path.stat().st_size > 400:
                print(f"  skip (exists): {slug}")
                continue
            print(f"Modul [{model}]: {slug} …")
            body = call_llm(client, model, MODULE_SYSTEM, user, dry_run=dry_run)
            out_path.write_text(f"# {title}\n\n{body}", encoding="utf-8")
            time.sleep(0.5)


def cmd_cards(client, model: str, dry_run: bool, skip_existing: bool = False) -> None:
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    for mod in sorted(MODULES_DIR.glob("*.md")):
        text = mod.read_text(encoding="utf-8")
        title = mod.stem
        system = "Karteikarten für ESF-Prüfung. Deutsch. JSONL only."
        user = f"""8–10 Karteikarten. Eine Zeile pro Karte, JSONL:
{{"front":"...","back":"...","tags":["esf","{title}"]}}

Fokus Prüfung: Begriffe, Zuordnung, Interpretation — wenig Formeln.
{EXAM_CONTEXT}

Modul:
---
{text}
---"""
        out_path = CARDS_DIR / f"{mod.stem}.jsonl"
        if skip_existing and out_path.exists() and out_path.stat().st_size > 50:
            print(f"  skip (exists): {mod.name}")
            continue
        print(f"Karten: {mod.name} …")
        out = call_llm(client, model, system, user, max_tokens=4096, dry_run=dry_run)
        out_path.write_text(out.strip() + "\n", encoding="utf-8")
        time.sleep(0.3)


def cmd_exercises(
    client,
    model: str,
    dry_run: bool,
    skip_existing: bool = False,
    only_reader: bool = False,
) -> None:
    EXERCISES_DIR.mkdir(parents=True, exist_ok=True)
    for mod in sorted(MODULES_DIR.glob("*.md")):
        if only_reader and mod.stem not in READER_STEMS:
            continue
        text = mod.read_text(encoding="utf-8")
        user = f"""3 Übungen (steigende Schwierigkeit) + Musterlösung + häufiger Fehler.

Überschrift: # Übungen — [Kapiteltitel aus Modul]
Keine breiten 5-Spalten-Tabellen für Zuordnungsaufgaben — lieber nummerierte Teilfragen a) b) c).

Mix: Zuordnung, Mini-Fall, Interpretation.
Max. 1 Aufgabe mit Kopfrechnen (nur wenn Modul quantitativ) — ohne Taschenrechner lösbar!

Modul:
---
{text}
---"""
        out_path = EXERCISES_DIR / f"{mod.stem}.md"
        if skip_existing and out_path.exists() and out_path.stat().st_size > 100:
            print(f"  skip (exists): {mod.name}")
            continue
        print(f"Übungen: {mod.name} …")
        out = call_llm(client, model, EXERCISE_SYSTEM, user, dry_run=dry_run)
        out_path.write_text(out, encoding="utf-8")
        time.sleep(0.3)


def cmd_glossary(client, model: str, sources: list[Path], dry_run: bool) -> None:
    combined = "\n\n".join(truncate(s.read_text(encoding="utf-8"), 30_000) for s in sources)
    system = "Fachglossar ESF. Deutsch, prüfungsfest."
    user = f"""Glossar: 25–40 Begriffe. Pro Begriff:
**Begriff** — Definition (1–2 Sätze); Abgrenzung; Mini-Beispiel Physio-Forschung

{EXAM_CONTEXT}

Quellen:
---
{combined}
---"""
    print("Glossar …")
    out = call_llm(client, model, system, user, max_tokens=8192, dry_run=dry_run)
    (ESF_DIR / "glossary.md").write_text(f"# ESF Glossar\n\n{out}", encoding="utf-8")
    print("  -> glossary.md")


def cmd_pruefung(client, sonnet: str, dry_run: bool) -> None:
    modules = "\n\n---\n\n".join(
        m.read_text(encoding="utf-8") for m in sorted(MODULES_DIR.glob("*.md"))
    )
    glossary = (ESF_DIR / "glossary.md").read_text(encoding="utf-8") if (ESF_DIR / "glossary.md").exists() else ""
    system = (
        "Prüfungssimulation ESF. Realistisch, fair, ohne Trickfragen."
        + EXAM_CONTEXT
    )
    user = f"""Erstelle eine **Probeklausur** (Markdown):

1. Deckblatt: Dauer 60–90 Min, 20–25 Aufgaben, Hilfsmittel: kein Taschenrechner
2. Genau **20–25 nummerierte Aufgaben** (Mix MC, Kurzantwort, Zuordnung, Mini-Fall)
3. Davon **genau 2 Rechenaufgaben** — Kopfrechnen (z. B. Mittelwert aus 4 Zahlen, einfacher Prozentsatz)
4. Rest: Interpretation, Begriffe, Forschungslogik, qual + quant
5. Am Ende: **Musterlösungen** (kompakt, nummeriert)

Basis:
{truncate(modules, 50_000)}

Glossar:
{truncate(glossary, 15_000)}
"""
    print(f"Prüfungssimulation [{sonnet}] …")
    out = call_llm(client, sonnet, system, user, max_tokens=12000, dry_run=dry_run)
    (ESF_DIR / "pruefung_simulation.md").write_text(out, encoding="utf-8")
    print("  -> pruefung_simulation.md")


def safe_print(msg: str) -> None:
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("ascii", errors="replace").decode("ascii"))


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    load_env()
    ap = argparse.ArgumentParser(description="ESF local learning pipeline")
    ap.add_argument(
        "step",
        choices=[
            "extract",
            "test-auth",
            "list-models",
            "outline",
            "modules",
            "cards",
            "exercises",
            "glossary",
            "pruefung",
            "resume",
            "status",
            "all",
        ],
    )
    ap.add_argument("--pdf-dir", type=Path, default=DEFAULT_PDF_DIR)
    ap.add_argument("--haiku", default=os.environ.get("ESF_MODEL_HAIKU", DEFAULT_HAIKU))
    ap.add_argument("--sonnet", default=os.environ.get("ESF_MODEL_SONNET", DEFAULT_SONNET))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-extract", action="store_true", help="PDF-Extraktion überspringen (source/ existiert)")
    ap.add_argument(
        "--skip-existing",
        action="store_true",
        help="vorhandene Module/Karten/Uebungen nicht neu generieren",
    )
    ap.add_argument("--include-nice", action="store_true", help="auch NICE-Kapitel als Module")
    ap.add_argument(
        "--only-reader",
        action="store_true",
        help="nur die 15 Flora-Reader-Stems (Woche 1+2) neu generieren",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="mit --only-reader: vorhandene Module/Übungen dieser Stems löschen",
    )
    args = ap.parse_args()

    if args.force and args.only_reader:
        delete_dirs: list[Path] = []
        if args.step in ("modules", "all", "resume"):
            delete_dirs.append(MODULES_DIR)
        if args.step in ("exercises", "all", "resume"):
            delete_dirs.append(EXERCISES_DIR)
        for d in delete_dirs:
            for stem in READER_STEMS:
                p = d / f"{stem}.md"
                if p.exists():
                    p.unlink()
                    safe_print(f"  gelöscht: {p.name}")

    safe_print(f"ESF output: {ESF_DIR}")

    if args.step in ("extract", "all") and not (
        args.skip_extract and args.step == "all"
    ):
        cmd_extract(args.pdf_dir)

    sources = list_sources()
    if args.step == "status":
        cmd_status()
        return

    if args.step not in ("extract", "test-auth") and not sources:
        print("Keine source/*.md — zuerst extract.", file=sys.stderr)
        sys.exit(1)

    client = None if args.step == "extract" else get_client()

    if args.step == "list-models":
        cmd_list_models()
        return

    if args.step == "test-auth":
        cmd_test_auth(client, args.haiku)
        return

    if args.step in ("outline", "all"):
        cmd_outline(client, args.haiku, sources, args.dry_run)

    skip = args.skip_existing or args.step == "resume"

    if args.step in ("modules", "all", "resume"):
        cmd_modules(
            client,
            args.haiku,
            args.sonnet,
            sources,
            args.dry_run,
            must_only=not args.include_nice,
            skip_existing=skip and not args.force,
            only_reader=args.only_reader,
        )

    if args.step in ("cards", "all", "resume"):
        if not list(MODULES_DIR.glob("*.md")) and args.step == "cards":
            print("Keine modules/ — zuerst modules oder all.", file=sys.stderr)
            sys.exit(1)
        cmd_cards(client, args.haiku, args.dry_run, skip_existing=skip)

    if args.step in ("exercises", "all", "resume"):
        if not list(MODULES_DIR.glob("*.md")) and args.step == "exercises":
            print("Keine modules/", file=sys.stderr)
            sys.exit(1)
        cmd_exercises(
            client,
            args.sonnet,
            args.dry_run,
            skip_existing=skip and not args.force,
            only_reader=args.only_reader,
        )

    if args.step in ("glossary", "all", "resume"):
        cmd_glossary(client, args.haiku, sources, args.dry_run)

    if args.step in ("pruefung", "all", "resume"):
        if not list(MODULES_DIR.glob("*.md")):
            print("Keine modules/ für Prüfung.", file=sys.stderr)
            sys.exit(1)
        cmd_pruefung(client, args.sonnet, args.dry_run)

    if args.step == "resume":
        cmd_status()

    print("Fertig.")


if __name__ == "__main__":
    main()
