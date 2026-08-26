# ETL — No-Regret Track (Phase 0)

Quelltreue Imports für ASTRA IMC. **Nicht** ins App-Repo — bis Pipeline stabil, dann nach `code/astra-imc-platform` verschieben.

## Voraussetzungen

1. **Schema:** IMC v1 + v1.2-Migrationen im App-Repo angewendet
2. **Raw-Mirror:** Tabellen `imc_source_snapshots` und `imc_source_raw_rows`
3. **Source-Katalog:** `imc_data_sources` inkl. `4c_turbine`
4. **Account:** `IMC_ETL_ACCOUNT_ID` = UUID aus `public.accounts`

### Lokal (empfohlen)

```powershell
cd C:\Users\he5013\ai-projects\code\astra-imc-platform
pnpm supabase:web:start
pnpm --filter web supabase migration list --local
```

Lokale DB-URL: `postgresql://postgres:postgres@127.0.0.1:54330/postgres`.
Der Port `54330` ist im App-Repo gesetzt, weil `54322` auf dieser Maschine mit IB Gateway / TWS kollidiert.

Account-ID ermitteln:

```sql
SELECT id, name, is_personal_account FROM public.accounts LIMIT 5;
```

### Python

```powershell
cd C:\Users\he5013\ai-projects\projects\rest_data_platform\scripts\etl
copy .env.example .env
# .env anpassen: IMC_ETL_ACCOUNT_ID setzen
pip install -r requirements.txt
```

## 4C A+-Raw-Ingest

Referenzdaten-Pfad (nicht committen):

`C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Reference_Data\`

```powershell
$env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:54330/postgres"

python ingest_raw.py --profile pop --file "C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Reference_Data\4C_POP_20260615.xlsx"
python ingest_raw.py --profile windfarm --file "C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Reference_Data\Offshore Wind Farm Database.xlsx"
python ingest_raw.py --profile turbine --file "C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Reference_Data\Offshore Wind Turbine Database.xlsx"
python ingest_raw.py --profile vpi --file "C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Reference_Data\Vessel & Ports Intelligence Database.xlsx"
```

Profile:

- `pop`: Header-Zeile 2, relevante Sheets `POP`, `LCOE`, `Corporate PPAs`
- `windfarm`: Header-Zeile 1, Projekt-/Supply-Chain-/Event-/Platform-Sheets
- `turbine`: Header-Zeile 1, Turbinenspezifikation und Turbine-on-Windfarms
- `vpi`: Header-Zeile 1, Vessel/Port/Measurement-Sheets

Minimaler Transform nach dem Raw-Ingest:

```powershell
$env:IMC_ETL_ACCOUNT_ID="5c064f1b-78ee-4e1c-ac3b-e99aa97c99bf"  # lokaler owner-Testaccount
python transform_4c_windfarm.py --latest
```

Alpha Ventus Pilot-Kuratierung (nach Transform):

```powershell
Get-Content .\curate_alpha_ventus.sql -Raw |
  docker exec -i supabase_db_next-supabase-saas-kit-turbo psql -U postgres -d postgres
```

Turbine-Minimal (Alpha Ventus / DE01):

```powershell
python transform_4c_turbine_alpha_ventus.py
python transform_mastr_turbines_farm.py --ext-windfarm-id DE01
# alle accepted DE-Matches:
python transform_mastr_turbines_farm.py --all-accepted
```

`transform_4c_windfarm.py` normalisiert leere Excel-Zellen zu `NULL` und kappt numerische Ausreißer auf die aktuellen v1-Spaltenlimits, statt den MVP-Transform zu blockieren.

Validierung:

```sql
SELECT count(*) FROM imc_source_raw_rows;
SELECT source_id, row_count, left(file_hash, 12) FROM imc_source_snapshots ORDER BY ingested_at DESC;
SELECT country, count(*) FROM imc_wind_farms GROUP BY 1 ORDER BY 2 DESC;
SELECT name, ST_AsText(location) FROM imc_wind_farms WHERE location IS NOT NULL LIMIT 5;
```

Stand 2026-06-24 lokal geladen:

- POP: 1852 Raw-Zeilen
- Offshore Wind Farm Database: 73423 Raw-Zeilen
- Offshore Wind Turbine Database: 1331 Raw-Zeilen
- Vessel & Ports Intelligence Database: 27296 Raw-Zeilen
- Gesamt: 103902 Raw-Zeilen
- Windfarm-Minimal-Transform: 3616 Quellzeilen verarbeitet; 3606 `imc_wind_farms` und 3606 `imc_farm_design`

## DQ (leicht)

```powershell
Get-Content .\dq_check_de_active.sql -Raw |
  docker exec -i supabase_db_next-supabase-saas-kit-turbo psql -U postgres -d postgres
