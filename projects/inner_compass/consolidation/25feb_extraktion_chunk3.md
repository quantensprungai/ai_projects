# IC Extraktion — 25. Feb 2026 Chat — Chunk 3/4

> **Scope:** Eingebettete Hintergrund-Docs (alter Master v0.1, Vision/Story/UX, Inspirationen, Ideen/Backlog) — was steht dort, das NICHT bereits in den Gen-2-Docs (PRD v3, Master v2, Strang 0) oder in den Chat-Diskussionen (Chunk 1+2) abgedeckt ist? Fokus auf verlorenes/nicht-migriertes Wissen.

---

## META

| Feld | Wert |
|------|------|
| Quelle | 4 eingebettete Dokumente im Konsolidierungs-Chat |
| Typ | EVALUATION (Delta-Analyse: Was fehlt in Gen 2?) |
| Strategie | C — Chunk 3/4 |
| Kürzel | KON25 |

### Eingebettete Dokumente:
- **DOC-M01**: Alter Master v0.1 (Juni 2025) — ~8.000 Wörter, Kap. I–XIII
- **DOC-VIS**: Vision, Story & UX — konsolidiert aus 5 hd_saas-Docs
- **DOC-INS**: Inspirationen & Theoretischer Hintergrund
- **DOC-IDE**: Ideen & Backlog

---

## SCHICHT A — SUBSTANZ

### Aus DOC-M01 (Alter Master v0.1) — Verlorenes bei Migration

---

### A-KON25-31: Hypothesenregister H-01 bis H-07 (Migration-Verlust)
**Inhalt:** Der alte Master enthält ein explizites Hypothesenregister mit 7 testbaren Hypothesen: H-01 Konvergenz, H-02 Spiegel>Test, H-03 Mehrsystem-Überlegenheit, H-04 Progressive Enthüllung, H-05 Experiment>passiv, H-06 Kulturübergreifende Resonanz (Fremd-Systeme unterbrechen Bestätigungsfehler), H-07 Selbst-Redundanz (Empowerment>Sucht). In Gen-2-Docs existieren die Thesen (Strang 0 v0.3), aber NICHT als testbare Hypothesen mit empirischem Bezug.
**Tag(s):** [LÜCKE] [CODE-KONZEPT-GAP]
**Reifegrad:** ARGUMENTATION
**Beziehung:** AUSLASSUNG — fehlt in Master v2 und PRD v3
**Ziel-Bereich:** Leitdokument Kap. XVII (Hypothesenregister)
**Herkunft:** ARTEFAKT (DOC-M01)

---

### A-KON25-32: KG-Schema-Detail (Node-/Edge-Typen, Qualitätsmetriken)
**Inhalt:** Alter Master definiert detaillierte Node-Typen (system_concept, meta_node, domain, phase, experiment, life_event) und Edge-Typen (maps_to mit confidence, belongs_to, contributes_to, relevant_for, activated_in, contradicts). Plus Qualitätsmetriken: confidence 0.0–1.0, source (embedding/llm/human/community), review_status, systems_supporting. Meta-Nodes erst ab 3+ systems_supporting. In PRD v3 teilweise vorhanden, aber weniger detailliert.
**Tag(s):** [SCHEMA] [CODE-KONZEPT-GAP]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG von PRD v3 Schicht D+E
**Ziel-Bereich:** cursor/architecture.md, KG-Schema
**Herkunft:** ARTEFAKT (DOC-M01)

---

### A-KON25-33: Pipeline-Architektur (5 Jobs vs. 3 in PRD)
**Inhalt:** Alter Master: 5 Jobs (extract_entities → generate_embeddings → cross_system_matching → generate_meta_nodes → human_review_queue). PRD v3 hat nur 3 Jobs implizit. Die 5-Job-Architektur ist vollständiger und enthält die human_review_queue als expliziten Qualitätssicherungsschritt.
**Tag(s):** [CODE-KONZEPT-GAP]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG von PRD v3 Pipeline
**Ziel-Bereich:** cursor/pipeline.md
**Herkunft:** ARTEFAKT (DOC-M01)

