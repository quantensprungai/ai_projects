<!-- Reality Block
last_update: 2026-08-26
status: draft
scope:
  summary: "2-Minuten Demo-Runbook Slice-1 Working Board (Alpha Ventus)."
  in_scope:
    - demo path
    - local prerequisites
  out_of_scope:
    - cloud deploy
    - upload
    - team narrative
notes:
  - "Team-Runde nicht hiermit starten: 04_communication/team_stand_plan_2026_08.md (Eisberg vor UI)."
-->

# Demo-Runbook — Slice 1 (Alpha Ventus)

Ziel: in **unter 2 Minuten** zeigen, dass ASTRA IMC ein belastbares Offshore-Asset-Register hat.

**Team-Session:** Nicht mit diesem Pfad beginnen. Erst Vorarbeit/Eisberg, dann diese Klicks, dann Plan — [`../04_communication/team_stand_plan_2026_08.md`](../04_communication/team_stand_plan_2026_08.md).

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
2. Account-Umschaltung → Team **research-team** (lokal; nicht `makerkit`)
3. Sidebar → **Assets**
4. Zeigen:
   - Default **Germany** + Status **Aktiv (ohne Cancelled)**
   - KPI: Parks / MW / **Status aufgeschlüsselt** (klickbar)
   - Banner **Pilot: Alpha Ventus**
   - Filter **Hafen → Emden** (Liste, Karte, Zeitstrahl folgen)
   - **Karte:** OSM Parks (Lifecycle-Farben) + Toggle **Schutzgebiete BfN marin** + Toggle **Häfen**
   - **Zeitstrahl:** Rückbau ca. (Inbetriebnahme + Lifetime / 25 Jahre)
5. **Alpha Ventus öffnen** (Banner, Karten-Popup oder Zeile)
6. Detail kurz: Foundation **Tripod**, Häfen, **Wetter Tag/Stunde + CSV** (CDS-Stunden), **Akteure** (eingeklappt), **Schiffseinsätze (VPI)**, **Sim-Rollen (Pilot)**, Turbinen AV01–AV12
7. Optional: Sidebar **Economics** (Portfolio) · **Vessels** (Katalog-CSV)
8. Zurück → Spalten sortieren → **CSV der Filtermenge exportieren**

## Drei Sätze fürs Publikum

1. *Das Working Board sitzt auf dem Register — die schlanke Tabelle ist Absicht, nicht der ganze Stand.*  
2. *Alpha Ventus: MaStR-Units, Emden, CDS-Stunden, Akteure, VPI-Einsätze — Sim-Rollen sind kuratierter Marc-Bridge, nicht die Historie.*  
3. *Marc/Thomas lesen die DB; AAS/DPP ist Export darauf. Simulation und Voll-DPP sind Non-Scope.*

## Falls leer

- Falscher Account (nicht `research-team`)
- Status-Filter auf einen einzelnen Lifecycle ohne Treffer
- `account_id` der Farms nicht am Team — siehe `ui_slice1_working_board.md`
