<!-- Reality Block
last_update: 2026-08-27
status: draft
scope:
  summary: "Interface Agreement Entwurf Plattform ↔ Marc (AnyLogic / Decom-Simulation)."
  in_scope:
    - input weather series hourly
    - park/port context export
    - vessel type catalog snapshot
    - sim output CSV back into DB
    - ownership matrix Plattform vs Marc
  out_of_scope:
    - running AnyLogic inside the platform
    - full VPI fleet import
    - continuous live sync / GIS routing product
notes:
  - "Grain decided for draft: hourly (user preference 2026-08-26). Daily remains derived KPI."
  - "Abnahme durch Marc erforderlich bevor Schema/ETL gebaut wird."
  - "2026-08-27: Transfer = Snapshot/Revision + Wetter on-demand CSV; kein Dauerstream. Barge-Typ offen."
-->

# Interface Agreement — Marc / AnyLogic (Draft v0)

Zweck: Verbindliche Vereinbarung zwischen **Marc (Simulation-Owner)** und **Plattform (Heiko)**, bevor Stunden-Wetter und Sim-Ergebnisse integriert werden.

## 1) Meta

| Feld | Wert |
|------|------|
| Modulname | Decom Logistics Simulation (AnyLogic) |
| Modul-Owner | Marc |
| Plattform-Owner | Heiko |
| Version | v0 (Draft) |
| Datum | 2026-08-27 |
| Status | **Draft** — Review mit Marc |

## 2) Fachlicher Scope

- **Ziel:** AnyLogic erhält reproduzierbare Wetter- und Kontext-Inputs aus Postgres und liefert Szenario-Ergebnisse zurück in die DB.
- **In Scope:** ERA5-basierte Zeitreihe Wind/Welle, Park-/Hafen-Kontext, optionale Vessel-**Typen**-Constraints (nicht Vollflotte), Sim-Output-CSV → `decom_*` (v2).
- **Out of Scope:** AnyLogic in der Plattform rechnen; VPI-Vollimport (17k Contracts); zweites paralleles CDS; Custom-Dashboard als Voraussetzung; **GIS-Produkt** (Routing/Polylinien) — Map-light (Leaflet + Attribute) reicht.
- **Transfer-Modell:** kein ständiger Export/Live-Stream. Statische Parameter → **Snapshot einmalig + Revision**; Wetter → **on-demand CSV** (siehe §3).
- **Stage:** A (Interface + Pilot Alpha Ventus), Erweiterung DE operational/under_construction danach.
- **Ampel:** Wetter ERA5 = Grün (Open Data); Vessel-Constraints = Gelb (4C/Typen); Kosten/CO₂-Outputs = Gelb bis Marc-Schema steht.

## 3) Lieferobjekte

### 3a) Plattform → Marc (Input)

| Objekt | Frequenz | Pilot |
|--------|----------|--------|
| Stunden-Wetterserie pro Park | on-demand Export / View | Alpha Ventus zuerst |
| Park-Kontext (1 Zeile) | Snapshot / mit Export | Alpha Ventus |
| Hafen-Kontext (Emden u. a.) | Snapshot / mit Export | Decom-Hafen Emden |
| Vessel-Typen-Katalog (5–8) | Snapshot einmalig + Revisions | nach Marc-Klärung |

### 3b) Marc → Plattform (Output)

| Objekt | Frequenz | Ziel |
|--------|----------|------|
| Sequenz-Vorlage (Schritte, Parallelität) | einmalig + Revisions | `decom_sequence_*` (v2) |
| Sim-Run-Ergebnis CSV | on-demand / pro Szenario | `decom_sim_runs` + Metrics |

### 3c) Transfer-Richtung (verbindlich Draft)

| Richtung | Was | Frequenz |
|----------|-----|----------|
| Plattform → Marc | Park/Port-Kontext, Vessel-Typen-Katalog, ERA5-Stunden | Snapshot / on-demand |
| Marc → Plattform | Sequenz-Vorlage, Sim-Run-CSV (optional) | Revision / Szenario |
| **Nicht** | Live-Stream Flotte, Dauer-Sync aller Parameter, Simulation in der App | — |

Erstliefertermin Input-Pilot: sobald Stunden-Ingest für AV steht.  
Erstliefertermin Output-Schema: mit Marc-Review dieses Dokuments.

## 3d) Owner-Matrix (Marc-Bedarf vs. Plattform-Ist)

