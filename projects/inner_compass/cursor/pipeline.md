# Inner Compass — Pipeline & Jobs

> Alle Pipeline-Jobs, ihre Inputs/Outputs, Reihenfolge, Prompts.

## 1. Pipeline-Überblick

```
PDF → extract_text → chunk → classify_domain → extract_entities
                                              → extract_meanings
                                              → extract_relationships
                                              → extract_processes
                                              → text2kg
                                              → synthesize_node
                                              → [extract_cross_mappings]
                                              → [generate_meta_nodes]
```

Jobs in `[Klammern]` sind noch nicht implementiert.

## 2. Bestehende Jobs (funktionieren)

### extract_text
- **Input:** PDF in sys_sources (Storage-Referenz)
- **Engine:** MinerU (GPU auf Spark, heading-aware)
- **Output:** sys_source_chunks (saubere Textblöcke, ~500-1000 Tokens)
- **Status:** ✅ Produktiv

### classify_domain
- **Input:** sys_source_chunk
- **Engine:** LLM
- **Output:** system-Tag auf Chunk ('hd' | 'bazi' | 'astro' | ...)
- **Status:** ✅ Produktiv

### extract_term_mapping
- **Input:** sys_source_chunk + bestehende sys_kg_nodes (Seed-basiert)
- **Engine:** LLM
- **Output:** sys_term_mapping (canonical_id, term, language, school, synonyms)
- **Logik:** Erkennt Systemelemente im Text und normalisiert ("Kraft-Tor" = "Power Gate" = Gate 34 → hd.gate.34)
- **Status:** ✅ Produktiv

### extract_interpretations (wird aufgeteilt → extract_meanings)
- **Input:** sys_source_chunk + erkannte Entities
- **Engine:** LLM
- **Output:** sys_interpretations (Payload: essence, mechanics, expression, dimensions)
- **Vertrag:** Siehe contracts.md → Interpretations-Payload
- **Status:** ✅ Produktiv, aber Aufspaltung geplant (siehe Abschnitt 3)

### text2kg
- **Input:** sys_interpretations
- **Engine:** Deterministisch
- **Output:** sys_kg_nodes (Upsert per canonical_id)
- **Logik:** Interpretation → Node. Aktuell NUR Nodes, keine echten Edges.
- **Status:** ✅ Produktiv, aber Edges fehlen

### synthesize_node
- **Input:** Alle sys_interpretations für einen Node
- **Engine:** LLM
- **Output:** sys_kg_nodes.canonical_description + sys_synthesis_wordings (Styles)
- **Status:** ✅ Produktiv

## 3. Geplante Aufspaltung: extract_interpretations → 4 Jobs

Aktuell macht `extract_interpretations` alles in einem LLM-Prompt. Besser: 4 fokussierte Jobs.

### extract_entities (NEU)
- **Input:** sys_source_chunk
- **Prompt:** "Welche Systemelemente werden in diesem Text besprochen?"
- **Output:** Array von (system, element_type, element_id) — matched gegen existierende Nodes
- **Warum separat:** Fokussierter Prompt = bessere Entity-Erkennung

### extract_meanings (= Nachfolger von extract_interpretations)
- **Input:** sys_source_chunk + erkannte Entities
- **Prompt:** "Was sagt der Text über jedes identifizierte Element?"
- **Output:** sys_interpretations (Payload mit dimensions + process-Feld)
- **Warum separat:** Kann auf erkannte Entities fokussieren statt selbst erkennen zu müssen

### extract_relationships (NEU)
- **Input:** sys_source_chunk + erkannte Entities
- **Prompt:** "Welche Beziehungen zwischen Elementen werden beschrieben?"
- **Output:** sys_kg_edges (from, to, relation_type, evidence) — NUR intra_system
- **Warum separat:** Triples ≠ Interpretationen. Verschiedene Extraktionslogik.

### extract_processes (NEU)
- **Input:** sys_source_chunk
- **Prompt:** "Welche zeitlichen Prozesse, Zyklen, Fallen, Wachstumspfade werden beschrieben?"
- **Output:** sys_dynamics (dynamic_type, payload)
- **Warum separat:** Prozesse brauchen andere Erkennung als statische Bedeutungen.

## 4. Neue Jobs (noch nicht implementiert)

