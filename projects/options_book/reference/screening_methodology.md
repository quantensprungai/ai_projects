<!-- Reality Block
last_update: 2026-06-24
status: draft
scope:
  summary: "Ticker-Discovery aus Claude Portfolio.pdf — Screening Names."
  in_scope:
    - criteria from strategy
    - scoring dimensions
    - portfolio fit
  out_of_scope:
    - automated screener API
notes:
  - "Quelle: PDF Seiten Strategy Research + Screening Names (~6–11 min)"
-->

# Screening-Methodik — wie kommen die Ticker?

> **Ja:** Die Ticker-Suche ist **Kern-Research** (Phase A.2), nicht nur Anzeige.  
> Das PDF erklärt die Reihenfolge explizit: **Strategie → Screen → Score → Deep Dive → Contracts → Monitor.**

---

## Reihenfolge im PDF (Brendan)

```text
1. Strategy Research     Constraints → LEAPs (Large Cap) + Shares (Small Cap)
2. Screening Names       Breiter Screen aus Strategie-Kriterien
3. Scoring + Portfolio   Katalysator, IV, Korrelation, Sektor-Mix
4. Deep Dive pro Name    z. B. Nokia Segment-Analyse, NOW Crash
5. Choosing Contracts    Strike, Expiry, Greeks, Liquidity
6. Trades laden          positions.json / Broker
7. Options Dashboard     Layer 1–4 (deterministisch, ~$1/Tag)
```

**Wichtig:** Schritt 7 ist **nicht** Research — das ist der Monitor, den wir gebaut haben.  
Alles davor (1–6) = **Research-Werkstatt**.

---

## Schritt 1 — Strategie **vor** jedem Ticker

Aus dem PDF (Mai-Challenge):

| Constraint | Konsequenz |
|------------|------------|
| Mix aus Risiko & Upside | Nicht alles YOLO, nicht alles defensiv |
| Downside begrenzt wo möglich | Policy Floors, Shares statt teurer Calls |
| **LEAPs** auf größere Namen | IV fair, These braucht Zeit (>45 DTE, eher 8–12 Mon.) |
| **Shares** auf kleinere Caps | Illiquid Options, IV zu hoch |
| Kein Weekly-Timing | Theta / Glücksspiel vermeiden |

Output bei uns: [`strategy_brief.md`](strategy_brief.md)

**Ohne Strategie kein Screen** — Brendan: *„I didn't just open a chat and ask what I should buy. I gave context.“*

---

## Schritt 2 — Screening Names (Ticker finden)

Kriterien kommen **direkt aus der Strategie** (PDF):

| Kriterium | Bedeutung |
|-----------|-----------|
| **Abverkauft + Erholungsgrund** | Beat-and-raise trotz Crash (NOW) |
| **Katalysator am Kalender** | Earnings, Policy, Partnership — datiert |
| **Momentum** | Erlaubt, wenn Upside **begründet** (nicht blind) |
| **IV vernünftig** | Options preislich passend zur These |
| **Passt zu Risk/Upside-Profil** | Setup muss zur Strategie passen |

Claude lief **breiten Screen** → viele Kandidaten, nicht nur 2–3 Namen.

Mai-Beispiel (aus PDF, **eine Session**): OCR, NBIS, NOW, HIMS, MP, NOK —  
UI „37 researched“ = **kumulativ** („Every Name We Discussed“), inkl. Passed/Rejected über Zeit.

---

## Schritt 3 — Scoring (nicht alle gleich behandeln)

PDF: *„didn't treat these all equally — scored across different dimensions“*

| Dimension | Frage |
|-----------|--------|
| **Catalyst timing** | Near / medium / long-term? (OCR near, NBIS medium, NOW long) |
| **IV environment** | Cheap / fair / rich für geplantes Vehicle? |
| **Market correlation** | Beta, Sektor, „was killt alle?“ |
| **Thesis quality** | Konkrete These pro Name, nicht nur „AI stock“ |
| **Position size** | Konzentriert vs. kleiner (MP: slow catalyst → kleiner) |

Ergebnis → Status in `universe.json`: `watchlist` | `passed` | `rejected` | später `in_book`.

---

## Schritt 4 — Portfolio-Fit (Book-Level)

PDF kombiniert Namen **bewusst**:

- **Verschiedene Katalysator-Fenster** — nicht alles auf ein Earnings-Event
- **Verschiedene Sektoren** — Healthcare vs. AI-Infra vs. Enterprise SaaS
- **Verschiedene Analyse-Tiefe** — Nokia „European AI“ → Segment-Deep-Dive; andere kürzer

Output: Teil von `research/book_rationale.md` (Session S4).

---

## Schritt 5 — Deep Dive (nur Shortlist)

Erst **nach** Screen + Score — z. B. Nokia:

- Revenue-Mix / Segmente
- Growth-Math (AI/Cloud in Legacy versteckt)
- P/S-Szenarien, implied Price

→ `research/deepdives/TICKER.md`

---

## Schritt 6 — Contracts (nur `in_book`-Kandidaten)

Strike, Expiry, Greeks, Spread, $5K-Matrix → `decisions/` + `contract_compare.py`

---

## In Cursor umsetzen (statt Claude Web)

Gleiche Schritte, gleiche PDF-Logik:

| PDF-Schritt | Cursor |
|-------------|--------|
| Context / Strategie | `strategy_brief.md` + Prompt S0 |
| Broad Screen | Prompt **S1** → `universe.json` |
| Score + Filter | Felder in universe + Session-Notiz |
| Portfolio-Fit | Prompt **S4** (Teil) |
| Deep Dive | Prompt **S2** → `deepdives/` |
| Contracts | Prompt **S3** + Script |

Claude Web im PDF = **Werkzeug der Wahl 2025**; Cursor = **gleiche Werkstatt**, bessere Persistenz.

---

## Was wir **nicht** automatisieren (MVP)

- Kein Bloomberg-Screener mit 500 Filtern
- Kein „37 Ticker aus PDF kopieren“
- Kein Auto-Buy

Discovery bleibt **qualitativ** — Kriterien aus PDF, Ausführung in Cursor-Sessions.
