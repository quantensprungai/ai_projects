<!-- Reality Block
last_update: 2026-06-24
status: active
scope:
  summary: "Profil B — Challenge / Upside (PDF-näher, höheres Torque)."
  in_scope:
    - allocation rules
    - catalyst binary slot
    - staging pyramiding
  out_of_scope:
    - auto-execution
notes:
  - "User-Wahl 2026-06-24: Upside-Chance über Standard-Disziplin"
  - "Paper startet mit €10K Regeln; Live-Ziel €30K+"
-->

# Strategy Brief — Profil B (Challenge / Upside)

> **Profil B** = PDF-Challenge **näher**: mehr Konzentration, Katalysator-Calls, Staging — **höheres Upside, höherer Drawdown**.  
> **Profil A (Standard):** [`strategy_brief.md`](strategy_brief.md) · **Micro:** gleiches Setup-Doc.

**User-bestätigt:** 2026-06-24 · Upside-Chance priorisiert.

---

## Profile im Überblick

| | **A Standard** | **B Challenge** |
|--|----------------|-----------------|
| **Ziel** | Disziplin, 6–14M These, lernen | **Upside**, PDF-ähnliches Torque |
| **NAV Paper** | €10.000 | **€10.000** (Regeln) |
| **NAV Live-Ziel** | €10.000+ | **€30.000+** empfohlen |
| **Namen** | 4 | **2–3** |
| **Max. pro Name** | ~20 % (~€2K) | **~40–50 %** (~€4–5K) |
| **Cash** | 20 % | **10–15 %** |
| **Catalyst Short Calls** | Nein | **Ja, 5–10 % NAV** |
| **LEAP-Horizont** | 8–14 Mon. | **8–12 Mon.** + **60–90 DTE** Event-Lines |
| **Pyramiding** | Nein (Trim bei Drift) | **Ja, 60/40 Staging** |
| **positions** | `positions.json` | `positions.challenge.json` (sync) + `.planned.json` (Orders) |
| **Script** | `use_paper_standard.ps1` | `use_paper_challenge.ps1` |

**Ein Paper-Konto** (DUR097452) — **nicht** Standard + Challenge gleichzeitig traden ohne klare JSON-Zuordnung.

---

## Philosophie (PDF-adaptiert)

1. **3–5 → 2–3 Überzeugungs-Namen** — Qualität über Diversifikation  
2. **Vehicle = These** — LEAP für Zeit, **Short Calls** für datierten Katalysator  
3. **Cash = Waffe** — **10–15 %**, nicht 20 % (mehr deploybar)  
4. **Staging:** **60 %** Erst-Entry · **40 %** Add nur bei **Bestätigung** (Breakout, Earnings-Beat, Thesis-Intakt)  
5. **Human-in-the-Loop** — Monitor meldet; **kein** Auto-Trade

---

## Kapital & Slots (Challenge @ €10K Paper)

| Slot | Typ | NAV-Richtwert | Vehicle |
|------|-----|---------------|---------|
| **1 — Core LEAP** | Value / Re-Rating | **35–50 %** | LEAP 8–12m, 0–1 OTM (mehr Delta ok) |
| **2 — Momentum / Policy** | Re-Rating oder Floor | **25–40 %** | LEAP oder **Shares** |
| **3 — Catalyst** | Event Binary | **5–10 %** | **Short Calls 60–90 DTE** um Earnings/Tag |
| **Cash** | Optionality | **10–15 %** | — |

**Max. Verlust pro Slot:** **25 %** des Slot-Nominals (absolut: **€1.000–1.250** bei 40–50 %-Slot).

**contract_compare:** `--capital 4000` (Core) · `--capital 1000` (Catalyst)

---

## Vehicle-Regeln (Challenge)

| Situation | Vehicle | Challenge-Note |
|-----------|---------|----------------|
| IV < 65 %, These > 6 Mon. | LEAP 8–12m | Strike **0–1 OTM** (mehr Delta als Standard) |
| IV ≥ 65 %, These intakt | **Shares** oder warten | NOW-Typ: Shares **oder** Post-Earnings LEAP |
| Dated catalyst (Earnings, Tag) | **Calls 60–90 DTE** | Archetype 3 — **max 10 % NAV** |
| Policy / IV rich | Shares | Pyramiding erlaubt (60/40) |
| Post-Earnings IV crush | LEAP Entry | Bevorzugter Entry vs. Pre-Event LEAP |

