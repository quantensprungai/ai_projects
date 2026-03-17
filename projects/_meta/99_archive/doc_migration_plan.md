> **ARCHIVIERT** (2026-02-16). Inhalt wurde in Cursor Rules (.cursor/rules/) oder doc_and_rules_strategy.md überführt.

# Doku-Migrationsplan – Von Alt zu Neu

<!-- Reality Block
last_update: 2026-02-13
status: draft
scope:
  summary: "Prozess: Alte Docs lesen → neue Logik definieren → Inhalte migrieren → Rules anpassen. Community-Empfehlungen eingearbeitet."
  in_scope:
    - Migrationsprozess
    - Zielstruktur HD-SaaS
    - Community/Vibecoding-Referenzen
  out_of_scope:
    - Andere Projekte (erst HD-SaaS als Pilot)
notes:
  - "Microsoft Engineering Playbook: Repo-spezifisch vs. Projekt-level trennen."
  - "Developer Toolkit: Dateien <300 Zeilen, co-location, descriptive naming."
  - "Vibe Coding Framework: D.O.C.S. (Documentation), strukturierte Komponenten."
-->

## 1. Was Community/Vibecoding/Cursor sagen

### Cursor & Developer Toolkit

- **Dateien < 300 Zeilen** – Token-Effizienz, KI liest gezielt
- **Descriptive Naming** – statt `utils.ts` → `validators/email.ts`
- **Co-location** – Implementierung, Tests, Types zusammen
- **Kontext-Verschwendung vermeiden** – schlechte Struktur = KI liest Irrelevantes

### Microsoft Engineering Playbook

- **Repo-spezifisch:** Getting started, Setup, Deploy, Design Decision Logs, ADRs
- **Projekt-level:** Intro, Stakeholder, Requirements, Team Agreements

### Vibe Coding Framework

- **D.O.C.S.** – strukturierte Dokumentation
- **Framework Components** – klar getrennte Bereiche (Core Concepts, Implementation, Best Practices)
- **Document Templates** – konsistente Formate

### Fazit

**Neue Logik zuerst, dann migrieren** – nicht „alte Dateien aufräumen“. Die Struktur muss vor der Migration stehen.

---

## 2. Der empfohlene Prozess

```
Phase 1: LESEN (Inventar)
  → Alle Docs durchgehen, Inhalt kategorisieren
  → Referenz-Graph verstehen (wer verlinkt wen)
  → Was ist aktiv, was ist Waisen/veraltet

Phase 2: ZIELSTRUKTUR definieren
  → Neue Logik (nicht an 00/01/02/03/04 kleben)
  → Max. 15–20 aktive Docs
  → Klare Trennung: Einstieg vs. Referenz vs. Archiv

Phase 3: MIGRATION
  → Inhalte aus alten Dateien in neue Struktur ziehen
  → Alte Dateien → 99_archive (mit Verweis auf neue Location)
  → Keine Duplikate – Inhalte konsolidieren

Phase 4: RULES anpassen
  → hd-saas-context.mdc auf neue Pfade
  → README / Chat-Handover aktualisieren
  → Referenzen in allen Docs prüfen
```

---

## 3. Zielstruktur HD-SaaS (neu)

**Prinzip:** 3 Ebenen – Einstieg (3–4 Docs), Referenz (8–10 Docs), Archiv (Rest)

### Einstieg (immer zuerst lesen)

| Doc | Inhalt | Zeilen-Ziel |
|-----|--------|-------------|
| **README.md** | Index + Links + „Einstieg für KI/neue Chats“ | < 80 |
| **current_status_local_dev.md** | Single Source of Truth: Status, Blocker, Datenstand | < 300 |
| **next_steps_was_fehlt_noch.md** | Priorität, Reihenfolge, Option B | < 200 |
| **chat_handover_hd_saas.md** | Copy-Paste Block | < 100 |

### Referenz (Contracts & Specs)

| Doc | Inhalt | Quelle (alt) |
|-----|--------|-------------|
| **02_system_design/interpretations_contract.md** | Payload-Form | bleibt |
| **02_system_design/dimensions_contract.md** | 12 Keys | bleibt |
| **02_system_design/text2kg_spec.md** | Nodes/Edges | bleibt |
| **02_system_design/plan_option_b_roadmap.md** | Roadmap | bleibt |
| **02_system_design/worker_contract_spark_supabase.md** | Worker ↔ Supabase | bleibt |
| **02_system_design/erkenntnisse_und_fuer_spaeter.md** | Living Doc | bleibt |
| **02_system_design/meta_system_analysis_integration.md** | Entscheidungen | bleibt |

### Referenz (Architektur & Vision – konsolidiert)

| Doc (neu) | Inhalt | Quellen (alt) – migrieren |
|-----------|--------|---------------------------|
| **00_overview/vision_and_flow.md** | Vision, Story, UI-Prinzipien, Flow | vision_2026_2027, story_and_mythology, ui_ux_principles_and_flow, interface_and_vision, app_picture_and_user_journey, platform_and_story_master |
| **02_system_design/architecture.md** | Architektur, Data Flows, Infra | architecture, data_flows, layers_overview |