| Marc-Bedarf | Owner | Plattform-Ist | Lücke |
|-------------|-------|---------------|-------|
| Windfarm LAT/LON | Plattform | ja (Overview/Karte) | — |
| Amount of OWT | Plattform | Design Turbinenanzahl + Einheiten (MaStR dünn) | MaStR-Breite optional |
| OHVS / MetMast | geteilt | Schema Platforms 0; Events/Freitext teils | leichtes Flag/ETL oder Marc-Annahme |
| OWT Components / Dimensions / Masses / Materials | Marc + Thomas | nicht in App (Scope Shield) | BOM/LCA-Spur; 4C-Specs nur Proxy später |
| MetOcean Wind/Wave/Windows | Plattform | ERA5 Tag+Stunde AV; CSV am Park | DE-Breite optional; Delays = Marc |
| Disassembly logistics / sequences / durations | Marc | nur Sim-Rollen-Pilot (Typ × Phase), keine Sequenz | bewusst Out of App |
| Vessel capacities / dayrates / fuel / speeds / jacking / avail | gemischt | Schema-Spalten da; Katalog dayrate/wind ~8; Speed/Crane oft aus VPI; Fuel 0; Jacking-Zeit fehlt | Katalog mit Marc befüllen, nicht Flotte scrapen |
| MetOcean restrictions | Marc defaults + Plattform Rohwerte | Wave-Limit ~131 Schiffe; Wind-Limit dünn | Schwellen in AnyLogic überschreibbar |
| Transfer routes | Marc (Annahme straight/real) | Hafen-Distanz km, keine Routen-Geometrie | kein GIS-Router jetzt |
| Ports LAT/LON | Plattform | ja | — |
| Port handling / capacities / companies / hinterland | Gelb | Häfen + Distanz; wenig Handling-Meta | Demo: Emden-Kontext; Rest Marc/später |

### Barges (offen mit Marc)

- Enum `imc_vessel_type`: **kein** generisches `barge` — nur **`jack_up_barge`** (Arbeits-Jack-up mit Beinen).
- Katalog: 1 Zeile `jack_up_barge`; Flotte praktisch nur Katalog (n≈1).
- Reine **Transport-/Feeder-Barges** (Pendulum/Feeder) sind **nicht** als Typ modelliert — landen ggf. in `other` oder fehlen.
- **Frage an Marc:** Braucht er `barge` / `feeder_barge` als eigenen Typ, oder reichen `heavy_lift` + `jack_up_barge` + Annahmen in AnyLogic?

## 4) Datenmodell — Input Wetter (Stunden)

**Entscheidung Draft:** Grain = **Stunde** (`timestamptz` UTC).  
Tagesmittel / `operable_day` bleiben **abgeleitete** KPI für Screener/UI — nicht zweite Wahrheitsquelle.

| Feld | Typ | Pflicht? | Beschreibung | Beispiel | Mapping |
|------|-----|----------|--------------|---------|---------|
| `farm_id` | uuid | ja | Interne Farm-ID | `…` | `imc_wind_farms.farm_id` |
| `ext_windfarm_id` | text | ja | 4C-Key | `DE01` | `imc_wind_farms.ext_windfarm_id` |
| `farm_name` | text | ja | Anzeigename | `Alpha Ventus` | `imc_wind_farms.name` |
| `ts_utc` | timestamptz | ja | Stundenstempel UTC | `2025-06-01T12:00:00Z` | neu: hourly table |
| `wind_ms` | numeric | ja | Windgeschwindigkeit 10 m (ERA5) | `8.4` | aus `u10`/`v10` |
| `hs_m` | numeric | nein* | Significant wave height | `1.1` | ERA5 wave; *null wenn Wave-Grid fehlt |
| `lat` / `lon` | numeric | ja | ERA5-Zellmittelpunkt | `54.00`, `6.50` | `imc_era5_grid_points` |

Optional später (nicht Blocker): `wind_dir_deg`, `gust`, `visibility`.

**Operable (nur KPI, nicht AnyLogic-Wahrheit):**  
Default-Schwellen 12 m/s Wind / 1,5 m Hs — in AnyLogic lokal nach Vessel-Typ überschreibbar. Plattform liefert Rohwerte + optional `operable_hour` mit dokumentierten Schwellen.

### Kontext-Zeilen (neben Zeitreihe)

| Feld | Quelle |
|------|--------|
| Foundation-Typ | kuratiert / Design |
| Capacity MW, #Turbinen | Design |
| Decom-Hafen, Distanz km | `imc_farm_ports` |
| Lifecycle | `lifecycle_phase` |

## 5) Datenmodell — Output Sim (Vorschlag, Marc bestätigt)

| Feld | Typ | Pflicht? | Beschreibung |
|------|-----|----------|--------------|
| `run_id` | text/uuid | ja | Szenario-Lauf |
| `farm_id` / `ext_windfarm_id` | uuid/text | ja | Join auf Register |
| `scenario_name` | text | ja | z. B. `baseline_emden` |
| `step_id` | text | ja | Sequenzschritt |
| `start_ts` / `end_ts` | timestamptz | ja | Sim-Zeit |
| `duration_h` | numeric | ja | Dauer |
| `vessel_type` | text | nein | Typencode |
| `cost_eur` | numeric | nein | |
| `co2_t` | numeric | nein | |
| `notes` | text | nein | |

