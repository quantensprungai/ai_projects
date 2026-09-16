#!/usr/bin/env python3
"""Filter discover_report.json for homelab-relevant PDF titles."""
import json
import re
import sys
from pathlib import Path

DEFAULT_REPORT = Path("/home/user/telegram-research/downloads/telegram-pdf/discover_report.json")

PATTERNS = [
    (
        r"blackout|stromausfall|emp|bbk|bevölkerungsschutz|krisenvorsorge|notvorr|"
        r"bunker|survival|prepping|prep\b|selbstversorg",
        "Krise/Prep",
    ),
    (
        r"wiederaufbau|resilienz|infrastruktur|community|kooperation|nachbarschaft|"
        r"souverän|autark|organis",
        "Wiederaufbau/Community",
    ),
    (
        r"solar|photovoltaik|\bpv\b|batterie|elektronik|funk|amateur|\bham\b|"
        r"werkstatt|mechanik|schwei|3d.?druck|ingenieur",
        "Technik/Energie",
    ),
    (
        r"permakultur|garten|landwirtschaft|saat|vorrat|haltbar|ferment|jagd|"
        r"fischerei|medizin|sanit|erste.?hilfe",
        "Versorgung/Gesundheit",
    ),
    (r"prophezei|apokalypse|endzeit|offenbarung|bibel", "Prophezeiung"),
    (r"waffe|schieß|verteidigung|taktik|kampf", "Sicherheit"),
]

RX = [(re.compile(p, re.I), label) for p, label in PATTERNS]


def main() -> None:
    report_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_REPORT
    data = json.loads(report_path.read_text(encoding="utf-8"))
    picks = []
    seen: set[int] = set()
    for item in data["items"]:
        blob = f"{item['title']} {item.get('caption', '')}"
        labels = {label for rx, label in RX if rx.search(blob)}
        if not labels:
            continue
        mid = item["id"]
        if mid in seen:
            continue
        seen.add(mid)
        mb = (item.get("size_bytes") or 0) / 1024 / 1024
        picks.append((mid, mb, sorted(labels), item["title"][:120]))
    picks.sort(key=lambda x: -x[0])
    print(f"Curated picks: {len(picks)} (from {data['pdf_hits']} PDF search hits)\n")
    for pid, mb, labels, title in picks[:60]:
        print(f"- [{pid}] {mb:.1f} MB | {' + '.join(labels)} | {title}")


if __name__ == "__main__":
    main()
