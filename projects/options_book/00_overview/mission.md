<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Mission: Morning Portfolio Monitor für Options + Shares."
  in_scope:
    - mission statement
    - success criteria
    - design principles
  out_of_scope:
    - implementation details
notes: []
-->

# Mission – Options Portfolio Monitor (AlgoBot)

## Zweck

Ein **täglicher Morning-Screen** für das eigene Options- und Aktien-Portfolio:

- Echte Positionen live bewerten (yfinance)
- Gesamtbuch-Risiko sichtbar machen (Greeks, Allocation, Macro)
- News-Zusammenfassung pro Ticker (Claude API, 1×/Tag)
- Alerts bei Ziel/Stop, IV-Moves, neuen Strikes/Expiries, DTE-Schwellen
- **Human-in-the-Loop:** System meldet Bedingungen, der Mensch entscheidet

## Erfolgskriterien

1. **Ein Screen morgens** — NAV, P&L, Alerts, Positionen, Macro, News in < 2 Min. erfassbar
2. **$0 Datenkosten** — yfinance + lokale Berechnung (Greeks, Macro)
3. **~$1/Tag Betrieb** — nur Layer 3 (Claude News) kostet API-Tokens; Caching pro Tag
4. **Kein manuelles Copy-Paste** — Positionen in `positions.json`, Daily Run automatisiert (Cron)
5. **Snapshots ermöglichen Diffs** — neue Strikes/Expiries vs. gestern erkennbar

## Design-Prinzipien

| Prinzip | Bedeutung |
|---------|-----------|
| **Facts, not advice** | Alerts formulieren Bedingungen („Target erreicht"), nie „kaufen/verkaufen" |
| **Deterministic first** | Layer 1, 2, Macro-Gate: gleiche Inputs → gleiche Outputs |
| **Claude nur wo nötig** | Schwere Research-Phase in Claude Web; Monitor nutzt API nur für News |
| **Layerweise bauen** | Layer N erst fertig, dann N+1 — jedes Layer importierbar |
| **Single SQLite DB** | Alle Runs, Snapshots, Analytics, News in einer DB |

## Nicht-Ziele

- Kein Broker-API / kein Auto-Trading
- Kein Intraday-Scalping (yfinance reicht für EOD/Daily)
- Keine Finanzberatung oder Gewinn-Garantie
