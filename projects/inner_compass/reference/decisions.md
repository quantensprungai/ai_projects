# Inner Compass — Design-Entscheidungen

> Lebendes Dokument. Neue Entscheidungen oben anfügen. Format: Decision → Rationale → Consequences.

---

## 2026-02-16: Dokumentations-Architektur (Zweischicht)

**Decision:** Cursor-Docs (6 Dateien, < 300 Zeilen, rein technisch) getrennt von Reference-Docs (PRD, Entscheidungen, Ideen, Inspirationen).

**Rationale:** Cursor braucht technische Wahrheit ohne Vision-Ballast. Der Mensch braucht den größeren Kontext. Zwei verschiedene Leser = zwei verschiedene Doc-Sets.

**Consequences:** cursor/ Ordner wird in Cursor-Rule referenziert. reference/ wird nur bei explizitem Verweis gelesen. Alte Docs → 99_archive/.

---

## 2026-02-16: 10 statt 8 Lebensbereiche

**Decision:** Sexualität & Intimität und Beziehungen & Community als eigenständige Bereiche.

**Rationale:** Bei 8 waren Sexualität in "Partnerschaft" und Community in "Familie" versteckt. Jedes System hat zu beiden Themen eigenständige, substantielle Aussagen (HD Sakral/Intimität, BaZi Peach Blossom, Astro 8.Haus). 10 Segmente im Kreis = 36° pro Segment, visuell sauber.

**Consequences:** life_domain Enum hat 10 Werte statt 8. Mandala hat 10 Segmente. Kein Schema-Impact (Tag, nicht Constraint).

---

## 2026-02-16: Mandala als Signatur statt Radar-Chart mit Tiefe

**Decision:** Die persönliche Landkarte zeigt nicht "Beziehung ist wichtiger als Beruf" (Tiefe-Metapher), sondern den gesamten visuellen Abdruck als einzigartige Signatur.

**Rationale:** Tiefe impliziert Bewertung. Die Form des Kompass IST die Signatur — asymmetrisch, einzigartig, ohne Wertung. Äußere Silhouette = Dichte der Chart-Elemente. Farbe = Systemübereinstimmung. Leuchtende Akzente = zeitliche Aktivität.

**Consequences:** Kein "Score" pro Lebensbereich nötig. Stattdessen: Zählung der Chart-Elemente pro Bereich + Farbkodierung. SM-teilbar als Fingerabdruck.

---

## 2026-02-16: Fluss-Diagramm als separater Visualisierungsmodus

**Decision:** Neben dem Mandala (WAS habe ich) ein Fluss-Diagramm (WIE hängt es zusammen), inspiriert vom Gene Keys Hologenetic Profile.

**Rationale:** Mandala = räumlich, statisch, Exploration. Fluss-Diagramm = prozesshaft, dynamisch, Narrativ. Verschiedene Fragen → verschiedene Visualisierungen.

**Consequences:** Fluss-Diagramm ist Phase 2-3 (braucht Schicht D für Cross-System-Flüsse). Premium-Feature.

---

## 2026-02-16: 15 statt 12 Dimensionen

**Decision:** 3 neue Keys: elemental_quality, temporal_phase, destiny_pattern.

**Rationale:** BaZi (Wuxing), Jyotish (Dashas), Maya (Farben) brauchen diese Dimensionen. Ohne sie sind 30%+ der System-spezifischen Bedeutungen nicht abbildbar.

**Consequences:** Nullable jsonb-Feld, keine Breaking Change. Alte Daten bleiben gültig. Pipeline-Prompts anpassen. 11 Kern-Dimensionen (user-facing), 4 ergänzende (system-spezifisch).

---

## 2026-02-16: Drei Sprachebenen (Wording-Strategie)

**Decision:** System-Ebene (Original-Terminologie), Meta-Ebene (eigenes Wording für übergreifende Konzepte), Handbuch-Ebene (Alltagssprache).