```

Ergebnis-Ampel: `projects/rest_data_platform/cursor/dq_ampel_slice1.md`

- `ext_windfarm_id` und weitere 4C-externe IDs sind mit v1.2 `TEXT`.
- `imc_turbine_models.ext_turbine_model_key`, `imc_ports.ext_port_key` und `imc_vessels.ext_vessel_key` sind vorhanden.
- Detailfelder aus Turbinen-/Foundation-/Vessel-Messwerten bleiben zuerst im Raw-Mirror und werden nur bei konkretem MVP-Bedarf normalisiert.
- Alpha Ventus wird weiterhin kuratiert (`source_id` …032), falls die 4C-Daten den Pilot nicht ausreichend abdecken.

## MaStR-DE Matching (Skelett)

Doku: `projects/rest_data_platform/cursor/mastr_matching_de.md`  
Migration: `code/astra-imc-platform/.../20260807120000_imc_mastr_matching.sql`

XML-Ordner (empfohlen):

`C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Extraction\MaStR\`

```powershell
# nach migration up --local
$env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:54330/postgres"

# Default: EinheitenWind nur Offshore (WindAnLandOderAufSee=889) + EEG + Kataloge
python ingest_mastr.py --xml-dir "C:\Users\he5013\academiccloudsync\ASTRA_Maritime_Circularity\02_Data\Extraction\MaStR"
# optional alle Wind-Einheiten:
# python ingest_mastr.py --xml-dir "...\MaStR" --scope all-wind

python match_mastr_de.py --latest
Get-Content .\review_mastr_matches.sql -Raw |
  docker exec -i supabase_db_next-supabase-saas-kit-turbo psql -U postgres -d postgres
# nach Accept in SQL:
python apply_mastr_matches.py --dry-run
python apply_mastr_matches.py
```

Fixture bleibt für Smoke-Tests: `fixtures/mastr_units_offshore_sample.csv`.

## Natura 2000 (BfN marin)

```powershell
python ingest_natura_bfn.py --replace
```

Lädt FFH + SPA aus dem BfN-WFS `schutzgebiet_marin` nach `imc_protected_areas`.
Siehe `../../cursor/natura_overlay_de.md`.

## Nordsee-Häfen (VPI)

Voraussetzung: VPI-Raw-Ingest + Windfarm-Transform. Nur Farmen in DE/NL/DK/BE/UK/IE/NO; der Hafen darf in einem anderen Land liegen.

```powershell
$env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:54330/postgres"
python transform_4c_ports.py --latest
python geocode_ports.py
Get-Content .\curate_alpha_ventus.sql -Raw |
  docker exec -i supabase_db_next-supabase-saas-kit-turbo psql -U postgres -d postgres