---

### A-KON25-34: Staffel × Phase Matrix (Planungswerkzeug)
**Inhalt:** Detaillierte Matrix welche Inhalte in welcher Staffel × Phase verfügbar sind. Z.B. Staffel 1 deckt Phasen 1–5 ab, Phase 6+7 brauchen Staffel 2. Staffel 3 füllt selektiv (kulturelle Breite + Wurzel-Weisheit). Fehlt in Gen-2-Docs komplett.
**Tag(s):** [LÜCKE]
**Reifegrad:** ASSERTION
**Beziehung:** AUSLASSUNG aus Gen-2
**Ziel-Bereich:** Leitdokument Kap. XI.2
**Herkunft:** ARTEFAKT (DOC-M01)

---

### A-KON25-35: Biografischer Kontext — detaillierte Abfrage-Strategie
**Inhalt:** Alter Master Kap. VIII.2: Was wir abfragen (Geschwisterposition, Lebensereignisse, Beziehungsstatus, Bildungsweg, aktuelle Lebensphase). WIE wir abfragen: Phase 0 (max 3–6 Items, überspringbar), Phase 2 (Mikro-Assessments), Phase 5 (story-basierte Tiefenreflexion), Persistent (Lebenskontext-Profil). Plus klare Ausschlüsse: keine klinischen Diagnosen, keine Therapie-Empfehlung, keine Pflichtabfragen, keine Weitergabe.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG von E-24 (Biografie-Layer). Detaillierter als Chat-Diskussion.
**Ziel-Bereich:** Leitdokument Kap. XII
**Herkunft:** ARTEFAKT (DOC-M01)

---

### A-KON25-36: Technische Schema-Anforderungen (user_life_events, user_context_snapshot)
**Inhalt:** Alter Master Kap. IX: Zwei neue Tabellen definiert. user_life_events (id, user_id, event_type, event_date_approx, age_at_event, narrative_text, structured_tags, privacy_flag, created_at). user_context_snapshot (id, user_id, household_type, education_level, relationship_status, children_count, health_flags, updated_at). Fehlt komplett in cursor/architecture.md.
**Tag(s):** [SCHEMA] [CODE-KONZEPT-GAP]
**Reifegrad:** ARGUMENTATION
**Beziehung:** AUSLASSUNG aus technischen Docs
**Ziel-Bereich:** cursor/architecture.md
**Herkunft:** ARTEFAKT (DOC-M01)

---

### A-KON25-37: Innere-Strategie-Output-Format (alter Master)
**Inhalt:** Alter Master VIII.3: Output ist "Hypothese in eigener Sprache" — Beispiel: "Dein wiederkehrendes Muster unter Druck scheint Rückzug und Analyse zu sein — das passt zu deiner offenen Emotionalzentrum-Thematik in HD und deinem Wasser-Überschuss in BaZi". Kein Typ-Label, sondern narrative Hypothese. Plus Konzeptpapier-Anforderung: Taxonomie der Strategien, Mapping auf Geburtssystem-Indikatoren, Fragenkatalog, Sprachregister.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ASSERTION
**Beziehung:** VERTIEFUNG von E-19 (Innere Strategie)
**Ziel-Bereich:** OE-09 (Konzeptpapier Innere Strategie)
**Herkunft:** ARTEFAKT (DOC-M01)

---

### Aus DOC-VIS (Vision, Story & UX) — Ergänzungen

---

### A-KON25-38: True Core Story — 7 Kapitel (narrativ, nicht technisch)
**Inhalt:** Story-Kapitel für öffentliche Kommunikation: (1) Die Zeit der Verluste, (2) Die Fragmente, (3) Die erste Verbindung (Synchronicity), (4) Die Plattform entsteht, (5) Die Welt erwacht (viral), (6) Der Übergang 2027, (7) Das Loslassen. Verbindung zu Plattform-Features pro Kapitel. Unterschiedlich von den 7 Phasen (Heldenreise des Users) — das hier ist die META-STORY des Projekts.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ASSERTION
**Beziehung:** ERGÄNZUNG zu Story/Release-Architektur (E-23). ACHTUNG: Diese 7 Kapitel ≠ die 7 Phasen der Heldenreise!
**Ziel-Bereich:** Strang 2 / Vermittlung, Leitdokument Kap. XI
**Herkunft:** ARTEFAKT (DOC-VIS)