**Rationale:** Copyright-Schutz (Not-Self, Useful God sind geschützt). Verständlichkeit (Fachtermini unverständlich für Laien). Synthese-Mehrwert (wenn 3 Systeme dasselbe beschreiben, braucht es einen eigenen Begriff).

**Consequences:** Wording entsteht als Nebenprodukt von generate_meta_nodes. LLM schlägt vor, Mensch finalisiert.

---

## 2026-02-16: Keine Entwicklungsstufen (anti-AQAL)

**Decision:** Keine hierarchische Bewertung ("du bist auf Stufe X"). Stattdessen: Zeitlinie (Phasen statt Stufen).

**Rationale:** Keines der integrierten Systeme kennt Entwicklungshierarchie. Generator ≠ "höher" als Projektor. Stufen implizieren Bewertung. Inner Compass spiegelt, bewertet nicht.

**Consequences:** Zeitlinie-Layer (Schicht C) ersetzt Stufen. Dynamische Aktualisierung statt statische Einordnung. AQAL-Quadranten als interner Qualitätscheck nutzbar (decken unsere Dimensionen alle 4 Perspektiven ab?).

---

## 2026-02-16: System-Filter als Linsen-Metapher

**Decision:** User kann zwischen "Alle Systeme" (Standard) und Einzelsystem-Linsen umschalten.

**Rationale:** Bedient 3 Zielgruppen: System-Kenner, kulturspezifische Nutzer, Einsteiger. Strategischer Nebeneffekt: Erster Cross-System-Switch wird zum größeren Aha-Moment.

**Consequences:** Trivial (system_id-Filter auf allen Queries). Handbuch-Sprache wechselt von Meta auf System-Ebene.

---

## 2026-02-16: Prozess-Layer mit 4-Schritt-Struktur

**Decision:** Erkennen → In Beziehung treten → Verstehen → Integrieren (inspiriert von IFS, ohne dessen Terminologie).

**Rationale:** IFS ist therapeutisch validiert, gibt Chart-Elementen einen konkreten Arbeitspfad. HD sagt "lebe dein Design" (vage). Wir sagen "hier sind 4 Schritte" (konkret).

**Consequences:** Neues process-Feld im Interpretations-Contract (trap, gift_activation, experiment_seed). Neuer Pipeline-Job: extract_process_patterns. Handbuch-Schicht 3+4 werden damit gefüllt.

---

## 2026-02: Postgres+pgvector statt ArangoDB/Neo4j

**Decision:** Bleiben bei Supabase/Postgres. pgvector für Embeddings.

**Rationale:** Supabase bietet Auth, RLS, Storage, Realtime. Kein separater Graph-DB-Server nötig. Edges sind eine Tabelle, Nodes sind eine Tabelle — das reicht für unsere Größenordnung.

**Consequences:** Kein Graph-Traversal-Performance-Vorteil. Wenn jemals Millionen Nodes: exportieren. Für jetzt: Einfachheit > Performance.

---

## 2026-02: Strukturbäume aus Deskriptoren, NICHT aus PDFs

**Decision:** Systemstruktur (welches Gate in welchem Center) aus JSON-Deskriptoren + Engine-Code. NICHT aus PDF-Extraktion.

**Rationale:** Struktur ist deterministisch und fest. PDFs beschreiben Interpretationen, nicht Struktur. "Gate 34 ist im Sakral-Zentrum" ist eine Tatsache, keine Interpretation.

**Consequences:** Phase 0 = Seed-Script (Deskriptor → Nodes + Edges). PDFs reichern Nodes an, erzeugen sie nicht. Graph existiert BEVOR erste PDF verarbeitet wird.

---

## 2026-02: Embeddings für Cross-System-Mapping statt manuell

**Decision:** Cosine Similarity + LLM-Validierung statt manuelles Kuratieren.

**Rationale:** Skaliert auf beliebig viele Systeme. 50 manuelle Mappings als Startpunkt, dann automatisch. LLM + Embeddings ersetzen manuelles Kuratieren komplett.

**Consequences:** pgvector Pflicht. extract_cross_mappings Job. Review-Status-Feld auf Edges. Human Review bleibt Option (approved/rejected), aber nicht Pflicht.

