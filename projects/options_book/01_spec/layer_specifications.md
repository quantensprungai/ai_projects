<!-- Reality Block
last_update: 2026-06-23
status: draft
scope:
  summary: "Layer 1–4 Spezifikationen aus Claude Portfolio.pdf (Prompts destilliert)."
  in_scope:
    - layer requirements
    - config defaults
    - outputs per layer
  out_of_scope:
    - Python implementation
notes:
  - "Quelle: Claude Portfolio.pdf — Brendan 4-Layer Options Monitor"
-->

# Layer-Spezifikationen (1–4)

> Jede Layer baut auf der vorherigen auf. **Layer N fertig → dann N+1.**

---

## Layer 1 — Data & Valuation

### Input
- `positions.json` (siehe [`positions_schema.md`](positions_schema.md))

### Data Pull (yfinance)
Pro Ticker im Book:
- Spot-Preis
- Volle Options-Chain (alle Expiries/Strikes)
- Pro gehaltenem Kontrakt matchen: **bid, ask, last, IV, volume, open interest**

### Mark-Preis
| Fall | Regel |
|------|-------|
| bid + ask vorhanden | `mark = (bid + ask) / 2` |
| sonst | `mark = last` |
| Shares | `mark = spot` |

### Greeks (lokal, Black-Scholes, **ohne** externe Lib)
Pro Option: **delta, gamma, theta, vega**
- Risk-free rate: konfigurierbar, Default **0.045** (annual)
- DTE: tatsächliche Tage bis Expiry

### Snapshots
Jeder Run speichert volle Chain pro Underlying:
- **JSON:** `snapshots/TICKER_YYYY-MM-DD.json`
- **SQLite:** gespiegelt in zentraler DB
- Zweck: Diffs in Layer 4, IV-History in Layer 2

### Valuation Output (pro Position)
- Mark, Current Value, Unrealized P&L ($ und %)
- DTE (Options)
- Progress to Target / Stop (%)

### CLI / Storage
- Flag: `--asof YYYY-MM-DD` — stempelt Run-Datum für Storage/Diff (**Marks vom aktuellen Feed**, keine historische Chain-Rekonstruktion)
- Alles in **eine SQLite-DB**
- Module **importierbar** für spätere Layer

### Layer-1 Checkliste
- [x] `positions.json` Parser (Options + Shares)
- [x] yfinance Spot + Chain Pull
- [x] Contract-Matching (strike, expiry, type)
- [x] Mark-Berechnung
- [x] Black-Scholes Greeks (lokal)
- [x] Snapshot JSON + SQLite Write
- [x] Valuation Output pro Position
- [x] `--asof` Flag (via run.py)
- [x] Beispiel-Positionen (`positions.json.example`)
- [x] Manueller Test-Run

---

## Layer 2 — Portfolio Analytics

> Building on Layer 1.

### Allocation
- % NAV nach **Ticker** und **Sektor**
- Sektor: Config-Lookup, Fallback yfinance
- **Concentration Flags** (info):
  - Ticker > **40%** NAV (konfigurierbar)
  - Sektor > **60%** NAV (konfigurierbar)

### Aggregate Greeks
| Metrik | Bedeutung |
|--------|-----------|
| Net Delta | Share-equivalent über gesamtes Book |
| Total Daily Theta | $/Tag bei flat prices |
| Net Vega | $-Impact pro 1 IV-Punkt |

### IV Environment (pro Option)
- IV Rank/Percentile aus **eigenen** Daily Snapshots
- Lookback Default: **252** Tage
- < 20 Tage History → Label **„building history"**
- Flags: **rich** (IV rank > **70**), **cheap** (IV rank < **30**)

### DTE Flags
- Schwellwert konfigurierbar, Default **45** Tage
- Surface fact — **kein** Roll-Rat

### Output
- Clean Analytics Summary
- SQLite Write pro Run

### Layer-2 Checkliste
- [x] Sektor-Mapping (Config + yfinance Fallback)
- [x] Allocation % Ticker + Sektor
- [x] Concentration Flags
- [x] Net Delta / Theta / Vega aggregiert
- [x] IV Rank aus Snapshot-History
- [x] DTE-Flags
- [x] Analytics Summary + DB Persist
- [x] Test mit Layer-1-Output

---

## Layer 3 — Macro Gate & Claude News

> Building on Layer 1–2.

### Teil A: Macro Gate (deterministisch, Score 0–100)
Gewichtete Mischung (Weights summieren 1.0, konfigurierbar):

| Input | Beschreibung |
|-------|--------------|
| VIX Level | + 1-Jahres-Percentile |
| VIX Term Structure | VIX vs. VIX3M |
| Market Breadth | % SPY Constituents > 200d MA (oder Proxy) |
| Credit Spread | HYG vs. TLT |

