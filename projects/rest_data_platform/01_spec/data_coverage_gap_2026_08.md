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
  - "Zahlen lokal 2026-08-27: Grid/OHVS/Turbine-Models/MaStR 1651; nächster Hebel Marc-Sync nicht ETL."
-->

# Datenabdeckung — Lücken & nächste Hol-Schritte (2026-08-27)

## Kurzfassung

| Bereich | In DB (kuratiert) | Raw-Mirror | Nächster Schritt |
|---------|-------------------|------------|------------------|
| 4C Windfarms + Design | 3606 Farms, 3606 Design | ja | stabil |
| 4C Grid light | **~1423** `imc_farm_grid` (DE ~120); Steckbrief | Project Details | POP modelled optional |
| 4C Platforms / OHVS | **~686** Platforms; Steckbrief Name·Typ·Owner | Platform Type | Shared ohne Farm-Link skipped |
| 4C Turbinen Specs | **~369** Modelle; **~619** Farms gelinkt; Steckbrief Typ | Specs + on-farm | weitere Spec-Felder nur bei Thomas |
| CAPEX/OPEX/Revenue | **befüllt** (~974 / ~17k / ~974 / ~421) | POP/LCOE | live |
| 4C Events | **~41k** gemappt | Events-Sheet | ok |
| 4C VPI Vessels | **8 + 2210**; Contracts DE ~**1183** | Specs/Contracts | kein 17k-Vollimport |
| 4C Supply Chain | DE ~**3633** | Supply-Chain | ok |
| Transmission / Auction / Floating | nicht kuratiert | Dateien lokal | bewusst nicht |
| MaStR | 51 agg, **33 accepted**, **1651** Units | EEG/Einheiten | Rest nur klare Namen |
| ERA5 daily | **3 Parks / 1858 Tage** | Cache | DE-Batch optional |
| ERA5 hourly | **AV CDS ~23k h** | Cache | weitere Parks optional |

## Wo stehen wir?

Working-Board-Backbone **fertig** (inkl. Typ/Netz/OHVS/Einheiten).  
**Kein weiterer ETL-Mega-Slice nötig.** Nächster Hebel: **Marc-Sync** + PR → main.

## Erledigt (4C / MaStR light)

1. ~~Stakeholders DE~~ · ~~VPI-Contracts DE~~ · ~~Grid~~ · ~~OHVS~~ · ~~MaStR Units~~ · ~~Turbine-Modelle Steckbrief~~

## Offen (priorisiert)

| Prio | Item | Hinweis |
|------|------|---------|
| 1 | Marc IA-Abnahme | Stunden-CSV, Katalog-Werte, Barge, Snapshot |
| 1 | PR Branch → main | Demo-Freeze Code |
| 2 | Thomas BOM an Einheiten | nicht aus 4C ableiten |
| 2 | Shubham AAS-Schnitt | Interop, nicht Register |
| 3 | DE-ERA5 daily batch | Screener, optional |
| 3 | MaStR-Rest | nur klare Cases |
| — | Transmission, GIS-Router, unit-Join 4C↔MaStR | nicht jetzt |

## Nicht jetzt

CAPEX-Forecasts, Voll-VPI (17k), GIS-Vollimport, `imc_transmission_assets`, Sim/LCA in der App, Decom-Steps aus 4C.
