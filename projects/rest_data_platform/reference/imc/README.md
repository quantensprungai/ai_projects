<!-- Reality Block
last_update: 2026-03-28
status: draft
scope:
  summary: "Index und Ablagehinweise für IMC/ASTRA-Artefakte (Schema, Mapping, Workshops, Samples)."
  in_scope:
    - artifact inventory
    - storage conventions
    - public schema / supabase note
  out_of_scope:
    - full reproduction of docx/xlsx content
notes:
  - "Binärdateien (.docx/.xlsx) sind bewusst nicht automatisch verschoben; Pfade hier dokumentieren."
-->

# IMC / ASTRA – Referenzartefakte (Ablage & nächste Schritte)

## Zweck

Hier liegt der **kuratierte Überblick** über eure IMC-Deliverables. Die **Source of Truth** für fachliche Entscheidungen bleibt in den Originaldateien (Excel/Word/SQL); dieses README verhindert, dass alles ungebunden im Repo-Root verstreut bleibt.

**Operativer Leitfaden:** Das Word *IMC/ASTRA — Schema & Daten Vorgehensplan* weiter als **Canvas zum Abhaken** nutzen. Projektseitige Einordnung, 4C-Sourcing-Optionen (Wind AXIOM, GIS Suite vs. Open Data) und Schema-Abgleich: [`../../03_roadmap/imc_data_implementation_leitfaden.md`](../../03_roadmap/imc_data_implementation_leitfaden.md).

## Empfohlene Ordnerstruktur (manuell anlegen / Dateien einsortieren)

Lege unter diesem Ordner optional an:

```
reference/imc/
  README.md                 (diese Datei)
  IMC_Schema_v1.sql       (kanonische SQL-Datei, public)
  mapping/
    IMC_4C_to_AAS_Submodel_Mapping_v1.xlsx
  matrices/
    IMC_3x3_Stage_Matrix_v3.xlsx
    IMC_LCA_DPP_Data_Extraction_v1.xlsx
  workshops/
    ASTRA_Phase0_Workshop_PolicyZiele_UseCases.docx
    IMC_AAS_DPP_JRC_Handout_v2_DE.docx
    IMC_ASTRA — Schema & Daten Vorgehensplan.docx
    IMC_DataPlan_Meeting4_Protocol_DE.docx
    IMC_Projektvorschlag_v5_DE.docx
  validation/
    IMC_Validierungspaket_Thomas_LCA_BOM.docx
    IMC_Validierungspaket_Marc_Decom_AnyLogic.docx
    IMC_Validierungspaket_Shubham_DPP_AAS.docx
  samples_4c/               (nur wenn Lizenz/Klarheit: Sample-Exports von 4C)
    README.md               (Hinweis: nicht committen wenn vertraulich)
```

**4C-Samples:** Nur ins Repo legen oder teilen, wenn Lizenz und Veröffentlichung geklärt sind. Sonst: geteilter Laufwerkspfad + Hash in `public.imc_data_sources.file_hash` dokumentieren.

## Artefakt-Index (was wofür)

| Artefakt | Rolle |
|----------|--------|
| `IMC_4C_to_AAS_Submodel_Mapping_v1.xlsx` | Spalte → Submodell → Priorität; Grundlage für ETL und DPP-Feldliste |
| `IMC_Schema_v1.sql` | DB-Entwurf v1 (4C-Kern + Provenance); **siehe Hinweis zu `public`/RLS unten** |
| `IMC_3x3_Stage_Matrix_v3.xlsx` | Stage-/Prozess-Matrix; Anker für Decom-Sequenz & Scope |
| `IMC_LCA_DPP_Data_Extraction_v1.xlsx` | BOM-Light, LCA, EoL, DPP-Mapping; ETL-Ziel für Thomas-Review |
| Phase-0 / Protokolle / Vorgehensplan `.docx` | Governance, Workshops, Nachvollziehbarkeit |
| Validierungspakete `.docx` | One-Pager für Thomas, Marc, Shubham |

