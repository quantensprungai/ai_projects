<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Handover-Block für KI-Sessions Options Trading."
  in_scope:
    - context summary
    - where to continue
  out_of_scope:
    - full specs
notes: []
-->

# Handover – Options Trading (AlgoBot)

## Was ist das?

**Morning Portfolio Monitor** für Options + Shares. 4 Layer (Data → Analytics → Macro/News → Alerts/Dashboard). Human-in-the-loop — **kein Auto-Trading**.

## Wo weitermachen?

1. [`cursor/status.md`](status.md) — aktueller Stand
2. [`03_roadmap/master_plan.md`](../03_roadmap/master_plan.md) — nächste unchecked Checkboxen
3. [`01_spec/layer_specifications.md`](../01_spec/layer_specifications.md) — technische Details pro Layer

## Phase

**Phase 0** (Setup). Doku steht. Code-Repo fehlt noch.

## Wichtige Regeln

- Layer N **fertig** vor Layer N+1
- Alerts = **Fakten**, nie Buy/Sell
- Options-Preise in `positions.json` = **pro Share**, Kontrakt = 100 Shares
- Claude API nur Layer 3 (~$1/Tag); Research in Claude Web (Flatrate)

## Copy-Paste für neue Session

```text
Projekt: options_book
Docs: projects/options_book/
Code: code/options-book/ (git@github.com:quantensprungai/options-book.git)
Plan: 03_roadmap/master_plan.md
Aktuell: Phase 0 — Code-Repo anlegen, dann Phase A Strategie
Spec: 01_spec/layer_specifications.md
Quelle: Claude Portfolio.pdf (4-Layer Morning Screen)
```