---

## 2026-02: 4-stufige Extraktion statt ein LLM-Call

**Decision:** extract_entities + extract_meanings + extract_relationships + extract_processes statt alles in einem Prompt.

**Rationale:** Verschiedene Wissensebenen (Fakten vs. Bedeutungen vs. Beziehungen vs. Prozesse) brauchen verschiedene Prompt-Strategien. Ein Call vermischt diese Level.

**Consequences:** 4x so viele LLM-Calls. Aber: Bessere Qualität, sauberere Daten, leichter debuggbar.

---

## 2026-02-16: Zwei-Gate-Filtering für Content-Akquise

**Decision:** Breit scrapen, dann zweistufig filtern statt strenge Keyword-Filter.

**Rationale:** Anna's Archive Scraping produziert ~85% Noise (z.B. "UX Design" bei Suche nach "human design"). Einfache Keyword-Filter sind zu aggressiv — Nischen-Themen wie "Projector Empowerment", "Pfeile", "Liebe im HD" fallen raus. Stattdessen: Gate 1 = leichtgewichtige LLM-Vorklassifikation auf Titel+Metadaten (vor Download), Gate 2 = volle Inhaltsklassifikation nach MinerU-Extraktion (im Worker).

**Consequences:** Kein manuelles Kuratieren nötig. Noise wird automatisch erkannt. Nischen-Themen kommen durch. Admin-Review-Queue für Grenzfälle (Confidence 0.3–0.6). Kein Stub im Produktivbetrieb.

---

## 2026-02-16: Clean Data Restart (keine alten HD-Daten übernehmen)

**Decision:** Bestehende hd_assets/hd_asset_chunks/hd_interpretations in Cloud-DB NICHT migrieren. Sauberer Neustart mit sys_*-Schema.

**Rationale:** Bisherige Daten: 85% Noise in Assets, alle Interpretations sind Stubs ("mvp_stub", system: "other"), Ingestion-Jobs nur noch failed extract_interpretations. 113 PDFs sind schnell neu prozessiert — und diesmal richtig (mit echtem LLM, ohne Noise, mit Pre-Filtering). Schema ändert sich komplett (hd_* → sys_*).

**Consequences:** Lokale DB: supabase:web:reset löscht alles. Cloud: manuell bereinigen. Kein Datenverlust (alles war Stub/Noise). Anna's Archive Pipeline mit verbessertem Filtering neu durchlaufen.

---

## 2026-02-16: Verarbeitung pro System, in Wellen

**Decision:** Systeme nacheinander verarbeiten (HD → Gene Keys → Astro → BaZi → ...), nicht alle gleichzeitig.

**Rationale:** Pro-System ermöglicht Qualitätsvalidierung, Noise-Erkennung und Pipeline-Tuning. Kein Bias-Risiko, da jedes System eigene Wissensbasis aufbaut und Cross-System-Mappings erst in P4 kommen.

**Consequences:** HD als erstes System (größtes Corpus, am besten validierbar). Erkenntnisse aus HD-Verarbeitung fließen in Pipeline-Optimierung für Folgesysteme.

---

## 2026-02-16: Clean Inner Compass statt hd_*-Patch

**Decision:** Frischen Makerkit-Stand pullen, dann sauberen Inner Compass Teil (Schema, Worker, Scripts) neu aufsetzen. Kein String-Replace auf 2400 Zeilen altem Worker.

**Rationale:** 10 Migrations → 1-2 saubere (sys_* + pgvector + neue Felder von Tag 1). Worker referenziert direkt sys_*. Kein Legacy-Code. Wissen/Patterns aus altem Worker werden übernommen, aber Code neu geschrieben.

**Consequences:** Alter Worker (hd_worker_mvp.py) bleibt als Referenz. Makerkit-Framework (Auth, Accounts, RLS, UI-Shell) bleibt wie es ist. Nur der projektspezifische Teil wird neu.

---