### Referenz (Worker & Pipeline)

| Doc | Inhalt | Quelle (alt) |
|-----|--------|-------------|
| **02_system_design/worker_contract_extract_interpretations.md** | bleibt | |
| **02_system_design/worker_contract_synthesize_node.md** | bleibt | |
| **02_system_design/worker_contract_extract_term_mapping.md** | bleibt | |
| **02_system_design/worker_contract_system_descriptor.md** | bleibt | |
| **02_system_design/system_descriptor_spec.md** | bleibt | |
| **02_system_design/layer_implementation_abgleich.md** | bleibt | |

### Optional (bei Bedarf)

| Doc | Inhalt | Quelle (alt) |
|-----|--------|-------------|
| **02_system_design/language_and_pipeline_overview.md** | bleibt | |
| **00_overview/local_vs_cloud_guardrails.md** | bleibt | |
| **00_overview/makerkit_bootstrap_and_orientation.md** | bleibt | |

### 99_archive (nach Migration)

| Doc (alt) | Aktion |
|-----------|--------|
| vision_2026_2027, story_and_mythology, ui_ux_principles_and_flow, interface_and_vision, app_picture_and_user_journey, platform_and_story_master | → Inhalt in vision_and_flow.md; dann archivieren |
| architecture, data_flows, layers_overview | → Inhalt in architecture.md; dann archivieren |
| market_context, value_proposition, problem_statement, mission | → In vision_and_flow.md oder README; dann archivieren |
| requirements, functional_spec, prd, edge_cases, user_journeys, parking_lot_backlog | → In next_steps oder README verlinken; dann archivieren |
| mvp, milestones, v1_v2_v3, risks_assumptions, hd_ingestion_slice_spec | → In plan_option_b verlinken; dann archivieren |
| agents, tools_integrations, prompts_and_personas | → In architecture oder archivieren |
| prompts, diagrams, datasets, branding (04_assets) | → Archivieren oder in README verlinken |
| text2kg_test_procedure, text2kg_implementation_sketch, export_supabase_to_arangodb, process_batch_llm_and_stub | → In text2kg_spec oder next_steps verlinken; archivieren |
| llm_alternativen_recherche, doc_audit_hd_saas | → Archivieren (Audit erledigt) |

---

## 4. Konkrete Migrationsschritte

### Schritt 1: vision_and_flow.md erstellen

- **Inhalt:** Vision 2026/27, Story & Mythologie, UI-Prinzipien, Interface, App Picture, Platform & Story Master
- **Ziel:** 1 Doc statt 7, < 300 Zeilen (oder 2 Docs: vision.md + flow.md)
- **Alte Dateien:** Nach Migration → 99_archive mit Verweis „Inhalt migriert nach vision_and_flow.md“

### Schritt 2: architecture.md erweitern

- **Inhalt:** Architektur, Data Flows, Layers Overview
- **Ziel:** 1 Doc statt 3
- **Alte Dateien:** → 99_archive

### Schritt 3: README erweitern

- **Abschnitt „Einstieg für KI/neue Chats“** (doc_audit)
- **Abschnitt „Weitere Docs“** – architecture, requirements, mvp, etc.
- **Links prüfen**

### Schritt 4: next_steps, interface_and_vision, ui_ux anpassen

- Option B als autoritativ
- Pfade zu interpretations_contract etc.

### Schritt 5: 99_archive befüllen

- Alte Dateien verschieben
- Jede mit Kopfzeile: „Inhalt migriert nach: …“

### Schritt 6: Rules aktualisieren

- hd-saas-context.mdc: Pfade prüfen
- ai-projects-global: unverändert

---

## 5. Risiken & Absicherung

- **Backup-Branch existiert:** backup-before-clean-restart-2026-02
- **Migration in Feature-Branch:** z.B. `feature/doc-migration-2026-02`
- **Kein Commit auf main** bis Migration getestet und geprüft

---

## 6. Aufwandsschätzung

| Phase | Aufwand |
|-------|---------|
| Phase 1: Lesen/Inventar | 1–2 h |
| Phase 2: Zielstruktur (bereits hier definiert) | — |
| Phase 3: Migration (vision_and_flow, architecture, README) | 2–3 h |
| Phase 4: 99_archive, Rules, Referenzen | 1–2 h |
| **Gesamt** | **~4–7 h** |

---

## 7. Nächster Schritt

**Option A:** Migration als Feature-Branch starten – ich lese alle Docs, erstelle vision_and_flow.md und architecture.md, migriere Inhalte.

**Option B:** Du prüfst diesen Plan erst, gibst Feedback, dann starte ich.

**Option C:** Nur Schritt 1 (vision_and_flow) als Pilot – wenn das gut passt, Rest.

---

## Referenzen

- `projects/_meta/doc_and_rules_strategy.md`
- `projects/hd_saas/02_system_design/doc_audit_hd_saas.md`
- Developer Toolkit: Project Structure Optimized for AI
- Microsoft Engineering Playbook: Repositories
- Vibe Coding Framework: Document Organisation
