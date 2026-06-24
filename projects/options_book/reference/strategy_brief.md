<!-- Reality Block

last_update: 2026-06-23

status: active

scope:

  summary: "Strategie-Constraints für Phase A Research (Cursor-Werkstatt)."

  in_scope:

    - constraints

    - vehicle rules

    - screening dimensions

    - thematic allocation (ai-2027 + elliot)

    - dual capital profiles EUR

  out_of_scope:

    - daily monitor thresholds

notes:

  - "Ein IBKR-Paper; Standard + Micro als logische Books"

-->



# Strategy Brief — Options Book



> **User-bestätigt** S0. Zwei **Kapital-Profile** (EUR) — **ein** IBKR-Paper-Konto, zwei Book-Dateien.



---



## Kapital-Profile



| | **Standard** | **Micro** |

|---|--------------|-----------|

| **NAV** | **€10.000** | **€1.000** |

| **Paper-Konto** | **DUR097452** (4002) — **beide Profile** | **dasselbe** Konto, logisch getrennt |

| **Namen im Book** | **4** | **2–3** |

| **Max. pro Name** | **~20 % NAV** (~**€2.000**) | **~25–40 % NAV** (~**€250–400**) |

| **Cash-Reserve** | **20 %** (~**€2.000**) | **0–20 %** (~**€0–200**) |

| **Max. investiert** | ~**€8.000** | ~**€800–1.000** |

| **Max. Verlust/Trade** | **25 %** Slot ≈ **€500** | **25 %** Slot ≈ **€50–100** |

| **LEAPs** | Ja, wenn IV/Liquidität passt | **Max. 1** LEAP; Rest **Shares** / Pass |

| **Earnings-Short-Calls** | Nein (Ausnahme Post-Earnings, klein) | **Nein** |

| **contract_compare** | `--capital 2000` | `--capital 250` (typ. 1 Slot) |



**Micro:** US-Options = **1 Kontrakt min.** — oft nur **1 LEAP** + **1–2 Share-Lines** (Fractional ok).



**FX:** US-Titel in **USD** — NAV in **EUR**; Wechselkurs wirkt auf P&L und Buying Power (bei Micro stärker spürbar).



**Ein Paper-Konto:** IBKR erlaubt nur ein Paper — Micro ist **virtuelles Sub-Book** (eigene JSON, Größenlimits im Monitor). Trades im selben Konto nur mit klarer Profil-Zuordnung; Micro optional erst **simuliert** (ohne Broker-Order) bis Live-€1K.

**Monitor / Scripts:** `use_paper_standard.ps1` vs `use_paper_micro.ps1` wechselt **Profil + positions-Datei**, nicht das IBKR-Konto.



---



## Kontext (gemeinsam)



| Feld | Wert |

|------|------|

| Broker | IBKR Paper **DUR097452** (4002) · Live **U11962966** (4001) |

| Phase | Paper je Profil, dann Live — **Human-in-the-Loop** |

| Basiswährung Konto | **EUR** (User) |

| Underlyings | US primary (USD-notiert) |

| Max. Ticker-Konzentration | **40 %** (Standard) · Micro: höher faktisch ok |

| Max. Sektor-Konzentration | **60 %** |



---



## Risiko & Holding (gemeinsam)



- **Max. Verlust pro Trade:** **25 %** des Allocations-Slots (absolut: Profil-Tabelle)

- **Holding:** LEAPs **8–14 Mon.** · Shares **6–24 Mon.**

- **Short Calls / Weeklies:** **Nein** (Standard: Ausnahme Post-Earnings **<90 DTE**, klein). Micro: entfällt.

- **Min. DTE LEAPs:** **> 45** (Spec), bevorzugt **> 180**

- **Human-in-the-Loop:** Monitor meldet Fakten — **keine** Auto-Orders



---



## Strategie-Kern (PDF-adaptiert)



| Bein | Wann | Vehicle |

|------|------|---------|

| **A** | Große/mittlere Caps, These braucht Zeit, **IV fair** | **LEAP Calls** (1–2 OTM) |

| **B** | Policy/Commodity, **IV hoch**, Floor-These | **Shares** |

| **C** | Re-Rating + gute Options-Liquidität | LEAPs |

| **D** | Momentum + near-term Katalysator | Kurze Calls (selten, klein) |



**Nicht:** Daytrading, Weekly YOLO, illiquide Deep-OTM (<500 OI).



---



