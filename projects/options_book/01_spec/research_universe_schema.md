<!-- Reality Block
last_update: 2026-06-24
status: draft
scope:
  summary: "JSON-Schema für research/universe.json (Phase A Output)."
  in_scope:
    - field definitions
    - status enum
  out_of_scope:
    - screener UI styling
notes: []
-->

# `research/universe.json` — Schema

Datei im Code-Repo: `code/options-book/research/universe.json`  
Vorlage (nur Struktur): `research/universe.schema.json`

---

## Top-Level

Array von Objekten — ein Objekt pro recherchiertem Ticker.

```json
[
  {
    "ticker": "…",
    "name": "…",
    "sector": "…",
    "status": "watchlist",
    "vehicle": "BUY — LEAPs",
    "thesis": "…",
    "bull_case": "…",
    "bear_case": "…",
    "catalysts": ["…"],
    "key_signals": ["…"],
    "tags": ["…"],
    "research_date": "2026-06-24",
    "screen_session": "2026-06-screen-1"
  }
]
```

---

## Pflichtfelder

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `ticker` | string | US-Symbol, uppercase |
| `name` | string | Firmenname |
| `status` | enum | siehe Lifecycle unten |

---

## Optionale Felder (qualitativ, aus Research)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `sector` | string | Sektor / Theme (frei, konsistent halten) |
| `vehicle` | string | Geplantes Instrument, z. B. `BUY — Shares`, `BUY — LEAPs` |
| `thesis` | string | 1–3 Sätze Investment-These |
| `bull_case` | string | Kurz Bull |
| `bear_case` | string | Kurz Bear |
| `catalysts` | string[] | Datierte Events; `✅` in Text optional |
| `key_signals` | string[] | Hervorgehobene Fakten (blau im UI) |
| `tags` | string[] | Kategorien (VALUE, AI-INFRA, …) |
| `research_date` | ISO date | Letzte inhaltliche Aktualisierung |
| `screen_session` | string | Referenz auf `reference/screen_*.md` |
| `notes` | string | Freitext, nicht im Dashboard |

---

## `status` — erlaubte Werte

| Wert | UI-Label |
|------|----------|
| `researched` | RESEARCHED |
| `watchlist` | WATCHLIST |
| `in_book` | IN BOOK |
| `passed` | PASSED |
| `rejected` | REJECTED |
| `traded` | TRADED |
| `mentioned` | MENTIONED |

---

## Beziehung zu `positions.json`

- **`in_book`** → mindestens eine Zeile in `positions.json` (oder geplant vor erstem Trade)
- Monitor-Pipeline ignoriert `universe.json` vollständig
- Bei Schließen einer Position: Status in universe auf `traded` oder `passed`, Zeile aus `positions.json` entfernen

## Beziehung zu Deep Dives

| Feld in universe.json | Ausführlich in |
|-----------------------|----------------|
| thesis (kurz) | `research/deepdives/TICKER.md` — Segmente, Growth-Math, P/S |
| bull_case / bear_case (kurz) | deepdives — volle Argumentation |
| vehicle | `research/decisions/TICKER_….md` nach Contract Pick |

Portfolio-Fit (Correlation, Vehicle Lesson): `research/book_rationale.md`

---

## Nicht in universe speichern

- Live-Preise, P/E, Market Cap (Dashboard holt live via yfinance)
- Greeks, IV-Rank (kommen aus Daily Run / DB, nur für Book)
- Claude-News (Layer 3, nur Book-Ticker)
