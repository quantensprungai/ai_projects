<!-- Reality Block
last_update: 2026-03-28
status: draft
scope:
  summary: "Einordnung IMC Word-Vorgehensplan, Abgleich mit Repo-SQL, strategische 4C-Datenwege (Inhalt/Umsetzung)."
  in_scope:
    - plan role vs repo
    - sourcing strategy Wind AXIOM GIS vs open data
    - schema drift warnings
  out_of_scope:
    - PT budgeting
    - legal license text
notes:
  - "Word-Dokument bleibt detailierter Arbeits-Canvas; diese Datei ist die projektseitige Kurzfassung."
-->

# IMC/ASTRA – Schema & Daten: Leitfaden (Repo)

## Nutzen wir den Word-Vorgehensplan noch?

**Ja – als operativen Leitfaden (lebendiges Dokument, abhaken).**  
Er beschreibt sinnvoll die **Reihenfolge**: Extensions → Schema v1 → Patches → RLS → 4C-ETL → spätere Module (BOM/LCA, Metocean, Geo, Decom, DPP, Regulatorik).

**Ergänzung im Repo (nicht Ersatz):**

| Quelle | Rolle |
|--------|--------|
| Word: *IMC/ASTRA — Schema & Daten Vorgehensplan* | Detaillierte Schritte, Canvas, Checklisten, Kommunikation an Thomas/Marc/Shubham |
| [`reference/imc/IMC_Schema_v1.sql`](../reference/imc/IMC_Schema_v1.sql) | **Kanone** für Tabellen-, Enum- und View-Namen in **public** |
| [`02_system_design/architecture.md`](../02_system_design/architecture.md) | Grenzen: eigenes App-Repo (`astra-imc-platform`), keine Vermischung mit Inner Compass |
| [`reference/imc/README.md`](../reference/imc/README.md) | Artefakt-Index (xlsx, docx, Samples) |

**Pflege-Regel:** Ändert sich das Schema, zuerst **SQL-Datei** anpassen, dann Word-Canvas; oder umgekehrt, aber **immer einen Abgleich** – sonst driftet der Leitfaden.

## Was sich gegenüber dem Word-Stand bereits geändert hat (technisch)

1. **Kein Schema `imc` mehr:** Alles liegt in **`public`** (kompatibel mit PostgREST/RLS der Anwendungsbasis). Der Word-Text „public statt imc“ ist richtig; ältere Fassungen mit `imc.*` sind obsolet.
2. **Beispiel-SQL im Word ggf. veraltet:** z. B. `INSERT INTO imc_data_sources (id, name, type, …)` passt **nicht** zum aktuellen DDL. Tatsächliche Spalten u. a.: `source_id`, `source_type`, `source_name`, `source_version`, `license_info`, `snapshot_date`, `file_hash`, `notes`, `created_at`.
3. **„v1.1“-Patches:** Es waren **keine drei neuen Tabellen**, sondern **drei Spaltengruppen** an drei bestehenden Tabellen: `imc_farm_milestones.planned_decom_year`, `imc_ports.min_draft_m` + `imc_ports.quay_length_m`, `imc_vessels.mobilisation_days`. Diese sind **in `IMC_Schema_v1.sql` im CREATE TABLE integriert**; am Dateiende gibt es auskommentierte `ALTER TABLE` nur für bereits deployed alte v1.
4. **FK-Reihenfolge im Word:** `imc_wind_farms` referenziert in v1 **kein** `turbine_model_id` direkt auf der Farm-Tabelle; Turbinenmodell sitzt in **`imc_farm_design.turbine_model_id`**. ETL-Reihenfolge: `imc_data_sources` → `imc_turbine_models` → `imc_wind_farms` → `imc_farm_design` / `imc_farm_grid` / … (wie Word, aber Join-Pfad und **`imc_`-Präfixe** beachten).
5. **Validierungs-SQL:** Tabellen- und Spaltennamen im Word durch Copy-Paste manchmal mit **Backslashes** – in Postgres sind es **Unterstriche** (`imc_wind_farms`, nicht `wind\farms`).

