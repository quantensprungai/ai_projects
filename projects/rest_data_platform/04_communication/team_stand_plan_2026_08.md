<!-- Reality Block
last_update: 2026-08-26
status: draft
scope:
  summary: "Stand + Plan 2026-08-26 und Ablauf für die Team-Session (Eisberg vor UI)."
  in_scope:
    - current status
    - near-term plan
    - presentation narrative
  out_of_scope:
    - slide design
    - cloud deploy
    - AAS exporter implementation
notes:
  - "Chat-SoT bleibt cursor/handover.md. Klickpfad: cursor/demo_runbook_slice1.md."
  - "Keine neue cursor/-Datei — Ordner ist voll."
  - "PPTX neu bauen optional: python scripts/build_team_session_pptx.py — Inhalt hier pflegen."
-->

# Stand, Plan, Team-Session — August 2026

**Zweck:** Einen gemeinsamen Stand festhalten und die nächste Team-Runde so führen, dass die Oberfläche nicht als „das war’s“ gelesen wird.

**Empfänger typisch:** Marc (AnyLogic), Thomas (LCA), Shubham (AAS/DPP), ggf. Projektleitung.

**Dauer Team-Session:** 25–30 Minuten (nicht 2-Minuten-Klickdemo).

---

## 1) Kurzfazit

- Backbone steht lokal: Register, Provenance, MaStR, Schutzgebiete, Häfen, ERA5 (Tag + Stunden-Pilot), CAPEX/OPEX/Events, Vessel-Katalog + VPI-Flotte.
- Die UI ist ein **Working Board auf diesem Register**, kein Produkt A (Screener) und kein DPP.
- Nächster inhaltlicher Schnitt: Partner-Review der IAs (Marc Stunden/Zeitraum; Thomas BOM). Simulation und Voll-DPP bleiben draußen.

---

## 2) Aktueller Stand (2026-08-26)

Zahlen lokal, abgeglichen **2026-08-26**.

**Folien:** [`ASTRA_IMC_Team_Stand_2026_08.pptx`](ASTRA_IMC_Team_Stand_2026_08.pptx) — Eisberg → Quellen → Schema-Visualizer → Board → Plan. Neu bauen (wenn Folien nachgezogen werden sollen): `python scripts/build_team_session_pptx.py`. **Dieses Markdown ist die inhaltliche SoT für die Präsi.**

**Landing (Code):** `de` + `en` aktiv (Default **de**) · Hero `working-board-hero-v2.png` · Sprachumschalter im Header.

### Was gebaut ist (Eisberg)

| Schicht | Inhalt |
|---------|--------|
| Plattform | Next.js/Makerkit + Supabase, Team-Accounts, RLS, Repo `astra-imc-platform` |
| Schema | `imc_*` v1/v1.2 + MaStR + Natura + Häfen + ERA5 daily/hourly + CAPEX/OPEX/Revenue/Events + Vessel-Katalog-Flag |
| Quellen | 4C Windfarm/POP/LCOE/Events/VPI Specs, MaStR-DE, BfN marin, Nordsee-Häfen, ERA5 CDS (+ AV Stunden-Pilot) |
| Provenance | `imc_data_sources`, Raw-Mirror, `source_id` an Ingests |
| Pilot | Alpha Ventus: Tripod, MaStR AV01–AV12, Emden, ERA5 Tag + ~720 h Pilot |
| UI Working Board | Assets: Liste/KPI/Filter/Karte/Zeitstrahl/Detail/CSV; CAPEX/OPEX/Erlöse + Events am Park; Wetter-CSV; **Vessels-Seite** Katalog + Flotte |

### Grobe Größenordnungen (lokal)

- Farms gesamt: **~3606**; DE aktiv (nicht cancelled): weiterhin ~76 mit Fokus Nordsee.
- MaStR: ~33 Parks accepted/applied, **1593** Einheiten.
- Schutzgebiete: **~205**.
- Häfen: **118** Ports, **677** Farm-Links; Distanz nicht überall; Draft/Kai leer.
- ERA5 daily: 3 Parks / **1858** Tage (AV, Albatros, Amrumbank West). DE-Batch nicht durch.
- ERA5 hourly: **AV Pilot ~720 h** (synthetic/CDS-Pfad); Grain für Marc-IA = Stunde.
- CAPEX/OPEX/Revenue: reported/summary ~974, modelled ~17k, opex ~974, revenue ~421; Events ~41k gemappt.
- Vessels: **8 Typenkatalog** + **2210** VPI-Instances; UI unter `/home/[account]/assets/vessels`. Hs in Flotte ~6 %; Katalog-Wetter = Platzhalter.
- Cloud-Projekt: pausiert; kein MCP-Chunk-Seed.

### Architektur, die gilt

- Postgres = System of Record. AAS = Interop/Export-Projektion, kein zweites Register.
- Marc/Thomas arbeiten **an der DB** (CSV/View). AAS ist für später externe Interop und den DPP-Prototyp.
- `operable` = Screener-KPI (Default 12 m/s / 1,5 m). Für AnyLogic zählen Reihen `day`/`hour` + `wind_ms` + `hs_m`.
- Vessel: **Katalog** = Sim-Defaults; **Flotte** = Referenz/Ops — nicht Farm-Detail.
- Produkt A = Decom Capacity Screener (noch nicht gebaut). Produkt B = DPP-Prototyp (Shubham, noch kein Exporter).

### Bewusst nicht drin (nicht vergessen)

