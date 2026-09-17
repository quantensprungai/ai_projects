<!-- Reality Block
last_update: 2026-09-17
status: draft
scope:
  summary: "Interface Agreement Plattform ↔ Thomas (LCA / BOM-Light / openLCA). Decom-first, kein ecoinvent-Spiegel."
  in_scope:
    - BOM-Light masses and recyclability from Thomas into IMC
    - PCF / C-module impact results back into DB
    - in/out workflow and SoT split vs openLCA/ecoinvent
    - mapping toward AAS 02023 later
  out_of_scope:
    - running openLCA inside the platform
    - inventing masses in the UI
    - mirroring ecoinvent process catalog in Postgres
    - live IPC/API in Stage A
notes:
  - "2026-09-17 Gespräch: openLCA 2 + ecoinvent vorhanden. BOM-Light ok. Start nur Decommissioning (C), nicht Produktion (A)."
  - "Abnahme durch Thomas (schriftlich) bevor Import-Pipeline gebaut wird."
-->

# Interface Agreement — Thomas / LCA & BOM (Draft v0.1)

Zweck: Verbindliche Vereinbarung zwischen **Thomas (LCA/BOM-Owner)** und **Plattform (Heiko)**.

Stand nach Gespräch **2026-09-17:** Tool **openLCA 2 + ecoinvent** (bei Thomas vorhanden). BOM-Light, weil öffentlich wenig belastbare Massen. Start **Rückbau (C1–C4)**, nicht Produktion (A1–A3). Feinspezifikationen (Stahlgüte, Fahrzeugjahr, …) bleiben in openLCA — **kein ecoinvent-Spiegel** in IMC.

Mail-Vorlage: [`../04_communication/mail_thomas_lca_openlca_2026_09.md`](../04_communication/mail_thomas_lca_openlca_2026_09.md)

## 1) Meta

| Feld | Wert |
|------|------|
| Modulname | LCA / BOM-Light / PCF (Decom-first) |
| Modul-Owner | Thomas |
| Plattform-Owner | Heiko |
| Version | v0.1 (Draft nach Gespräch) |
| Datum | 2026-09-17 |
| Status | **Draft** — schriftliche Abnahme Thomas ausstehend |

## 2) Fachlicher Scope

- **Ziel:** Register liefert Asset-Anker; Thomas recherchiert Massen + Recycling und rechnet in openLCA; Plattform speichert versionierte Stückliste und Impacts (Park-UI, später DPP/AAS).
- **In Scope:** BOM-Light, Recyclability-Felder, GWP (und später weitere Kategorien) je C-Modul, Provenance (Methode, ecoinvent-Version, Proxy-Flag), optional Dataset-UUID als Referenz.
- **Out of Scope:** openLCA in der Plattform rechnen; Massen in der UI schätzen; ecoinvent-Katalog / Stahlgüten / Lkw-Jahre in Postgres; Live-IPC in Stage A; A1–A3 bis bessere BOM.
- **Stage:** A — Pilot Alpha Ventus / REpower 5M / Tripod.
- **Ampel:** Workflow/Schema = Grün; konkrete Massen/GWP = Gelb bis erste CSV; Offshore-Korrekturen = Gelb.

## 2b) SoT-Schnitt (verbindlich)

| Sache | Source of Truth | Nicht |
|-------|-----------------|-------|
| Park, Einheiten, Foundation, Decom-Jahr, Distanz | IMC | — |
| Massen, Recyclingweg, Recyclingquote | Thomas-Sheet → nach Import **IMC** | nicht UI, nicht ecoinvent-Export |
| Stahlgüte, Fahrzeugjahr, Strommix, LCI-Prozess | **openLCA / ecoinvent** | nicht IMC-Stammdaten |
| kg CO₂-eq (und andere Impacts) | openLCA-Lauf → IMC Ergebniszeile | nicht in der App nachrechnen |

Wenn Sheet und openLCA auseinanderlaufen, gilt für die Plattform die **importierte CSV**. Thomas rechnet mit denselben Vordergrundzahlen. Neue Version = neue `as_of`-Zeilen, kein stilles Überschreiben.

## 3) Workflow (Stage A, dateibasiert)

```
1. Kontext raus          IMC → Thomas
2. Recherche             Thomas (Massen, Recycling, Quelle, Proxy)
3. Stückliste rein       CSV → IMC  (= SoT BOM + Recycling)
4. Rechnen               openLCA (dieselben Massen; ecoinvent nur Hintergrund)
5. Impacts rein          CSV → IMC (engine=openlca, C1–C4)
6. Anzeigen              Park-Dossier
```

