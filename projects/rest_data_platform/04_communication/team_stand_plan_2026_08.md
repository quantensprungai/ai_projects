<!-- Reality Block
last_update: 2026-08-27
status: draft
scope:
  summary: "Stand + Plan 2026-08-27 und Ablauf für die Team-Session (Eisberg vor UI)."
  in_scope:
    - current status
    - near-term plan
    - presentation narrative
  out_of_scope:
    - slide design polish beyond script rebuild
    - cloud deploy
    - AAS exporter implementation
notes:
  - "Chat-SoT bleibt cursor/handover.md. Klickpfad: cursor/demo_runbook_slice1.md."
  - "Keine neue cursor/-Datei — Ordner ist voll."
  - "PPTX neu bauen optional: python scripts/build_team_session_pptx.py — Inhalt hier pflegen."
  - "2026-08-27: Assets-IA (Waves, Dossier, Site-Filter), Vessel-Katalog Marc-Felder, Contracts-UI, Marc-IA Owner-Matrix."
  - "2026-08-26 Abend: Zahlen/UI auf Demo-Freeze nachgezogen (CDS h, Akteure, Schiffseinsätze, Economics)."
-->

# Stand, Plan, Team-Session — August 2026

**Zweck:** Einen gemeinsamen Stand festhalten und die nächste Team-Runde so führen, dass die Oberfläche nicht als „das war’s“ gelesen wird.

**Empfänger typisch:** Marc (AnyLogic), Thomas (LCA), Shubham (AAS/DPP), ggf. Projektleitung.

**Dauer Team-Session:** 25–30 Minuten (nicht 2-Minuten-Klickdemo).

---

## 1) Kurzfazit

- Backbone steht lokal: Register, Provenance, MaStR, Schutzgebiete, Häfen, ERA5 (Tag + **AV CDS-Stunden**), CAPEX/OPEX/Events, Vessel-Katalog + VPI-Flotte, Akteure DE, Schiffseinsätze DE light.
- Die UI ist ein **Working Board auf diesem Register** — mit **Waves** (Gegenverkehr light), Park-Dossier und Vessels-Katalog für Marc — kein Voll-Screener und kein DPP.
- **Demo-Freeze** für Light-ETLs gilt weiter. Nächster Hebel = **Partner-Sync Marc** (Stunden-CSV-Abnahme, Katalog-Werte, Barge-Typ, Sequenz).
- Simulation und Voll-DPP bleiben draußen. Decom-Steps werden **nicht** aus 4C-Akteuren/Contracts abgeleitet.
- Transfer-Modell mit Marc: **Snapshot + on-demand Wetter-CSV** — kein Dauerstream. GIS = **Map-light**, kein Router-Produkt.

---

## 2) Aktueller Stand (2026-08-27)

Zahlen lokal, abgeglichen **2026-08-26**; UI-Stand **2026-08-27** (Branch `feat/assets-ia-restructure`).

**Folien:** [`ASTRA_IMC_Team_Stand_2026_08.pptx`](ASTRA_IMC_Team_Stand_2026_08.pptx) — Eisberg → Quellen → Schema-Visualizer → Board → Plan. Neu bauen: `python scripts/build_team_session_pptx.py`. **Dieses Markdown ist die inhaltliche SoT für die Präsi** (PPTX optional/nachlaufend).

**Landing (Code):** `de` + `en` aktiv · Hero `working-board-hero-v2.png` · Sprachumschalter im Header. Workspace-Demo oft unter `/en/`.

### Was gebaut ist (Eisberg)

| Schicht | Inhalt |
|---------|--------|
| Plattform | Next.js/Makerkit + Supabase, Team-Accounts, RLS, Repo `astra-imc-platform` |
| Schema | `imc_*` v1/v1.2 + MaStR + Natura + Häfen + ERA5 daily/hourly + CAPEX/OPEX/Revenue/Events + Vessel (+ Jacking/Availability am Katalog) + Stakeholders |
| Quellen | 4C Windfarm/POP/LCOE/Events/VPI Specs+Contracts/Supply Chain, MaStR-DE, BfN marin, Nordsee-Häfen, ERA5 CDS |
| Provenance | `imc_data_sources`, Raw-Mirror, `source_id` an Ingests |
| Pilot AV | Tripod, MaStR AV01–AV12, Emden, ERA5 Tag + **~23k CDS-Stunden**, Akteure, Schiffseinsätze, Sim-Rollen-Pilot |
| UI Working Board | **Nav:** Assets → Waves → Economics → Vessels. Park-Dossier (Steckbrief inkl. Site-Design, Economics, Lebenszyklus, Einheiten, Standort, Wetter, Akteure, Schiffe). Register-Filter Depth/Shore. Waves Gegenverkehr. Vessels: Katalog Marc-Felder + CSV, Contracts DE light (Suche/Sort/Scroll), Flotte |

