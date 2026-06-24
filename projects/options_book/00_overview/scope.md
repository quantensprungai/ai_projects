<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Scope/Non-Scope für AlgoBot Portfolio Monitor."
  in_scope:
    - in-scope features
    - non-scope boundaries
  out_of_scope:
    - broker integration details
notes: []
-->

# Scope – Options Portfolio Monitor

## In Scope

### Phase A — Research (Claude Web, qualitativ)
- [ ] Strategie definieren (Constraints: Kontogröße, Risiko, Holding Period)
- [ ] Ticker-Screening (Katalysator, IV-Umfeld, Korrelation, Sektor-Diversifikation)
- [ ] Contract-Auswahl (Strike, Expiry, Greeks, IV vs. Kosten)
- [ ] Initiale Positionen manuell im Broker setzen → in `positions.json` übernehmen

### Phase B — Monitor bauen (4 Layer, Python)
- [ ] **Layer 1:** yfinance Pull, Mark/P&L, Black-Scholes Greeks, Snapshots (JSON + SQLite)
- [ ] **Layer 2:** Allocation, Aggregate Greeks, IV-Rank (eigene History), DTE-Flags
- [ ] **Layer 3:** Macro Score 0–100 (VIX, Term Structure, Breadth, Credit) + Claude News
- [ ] **Layer 4:** Chain-Diff, Condition Alerts, Streamlit Dashboard, optional Notifier

### Phase C — Betrieb
- [ ] `--asof YYYY-MM-DD` Flag für Run-Datum
- [ ] Cron: 1× werktags nach Marktschluss
- [ ] Log-Output in Datei
- [ ] Env-Vars: `ANTHROPIC_API_KEY`, optional Telegram/iMessage

## Non-Scope (explizit ausgeschlossen)

| Thema | Warum |
|-------|-------|
| Order-Execution / Broker-API | Human-in-the-Loop by design |
| Intraday-Bars / Live-Streaming | yfinance-Einschränkung; Daily reicht |
| Historische Chain-Rekonstruktion | Marks kommen vom aktuellen Feed; `--asof` nur für Storage/Diff |
| Backtesting der Research-Phase | Phase A ist qualitativ, nicht backtestbar |
| Multi-User / SaaS | Persönliches Tool |
| Premium-Daten (FMP, Polygon) | Optional später; MVP mit yfinance |

## Asset-Typen

| Typ | Unterstützt | Hinweis |
|-----|-------------|---------|
| Call/Put Options | ✅ | Preise pro Share; Kontrakt = 100 Shares |
| Shares | ✅ | `contracts` = Anzahl Aktien |
| Spreads / Multi-Leg | ❌ MVP | Später als Erweiterung |

## Kostenmodell

| Komponente | Kosten |
|------------|--------|
| yfinance, lokale Compute, SQLite, Streamlit | $0 |
| Claude API (Layer 3, 1×/Tag, gecacht) | ~$1/Tag |
| Claude Web (Phase A Research) | Flatrate-Abo |