## 2026-02-16: Interpretation-zentrierter Ansatz statt NVIDIA-style Triple-Extraktion

**Decision:** Bedeutungs-Extraktion (15 Dimensionen pro Chunk, ~1000 Tokens) statt starre Triple-Extraktion (Subject-Predicate-Object per 512 Zeichen wie NVIDIA text2kg Playbook).

**Rationale:** NVIDIA text2kg ist NER+RE für faktische Domänen (News, Finance) mit festen Entity-Typen (ORG, PERSON) und 15 Relationsverben. Esoterische Texte brauchen Kontext für Bedeutung — 512-Zeichen-Chunks reißen das auseinander. Unsere Dimensions-Struktur (shadow, gift, archetype...) fängt mehr auf als flache Triples. Text2kg kommt danach deterministisch.

**Consequences:** Kein NVIDIA-Pipeline-Klon. Eigene Ontologie (Gate, Center, Stem, Archetype). Eigene Relationsverben (symbolisiert, korrespondiert_mit, aktiviert). Chunk-Größe bleibt ~1000 Tokens. Von NVIDIA übernehmen: Pipeline-Architektur, ggf. cuGraph für spätere Graph-Analytik, LoRA Fine-Tuning als Option.

---

## 2026-02-16: pgvector bestätigt als richtige Lösung

**Decision:** Postgres+pgvector für Embeddings und Cross-System-Mapping. Kein separater Vector-DB-Server.

**Rationale:** Supabase hat pgvector-Extension bereits. Für ~500-5000 Nodes mehr als ausreichend. Einziger Zweck: Cosine Similarity für Cross-System-Mapping-Kandidaten (Schicht D). Kein Pinecone/Weaviate/Qdrant nötig.

**Consequences:** `sys_kg_nodes.embedding vector(1536)` + ivfflat-Index kommt in Schema-Migration. text-embedding-3-large oder lokales Modell auf Spark.

---

## 2026-02: LLM-Wahl: Qwen3-32B als Default

**Decision:** Qwen3-32B als primäres Extraktions-/Synthesis-Modell auf Spark.

**Rationale:** Multilingual (100+ Sprachen), JSON/Structured Output, Apache-2.0 Lizenz, läuft bereits als NVFP4 auf Spark. BaZi-Quellen (Chinesisch) und Jyotish-Quellen (Sanskrit) profitieren von Mehrsprachigkeit.

**Consequences:** DeepSeek R1 8B als Alternative wenn Content zu stark gefiltert wird. A/B-Test mit 5-10 Chunks empfohlen bei Model-Wechsel. Model-Switcher erlaubt Wechsel ohne Code-Änderung.

---

## 2026-02: Deep Structure Seed = Backlog, nicht Sprint

**Decision:** Strukturvertiefung (832 → ~2000 Nodes) erfolgt demand-driven, nicht als Block vor S5.

**Rationale:** 832 Nodes (HD: 526, alle 10 Systeme) reichen vollständig für S5-Validierung. Wenn vor der Pipeline-Validierung 15-20h Daten kuratiert werden, blockiert das den kritischen Pfad. Falls S5 Contract-Anpassungen erfordert, müssten kuratierte Daten ggf. nochmal angefasst werden.

**Consequences:** S5 startet sofort mit bestehendem Graph. Fehlende Nodes werden erst nachgezogen wenn die Pipeline sie tatsächlich vermisst. Vollständiger Backlog in `reference/deep_structure_plan.md`. HD-Vertiefung (Crosses, PHS, Partners) nach S7 in P1.

---

## 2026-01: Schema hd_* → sys_* (Clean Restart)

**Decision:** EINE saubere Migration statt 10 Patches. 10 Tabellen mit sys_* Präfix.

**Rationale:** Kognitiver Overhead: hd_kg_nodes liest sich als "HD" statt "Meta-System". Technische Schuld: 10 Migrations-Dateien. pgvector von Anfang an.

**Consequences:** ~2-3 Tage Aufwand. Infra bleibt (Spark, Worker, MinerU). Nur Tabellennamen + neue Felder.