### extract_process_patterns (NEU, Priorität: hoch)
- **Input:** sys_source_chunks mit Interpretationen
- **Prompt:** "Suche nach: Fallen/Schatten (trap), Aktivierungswegen (gift_activation), konkreten Experimenten (experiment_seed)"
- **Output:** process-Feld im Interpretations-Payload
- **Abhängigkeit:** Erweiterer Contract (process-Feld muss existieren)

### extract_cross_mappings (NEU, Priorität: mittel)
- **Input:** Alle Nodes mit canonical_description + embedding (über Systeme hinweg)
- **Methode:**
  1. Cosine Similarity aller Embeddings zwischen Systemen
  2. Kandidaten (Similarity > 0.75) → LLM-Validierung
  3. LLM bewertet: "Ist hd.gate.34 thematisch verwandt mit bazi.stem.jia?"
- **Output:** sys_kg_edges (relation_type=maps_to, edge_scope=cross_system, review_status=candidate)
- **Review:** Human bestätigt/verwirft Kandidaten
- **Abhängigkeit:** pgvector + Embeddings müssen existieren

### generate_meta_nodes (NEU, Priorität: mittel)
- **Input:** Alle cross_system maps_to-Edges (approved)
- **Methode:**
  1. Graph-Clustering: Welche Nodes aus 3+ Systemen sind über maps_to verbunden?
  2. Pro Cluster: Meta-Knoten erzeugen
  3. LLM benennt: "Welcher universelle Archetyp verbindet diese Elemente?"
- **Output:** sys_kg_nodes (system=meta, node_type=meta_concept) + maps_to-Edges
- **Abhängigkeit:** extract_cross_mappings muss gelaufen sein

## 5. Embedding-Generierung

Kein eigenständiger Job, sondern Teil von synthesize_node:

```
synthesize_node (erweitert):
  1. Alle Interpretationen → canonical_description (LLM)
  2. canonical_description → embedding (text-embedding-3-large)
  3. embedding → sys_kg_nodes.embedding (pgvector)
  4. Synthesis Wordings erzeugen (natural, coaching, poetic, technical)
```

## 6. Strukturbaum-Seeding (Phase 0)

VOR der PDF-Verarbeitung: Deskriptoren → Graph-Struktur.

```python
# Pseudocode:
descriptor = load_json("system_descriptors/hd.json")

for center_id, data in descriptor["structure"]["centers"].items():
    upsert_node(node_key=f"hd.center.{center_id}", node_type="Center", system="hd")
    for gate_num in data["gates"]:
        upsert_node(node_key=f"hd.gate.{gate_num}", node_type="Gate", system="hd")
        upsert_edge(from="hd.gate.{gate_num}", to="hd.center.{center_id}", type="part_of")

for ch_id, ch_data in descriptor["structure"]["channels"].items():
    upsert_node(node_key=f"hd.channel.{ch_id}", node_type="Channel", system="hd")
    for gate in ch_data["gates"]:
        upsert_edge(from=f"hd.gate.{gate}", to=f"hd.channel.{ch_id}", type="part_of")
```

Der Graph existiert BEVOR die erste PDF verarbeitet wird.
PDFs REICHERN die Nodes AN (Interpretationen), sie ERZEUGEN sie nicht.

## 7. Worker-Architektur

- Python systemd-Services auf Spark
- Kommunikation via Supabase service_role (kein direkter DB-Zugriff)
- Job Queue: sys_ingestion_jobs (status: queued → processing → processed/failed)
- Retry: attempts-Feld, max 3 Versuche
- LLM-Zugriff: OpenAI-kompatible API (SGLang/vLLM auf Spark)
- Model-Switcher: Konfigurierbar pro Job-Typ

## 8. Content-Akquise: Zwei-Gate-Filtering

### Problem
Anna's Archive Scraping produziert ~85% Noise (z.B. "UX Design" bei Suche nach "human design").
Einfache Keyword-Filter sind zu aggressiv — Nischen-Themen (Projektoren, Pfeile, Liebe im HD) fallen raus.

### Gate 1 — LLM-Vorklassifikation (VOR Download)
- **Input:** Nur Titel + Autoren + Topic + Sprache (aus metadata.json)
- **Engine:** LLM (leichtgewichtig, wenige Tokens pro Eintrag)
- **Prompt:** "Ist dieses Buch relevant für [System]? relevant/irrelevant/unsicher + Confidence"
- **Output:** Nur relevant + unsicher → Download-Queue
- **Kosten:** Minimal (~7000 Einträge = wenige Cent)
- **Vorteil:** Fängt offensichtlichen Noise ("Interior Design", "UX Design"), lässt Nischen durch

