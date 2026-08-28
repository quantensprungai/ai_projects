"""Gemeinsame Aufbereitung von ESF-Markdown für PDF-Export (xhtml2pdf)."""
from __future__ import annotations

import re

# Unicode/Emoji → PDF-sicher (DejaVu hat keine Emojis, Subscripts oft kaputt)
CHAR_REPLACEMENTS: list[tuple[str, str]] = [
    ("H₀", "H0 (Nullhypothese)"),
    ("H₁", "H1 (Alternativhypothese)"),
    ("₀", "0"),
    ("₁", "1"),
    ("₂", "2"),
    ("≤", "<="),
    ("≥", ">="),
    ("→", "->"),
    ("✓", "[ja]"),
    ("✗", "[nein]"),
    ("⚠️", "Achtung:"),
    ("⚠", "Achtung:"),
    ("✅", "Ja:"),
    ("❌", "Nein:"),
    ("✏️", ""),
    ("📖", ""),
    ("­", ""),  # soft hyphen
]

# Abkürzungen beim ersten Vorkommen im Abschnitt erweitern (PDF-Lesbarkeit)
ABBREV_RULES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bESF\b"), "Empirische Sozialforschung (ESF)"),
    (re.compile(r"\bPT\b"), "Physiotherapie (PT)"),
    (re.compile(r"\bET\b"), "Ergotherapie (ET)"),
    (re.compile(r"\bRCT\b"), "Randomisierte kontrollierte Studie (RCT)"),
    (re.compile(r"\bADL\b"), "Aktivitäten des täglichen Lebens (ADL)"),
    (re.compile(r"\bEbM\b"), "Evidenzbasierte Medizin (EbM)"),
    (re.compile(r"\bVAS\b"), "Visuelle Analogskala (VAS)"),
    (re.compile(r"\bp-Wert\b", re.I), "p-Wert (Signifikanzwahrscheinlichkeit)"),
]