### Grobe Größenordnungen (lokal)

- Farms gesamt: **~3606**; DE aktiv (nicht cancelled): weiterhin ~76 mit Fokus Nordsee.
- MaStR: ~33 Parks accepted/applied, **1593** Einheiten.
- Schutzgebiete: **~205**.
- Häfen: **118** Ports, **677** Farm-Links; Distanz nicht überall; Draft/Kai leer.
- ERA5 daily: 3 Parks / **1858** Tage (AV, Albatros, Amrumbank West). DE-Batch nicht durch.
- ERA5 hourly: **AV CDS ~23 232 h** (2024-01→2026-08, `cds+hourly`). Grain für Marc-IA = Stunde.
- CAPEX/OPEX/Revenue: reported/summary ~974, modelled ~17k, opex ~974, revenue ~421; Events ~41k gemappt.
- Vessels: **8 Typenkatalog** + **2210** VPI-Instances; Schiffseinsätze DE ~**1183** (Linking Farm/Vessel erschöpft); Akteure DE ~**3633** Links.
- Cloud-Projekt: pausiert; kein MCP-Chunk-Seed.

### Architektur, die gilt

- Postgres = System of Record. AAS = Interop/Export-Projektion, kein zweites Register.
- Marc/Thomas arbeiten **an der DB** (CSV/View). AAS ist für später externe Interop und den DPP-Prototyp.
- `operable` = Screener-KPI (Default 12 m/s / 1,5 m). Für AnyLogic zählen Reihen `day`/`hour` + `wind_ms` + `hs_m`.
- Vessel-Schichten am Park (nicht vermischen):
  - **Akteure** = 4C Supply Chain (Owner/OEM/…) — Demo / AAS-Parties light
  - **Schiffseinsätze (VPI)** = historische echte Schiffe — Kontext, kein Sim-Plan, keine Day-Rates aus VPI
  - **Sim-Rollen (Pilot)** = kuratierte Typ×Phase für Marc — nicht VPI-Historie
- **Waves** = Produkt A *light* (Gegenverkehr MW/Parks) — kein voller Capacity Screener.
- Produkt B = DPP-Prototyp (Shubham, noch kein Exporter).

### Bewusst nicht drin (nicht vergessen)

| Fehlt | Warum | Owner |
|-------|--------|--------|
| BOM / Massen / GWP | Fachdaten Thomas | Thomas |
| Decom-Sequenz, Dauern, Kosten | Fachmodell Marc; Plattform simuliert nicht | Marc |
| AASX / semanticIds final | Form Shubham; Interface fehlt | Shubham + Heiko |
| Vessel-Wetter / Fuel / Jacking final | Katalog-Platzhalter → Marc-Override | Marc |
| Barge / Feeder als eigener Typ | Enum nur `jack_up_barge` — Frage an Marc | Marc |
| Upload, Custom-Dashboards, Cloud-Vollstand, GIS-Router | Stage A / Scope | — |

---

## 3) Plan (als Nächstes)

Zwei Spuren parallel. Keine Spur blockiert die andere.

### Spur A — Daten / Screener-Bausteine

1. **Partner-Review IA Marc** (Stunden-CSV ok? Zeitraum? Katalog-Defaults override? Barge-Typ? Snapshot-Modell bestätigt?).
2. ~~CAPEX-Portfolio UI~~ (`/assets/economics`).
3. ~~CDS-Stunden Alpha Ventus~~ (`cds+hourly` ~23k h) + Stunden-CSV am Park.
4. ~~Stakeholders DE~~ + ~~VPI-Contracts DE light~~ + Park-UI (Akteure / Schiffseinsätze / Sim-Rollen).
5. ~~Assets-IA~~: Waves, Park-Dossier, Site-Design-Filter, Vessel-Katalog Marc-Felder, Contracts-UI.
6. Optional: DE-ERA5-Tagesbatch Screener; Grid/OHVS/MaStR-Breite.
7. Cloud nur mit direktem `psql`/`DATABASE_URL`, nicht MCP.
8. PR `feat/assets-ia-restructure` → main wenn Demo ok.

### Spur B — Interop / DPP-Form

1. Heiko legt Industrie-Normen ab (IDTA, DPP/ESPR/CIRPASS, Shubham-Draft).
2. Gemeinsam mit Shubham: AAS-Schnitt Alpha Ventus + **Interface Agreement** DB→AAS (Parties aus Akteuren denkbar).
3. Festziehen: Shell vs. DB-only (ERA5-Tage/Stunden, GIS-Joins, Vessel-Katalog).
4. Erst danach Code: AASX-Export / `dpp_templates`.

### Danach / geblockt auf Partner

