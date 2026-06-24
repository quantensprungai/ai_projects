<!-- Reality Block
last_update: 2026-06-24
status: draft
scope:
  summary: "Claude-Web-Research aus Screenshots — Artifact-Kette, nicht Einzel-Prompt."
  in_scope:
    - session flow from user screenshots
    - cursor file mapping
  out_of_scope:
    - copying Brendan tickers/prices
notes:
  - "Screenshots 2026-06-24 — Strategy JSX, Verified Data, Archetypes, Nokia DD, Contracts"
-->

# Claude Web Research — aus den Screenshots

> Die Screenshots zeigen **keinen** copy-paste Mega-Prompt, sondern eine **Kette aus Dialog + JSX-Artifacts**.  
> Das PDF-Transkript bestätigt: **Context/Constraints zuerst**, dann Strategie → Screen → Tiefe → Contracts.

---

## Was die Screenshots zeigen (Reihenfolge)

```text
① Strategy Artifact     „Concentrated Thesis Strategy“ + Vehicle Framework
② Verified Data         Ticker-Tabelle (Preis, Cap, Earnings, Implied Move)
③ Archetypes            5 Thesis-Typen → Vehicle + Book-%
④ Screen / Score        Namen den Archetypes zuordnen + Katalysator
⑤ Deep Dive             z. B. Nokia Segmente, P/S, 2028-Szenarien
⑥ Pairing               Korrelation (NOW↔NOK, NOW↔MP …)
⑦ Scenarios             Event-Woche (Bull/Base/Disappointment %)
⑧ Contract Artifact     Strike-Vergleich + „ACTUAL ROBINHOOD DATA“
⑨ Execution Rules       Limit orders, 60/40 staging, cash reserve
```

**Monitor (Greeks Dashboard, Options Terminal)** = **danach** — Phase B, nicht Research.

---

## Artifact ① — Strategy Overview (JSX)

Inhalt (Brendan-Beispiel **$50K** — bei dir **$10K** skalieren):

- **Philosophy:** 3–5 conviction names, vehicle matches thesis, cash as weapon (15–30 %)
- **Allocation (Beispiel):** LEAP 40 % · Short Calls 20 % · Mid-cap Shares 18 % · Cash 15 % · Micro 7 %
- **Vehicle decision tree:**
  1. Liquid options? → sonst Shares
  2. IV < ~65 %? → Calls ok; sonst Shares / warten auf IV crush
  3. Katalysator innerhalb Expiry? → Expiry an Event koppeln

→ bei uns: [`strategy_brief.md`](strategy_brief.md) + [`thesis_archetypes.md`](thesis_archetypes.md)

---

## Artifact ② — „Verified data — locked in“

Tabelle **nach** dem Screen — nicht vorher erfunden:

| Spalte | Zweck |
|--------|--------|
| Position | Ticker |
| Stock Price | Stand zum Research-Datum |
| Market Cap | Größenklasse / Vehicle |
| Earnings Date | Katalysator-Kalender |
| Implied Move | Earnings-Risiko / Catalyst Binary |

Beispiel-Zeilen im Screenshot: NBIS, NOW, HIMS, OSCR — **Mai-2026-Session**, nicht übernehmen.

→ bei uns: `research/universe.json` + optional `reference/screen_YYYY-MM.md`  
→ Preise **zum Screen-Datum** via yfinance; **fein** erst S3 mit IBKR.

---

## Artifact ③ — Five Thesis Archetypes

| Archetype | Vehicle | Book % (Brendan) | Signale |
|-----------|---------|------------------|---------|
| Value Mean Reversion | LEAP 8–12m | 30–50 % | P/E floor, inst. buying, crash + catalyst |
| Momentum Re-rating | LEAP + Short Calls | 20–35 % | P/S gap vs peers, partner validation |
| Catalyst Binary | Short calls 2–5m | 5–10 % / name | IV rank, implied move, earnings date |
| Policy / Structural Floor | **Shares** | 8–15 % | Govt floor, IV too high for calls |
| (5. teils abgeschnitten) | | | |

→ Namen **klassifizieren**, nicht blind listen.

---

## Artifact ④–⑥ — Tiefe + Portfolio

- **Nokia Deep Dive:** Segment-Tabelle → Growth-Math → Peer P/S → implied price @ Multiples
- **Correlation table:** welche Paare low/medium — Book-Level vor dem 3.–5. Namen
- **Process:** Week 1–2 Research → Week 2 Selection → Entry staged → Monitor thesis not price

→ `research/deepdives/TICKER.md` · `research/book_rationale.md`

---

## Artifact ⑦ — Scenario (Event-Woche)

Wahrscheinlichkeiten + Spot/Option-Pfade für **ein** Katalysator-Event (z. B. Knowledge + Jensen).

→ optional `research/scenarios/TICKER_EVENT.md` — qualitativ, Preise in S3 verifizieren

---

## Artifact ⑧ — Contract Analysis

- Tabs pro Ticker (NOW / NOK / MP)
- Strike tradeoffs (ATM vs 1–2 OTM vs deep OTM)
- Tabelle: Premium, Spread, OI, Greeks, **Robinhood live data**
- „Why this decision“ + $5K matrix

→ `scripts/contract_compare.py` + IBKR · `research/decisions/`

---

## Wie instruiert er Claude Web? (aus Screenshots + Transkript)

**Nicht** ein geheimer Prompt — sondern:

1. **Erste Nachricht:** Kontogröße, Risiko, Holding, Ziel (Mix Upside/capped downside)
2. **Claude erzeugt Strategy JSX** — User iteriert („mehr cash“, „nur 3 Namen“)
3. **Follow-up:** „Run a screen using this strategy“ / „Classify these names“
4. **Daten verifizieren:** „Lock in verified data“ → Tabelle
5. **Pro Shortlist:** „Deep dive NOK fundamentals“ → Artifact/Text
6. **Pairing:** „Compare NOW+MP vs tech cluster“
7. **Contracts:** Paste Robinhood chain **or** connector → „Compare strikes“

**Research = Multi-Turn + Artifacts.**  
**Layer 1–4 Prompts** (im PDF-Video ~15 min) sind **nur** der Monitor-Build.

---

## Cursor-Äquivalent (dein $10K)

| Claude Web Artifact | Cursor Output |
|---------------------|---------------|
| Strategy overview JSX | `strategy_brief.md` + `thesis_archetypes.md` |
| Verified data table | `universe.json` (Felder: price_asof, earnings, implied_move) |
| Archetype cards | `archetype` Feld in universe |
| Nokia DD | `deepdives/NOK.md` |
| Correlation | `book_rationale.md` |
| Scenario week | `scenarios/*.md` (optional) |
| Contract JSX | `contract_compare.py` + IBKR |
| Greeks terminal | **fertig** — `run_dashboard.ps1` |

---

## Wichtig für dich

- Screenshots = **Brendans Mai-2026-Book ($50K+)** — **Methodik** übernehmen, **Inhalt nicht**
- Dein Book: **NOK + MP @ $10K** — eigenen Screen starten
- **Echte Preise für Trades:** IBKR in S3, nicht die Screenshot-Zahlen

Nächster Schritt: [`prompts/00_strategy.md`](../../code/options-book/research/prompts/00_strategy.md) in Cursor ausführen.
