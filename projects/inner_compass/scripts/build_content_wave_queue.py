#!/usr/bin/env python3
"""Build literature_content_wave_queue_YYYY-MM-DD.csv from extraction pass plan.

All curated works (status=ok) stay in scope. Waves only sequence processing order.
"""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
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


def is_done(r: dict) -> bool:
    fn = f"{r['filename']} {r['relative_path']}"
    return any(d.lower() in fn.lower() for d in DONE_MARKERS)


def wave_key(r: dict, matrix: dict) -> int:
    m = matrix.get(r["relative_path"], {})
    rolle = m.get("rolle", "")
    path = r["relative_path"].lower()
    if "/k2/" in path or rolle == "K2_ref":
        return 1
    if "/k2+k3/" in path:
        return 2
    if "/k3/" in path or rolle == "K3_deutung":
        return 3
    if "/k4/" in path or rolle == "K4_deutung":
        return 4
    return 3


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
    done = [r for r in ok if is_done(r)]
    todo = [r for r in ok if not is_done(r)]

    print(f"total={len(plan)} ok={len(ok)} done={len(done)} queued={len(todo)}")
    print("by system ok:", dict(Counter(r["system_id"] for r in ok).most_common()))
    for r in done:
        print(f"  DONE {r['system_id']:10} {r['filename'][:72]}")

    by_wave: dict[int, list] = defaultdict(list)
    for r in todo:
        by_wave[wave_key(r, matrix)].append(r)
    for w in sorted(by_wave):
        print(f"WAVE {w}: {len(by_wave[w])} — {dict(Counter(r['system_id'] for r in by_wave[w]).most_common())}")

    fields = [
        "wave",
        "queue_order",
        "system_id",
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
    for r in done:
        m = matrix.get(r["relative_path"], {})
        rows_out.append(
            {
                "wave": 0,
                "queue_order": 0,
                "system_id": r["system_id"],
                "rolle": m.get("rolle", ""),
                "status_pipeline": "done_s5_s6",
                "filename": r["filename"],
                "relative_path": r["relative_path"],
                "pass_k2_struct": r["pass_k2_struct"],
                "pass_k3_rules": r["pass_k3_rules"],
                "pass_k4_meanings": r["pass_k4_meanings"],
                "pass_notes": r.get("pass_notes", ""),
            }
        )

    order = 1
    for w in (1, 2, 3, 4):
        items = sorted(
            by_wave[w],
            key=lambda r: (SYS_PRIO.get(r["system_id"], 99), r["relative_path"]),
        )
        for r in items:
            m = matrix.get(r["relative_path"], {})
            rows_out.append(
                {
                    "wave": w,
                    "queue_order": order,
                    "system_id": r["system_id"],
                    "rolle": m.get("rolle", ""),
                    "status_pipeline": "queued",
                    "filename": r["filename"],
                    "relative_path": r["relative_path"],
                    "pass_k2_struct": r["pass_k2_struct"],
                    "pass_k3_rules": r["pass_k3_rules"],
                    "pass_k4_meanings": r["pass_k4_meanings"],
                    "pass_notes": r.get("pass_notes", ""),
                }
            )
            order += 1

    out = REF / f"literature_content_wave_queue_{DATE}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        wri = csv.DictWriter(f, fieldnames=fields)
        wri.writeheader()
        wri.writerows(rows_out)
    print(f"Wrote {out.name} ({len(rows_out)} rows)")


if __name__ == "__main__":
    main()
