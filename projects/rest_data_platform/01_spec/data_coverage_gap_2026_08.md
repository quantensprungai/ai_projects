<!-- Reality Block
last_update: 2026-08-27
status: draft
scope:
  summary: "Kurzinventar: was aus 4C/MaStR/ERA5/CAPEX schon in der DB ist vs. Lücken und nächste Hol-Schritte."
  in_scope:
    - local DB coverage snapshot
    - prioritized next ingest/transform items
  out_of_scope:
    - full field catalogs
notes:
  - "Zahlen lokal Stand 2026-08-27; Grid/OHVS nachgezogen; MaStR Units 1651 (park_key-Fix)."
-->

# Datenabdeckung — Lücken & nächste Hol-Schritte (2026-08-27)

## Kurzfassung

| Bereich | In DB (kuratiert) | Raw-Mirror | Nächster Schritt |
|---------|-------------------|------------|------------------|
| 4C Windfarms + Design | 3606 Farms, 3606 Design | ja | stabil |
| 4C Grid light | **~1423** `imc_farm_grid` (DE ~120); Steckbrief | Project Details | POP modelled optional |
| 4C Platforms / OHVS | **~686** `imc_offshore_platforms`; Steckbrief Name·Typ·Owner | Platform Type | Shared ohne Farm-Link skipped |
| CAPEX/OPEX/Revenue | **befüllt** (~974 / ~17k / ~974 / ~421) | POP/LCOE | Portfolio UI live |
| 4C Events | **~41k** gemappt im Detail | Events-Sheet | UI Streifen+Tabelle am Park |
| 4C Turbinen Specs | Pilot stark; Units MaStR | Specs 360 + on-farm 971 | Spec-Katalog + Links ausweiten |
| 4C VPI Vessels | **8 Katalog + 2210 Flotte**; Contracts DE ~**1183** | Specs 2210, Contracts 17k | UI Einsätze+Sim-Rollen; kein 17k-Vollimport |
| 4C Supply Chain | DE ~**3633** Stakeholder-Links | Supply-Chain-Sheet | Park-UI Akteure; keine Decom-Ableitung |
| 4C Cables/Auction/Floating | nicht kuratiert | Dateien lokal | Later / Transmission bewusst nicht |
| MaStR | 51 Parks agg, **33 accepted**, 1 candidate, 1 rejected, **1651** Units | EEG/Einheiten | Rest nur bei klaren Namen (kein Rewrite) |
| ERA5 daily | **3 Parks / 1858 Tage** | Cache | DE-Batch optional |
| ERA5 hourly | **AV CDS ~23k h** (2024-01→2026-08) | Cache | optional DE-Tagesbatch; weitere Parks |
| `ext_windfarm_id` | **~974** | — | Re-Run Windfarm-Transform |

## Wo stehen wir?

Stage-A Backbone für Working Board + Partner-Drafts ist **da**: Farms, Grid/OHVS light, CAPEX, Events, Häfen/Natura light, ERA5, Akteure, VPI-Einsätze DE, Sim-Rollen-Pilot, MaStR Units.  
**Nächster Hebel:** Marc-Sync (nicht weitere ETL-Breite).

## Noch sinnvoll aus 4C / MaStR (ohne Scope-Sprengung)

1. ~~Stakeholders / OEM / Owners~~ (4C DE) — Park-UI Akteure  
2. ~~VPI-Contracts DE light~~ — Schiffseinsätze UI  
3. ~~Grid / Export-Kabel Meta~~ — `transform_4c_farm_grid.py` + Steckbrief  
4. ~~OHVS / Platforms light~~ — `transform_4c_platforms.py` + Steckbrief  
5. ~~MaStR-Matches Pipeline~~ — Accept/Apply/Units; Rest-Agg (Gode 1+2, Nordsee Ost Split, Bard-Cluster) bewusst offen  
6. **Turbinen-Spec-Katalog** an `imc_turbine_models` hängen (OEM, Rotor, …)  
7. **Vessel-Wetter final** — Katalog-Platzhalter → Marc-Override  

## Nicht jetzt

CAPEX-Forecasts, Voll-VPI (17k), GIS-Vollimport, `imc_transmission_assets`, Sim/LCA in der App, Decom-Steps aus 4C generieren.