## Vehicle-Regeln (Entscheidungsbaum)



| Situation | Vehicle | Logik |

|-----------|---------|--------|

| Deep Value / Crash + IV fair | LEAP Calls | Zeit für 3–4 Earnings |

| Re-Rating + enger Spread / hohes OI | LEAP Calls | Torque + execution |

| IV teuer vs. Beta / Commodity | **Shares** | Floor ohne Theta |

| Mega-Cap, begrenztes Upside | Pass oder kleine Shares | Skip capped upside |

| Legal/Audit ungelöst | **Hard pass** | SMCI-Muster |

| Spread >15 % | Pass oder Shares only | Execution killt EV |



**Strike:** 1–2 OTM · **Expiry:** LEAP **8–12 Mon.** · **Limit**, nicht Ask jagen.



---



## Screening-Dimensionen



| Dimension | Gewicht | Frage |

|-----------|---------|--------|

| Katalysator | hoch | Datiert? near / medium / long? |

| These-Typ | hoch | Value / Re-Rating / Momentum / Policy? |

| IV vs. Vehicle | hoch | LEAP oder Shares? |

| Liquidität | hoch | OI, Spread (<10 % ideal) |

| Korrelation | mittel | Was killt mehrere Slots? |

| Sektor | mittel | Nicht alles gleiches Narrativ |



---



## Themen & Sektoren (ai-2027 + elliot, Juni 2026)



> Linse für **S1 Screen** — keine Ticker-Pflichtliste.



| Prio | Thema | Archetype | Vehicle | NAV-Richtwert |

|------|-------|-----------|---------|---------------|

| **A** | Physische Knappheit (Energy, Grid, Rare Earth) | Policy Floor | **Shares** | ~25–35 % |

| **B** | AI-Infrastruktur (nicht reine Semi-Bubble) | Momentum Re-Rating | LEAP wenn IV ok | ~20–30 % |

| **C** | Value nach Tech-Stress | Value Mean Reversion | LEAP | ~20–30 % |

| **D** | Security / Resilienz | Policy / Re-Rating | Shares / LEAP | ~10–20 % |

| **E** | Cash | Cash | — | **Standard 20 %** · **Micro 0–20 %** |



**Meiden:** Mega-Cap-Semi-Momentum ohne Floor; AI-Wrapper ohne Moat; ohne Katalysator.



**Geografie:** US primary (liquid ADRs ok).



**Makro-Szenario elliot („Sommer des Elends“):** Öl↑, DXY↑, Stagflation, Tech-Stress — **Bear-Overlay**, nicht Base-Case. Book: **MP** teil-Hedge (Physical/Policy), **NOK** vulnerable, **Cash 20 %** Puffer. Nicht identisch mit elliot-Rotation (XLE). Detail: `research/deepdives/MP.md` §7.



---



## Portfolio-Paarung



| Profil | Slots | Ziel |

|--------|-------|------|

| **Standard** | 4 | Themen **A–D** |

| **Challenge** | 2–3 | Upside / PDF-näher — [`strategy_brief_challenge.md`](strategy_brief_challenge.md) |

| **Micro** | 2–3 | z. B. **1× A Shares** + **1× B/C LEAP** |



- Katalysator-Fenster streuen · Beta-Blend ~**0,85–1,10**

- Korrelation: AI-Infra (B,C) · Policy/China (A) · Risk-off/VIX (LEAPs)



---



## Was wir **nicht** traden



- Weekly / 0DTE / reines Theta

- OI <500 oder Spread >15 %

- Meme ohne These · Legal-Overhang · Duplikat ohne Diversifikationsgrund



---



## Positionen & Research



| Profil | positions | Hinweis |

|--------|-----------|---------|

| Standard | `code/options-book/positions.json` | Default |

| Challenge | `code/options-book/positions.challenge.json` | Profil B Upside |

| Micro | `code/options-book/positions.micro.json` | Simuliert oder manuell (selbes Paper-Konto) |



Research: `code/options-book/research/universe.json` (Profil im Prompt nennen).



Setup Paper-Konten: [`paper_trading_setup.md`](paper_trading_setup.md)



---



## Changelog



| Datum | Änderung |

|-------|----------|

| 2026-06-23 | **Ein Paper-Konto:** Micro = logisches Sub-Book, nicht zweites IBKR |

| 2026-06-24 | **Profil B Challenge** — [`strategy_brief_challenge.md`](strategy_brief_challenge.md) |

