# IC Extraktion — 25. Feb 2026 Chat 2 — Chunk 5/5

> **Scope:** Leitdokument v3 als Chat-Artefakt — Schicht E (Synthese-Überschuss) + Schicht F (Delta gegen Leitdokument v2 + PRD v3)

---

## META

| Feld | Wert |
|------|------|
| Quelle | Leitdokument v3 (28 Seiten, DOCX-Artefakt) + Delta-Analyse-Dokument (16 Seiten) |
| Referenz | Leitdokument v2 (aus Chat 1), PRD v3 |
| Typ | ARTEFAKT-EXTRAKTION |
| Strategie | C — Chunk 5/5 |
| Kürzel | KC25 |

---

## SCHICHT E — SYNTHESE-ÜBERSCHUSS (im Artefakt, nie im Chat besprochen)

---

### E-KC25-01: Neues Kapitel XIII — Wissensextraktion & KG Quality (komplett)
**Inhalt:** Vollständiges Kapitel mit: Quellenstrategie-Reihenfolge (3 Schritte), Quellenklassen (Primär/Sekundär/Tertiär mit Verwendungsregeln), Chunking-Standards (500–1500 Tokens, 100 Overlap, Metadaten), Provenance & QA (confidence < 0.7 → auto-flag für human_review), Lizenz-Policy. Im Chat wurde nur die Reihenfolge und AL-Korrektur besprochen, nicht die Details.
**Typ:** KAPITEL
**Qualität:** WERTVOLL — operationalisiert E-28 komplett
**Im Ist-Stand?:** TEILWEISE — cursor/pipeline.md hat einiges, aber Chunking-Standards und QA-Thresholds fehlen dort

---

### E-KC25-02: Schema-Erweiterungen (Kap. X.4) — Node-Schema mit dynamic_type + phase + source_provenance
**Inhalt:** Vollständiges JSON-Schema für Nodes mit neuen Feldern: `dynamic_type: enum`, `phase: int|null`, `source_provenance: { source_id, page, chunk_id, text_snippet, language, confidence, human_reviewed }`. Im Chat wurde nur das Prinzip besprochen, nie das konkrete Schema.
**Typ:** SCHEMA
**Qualität:** WERTVOLL — direkt implementierbar
**Im Ist-Stand?:** TEILWEISE — cursor/architecture.md hat sys_nodes, aber ohne dynamic_type und provenance-Felder

---

### E-KC25-03: System-Annotation als eigener Node-Typ
**Inhalt:** `system_annotation` als neuer Node-Typ in X.2 — speichert Lehrsprache einzelner Autoren (z.B. Ra Uru Hu Formulierungen). Benötigt `human_review=true` bevor user-facing. Im Chat wurde nur "Lehrsprache separat speichern" besprochen, der Node-Typ ist Synthese.
**Typ:** SCHEMA
**Qualität:** WERTVOLL — löst das IP-Problem (E-13) auf Schema-Ebene
**Im Ist-Stand?:** UNKLAR — nicht in cursor/contracts.md gefunden

---

### E-KC25-04: Lebensbereiche-Liste v3 (verändert gegenüber v2)
**Inhalt:** Die 11 Bereiche in v3 weichen von v2 ab: "Sexualität & Intimität" wurde zu "Transformation & Wachstum", "Beziehungen & Community" zu "Gemeinschaft & Gesellschaft", "Kreativität & Ausdruck" zu "Kommunikation & Ausdruck". Diese Umbenennungen wurden im Chat NICHT besprochen — reine KI-Synthese.
**Typ:** DEFINITION
**Qualität:** PRÜFUNGSBEDARF — Umbenennungen sind nicht begründet und könnten gewollt oder versehentlich sein
**Im Ist-Stand?:** UNKLAR — aktuelle Version in IC_Leitdokument v5.1 könnte anders sein

---

### E-KC25-05: Edge-Typen erweitert (X.3)
**Inhalt:** Neue Edge-Typen in v3: `influences` (kausaler Einfluss), `deepens` (Vertiefungsbeziehung A→B→C), `active_during` (zeitliche Aktivierung), `belongs_to_domain`, `part_of_phase`. Im v2 gab es nur: maps_to, belongs_to, contributes_to, relevant_for, activated_in, contradicts, expresses_as. "deepens" und "part_of_phase" sind konzeptionell neu.
**Typ:** SCHEMA
**Qualität:** PLAUSIBEL — "deepens" bildet die Schichtlogik A→B→C im KG selbst ab
**Im Ist-Stand?:** UNKLAR

---

