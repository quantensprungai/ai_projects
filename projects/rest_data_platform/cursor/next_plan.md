<!-- Reality Block
last_update: 2026-08-26
status: active
scope:
  summary: "Aktiver Arbeitsplan ASTRA IMC — Grünwiese-Priorität, ohne Stage-A-Denkrahmen."
  in_scope:
    - next implementation order
    - glossary for events vs marc steps
  out_of_scope:
    - full roadmap rewrite
notes:
  - "Handover-Block in handover.md parallel aktualisieren."
  - "2026-08-26: Vessels-UI polish; Plan auf Logistics-Struktur + CDS-Stunden + CAPEX-Portfolio umgestellt."
  - "2026-08-26: CAPEX-Portfolio UI live (/assets/economics); CDS-Stunden AV 2024-01→2026-08 fertig (cds+hourly ~23k)."
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
| Vessels | Typenkatalog + Flotte + Day-Rates + Contracts (light) + Farm-Assignments |
| Economics | am Park + Portfolio `/assets/economics` (4C reported/modelled) |
| Partner | IA-Review Marc/Thomas parallel, blockiert nicht die Strukturarbeit |

## Ist (lokal, 2026-08-26)

| Baustein | Stand |
|----------|--------|
| ERA5 daily | 3 Parks / 1858 Tage |
| ERA5 hourly | **AV CDS** ~23 232 h (2024-01-01→2026-08-25, `cds+hourly`); Schema/Views/UI Tag+Stunde |
| CAPEX/OPEX/Events | in DB + am Asset-Detail |
| Vessel-Katalog / Flotte | 8 + 2210, UI `/assets/vessels` |
| `day_rate_eur` | Spalte da, **0 befüllt** |
| `imc_vessel_assignments` | Tabelle da, **0 Zeilen** |
| Vessel-Contracts | IMC-Tabelle + Pilotzeilen; VPI-Bulk (~17k) noch offen |
| CAPEX-Portfolio | UI `/assets/economics` — KPI, Filter, Sort, CSV, Link Detail |

### CDS-Stunden Alpha Ventus — Klarstellung

**Erledigt (lokal):** CDS-Mehrjahr AV in `imc_era5_hourly`, Provenance `cds+hourly`, UI Tag/Stunde + CSV am Park.  
**Optional danach:** DE-Tagesbatch Screener-KPI; weitere Parks stündlich nur bei Bedarf.

## Reihenfolge (jetzt)

1. ~~Logistics-Struktur~~ — Contracts + Day-Rate + Assignments + ERA5 Tag/Stunde UI  
2. ~~Partner-IA lesen / selbst entscheiden was geht~~ — siehe Abschnitt „IA-Selbstentscheidungen“  
3. ~~CAPEX-Portfolio-Seite~~ — `/home/[account]/assets/economics`  
4. ~~ERA5 Stunden CDS (echt)~~ — AV 2024-01→2026-08, `cds+hourly`  
5. **Locale-Persistenz** — Workspace-Switch hält `/en/` (WorkspaceDropdown + Team-Home-Redirect)  
6. Optional: ~~Stakeholders/OEM~~ (DE Supply Chain geladen); VPI-Contracts-Subset-ETL; DE-ERA5-Tagesbatch; i18n-Switcher in Team-Chrome

## IA-Selbstentscheidungen (ohne Partner-Warten)

### Marc — wir können selbst setzen (Draft → „vorläufig freigegeben Plattform“)

| Punkt | Vorschlag | Blockt CAPEX-Portfolio? |
|-------|-----------|-------------------------|
| Grain | **Stunde** (schon Draft) | nein |
| Zeitraum Pilot AV | **2024-01-01 → 2026-08** (wie Tages-Serie) bis Marc widerspricht | nein für Portfolio |
| Vessel-Typen | **unser Katalog (8)** bleibt Default; Marc override | nein |
| Sim-Output-Spalten | warten auf Marc | nein |
| CDS vs Synthetic | Stunden heute **synthetic** nur Pfadtest; echter CDS-Ingest = eigener Track | nein |

### Thomas — blockt CAPEX-Portfolio nicht

BOM/PCF/Toolwahl sind **LCA-Spur**. Portfolio braucht nur 4C Economics (schon in DB). Thomas-Offene bleiben für LCA/DPP.

### CAPEX-Portfolio — Scope den wir allein festlegen können

| In | Out (erst später) |
|----|-------------------|
| KPI: Parks mit reported / modelled / opex / revenue | Forecast-Kurven, Discounting |
| Filter: Land, Lifecycle, Capacity-Band | „eigene“ Schätzungen ohne 4C |
| Tabelle + Sort: Total CAPEX, €/MW, OPEX/yr, Mechanismus | Live-Marktpreise |
| Drill-down Link → Asset-Detail (Breakdown schon da) | AnyLogic-Kosten |
| Badge reported vs modelled (ⓘ) | Thomas-Massen |

Datenbasis lokal: reported ~974, modelled ~17k, opex ~974, revenue ~421 (wie Handover) — Portfolio = Aggregat/UI auf genau diesen Tabellen.

## Logistics — was „Struktur“ heißt (nicht Vollausbau)

| Teil | Sinnvoll jetzt | Später / nicht blind |
|------|----------------|----------------------|
| Day-Rate UI | Spalte im Katalog + Flotte; Katalog-Seed/Override | Markt-Scraper, Live-Charter |
| Contracts | Tabelle + Provenance + Pilot-Subset oder leere Liste | 17k Contracts blind importieren |
| Farm-Assignments | Tabelle nutzen, Pilot AV + 2–3 Schiffe, UI-Abschnitt | Historie aller VPI-Events |

**Jetzt strukturieren: ja.** Voll-ETL Contracts + dicke Day-Rate-Markt-UI: nein — erst Gerüst, dann Daten nach Quelle.

## CAPEX-Seite — wann?

Park-Detail hat CAPEX/OPEX/Erlöse schon. Eine **eigene CAPEX-/Portfolio-Seite** ist der nächste große UI-Block **nach** Logistics-Struktur (1) und idealerweise Stunden-Export (2) — sonst zwei dicke UI-Baustellen parallel ohne Logistik-Rückgrat.

## Klarstellungen (kurz)

- **Events ≠ Marc-Sequenz** — 4C Lifecycle vs. AnyLogic-Zerlegung  
- **VPI** — Specs = Flotte; Contracts = separates Sheet; Assignments = unsere Verknüpfung  
- Häfen/Natura: für Sim weiter Draft/Kai/decom-Rolle nachziehen, wenn Partner braucht  

## Nicht blind

AnyLogic/LCA in der App · MCP-Cloud-Seed · CAPEX-Forecast-Charts ohne Bedarf · Contracts-17k ohne Mapping
