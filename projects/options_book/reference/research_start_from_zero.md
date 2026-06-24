<!-- Reality Block
last_update: 2026-06-24
status: draft
scope:
  summary: "Research bei null starten — heute, $10K, ohne PDF-Daten."
  in_scope:
    - start sequence
    - data sources per step
    - brendan vs cursor
  out_of_scope:
    - monitor layer prompts
notes: []
-->

# Research bei null starten — wie Brendan vs. wie du

> **Ja:** Ihr solltet bei **null Research-Inhalt** starten — mit **heutigem** Markt, nicht Mai-2026-Screenshots.  
> **Nein:** Research startet **nicht** mit MCP oder Yahoo-Chain — das kommt **später**.

---

## Was Brendan laut PDF/Screenshots **nicht** macht

| Tool | Research-Start? | Wofür bei ihm |
|------|-----------------|---------------|
| **MCP** | ❌ nicht im PDF | — (Robinhood hat keine API) |
| **Yahoo Finance** | ❌ nicht für Research-Start | **Monitor Layer 1** (Python, nach den Trades) |
| **Robinhood API** | ❌ existiert nicht | **Contract-Phase:** Chain **manuell** / Screenshot / App → „ACTUAL ROBINHOOD DATA“ |
| **Claude API** | ❌ für Research | Flatrate **Claude Web** Chat |

Research-Start = **Chat + Constraints** → Strategy Artifact → qualitativer Screen → **dann** Daten „lock in“.

---

## Zwei getrennte Startpunkte

### A) Du hast **kein Book** (wirklich null)

```text
S0  Strategie ($10K)     →  nur Text, keine Ticker
S1  Broad Screen         →  qualitative Kandidaten + Archetype
S1b Verified row         →  Spot + Earnings-Datum (yfinance reicht)
S2  Deep Dive Shortlist  →  Fundamentals (Web/Wissen, keine Strikes)
S3  Contracts             →  IBKR Chain oder contract_compare.py
S4  Trade + positions.json
```

### B) Du hast **schon Positionen** (dein Fall: NOK + MP)

Book ist **nicht** null — **Research** ist null (leere Thesen).

```text
S0  ✅ strategy_brief ($10K)
S2  Zuerst: Deep Dive NOK + MP mit HEUTIGEN Daten
S3  Bestehende Strikes validieren (IBKR vs. entry)
S1  Danach: Screen für Name #3 (mit ~$2–3K Cash + Rest NAV)
```

**Empfehlung:** **B** — nicht so tun als wäre das Book weg.

---

## Datenquelle **pro Schritt** (heute, bei dir)

| Schritt | Brauchst du Live-Daten? | Quelle |
|---------|-------------------------|--------|
| **S0 Strategie** | Nein | Deine Constraints in Cursor |
| **S1 Screen** | Optional Spot/Cap | `yfinance` oder Cursor Web-Suche — **grober** Check |
| **S1b Verified table** | Ja, **Stand heute** | Kleines Script oder Agent: Spot, Cap, next earnings |
| **S2 Deep Dive** | Spot + Fundamentals | Web-Recherche, 10-K-Segmente — **keine** Option Chain nötig |
| **S3 Contract** | **Ja, Pflicht** | **IBKR Gateway** (beste) · Fallback: `contract_compare.py` (yfinance) |
| **Monitor daily** | Ja | `run.py` (yfinance) — schon gebaut |

**MCP IBKR:** optional Stufe 3 — Claude liest Portfolio/Chain **in Cursor**, wenn du Connector einrichtest. **Nicht nötig** zum Start; Python-Scripts reichen.

---

## Konkret: **heute in Cursor** (30–60 Min.)

### Schritt 1 — Strategie bestätigen (5 Min.)

Datei lesen: `strategy_brief.md` ($10K). In Cursor:

> „Bestätige strategy_brief für $10K. Keine neuen Ticker.“

### Schritt 2 — Verified Data für **NOK + MP** (10 Min.)

Agent führt aus (Beispiel):

```powershell
cd code\options-book
.venv\Scripts\python.exe -c "
import yfinance as yf
for t in ['NOK','MP']:
    x = yf.Ticker(t)
    p = x.fast_info.get('lastPrice') or x.info.get('currentPrice')
    cap = x.fast_info.get('marketCap')
    print(t, p, cap)
"
```

Ergebnis in `universe.json` ergänzen: `price_asof`, `price_date` (heute), später `earnings_date`, `implied_move` wenn verfügbar.

**Das ist euer „Verified data — locked in“** — **heutiger** Stand, nicht Screenshot.

### Schritt 3 — S2 Deep Dive **einen** Ticker (30 Min.)

Prompt: `@research/prompts/02_deep_dive.md` + **NOK** oder **MP**

- Segment-/These-Analyse **selbst** schreiben lassen
- **Explizit:** „Nutze keine Brendan/PDF-Zahlen; markiere unsichere Annahmen“

### Schritt 4 — S3 **nur wenn** du Strikes prüfen willst

Paper-Gateway morgen oder heute Live:

```powershell
.venv\Scripts\python.exe scripts\contract_compare.py --ticker NOK --expiry 2027-01-15 --strikes 18,20,22 --type call --capital 2000
```

(`--capital 2000` ≈ 20 % von $10K)

---

## Wie Brendan „startet“ (zusammengefasst)

1. **Leerer Chat** — nicht „scan the market“
2. **Constraints** (Kontogröße, Risiko, LEAP vs Shares) — wie dein `strategy_brief`
3. **Claude baut Strategy JSX** — du iterierst
4. **„Screen names that fit“** — qualitativ, breit
5. **„Lock verified data“** — Tabelle mit **Preisen zum Session-Datum** (Quelle im Video: Robinhood/App, nicht MCP)
6. **Deep dives + contracts** mit **frischen** Broker-Daten
7. **Erst dann** Python Monitor mit **Yahoo** (Layer 1–4)

Du machst **dieselbe Reihenfolge** in Cursor + Dateien; Yahoo/IBKR an **den richtigen Stellen**.

---

## Was wir **nicht** tun

- PDF-Ticker/Preise als Startpunkt
- Option Chain beim ersten Screen
- MCP als Voraussetzung
- Monitor (`run.py`) als Research-Ersatz

---

## Nächster Klick

In Cursor neue Session:

```
@strategy_brief.md @research/prompts/02_deep_dive.md
Deep Dive MP (Policy Floor Archetype). Stand heute 2026-06-24.
Hole Spot/Cap live via yfinance. Keine PDF-Daten.
Schreibe research/deepdives/MP.md und aktualisiere universe.json.
```

Danach dasselbe für NOK — **das ist „Analyse bei null“** für dein echtes Book.