### E-KC25-06: Phasen-Umbenennung (IV)
**Inhalt:** Die 7 Phasen in v3 haben teilweise andere Namen als in v2: Phase 1 "Ankommen" → "Erkennen". Phase 2 "Erkennen" → "Verstehen". Phase 4 "Disposition" → "Schatten". Phase 5 "Konfrontation" → "Navigation". Die Umbenennungen wurden im Chat NICHT besprochen.
**Typ:** DEFINITION
**Qualität:** PRÜFUNGSBEDARF — "Schatten" statt "Disposition" ändert den Fokus erheblich. Phase 4 war im Chat der "KERNMOMENT" (Meta-System erlebbar), jetzt heißt sie "Schatten" (Konfrontation). Das ist eine signifikante Bedeutungsverschiebung.
**Im Ist-Stand?:** UNKLAR — v5.1 Benennung prüfen

---

### E-KC25-07: Change-Log komplett (Kap. XX)
**Inhalt:** 17 Einträge im Change-Log, datiert 25.02.2026, dokumentierend v1→v2→v3 mit allen Quellen pro Änderung. Reine Governance-Synthese.
**Typ:** TABELLE
**Qualität:** WERTVOLL
**Im Ist-Stand?:** JA — Change-Log-Praxis beibehalten

---

## SCHICHT F — DELTA: ARTEFAKT (v3) vs. REFERENZ-DOCS (v2, PRD v3)

---

### F-KC25-01: Leitdokument v2 → v3: 6 neue Entscheidungen (E-25 bis E-30)
**Referenz-Doc:** Leitdokument v2
**Art:** BEWUSSTE-ÄNDERUNG
**Inhalt:** E-25 Dynamics-Taxonomie, E-26 HD-Zerlegungslogik, E-27 Scores experimental, E-28 Quellenstrategie, E-29 Wissensquellen Research, E-30 KI-Kulturdarstellung. Alle im Chat besprochen und entschieden.
**Relevanz:** HOCH — aber dokumentiert, also kein Verlustrisiko

---

### F-KC25-02: Phasen-Umbenennung ohne Chat-Diskussion
**Referenz-Doc:** Leitdokument v2 (Kap. IV)
**Art:** UNBEWUSSTE-DRIFT
**Inhalt:** Phase 1 "Ankommen"→"Erkennen", Phase 4 "Disposition"→"Schatten" etc. (siehe E-KC25-06). Nicht im Chat besprochen. Besonders Phase 4: "Disposition" (Staunen, Meta-System erlebbar) vs. "Schatten" (Konfrontation) ist eine fundamentale Tonänderung.
**Relevanz:** HOCH — Kernmoment-Phase wurde semantisch umgedeutet

---

### F-KC25-03: Lebensbereiche-Umbenennung ohne Chat-Diskussion
**Referenz-Doc:** Leitdokument v2 (Kap. IX)
**Art:** UNBEWUSSTE-DRIFT
**Inhalt:** "Sexualität & Intimität" → "Transformation & Wachstum" etc. (siehe E-KC25-04). Nicht besprochen. "Sexualität" als eigenständiger Bereich war eine bewusste Entscheidung in Chat 1 (D-KON25-06).
**Relevanz:** HOCH — verworfen eine Entscheidung aus Chat 1 ohne Begründung

---

### F-KC25-04: Neues Kapitel XIII komplett ohne Chat-Vorlage
**Referenz-Doc:** Leitdokument v2
**Art:** BEWUSSTE-ÄNDERUNG (aus Deep Review Punkt 2)
**Inhalt:** Wissensextraktion & KG Quality als vollständiges neues Kapitel. War im Chat als "Quellenstrategie-Reihenfolge verbindlich" besprochen, aber die Detailtiefe (Chunking-Standards, QA-Thresholds, Quellenklassen) ist Synthese.
**Relevanz:** MITTEL — wertvolle Ergänzung, keine Drift

---

### F-KC25-05: Edge-Typen-Erweiterung ohne Chat-Diskussion
**Referenz-Doc:** Leitdokument v2 (Kap. X.3)
**Art:** UNBEWUSSTE-DRIFT
**Inhalt:** Neue Edge-Typen (deepens, influences, active_during, belongs_to_domain, part_of_phase) und entfernte Edge-Typen (expresses_as aus v2 fehlt in v3). Nicht besprochen.
**Relevanz:** MITTEL — Schema-Änderung die Implementierung beeinflusst

---

## ZUSAMMENFASSUNG CHUNK 5

| Schicht | Einträge |
|---------|----------|
| E — Synthese-Überschuss | 7 |
| F — Delta v3↔v2/PRD | 5 |

**Kritischste Findings:**
1. **Phasen-Umbenennung** (F-02, E-06) — Phase 4 "Disposition" → "Schatten" ist eine unbewusste Drift die den KERNMOMENT des Produkts semantisch verändert. Muss überprüft werden ob v5.1 das korrigiert hat.
2. **Lebensbereiche-Umbenennung** (F-03, E-04) — "Sexualität & Intimität" verschwunden ohne Begründung. War bewusste Entscheidung aus Chat 1. 
3. **Schema-Erweiterungen** (E-02, E-03, E-05) — Node-Schema mit provenance + dynamic_type und system_annotation als Node-Typ sind wertvoll und direkt implementierbar. Aber Edge-Typ-Änderungen sind undokumentiert.
