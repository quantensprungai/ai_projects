<!-- Reality Block
last_update: 2026-06-23
status: active
scope:
  summary: "Taktung Phase A Research vs Phase B Monitor; Automatisierung."
  in_scope:
    - cadence table
    - single paper dual profile
    - research_hygiene roadmap
  out_of_scope:
    - layer 1-4 implementation detail
notes:
  - "Ergänzt research_workflow.md und daily_run_automation.md"
-->

# Research-Cadence & Automatisierung

> **Monitor täglich, Research gestaffelt.** Phase A (qualitativ) und Phase B (deterministisch) haben unterschiedliche Rhythmen.

Siehe auch: [`01_spec/research_workflow.md`](../01_spec/research_workflow.md) · [`daily_run_automation.md`](daily_run_automation.md) · [`paper_trading_setup.md`](paper_trading_setup.md)

---

## Ein Paper-Konto, zwei Profile

IBKR erlaubt typischerweise **nur ein Paper-Konto** (`DUR097452`).

| Profil | NAV | Datei | Broker |
|--------|-----|-------|--------|
| **Standard** | €10.000 | `positions.json` | Echte Paper-Trades |
| **Micro** | €1.000 | `positions.micro.json` | Simuliert oder manuell getaggt |

Scripts: `use_paper_standard.ps1` / `use_paper_micro.ps1` — wechseln `BOOK_PROFILE`, `BOOK_NAV_EUR`, `POSITIONS_FILE`, **nicht** die IBKR-Account-ID.

**Regel:** Nicht Standard + Micro blind per `sync_positions.py` mischen.

---

## Was wie oft?

| Stufe | Was | Takt | Automatisierung |
|-------|-----|------|-----------------|
| **B** Monitor | Layer 1–4, Alerts, Greeks | **täglich** Mo–Fr nach US-Close | `run.py` + Task Scheduler / Cursor Automation |
| **A.2b** Preise Universe | Spot, Market Cap | **wöchentlich** | `verify_universe_prices.py` |
| **A.2b** Hygiene | Stale Deep Dives, Earnings-Fenster | **wöchentlich** | `research_hygiene.py` *(Roadmap)* |
| **A.2** Broad Screen light | Scores, neue Kandidaten | **monatlich** oder freier Slot | Cursor Agent + externes Markt-Memo |
| **A.2b** Deep Dive | Segmente, Bewertung, These | **quartalsweise** oder vor Katalysator | Cursor S2 (Human Review) |
| **A.1** Strategy | Constraints, Themen | **selten** (Regime-Wechsel) | Manuell → `strategy_brief.md` |
| **A.3** Contract Pick | Strike, Expiry, OI | **bei Entry / Roll** | `contract_compare.py` + IBKR — **Entscheidung menschlich** |

**Nicht automatisieren (MVP):** Auto-Buy, täglicher voller Deep Dive, fremde PDF-Watchlists übernehmen.

---

## Architektur (3 Schichten)

```text
┌─────────────────────────────────────────────────────────┐
│  AUTOMATISCH — Code / Scheduler                         │
│  Mo–Fr 22:00 CET   python run.py                        │
│  So               python scripts/verify_universe_prices.py │
│  So (später)      python scripts/research_hygiene.py    │
└─────────────────────────────────────────────────────────┘
                          ↓ Flags / Kalender
┌─────────────────────────────────────────────────────────┐
│  HALB-AUTOMATISCH — Cursor Automation / Agent           │
│  1×/Monat   Strategy-Context (Bericht A, ai-2027/elliot)│
│  1×/Monat   Universe-Score aktualisieren (S1 light)     │
│  on-trigger Deep-Dive-Update für 1 Ticker (S2)          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  MENSCH — Human-in-the-Loop                             │
│  Strategy · Pass/Reject · Trade · Contract-Wahl       │
└─────────────────────────────────────────────────────────┘
```

Daily Run: [`daily_run_automation.md`](daily_run_automation.md) — Python, nicht Cursor als Layer-3-Ersatz.

---

## `research_hygiene.py` (Roadmap)

Geplantes wöchentliches Script:

- Deep Dives mit `research_date` > 90 Tage → Flag `stale`
- Earnings der Book-Ticker in den nächsten 14 Tagen → Liste
- Universe-Einträge ohne aktuelles `price_date` → Refresh anstoßen
- Optional: Hinweis „Monats-Screen fällig“ wenn < 4 `watchlist`/`in_book` und freier Slot

Output: `research/hygiene_report.json` oder Log — **keine** Trades.

---

## Code-Roadmap (Profil-aware Monitor)

| Item | Status |
|------|--------|
| `BOOK_PROFILE`, `POSITIONS_FILE` in `.env` | ✅ Scripts |
| `run.py` liest `POSITIONS_FILE` | 🔲 offen |
| `research_hygiene.py` | 🔲 offen |
| Task Scheduler `run_daily.ps1` | 🔲 User-Setup |

---

## Changelog

| Datum | Änderung |
|-------|----------|
| 2026-06-23 | Erstellt: Cadence, Single-Paper, Hygiene-Roadmap |
