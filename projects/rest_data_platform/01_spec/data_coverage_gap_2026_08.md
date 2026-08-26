<!-- Reality Block
last_update: 2026-08-26
status: draft
scope:
  summary: "Kurzinventar: was aus 4C/MaStR/ERA5/CAPEX schon in der DB ist vs. Lücken und nächste Hol-Schritte."
  in_scope:
    - local DB coverage snapshot
    - prioritized next ingest/transform items
  out_of_scope:
    - full field catalogs
notes:
  - "Zahlen lokal Stand 2026-08-26; CAPEX/Events/ERA5-hourly nachgezogen."
-->

# Datenabdeckung — Lücken & nächste Hol-Schritte (2026-08-26)

## Kurzfassung

| Bereich | In DB (kuratiert) | Raw-Mirror | Nächster Schritt |
|---------|-------------------|------------|------------------|
| 4C Windfarms + Design | 3606 Farms, 3606 Design | ja | Stakeholders/Grid light optional |
| CAPEX/OPEX/Revenue | **befüllt** (~974 / ~17k / ~974 / ~421) | POP/LCOE | UI ok; Portfolio später |
| 4C Events | **~41k** gemappt im Detail | Events-Sheet | UI Streifen+Tabelle am Park |
| 4C Turbinen Specs | Pilot stark; Units MaStR | Specs 360 + on-farm 971 | Spec-Katalog + Links ausweiten |
| 4C VPI Vessels | **8 Katalog + 2210 Flotte** | Specs 2210, Contracts 17k | UI `/assets/vessels`; Contracts später; Wetter override Marc |
| 4C Cables/Auction/Floating | nicht kuratiert | Dateien lokal | Later |
| MaStR | 51 Parks agg, 33 Matches, 1593 Units | EEG/Einheiten | Rest-Matches; Unit-Enrichment |
| ERA5 daily | **3 Parks / 1858 Tage** | Cache | DE-Batch optional |
| ERA5 hourly | **AV CDS ~23k h** (2024-01→2026-08) | Cache | optional DE-Tagesbatch; weitere Parks |
| `ext_windfarm_id` | **~974** | — | Re-Run Windfarm-Transform |

## Wo stehen wir?

Stage-A Kern für Working Board + Partner-Drafts ist **da**: Farms, CAPEX, Events, Häfen/Natura light, ERA5 daily + hourly-Schema.  
**Blocker für Marc/Thomas:** IA-Review (nicht mehr Daten-ETL).

## Noch sinnvoll aus 4C / MaStR (ohne Scope-Sprengung)

1. **Stakeholders / OEM / Owners** (4C) — Supply-Chain light am Park  
2. **Grid / Export-Kabel Meta** (4C) — wo schon in POP, selten extra Sheet nötig  
3. **MaStR-Matches** ausweiten (heute ~33 accepted) + Unit-Felder anreichern  
4. **Turbinen-Spec-Katalog** an `imc_turbine_models` hängen (OEM, Rotor, …)  
5. **Vessel-Wetter final** — Katalog-Platzhalter → Marc-Override; Assignments später  
6. **Foundation-Messwerte** nur Pilot-Typen wenn Marc/Thomas brauchen  

## Nicht jetzt

CAPEX-Dashboard/Forecasts, Voll-VPI, GIS-Vollimport, Sim/LCA in der App.
