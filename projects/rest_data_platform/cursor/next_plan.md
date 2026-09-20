<!-- Reality Block
last_update: 2026-09-20
status: active
scope:
  summary: "Aktiver Arbeitsplan ASTRA IMC — Cloud live; Waves-Drilldown; Marc-Sync / PR; Thomas LCA Decom-first."
  in_scope:
    - next implementation order
    - glossary for events vs marc steps
    - daten-backlog light
  out_of_scope:
    - full roadmap rewrite
    - GIS routing product
notes:
  - "2026-09-20: Typkarte Elektrik + imc_farm_foundations (~506/451); Commit 8661a570; Waves Jahr→Parks→Proxy+Lücken."
  - "2026-09-18: Plan Einheiten×4C-Specs×MaStR — cursor/unit_spec_integration_plan.md"
  - "2026-09-17: Thomas-Gespräch — openLCA 2; BOM-Light + Recycling in IMC via CSV; Decom C1–C4 zuerst; kein LCI-Spiegel. IA + Mail-Vorlage."
  - "2026-09-15: Analysis Runs Stufe 1+2 (imc_analysis_runs + API v0 + Park-UI); Live-Engine out of scope."
  - "2026-09-04: Coolify live; curated IMC-Daten in Cloud auf Team astra-imc (3606 Farms)."
  - "Handover-Block in handover.md parallel aktualisieren."
  - "2026-08-27: 4C Turbine-Modelle (~369 / ~619 Farms) im Steckbrief; Grid/OHVS; MaStR 1651 Units."
  - "2026-08-27: Grid light + OHVS/Platforms + MaStR park_key-Fix; Site-Design; Assets-IA; Vessel Marc-Felder."
  - "2026-08-26: Stakeholders/VPI DE; CAPEX-Portfolio; CDS-Stunden AV."
-->

# Aktiver Plan (2026-09-04)

## Wo liegt was?

| Artefakt | Pfad | Zweck |
|----------|------|--------|
| **Diesen Plan** | `cursor/next_plan.md` | Kurze To-do-Reihenfolge für Chats |
| **Handover** | `cursor/handover.md` | Copy-Paste Kontextblock für neuen Chat |
| **Team-Stand** | `04_communication/team_stand_plan_2026_08.md` | Narrative für Session/Folien |
| **IA Marc** | `01_spec/interface_agreement_marc_anylogic_v0.md` | Stunden-Wetter + Sim-CSV + Owner-Matrix |
| **IA Thomas** | `01_spec/interface_agreement_thomas_lca_v0.md` | BOM-Light + Recycling + C-Module; Mail: `04_communication/mail_thomas_lca_openlca_2026_09.md` |
| **Einheiten × Specs** | `cursor/unit_spec_integration_plan.md` | 4C-Typ-Specs + MaStR-WEA, ohne 4C-Massen als LCA-SoT |

## Zielbild (grün, nicht „Stage A genug“)

Plattform = **Offshore-Register + Logistik + Economics + Wetter + Waves**, aus dem Partner exportieren (CSV/Views), nicht in dem sie simulieren/LCA rechnen.

| Spur | Soll |
|------|------|
| Wetter | Tages- **und** Stundenreihen, Export am Park |
| Vessels | Typenkatalog + Flotte + Day-Rates + Contracts (light) + Sim-Rollen-Pilot |
| Economics | am Park + Portfolio `/assets/economics` (4C reported/modelled) |
| Waves | Gegenverkehr Ausbau/Rückbau `/assets/waves` — Jahr aufdröseln + Proxy-Rollup + Lückenliste (Produkt A light) |
| Karte | **Map-light** (Leaflet + Attribute) — kein GIS-Produkt/Router |
| Partner | IA-Review Marc/Thomas — **jetzt der Hebel**, nicht weitere ETL-Breite |

## Ist (lokal / Code, 2026-08-27)