### Gate 2 — Vollklassifikation (nach MinerU, im Worker)
- **Input:** Extrahierter Text (erste Chunks des Assets)
- **Engine:** classify_domain Job (voller LLM)
- **Output:** system-Tag + Confidence
- **Confidence < 0.3:** Status → `skipped_irrelevant` (keine weiteren Jobs)
- **Confidence 0.3–0.6:** Status → `needs_review` (Admin-Queue)
- **Confidence > 0.6:** Normal weiterverarbeiten

### Verarbeitungsreihenfolge: Pro System, in Wellen
1. HD (größtes Corpus, am besten validierbar)
2. Gene Keys / I Ching (eng verwandt)
3. Western Astro (gut strukturierte Literatur)
4. BaZi (chinesische Quellen, extra Validierung)
5. Jyotish, Akan, etc. (Nischen-Systeme)

Kein Bias-Risiko: Jedes System baut eigene Wissensbasis auf. Cross-System-Mappings kommen erst in P4.

## 9. Batch-Processing & LLM-Steuerung

### Stub vs. LLM
- **LLM aktiv:** Wenn `IC_LLM_URL` / `IC_LLM_SYNTHESIS_URL` gesetzt → LLM-Extraktion
- **Stub-Fallback:** NUR als expliziter `--dry-run`-Modus (Pipeline-Mechanik testen). NIE im Produktivbetrieb.
- **Model-Switcher:** LLM auf Spark ein-/ausschalten ohne Code-Änderung

### Zwei-Phasen-Betrieb (Ressourcen schonen)

| Phase | LLM | Worker-Filter | Was passiert |
|-------|-----|---------------|-------------|
| 1 — Text-Extraktion | AUS | `IC_WORKER_JOB_TYPES=extract_text` | Nur MinerU/OCR. Chunks werden geschrieben, Folge-Jobs gequeued. |
| 2 — Wissens-Extraktion | AN | Filter entfernen | classify, term_mapping, interpretations, text2kg, synthesis mit LLM. |

→ Vollständiger Ablauf: `reference/s5_runbook.md`

### LLM-Modell (aktuell)
- **Default:** Qwen3-32B (multilingual, JSON/Structured Output, Apache-2.0)
- **Alternative:** DeepSeek R1 8B (abliterated, weniger Filter)
- Model-Wechsel: `IC_LLM_URL` Port/Modell ändern

## 10. Neue Batch-Jobs (aus Gesamtinventur v0.5)

Ergänzen die bestehende Pipeline um IC-spezifische Extraktion. Alle laufen als Worker-Jobs auf Spark.

### tag_ic_metadata (Priorität: hoch)
- **Input:** sys_interpretations (bestehende)
- **Engine:** LLM
- **Prompt:** "Ordne diese Interpretation den IC-Prozess-Dimensionen zu: ic_step (1–9), ic_depth (1–4), ic_brunnen_layer (1–4), ic_leiter_stufe (1–5), ic_grammatik, ic_register."
- **Output:** `ic_tags`-Objekt im Interpretations-Payload (→ contracts.md §10)
- **Abhängigkeit:** contracts.md §10 muss im Worker implementiert sein
- **Wann:** Nach synthesize_node, vor Content-Delivery

### extract_pattern_traps (Priorität: hoch)
- **Input:** sys_interpretations aus 2+ Systemen × gleiche Domäne
- **Engine:** LLM + deterministische Kombinatorik
- **Methode:**
  1. Alle Interpretationen pro Domäne sammeln (system-übergreifend)
  2. Shadow-Dimensionen + Traps aus verschiedenen Systemen kreuzen
  3. LLM: "Welche kombinatorische Falle entsteht wenn [HD shadow] + [BaZi clash] + [EG fixierung] zusammentreffen?"
- **Output:** sys_dynamics (dynamic_type='trap', payload mit pattern_trap-Struktur)
- **Abhängigkeit:** Cross-System-Mappings (P4) verbessern die Qualität, aber erste Traps auch ohne möglich

