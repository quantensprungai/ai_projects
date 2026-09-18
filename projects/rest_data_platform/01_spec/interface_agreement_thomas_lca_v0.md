<!-- Reality Block
last_update: 2026-09-17
status: draft
scope:
  summary: "Interface Agreement Plattform ↔ Thomas (LCA / BOM-Light / openLCA). Decom-first, kein LCI-Katalog-Spiegel. Hintergrund-DB: BAFU."
  in_scope:
    - BOM-Light masses and recyclability from Thomas into IMC
    - C-module impact results (EF 3.1 / optional ReCiPe, not GWP-only) back into DB
    - in/out workflow and SoT split vs openLCA/BAFU
    - mapping toward AAS 02023 later (GWP only)
  out_of_scope:
    - running openLCA inside the platform
    - inventing masses in the UI
    - mirroring BAFU/ecoinvent process catalog in Postgres
    - live IPC/API in Stage A
notes:
  - "2026-09-17 Gespräch: openLCA 2; BOM-Light; Decom C-first."
  - "2026-09-17 Mail Thomas: Hintergrund-DB = BAFU (nicht ecoinvent). Methoden voraussichtlich EF 3.1 und evtl. ReCiPe 2016; mehrere Wirkungskategorien (nicht nur GWP)."
  - "Abnahme durch Thomas (schriftlich) bevor Import-Pipeline gebaut wird."
-->

# Interface Agreement — Thomas / LCA & BOM (Draft v0.2)

Zweck: Verbindliche Vereinbarung zwischen **Thomas (LCA/BOM-Owner)** und **Plattform (Heiko)**.

Stand nach Gespräch **2026-09-17** und Mail Thomas am selben Tag: Tool **openLCA 2**. Hintergrund-LCI: **BAFU-Datenbank** (nicht ecoinvent). BOM-Light, weil öffentlich wenig belastbare Massen. Start **Rückbau (C1–C4)**, nicht Produktion (A1–A3). Feinspezifikationen bleiben in openLCA — **kein LCI-Katalog-Spiegel** in IMC. LCIA voraussichtlich **EF 3.1**, optional **ReCiPe 2016**; **mehrere Wirkungskategorien** (GWP, Ökotox, Humantox, bei ReCiPe u. a. marine Toxizität), nicht nur Climate Change.

Mail-Vorlage: [`../04_communication/mail_thomas_lca_openlca_2026_09.md`](../04_communication/mail_thomas_lca_openlca_2026_09.md)

## 1) Meta

| Feld | Wert |
|------|------|
| Modulname | LCA / BOM-Light / PCF (Decom-first) |
| Modul-Owner | Thomas |
| Plattform-Owner | Heiko |
| Version | v0.2 (Draft nach Thomas-Mail BAFU + Multi-Impact) |
| Datum | 2026-09-17 |
| Status | **Draft** — schriftliche Abnahme Thomas ausstehend |

## 2) Fachlicher Scope

- **Ziel:** Register liefert Asset-Anker; Thomas recherchiert Massen + Recycling und rechnet in openLCA; Plattform speichert versionierte Stückliste und Impacts (Park-UI, später DPP/AAS).
- **In Scope:** BOM-Light, Recyclability-Felder, Impacts je C-Modul **aller Kategorien der gewählten Methode(n)** (nicht GWP-only), Provenance (Methode, BAFU-Versionsstring, Proxy-Flag), optional Dataset-UUID als Referenz.
- **Out of Scope:** openLCA in der Plattform rechnen; Massen in der UI schätzen; BAFU-/ecoinvent-Katalog / Stahlgüten / Lkw-Jahre in Postgres; Live-IPC in Stage A; A1–A3 bis bessere BOM.
- **Stage:** A — Pilot Alpha Ventus / gemischte Typen Senvion 5M + Areva M5000-116.
- **Ampel:** Workflow/Schema = Grün; konkrete Massen/Impacts = Gelb bis erste CSV; Offshore-Korrekturen = Gelb.

## 2b) SoT-Schnitt (verbindlich)

| Sache | Source of Truth | Nicht |
|-------|-----------------|-------|
| Park, Einheiten, Foundation, Decom-Jahr, Distanz | IMC | — |
| Massen, Recyclingweg, Recyclingquote | Thomas-Sheet → nach Import **IMC** | nicht UI, nicht LCI-Export |
| Stahlgüte, Fahrzeugjahr, Strommix, LCI-Prozess | **openLCA / BAFU** | nicht IMC-Stammdaten |
| Impact-Werte (GWP, Tox, …) | openLCA-Lauf → IMC Ergebniszeile | nicht in der App nachrechnen |