| Baustein | Stand |
|----------|--------|
| Nav | **Assets → Waves → Economics → Vessels** (Labels DE=EN Produktbegriffe) |
| Waves | `/assets/waves` Dual-Serie MW; Jahr → Parkliste + Proxy-Massen-Rollup + Lückenliste; Filter vom Register |
| Park-Dossier | Steckbrief · Economics · Lebenszyklus · **Typkarte** · **Fundamente** · **Einheiten** · Standort · Wetter · Akteure · Schiffe · Szenarien |
| Site-Design | Steckbrief: Tiefe/Küste/Fläche/Wind; Register-Filter `depth` / `shore` |
| 4C Turbine-Typ | `imc_turbine_models` ~**369**; ~**619** Farms gelinkt; Steckbrief OEM·Modell·MW·Ø·HH (+ Multi-Typ-Aliases) |
| Grid / OHVS | `imc_farm_grid` ~**1423** (DE ~120); Platforms ~**686**; Steckbrief Landing/Export/Infield/OSS/OHVS (Owner) |
| MaStR | 51 agg · **33 accepted** · 1 candidate · 1 rejected · **1651** Units (park_key-Varianten) |
| ERA5 daily | 3 Parks / 1858 Tage |
| ERA5 hourly | **AV CDS** ~23 232 h (2024-01-01→2026-08-25, `cds+hourly`); UI Tag+Stunde + CSV |
| CAPEX/OPEX/Events | in DB + Asset-Detail + Portfolio `/assets/economics` |
| Vessel-Katalog / Flotte | 8 + 2210, UI `/assets/vessels`; Marc-Felder + Platzhalter (Fuel/Jacking/Avail) |
| Schiffseinsätze (VPI) | DE light ~**1183**; AV ~60; UI Filter; globale Tabelle scrollbar + Schiffname |
| Sim-Rollen (Pilot) | AV: CTV/SOV/WTIV × Phase (kuratiert); UI-Text ohne Partnernamen |
| Akteure | DE Supply Chain ~**3633**; Parties-CSV Export |
| Code-Branch | `feat/assets-ia-restructure` (gepusht) |
| Cloud | **Live:** https://imc.ostfriesland.ai · Team `astra-imc` · curated Daten 2026-09-04 = lokal (3606 Farms, 118 Häfen, 23k ERA5-h). Roh-Excel nicht in Cloud. Details: `cursor/cloud_bootstrap.md` |
| Locale / i18n | Workspace hält `/en/`; Message-Cache → Restart nach neuen Keys |

### Park-Blöcke (verbindlich)

| Block | Inhalt | Default |
|-------|--------|---------|
| Steckbrief | Stammdaten + Site-Design + **Netz/OHVS** | offen |
| Economics | CAPEX/OPEX + Link Portfolio | offen |
| Lebenszyklus | 4C Events | zu |
| **Typkarte (4C)** | Physik + Elektrik + Proxy-Massen (`weights_are_proxy`) | offen |
| **Fundamente (VPI)** | Typ × Stück × Proxy-Masse (`imc_farm_foundations`) | offen |
| Einheiten | MaStR-Stückliste — BOM-Anker (≠ 4C-Typ) | zu |
| Standort | Häfen | zu |
| Wetter | ERA5 | zu |
| Akteure | 4C Supply Chain + Parties-CSV | zu |
| Schiffe | VPI-Einsätze + Sim-Rollen | zu |
| Szenarien | Analysis Runs (AnyLogic/openLCA-Import) | zu |

### Logistik-Schichten am Park (verbindlich)

| UI | Quelle | Nutzen | Nicht |
|----|--------|--------|-------|
| **Akteure** | 4C Supply Chain | Demo, AAS-Parties light | Partner-Sequenz / Decom-Steps |
| **Schiffseinsätze (VPI)** | Vessel Contracts DE | Historie / Kontext | Sim-Plan, Day-Rate-Markt |
| **Sim-Rollen (Pilot)** | kuratierte Assignments | Typ×Phase Bridge | VPI-Historie ersetzen |

**Nicht ableiten:** Decom-Workflow aus Akteuren oder Contracts. Sequenz + BOM kommen von Partnern.

## Marc — Snapshot-Modell (kein Dauerstream)

| Richtung | Was | Frequenz |
|----------|-----|----------|
| Plattform → Marc | Park/Port-Kontext, Vessel-Typen-Katalog, ERA5-Stunden | Snapshot / on-demand |
| Marc → Plattform | Sequenz-Vorlage, Sim-Run-CSV (optional) | Revision / Szenario |
| Nicht | Live-Stream Flotte, Dauer-Sync, Simulation in der App | — |

Details + Owner-Matrix + Barge-Offenpunkt: `01_spec/interface_agreement_marc_anylogic_v0.md` §3c/3d.

**Barges:** Enum nur `jack_up_barge` — kein generisches Transport-/Feeder-`barge`. Mit Marc klären.

## Daten-Backlog (Slice-weise, kein Mega-Plan)

1. ~~Site-Design / Depth-Shore~~ · ~~Vessel Marc-Felder / Contracts-UI~~ · ~~Grid / OHVS~~ · ~~MaStR Units~~ · ~~4C Turbine-Modelle Steckbrief~~
2. Optional mit Marc: Day-Rates/Fuel/Jacking-Werte finalisieren (jetzt Platzhalter)
3. Rest-MaStR nur bei klaren Namen (Gode 1+2 / Nordsee Ost Split / Bard) — kein Rewrite
4. Routing/Polylinien erst wenn Marc „real routes“ will
5. Transmission / Spec-Vollbreite / DE-ERA5-Batch — nur bei konkretem Partner-Bedarf; Typ-Specs siehe `cursor/unit_spec_integration_plan.md`

## Was offen ist / was jetzt tun

