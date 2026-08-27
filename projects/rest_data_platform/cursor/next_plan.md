<!-- Reality Block
last_update: 2026-08-27
status: active
scope:
  summary: "Aktiver Arbeitsplan ASTRA IMC — Site-Filter + Marc-IA Gap; Snapshot-Modell; Map-light."
  in_scope:
    - next implementation order
    - glossary for events vs marc steps
    - daten-backlog light
  out_of_scope:
    - full roadmap rewrite
    - GIS routing product
notes:
  - "Handover-Block in handover.md parallel aktualisieren."
  - "2026-08-27: Site-Design Steckbrief + Register Depth/Shore; IA Marc Owner-Matrix + Barge-offen; GIS=Map-light."
  - "2026-08-27: Assets-IA — Nav Waves, Gegenverkehr-Seite, Park-Dossier inkl. Einheiten; Branch feat/assets-ia-restructure."
  - "2026-08-26: Stakeholders DE + VPI-Contracts DE + Park-UI (Akteure / Schiffseinsätze / Sim-Rollen)."
  - "2026-08-26: CAPEX-Portfolio UI; CDS-Stunden AV; Locale Workspace-Switch."
-->

# Aktiver Plan (2026-08-27)

## Wo liegt was?

| Artefakt | Pfad | Zweck |
|----------|------|--------|
| **Diesen Plan** | `cursor/next_plan.md` | Kurze To-do-Reihenfolge für Chats |
| **Handover** | `cursor/handover.md` | Copy-Paste Kontextblock für neuen Chat |
| **Team-Stand** | `04_communication/team_stand_plan_2026_08.md` | Narrative für Session/Folien |
| **IA Marc** | `01_spec/interface_agreement_marc_anylogic_v0.md` | Stunden-Wetter + Sim-CSV + Owner-Matrix |
| **IA Thomas** | `01_spec/interface_agreement_thomas_lca_v0.md` | BOM/PCF |
| **Datenlücken** | `01_spec/data_coverage_gap_2026_08.md` | 4C/MaStR/ERA5/CAPEX Ist |

## Zielbild (grün, nicht „Stage A genug“)

Plattform = **Offshore-Register + Logistik + Economics + Wetter + Waves**, aus dem Partner exportieren (CSV/Views), nicht in dem sie simulieren/LCA rechnen.

| Spur | Soll |
|------|------|
| Wetter | Tages- **und** Stundenreihen, Export am Park |
| Vessels | Typenkatalog + Flotte + Day-Rates + Contracts (light) + Sim-Rollen-Pilot |
| Economics | am Park + Portfolio `/assets/economics` (4C reported/modelled) |
| Waves | Gegenverkehr Ausbau/Rückbau `/assets/waves` (Produkt A light) |
| Karte | **Map-light** (Leaflet + Attribute) — kein GIS-Produkt/Router |
| Partner | IA-Review Marc/Thomas — **jetzt der Hebel**, nicht weitere ETL-Breite |

## Ist (lokal / Code, 2026-08-27)

| Baustein | Stand |
|----------|--------|
| Nav | **Assets → Waves → Economics → Vessels** (Labels DE=EN Produktbegriffe) |
| Waves | `/assets/waves` Dual-Serie MW; Filter vom Register; CTA auf Assets-Liste |
| Park-Dossier | Steckbrief · Economics · Lebenszyklus · **Einheiten** · Standort · Wetter · Akteure · Schiffe |
| Site-Design | Steckbrief: Tiefe/Küste/Fläche/Wind; Register-Filter `depth` / `shore` |
| ERA5 daily | 3 Parks / 1858 Tage |
| ERA5 hourly | **AV CDS** ~23 232 h (2024-01-01→2026-08-25, `cds+hourly`); UI Tag+Stunde + CSV |
| CAPEX/OPEX/Events | in DB + Asset-Detail + Portfolio `/assets/economics` |
| Vessel-Katalog / Flotte | 8 + 2210, UI `/assets/vessels`; Marc-Felder + Platzhalter (Fuel/Jacking/Avail) |
| Schiffseinsätze (VPI) | DE light ~**1183**; AV ~60; UI Filter; globale Tabelle scrollbar + Schiffname |
| Sim-Rollen (Pilot) | AV: CTV/SOV/WTIV × Phase (kuratiert); UI-Text ohne Partnernamen |
| Akteure | DE Supply Chain ~**3633**; Parties-CSV Export |
| Code-Branch | `feat/assets-ia-restructure` ( gepusht ) |
| Locale / i18n | Workspace hält `/en/`; Message-Cache → Restart nach neuen Keys |

### Park-Blöcke (verbindlich)

| Block | Inhalt | Default |
|-------|--------|---------|
| Steckbrief | Stammdaten + Site-Design | offen |
| Economics | CAPEX/OPEX + Link Portfolio | offen |
| Lebenszyklus | 4C Events | zu |
| Einheiten | Turbinen/MaStR — BOM-Anker | zu |
| Standort | Häfen | zu |
| Wetter | ERA5 | zu |
| Akteure | 4C Supply Chain + Parties-CSV | zu |
| Schiffe | VPI-Einsätze + Sim-Rollen | zu |

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

1. ~~Site-Design Steckbrief~~ · ~~Register-Filter Depth/Shore~~ · ~~Marc-IA Gap-Review (Matrix + Barge)~~ · ~~Vessel-Katalog Marc-Felder (UI + Fuel/Jacking/Avail-Platzhalter)~~ · ~~Contracts-UI Kosmetik (scroll + Schiffname)~~
2. Optional: Day-Rates/Fuel mit Marc finalisieren (Werte sind Platzhalter)
3. Grid/OHVS/Turbinen-Specs/MaStR — eigene Stories
4. Routing/Polylinien erst wenn Marc „real routes“ verbindlich will

## Reihenfolge (jetzt)

1. ~~Logistics-Struktur~~ · ~~CAPEX-Portfolio~~ · ~~CDS AV Stunden~~ · ~~Stakeholders/VPI DE~~ · ~~Assets-IA (Waves + Dossier)~~ · ~~Site-Design + Depth/Shore-Filter~~ · ~~Vessel-Katalog Marc-Felder~~ · ~~Contracts-UI Kosmetik~~  
2. **Marc-Sync** — Stunden-CSV-Abnahme, Katalog-Defaults, Owner-Matrix/Barge in IA (§3d)  
3. Optional Daten-Backlog light: Katalog-Werte finalisieren; Einheiten BOM-Hinweis; DE-ERA5-Tagesbatch; Thomas BOM/LCA  
4. PR `feat/assets-ia-restructure` → main wenn Demo ok  

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

BOM/PCF/Toolwahl sind **LCA-Spur**. Portfolio braucht nur 4C Economics (schon in DB). Einheiten-Block ist der UI-Anker für spätere Massen.

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
