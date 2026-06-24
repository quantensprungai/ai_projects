<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Options Portfolio Monitor (AlgoBot) – Doku-Index: Morning-Dashboard, 4 Layer, Human-in-the-Loop."
  in_scope:
    - project overview
    - scope / non-scope
    - links to plan and layer specs
  out_of_scope:
    - broker API / auto-execution
    - live trading credentials
notes:
  - "Quelle: Claude Portfolio.pdf (Brendan / AI Trading, 4-Layer-System)"
  - "Code-Repo: code/options-book/ → quantensprungai/options-book"
  - "Broker: IBKR, API: TWS API + IB Gateway"
-->

# Options Book – Doku Index

> **One screen, every morning.** Deterministischer Portfolio-Monitor für Options + Shares. Meldet Fakten und Ziel-/Stop-Treffer — **keine** Buy/Sell-Empfehlungen, **kein** Order-Routing.

## Schnelleinstieg

| Frage | Datei |
|-------|-------|
| Gesamtplan, Phasen, Checklisten | [`03_roadmap/master_plan.md`](03_roadmap/master_plan.md) |
| Was ist drin / was nicht? | [`00_overview/scope.md`](00_overview/scope.md) |
| Zielbild & Philosophie | [`00_overview/mission.md`](00_overview/mission.md) |
| Layer 1–4 im Detail (Prompts/Specs) | [`01_spec/layer_specifications.md`](01_spec/layer_specifications.md) |
| Deep Dive Template (S2) | [`01_spec/deep_dive_template.md`](01_spec/deep_dive_template.md) |
| Research → Universe → Book | [`01_spec/research_workflow.md`](01_spec/research_workflow.md) |
| **Research-Taktung & Automatisierung** | [`reference/research_cadence.md`](reference/research_cadence.md) |
| Research-Werkstatt (Cursor) | [`cursor/research_workshop.md`](cursor/research_workshop.md) |
| Portfolio-Fit | [`research/book_rationale.md`](../../code/options-book/research/book_rationale.md) |
| Ticker-Discovery / Screening | [`reference/screening_methodology.md`](reference/screening_methodology.md) |
| Claude Web Research (PDF + Screenshots) | [`reference/claude_web_research_from_pdf.md`](reference/claude_web_research_from_pdf.md) |
| Research bei null starten | [`reference/research_start_from_zero.md`](reference/research_start_from_zero.md) |
| Aktueller Stand | [`cursor/status.md`](cursor/status.md) |
| Broker IBKR vs. Robinhood | [`reference/broker_comparison.md`](reference/broker_comparison.md) |
| IBKR Gateway Setup | [`reference/ibkr_gateway_setup.md`](reference/ibkr_gateway_setup.md) |
| KI-Session übergeben | [`cursor/handover.md`](cursor/handover.md) |

## Architektur (4 Layer)

```text
Layer 1  Data & Valuation     yfinance, Greeks (Black-Scholes), Snapshots → SQLite
Layer 2  Portfolio Analytics  Allocation, Aggregate Greeks, IV-Rank, DTE-Flags
Layer 3  Macro Gate & News    VIX/Breadth/Credit (deterministisch) + Claude API (News)
Layer 4  Alerts & Dashboard   Diff, Alerts, Streamlit UI, optional Telegram/iMessage
```

## Phasen (Kurz)

| Phase | Was | Tooling |
|-------|-----|---------|
| **A** | Strategie, Screening, Contract-Auswahl | **Cursor** (Research-Werkstatt) · optional Claude Web |
| **B1–B4** | Layer 1–4 bauen | Python, Claude Code / IDE |
| **C** | Daily Run, Cron, Betrieb | lokal, ~$1/Tag API (Layer 3) |

## Verwandte Orte

- **Quelle (extern):** `Nextcloud/.../AlgoBot/Claude Portfolio.pdf`
- **Code:** [`code/options-book/`](../../code/options-book/) — `git@github.com:quantensprungai/options-book.git`
- **Abgrenzung:** [`projects/trading_bot/`](../trading_bot/) — generisches Skelett, nicht dasselbe Vorhaben

## Ordnerstruktur

```text
projects/options_book/
├── cursor/           ← status, handover (max. 6–8 aktive Docs)
├── 00_overview/      ← Mission, Scope
├── 01_spec/          ← Layer-Specs, positions.json-Schema
├── 03_roadmap/       ← master_plan.md (Haupt-Checkliste)
└── README.md
```