| Priorität | Was | Warum |
|-----------|-----|--------|
| **1 Jetzt** | **Waves-Drilldown** — Jahr → Parks → Proxy-Rollup + Lückenliste | Gegenverkehr lesbar; Coverage sichtbar |
| **1 parallel** | **Marc-Sync** (Stunden-CSV, Katalog-Defaults, Barge, Snapshot-IA) | Fachblocker; ETL-Breite ist ausreichend |
| **1 parallel** | **PR** `feat/assets-ia-restructure` → main wenn Demo ok | Code einfrieren; Coolify+Cloud-Daten stehen |
| **2 Partner** | **Thomas:** Mail + AV-Stücklisten-CSV (Massen/Recycling) → Import; Impacts C1–C4; Shubham AAS | Massen kommen von Thomas, nicht aus 4C/openLCA-Dump |
| **2 parallel** | ~~Einheiten × Specs Stufe 1–2~~ — erledigt (`8661a570`); MaStR-Join Mixed-Parks weiter wo Payload klar | siehe unit_spec_integration_plan |
| **3 Optional** | DE-ERA5-Tagesbatch; Katalog-Zahlen mit Marc; MaStR-Rest nur klar | kein Sim-/BOM-Blocker |
| **Nicht** | Transmission-Vollimport, GIS-Router, Join über 4C-WEA-IDs, Contracts-17k, Live-AnyLogic/MCP | MaStR-Typ-Join ist ok |

**Pilot AV vs. andere:** Typ/Grid/OHVS/MaStR-Einheiten sind DE-breit wo gelinkt. AV bleibt dichter bei **ERA5-Stunden**, **Sim-Rollen**, Kuratierung (Emden/Tripod) und Demo-Pfad — nicht mehr „einziger Park mit Daten“.

## Reihenfolge (jetzt)

1. ~~… Grid/OHVS / MaStR / 4C-Turbine-Typ …~~ (Daten-Backlog light erledigt)  
2. ~~Einheiten×Specs Stufe 1–2 + VPI-Fundamente~~ (`8661a570`)  
3. **Waves-Drilldown** — Jahr → Parkliste → Proxy-Rollup + Lückenliste  
4. **Marc-Sync** — Stunden-CSV-Abnahme, Katalog-Defaults, Owner-Matrix/Barge in IA (§3d)  
5. Optional: DE-ERA5-Tagesbatch; Thomas BOM/LCA; Katalog-Werte final  
6. PR `feat/assets-ia-restructure` → main wenn Demo ok  

## IA-Selbstentscheidungen (ohne Partner-Warten)

### Marc — wir können selbst setzen (Draft → „vorläufig freigegeben Plattform“)

| Punkt | Vorschlag | Blockt CAPEX-Portfolio? |
|-------|-----------|-------------------------|
| Grain | **Stunde** (schon Draft) | nein |
| Zeitraum Pilot AV | **2024-01-01 → 2026-08** bis Marc widerspricht | nein |
| Vessel-Typen | **unser Katalog (8)** bleibt Default; Marc override | nein |
| Transfer | Snapshot + on-demand Wetter — kein Dauerstream | nein |
| GIS | Map-light; kein Router | nein |
| Sim-Output-Spalten | warten auf Marc | nein |
| Barge-Typ | offen (Frage in IA §3d) | nein |
| CDS vs Synthetic | AV Stunden = **CDS echt** | nein |

### Thomas — blockt CAPEX-Portfolio nicht

Tool **openLCA 2 + BAFU** (nicht ecoinvent). BOM/Recycling sind **LCA-Spur**; SoT nach CSV-Import in IMC. LCIA: EF 3.1, optional ReCiPe 2016, mehrere Kategorien. Portfolio braucht nur 4C Economics. Einheiten-Block = MaStR-Anker, keine Massen; 4C hat Typ-am-Park, nicht Typ-je-WEA.

## Logistics — was „Struktur“ heißt (nicht Vollausbau)

| Teil | Sinnvoll jetzt | Später / nicht blind |
|------|----------------|----------------------|
| Day-Rate UI | Spalte im Katalog + Flotte; Katalog-Seed/Override | Markt-Scraper, Live-Charter |
| Contracts | DE-Subset + UI Schiffseinsätze + scrollbare globale Tabelle | 17k Contracts blind |
| Farm-Assignments | Pilot Sim-Rollen AV | Historie aller VPI-Events als Assignments |

## Klarstellungen (kurz)

- **Events ≠ Partner-Sequenz** — 4C Lifecycle vs. Sim-Zerlegung  
- **Einheiten ≠ Lebenszyklus** — Inventar/BOM-Anker vs. Event-Timeline  
- **VPI** — Specs = Flotte; Contracts = Schiffseinsätze; Assignments = Sim-Rollen  
- Anteils-% bei Ownern: Freitext-Extrakt (~oft vorhanden), **kein** Cap-Table  

## Nicht blind

AnyLogic/LCA in der App · MCP-Cloud-Seed · CAPEX-Forecast-Charts ohne Bedarf · Contracts-17k ohne Mapping · Decom-Steps aus 4C generieren · Mega-Dashboard · GIS-Router / Mega-Datenplan
