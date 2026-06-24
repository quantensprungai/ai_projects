<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Aktueller Projektstand options-book."
  in_scope:
    - current phase
    - next actions
    - blockers
  out_of_scope:
    - historical log
notes: []
-->

# Status – options-book

**Stand:** 2026-06-23  
**Phase:** Layer 4 ✅ — Daily Automation (Cursor oder Task Scheduler) als Nächstes

## Erledigt

- [x] Projekt `projects/options_book/` (umbenannt von options_trading)
- [x] Code-Repo `code/options-book/` + Remote `git@github.com:quantensprungai/options-book.git`
- [x] Master-Plan + Layer-Specs
- [x] Broker: **IBKR**; API: **TWS API + IB Gateway** (nicht Client Portal)

- [x] Layer 2: Allocation, Aggregate Greeks, IV-Rank, DTE-Flags

## Als Nächstes

1. **Layer 3:** Macro Gate + Claude News
2. SAC-Hinweis: [`reference/windows_smart_app_control.md`](../reference/windows_smart_app_control.md)

## Offen / Entscheidungen

| Thema | Status |
|-------|--------|
| API | ✅ **TWS API** (ib_async), nicht Client Portal REST |
| UI manuell | IBKR Desktop optional |
| API-Hintergrund | IB Gateway (empfohlen) vs. TWS |
| Marktdaten-Abo US Options | ❓ prüfen |

## Referenz

- Plan: [`03_roadmap/master_plan.md`](../03_roadmap/master_plan.md)
- APIs: [`reference/ibkr_api_choice.md`](../reference/ibkr_api_choice.md)
