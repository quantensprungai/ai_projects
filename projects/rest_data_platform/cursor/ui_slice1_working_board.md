<!-- Reality Block
last_update: 2026-08-06
status: draft
scope:
  summary: "Slice-1 UI — Asset Working Board (Liste + Detail + CSV, kein Upload)."
  in_scope:
    - screens and fields
    - filter defaults
    - success criteria
  out_of_scope:
    - upload
    - GIS/charts
    - edit UI
notes:
  - "Implementierung: code/astra-imc-platform Team-Account /assets"
-->

# Slice-1 UI — Asset Working Board

Narrativ: *Offshore-Register für den Ostfriesland-/Nordsee-Kontext — Pilot Alpha Ventus.*

## Form

**Working Board** — KPI-Leiste + Dropdown-Filter + Tabelle + Detail.  
Kein BI-Dashboard, keine Regler/Charts, kein Upload in Slice 1.

## Screen A — Liste

Route: `/home/[account]/assets`

| Element | Inhalt |
|---------|--------|
| KPI | Parks (gefiltert), Summe MW, Anteil operational/unter Bau |
| Filter | Land (Default `Germany`), Lifecycle (Default `active` = ohne Cancelled), Suche Name |
| Tabelle | Name, Status, Kapazität MW, Turbinen, Foundation, Region, Quelle |
| Aktion | CSV der aktuellen Filtermenge |
| Pin | Alpha Ventus Banner/Hinweis, wenn in Filtermenge |

Daten: `imc_v_farm_overview` / `imc_wind_farms` (RLS via Team-Account).

## Screen B — Detail

Route: `/home/[account]/assets/[farmId]`

Read-only: Name, Land, Region, Sea/Georegion, Lifecycle, Kapazität, Turbinen, Foundation, Fixed/Floating, Lat/Lon (Text), Provenance. Leere Felder als `—`.

## Non-Goals

Upload, globales Weltregister ohne DE-Default, CAPEX/OPEX, Vessels/Ports, GIS, Charts/Slider, Edit-UI.

## Success

Team-Nutzer in &lt;30s: DE-Parks sehen → Alpha Ventus öffnen → CSV exportieren.

## Lokale Daten-Bindung

ETL schreibt `imc_wind_farms.account_id` auf `IMC_ETL_ACCOUNT_ID`. Für die Team-UI müssen die Zeilen dem Team-Account gehören, z. B.:

```sql
UPDATE public.imc_wind_farms
SET account_id = '<team-account-uuid>'
WHERE account_id = '<etl-account-uuid>';
```

Verifiziert 2026-08-06 (lokal): 181 DE-Parks, Alpha Ventus (`b3920ba9-…`), KPIs/Detail-Joins ok; Route `/home/makerkit/assets`.
