#!/usr/bin/env python3
"""Build literature_content_wave_queue — structure-first, not alphabetical.

Orientation (NOT K1 runtime charts):
  1. K2 catalog layers / subsystem priority (bodygraph → PHS → optional)
  2. Registry download_priority_order (canonical → commentaries → schools)
  3. Werk-Typ Rolle (K2_ref → K3 → K4)
  4. System priority (active systems first)

All status=ok works stay in scope; waves sequence processing only.
"""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

REF = Path(__file__).resolve().parents[1] / "reference"
DATE = "2026-07-18"

DONE_MARKERS = [
    "Complete Rave",
    "Rave I'Ching",
    "Rave I’Ching",
    "Life Force",
    "64 Ways",
    "Opening Doors with Gene Keys",
    "Destiny Code COMBINED",
    "Destiny Code Combined",
]

SYS_PRIO = {
    s: i
    for i, s in enumerate(
        [
            "hd",
            "bazi",
            "genekeys",
            "ziwei",
            "astro",
            "jyotish",
            "i_ching",
            "wu_xing",
            "kabbalah_jewish",
            "kabbalah_hermetic",
            "chakra",
            "enneagram",
            "numerology",
            "mayan_tzolkin",
            "nine_star_ki",
            "akan",
            "pancha_bhuta",
            "western_elements",
        ]
    )
}

# Lower = earlier. Matches hd_catalog_v0.json subsystems + deep_structure_plan layers.
# Bodygraph pedagogy ≈ K2 seed dependency (catalog layers), not K1 chart runtime.
# Already done: Rave I'Ching (gates/lines), Life Force (channels) → next deepen same layers.
HD_LAYER_RULES: list[tuple[int, str, list[str]]] = [
    (8, "bodygraph_types", ["generator book", "living your design", "design concepts", "how to read a graph"]),
    (10, "bodygraph_channels", ["channels by type", "life force", "the channels"]),
    (12, "bodygraph_gates_lines", ["rave i'ching", "rave i’ching", "line companion", "book of lines", "384 linien", "die 384", "line resonance", "many faces of fear", "roads and tunnels"]),
    (14, "bodygraph_centers", ["nine centres", "nine centers", "understanding the centers", "the centres", "centers in human"]),
    (16, "bodygraph_circuits", ["bodygraph circuitry", "circuitry", "circuits", "keynotes"]),
    (20, "bodygraph_profiles", ["profile", "incarnation cross"]),
    (30, "phs", ["variable", "phs", "primary health", "lunar & planetary color", "color analysis", "variablen"]),
    (35, "rave_psychology", ["not-self", "not self", "conditioning", "open center"]),
    (50, "schools", ["quantum", "parkyn", "curry", "science of differentiation", "revelation", "jenna"]),
    (70, "teaching", ["student manual", "facilitator", "understanding your clients"]),
    (80, "dream_rave", ["dreamrave", "dream rave"]),
    (85, "bg5", ["bg5", "business consulting", "career and business"]),
    (90, "design_of_forms", ["biology design", "design of forms", "resonance mapping", "way of the flesh"]),
    (95, "cosmology", ["cosmology", "prophezeiung", "prophecy", "global cycles", "sociology", "penta"]),
]

BAZI_LAYER_RULES: list[tuple[int, str, list[str]]] = [
    (10, "classics_ziping", ["子平真诠", "滴天髓", "三命通会", "渊海子平", "ziping", "di tian", "san ming"]),
    (20, "ten_gods", ["10 gods", "ten gods", "十神", "power of x"]),
    (30, "stems_branches", ["heavenly stem", "earthly branch", "jiazi", "六十甲子", "nayin", "纳音"]),
    (40, "structures", ["useful god", "yong shen", "day master", "ri zhu", "structures", "geju"]),
    (50, "luck_timing", ["da yun", "大运", "luck pillar", "luck cycle", "annual"]),
    (60, "modern_overview", ["destiny code", "joey yap", "ba zi", "bazi"]),
    (70, "commentaries", ["评注", "阐微", "千里"]),
]

GK_LAYER_RULES: list[tuple[int, str, list[str]]] = [
    (10, "keys_spectrum", ["64 ways", "gene keys", "shadow", "gift", "siddhi"]),
    (20, "golden_path", ["activation", "venus sequence", "pearl", "golden path"]),
    (30, "codon_rings", ["codon", "ring of"]),
    (40, "bridge_hd", ["human design", "circuitry", "revelation"]),
]

ASTRO_LAYER_RULES: list[tuple[int, str, list[str]]] = [
    (10, "classical_structure", ["tetrabiblos", "ptolemy", "dorotheus", "valens"]),
    (20, "traditional_practice", ["lilly", "christian astrology", "demetra", "ancient astrology"]),
    (30, "modern", ["rudhyar", "hand", "planets in transit", "personality"]),
]

ZIWEI_LAYER_RULES: list[tuple[int, str, list[str]]] = [
    (10, "stars_palaces", ["紫微", "ziwei", "zi wei", "palace", "star"]),
    (20, "classics", ["斗数", "doushu"]),
    (30, "modern", []),
]

JYOTISH_LAYER_RULES: list[tuple[int, str, list[str]]] = [
    (10, "grahas_rashis", ["brihat", "parashara", "graha", "rashi"]),
    (20, "nakshatra", ["nakshatra", "pada"]),
    (30, "dashas_yogas", ["dasha", "yoga", "vimshottari"]),
    (40, "modern", []),
]