Wenn Sheet und openLCA auseinanderlaufen, gilt für die Plattform die **importierte CSV**. Thomas rechnet mit denselben Vordergrundzahlen. Neue Version = neue `as_of`-Zeilen, kein stilles Überschreiben.

## 3) Workflow (Stage A, dateibasiert)

```
1. Kontext raus          IMC → Thomas
2. Recherche             Thomas (Massen, Recycling, Quelle, Proxy)
3. Stückliste rein       CSV → IMC  (= SoT BOM + Recycling)
4. Rechnen               openLCA (dieselben Massen; BAFU nur Hintergrund)
5. Impacts rein          CSV → IMC (engine=openlca, C1–C4, n Kategorien × Methode)
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
CSV-Paket: [`templates/README.md`](templates/README.md). Daten: Park, Einheiten, Stückliste, Impacts. Feldpflicht/Beispiele für Thomas: [`templates/feldkatalog.csv`](templates/feldkatalog.csv) (gleiche Tabellen wie §5/§6, reist mit; IA bleibt intern). Semikolon-getrennt für Excel.

## 5) Datenmodell — Stückliste (BOM-Light + Recycling)

Massen und Recycling **erarbeitet Thomas**; Import ist der Weg in die DB.  
Kopie für den Anhang (ohne dieses IA): [`templates/feldkatalog.csv`](templates/feldkatalog.csv), Filter `tabelle=bom_light`.

| Feld | Typ | Pflicht? | Beschreibung | Beispiel |
|------|-----|----------|--------------|---------|
| `farm_id` / `ext_windfarm_id` | uuid/text | ja | Join Register | |
| `turbine_model` | text | ja | z. B. REpower 5M | |
| `subsystem` | text | ja | tower / nacelle / blade / foundation / … | `nacelle` |
| `material` | text | ja | **grob** (kein BAFU-/ecoinvent-Flowname) | `steel` |
| `mass_t` | numeric | ja | Masse in Tonnen | `120.5` |
| `eol_route` | text | ja | `recycle` \| `landfill` \| `incineration` \| `unknown` | `recycle` |
| `recycling_rate` | numeric | nein | 0–1, nur wenn Route recycle | `0.85` |
| `is_proxy` | boolean | ja | Proxy-Annahme? | `true` |
| `source_note` | text | ja | Literatur/Messung/Annahme | |
| `as_of` | date | ja | Stand der Annahme | `2026-09-17` |
| `olca_process_id` | text | nein | UUID des in openLCA gewählten Datasets | später |

## 6) Datenmodell — Impacts (C-Module)

Kopie für den Anhang: [`templates/feldkatalog.csv`](templates/feldkatalog.csv), Filter `tabelle=impacts`.

| Feld | Typ | Pflicht? | Beschreibung |
|------|-----|----------|--------------|
| `external_run_id` / `result_id` | text | ja | Lauf |
| `farm_id` / `ext_windfarm_id` | uuid/text | ja | |
| `scenario_name` | text | ja | z. B. `av_decom_baseline` |
| `method` | text | ja | LCIA-Methode, genau wie in openLCA | `EF_3.1` bzw. `ReCiPe_2016` |
| `category` | text | ja | Wirkungskategorie der Methode (nicht nur GWP) | `climate_change`, `ecotoxicity`, `human_toxicity`, `marine_ecotoxicity`, … — **openLCA-Name + Einheit mitliefern** |
| `value` | numeric | ja | |
| `unit` | text | ja | kategorieabhängig | `kg CO2-eq`, `CTUe`, `CTUh`, … |
| `lifecycle_phase` | text | ja | `C1` \| `C2` \| `C3` \| `C4` |
| `lci_db` | text | ja | Hintergrund-DB plus Version | `BAFU <Versionsstring>` |
| `tool` | text | ja | `openLCA` |
| `is_proxy` | boolean | ja | |
| `notes` | text | nein | |

C-Module (**EN 15804**): **C1** Rückbau vor Ort, **C2** Transport, **C3** Behandlung, **C4** Deponie/Rest. Das ist die **Phasen-Gliederung** der Zahlen, nicht die AAS-Vorlage.

Eine Ergebniszeile = eine Methode × eine Kategorie × ein C-Modul. EF 3.1 und ReCiPe 2016 sind **getrennte `method`-Werte** (lieber zwei `external_run_id`, oder eine Datei mit beiden). Kategorie-Namen und Einheiten **wie openLCA exportiert**, nicht umbenennen.

AAS/Shubham: IDTA **02023** Carbon Footprint bleibt **nur GWP** (`PcfCO2eq` + `LifeCyclePhases`). Ökotox / Humantox / marine Toxizität bleiben in Postgres (`imc_analysis_run_impacts`). Methode steht in 02023 unter CalculationMethods — unabhängig von C1–C4. SoT bleibt Postgres; AAS ist Export.

## 7) Verknüpfung

- Join: `ext_windfarm_id` + Turbine-Modell; intern `farm_id`
- Proxy explizit `is_proxy = true`
- Fehlende Keys: reject + Report
- Dubletten Stückliste: `(farm_id, subsystem, material, as_of)`
- Dubletten Impact: `(external_run_id, method, category, lifecycle_phase)`

## 8) Lieferformat

| Richtung | Format | Transport Stage A |
|----------|--------|-------------------|
| Plattform → Thomas | CSV/XLSX | Download am Park / Shared Drive |
| Stückliste + Impacts → Plattform | CSV/XLSX (Köpfe laut Templates) | Shared Drive → ETL; UI analog Sim-Runs sobald Schema steht |
| Optional Archiv | JSON-LD Zip (Foreground only) | Storage, nicht geparst als SoT |

## 9) Qualitätsregeln

- Pflicht Stückliste: subsystem, material, mass_t, eol_route, is_proxy, source_note, as_of
- Pflicht Impact: method, category, value, unit, tool, lci_db, lifecycle_phase, is_proxy
- `material` = grobe Klasse, kein BAFU-/ecoinvent-Aktivitätsname
- Versionierung über `as_of` + Source-Eintrag; Impacts als neuer Run, kein In-Place-Update
- `lci_db` = BAFU plus Versionsstring (kein stilles „BAFU“ ohne Version)

## 10) Akzeptanzkriterien

- [ ] Alpha Ventus / REpower 5M Stückliste (wenige Zeilen) importierbar
- [ ] Recyclingweg/-quote unterscheidbar
- [ ] Mindestens die Kategorien der gewählten Methode je C-Modul oder dokumentierte Lücke
- [ ] Proxy vs. gemessen unterscheidbar
- [ ] Thomas-Abnahme schriftlich (OK oder Änderungsliste)
- [ ] Keine UI-erfundenen Massen; kein BAFU-/ecoinvent-Dump in IMC

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
| BAFU-Version drift | Versionsstring an jedem Impact-Lauf |
| A1–A3-Erwartung | bewusst später; Scope Shield |

## 13) Offene Punkte (Thomas)

1. ~~Impact-Set GWP-only~~ **erledigt Richtung:** EF 3.1 (+ optional ReCiPe 2016), alle Kategorien der Methode, nicht nur GWP. Bitte exakte openLCA-Kategorienamen + Einheiten in der CSV.
2. Mapping-Liste (`olca_process_id`) schon in v1 der Stückliste — oder erst Ergebnisse?
3. Reichen ~15–25 BOM-Zeilen für AV, oder braucht er mehr Auflösung in der Sheet-Datei (nicht in IMC-Feinspez)?
4. C3/C4: reicht grobe Masse × Dataset, oder fehlende Recyclingquoten als `unknown`?
5. BAFU: bitte **genauer Datensatzname + Versionsstring** für `lci_db` (z. B. UVEK/KBOB-Jahr).

## 14) Entscheidung

- Gespräch: 2026-09-17 (Tool + Decom-first + BOM-Light)
- Schriftliche Freigabe: _ausstehend Thomas + Heiko_

---

## Anhang — Ist-Stand Plattform (2026-09-17)

- Kuratierte BOM-Tabellen: noch nicht befüllt (v2)
- Analysis-Runs (`imc_analysis_runs` / `_impacts`, `engine=openlca`) existieren im Code — Ingest-Pfad analog AnyLogic, UI Impacts secondary
- Arbeitsgrundlage: Extraction-XLSX + diese IA
- CAPEX/OPEX-Zeilen in DB oft 0; nicht Blocker für BOM
