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
    - guessing unit type without MaStR Typenbezeichnung/Rotor
    - GIS turbine layout
    - replacing Thomas BOM with 4C weights
notes:
  - "4C Turbine on Windfarms = Typ am Park, keine WEA-IDs, AV zaehlt 12+12."
  - "Stufe 0 2026-09-18: MaStR hat Typ je WEA (AV 6+6); 4C-Gewichte gefuellt."
  - "Areva Wind → Adwen → Siemens Gamesa: Nameplate bleibt Areva; oem_group = Siemens Gamesa."
-->

# Plan — Einheiten × 4C-Specs × MaStR

Ziel: Thomas und die UI sehen **Typ-Physik** (4C) und **WEA-Identität** (MaStR) zusammen, ohne Massen aus 4C zur LCA-SoT zu machen und ohne Mixed-Parks zu erraten.

## Drei Körner (nicht vermischen)

| Korn | Quelle | Wo heute | Was fehlt |
|------|--------|----------|-----------|
| Park | 4C Windfarm | `imc_wind_farms` + design | — |
| **Typ** am Park | 4C `Turbine on Windfarms` + Specs | `imc_turbine_models` (OEM, Modell, MW, Ø, HH) + Farm-Link/Aliases | Specs/Measurements (Gewicht, Blatt, Getriebe, …) |
| **Einheit** | MaStR `EinheitenWind` | `imc_turbines` (SEE, Name, MW, Datum, Status, Punkt) | Hersteller, Typ, Nabe, Rotor, Tiefe, Küste — **im Payload**, nicht im Transform; `turbine_model_id` leer |

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
2. **Kein Raten** aus 4C-on-farm (zählt 12+12). Mixed-Parks: MaStR `Typenbezeichnung`/`Rotordurchmesser` ist der Join, wo gefüllt. Ohne MaStR-Typ bleibt die Einheit ohne Modell.
3. Specs leben am **Modell**, Einheiten **zeigen** das Modell wenn gelinkt.
4. Cloud: nur kuratierte Spalten, kein `imc_source_raw_rows`.

## Stufen

### 0 — Inventar AV (erledigt 2026-09-18)

Ergebnis: [`reference/imc/av_unit_spec_inventory_2026_09.md`](../reference/imc/av_unit_spec_inventory_2026_09.md). Skript: `scripts/etl/inventory_av_unit_specs.py`.

- 4C Specs **gefüllt** inkl. Rotor-/Blatt-/Gondelmasse (Senvion 130/24/325 t; Areva 112/16.5/233 t). Turm Senvion „Site-specific“, Areva 350 t.
- VPI Measurements = Kopie der Specs für diese zwei `TurbineId`s — nicht extra speichern.
- 4C on-farm: 2 Zeilen, **je 12** Turbinen (kein 6+6). VPI Foundation: **6 Tripod 700 t + 6 Jacket 500 t** und Text 6× Senvion.
- MaStR AV01–06 `REpower5M` / 126 m; AV07–12 `Areva Wind M5000` / 116 m. Typ **pro Einheit** war im Raw-Payload.

Abbruchkriterium Gewichte: **nicht** gegriffen. Stufe 2 darf `turbine_model_id` aus MaStR-Typ/Rotor setzen (kein Raten).

### 1 — Typ-Specs an `imc_turbine_models` (ETL + Migration)

Nullable Spalten + `specs jsonb` + `oem_group` (Areva-Linie → Siemens Gamesa). Massen `weights_are_proxy=true`.

ETL: `transform_4c_turbine_models.py`. VPI Measurements nicht separat, solange sie Specs duplizieren.

UI: Steckbrief 4C-Proxy-Massen + OEM-Gruppe wenn ≠ Nameplate.

### 2 — Mehr MaStR an `imc_turbines`

Kandidaten (nur wenn im Payload): Hersteller, Typenbezeichnung, Nabenhöhe, Rotordurchmesser, Seehöhe/Wassertiefe falls vorhanden.

`turbine_model_id` setzen wenn MaStR `Typenbezeichnung`/`Rotordurchmesser` eindeutig auf ein 4C-Modell **am selben Park** zeigt (AV: 126 m → Senvion 5M, 116 m → Areva M5000-116). Alias REpower↔Senvion, Areva↔Adwen↔Siemens Gamesa (`oem_group`). Nameplate bleibt Areva Wind.

UI-Einheiten: Spalte Typ (MaStR-Text) ≠ 4C-Modell (Join).

### 3 — Export an Thomas

`av_units.csv`: MaStR-Typ + Nabe/Rotor dürfen mit. 4C-Massen nur als Proxy-Hinweis am Typ. Foundation-Massen (VPI 700/500 t) nicht in die Turbinen-Stückliste.

### 4 — Nicht in dieser Spur

Foundation-Measurements-Tabelle, GIS-Punkte je WEA, EU-Register, Auto-Match Mixed-Parks.

## Reihenfolge vs. Rest

Nach Thomas-Kurzmail / Marc-Sync. Code erst nach Stufe 0 (AV-Stichprobe). Migrationen ins App-Repo; ETL bleibt im Meta-Repo bis stabil.

## Akzeptanz

- AV-Steckbrief: Typ-Specs sichtbar, Quelle 4C.
- AV-Einheiten: MaStR-Anreicherung ohne erfundenes Modell.
- Thomas kann BOM weiter je Typ füllen; Einheiten bleiben Anker.
- 4C-Gewicht ≠ importierte `mass_t`.