IPC/REST (`Tools > Developer tools > IPC Server`, [olca-ipc](https://greendelta.github.io/openLCA-ApiDoc/)) erst, wenn 3+5 zweimal manuell geklappt haben. JSON-LD-Export des **Foreground-Product-Systems** optional als Archiv, nicht als Register-Inhalt. Kein Full-Database-Dump.

## 4) Lieferobjekte

### 4a) Plattform → Thomas (In)

| Objekt | Inhalt |
|--------|--------|
| Farm + Design | Name, `ext_windfarm_id`, Capacity, #Turbinen, Foundation, Turbine-Modell |
| MaStR-Einheiten (DE) | wo gematcht: Unit-IDs, Inbetriebnahme (BOM-Anker, keine Massen) |
| Decom-Kontext | `planned_decom_year` / Events; optional Dauer/Schiffstyp/Distanz aus Marc-Lauf |
| Optional | CAPEX-% zur Gewichtung (kein Blocker) |

Format: CSV/XLSX aus Register. Kein AAS.

### 4b) Thomas → Plattform (Out)

Zwei Dateien, zwei Rhythmen:

| Objekt | Frequenz | Ziel |
|--------|----------|------|
| Stückliste BOM-Light + Recycling | einmalig + Revisions (`as_of`) | `imc_bom_*` (v2; bis dahin Staging-CSV) |
| Impact-Ergebnisse | je Szenario-/Methodenlauf | `imc_analysis_runs` + `imc_analysis_run_impacts` (`engine=openlca`) |

Referenz außerhalb Git: `IMC_LCA_DPP_Data_Extraction_v1.xlsx`  
Checkliste: [`../reference/imc/validation_handoff_one_pagers.md`](../reference/imc/validation_handoff_one_pagers.md)  
CSV-Köpfe: [`templates/thomas_bom_light_sample.csv`](templates/thomas_bom_light_sample.csv), [`templates/thomas_lca_impacts_sample.csv`](templates/thomas_lca_impacts_sample.csv)

## 5) Datenmodell — Stückliste (BOM-Light + Recycling)

Massen und Recycling **erarbeitet Thomas**; Import ist der Weg in die DB.

| Feld | Typ | Pflicht? | Beschreibung | Beispiel |
|------|-----|----------|--------------|---------|
| `farm_id` / `ext_windfarm_id` | uuid/text | ja | Join Register | |
| `turbine_model` | text | ja | z. B. REpower 5M | |
| `subsystem` | text | ja | tower / nacelle / blade / foundation / … | `nacelle` |
| `material` | text | ja | **grob** (nicht ecoinvent-Flowname) | `steel` |
| `mass_t` | numeric | ja | Masse in Tonnen | `120.5` |
| `eol_route` | text | ja | `recycle` \| `landfill` \| `incineration` \| `unknown` | `recycle` |
| `recycling_rate` | numeric | nein | 0–1, nur wenn Route recycle | `0.85` |
| `is_proxy` | boolean | ja | Proxy-Annahme? | `true` |
| `source_note` | text | ja | Literatur/Messung/Annahme | |
| `as_of` | date | ja | Stand der Annahme | `2026-09-17` |
| `olca_process_id` | text | nein | UUID des in openLCA gewählten Datasets | später |

## 6) Datenmodell — Impacts (C-Module)

| Feld | Typ | Pflicht? | Beschreibung |
|------|-----|----------|--------------|
| `external_run_id` / `result_id` | text | ja | Lauf |
| `farm_id` / `ext_windfarm_id` | uuid/text | ja | |
| `scenario_name` | text | ja | z. B. `av_decom_baseline` |
| `method` | text | ja | `IPCC_GWP100` oder `EF3_climate_change` — Thomas legt Default fest |
| `category` | text | ja | Stage A: `climate_change` |
| `value` | numeric | ja | |
| `unit` | text | ja | `kg CO2-eq` |
| `lifecycle_phase` | text | ja | `C1` \| `C2` \| `C3` \| `C4` |
| `lci_db` | text | ja | z. B. `ecoinvent 3.x` inkl. Versionsstring |
| `tool` | text | ja | `openLCA` |
| `is_proxy` | boolean | ja | |
| `notes` | text | nein | |

C-Module (EN 15804, Decom-first): **C1** Rückbau vor Ort (Dauer/Geräte oft aus Marc), **C2** Transport (Distanz IMC), **C3** Behandlung, **C4** Deponie/Rest.

Späteres AAS-Mapping: IDTA **02023** (Export, nicht SoT).

## 7) Verknüpfung

- Join: `ext_windfarm_id` + Turbine-Modell; intern `farm_id`
- Proxy explizit `is_proxy = true`
- Fehlende Keys: reject + Report
- Dubletten Stückliste: `(farm_id, subsystem, material, as_of)`
- Dubletten Impact: `(external_run_id, category, lifecycle_phase)` bzw. unique `external_run_id` je Farm wie Analysis-Runs

## 8) Lieferformat

| Richtung | Format | Transport Stage A |
|----------|--------|-------------------|
| Plattform → Thomas | CSV/XLSX | Download am Park / Shared Drive |
| Stückliste + Impacts → Plattform | CSV/XLSX (Köpfe laut Templates) | Shared Drive → ETL; UI analog Sim-Runs sobald Schema steht |
| Optional Archiv | JSON-LD Zip (Foreground only) | Storage, nicht geparst als SoT |

## 9) Qualitätsregeln

- Pflicht Stückliste: subsystem, material, mass_t, eol_route, is_proxy, source_note, as_of
- Pflicht Impact: method, category, value, unit, tool, lci_db, lifecycle_phase, is_proxy
- `material` = grobe Klasse, kein ecoinvent-Aktivitätsname
- Versionierung über `as_of` + Source-Eintrag; Impacts als neuer Run, kein In-Place-Update

## 10) Akzeptanzkriterien

- [ ] Alpha Ventus / REpower 5M Stückliste (wenige Zeilen) importierbar
- [ ] Recyclingweg/-quote unterscheidbar
- [ ] Mindestens eine GWP-Zeile je C-Modul oder dokumentierte Lücke
- [ ] Proxy vs. gemessen unterscheidbar
- [ ] Thomas-Abnahme schriftlich (OK oder Änderungsliste)
- [ ] Keine UI-erfundenen Massen; kein ecoinvent-Dump in IMC

## 11) RACI light

| Rolle | Wer |
|-------|-----|
| Massen, Recycling, Dataset-Wahl, Methodik | Thomas |
| Park-Kontext, Schema, Import, Provenance, UI | Plattform |
| Decom-Dauer / Vessel (optional C1/C2) | Marc → Plattform → Thomas |
| AAS 02023-Projektion | Plattform + Shubham nach Datenlage |
| Abnahme | Thomas + Heiko |

## 12) Risiken und Annahmen

| Risiko | Mitigation |
|--------|------------|
| Onshore-Proxy für Offshore | `is_proxy` + Notes |
| Sheet ≠ openLCA-Vordergrund | IMC-CSV ist Plattform-SoT; Thomas gleicht vor dem Lauf ab |
| ecoinvent-Lizenz/Version drift | Versionsstring an jedem Impact-Lauf |
| A1–A3-Erwartung | bewusst später; Scope Shield |

## 13) Offene Punkte (Thomas, zum Abnicken)

1. Impact-Set Stage A: **IPCC GWP100** oder **EF 3.0 Climate change**?
2. Mapping-Liste (`olca_process_id`) schon in v1 der Stückliste — oder erst Ergebnisse?
3. Reichen ~15–25 BOM-Zeilen für AV, oder braucht er mehr Auflösung in der Sheet-Datei (nicht in IMC-Feinspez)?
4. C3/C4: reicht grobe Masse × Dataset, oder fehlende Recyclingquoten als `unknown`?

## 14) Entscheidung

- Gespräch: 2026-09-17 (Tool + Decom-first + BOM-Light)
- Schriftliche Freigabe: _ausstehend Thomas + Heiko_

---

## Anhang — Ist-Stand Plattform (2026-09-17)

- Kuratierte BOM-Tabellen: noch nicht befüllt (v2)
- Analysis-Runs (`imc_analysis_runs` / `_impacts`, `engine=openlca`) existieren im Code — Ingest-Pfad analog AnyLogic, UI Impacts secondary
- Arbeitsgrundlage: Extraction-XLSX + diese IA
- CAPEX/OPEX-Zeilen in DB oft 0; nicht Blocker für BOM
