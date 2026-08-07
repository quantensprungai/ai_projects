<!-- Reality Block
last_update: 2026-08-07
status: active
scope:
  summary: "Thin Natura 2000 overlay (BfN marine FFH/SPA) for Assets map + farm proximity."
  in_scope:
    - imc_protected_areas
    - BfN WFS ingest
    - map toggle + detail nearest site
  out_of_scope:
    - full GIS layer tree (4C-style)
    - planning-grade geometry
    - land-only Natura outside marine BfN service
notes:
  - "Nicht für Planungszwecke (BfN Nutzungsbestimmung)."
-->

# Natura Overlay (DE marin) — thin Stage-A

## Entscheidung

**Kein 4C-GIS-Nachbau.** Eine Kontext-Schicht:

- Parks bleiben **Punkte** (Lifecycle-Farben)
- Natura = halbtransparente **Polygone** (Toggle)
- Detail: nächstes Gebiet + Distanz / Überlapp

## Quelle

- BfN WFS `schutzgebiet_marin`
- Layer: FFH + Vogelschutzgebiete (SPA)
- `source_id`: `a1000001-0002-4001-8001-000000000013`

## Lokal laden

```powershell
cd C:\Users\he5013\ai-projects\code\astra-imc-platform\apps\web
pnpm exec supabase migration up --local

cd C:\Users\he5013\ai-projects\projects\rest_data_platform\scripts\etl
python ingest_natura_bfn.py --replace
```

## UI

- Assets-Karte: Checkbox „Natura 2000 (BfN marin)“
- Asset-Detail: Feld „Nächstes Schutzgebiet“

## Bewusst nicht

Layer-Baum, Interconnectors, Measure/Compare, dunkles Maritime-Basemap.
