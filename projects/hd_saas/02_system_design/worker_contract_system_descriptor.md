# Worker Configuration Contract – System Descriptor Integration

<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Wie jeder Worker (extract_interpretations, text2kg, synthesize_node, …) den System-Descriptor lädt und nutzt."
  in_scope:
    - Zugriff auf Descriptor (DB, Cache)
    - Pflichtfelder/Nutzung pro Job
    - Fehlerfälle
  out_of_scope:
    - Implementierungsdetails im Code (nur Contract)
notes:
  - "Descriptor-Spec: system_descriptor_spec.md. DB: public.hd_systems."
-->

Dieser Contract regelt, wie jeder Worker (extract_interpretations, text2kg, extract_term_mapping, extract_dynamics, extract_interactions, synthesize_node) den **System Descriptor** lädt und nutzt.

## Zweck

Alle systembezogenen Worker benötigen konsistente System-Informationen:

- erlaubte **element_types**
- **canonical_id**-Regeln (Präfix, Format)
- **allowed_relation_types** (KG)
- Synthesis-Stile und Sprach-Defaults
- Term-Mapping-Schulen

Ohne Descriptor-Integration würden diese Regeln im Code oder in ENV verstreut liegen; mit Descriptor sind sie **eine** Quelle (DB oder JSON-Dateien).

---

## Zugriff auf den Descriptor

### Aus der DB (Laufzeit)

Beim Start eines Jobs (oder einmalig pro Worker-Prozess) lädt der Worker aus Supabase:

```sql
SELECT descriptor
FROM public.hd_systems
WHERE system_id = $SYSTEM
```

- **$SYSTEM** kommt aus Job-`debug.system_id` oder aus Asset-Metadaten (z. B. nach classify_domain).
- Der Descriptor wird **gecached** für die gesamte Job-Sequenz (z. B. ein Asset-Durchlauf), um wiederholte DB-Roundtrips zu vermeiden.

### Fallback

Wenn `hd_systems` noch nicht befüllt ist oder der Eintrag fehlt: Worker kann auf **statische Defaults** (z. B. nur hd/bazi mit Minimal-Regeln) oder auf die **JSON-Dateien** in `system_descriptors/*.json` zurückfallen (wenn im Deployment verfügbar). Die autoritative Quelle für Produktion ist die DB.

---

## Pflichtfelder pro Job

### 1) extract_interpretations

- Validiert **element_type** gegen `descriptor.element_types` (wenn nicht in Liste → skip oder warn).
- Normalisiert **element_id** gemäß `descriptor.identifier_rules` (falls definiert).
- Erzeugt **payload.dimensions** als Default-Block (Keys wie im interpretations_contract).
- Setzt **payload.source** = `llm_extraction` oder `mvp_stub` (wie bereits implementiert).

### 2) extract_term_mapping

- Nutzt **descriptor.term_mapping_rules** (schools, synonym_sources, normalization).
- Erzeugt **canonical_id** gemäß `descriptor.canonical_prefix` + Regeln.
- **allow_unknown_terms**: wenn false, unbekannte Begriffe nicht als neue Terms anlegen (oder nur mit Flag).

### 3) text2kg

- **node_key:** Nutzt `descriptor.canonical_prefix` + element_type + element_id (oder Term-Mapping-Lookup wie bisher; Term-Mapping bleibt erste Quelle für canonical_id).
- Erlaubt **nur** `descriptor.kg_rules.allowed_relation_types` für KG-Edges (wenn Edges aus payload.relations erzeugt werden).
- **node_type** = element_type, gemäß `descriptor.kg_rules.node_types` (oder Fallback).
- **Dimensions** MUST in node.metadata.dimensions; **interactions** nur in node.metadata.interactions, niemals als Edges.

### 4) extract_dynamics

- Läuft **nur**, wenn `descriptor.dynamics_rules.has_dynamics === true`.
- Nutzt **descriptor.dynamics_rules.dynamic_types** und **temporal_alignment** für Typen und Phasen.
- **Langfristig (optional):** Extrahierte bzw. verwendete Dynamics-Typen (z. B. `phase_cycle`, `trap`, `growth_path`, `channel_duality_spectrum`) gegen `descriptor.dynamics_rules.dynamic_types` prüfen; unbekannte Typen skip oder warnen, damit nur im Descriptor definierte Typen in **hd_dynamics** landen.

### 5) extract_interactions

- Läuft **nur**, wenn `descriptor.interaction_rules.supports_interactions === true`.
- Nutzt **descriptor.interaction_rules.interaction_entities** (type, profile, center, …) für die Zuordnung.

### 6) synthesize_node

- Nutzt **descriptor.synthesis_rules.default_style**, **allowed_styles**, **wording_tone**, **language_defaults**.
- Erzeugt **canonical_wording** und Stil-Varianten nur, wenn im Descriptor erlaubt.

---

## Fehlerfälle

| Fall | Verhalten |
|------|-----------|
| **Unbekanntes system_id** | Job **failed** oder skip mit Warnung (kein Descriptor gefunden). |
| **Unbekanntes element_type** (nicht in descriptor.element_types) | Chunk/Interpretation **skip** + Warnung in Debug; Job läuft weiter. |
| **Ungültiger element_id** (z. B. Format verletzt identifier_rules) | **Normalisieren** wenn möglich, sonst skip + Warnung. |
| **Descriptor fehlt in DB** | Fallback auf Defaults oder JSON-Datei; wenn kein Fallback, Job failed. |

---

## Referenzen

- **Spec:** `system_descriptor_spec.md`
- **JSON-Deskriptoren:** `system_descriptors/hd.json`, `bazi.json`, `astro.json`, `genekeys.json`
- **DB:** `public.hd_systems` (Migration `20260210120000_hd_systems.sql`)
- **Worker-Übersicht:** `worker_contract_spark_supabase.md`