## Strategie & Umsetzung: Was die 4C-Produktinfos für euch bedeuten (ohne PT-Fokus)

Die Broschüre ändert **nicht** die Phasenlogik des Vorgehensplans, aber **optional die Datenbeschaffung** innerhalb bestehender Blöcke:

### A) Metocean / „Wetter & Fenster“ (Phase 4 im Plan)

| Option | Strategische Bedeutung |
|--------|-------------------------|
| **Eigen** (Copernicus ERA5 o. ä.) | Maximale **Reproduzierbarkeit** und **Kontrolle** über Aggregation; passt zu „wir besitzen die Pipeline“. |
| **Wind AXIOM (4C)** | Schnellerer Weg zu **hub-hohen Wind- und Metocean-Produkten**, wenn Lizenz/Academic das abdeckt. Ihr speist **nur die exportierten Kennzahlen** in eure Tabellen (z. B. später `era5_*` oder generisch `metocean_site_aggregates`). |

**Entscheidungskriterien (Inhalt):** dürfen die Rohdaten **persistiert** werden? ist **Methodik** für Paper/DPP nachvollziehbar? reicht ein **4C-Export-Snapshot** mit `source_id` + `file_hash`?

### B) Räumliche Daten / GIS (Phase 5 + ggf. Turbinenpunkte)

| Option | Strategische Bedeutung |
|--------|-------------------------|
| **GIS Spatial Data Suite (4C)** | Parkgrenzen, Turbinenpositionen, Kabel **bereits vektorisiert** – weniger manuelles Zusammenbauen aus Streudaten. |
| **Open (BfN, EEA, …)** | Unabhängigkeit von 4C-Lizenz für **Schutzgebiete**; weiterhin sinnvoll parallel oder primär für Natura2000. |

**Umsetzung:** Euer Schema bleibt **PostGIS-first**; die **Quelle** wechselt (4C-Geodatabase-Export vs. eigener Download). Provenance in `imc_data_sources` immer setzen.

### C) Vessels & Ports

Broschüre bestätigt: **Excel/Export** aus dem gleichen Ökosystem wie eure Samples – strategisch: **kein Scraping nötig**, Fokus auf **Mapping + Qualität + Lizenz**. Passt zu Phase 2 / VPI-Pfad im Leitfaden.

### D) Was sich **strategisch nicht** durch 4C-Marketing ersetzt

- **BOM/LCA, DPP/AAS, Decom-Graph, AnyLogic-Outputs** – bleiben **eure** Module und Owner (Thomas, Marc, Shubham).
- **Regulatorik „maschinenlesbar“:** RegCheatSheet/PDF bleibt eher **Referenz**; strukturierte Tabellen (`regulatory_permits` etc.) weiter aus **Behördenquellen + Kuratierung**.

## Empfohlene Vorgehensweise (Kurz)

1. **Word-Vorgehensplan behalten** als **Checkliste und Kommunikationsgrundlage** (Phasen 1–8).
2. **Technische Wahrheit** immer aus **`IMC_Schema_v1.sql`** + geplanten Migrationen im **App-Repo** (`astra-imc-platform`).
3. **4C-Produkte** (Wind AXIOM, GIS Suite, Academic) als **Sourcing-Optionen** dokumentieren: in `reference/imc/README.md` oder im Word einen Abschnitt „Datenwege“ mit **Entscheidung: Export A vs. Pipeline B** pro Datenstrom (ohne PT-Tabelle, wenn ihr das nicht wollt).
4. **Phase 0 DPP-Feldliste** (Shubham/Marc) weiter parallel – sie steuert, **welche** späteren Tabellen (v2) wirklich nötig sind; der Word-Plan listet sie schon als Ausbau.

## Verknüpfung

- Projektindex: [`../README.md`](../README.md)
- Architektur & Doku-Layering: [`../02_system_design/architecture.md`](../02_system_design/architecture.md)
