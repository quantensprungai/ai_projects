<!-- Reality Block
last_update: 2026-09-20
status: active
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
  - "Stufe 1–2 2026-09-20: Specs jsonb + Elektrik auf Typkarte; imc_farm_foundations (~506/451); Commit 8661a570."
  - "Areva Wind → Adwen → Siemens Gamesa: Nameplate bleibt Areva; oem_group = Siemens Gamesa."
-->

# Plan — Einheiten × 4C-Specs × MaStR

Ziel: Thomas und die UI sehen **Typ-Physik** (4C) und **WEA-Identität** (MaStR) zusammen, ohne Massen aus 4C zur LCA-SoT zu machen und ohne Mixed-Parks zu erraten.

## Drei Körner (nicht vermischen)

| Korn | Quelle | Wo heute | Stand |
|------|--------|----------|-------|
| Park | 4C Windfarm | `imc_wind_farms` + design | — |
| **Typ** am Park | 4C `Turbine on Windfarms` + Specs | `imc_turbine_models` + Specs jsonb (Physik, Elektrik, Proxy-Massen) + Farm-Link/Aliases | Stufe 1 erledigt |
| **Einheit** | MaStR `EinheitenWind` | `imc_turbines` + MaStR-Typ/Nabe/Rotor wo Payload; `turbine_model_id` wo Join eindeutig | Stufe 2 light erledigt |
| **Fundament** am Park | VPI Fixed Foundation Measurements | `imc_farm_foundations` (Typ × Stück × Proxy-t) | erledigt (~506 / ~451 Parks) |

4C hat **keine** AV01–AV12. VPI `Turbine Measurements` hängt an `TurbineId` (= Modell), nicht an einer WEA.

## Was sonst noch ausgeklammert ist (nicht nur Turbinen)

Schon entschieden „später / nicht Stage-A-Register“:

| Block | Wo liegt es | Warum draußen |
|-------|-------------|---------------|
| VPI Platform / Floating Measurements | dieselbe VPI-xlsx | nicht in `imc_farm_foundations` |
| MaStR-XML-Rest (EEG, …) | Raw `payload` jsonb | nur Typ/Nabe/Rotor wo transformiert |
| Mixed-Parks ohne MaStR-Stückzahl je Typ | — | kein Raten aus 4C 12+12 |
| GIS-Layout / WFS | Scout, kein Import | kein Router |
| Transmission, Auction, Floating Tracker | Dateien lokal | nicht AV/Emden-Engpass |
| VPI Contracts 17k | DE-Subset ~1183 live | kein Vollimport |
| Helicopter Contracts | VPI-Sheet | ungenutzt |

Rohdaten sind da (lokal, nicht Cloud). Specs + Fundamente sind transformiert; Marketing-Felder (Selling Points) bleiben draußen.

## Leitplanken

1. **Thomas-BOM bleibt SoT für Massen/Recycling.** 4C-Gewichte = Vergleich / `is_proxy`, nie still überschreiben.
2. **Kein Raten** aus 4C-on-farm (zählt 12+12). Mixed-Parks: MaStR `Typenbezeichnung`/`Rotordurchmesser` ist der Join, wo gefüllt. Ohne MaStR-Typ bleibt die Einheit ohne Modell.
3. Specs leben am **Modell**, Einheiten **zeigen** das Modell wenn gelinkt.
4. Cloud: nur kuratierte Spalten, kein `imc_source_raw_rows`.
5. Waves-Proxy-Summen zeigen **Lückenliste** — fehlende Positionen nicht als 0.

## Stufen

### 0 — Inventar AV (erledigt 2026-09-18)

Ergebnis: [`reference/imc/av_unit_spec_inventory_2026_09.md`](../reference/imc/av_unit_spec_inventory_2026_09.md). Skript: `scripts/etl/inventory_av_unit_specs.py`.

- 4C Specs **gefüllt** inkl. Rotor-/Blatt-/Gondelmasse (Senvion 130/24/325 t; Areva 112/16.5/233 t). Turm Senvion „Site-specific“, Areva 350 t.
- VPI Measurements = Kopie der Specs für diese zwei `TurbineId`s — nicht extra speichern.
- 4C on-farm: 2 Zeilen, **je 12** Turbinen (kein 6+6). VPI Foundation: **6 Tripod 700 t + 6 Jacket 500 t** und Text 6× Senvion.
- MaStR AV01–06 `REpower5M` / 126 m; AV07–12 `Areva Wind M5000` / 116 m. Typ **pro Einheit** war im Raw-Payload.

Abbruchkriterium Gewichte: **nicht** gegriffen. Stufe 2 darf `turbine_model_id` aus MaStR-Typ/Rotor setzen (kein Raten).

### 1 — Typ-Specs an `imc_turbine_models` (erledigt 2026-09-20)

Nullable Spalten + `specs jsonb` + `oem_group` (Areva-Linie → Siemens Gamesa). Massen `weights_are_proxy=true`.

ETL: `transform_4c_turbine_models.py` + Cloud-Specs-Merge (~357 Modelle). VPI Turbine Measurements nicht separat, solange sie Specs duplizieren.

UI: Typkarte — Physik, Elektrik (Spannung/Frequenz/Umrichter), Leistungsregelung, Proxy-Massen + OEM-Gruppe wenn ≠ Nameplate.

### 2 — Mehr MaStR an `imc_turbines` (light erledigt)

Kandidaten (nur wenn im Payload): Hersteller, Typenbezeichnung, Nabenhöhe, Rotordurchmesser, Seehöhe/Wassertiefe falls vorhanden.

`turbine_model_id` setzen wenn MaStR `Typenbezeichnung`/`Rotordurchmesser` eindeutig auf ein 4C-Modell **am selben Park** zeigt (AV: 126 m → Senvion 5M, 116 m → Areva M5000-116). Alias REpower↔Senvion, Areva↔Adwen↔Siemens Gamesa (`oem_group`). Nameplate bleibt Areva Wind.

UI-Einheiten: Spalte Typ (MaStR-Text) ≠ 4C-Modell (Join).

### 2b — VPI-Fundamente (erledigt 2026-09-20)

Tabelle `imc_farm_foundations` (RLS, Proxy-Flag). ETL: `transform_vpi_foundations.py`. Cloud ~506 Zeilen / ~451 Parks. Park-UI-Block unter Typkarte. AV: 6× Tripod 700 t + 6× Jacket 500 t.

### 3 — Export an Thomas

`av_units.csv`: MaStR-Typ + Nabe/Rotor dürfen mit. 4C-Massen nur als Proxy-Hinweis am Typ. Foundation-Massen (VPI) eigener Block, nicht in die Turbinen-Stückliste.

### 4 — Nicht in dieser Spur

GIS-Punkte je WEA, EU-Register, Auto-Match Mixed-Parks ohne MaStR, Floating/Platform-Measurements, Thomas-BOM durch 4C ersetzen.

## Reihenfolge vs. Rest

~~Stufe 0–2 / Fundamente~~ erledigt. Nächstes UI: Waves-Drilldown (Jahr → Parks → Proxy + Lücken). Thomas-BOM bleibt Partner-Pfad.

## Akzeptanz

- ~~AV-Steckbrief: Typ-Specs sichtbar, Quelle 4C.~~
- ~~AV-Einheiten: MaStR-Anreicherung ohne erfundenes Modell.~~
- ~~Fundamente VPI am Park, Proxy-Badge.~~
- Thomas kann BOM weiter je Typ füllen; Einheiten bleiben Anker.
- 4C-Gewicht ≠ importierte `mass_t`.
