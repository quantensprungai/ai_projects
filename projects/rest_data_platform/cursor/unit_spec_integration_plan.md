<!-- Reality Block
last_update: 2026-09-18
status: draft
scope:
  summary: "Plan: 4C Typ-Specs/Measurements + MaStR-WEA klug an Einheiten haengen, ohne 4C-Massen als LCA-SoT."
  in_scope:
    - grain map farm / type / unit
    - ETL + schema + UI sequence
    - what stays raw / later
  out_of_scope:
    - inventing AV01=Senvion
    - GIS turbine layout
    - replacing Thomas BOM with 4C weights
notes:
  - "4C Turbine on Windfarms = Typ am Park, keine WEA-IDs."
  - "MaStR EinheitenWind Rohpayload liegt schon im lokalen Raw-Mirror."
-->

# Plan — Einheiten × 4C-Specs × MaStR

Ziel: Thomas und die UI sehen **Typ-Physik** (4C) und **WEA-Identität** (MaStR) zusammen, ohne Massen aus 4C zur LCA-SoT zu machen und ohne Mixed-Parks zu erraten.

## Drei Körner (nicht vermischen)

| Korn | Quelle | Wo heute | Was fehlt |
|------|--------|----------|-----------|
| Park | 4C Windfarm | `imc_wind_farms` + design | — |
| **Typ** am Park | 4C `Turbine on Windfarms` + Specs | `imc_turbine_models` (OEM, Modell, MW, Ø, HH) + Farm-Link/Aliases | Specs/Measurements (Gewicht, Blatt, Getriebe, …) |
| **Einheit** | MaStR `EinheitenWind` | `imc_turbines` (SEE, Name, MW, Datum, Status, Punkt) | weitere MaStR-Felder; `turbine_model_id` fast immer leer |

4C hat **keine** AV01–AV12. VPI `Turbine Measurements` hängt an `TurbineId` (= Modell), nicht an einer WEA.

## Was sonst noch ausgeklammert ist (nicht nur Turbinen)

Schon entschieden „später / nicht Stage-A-Register“:

| Block | Wo liegt es | Warum draußen |
|-------|-------------|---------------|
| 4C Specs ~38 Felder (Cut-in, Generator, Blattmaterial, RotorWeightt, …) | Excel + Raw-Mirror | nur MW/Ø/HH transformiert |
| VPI Turbine / Foundation / Platform Measurements | dieselbe VPI-xlsx | v2, nicht voll normalisieren |
| MaStR-XML-Rest (Hersteller, Typ, Nabe, Rotor, EEG, …) | Raw `payload` jsonb | Transform schreibt 6 Felder |
| 4C↔MaStR Unit-Join | — | kein gemeinsamer Key |
| GIS-Layout / WFS | Scout, kein Import | kein Router |
| Transmission, Auction, Floating Tracker | Dateien lokal | nicht AV/Emden-Engpass |
| VPI Contracts 17k | DE-Subset ~1183 live | kein Vollimport |
| Helicopter Contracts | VPI-Sheet | ungenutzt |

Rohdaten sind da (lokal, nicht Cloud). Es fehlt Transform + schlanke Spalten, kein neuer Download.

## Leitplanken

1. **Thomas-BOM bleibt SoT für Massen/Recycling.** 4C-Gewichte = Vergleich / `is_proxy`, nie still überschreiben.
2. **Kein Raten** welches Exemplar Senvion/Areva ist. Mixed-Parks: Typ am Park; Einheit ohne Modell, bis Kuratierung oder belastbarer Match.
3. Specs leben am **Modell**, Einheiten **zeigen** das Modell wenn gelinkt.
4. Cloud: nur kuratierte Spalten, kein `imc_source_raw_rows`.

## Stufen

### 0 — Inventar AV (1 Sitzung, kein Schema)

- 4C Specs + VPI Measurements für die zwei AV-`TurbineId`.
- Ein MaStR-`payload` für AV01: welche Keys außer SEE/Name/MW/Datum/Status/LatLon.
- Kurz: was wäre für Thomas-BOM nützlich vs. nur Steckbrief.

Abbruchkriterium: wenn 4C-Gewichte leer/widersprüchlich → nur MaStR-Anreicherung, Specs als optional jsonb.

### 1 — Typ-Specs an `imc_turbine_models` (ETL + Migration)

Nullable Spalten oder `specs jsonb` + Provenance `source_id`: Blattzahl/-länge/-masse, Rotor-/Turm-/Gondelmasse, Getriebe, Generator — nur wo 4C/VPI gefüllt.

ETL: `transform_4c_turbine_models.py` erweitern (Specs ∪ Measurements, Konfliktregel: Measurements vor Specs oder umgekehrt, dokumentieren).

UI: Steckbrief „Typ“ um 4–6 Kennzahlen, Flag 4C/Proxy.

### 2 — Mehr MaStR an `imc_turbines`

Kandidaten (nur wenn im Payload): Hersteller, Typenbezeichnung, Nabenhöhe, Rotordurchmesser, Seehöhe/Wassertiefe falls vorhanden.

`turbine_model_id` setzen **nur** bei eindeutigem Park (ein 4C-Typ) oder nach Kuratierung. AV: erstmal leer lassen oder Pilot-Override 6+6 nur mit Quelle (Literatur), analog Tripod.

UI-Einheiten: Spalte Typ (MaStR-Text) ≠ 4C-Modell (Join).

### 3 — Export an Thomas

`av_units.csv`: MaStR-Felder + `turbine_model` wenn gelinkt, sonst leer. Keine 4C-Massen in die Stückliste kopieren — höchstens Hinweis „4C NacelleWeightt am Typ X = … (Proxy)“.

### 4 — Nicht in dieser Spur

Foundation-Measurements-Tabelle, GIS-Punkte je WEA, EU-Register, Auto-Match Mixed-Parks.

## Reihenfolge vs. Rest

Nach Thomas-Kurzmail / Marc-Sync. Code erst nach Stufe 0 (AV-Stichprobe). Migrationen ins App-Repo; ETL bleibt im Meta-Repo bis stabil.

## Akzeptanz

- AV-Steckbrief: Typ-Specs sichtbar, Quelle 4C.
- AV-Einheiten: MaStR-Anreicherung ohne erfundenes Modell.
- Thomas kann BOM weiter je Typ füllen; Einheiten bleiben Anker.
- 4C-Gewicht ≠ importierte `mass_t`.