- Thomas: BOM-Light + PCF → DB, dann AAS 02023.
- Marc: Sequenz-Vorlage + Sim-Output-CSV → DB (`decom_*` v2); Vessel-Defaults override; Barge-Entscheidung.
- Upload erst bei konkretem Partner-CSV-Bedarf.

### Nicht tun

AnyLogic in der Plattform · VPI-Vertragsvollimport (17k) · Decom-Steps aus 4C generieren · zweites CDS parallel · MCP-Cloud-Seed · CAPEX-Forecast-UI vor Bedarf · GIS-Router / Mega-Datenplan.

---

## 4) Team-Session — Eisberg, dann Working Board, dann Plan

### Warum nicht mit der UI starten

Die Oberfläche ist absichtlich dünn (Scope Shield). Wer zuerst die Tabelle sieht, sagt: „simple, wo ist LCA, wo ist Simulation, wo ist der Pass?“  
Die richtige Reihenfolge: **Arbeit darunter → Oberfläche als Ergebnis → Lücken mit Owner und nächstem Schritt.**

### Ablauf (25–30 min)

| Min | Block | Was du tust | Was du nicht tust |
|-----|--------|-------------|-------------------|
| 0–3 | Rahmen | Zwei Produkte A/B. Dual-Track: DB = Wahrheit, AAS = Form. Snapshot≠Live-Stream. | App öffnen |
| 3–12 | Eisberg | Quellen, Matching, Provenance, Geo, Häfen, Wetter (**CDS-Stunden**), CAPEX/Events, Vessel-Katalog, Akteure. Alpha Ventus nennen. | Feature-Wunschliste aufnehmen |
| 12–20 | Working Board | Demo: Assets (Depth/Shore) → Waves → Park-Dossier (Steckbrief/Site, Wetter CSV, Akteure, Schiffseinsätze, Sim-Rollen) → Economics → Vessels (Katalog-CSV + Contracts Suche). | Alle Filter durchklicken; 17k Contracts versprechen; GIS-Router versprechen |
| 20–27 | Nächste Schritte | Abschnitt 3. Pro Person ein Satz. Fokus **Marc-Abnahme** (IA §3c/3d). | Zusagen Simulation/DPP-Produkt |
| 27–30 | Bitten | Was du von wem brauchst. | Offene Runde ohne Entscheidung |

### Drei Sätze, bevor jemand „da fehlt …“ sagt

1. *Was fehlt, ist benannt und hat einen Owner — das ist der Schnitt, nicht ein vergessenes Ticket.*  
2. *Die Plattform liefert Informationsgrundlagen, keine AnyLogic- und keine SimaPro-Rechnung.*  
3. *AAS kommt als Export unseres Registers, nicht als Ersatz. Marc und Thomas bekommen Daten aus der DB (Snapshot / on-demand).*

### Satz pro Person

- **Marc:** CDS-Stunden + CSV am Park + Vessel-Typenkatalog (Platzhalter inkl. Fuel/Jacking). Brauche: Zeitraum/Grain OK? Defaults override? Barge/Feeder eigener Typ? Sequenz-Vorlage wann?
- **Thomas:** Register und Pilot stehen; Massen/GWP kommen von dir in die DB (Einheiten-Block = UI-Anker).
- **Shubham:** Sobald Normen da: Mapping + Interface Agreement. Parties können an Akteure anknüpfen. Du Form, ich Spalten und Keys.
- **Leitung:** Stage A = Register + Schnittstellen, kein Vollprodukt. Demo-Freeze + IA-Draft — Partner-Hebel jetzt.

### Demo

Voraussetzung und Klickpfad: [`../cursor/demo_runbook_slice1.md`](../cursor/demo_runbook_slice1.md).  
Zusätzlich zeigen: `/assets/waves` · `/assets/economics` · Park Alpha Ventus (Dossier) · `/assets/vessels` (Katalog + Contracts).  
Lokal Team-Slug oft **`research-team`**. Branch: `feat/assets-ia-restructure`.

---

## 5) Verweise

- Chat-Handover: [`../cursor/handover.md`](../cursor/handover.md)
- Aktiver Plan: [`../cursor/next_plan.md`](../cursor/next_plan.md)
- IA Marc: [`../01_spec/interface_agreement_marc_anylogic_v0.md`](../01_spec/interface_agreement_marc_anylogic_v0.md)
- Datenlücken: [`../01_spec/data_coverage_gap_2026_08.md`](../01_spec/data_coverage_gap_2026_08.md)
- Slice-1 UI: [`../cursor/ui_slice1_working_board.md`](../cursor/ui_slice1_working_board.md)
- Interface-Template: [`../01_spec/interface_agreement_template.md`](../01_spec/interface_agreement_template.md)
- Dual-Track Shubham: [`phase0_shubham_session_en.md`](phase0_shubham_session_en.md)
- Architektur: [`../02_system_design/architecture.md`](../02_system_design/architecture.md)