```

### CAPEX / OPEX / Revenue (POP + LCOE)

```powershell
$env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:54330/postgres"
python transform_4c_capex.py --latest
```

Schreibt `imc_farm_capex_reported|modelled|summary`, `imc_farm_opex_*`, `imc_farm_revenue`. Setzt fehlende `ext_windfarm_id` per POP-`WindfarmId` (COALESCE).

### 4C Events (Lifecycle-Log)

```powershell
$env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:54330/postgres"
python transform_4c_events.py --latest
# optional nur gemappte Typen (ohne 'other'):
python transform_4c_events.py --latest --mapped-only
```

→ `imc_farm_events` (Consent, FID, Construction, First Power, Decom-Hinweise, …). **Nicht** Marc-Zerlegungssequenz.

- 4C-Excel hat **keine** Hafen-Lat/Lon. `geocode_ports.py` nutzt Nominatim + `ports_geocode_overrides.csv`.
- Cache: `scripts/etl/.cache/` (gitignore). Treffer außerhalb NW-Europa (BBox) werden verworfen; ohne Punkt bleibt der Name im Detail.
- Alpha Ventus `decom`→Emden nur, wenn 4C keine decom-Zeile geliefert hat.

Stand 2026-08-14 lokal:

- `imc_ports` 118 (109 mit Punkt, 9 ohne Marker)
- `imc_farm_ports` 677 (DE 184 / UK 294 / NL 72 / DK 52 / BE 44 / IE 20 / NO 11)
- Alpha Ventus: 4C O&M Borkum, Eemshaven, Norddeich, Wilhelmshaven; Installation Eemshaven + Wilhelmshaven; **decom Emden** kuratiert (4C hatte keinen decom-Link)

## ERA5 Wetterfenster

Generischer Punkt-Ingest (Standort aus `imc_wind_farms.location`). First run: Alpha Ventus; derselbe Befehl für jeden anderen Park mit Koordinaten.

```powershell
$env:DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:54330/postgres"
# Migration 20260814140000 (daily) + 20260826120000 (hourly) anwenden, dann:
python ingest_era5.py --farm-name "Alpha Ventus" --days 90 --synthetic
python ingest_era5.py --farm-name "Alpha Ventus" --days 30 --synthetic --grain hourly
# mit CDS-Account (Jahre werden intern gesplittet, Grid 0.25° gecacht):
python ingest_era5.py --farm-name "Alpha Ventus" --start 2025-01-01 --end 2026-08-12 --cds --grain both
python ingest_era5.py --country Germany --start 2025-01-01 --end 2026-08-12 --cds
```

- Tabellen: `imc_era5_grid_points`, `imc_era5_weather_windows` (Tag), `imc_era5_hourly` (Stunde)
- Views: `imc_v_farm_era5_context`, `imc_v_farm_era5_days`, `imc_v_farm_era5_hourly`, `imc_v_farm_era5_hourly_context`
- `--grain daily` (Default) = Screener-KPI; `--grain hourly` = Marc/AnyLogic; `--grain both` schreibt beides
- Defaults operable: Wind ≤ 12 m/s und Hs ≤ 1.5 m (CLI überschreibbar)
- `--synthetic` = deterministische Demo-Serie (kein CDS-Key); `--cds` = echte ERA5 über cdsapi
- Cache: `scripts/etl/.cache/era5/` je 0.25°-Zelle und Jahr. `--country Germany` nutzt vorhandene Zellen mit.
- Partner-Export: View `imc_v_farm_era5_hourly` → CSV `era5_hourly_{ext_windfarm_id}_…`
- Stand 2026-08-26: Stunden-Schema + Ingest `--grain hourly|both`; DE-Tagesbatch optional (nicht Marc-Ersatz)

## Stakeholders / Supply Chain (4C)

```powershell
# Unique-Index Migration 20260826190000, dann:
python transform_4c_stakeholders.py --latest --country Germany
# Vollimport:
python transform_4c_stakeholders.py --latest --all
```

- Quelle: Sheet `Windfarm Supply Chain` → `imc_orgs` + `imc_farm_stakeholders`
- Light-Default: nur `Country=Germany` (~3.6k Zeilen)
- UI: Park-Detail Abschnitt Stakeholders

## Vessel-Typen-Katalog + Flotte (Marc / VPI)

```powershell
# Migration 20260826140000_imc_vessel_type_catalog.sql, dann Katalog-Seed:
# seed_vessel_type_catalog.sql
# Flotte aus VPI Raw:
python transform_4c_vessels.py --latest
```

- Katalog: 8 Zeilen `is_type_catalog=true` (Sim-Defaults / Placeholder-Wetter)
- Flotte: ~2210 Instances `is_type_catalog=false`, `ext_vessel_key` = VPI `VesselId`
- View: `imc_v_vessels_anylogic` — Marc-Filter typischerweise `is_type_catalog = true`
- Inventar: `reference/imc/vpi_vessel_inventory_2026_08.md`
- Kategorie-Mapping: CTV→ctv, W2W→sov, Cable→cable_layer, Survey→survey, Heavy Maint.→heavy_lift, Rest→other (+ Original in `vessel_sub_type`)

## Nächste Skripte (Backlog)

- ~~Stakeholders Supply Chain~~ (`transform_4c_stakeholders.py`)
- Vessel-**Contracts** light (Subset, nicht 17k blind)
- Turbine-Transform auf weitere DE-Parks ausweiten
- optional DE-ERA5-Tagesbatch Screener-KPI