**Spread > 10 %:** Pass · **OI < 500:** Pass · **Weeklies / 0DTE:** Nein

---

## Archetypes (Priorität Upside)

| Archetype | Book % | Upside-Hebel |
|-----------|--------|--------------|
| **Momentum Re-rating** | 30–50 % | LEAP + ggf. Event-Call |
| **Value Mean Reversion** | 25–40 % | LEAP nach Crash, **größerer Slot** |
| **Catalyst Binary** | **5–10 %** | **Neu vs. Standard** — Short Calls 2–3 Mon. |
| **Policy Floor** | 20–35 % | Shares, **Add auf Stärke** |
| **Cash** | 10–15 % | Deploy nach Panic / IV crush |

---

## Staging & Pyramiding (60/40)

```text
Tranche 1 (60 %):  S3 Entry — Limit @ Mid (IBKR Snapshot)
Tranche 2 (40 %):  Nur wenn:
  - Spot > Entry + 10 % UND These unverändert (S2 Hold), ODER
  - Earnings-Beat + Guidance bestätigt Archetype, ODER
  - Policy-Katalysator (z. B. MP Escalation) — explizit im Deep Dive
```

**Kein Add** wenn Stop-Loss-Zone oder S2-These gebrochen.

**Trim:** Optional **25–33 %** Gewinnmitnahme bei **+100 %** auf Slot (Challenge-Regel, nicht Standard-Trim).

---

## Themen A–D (gleiche Linse, aggressivere Größe)

| Thema | Challenge-Fokus | Beispiel |
|-------|-------------------|----------|
| **A** Policy/Physical | **Größerer Share-Slot**, Pyramiding | MP |
| **B** AI-Infra | LEAP + Event-Call um Earnings | NOK |
| **C** Value MR | **50 %-Slot** wenn IV ok | — |
| **D** Security | Shares oder LEAP | FTNT |

**elliot Misery:** Challenge **toleriert** mehr Risk-on — Cash nur **10–15 %**, nicht Misery-optimiert. Bewusst.

---

## Aktuelles Book — Challenge-Mapping (2026-06-24)

| Ticker | Standard | Challenge-Vorschlag |
|--------|----------|---------------------|
| **MP** | 100 Sh (~55 % nach Trim) | **Core Policy 40 %** — Shares, 60 % now / 40 % Add auf Escalation |
| **NOK** | 5× $20C LEAP | **Core LEAP 35–40 %** — Hold; optional **Earnings-Call** 5 % |
| **NOW** | 1× $110C LEAP | **Prüfen:** IV ~66 % → **Shares 25 %** *oder* LEAP **nach** Q2; Catalyst-Call nur um Earnings |
| **FTNT** | watchlist | Slot D — **25 % Shares** wenn Entry |

**Migration:** Standard-Orders in IBKR **nicht duplizieren**. Challenge-`positions.challenge.json` = **Zielzustand** nach Profil-Wechsel / Re-Entry.

---

## Monitor & Alerts (Challenge)

| Parameter | Standard | Challenge |
|-----------|----------|-----------|
| Ticker-Cap Warnung | 40 % | **50 %** |
| Sektor-Cap | 60 % | **75 %** |
| Konzentration | Trim empfohlen | **OK bis Cap** — Review in S2 |

Config: `BOOK_PROFILE=challenge` in `.env` · `use_paper_challenge.ps1`

---

## Was wir **zusätzlich** traden (nur Challenge)

- **Short Calls 60–90 DTE** um **bestätigte** Earnings/Events (max 10 % NAV)  
- **ATM / 0-OTM LEAPs** wenn IV < 65 %  
- **40 % Add-Tranche** auf Gewinner-Thesis  

## Was weiterhin **tabu** ist

- Weeklies / 0DTE · Meme · Spread > 15 % · Auto-Execution · Blind PDF-Ticker kopieren

---

## Nächste Schritte (Challenge)

1. `.\scripts\use_paper_challenge.ps1`  
2. Book in `positions.challenge.json` pflegen (nicht Standard mischen)  
3. Offene Standard-Orders klären → Challenge-Zielgrößen neu S3  
4. Catalyst-Kalender in Universe (Earnings-Datum)  
5. Nach Fills: `run_daily.ps1` · Dashboard Tab **Portfolio**

---

## Changelog

| Datum | Änderung |
|-------|----------|
| 2026-06-24 | Profil B Challenge initial — User Upside-Chance |