## 6) Verknüpfung

- Primärschlüssel Input: `(farm_id, ts_utc)`
- Primärschlüssel Output: `(run_id, step_id)` bzw. Zeilen-ID
- Join: `ext_windfarm_id` (4C) + intern `farm_id`
- Fehlende Keys: Import reject mit Report (kein silent drop)

## 7) Lieferformat

| Richtung | Format | Encoding | Transport |
|----------|--------|----------|-----------|
| Plattform → Marc | CSV (UTF-8, `,`) + SQL-View | UTF-8 | Download am Asset-Detail / später API |
| Marc → Plattform | CSV (UTF-8, `,`) | UTF-8 | Upload/Storage oder manuell → ETL (Stage A) |

Dateiname Input-Vorschlag:  
`era5_hourly_{ext_windfarm_id}_{YYYYMMDD}_{YYYYMMDD}.csv`

Beispiel-Datei (3–5 Zeilen): **noch zu erzeugen** nach Stunden-Ingest AV.

## 8) Qualitätsregeln

- Pflicht: `farm_id`, `ts_utc`, `wind_ms`
- `hs_m` null erlaubt, wenn Wave nicht verfügbar — in Metadaten vermerken
- Keine Dubletten `(farm_id, ts_utc)`
- Source/Stand: `imc_data_sources` + Snapshot-Hash / CDS-Request-Metadaten
- Fehler: reject Zeile + Qualitätsreport

## 9) Akzeptanzkriterien

- [ ] Stunden-Export Alpha Ventus ≥ 30 Tage lückenarm
- [ ] Marc kann Serie in AnyLogic laden ohne manuelles Nachrechnen der Mittelwerte
- [ ] Join `ext_windfarm_id` funktioniert
- [ ] Sim-CSV-Stichprobe importierbar (sobald Schema freigegeben)
- [ ] Owner-Abnahme Marc
- [ ] Barge-/Feeder-Typ-Entscheidung dokumentiert (§3d)

## 10) RACI light

| Rolle | Wer |
|-------|-----|
| CDS/ERA5-Ingest, Views, Export | Plattform |
| Schwellen/Vessel-Typen, Sim-Logik | Marc |
| Sequenz Alpha Ventus (Tripod) | Marc |
| Schema `decom_*` Migration | Plattform nach Abnahme |

## 11) Risiken und Annahmen

| Risiko | Auswirkung | Mitigation |
|--------|------------|------------|
| Stunden ≈ 24× Speicher/CDS vs. Tag | DE-Batch teurer/langsamer | Zuerst Pilot-Parks stündlich; DE-Tagesbatch optional parallel |
| Wave-Grid ≠ Wind-Grid | `hs_m` Lücken | null + Flag; nächster CDS-Wave-Punkt |
| Marc braucht andere Variablen | Re-Export | IA Version bump |
| Transport-Barge fehlt im Enum | Feeder/Pendulum falsch typisiert | Marc bestätigt `jack_up_barge`+Annahme oder neuer Typ |

**Annahme:** CDS liefert bereits stündlich; aktuell aggregiert der Ingest auf **Tagesmittel** (`imc_era5_weather_windows`). Stunden speichern = Schema + Ingest-Änderung, nicht neue Datenquelle.  
**Annahme:** Statische Inputs ändern sich selten → Snapshot/Revision statt Dauer-Sync.

## 12) Offene Punkte (Marc)

1. Bestätigung **Stunden** (dieser Draft) vs. Tagesmittel nur für Screener?
2. Zeitraum Pilot (z. B. 2024–2026 YTD wie AV-Tage)?
3. Vessel-Typen-Liste: liefert Marc oder Plattform aus 4C-VPI-Aggregat?
4. Sim-Output-Spalten final?
5. **Barge:** eigener Typ `barge`/`feeder_barge` nötig, oder `heavy_lift` + `jack_up_barge` + AnyLogic-Annahmen?
6. Transfer routes: straight-line Annahme ok, oder später „real routes“ (dann erst GIS-Router)?

## 13) Entscheidung

- Entscheidungstermin: _TBD Team-Session_
- Freigegeben durch: _Marc + Heiko_

---

## Anhang — Ist-Stand Plattform (2026-08-27, lokal)

- Tabelle/View täglich: `imc_era5_weather_windows` / `imc_v_farm_era5_days` — 3 Parks / 1858 Tage
- Stunden: Alpha Ventus CDS ~23k h; UI Tag+Stunde + CSV-Export am Park
- DE-Batch (operational + under_construction, ~37 Parks): **nicht durch**
- Vessel-Katalog kuratiert (~8 Typen inkl. 1× `jack_up_barge`); Vollflotte nicht Marc-Input
- Map: Leaflet Map-light (Parks/Häfen/Attribute) — **kein** Routing-Produkt