---

### A-KON25-39: Plattform-Phasen synchron zur Story (6 Phasen, 24 Monate)
**Inhalt:** Phase 1 "Der Ruf" (Mo.1–2): Core Profile, Daily Signal. Phase 2 "Fragmente" (3–4): Dual-System, Insights Feed. Phase 3 "Synthesis" (5–6): Cross-System-Karte, Relationship. Phase 4 "Erwachen" (7–12): Timeline, AI Coach. Phase 5 "Selbstermächtigung" (12–18): Mentorless Mode. Phase 6 "Loslassen" (18–24): Opt-in Deactivation, Legacy Mode.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ASSERTION
**Beziehung:** ERGÄNZUNG zu E-23. Timing-Perspektive die im Leitdokument fehlt.
**Ziel-Bereich:** Strang 1 / Roadmap
**Herkunft:** ARTEFAKT (DOC-VIS)

---

### A-KON25-40: Expertensprache versteckt, dann erforschbar
**Inhalt:** Default: Nur Muster, Zyklen, Kräfte — keine Gates, Nakshatras, Stems. Optional: Tab "Mechanik anzeigen" für Deep Divers / Profis. User sagt NICHT "Analysiere Mars über Gate 21" sondern "Warum fühle ich mich heute so gedrückt?" — Agent übersetzt intern.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG von E-09 (Drei Sprachebenen)
**Ziel-Bereich:** Strang 1 / UX
**Herkunft:** ARTEFAKT (DOC-VIS)

---

### A-KON25-41: Vision 2027 — MCP-Readiness
**Inhalt:** 2027: Menschen sprechen mit ihren AIs; AIs sprechen über MCP mit unserer App. App muss MCP-ready sein: Fremde Agents können Patterns, KG-Statements, Synthesis-Texte, Diagramme, Zeitzyklen abrufen. Positionierung: "Erste Multi-System-AI-Archetypen-Intelligence — persönlicher Agent, spirituelle OS-Layer."
**Tag(s):** [ARCHITEKTUR] [RISIKO]
**Reifegrad:** STUB
**Beziehung:** ERGÄNZUNG — fehlt in allen aktuellen Docs
**Ziel-Bereich:** Strang 1 / Technische Vision, cursor/architecture.md
**Herkunft:** ARTEFAKT (DOC-VIS)

---

### A-KON25-42: App-Namen-Kandidaten
**Inhalt:** LUMA, ORA, KAI, ANIMA, ORIN, MIRA, AEONIA, ARKEA, NUMA, SOLARA, KINO, SENDA, LARENA, AURA, INARI. Kriterien: Bedeutung ohne Dogma, international, zeitlos.
**Tag(s):** [NAMING-EVOLUTION]
**Reifegrad:** STUB
**Beziehung:** ERGÄNZUNG zu OE-01 (Naming)
**Ziel-Bereich:** Branding
**Herkunft:** ARTEFAKT (DOC-VIS)

---

### Aus DOC-INS (Inspirationen) — Quelleneinordnung

---

### A-KON25-43: IFS-Haltung übernommen, nicht System
**Inhalt:** Von IFS übernommen: "Teile haben verschiedene Rollen und Absichten" (resoniert mit HD-Zentren, BaZi-Pillars, Astro-Planeten). 4-Schritt-Prozess: Erkennen→In Beziehung treten→Verstehen→Integrieren. Haltung der Neugier statt Bewertung. NICHT übernommen: IFS-Terminologie (Parts, Exile, Manager), Therapie-Anspruch, Self-Begriff.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG der Prozess-Schicht (Handbuch Schicht 3+4)
**Ziel-Bereich:** Leitdokument, Inspirationen-Referenz
**Herkunft:** ARTEFAKT (DOC-INS)

