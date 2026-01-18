<!-- Reality Block
last_update: 2026-01-18
status: draft
scope:
  summary: "Konsolidierte Vision/Scope-Frame aus hd_system_raw + keep4/keep5 (entscheidungsrelevant, ohne MVP-Scope zu sprengen)."
  in_scope:
    - product frame
    - personas/schools as rendering layer
    - terminology strategy (canonical IDs vs labels)
    - decision hooks (what impacts architecture)
  out_of_scope:
    - detailed UX screens
    - implementation
notes:
  - "keep4/keep5 enthalten Ideen, die bewusst als vNext eingeordnet werden."
-->

# Vision & Scope Frame – HD‑SaaS (konservativ, entscheidungsrelevant)

## Nordstern (was das System am Ende sein soll)

Ein **HD Knowledge & Guidance System**, in dem:

- **Mechanik** (Type/Strategy/Authority/Definition/Chart‑Berechnung) deterministisch ist,
- **Wissen** (Schulen/Quellen) versioniert gespeichert ist,
- **Logik/Priorität** explizit modelliert wird (Precedence/Overrides),
- ein LLM als **Interface** arbeitet (Synthesis/Erklärung), aber nicht als “Speicher”.

## Zentrale Produkt-Idee aus `keep5`: Personas & “Schools” = Rendering Layer

Wir behandeln “Schulen/Perspektiven” (z.B. Business‑HD/64keys, Gene Keys, Classic Ra/IHDS, Mainstream) nicht als separate Apps, sondern als:

- **Persona/School = UI/UX Skin + Terminology Preference + Output Style**
- Die **Engine bleibt identisch** (gleiche Mechanik + gleiche Datenobjekte).

Das ist wichtig, weil es direkt beeinflusst, wie wir Daten speichern: **kanonische IDs** vs. **viele Labels/Varianten**.

## Terminologie-Strategie (entscheidungsrelevant)

Grundsatz:

- **Canonical Concept IDs** sind stabil (z.B. `hd.gate.34`, `hd.center.spleen`, `hd.profile.5_1`).
- Pro Concept können mehrere **Interpretations-/Label‑Layer** existieren:
  - `classic_ra` (Originalterminologie)
  - `business_64keys` (Business/Coaching Sprache)
  - `gene_keys` (Shadow/Gift/Siddhi Lens)
  - `mainstream` (zugänglicher Stil)
  - `custom_modern` (euer eigener Stil; “eigene Sprache”)

Ergebnis: Wir können später “eigene Sprache” bauen, ohne die Ontologie zu zerbrechen.

## Prioritäts-/Logik-Ebene (aus `hd_system_raw` + Notizen)

Wir brauchen zwei Arten von “Logik”:

- **Mechanische Regeln (hart, deterministisch)**: Type/Authority/Definition, Centers/Channels, Aktivierungen.
- **Interpretations- und Precedence‑Regeln (soft, versioniert)**:
  - “Authority > Mind”
  - “Beginner zuerst: Strategy & Authority”
  - dokumentierte Weights wie **Sun/Earth 70/30** (falls genutzt)
  - später: Heuristiken/Priorisierung für Output (was zuerst erklärt wird)

Das ist ein eigenes Datenobjekt (Rules/Precedence), nicht “nur Prompt”.

## Was ist jetzt wichtig vs. später?

### Jetzt wichtig (weil Architektur/Data‑Model beeinflusst)

- Canonical IDs + Layered interpretations (multi‑school kompatibel)
- Tenant‑Scoping (Makerkit `public.accounts`)
- Ingestion Slice (Korpus‑Aufbau intern) als Grundlage für Extraction/KG/Dynamics

### Später (Parking‑Lot, vNext)

- End‑User Uploads (Lebenslauf/Journaling)
- Multi‑Cultural “10 Systeme” Vision (beyond HD)
- Voice/Avatar/Content‑Formate (Story/AL‑Strang)