| Fehlt | Warum | Owner |
|-------|--------|--------|
| BOM / Massen / GWP | Fachdaten Thomas | Thomas |
| Decom-Sequenz, Dauern, Kosten | Fachmodell Marc; Plattform simuliert nicht | Marc |
| AASX / semanticIds final | Form Shubham; Interface fehlt | Shubham + Heiko |
| Vessel-Weather final / Assignments | Platzhalter + Marc-Override; Assignments später | Marc / später |
| Upload, Custom-Dashboards, Cloud-Vollstand | Stage A | — |

---

## 3) Plan (als Nächstes)

Zwei Spuren parallel. Keine Spur blockiert die andere.

### Spur A — Daten / Screener-Bausteine

1. Partner-Review IA Marc (Stunden ok? Zeitraum? Vessel-Defaults von euch oder Override?).
2. ~~CAPEX-Portfolio UI~~ (`/assets/economics`) — reported/modelled aus 4C.
3. ~~CDS-Stunden Alpha Ventus~~ (2024-01→2026-08, `cds+hourly` ~23k h) + Stunden-CSV am Park.
4. Optional: DE-ERA5-Tagesbatch; Stakeholders/OEM/Grid light; VPI-Contracts light.
5. Cloud nur mit direktem `psql`/`DATABASE_URL`, nicht MCP.

### Spur B — Interop / DPP-Form

1. Heiko legt Industrie-Normen ab (IDTA, DPP/ESPR/CIRPASS, Shubham-Draft).
2. Gemeinsam mit Shubham: AAS-Schnitt Alpha Ventus + **Interface Agreement** DB→AAS.
3. Festziehen: Shell vs. DB-only (ERA5-Tage/Stunden, GIS-Joins, Vessel-Katalog).
4. Erst danach Code: AASX-Export / `dpp_templates`.

### Danach / geblockt auf Partner

- Thomas: BOM-Light + PCF → DB, dann AAS 02023.
- Marc: Sequenz-Vorlage + Sim-Output-CSV → DB (`decom_*` v2); Vessel-Wetter override.
- Upload erst bei konkretem Partner-CSV-Bedarf.

### Nicht tun

AnyLogic in der Plattform, VPI-Vertragsvollimport, zweites CDS parallel, MCP-Cloud-Seed, CAPEX-Forecast-UI vor IA-Freigabe.

---

## 4) Team-Session — Eisberg, dann Working Board, dann Plan

### Warum nicht mit der UI starten

Die Oberfläche ist absichtlich dünn (Scope Shield). Wer zuerst die Tabelle sieht, sagt: „simple, wo ist LCA, wo ist Simulation, wo ist der Pass?“  
Die richtige Reihenfolge: **Arbeit darunter → Oberfläche als Ergebnis → Lücken mit Owner und nächstem Schritt.**

### Ablauf (25–30 min)

| Min | Block | Was du tust | Was du nicht tust |
|-----|--------|-------------|-------------------|
| 0–3 | Rahmen | Zwei Produkte A/B. Dual-Track: DB = Wahrheit, AAS = Form. | App öffnen |
| 3–12 | Eisberg | Quellen, Matching, Provenance, Geo, Häfen, Wetter, CAPEX/Events, Vessel-Katalog. Alpha Ventus nennen. | Feature-Wunschliste aufnehmen |
| 12–20 | Working Board | Demo: Assets + Park-Detail (CAPEX/Events/Wetter) + **Vessels**-Seite (Katalog-CSV). | Alle Filter durchklicken |
| 20–27 | Nächste Schritte | Abschnitt 3. Pro Person ein Satz. | Zusagen Simulation/DPP-Produkt |
| 27–30 | Bitten | Was du von wem brauchst. | Offene Runde ohne Entscheidung |

### Drei Sätze, bevor jemand „da fehlt …“ sagt

1. *Was fehlt, ist benannt und hat einen Owner — das ist der Schnitt, nicht ein vergessenes Ticket.*  
2. *Die Plattform liefert Informationsgrundlagen, keine AnyLogic- und keine SimaPro-Rechnung.*  
3. *AAS kommt als Export unseres Registers, nicht als Ersatz. Marc und Thomas bekommen Daten aus der DB.*

### Satz pro Person

- **Marc:** Stunden-Wetter-Pilot + Vessel-Typenkatalog (CSV). Brauche: Zeitraum/Grain OK? Defaults override oder eigene Werte?
- **Thomas:** Register und Pilot stehen; Massen/GWP kommen von dir in die DB.
- **Shubham:** Sobald Normen da: Mapping + Interface Agreement. Du Form, ich Spalten und Keys.
- **Leitung:** Stage A = Register + Schnittstellen, kein Vollprodukt.

### Demo

Voraussetzung und Klickpfad: [`../cursor/demo_runbook_slice1.md`](../cursor/demo_runbook_slice1.md).  
Zusätzlich: `/home/research-team/assets/vessels` — Katalog + Flotte.  
Lokal Team-Slug oft **`research-team`**.

---

## 5) Verweise

- Chat-Handover: [`../cursor/handover.md`](../cursor/handover.md)
- Aktiver Plan: [`../cursor/next_plan.md`](../cursor/next_plan.md)
- Datenlücken: [`../01_spec/data_coverage_gap_2026_08.md`](../01_spec/data_coverage_gap_2026_08.md)
- Slice-1 UI: [`../cursor/ui_slice1_working_board.md`](../cursor/ui_slice1_working_board.md)
- Interface-Template: [`../01_spec/interface_agreement_template.md`](../01_spec/interface_agreement_template.md)
- Dual-Track Shubham: [`phase0_shubham_session_en.md`](phase0_shubham_session_en.md)
- Architektur: [`../02_system_design/architecture.md`](../02_system_design/architecture.md)
