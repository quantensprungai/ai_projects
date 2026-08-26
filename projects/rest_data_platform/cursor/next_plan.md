<!-- Reality Block
last_update: 2026-08-26
status: active
scope:
  summary: "Aktiver Arbeitsplan ASTRA IMC — Demo-Freeze Backbone, dann Marc-Sync."
  in_scope:
    - next implementation order
    - glossary for events vs marc steps
  out_of_scope:
    - full roadmap rewrite
notes:
  - "Handover-Block in handover.md parallel aktualisieren."
  - "2026-08-26: Stakeholders DE + VPI-Contracts DE + Park-UI (Akteure / Schiffseinsätze / Sim-Rollen)."
  - "2026-08-26: CAPEX-Portfolio UI; CDS-Stunden AV; Locale Workspace-Switch."
-->

# Aktiver Plan (2026-08-26)

## Wo liegt was?

| Artefakt | Pfad | Zweck |
|----------|------|--------|
| **Diesen Plan** | `cursor/next_plan.md` | Kurze To-do-Reihenfolge für Chats |
| **Handover** | `cursor/handover.md` | Copy-Paste Kontextblock für neuen Chat |
| **Team-Stand** | `04_communication/team_stand_plan_2026_08.md` | Narrative für Session/Folien |
| **IA Marc** | `01_spec/interface_agreement_marc_anylogic_v0.md` | Stunden-Wetter + Sim-CSV |
| **IA Thomas** | `01_spec/interface_agreement_thomas_lca_v0.md` | BOM/PCF |
| **Datenlücken** | `01_spec/data_coverage_gap_2026_08.md` | 4C/MaStR/ERA5/CAPEX Ist |

## Zielbild (grün, nicht „Stage A genug“)

Plattform = **Offshore-Register + Logistik + Economics + Wetter**, aus dem Partner exportieren (CSV/Views), nicht in dem sie simulieren/LCA rechnen.

| Spur | Soll |
|------|------|
| Wetter | Tages- **und** Stundenreihen, Export am Park |
| Vessels | Typenkatalog + Flotte + Day-Rates + Contracts (light) + Sim-Rollen-Pilot |
| Economics | am Park + Portfolio `/assets/economics` (4C reported/modelled) |
| Partner | IA-Review Marc/Thomas — **jetzt der Hebel**, nicht weitere ETL-Breite |

## Ist (lokal, 2026-08-26)

| Baustein | Stand |
|----------|--------|
| ERA5 daily | 3 Parks / 1858 Tage |
| ERA5 hourly | **AV CDS** ~23 232 h (2024-01-01→2026-08-25, `cds+hourly`); UI Tag+Stunde + CSV |
| CAPEX/OPEX/Events | in DB + Asset-Detail + Portfolio `/assets/economics` |
| Vessel-Katalog / Flotte | 8 + 2210, UI `/assets/vessels` |
| `day_rate_eur` | Katalog-Platzhalter gesetzt; Flotte/Contracts meist leer |
| Schiffseinsätze (VPI) | DE light ~**1183** in `imc_vessel_contracts` (`vpi:{id}`); AV ~60; UI Filter |
| Sim-Rollen (Pilot) | AV: CTV/SOV/WTIV × Phase (kuratiert, nicht aus VPI abgeleitet) |
| Akteure | DE Supply Chain ~**3633** Links; Park-UI Kernkacheln + Anteile (Freitext-%) + Gruppen |
| Locale / i18n | Workspace hält `/en/`; Message-Cache `cacheLife('max')` → Restart nach neuen Keys |

### Logistik-Schichten am Park (verbindlich)

| UI | Quelle | Nutzen | Nicht |
|----|--------|--------|-------|
| **Akteure** | 4C Supply Chain | Demo, AAS-Parties light | Marc-Sequenz / Decom-Steps |
| **Schiffseinsätze (VPI)** | Vessel Contracts DE | Historie / Kontext | Sim-Plan, Day-Rate-Markt |
| **Sim-Rollen (Pilot)** | kuratierte Assignments | Marc Typ×Phase Bridge | VPI-Historie ersetzen |

**Nicht ableiten:** Decom-Workflow aus Akteuren oder Contracts. Marc braucht eigene Sequenz (+ Thomas BOM für LCA).

## Reihenfolge (jetzt)

1. ~~Logistics-Struktur~~ · ~~CAPEX-Portfolio~~ · ~~CDS AV Stunden~~ · ~~Stakeholders DE~~ · ~~VPI-Contracts DE~~ · ~~Park-UI-Schliff~~  
2. **Demo-Freeze** — Stand committen; keine weiteren Light-ETLs ohne Bedarf  
3. **Marc-Sync** — Stunden-CSV-Abnahme, Katalog-Defaults, was er wirklich braucht (Sequenz/Sim-CSV)  
4. Optional: DE-ERA5-Tagesbatch Screener; Thomas BOM/LCA; i18n-Switcher in Team-Chrome  

## IA-Selbstentscheidungen (ohne Partner-Warten)

### Marc — wir können selbst setzen (Draft → „vorläufig freigegeben Plattform“)

| Punkt | Vorschlag | Blockt CAPEX-Portfolio? |
|-------|-----------|-------------------------|
| Grain | **Stunde** (schon Draft) | nein |
| Zeitraum Pilot AV | **2024-01-01 → 2026-08** bis Marc widerspricht | nein |
| Vessel-Typen | **unser Katalog (8)** bleibt Default; Marc override | nein |
| Sim-Output-Spalten | warten auf Marc | nein |
| CDS vs Synthetic | AV Stunden = **CDS echt** | nein |

### Thomas — blockt CAPEX-Portfolio nicht

BOM/PCF/Toolwahl sind **LCA-Spur**. Portfolio braucht nur 4C Economics (schon in DB).

## Logistics — was „Struktur“ heißt (nicht Vollausbau)

| Teil | Sinnvoll jetzt | Später / nicht blind |
|------|----------------|----------------------|
| Day-Rate UI | Spalte im Katalog + Flotte; Katalog-Seed/Override | Markt-Scraper, Live-Charter |
| Contracts | DE-Subset + UI Schiffseinsätze | 17k Contracts blind |
| Farm-Assignments | Pilot Sim-Rollen AV | Historie aller VPI-Events als Assignments |

## Klarstellungen (kurz)

- **Events ≠ Marc-Sequenz** — 4C Lifecycle vs. AnyLogic-Zerlegung  
- **VPI** — Specs = Flotte; Contracts = Schiffseinsätze; Assignments = unsere Sim-Rollen  
- Anteils-% bei Ownern: Freitext-Extrakt (~oft vorhanden), **kein** Cap-Table; `stake_value` oft MW/€  

## Nicht blind

AnyLogic/LCA in der App · MCP-Cloud-Seed · CAPEX-Forecast-Charts ohne Bedarf · Contracts-17k ohne Mapping · Decom-Steps aus 4C generieren