Markdown-Spiegel der Validierungsinhalte (durchsuchbar im Repo): [`validation_handoff_one_pagers.md`](validation_handoff_one_pagers.md).

## Supabase / `public`: `IMC_Schema_v1.sql`

Die Datei [`IMC_Schema_v1.sql`](IMC_Schema_v1.sql) legt **Enums, Tabellen, Views (`security_invoker`), RLS und Grants in `public`** an — **kein** separates Schema `imc` mehr. **Namenskonvention:** Präfix **`imc_`** für alle IMC-Tabellen und -Views (`imc_v_*`), ENUMs ebenfalls `imc_*`; Ausnahme/Kürzung: **`imc_orgs`** (statt `organisations`). Damit sind PostgREST, der Supabase-Client und **Team-Account-Tenancy** (`has_role_on_account`, `imc_wind_farms.account_id`) nutzbar.

**Ausführung in der App:** dieselbe DDL als Supabase-Migration im Code-Repo [`code/astra-imc-platform/`](../../../../code/astra-imc-platform/) unter `apps/web/supabase/migrations/20260327120000_imc_astra_v1.sql` (Extensions mit `WITH SCHEMA extensions`); nach Schema-Änderungen hier zuerst Referenz pflegen, dann Migration bauen: `node projects/rest_data_platform/scripts/build_imc_migration.mjs` (Repo-Root `ai-projects`) oder Diff erzeugen.

**Leitfaden zu Policies:** [`../../01_spec/imc_rls_policy_patterns.md`](../../01_spec/imc_rls_policy_patterns.md).

## Inhaltliche Einordnung (deine Fragen kurz beantwortet)

- **Nicht 100+ Tabellen aus 4C:** Richtig – Normalisierung + EAV (z. B. CAPEX nach Kategorie) reduziert die physische Tabellenzahl; viele 4C-Spalten landen als Zeilen oder JSONB, nicht als eigene Tabelle.
- **Phase 0 DPP-Feldliste:** Passt zum Schema; v1 deckt den 4C-lastigen Teil ab, **Material, LCA, Umwelt, Recyclability, Decom-Graph, AAS-Export** kommen als **v2-Module** dazu – priorisiert über die Feldliste (Shubham/Marc), reviewed von Heiko/Thomas.
- **Prozesskette (12/15 Schritte):** Über `event_type` / später `decom_*` erweiterbar; neue Schritte = neue Enum-Werte oder neue Zeilen, kein Blocker.
- **Was du schon liefern kannst vs. Team:** Siehe [`validation_handoff_one_pagers.md`](validation_handoff_one_pagers.md) – du kannst ETL/ERA5/Natura/Boilerplate stark vorbereiten; SimaPro/AnyLogic/AASX-Konformität bleiben bei den Owners.

## Nächste Schritte (Reihenfolge)

1. **Schema:** `public` (festgehalten in `02_system_design/architecture.md`); SQL: `IMC_Schema_v1.sql`.
2. **Migration:** v1 liegt im App-Repo (`20260327120000_imc_astra_v1.sql`); lokal `pnpm supabase:web:reset` + `typegen`. Weitere Schritte: neue Migrationen splitten oder per `schemas/*` + Diff.
3. **4C-ETL:** Erst `imc_data_sources` + Windfarm-Pfad (`imc_wind_farms` …); dann POP/VPI; Spalten 1:1 aus Sample validieren (zwei POP-Dateigrößen im Explorer – eine Version als „canonical“ markieren).
4. **Parallel Phase 0:** DPP-Feldliste (JRC-Logik) – Ergebnis merged in Schema v2 und in `dpp_templates` o. ä.
5. **Samples:** Nur nach Freigabe ins Repo unter `samples_4c/` oder nur Hash + Pfad in `imc_data_sources`.

## Link zur Projektdoku

Gesamtindex: [`../../README.md`](../../README.md).
