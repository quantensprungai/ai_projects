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

## Nächste Skripte (Backlog)

- `ingest_era5.py` — CDS-API → v2-Tabellen (oder Raw-Mirror)
- `transform_4c_pop.py` / `transform_4c_vpi.py`
- Turbine-Transform auf weitere DE-Parks ausweiten
