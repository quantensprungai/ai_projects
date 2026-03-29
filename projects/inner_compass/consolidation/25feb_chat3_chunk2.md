# IC Extraktion — 25. Feb 2026 Chat 3 — Chunk 2/3

> **Scope:** KG-Schema-Konsolidierung (v1.0→v1.1), Extraction Prompts v1.0, System×Ebenen Mapping, Schema-Korrekturen

---

## META

| Feld | Wert |
|------|------|
| Quelle | Chat 3, 25. Feb 2026 |
| Typ | KONSTRUKTION (Schema + Pipeline) |
| Strategie | C — Chunk 2/3 |
| Kürzel | KV25 |

---

## SCHICHT A — SUBSTANZ

---

### A-KV25-10: 10 neue KG-Felder aus Synthese-Lexikon
**Inhalt:** ontological_layer (INT 1–13, HD-intern), activation_mode (conscious/unconscious/dual/open), expression_quality (exaltation/detriment/variable), expression_stern (BOOLEAN — nicht Enum!), development_stage (distorted/aligned/transcendent, system-agnostisch), circuit (individual/tribal/collective), chart_position (upper/lower), planetary_source (ENUM), planetary_weight (FLOAT 0.0–1.0), golden_path_sequence (activation/venus/pearl/saturn). Plus school_references als Array (nicht festes Objekt).
**Tag(s):** [SCHEMA] [ENTSCHEIDUNG]
**Reifegrad:** IMPLEMENTIERT (in IC_KG_Schema v1.1)
**Beziehung:** ERGÄNZUNG zu E-36 (level_tag als Pflichtfeld)
**Ziel-Bereich:** IC_KG_Schema v1.1, cursor/architecture.md
**Herkunft:** CHAT + ARTEFAKT

---

### A-KV25-11: v3-Gaps in v4 wiederhergestellt
**Inhalt:** 5 Edge-Typen fehlten in v4 (influences, deepens, active_during, belongs_to_domain, part_of_phase). 5 Node-Typen fehlten in v4 (domain, experiment, life_event, inner_strategy, system_annotation). dimension_key als Pflichtfeld fehlte. KG-Schicht E hatte unterschiedliche Bedeutung (v3: Meta-Nodes, v4: User-Aktion → beides muss koexistieren: Innere Strategie = Schicht C, User-Aktion = Schicht E). Alle wiederhergestellt in Schema v1.0.
**Tag(s):** [CODE-KONZEPT-GAP] [SCHEMA]
**Reifegrad:** IMPLEMENTIERT
**Beziehung:** KORREKTUR von v4-Verlust
**Ziel-Bereich:** IC_KG_Schema
**Herkunft:** CHAT (Gap-Analyse)

---

### A-KV25-12: 3 kritische Schema-Korrekturen (v1.0→v1.1)
**Inhalt:** (1) expression_stern = Boolean, nicht eigener Enum-Wert. Stern = Exaltation + Detriment gleichzeitig auf derselben Linie. (2) development_stage = system-agnostisch (distorted/aligned/transcendent statt shadow/gift/siddhi). Schuloriginalvokabular in school_references[].stage_label erhalten. (3) school_references = Array mit optionalem lens_type, nicht festes HD-Objekt. Auch BaZi (Joey Yap vs. klassisch), Jyotish (Parashara vs. Jaimini), Astro haben Schulen.
**Tag(s):** [SCHEMA] [ENTSCHEIDUNG]
**Reifegrad:** IMPLEMENTIERT
**Beziehung:** KORREKTUR v1.0→v1.1
**Ziel-Bereich:** IC_KG_Schema v1.1
**Herkunft:** CHAT (User-Korrekturen)

---

### A-KV25-13: 12 Extraction Prompts (P-A01 bis P-QA03)
**Inhalt:** Pipeline-vollständig: P-A01 Entitäten (alle Systeme), P-A02 HD-spezifisch (Gates/Kanäle), P-B01 Interpretationen+Lehrsprache, P-B02 Dynamic-Type-Klassifikation, P-C01 Cross-System-Bridges, P-C02 Widersprüche, P-C03 Meta-Nodes (≥3 Systeme), P-D01 Handbuch-Schicht-1, P-E01 Experiment-Generierung, P-QA01 level_tag-Validierung, P-QA02 human_review-Check, P-QA03 Schema-Vollständigkeit. STOPP-Gate zwischen C und D. Lizenz-Gate vor Schritt 1.
**Tag(s):** [ARCHITEKTUR] [SCHEMA]
**Reifegrad:** IMPLEMENTIERT (in IC_Extraction_Prompts v1.0)
**Beziehung:** OPERATIONALISIERUNG von E-28 (Quellenstrategie)
**Ziel-Bereich:** IC_Extraction_Prompts v1.0
**Herkunft:** ARTEFAKT

---

