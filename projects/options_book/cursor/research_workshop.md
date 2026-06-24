<!-- Reality Block
last_update: 2026-06-24
status: draft
scope:
  summary: "Research-Werkstatt in Cursor — Session-Playbooks (ersetzt Claude Web)."
  in_scope:
    - session types
    - cursor workflow
    - file outputs
  out_of_scope:
    - layer 1-4 monitor
notes: []
-->

# Research-Werkstatt in Cursor

> **Kurz:** Du brauchst Claude Web nicht zwingend. Cursor **ist** die Werkstatt — Chat + Agent schreibt Dateien, Scripts liefern Live-Daten.

---

## Warum Cursor statt Claude Web?

| | Claude Web (PDF) | Cursor (unser Setup) |
|---|------------------|----------------------|
| Qualitative Analyse | ✅ Chat | ✅ Chat (gleiche Modelle) |
| Tabellen / Strike-Vergleich | JSX-Artifacts | ✅ Agent + `contract_compare.py` |
| Persistenz | Chat-Verlauf | ✅ **Git-Dateien** (universe, deepdives) |
| Anbindung Monitor | Copy-Paste → positions.json | ✅ Agent aktualisiert direkt |
| Kosten | Flatrate Web | Cursor-Abo (+ Layer 3 API separat) |

Das PDF nutzt Claude Web, weil Brendan dort gearbeitet hat — **nicht**, weil es technisch nötig wäre.

---

## Drei Schichten der Werkstatt

```text
1. Cursor Chat/Agent     → Denken, Text, Entscheidungen (ersetzt Claude-Web-Dialog)
2. research/*.md + .json → Persistente Artefakte (ersetzt JSX-Inhalt)
3. scripts/*.py          → Live-Daten (ersetzt „Robinhood Data“-Panel)
```

**Nicht** alles als Streamlit nachbauen — nur **Monitor** bleibt Dashboard. Research lebt in **Dateien + Cursor-Sessions**.

Optional später: Streamlit-Tab „Research“ nur zum **Lesen** der deepdives (kein Muss).

---

## Session-Typen

### S0 — Strategie (einmalig)

**Prompt:** „Lies `strategy_brief.md` und hilf mir, die leeren Felder aus meinem Setup auszufüllen.“

**Output:** `projects/options_book/reference/strategy_brief.md`

---

### S1 — Broad Screen

**Prompt-Vorlage:** [`research/prompts/01_broad_screen.md`](../../code/options-book/research/prompts/01_broad_screen.md)

**Agent-Aufgaben:**
1. `strategy_brief.md` lesen
2. Kandidaten diskutieren
3. `research/universe.json` anlegen/ergänzen (status: `researched` | `watchlist` | `rejected`)

---

### S2 — Deep Dive (pro Ticker)

**Prompt-Vorlage:** `research/prompts/02_deep_dive.md`

**Inhalt (wie PDF Nokia):**
- Revenue-Mix / Segmente
- Growth-Math (konservativ + Base Case)
- Bewertung (P/S-Szenarien, implied Price)
- Bull / Bear / Catalysts

**Output:** `research/deepdives/TICKER.md`  
**Universe:** status → `watchlist` oder `rejected`, thesis kurz aktualisieren

---

### S3 — Contract Pick

**Prompt-Vorlage:** `research/prompts/03_contract_pick.md`

**Agent-Aufgaben:**
1. Script ausführen:
   ```powershell
   cd code\options-book
   .venv\Scripts\python.exe scripts\contract_compare.py --ticker NOW --expiry 2027-01-15 --strikes 100,120,135 --type call --capital 5000
   ```
2. Ergebnis interpretieren (Spread, OI, Torque vs. $100 Strike)
3. Entscheidung dokumentieren

**Output:** `research/decisions/TICKER_120C_2027-01-15.md`

---

### S4 — Book Build

**Prompt-Vorlage:** `research/prompts/04_book_build.md`

**Inhalt (wie PDF):**
- Sector Correlation zwischen Shortlist-Namen
- Cross-Name Vehicle Comparison
- Vehicle Selection Lesson
- Finale `positions.json` + universe `in_book`

**Output:** `research/book_rationale.md`, `positions.json`

---

## Cursor-Session starten (Copy-Paste)

```
Kontext: options-book Phase A Research.
Lies: projects/options_book/reference/strategy_brief.md
      projects/options_book/01_spec/research_workflow.md
Regel: .cursor/rules/options-book-research.mdc

Session S2 Deep Dive für [TICKER].
Schreibe research/deepdives/[TICKER].md und aktualisiere universe.json.
Keine erfundenen Kursdaten — Live-Daten nur via scripts/contract_compare.py.
```

---

## Nach der Session

1. `universe.json` + deepdives committen (wenn gewünscht)
2. Bei `in_book`: Trade im Broker → `sync_positions.py`
3. `python run.py --layer 4` — Monitor übernimmt

---

## Handover-Zeile

```
Research: [S1|S2|S3|S4] für [TICKER] — deepdives/… + universe status [X]
Nächster Schritt: [Contract Pick | Book Build | Paper sync]
```
