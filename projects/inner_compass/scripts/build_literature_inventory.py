#!/usr/bin/env python3
"""Scan local Literatur folder and regenerate IC literature CSVs."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

SOURCE_ROOT = Path(
    r"C:\Users\he5013\Nextcloud\Hochschule\X. Eigenes\Human Design\App\Literatur"
)
REF_DIR = Path(__file__).resolve().parents[1] / "reference"
DATE_TAG = "2026-06-30"
MD5_RE = re.compile(r"[a-f0-9]{32}")

TOP_TO_SYSTEM = {
    "hd": "hd",
    "other_hd": "hd",
    "gene_keys": "genekeys",
    "I Ching": "i_ching",
    "astro": "astro",
    "bazi": "bazi",
    "chakra": "chakra",
    "joveish": "jyotish",
    "pancha_bhuta": "pancha_bhuta",
    "wu_xing": "wu_xing",
    "western_elements": "western_elements",
    "ziwei": "ziwei",
    "enneagram": "enneagram",
    "mayan_tzolkin": "mayan_tzolkin",
    "numerology": "numerology",
    "nine_star": "nine_star_ki",
    "akan": "akan",
    "archiv": "archiv",
}

# Curated gaps for AA manual search (not on disk)
AA_NEED = [
    {
        "curriculum_id": "hd.ra.rave_cosmology_iv",
        "system_id": "hd",
        "priority": "high",
        "target_author": "Ra Uru Hu",
        "target_title": "Rave Cosmology IV",
        "aa_search_query": "Ra Uru Hu Rave Cosmology IV",
        "k3_k4": "both",
    },
    {
        "curriculum_id": "hd.ra.rave_cosmology_v",
        "system_id": "hd",
        "priority": "high",
        "target_author": "Ra Uru Hu",
        "target_title": "Rave Cosmology V",
        "aa_search_query": "Ra Uru Hu Rave Cosmology V",
        "k3_k4": "both",
    },
    {
        "curriculum_id": "hd.ra.rave_cosmology_vi",
        "system_id": "hd",
        "priority": "high",
        "target_author": "Ra Uru Hu",
        "target_title": "Rave Cosmology VI",
        "aa_search_query": "Ra Uru Hu Rave Cosmology VI",
        "k3_k4": "both",
    },
    {
        "curriculum_id": "hd.ra.rave_cosmology_vii",
        "system_id": "hd",
        "priority": "high",
        "target_author": "Ra Uru Hu",
        "target_title": "Rave Cosmology VII",
        "aa_search_query": "Ra Uru Hu Rave Cosmology VII",
        "k3_k4": "both",
    },
    {
        "curriculum_id": "kab.jewish.zohar",
        "system_id": "kabbalah_jewish",
        "priority": "high",
        "target_author": "Various",
        "target_title": "The Zohar (English translation, e.g. Soncino or Matt)",
        "aa_search_query": "Zohar English translation",
        "k3_k4": "K4",
    },
    {
        "curriculum_id": "kab.jewish.meditation_kaplan",
        "system_id": "kabbalah_jewish",
        "priority": "high",
        "target_author": "Aryeh Kaplan",
        "target_title": "Meditation and Kabbalah",
        "aa_search_query": "Aryeh Kaplan Meditation and Kabbalah",
        "k3_k4": "K3",
    },
    {
        "curriculum_id": "chakra.judith.eastern_body",
        "system_id": "chakra",
        "priority": "medium",
        "target_author": "Anodea Judith",
        "target_title": "Eastern Body, Western Mind",
        "aa_search_query": "Anodea Judith Eastern Body Western Mind",
        "k3_k4": "K4",
    },
    {
        "curriculum_id": "i_ching.parkyn.book_of_lines",
        "system_id": "i_ching",
        "priority": "medium",
        "target_author": "Chetan Parkyn",
        "target_title": "The Book of Lines",
        "aa_search_query": "Chetan Parkyn Book of Lines Human Design",
        "k3_k4": "K3",
    },
    {
        "curriculum_id": "ziwei.wang_tingzhi.zhongzhou",
        "system_id": "ziwei",
        "priority": "high",
        "target_author": "王亭之",
        "target_title": "中州派紫微斗數 (系列)",
        "aa_search_query": "王亭之 紫微斗數",
        "k3_k4": "both",
    },
    {
        "curriculum_id": "enneagram.naranjo.character",
        "system_id": "enneagram",
        "priority": "high",
        "target_author": "Claudio Naranjo",
        "target_title": "Character and Neurosis",
        "aa_search_query": "Claudio Naranjo Character and Neurosis",
        "k3_k4": "K4",
    },
    {
        "curriculum_id": "enneagram.palmer.enneagram",
        "system_id": "enneagram",
        "priority": "medium",
        "target_author": "Helen Palmer",
        "target_title": "The Enneagram",
        "aa_search_query": "Helen Palmer Enneagram",
        "k3_k4": "K4",
    },
    {
        "curriculum_id": "numerology.pythagorean.core",
        "system_id": "numerology",
        "priority": "medium",
        "target_author": "Various",
        "target_title": "Pythagorean numerology reference (e.g. Decoz or classic)",
        "aa_search_query": "Pythagorean numerology handbook",
        "k3_k4": "K3",
    },
    {
        "curriculum_id": "mayan.tzolkin.gmt",
        "system_id": "mayan_tzolkin",
        "priority": "medium",
        "target_author": "Various",
        "target_title": "Tzolkin / Dreamspell reference (GMT or Argüelles)",
        "aa_search_query": "Tzolkin calendar Jose Arguelles",
        "k3_k4": "K3",
    },
    {
        "curriculum_id": "nine_star_ki.core",
        "system_id": "nine_star_ki",
        "priority": "low",
        "target_author": "Various",
        "target_title": "Nine Star Ki standard reference",
        "aa_search_query": "Nine Star Ki astrology",
        "k3_k4": "K3",
    },
]


def extract_md5(name: str) -> str:
    for m in MD5_RE.findall(name.lower()):
        return m
    return ""


def parse_title_author(filename: str) -> tuple[str, str]:
    stem = filename
    if " -- " in stem:
        parts = stem.split(" -- ", 1)
        return parts[0].strip(), parts[1].split(" -- ")[0].strip()
    return stem, ""


def resolve_system_id(rel: str) -> str:
    parts = Path(rel).parts
    top = parts[0]
    if top == "kabalah":
        if len(parts) > 1 and parts[1] == "kabbalah_hermetic":
            return "kabbalah_hermetic"
        if len(parts) > 1 and parts[1] == "kabbalah_jewish":
            return "kabbalah_jewish"
        # Sefer Yetzirah at kabalah root — dual-tag jewish primary
        return "kabbalah_jewish"
    mapped = TOP_TO_SYSTEM.get(top)
    if mapped:
        return mapped
    low = rel.lower()
    if "numerology" in low or "decoz" in low:
        return "numerology"
    return "unclassified"


def bucket_for(top: str, system_id: str) -> str:
    if top == "archiv":
        return "archiv"
    if top in ("hd", "other_hd"):
        return "hd_ra" if top == "hd" else "hd_other"
    return system_id


def is_ra_line(name: str) -> bool:
    n = name.lower()
    return any(
        k in n
        for k in (
            "ra uru hu",
            "ra uru",
            "jovian archive",
            "human design school",
            "ihds",
            "never mind",
            "book of letters",
            "die prophezeiung",
        )
    )


def infer_rolle(system_id: str, name: str, rel: str) -> str:
    if system_id == "unclassified":
        return "unknown"
    if system_id == "archiv":
        return "archiv_duplikat"
    n = name.lower()
    if system_id == "hd":
        if is_ra_line(name):
            return "K2_ref"
        if any(k in n for k in ("karen curry", "quantum human", "encyclopedia")):
            return "K3_deutung"
        if "robin winn" in n:
            return "K2_ref"
        if "richard rudd" in n and "gene" not in rel.lower():
            return "K3_deutung"
        return "K3_deutung"
    if system_id == "genekeys":
        return "K3_deutung"
    if "/K4/" in rel.replace("\\", "/") or rel.endswith("K4"):
        return "K4_deutung"
    if "/K3/" in rel.replace("\\", "/"):
        return "K3_deutung"
    if "K2+K3" in rel:
        return "K2_ref"
    if system_id in ("astro", "bazi", "i_ching", "jyotish", "kabbalah_jewish", "kabbalah_hermetic"):
        return "K2_ref"
    if system_id == "chakra":
        if "wheels of life" in n or "serpent power" in n:
            return "K2_ref"
        return "K3_deutung"
    if system_id in ("ziwei", "bazi", "jyotish"):
        return "K2_ref"
    if system_id == "enneagram":
        return "K4_deutung"
    if system_id in ("mayan_tzolkin", "numerology", "nine_star_ki"):
        return "K3_deutung"
    return "K2_ref"


def infer_status(system_id: str, name: str, top: str) -> str:
    if top == "archiv":
        return "archiv_duplikat"
    if system_id == "unclassified":
        return "manuell_pruefen"
    if "weiser" == name.lower().split(" -- ")[0].lower() or name.startswith("Weiser --"):
        return "manuell_pruefen"
    if "how do you choose" in name.lower():
        return "manuell_pruefen"
    return "ok"


def infer_passes(system_id: str, name: str, status: str, rolle: str) -> tuple[str, str, str, str]:
    if status in ("manuell_pruefen", "archiv_duplikat"):
        if status == "archiv_duplikat":
            return "skip", "skip", "skip", "Archiv-Duplikat — aktive Kopie in hd/ oder i_ching/ nutzen."
        return "manual_first", "manual_first", "manual_first", "Manuell pruefen vor Extraktion."

    if system_id == "hd" and is_ra_line(name):
        core = any(
            k in name.lower()
            for k in (
                "complete rave i'ching",
                "complete rave i'ching",
                "life force",
                "channels",
                "black book",
                "definitive book",
                "complete guide",
                "rave anatomy",
                "six lines",
                "incarnation cross",
            )
        )
        if core:
            return "yes", "yes", "yes", "Ra-Linie P0: drei Paesse."
        return "yes", "yes", "yes", "Ra-Linie: drei Paesse."

    if system_id == "hd":
        return "optional", "yes", "yes", "Nicht-Ra: K3/K4 priorisieren."

    if system_id == "genekeys":
        return "yes", "yes", "yes", "Gene Keys: K3/K4 Kern."

    if system_id in ("astro", "bazi", "i_ching", "jyotish", "pancha_bhuta", "wu_xing", "western_elements"):
        return "yes", "yes", "optional", "K2+K3 priorisieren; K4 optional."

    if system_id in ("kabbalah_jewish", "kabbalah_hermetic"):
        return "yes", "yes", "optional", "Tradition-Tag setzen; juedisch vs hermetisch nicht mischen."

    if system_id == "chakra":
        return "yes", "yes", "optional", "Tantra-Linie vs westliches Chakra unterscheiden."

    if system_id == "ziwei":
        return "yes", "yes", "yes", "Ziwei P0: 中州派-Serie + 星曜性质."

    if system_id == "enneagram":
        return "optional", "yes", "yes", "Enneagram: K4-Pass (Typen/Neurose)."

    if system_id == "mayan_tzolkin":
        return "yes", "yes", "optional", "Mayan/Tzolkin: K2/K3 priorisieren."

    if system_id == "numerology":
        return "yes", "yes", "optional", "Numerologie: K3-Kern."

    return "optional", "yes", "optional", ""


def load_legacy_passes() -> dict[str, dict]:
    legacy_path = REF_DIR / "literature_extraction_pass_plan_2026-05-07.csv"
    out: dict[str, dict] = {}
    if not legacy_path.exists():
        return out
    with legacy_path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            fn = row.get("filename", "")
            md5 = extract_md5(fn)
            key = md5 or fn.lower()
            out[key] = row
    return out


def scan_files() -> list[dict]:
    rows = []
    for fp in sorted(SOURCE_ROOT.rglob("*")):
        if not fp.is_file():
            continue
        rel = fp.relative_to(SOURCE_ROOT).as_posix()
        parts = Path(rel).parts
        top = parts[0] if parts else "(root)"
        name = fp.name
        md5 = extract_md5(name)
        title, author = parse_title_author(name)
        system_id = resolve_system_id(rel)
        bucket = bucket_for(top, system_id)
        rolle = infer_rolle(system_id, name, rel)
        status = infer_status(system_id, name, top)
        k2, k3, k4, notes = infer_passes(system_id, name, status, rolle)
        rows.append(
            {
                "relative_path": rel,
                "top_folder": top,
                "bucket": bucket,
                "filename": name,
                "extension": fp.suffix.lower(),
                "md5_annas": md5,
                "title_from_filename": title,
                "author_from_filename": author,
                "size_bytes": fp.stat().st_size,
                "system_id": system_id,
                "rolle": rolle,
                "format": fp.suffix.lstrip(".").lower() or "unknown",
                "size_mb": round(fp.stat().st_size / (1024 * 1024), 2),
                "status": status,
                "pass_k2_struct": k2,
                "pass_k3_rules": k3,
                "pass_k4_meanings": k4,
                "pass_notes": notes,
            }
        )
    return rows


def apply_legacy(rows: list[dict], legacy: dict[str, dict]) -> None:
    for row in rows:
        key = row["md5_annas"] or row["filename"].lower()
        old = legacy.get(key)
        if not old:
            continue
        if row["status"] == "ok" and old.get("status") == "ok":
            for field in ("pass_k2_struct", "pass_k3_rules", "pass_k4_meanings", "pass_notes"):
                if old.get(field):
                    row[field] = old[field]


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


def build_have_vs_need(rows: list[dict]) -> list[dict]:
    counts = Counter(r["system_id"] for r in rows if r["system_id"] != "archiv")
    # hd counts both hd folders already merged via system_id
    specs = [
        ("hd", "Ra + HD-Schulen", "vorhanden", "P0-Extraktion: Complete Rave I'Ching, Life Force, Black Book; Cosmology IV–VII fehlen."),
        ("genekeys", "Rudd Golden Path", "vorhanden", "14 Werke — Golden Path vollständig prüfen."),
        ("i_ching", "Wilhelm/Shaughnessy/Huang + Brücken", "vorhanden", "9 Werke inkl. Parkyn Book of Lines."),
        ("kabbalah_jewish", "Kaplan/Scholem/Idel", "vorhanden", "Zohar Matt Vol 1+2 + Kaplan Meditation and Kabbalah."),
        ("kabbalah_hermetic", "Fortune/Regardie/Crowley", "vorhanden", "5 Werke — Liber 777 Dublette behalten oder eine wählen."),
        ("chakra", "Serpent Power + Wheels of Life", "vorhanden", "12 Werke inkl. Eastern Body Western Mind."),
        ("pancha_bhuta", "Samkhya/Caraka/Sushruta/Ayurveda", "vorhanden", "5 Werke — Übersetzungslinie verifizieren."),
        ("wu_xing", "Neijing + Maciocia/Kaptchuk", "vorhanden", "4 Werke."),
        ("western_elements", "Antike Elementlehre", "vorhanden", "2 Werke (Aristoteles, Empedocles)."),
        ("jyotish", "Parashara / Brihat", "vorhanden", "4 Werke."),
        ("bazi", "Joey Yap + klassisch", "vorhanden", "31 Werke inkl. 滴天髓."),
        ("astro", "Lilly/Hand/Ptolemy/Rudhyar", "vorhanden", "6 Werke."),
        ("ziwei", "王亭之 / Schulanker", "vorhanden", "13 Werke — 中州派-Kern komplett."),
        ("mayan_tzolkin", "GMT/Kin", "teilweise", "Mayan Factor + Earth Ascending; optional Dreamspell-Kit."),
        ("nine_star_ki", "Kushi/Sachs", "vorhanden", "2 Kernwerke (Kushi 1991 + Sachs Complete Guide)."),
        ("numerology", "Grundwerke", "vorhanden", "Decoz + Goodwin Vol 1+2 + Jordan."),
        ("akan", "Gyekye/Rattray", "vorhanden", "3 Werke (Gyekye + Ashanti 1923 + Folk-tales)."),
        ("enneagram", "Riso/Naranjo/Palmer", "vorhanden", "Riso Personality Types + Wisdom; Naranjo Character + Structures."),
    ]
    result = []
    for sid, kern, habe_default, aktion in specs:
        n = counts.get(sid, 0)
        if n == 0:
            habe = "fehlt"
        elif sid in ("i_ching", "kabbalah_jewish", "chakra") and "fehlen" in aktion:
            habe = "teilweise"
        else:
            habe = habe_default if n > 0 else "fehlt"
        result.append(
            {
                "system_id": sid,
                "dateien_im_ordner": n,
                "kanon_kern_kurz": kern,
                "habe_vs_bedarf": habe,
                "nächste_aktion": aktion,
            }
        )
    return result


def reconcile_aa_need(rows: list[dict]) -> list[dict]:
    """Mark AA_NEED entries found when matching files exist on disk."""
    texts = " ".join(f"{r['relative_path']} {r['filename']}".lower() for r in rows)

    def has(*needles: str) -> bool:
        return all(n.lower() in texts for n in needles)

    checks: dict[str, tuple[bool, str]] = {
        "kab.jewish.zohar": (has("zohar") and has("matt"), "Matt Pritzker Vol 1+2 on disk."),
        "kab.jewish.meditation_kaplan": (
            has("meditation and kabbalah") and (has("kaplan") or has("weiser")),
            "",
        ),
        "chakra.judith.eastern_body": (has("eastern body") and has("western mind"), ""),
        "i_ching.parkyn.book_of_lines": (has("book of lines") and has("parkyn"), ""),
        "ziwei.wang_tingzhi.zhongzhou": (
            has("ziwei") and ("王亭之" in texts or has("中州派")),
            "13 files in ziwei/.",
        ),
        "enneagram.naranjo.character": (has("naranjo") and has("character and neurosis"), ""),
        "enneagram.palmer.enneagram": (has("palmer") and has("enneagram"), "1988 edition."),
        "numerology.pythagorean.core": (has("decoz") and has("numerology"), ""),
        "mayan.tzolkin.gmt": (has("mayan factor") or has("argüelles"), "Mayan Factor; GMT line optional."),
        "nine_star_ki.core": (
            has("nine star") and (has("kushi") or has("sachs")),
            "Kushi 1991 + Sachs Complete Guide on disk.",
        ),
        "akan.core": (has("gyekye") or has("rattray"), "Gyekye + Rattray Ashanti on disk."),
    }

    out = []
    for item in AA_NEED:
        row = {**item, "aa_coverage_status": "not_found", "notes": ""}
        cid = item["curriculum_id"]
        if cid in checks:
            found, note = checks[cid]
            if found:
                row["aa_coverage_status"] = "found"
                row["notes"] = note
        out.append(row)
    return out


def main() -> None:
    if not SOURCE_ROOT.is_dir():
        raise SystemExit(f"SOURCE_ROOT not found: {SOURCE_ROOT}")

    legacy = load_legacy_passes()
    rows = scan_files()
    apply_legacy(rows, legacy)

    inv_path = REF_DIR / f"literature_local_inventory_{DATE_TAG}.csv"
    matrix_path = REF_DIR / f"literature_download_matrix_{DATE_TAG}.csv"
    pass_path = REF_DIR / f"literature_extraction_pass_plan_{DATE_TAG}.csv"
    need_path = REF_DIR / f"literature_have_vs_need_{DATE_TAG}.csv"
    aa_path = REF_DIR / f"literature_aa_need_{DATE_TAG}.csv"
    meta_path = REF_DIR / f"literature_local_inventory_{DATE_TAG}.meta.json"

    write_csv(
        inv_path,
        [
            "relative_path",
            "top_folder",
            "bucket",
            "filename",
            "extension",
            "md5_annas",
            "title_from_filename",
            "author_from_filename",
            "size_bytes",
        ],
        rows,
    )

    matrix_rows = [
        {
            "filename": r["filename"],
            "relative_path": r["relative_path"],
            "system_id": r["system_id"],
            "rolle": r["rolle"],
            "format": r["format"],
            "size_mb": str(r["size_mb"]).replace(".", ","),
            "status": r["status"],
        }
        for r in rows
    ]
    write_csv(
        matrix_path,
        ["filename", "relative_path", "system_id", "rolle", "format", "size_mb", "status"],
        matrix_rows,
    )

    pass_rows = [
        {
            "filename": r["filename"],
            "relative_path": r["relative_path"],
            "system_id": r["system_id"],
            "status": r["status"],
            "pass_k2_struct": r["pass_k2_struct"],
            "pass_k3_rules": r["pass_k3_rules"],
            "pass_k4_meanings": r["pass_k4_meanings"],
            "pass_notes": r["pass_notes"],
        }
        for r in rows
    ]
    write_csv(
        pass_path,
        [
            "filename",
            "relative_path",
            "system_id",
            "status",
            "pass_k2_struct",
            "pass_k3_rules",
            "pass_k4_meanings",
            "pass_notes",
        ],
        pass_rows,
    )

    have_rows = build_have_vs_need(rows)
    write_csv(
        need_path,
        ["system_id", "dateien_im_ordner", "kanon_kern_kurz", "habe_vs_bedarf", "nächste_aktion"],
        have_rows,
    )

    aa_rows = reconcile_aa_need(rows)
    write_csv(
        aa_path,
        [
            "curriculum_id",
            "system_id",
            "priority",
            "target_author",
            "target_title",
            "aa_search_query",
            "k3_k4",
            "aa_coverage_status",
            "notes",
        ],
        aa_rows,
    )

    by_bucket = Counter(r["bucket"] for r in rows)
    by_system = Counter(r["system_id"] for r in rows)
    p0 = sum(
        1
        for r in rows
        if r["pass_k2_struct"] == "yes"
        and r["pass_k3_rules"] == "yes"
        and r["pass_k4_meanings"] == "yes"
        and r["status"] == "ok"
    )

    meta = {
        "source_root": str(SOURCE_ROOT),
        "inventory_csv": inv_path.name,
        "generated": DATE_TAG,
        "total_files": len(rows),
        "unique_md5": len({r["md5_annas"] for r in rows if r["md5_annas"]}),
        "file_counts_by_system_id": dict(sorted(by_system.items())),
        "file_counts_by_bucket": dict(sorted(by_bucket.items())),
        "extraction_p0_full_k234": p0,
        "aa_need_count": len(AA_NEED),
        "notes": [
            "Scan via build_literature_inventory.py + Get-ChildItem equivalent (pathlib rglob).",
            "SoT for PDFs: Nextcloud Literatur folder on this machine.",
            "archiv/ = duplicate editions — status archiv_duplikat, skip extraction.",
            "AA gaps: literature_aa_need_2026-06-30.csv",
        ],
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Scanned {len(rows)} files from {SOURCE_ROOT}")
    print(f"  inventory: {inv_path.name}")
    print(f"  matrix:    {matrix_path.name}")
    print(f"  pass plan: {pass_path.name}")
    print(f"  have/need: {need_path.name}")
    print(f"  aa need:   {aa_path.name} ({len(AA_NEED)} gaps)")
    print(f"  P0 K2+K3+K4 ok: {p0}")


if __name__ == "__main__":
    main()