---

### A-KON25-44: Gene Keys — Shadow/Gift-Rahmen als systemübergreifendes Konzept
**Inhalt:** Gene Keys Shadow→Gift→Siddhi wird als dimension_key (shadow, gift) systemübergreifend angewendet — nicht nur für Gene Keys selbst. Das Spektrum-Modell (dynamic_type: spectrum) ist die Abstraktion. Gene Keys ist Staffel 2, aber das Konzept wird ab Staffel 1 genutzt.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG des Dimensions-Contract (shadow/gift Dimensions)
**Ziel-Bereich:** cursor/contracts.md, KG-Architektur
**Herkunft:** ARTEFAKT (DOC-INS)

---

### Aus DOC-IDE (Ideen/Backlog) — Offene Ideen

---

### A-KON25-45: Priority Rules / Emergent Logic / Conflict Resolution
**Inhalt:** Wenn Dimensionen kollidieren (Type vs. Authority in HD): Authority > Type > Profile als Regelwerk. Emergent Logic: offenes Solarplexus + Generator = neues Muster → braucht Reasoning-Layer. Conflict Resolution bei widersprüchlichen Quellen: Interpretationen bleiben getrennt, Synthesis konsolidiert oder zeigt quellenspezifisch.
**Tag(s):** [ARCHITEKTUR] [LÜCKE]
**Reifegrad:** STUB
**Beziehung:** ERGÄNZUNG — fehlt in KG-Architektur
**Ziel-Bereich:** cursor/architecture.md (Reasoning-Layer)
**Herkunft:** ARTEFAKT (DOC-IDE)

---

### A-KON25-46: Daily Compass als Retention-Mechanismus
**Inhalt:** Tägliche Push-Notification: "Heute ist Maya Kin X, dein Transit ist Y, dein BaZi Tageseinfluss ist Z. Fokus: [Lebensbereich]." Vereint alle 4 Dynamik-Dimensionen in einem täglichen Touchpoint.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** STUB
**Beziehung:** ERGÄNZUNG zu Feature-Map
**Ziel-Bereich:** Strang 1 / Feature-Backlog
**Herkunft:** ARTEFAKT (DOC-IDE)

---

## SCHICHT B — END-OF-ANSWER DIREKTIVEN

Nicht anwendbar für eingebettete Dokumente (keine Dialog-Enden).

---

## SCHICHT C — KI-SELBSTKORREKTUREN

Nicht anwendbar für eingebettete Dokumente.

---

## SCHICHT D — NUTZER-KLÄRUNGSMOMENTE

Nicht anwendbar für eingebettete Dokumente.

---

## ZUSAMMENFASSUNG CHUNK 3

| Schicht | Einträge |
|---------|----------|
| A — Substanz | 16 (A-KON25-31 bis A-KON25-46) |
| B — End-of-Answer | 0 (Dokumente, kein Dialog) |
| C — KI-Korrekturen | 0 |
| D — Nutzer-Klärungen | 0 |

**Top-3 Erkenntnisse:**
1. **Hypothesenregister** (A-31) — komplett verloren bei Gen-1→Gen-2-Migration. Existiert im alten Master als 7 testbare Hypothesen, fehlt in Master v2 und PRD v3 vollständig. Für Strang 3 (Forschung) kritisch.
2. **True Core Story ≠ 7 Phasen** (A-38) — die öffentliche Projekt-Story (7 Kapitel) und die User-Heldenreise (7 Phasen) sind zwei verschiedene Dinge. Diese Unterscheidung fehlt in den aktuellen Docs.
3. **Technische Schema-Lücken** (A-32, A-33, A-36) — user_life_events, user_context_snapshot, 5-Job-Pipeline, KG-Qualitätsmetriken — alles im alten Master definiert, nicht in cursor/ migriert.

**Weiter mit Chunk 4:** Leitdokument v2.0 Artefakt-Extraktion (Schicht E: Synthese-Überschuss + Schicht F: Delta gegen Referenz-Docs)