### extract_reflexion_questions (Priorität: hoch)
- **Input:** sys_interpretations (pro Element)
- **Engine:** LLM
- **Prompt:** "Formuliere eine offene, einladende Reflexionsfrage für dieses Element. Ton: nicht direktiv, neugierig. Format: 'Was passiert wenn...?' / 'Wo in deinem Leben...?' / 'Wie fühlt sich ... an?'"
- **Output:** `ic_tags.ic_reflexion_frage` im Interpretations-Payload
- **Qualitätsregel:** Fragen folgen dem IC-Prinzip "Kein neuer Guru" (P1)

### extract_experiments (Priorität: mittel)
- **Input:** sys_interpretations × process.trap × process.gift_activation
- **Engine:** LLM
- **Prompt:** "Entwirf ein konkretes 7-Tage-Experiment für dieses Element. Format: Was tun? Wie beobachten? Woran merke ich etwas?"
- **Output:** `ic_tags.ic_experiment_seed` + erweitertes `process.experiment_seed`
- **Qualitätsregel:** Experimente sind Einladungen, keine Anweisungen (P1 + P4)

## 11. Echtzeit-Pipeline (NEU — nicht Batch)

Separate Services neben dem bestehenden Batch-Worker. Laufen als eigene Prozesse.

### Transit-Service
- **Was:** Berechnet aktuelle Planetenpositionen und leitet daraus aktive Tore/Aspekte ab
- **Engine:** pyswisseph (Echtzeit) → gleiche Logik wie Chart-Berechnung, aber für JETZT
- **Cache:** 15-Minuten-TTL (Planetenpositionen ändern sich langsam)
- **Output:** Aktive HD-Tore, aktive Astro-Aspekte, BaZi-Tages-/Monatspillar, Maya Wavespell-Tag
- **Wo:** JETZT-Space + ZEIT-Space
- **Technisch:** Python-Service auf Spark oder Edge Function auf Supabase

### Overlay-Service
- **Was:** Kombiniert statischen User-Chart × aktuelle Transite × KG-Interpretationen
- **Engine:** LLM (on-demand) oder Template-basiert (für häufige Kombinationen)
- **Input:** user_charts (statisch) + Transit-Service Output + sys_kg_nodes Lookup
- **Output:** Personalisierter Overlay-Text (→ XVI.1 in Gesamtinventur: 3 Text-Modi)
- **Beispiel:** "Die Sonne steht heute in Tor 41. Das aktiviert DEINEN Kanal 41-30 — das Thema Neuanfang ist für DICH gerade besonders lebendig."
- **Cache:** Pro User × Transit-Kombination, 1 Stunde TTL

### Konvergenz-Service
- **Was:** Erkennt wenn 3+ Systeme gleichzeitig auf dieselbe Domäne zeigen
- **Engine:** Deterministisch (Cross-System-Edges + aktive Transite + User-Chart)
- **Methode:**
  1. Aktive Chart-Elemente des Users → KG-Lookup → life_domain Tags
  2. Aktive Transite → KG-Lookup → life_domain Tags
  3. Zählen: Welche Domäne hat 3+ aktive Elemente aus verschiedenen Systemen?
- **Output:** Top 1–3 Konvergenz-Highlights für JETZT-Space
- **Cache:** Pro User, 15 Min TTL (an Transit-Service gekoppelt)

## 12. NLP-Pipeline (NEU — ab v2)

### Narrativ-Analyse
- **Trigger:** User beantwortet offene Frage (Onboarding oder Reflexion)
- **Input:** Freitext (1–5 Sätze)
- **Engine:** LLM
- **Output:**
  - EG-Cluster-Hypothese (Bauch/Kopf/Herz + Subtyp-Tendenz)
  - Aktuelle Phase-Schätzung (1–7)
  - Emotionaler Zustand (reguliert / aktiviert / erstarrt)
  - Thematische Domäne (welcher Lebensbereich steht im Fokus)
- **Ziel:** Ergänzt Chart-basierte Ableitung, validiert oder korrigiert EG-Bridge

### Stimmen-Erkennung (v3)
- **Trigger:** User schreibt Reflexionstext in WERKSTATT
- **Input:** Freitext (fortlaufend)
- **Engine:** LLM
- **Output:** "Welcher innere Teil spricht gerade?" (Kritiker, Macher, Kind, Helfer, ...)
- **Feedback:** Sanfte Benennung im UI ("Du schreibst gerade sehr streng über dich. Kennst du diese Stimme?")
