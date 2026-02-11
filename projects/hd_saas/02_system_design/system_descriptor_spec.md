# System Descriptor – Multi-System Registry (Spec)

<!--
last_update: 2026-02-10
status: final
scope:
  summary: "Zentrale Definition aller integrierten Archetyp-Systeme (Human Design, BaZi, Astro, Gene Keys) inkl. Input-Format, Element-Typen, Canonical-ID-Konventionen, Mapping-Regeln und Sprachlogik."
  in_scope:
    - Descriptor-Format (JSON)
    - Verwendung in classify_domain, extract_interpretations, term_mapping, text2kg, dynamics, synthesis
    - DB-Registry (public.hd_systems)
    - Worker-Contract (Descriptor-Integration)
notes:
  - "Konkrete Deskriptoren: system_descriptors/*.json. Worker: worker_contract_system_descriptor.md. DB: Migration hd_systems."
-->

Der **System Descriptor** ist ein verpflichtender, zentraler Teil der HD-SaaS-App. Er beschreibt jedes integrierte Archetypen-System formal, sodass alle Verarbeitungsschritte (Classification → Extraction → Term-Mapping → KG → Dynamics → Synthesis) deterministisch arbeiten können.

Der Descriptor dient als:

- **Top-Level Whiteboard** für systemische Regeln
- **Contract** für alle Jobs (classify_domain, extract_interpretations, text2kg, synthesis …)
- **Referenz** für Term-Mapping
- **Erweiterungs-Slot** für neue Systeme

Ohne Descriptor kollidieren Begriffe: „Gate“ in HD ist etwas anderes als „Gate“ in anderen Systemen. „House“ in Astro ist etwas anderes als „Palace“ in Zi Wei Dou Shu. Der Descriptor stellt sicher, dass Begriffe **nicht** kollidieren.

---

## 1) Zweck

- **Identitäts-Anker** pro System
- **Struktur-Blueprint** für alle systembezogenen Entities
- **Kanonische Benennung & Präfixe** (canonical_id-Regeln)
- **Validierungs-Contract** für Interpretations (element_type, element_id)
- **Term-Mapping-Basis** für Synonyme und Schulen
- **KG-Normalisierung** (node_key, erlaubte relation_types)
- **Synthesis-Steuerung** (Sprache, Stil, Ton)
- **Modularität:** Neue Systeme = ein neuer Descriptor (+ Eintrag in Registry)

---

## 2) Speicherorte

| Ort | Inhalt |
|-----|--------|
| **Dateien (autoritative Quelle)** | `projects/hd_saas/02_system_design/system_descriptors/{system_id}.json` (z. B. hd.json, bazi.json). Die Descriptoren liegen **nur** hier im Repo; sie müssen **nicht** ins Code-Verzeichnis (`code/hd_saas_app/`) kopiert werden. |
| **DB (Laufzeit)** | `public.hd_systems` – Tabelle mit system_id, system_name, canonical_prefix, descriptor (jsonb). Migration existiert: `code/hd_saas_app/apps/web/supabase/migrations/20260210120000_hd_systems.sql`. Die Tabelle wird per **Seed** aus den JSON-Dateien befüllt; Worker laden Descriptoren zur Laufzeit aus der DB. |

Die JSON-Dateien in `projects/` sind die einzige Quelle; die DB dient dem Laufzeit-Lookup (z. B. `SELECT descriptor FROM public.hd_systems WHERE system_id = $1`). **Seed-Skript:** `code/hd_saas_app/apps/web/scripts/seed_hd_systems.py` – liest alle `*.json` aus dem Descriptoren-Verzeichnis (Default: relativ zum Repo-Root `projects/hd_saas/02_system_design/system_descriptors`, oder Umgebungsvariable `HD_DESCRIPTORS_DIR` / erstes CLI-Argument) und schreibt sie per Upsert in `public.hd_systems`. Benötigt `SUPABASE_URL` und `SUPABASE_SERVICE_ROLE_KEY` (z. B. aus `.env` im Script-Verzeichnis oder `~/hd/.env`).

---

## 3) System Descriptor (Format)

Jedes System wird beschrieben durch:

```json
{
  "system_id": "string",
  "system_name": "string",
  "canonical_prefix": "string",

  "input_format": "datetime | datetime+location | name | date",
  "calendar_basis": "gregorian | lunar | sidereal | solar",

  "element_types": ["type", "strategy", "gate", "profile", "stem", "branch", ...],

  "identifier_rules": {
    "gate": "1-64",
    "line": "1-6",
    "day_master": "10 Heavenly Stems",
    "house": "1-12"
  },

  "canonical_id_rules": {
    "format": "{prefix}{element_type}.{element_id}",
    "examples": ["hd.type.generator", "bazi.day_master.geng", "astro.house.7"]
  },

  "term_mapping_rules": {
    "schools": ["HD_classic", "64keys", "GeneKeys"],
    "synonym_sources": ["interpretations", "LLM", "manual"],
    "normalization": "lowercase_underscore",
    "allow_unknown_terms": false
  },

  "kg_rules": {
    "allowed_relation_types": ["part_of", "depends_on", "maps_to", "amplifies", ...],
    "node_types": ["Gate", "Line", "Profile", "Type", "Authority", "Center"]
  },

  "dynamics_rules": {
    "has_dynamics": true,
    "dynamic_types": ["phase_cycle", "trap", "growth_path"],
    "temporal_alignment": ["saturn_return", "uranus_opposition"]
  },

  "synthesis_rules": {
    "default_style": "natural",
    "allowed_styles": ["natural", "coaching", "poetic", "technical"],
    "language_defaults": ["de", "en"],
    "wording_tone": "klar, modern, nicht-esoterisch"
  },

  "interaction_rules": {
    "supports_interactions": true,
    "interaction_entities": ["type", "profile", "center"]
  },

  "body_mechanics_support": true,
  "hidden_expectations_support": true,
  "relationship_dynamics_support": true,
  "environment_fate_support": true,

  "documentation_ref": "specs/hd_system.md"
}
```

### 3.1 Descriptor-Felder: required vs. optional

| Feld | Required | Beschreibung |
|------|----------|---------------|
| **system_id** | ja | Eindeutige System-ID (z. B. `hd`, `bazi`, `astro`). Wird für Klassifikation und DB-Lookup verwendet. |
| **system_name** | ja | Anzeigename des Systems (z. B. „Human Design“, „BaZi (Four Pillars of Destiny)“). |
| **canonical_prefix** | ja | Präfix für canonical_id (z. B. `hd.`, `bazi.`). Muss mit Trenner enden, wenn Format `{prefix}{element_type}.{element_id}` genutzt wird. |
| **element_types** | ja | Liste der Element-Typen des Systems. Ohne sie ist keine Validierung von element_type möglich. |
| input_format | nein | Wie wird Input geliefert: `datetime`, `datetime+location`, `assessment|observation`, `name`, etc. |
| calendar_basis | nein | `gregorian`, `lunar_solar`, `sidereal`, `none`, etc. |
| identifier_rules | nein | Regeln pro element_type für gültige element_id-Werte (z. B. gate 1–64). Fehlt → keine strenge Validierung. |
| canonical_id_rules | nein | Format-String + optionale examples. Fehlt → Konvention aus canonical_prefix + element_type + element_id. |
| term_mapping_rules | nein | schools, normalization, allow_unknown_terms. Fehlt → Term-Mapping-Job nutzt Defaults oder skippt. |
| kg_rules | nein | allowed_relation_types, node_types. Fehlt → text2kg nutzt keine system-spezifischen Relationen. |
| dynamics_rules | nein | has_dynamics, dynamic_types, temporal_alignment. Fehlt → has_dynamics = false angenommen. |
| synthesis_rules | nein | default_style, wording_tone, language_defaults, allowed_styles. Fehlt → Synthesis nutzt globale Defaults. |
| interaction_rules | nein | supports_interactions, interaction_entities. Fehlt → supports_interactions = false angenommen. |
| body_mechanics_support | nein | Boolean. Fehlt → false. Steuert Nutzung von dimensions.body_mechanics. |
| hidden_expectations_support | nein | Boolean. Fehlt → false. Steuert dimensions.projection_field. |
| relationship_dynamics_support | nein | Boolean. Fehlt → false. Steuert dimensions.relationship_pattern. |
| environment_fate_support | nein | Boolean. Fehlt → false. Steuert dimensions.environment. |
| research_layer | nein | Nur für Systeme mit Forschungshypothesen (z. B. HD). Optional. |
| documentation_ref | nein | Verweis auf System-Spec (z. B. `specs/hd_system.md`). |

**Integration:** Wenn ein optionales Feld fehlt, sollen Worker einen definierten Default annehmen (z. B. Layer-Flags = false), statt abzustürzen.

---

## 4) Warum brauchen wir den Descriptor?