LERNKONTROLLE_RE = re.compile(
    r"\n##\s+Lernkontrolle:.*?(?=\n##\s+|\n---\s*\n|\Z)",
    re.DOTALL | re.IGNORECASE,
)
CHAPTER_H1_RE = re.compile(
    r"^#\s+(?:KAPITEL|Kapitel)\s+(\d+)[:\s]+(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
UEBUNGEN_H1_RE = re.compile(
    r"^#\s+(?:Übungen\s*[—–-]\s*|(?:\d+\s+)?ÜBUNGSAUFGABEN\s*[–-]\s*)(.+)$",
    re.IGNORECASE | re.MULTILINE,
)
NUMBERED_H1_RE = re.compile(r"^#\s+(\d+)\.\s+(.+)$")

H2_SPLIT_RE = re.compile(r'(?=<h2 class="section-title")')
H3_SPLIT_RE = re.compile(r'(?=<h3 class="subsection-title")')
TABLE_RE = re.compile(r"<table>.*?</table>", re.DOTALL)
LIST_RE = re.compile(r"<(ul|ol)>(.*?)</\1>", re.DOTALL)
FIRST_ROW_RE = re.compile(r"<tr>(.*?)</tr>", re.DOTALL)
CELL_RE = re.compile(r"<t[hd][^>]*>", re.IGNORECASE)

# Kurze Listen zusammenhalten; lange nummerierte Merkmalslisten separat behandeln
MAX_KEEP_TOGETHER_LIST_ITEMS = 8


def normalize_chapter_heading(line: str) -> str:
    """# 3. Titel -> # Kapitel 3: Titel (einheitlich für Woche 2)."""
    m = NUMBERED_H1_RE.match(line.strip())
    if m:
        return f"# Kapitel {m.group(1)}: {m.group(2).strip()}"
    return line


def dedupe_chapter_headings(text: str) -> str:
    """Erstes # Kapitel … behalten; Duplikate und ALL-CAPS-Doppel entfernen."""
    lines = text.splitlines()
    out: list[str] = []
    prev_h1_norm: str | None = None
    seen_chapter_nums: set[str] = set()
    in_chapter = False

    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            line = normalize_chapter_heading(line)
            norm = re.sub(r"\s+", " ", line[2:].strip().lower())
            num_m = re.search(r"kapitel\s+(\d+)", norm, re.I)
            chapter_num = num_m.group(1) if num_m else None
            if prev_h1_norm is not None and norm == prev_h1_norm:
                continue
            if chapter_num and chapter_num in seen_chapter_nums and in_chapter:
                continue
            if (
                chapter_num
                and re.match(r"^#\s+KAPITEL\s+\d+", line.strip(), re.I)
                and chapter_num in seen_chapter_nums
            ):
                continue
            if chapter_num:
                seen_chapter_nums.add(chapter_num)
                in_chapter = True
            prev_h1_norm = norm
            out.append(line)
            continue
        if line.strip() == "---" and out and out[-1].strip().startswith("# "):
            in_chapter = False
            prev_h1_norm = None
        out.append(line)
    return "\n".join(out).strip() + "\n"


def strip_lernkontrolle(text: str) -> str:
    """Lernkontrolle aus Lesetext entfernen — gehört zu Übungen/Sage, nicht in PDF-Inhalt."""
    return LERNKONTROLLE_RE.sub("", text).strip() + "\n"


def normalize_for_pdf(text: str) -> str:
    for old, new in CHAR_REPLACEMENTS:
        text = text.replace(old, new)
    # Doppelte Erklärungen H0 (Nullhypothese) (Nullhypothese) vermeiden
    text = re.sub(
        r"H0 \(Nullhypothese\) \(Nullhypothese\)",
        "H0 (Nullhypothese)",
        text,
    )
    text = re.sub(
        r"H1 \(Alternativhypothese\) \(Alternativhypothese\)",
        "H1 (Alternativhypothese)",
        text,
    )
    return text


def split_pdf_sections(md: str, doc_title: str) -> list[tuple[str, str]]:
    """Teilt MD in Abschnitte mit je einer Kopfzeile für alle Seiten des Abschnitts."""
    lines = md.splitlines()
    sections: list[tuple[str, str]] = []
    header = doc_title
    buf: list[str] = []

    def flush() -> None:
        nonlocal buf, header
        text = "\n".join(buf).strip()
        if text:
            sections.append((header, text))
        buf = []

    for line in lines:
        ch = CHAPTER_H1_RE.match(line)
        ub = UEBUNGEN_H1_RE.match(line)
        if ch or ub:
            flush()
            if ch:
                header = f"{doc_title} · Kapitel {ch.group(1)}: {ch.group(2).strip()}"
            else:
                header = f"{doc_title} · Übungen: {ub.group(1).strip()}"
        buf.append(line)
    flush()
    return sections if sections else [(doc_title, md)]


def preprocess_md_for_pdf(md: str, doc_title: str, *, exercises: bool = False) -> str:
    md = dedupe_chapter_headings(md)
    if not exercises:
        md = strip_lernkontrolle(md)
    md = normalize_for_pdf(md)
    return md.lstrip("\n")


def preprocess_section_md(section_md: str) -> str:
    """Pro PDF-Abschnitt Abkürzungen einmal auflösen."""
    expanded = section_md
    for pat, repl in ABBREV_RULES:
        if pat.search(expanded):
            expanded = pat.sub(repl, expanded, count=1)
    return expanded


def _table_shape(table_html: str) -> tuple[int, int]:
    first_row = FIRST_ROW_RE.search(table_html)
    cols = len(CELL_RE.findall(first_row.group(1))) if first_row else 0
    rows = table_html.count("<tr>")
    return cols, rows


def tag_smart_tables(html: str) -> str:
    """Vergleichstabellen zusammenhalten; nur breite Tabellen verkleinern und umbrechen."""

    def classify(match: re.Match[str]) -> str:
        table_html = match.group(0)
        cols, rows = _table_shape(table_html)
        if cols >= 5:
            css_class = "wide-table"
        elif cols >= 3 and rows <= 12:
            css_class = "comparison-table"
        elif rows <= 8:
            css_class = "compact-table"
        else:
            css_class = "tall-table"
        return table_html.replace("<table>", f'<table class="{css_class}">', 1)

    return TABLE_RE.sub(classify, html)


def tag_smart_lists(html: str) -> str:
    """Nur kurze Listen page-break-inside: avoid — lange Listen dürfen umbrechen."""

    def maybe_tag(match: re.Match[str]) -> str:
        tag_name = match.group(1)
        full = match.group(0)
        item_count = full.count("<li>")
        if item_count <= MAX_KEEP_TOGETHER_LIST_ITEMS:
            return full.replace(f"<{tag_name}>", f'<{tag_name} class="keep-together">', 1)
        return full

    return LIST_RE.sub(maybe_tag, html)


def _wrap_h3_blocks(h2_section: str) -> str:
    parts = H3_SPLIT_RE.split(h2_section)
    if len(parts) <= 1:
        return h2_section
    out: list[str] = [parts[0]]
    for part in parts[1:]:
        if not part.strip():
            continue
        if 'class="comparison-table"' in part:
            out.append(f'<div class="subsection-block comparison-subsection">{part}</div>')
        else:
            out.append(f'<div class="subsection-block">{part}</div>')
    return "".join(out)


def wrap_section_blocks(html: str) -> str:
    """h2-Abschnitte strukturieren; h3-Unterblöcke (Tabellen, 5-Merkmale-Listen) zusammenhalten."""
    segments = H2_SPLIT_RE.split(html)
    out: list[str] = []
    for seg in segments:
        if not seg.strip():
            continue
        if seg.startswith('<h2 class="section-title">Vertiefung'):
            seg = _wrap_h3_blocks(seg)
            out.append(f'<div class="section-block section-vertiefung">{seg}</div>')
        elif seg.startswith("<h2 "):
            seg = _wrap_h3_blocks(seg)
            out.append(f'<div class="section-block">{seg}</div>')
        else:
            out.append(seg)
    return "".join(out)


def enhance_html_breaks(html: str) -> str:
    """Überschriften, Tabellen und logische Unterabschnitte für saubere Seitenumbrüche aufbereiten."""
    html = html.replace("<h1>", '<h1 class="chapter-title">')
    html = html.replace("<h2>", '<h2 class="section-title">')
    html = html.replace("<h3>", '<h3 class="subsection-title">')
    html = tag_smart_tables(html)
    html = tag_smart_lists(html)
    return wrap_section_blocks(html)