SYSTEM_RULES = {
    "hd": HD_LAYER_RULES,
    "bazi": BAZI_LAYER_RULES,
    "genekeys": GK_LAYER_RULES,
    "astro": ASTRO_LAYER_RULES,
    "ziwei": ZIWEI_LAYER_RULES,
    "jyotish": JYOTISH_LAYER_RULES,
}


def is_done(r: dict) -> bool:
    fn = f"{r['filename']} {r['relative_path']}"
    return any(d.lower() in fn.lower() for d in DONE_MARKERS)


def rolle_rank(rolle: str) -> int:
    return {"K2_ref": 1, "K3_deutung": 2, "K4_deutung": 3}.get(rolle, 9)


def structure_layer(system_id: str, filename: str, relative_path: str) -> tuple[int, str]:
    text = f"{filename} {relative_path}".lower()
    rules = SYSTEM_RULES.get(system_id, [])
    best = (60, "general")
    for layer, name, needles in rules:
        if not needles and layer == best[0]:
            continue
        if any(n.lower() in text for n in needles):
            if layer < best[0]:
                best = (layer, name)
    # Path folder hints (K2/K3/K4) as weak signal if still general
    if best[1] == "general":
        path = relative_path.lower()
        if "/k2/" in path:
            best = (25, "path_k2")
        elif "/k2+k3/" in path:
            best = (35, "path_k2k3")
        elif "/k3/" in path:
            best = (45, "path_k3")
        elif "/k4/" in path:
            best = (55, "path_k4")
    return best


def main() -> None:
    plan = list(
        csv.DictReader(open(REF / f"literature_extraction_pass_plan_{DATE}.csv", encoding="utf-8"))
    )
    matrix = {
        r["relative_path"]: r
        for r in csv.DictReader(
            open(REF / f"literature_download_matrix_{DATE}.csv", encoding="utf-8")
        )
    }

    ok = [r for r in plan if r["status"] == "ok"]
    scored: list[tuple] = []
    for r in ok:
        m = matrix.get(r["relative_path"], {})
        rolle = m.get("rolle", "")
        layer, layer_name = structure_layer(r["system_id"], r["filename"], r["relative_path"])
        done = is_done(r)
        scored.append(
            (
                0 if done else 1,  # done first as wave 0
                SYS_PRIO.get(r["system_id"], 99),
                layer,
                rolle_rank(rolle),
                r["relative_path"],
                r,
                m,
                layer_name,
                done,
            )
        )

    scored.sort(key=lambda x: x[:5])

    fields = [
        "wave",
        "queue_order",
        "system_id",
        "structure_layer",
        "structure_layer_name",
        "rolle",
        "status_pipeline",
        "filename",
        "relative_path",
        "pass_k2_struct",
        "pass_k3_rules",
        "pass_k4_meanings",
        "pass_notes",
    ]
    rows_out: list[dict] = []
    order = 1
    for _done_flag, _sys, layer, _rr, _path, r, m, layer_name, done in scored:
        # Wave = structure band, not alphabet
        if done:
            wave = 0
            q = 0
            status = "done_s5_s6"
        else:
            if layer <= 25:
                wave = 1  # core structure
            elif layer <= 45:
                wave = 2  # PHS / mid layers / path K2+K3
            elif layer <= 70:
                wave = 3  # schools / modern / K3
            else:
                wave = 4  # optional subsystems / cosmology / K4-deep
            q = order
            order += 1
            status = "queued"

        rows_out.append(
            {
                "wave": wave,
                "queue_order": q,
                "system_id": r["system_id"],
                "structure_layer": layer,
                "structure_layer_name": layer_name,
                "rolle": m.get("rolle", ""),
                "status_pipeline": status,
                "filename": r["filename"],
                "relative_path": r["relative_path"],
                "pass_k2_struct": r["pass_k2_struct"],
                "pass_k3_rules": r["pass_k3_rules"],
                "pass_k4_meanings": r["pass_k4_meanings"],
                "pass_notes": r.get("pass_notes", ""),
            }
        )

    out = REF / f"literature_content_wave_queue_{DATE}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        wri = csv.DictWriter(f, fieldnames=fields)
        wri.writeheader()
        wri.writerows(rows_out)

    print(f"Wrote {out.name} ({len(rows_out)} rows)")
    print("by wave:", dict(Counter(str(r["wave"]) for r in rows_out)))
    print("\n=== HD first 12 queued (structure order) ===")
    hd = [r for r in rows_out if r["system_id"] == "hd" and r["status_pipeline"] == "queued"][:12]
    for r in hd:
        print(
            f"  q={r['queue_order']:3} L{r['structure_layer']:2}/{r['structure_layer_name']:22} "
            f"{r['filename'][:70]}"
        )
    print("\n=== BaZi first 8 queued ===")
    bz = [r for r in rows_out if r["system_id"] == "bazi" and r["status_pipeline"] == "queued"][:8]
    for r in bz:
        safe = r["filename"][:70].encode("ascii", "replace").decode("ascii")
        print(
            f"  q={r['queue_order']:3} L{r['structure_layer']:2}/{r['structure_layer_name']:22} "
            f"{safe}"
        )


if __name__ == "__main__":
    main()
