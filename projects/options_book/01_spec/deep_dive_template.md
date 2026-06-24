<!-- Reality Block
last_update: 2026-06-23
status: active
scope:
  summary: "S2 Deep Dive — Pflichtstruktur (PDF-Mapping)."
  in_scope:
    - section list
    - file locations
  out_of_scope:
    - automated deep dive generation
notes:
  - "Spiegelt Claude Portfolio Artifacts ④–⑦"
-->

# Deep Dive Template (S2)

> **Zweck:** Qualitative Tiefe wie im PDF — **vor** S3 Contract Pick.  
> **Nicht** ersetzen durch Yahoo-Screen allein.

---

## Dateien

| Artefakt | Pfad |
|----------|------|
| **Template (kopieren)** | `code/options-book/research/deepdives/_TEMPLATE.md` |
| **Output pro Ticker** | `code/options-book/research/deepdives/TICKER.md` |
| **Optional Event-Szenario** | `code/options-book/research/scenarios/TICKER_EVENT.md` |
| **Prompt** | `code/options-book/research/prompts/02_deep_dive.md` |
| **Universe-Update** | `research/universe.json` (thesis, bull/bear, catalysts, signals) |

---

## Pflicht-Abschnitte (PDF-Mapping)

| # | Abschnitt | PDF-Entsprechung |
|---|-----------|------------------|
| 0 | Investment Summary + Verified Data | Artifact ② (Spot, Cap, Earnings) |
| 1 | Segmente | Nokia DD — Revenue-Mix |
| 2 | Growth-Math Base + Conservative | Segment-Tabelle 2026–2029 |
| 3 | Peers + Implied Price | P/S Re-Rating Matrix |
| 4 | Bear / Base / Bull **%** | Probability Distribution |
| 5 | Catalysts + Key Signals | Deep Dive + Process |
| 6 | Vehicle + Book-Fit + Korrelation | Archetypes + Correlation Table |
| 7 | Makro-Stress (elliot / ai-2027) | optional §7 — Sommer des Elends |
| 8 | Position Review | Execution |
| 9 | S3 Checkliste | Artifact ⑧ |
| 10 | Entscheidung S2 | hold / rejected / exit |

---

## Regeln

- **Quellen + Datum** — Nokia IR, Earnings Call, yfinance nur für Spot/Cap
- **Keine erfundeten Optionspreise** in S2 — nur S3 mit IBKR
- **VERIFY** wenn Daten alt oder widersprüchlich
- Nach S2: `universe.json` aktualisieren, `research_date` setzen

---

## Workflow

```text
S1 universe (watchlist) → S2 deepdives/TICKER.md → S3 decisions/ + contract_compare
                     ↘ scenarios/ (optional, Event-Woche)
```

Siehe: [`research_workflow.md`](research_workflow.md) · [`reference/claude_web_research_from_pdf.md`](../reference/claude_web_research_from_pdf.md)