### A-KV25-14: P-D02/D03/D04 fehlen (Gap erkannt)
**Inhalt:** Nur P-D01 (Handbuch-Schicht 1) existiert. P-D02 (Synthese), P-D03 (Prozess), P-D04 (Experiment) fehlen. Zudem: P-D04 vs. P-E01 sind konzeptuell zwei verschiedene Dinge — Handbuch-Text Schicht 4 (D-Node, User liest) vs. strukturierter Selbstversuch (E-Node, User handelt). Beide werden gebraucht.
**Tag(s):** [LÜCKE]
**Reifegrad:** ASSERTION
**Beziehung:** GAP in IC_Extraction_Prompts
**Ziel-Bereich:** IC_Extraction_Prompts v1.1
**Herkunft:** CHAT (Gap-Analyse)

---

### A-KV25-15: System×Ebenen×UX-Phase Mapping-Tabelle (48 Elemente)
**Inhalt:** 48 Elemente aus 7 Systemen, vollständig gemappt auf: system_class, level_tags (1–7), ux_phases (1–7), kg_layer, dynamic_type, human_review. Kernbefunde: Ebene 4 (Disposition) ist die dichteste — fast jeder System hat dort Einstieg. Gene Keys: alle human_review required + Lizenz-Hinweis. Ebene 7 (Dharma) konsequent erst in UX-Phase 6–7.
**Tag(s):** [SCHEMA] [ARCHITEKTUR]
**Reifegrad:** IMPLEMENTIERT (CSV + XLSX)
**Beziehung:** OPERATIONALISIERUNG von E-36 (System×Ebenen)
**Ziel-Bereich:** IC_System_Ebenen_UXPhase_Mapping v1.0
**Herkunft:** ARTEFAKT

---

### A-KV25-16: "Das ist kein Schema-Problem — das ist ein Prompt-Engineering-Problem"
**Inhalt:** Die Dynamics-Differenzierung (phase_cycle/trap/growth_path/spectrum) braucht keine Schema-Änderung — der dynamic_type ENUM deckt es ab. Die Abgrenzung muss im LLM-Extraktions-Prompt kalibriert werden, nicht im Schema. Extraktions-Signale pro Typ definiert.
**Tag(s):** [KLÄRUNG] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** BESTÄTIGUNG von E-25
**Ziel-Bereich:** IC_Extraction_Prompts
**Herkunft:** CHAT

---

## SCHICHT C — KI-SELBSTKORREKTUREN

---

### C-KV25-01
**Ursprüngliche Aussage:** expression_quality: exaltation | detriment | stern | variable (4 Enum-Werte)
**Korrektur:** User: "stern ist glaube ich exaltation + detriment zusammen." → expression_stern = Boolean, expression_quality bleibt 3-wertig.
**Relevanz:** HOCH — Schema-Korrektur mit Implementierungs-Impact

---

### C-KV25-02
**Ursprüngliche Aussage:** frequency_level: shadow | gift | siddhi (Gene-Keys-spezifisch)
**Korrektur:** User: "ist das nicht zu system spezifisch?" → development_stage: distorted | aligned | transcendent (system-agnostisch). Schulvokabular in stage_label erhalten.
**Relevanz:** HOCH — Prinzip-Korrektur für system-agnostische Architektur

---

### C-KV25-03
**Ursprüngliche Aussage:** school_reference: {classical_hd, gene_keys, quantum_hd} (festes HD-Objekt)
**Korrektur:** User: "gibt es vielleicht auch in den anderen systemen weitere schulen?" → school_references als Array, generisch für alle Systeme.
**Relevanz:** HOCH — Architektur-Korrektur

---

## SCHICHT D — NUTZER-KLÄRUNGSMOMENTE

---

### D-KV25-03
**Nutzer-Impuls:** "die nodes und edges müssen wir nochmal überprüfen. sind das jetzt weniger geworden oder ist das eine zusätzliche sichtweise?"
**Ergebnis:** Systematischer Vergleich KG-Schema aktuell vs. Synthese-Lexikon. 10 neue Felder identifiziert, 5 fehlende Edge-Typen, 5 fehlende Node-Typen, KG-Schicht-E-Konfusion aufgedeckt. Führt zum vollständigen IC_KG_Schema v1.0.
**Relevanz:** HOCH — Trigger für die gesamte Schema-Konsolidierung

---

## ZUSAMMENFASSUNG CHUNK 2

| Schicht | Einträge |
|---------|----------|
| A | 7 |
| C | 3 |
| D | 1 |

**Top-3 Erkenntnisse:**
1. **3 User-Korrekturen** (C-01/02/03) — expression_stern Boolean, development_stage system-agnostisch, school_references Array. Jede einzelne hat das Schema fundamental verbessert.
2. **v3-Gaps wiederhergestellt** (A-11) — 10 Node/Edge-Typen die zwischen v3→v4 verloren gingen. Plus KG-Schicht-E-Konfusion aufgelöst.
3. **48-Element Mapping-Tabelle** (A-15) — erstes vollständiges System×Ebenen×Phase Mapping. Direkt als KG-Extraktions-Regelwerk verwendbar.