Gleiche Daten → gleicher Score. **Kosten: $0.**

### Teil B: News Analysis (Claude API)
Pro Ticker im Book, 1×/Tag:
1. Headlines via `yfinance.news` (Fenster Default **3** Tage)
2. Claude API → pro Name:
   - Kurz-Summary
   - Sentiment: positive / neutral / negative
   - Key Drivers
   - Flag wenn Position betroffen

**Nicht** Trade-Trigger. Claude **summarisiert und flaggt**, sagt nicht buy/sell.

### Caching & Kosten
- Cache pro Name **pro Tag** — Re-Runs re-billen nicht
- Einziger Paid-Teil: ~**$1/Tag** (abhängig von Anzahl Ticker)

### Storage
- Macro Score + News pro Run → SQLite

### Layer-3 Checkliste
- [x] VIX, VIX3M, Breadth-Proxy, HYG/TLT Pull
- [x] Macro Score 0–100 (konfigurierbare Weights)
- [x] yfinance News Pull pro Ticker
- [x] Claude API Integration (Summary Template)
- [x] Daily Cache (Name + Date)
- [x] SQLite Persist (macro + news)
- [ ] Test: Re-Run mit API-Key → Cache kein Re-Bill
- [ ] `ANTHROPIC_API_KEY` in `.env` (lokal)

---

## Layer 4 — Alerts & Dashboard

> Ties Layers 1–3 together.

### A) New Strike / Expiry Detection
Diff: heutiger Chain-Snapshot vs. vorheriger Run pro Underlying:
- Neue Expiry-Dates listen
- Neue Strikes in Band um gehaltene Strikes (Default **±30%**)

### B) Condition Alerts
Surface facts — **never buy/sell**:

| Alert | Priorität | Trigger |
|-------|-----------|---------|
| `target_hit` | high | mark ≥ target_price |
| `stop_hit` | high | mark ≤ stop_price |
| `target_near` | info | innerhalb X% vom Target (Default **80%**) |
| `iv_change` | warning | IV vs. prior snapshot ≥ **20%** |
| `new_strikes` | info | aus Diff |
| `new_expiry` | info | aus Diff |
| `dte_warning` | warn | DTE < Schwellwert (Layer 2) |
| `concentration` | info | aus Layer 2 |
| `news_flag` | warn/info | aus Layer 3, one-line driver |

### C) Dashboard (Streamlit, Bloomberg-style, eine Seite)
- **Status Strip:** NAV, P&L, # Positions, Alert Count, Macro Score, Net Delta, Daily Theta, As-Of
- **Active Alerts:** farbcodiert nach Severity; new-strike = gelb
- **Positions Grid:** Strike, Expiry, DTE-Pill, Entry, Mark, Value, P&L, Delta, Theta/day, Vega, IV, Progress Bars Target/Stop
- **Theta Decay Chart:** aggregiert $ bis längste Expiry; extrinsic decay curve (BS @ const spot/IV, illustrativ)
- **Strike Ladder:** ±6 Strikes um gehaltene; bid/ask/last/IV/vol/OI; held highlighted; NEW badge
- **Allocation Bars:** by Ticker + Sector mit Concentration Flags
- **News Feed:** Claude Summaries aus Layer 3

### D) Notifier (optional, default off)
- Telegram (bot token + chat ID in env) oder iMessage (macOS, `osascript`)
- Aufruf am Run-Ende: `notifier.maybe_send(alerts, asof)`
- Disabled = no-op

### E) Scheduling
- Cron-Zeile: 1× werktags nach Marktschluss
- Log → Datei

### Layer-4 Checkliste
- [x] Chain-Diff Engine (vs. prior snapshot)
- [x] Alert Engine (alle Typen + Phrasen)
- [x] Streamlit Dashboard (Kern-Panels)
- [x] Notifier (Telegram + iMessage, config flag)
- [x] Runner: Layer 1 → 2 → 3 → 4 → optional Notify
- [x] Cron + Logging (`scripts/run_daily.ps1`, `logs/run_*.log`)
- [x] End-to-End Test: ein voller Morning Run
- [ ] Cursor Automation oder Task Scheduler (User-Setup)

---

## Geplante Code-Struktur (Referenz)

```text
options-book/
├── positions.json
├── config.yaml              # thresholds, weights, notifier
├── run.py                   # CLI entry, --asof
├── layer1/                  # data, valuation, greeks, snapshots
├── layer2/                  # analytics
├── layer3/                  # macro, news, cache
├── layer4/                  # alerts, dashboard, notifier
├── snapshots/               # JSON chain dumps
├── data/
│   └── portfolio.db         # SQLite
├── logs/
├── requirements.txt
└── .env.example
```
