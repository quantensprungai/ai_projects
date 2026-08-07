<!-- Reality Block
last_update: 2026-08-07
status: draft
scope:
  summary: "2-Minuten Demo-Runbook Slice-1 Working Board (Alpha Ventus)."
  in_scope:
    - demo path
    - local prerequisites
  out_of_scope:
    - cloud deploy
    - upload
notes: []
-->

# Demo-Runbook — Slice 1 (Alpha Ventus)

Ziel: in **unter 2 Minuten** zeigen, dass ASTRA IMC ein belastbares Offshore-Asset-Register hat.

## Voraussetzung

```powershell
cd C:\Users\he5013\ai-projects\code\astra-imc-platform
pnpm supabase:web:start   # DB :54330
pnpm dev                  # App :3000
```

Optional nach Transform erneut kuratieren:

```powershell
Get-Content ..\..\projects\rest_data_platform\scripts\etl\curate_alpha_ventus.sql |
  docker exec -i supabase_db_next-supabase-saas-kit-turbo psql -U postgres -d postgres
```

## Pfad (sagen + klicken)

1. Öffnen: http://localhost:3000 → **Anmelden**
2. Account-Umschaltung → Team **makerkit**
3. Sidebar → **Assets**
4. Zeigen:
   - Default **Germany** + Status **Aktiv (ohne Cancelled)**
   - KPI: Parks / MW / In Betrieb · unter Bau
   - Banner **Pilot: Alpha Ventus**
5. **Alpha Ventus öffnen** (Banner oder Zeile)
6. Detail: Status In Betrieb, Foundation **Tripod**, Kuratierungsnotiz, **MaStR-Park / Inbetriebnahme**, **Turbine Areva M5000 + Senvion 5M**, Lat/Lon, Quelle 4C
7. Zurück → **CSV exportieren**

## Drei Sätze fürs Publikum

1. *Das ist unser Stage-A Working Board — kein 4C-Klon, Fokus Ostfriesland/Nordsee.*  
2. *Alpha Ventus ist der Vertical-Slice-Pilot: kuratiert, MaStR-angereichert, Turbinenmodelle verknüpft.*  
3. *Upload und DPP kommen später; heute: Register + Enrichment + Export.*

## Falls leer

- Falscher Account (nicht `makerkit`)
- Status-Filter auf einen einzelnen Lifecycle ohne Treffer
- `account_id` der Farms nicht am Team — siehe `ui_slice1_working_board.md`