| Frage | Antwort |
|-------|--------|
| Welche Entities existieren im System? | `element_types`, `identifier_rules` → Klassifikation und Validierung |
| Wie sieht ein canonical_id aus? | `canonical_id_rules`, `canonical_prefix` → text2kg erzeugt deterministische node_keys |
| Welche Synonyme gehören zu welchem System? | `term_mapping_rules.schools` → extract_term_mapping |
| Welche Relationstypen sind erlaubt? | `kg_rules.allowed_relation_types` → text2kg erzeugt nur erlaubte Kanten |
| Wie soll Synthesis klingen? | `synthesis_rules` → canonical_wording, Stil |
| Hat das System Dynamics? | `dynamics_rules.has_dynamics` → extract_dynamics nur wenn true |
| Hat das System Interactions? | `interaction_rules.supports_interactions` → extract_interactions |
| Unterstützt Body-Mechanics-Layer? | `body_mechanics_support` → Dimensions.body_mechanics nutzbar |
| Unterstützt Hidden-Expectations-Layer? | `hidden_expectations_support` → Dimensions.projection_field nutzbar |
| Unterstützt Relationship-Dynamics? | `relationship_dynamics_support` → Dimensions.relationship_pattern nutzbar |
| Unterstützt Environment/Fate? | `environment_fate_support` → Dimensions.environment nutzbar |

Die vier Layer-Flags steuern, ob das System die erweiterten Dimensions-Slots (siehe **dimensions_contract.md**) semantisch befüllen kann.

---

## 5) Konkrete Deskriptoren

Fertige JSON-Deskriptoren liegen in:

- `system_descriptors/hd.json` – Human Design
- `system_descriptors/bazi.json` – BaZi (Four Pillars of Destiny)
- `system_descriptors/astro.json` – Western Astrology
- `system_descriptors/genekeys.json` – Gene Keys
- `system_descriptors/enneagram.json` – Enneagram (nicht geburtsbasiert; Input nur Assessment/Observation, **kein** automatisches HD→Enneagram-Mapping im Core)
- `system_descriptors/jyotish.json` – Jyotish (Vedic Astrology)
- `system_descriptors/numerology.json` – Numerologie (Life Path etc.)
- `system_descriptors/nine_star_ki.json` – Nine Star Ki
- `system_descriptors/mayan_tzolkin.json` – Mayan Tzolkin

Siehe diese Dateien für die exakten Felder pro System.

---

## 6) Verwendung im Worker

Alle Jobs, die systembezogen arbeiten, **sollen** den Descriptor nutzen (sobald die Integration implementiert ist):

| Job | Nutzung |
|-----|--------|
| **classify_domain** | Weiß, welche Systeme existieren (system_id-Liste) |
| **extract_interpretations** | Validiert element_type gegen descriptor.element_types; normalisiert element_id |
| **extract_term_mapping** | Nutzt term_mapping_rules (schools, normalization) |
| **text2kg** | node_key aus canonical_prefix + element_type + element_id; nur allowed_relation_types für Edges |
| **extract_dynamics** | Nur wenn dynamics_rules.has_dynamics = true |
| **extract_interactions** | Nur wenn interaction_rules.supports_interactions |
| **synthesize_node** | synthesis_rules (default_style, wording_tone, language_defaults) |

**Contract:** `worker_contract_system_descriptor.md`

---

## 7) DB-Tabelle `public.hd_systems`

- **Migration:** `code/hd_saas_app/apps/web/supabase/migrations/20260210120000_hd_systems.sql`
- **Spalten:** id, system_id (unique), system_name, canonical_prefix, descriptor (jsonb), created_at, updated_at
- **Zugriff:** Worker lädt z. B. `SELECT descriptor FROM public.hd_systems WHERE system_id = $1` (gecached pro Job-Sequenz).

---

## 8) Referenzen

- **Layer-Übersicht:** `layers_overview.md` (Kritische Ergänzung 5)
- **Dimensions-Schema:** `dimensions_contract.md` (Core + body_mechanics, environment, relationship_pattern, projection_field)
- **Interpretations-Payload:** `interpretations_contract.md` (payload.dimensions muss alle Keys aus dimensions_contract enthalten)
- **Worker-Contract:** `worker_contract_system_descriptor.md`
- **Abgleich:** `layer_implementation_abgleich.md` (System Descriptor als „später nötig“ → jetzt Spec + Descriptoren + Migration angelegt)

---

## 9) Status & Mini-Hinweise

| Thema | Status / Hinweis |
|-------|-------------------|
| **hd_interpretations.payload** | Entspricht der neuen LLM-Prompt-Definition: `interpretations_contract.md` und Worker (`_default_interpretation_payload_shape` + LLM-Prompt) definieren dieselben Keys inkl. der 12 Dimensions-Slots (Core + body_mechanics, environment, relationship_pattern, projection_field). Gespeicherte Payloads haben dieses Schema. |
| **text2kg – Edges** | Im MVP erzeugt text2kg **noch keine Kanten** (relation_types). Der Descriptor enthält `kg_rules.allowed_relation_types`; diese werden künftig für Edge-Erzeugung genutzt. |
| **term_mapping – Seeds** | Seeds für Term-Mapping existieren derzeit nur für HD/BaZi. Descriptoren für Astro, Jyotish etc. sind angelegt; entsprechende Seeds können später ergänzt werden. |
