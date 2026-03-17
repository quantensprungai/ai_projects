# Inner Compass — Status & Nächste Schritte

> **Stand:** 2026-02-16 (S1-S4 erledigt) | Bei jedem Meilenstein aktualisieren!

## Was EXISTIERT und FUNKTIONIERT

### Infrastruktur ✅
- Makerkit-App (Next.js + Supabase): Auth, Accounts, UI-Shell
- Spark GPU-Server: MinerU (PDF-Parsing), SGLang/vLLM (LLM-Inferenz)
- Tailscale VPN: Spark ↔ Supabase ↔ Dev
- System-Deskriptoren: 10 JSON-Dateien (HD, BaZi, Astro, Jyotish, Maya, Gene Keys, Enneagram, Numerology, Nine Star Ki, Akan)

### Alter HD-Worker (Referenz, wird neu geschrieben)
- hd_worker_mvp.py (~2400 Zeilen) — Pipeline funktioniert end-to-end für HD
- 10 Custom-Migrations mit hd_*-Präfix — werden durch 1-2 saubere sys_*-Migrations ersetzt
- Patterns/Logik werden übernommen, Code wird neu geschrieben

### Content-Akquise (Anna's Archive Toolkit)
- Pipeline-Architektur: Solide (Topics → Scraping → metadata.json → assets.jsonl → Download → Upload)
- Datenqualität: ~85% Noise bei HD-Keywords (Lösung: Zwei-Gate-Filtering, siehe pipeline.md §8)
- hd_saas_uploader.py: `--sys-mode` für PDF-Upload (sys_sources, sys_ingestion_jobs, sys_uploads_raw) — S5 nutzbar
- Bestehende DB-Daten: Nur Stubs, werden NICHT migriert (Clean Data Restart)
- assets.jsonl in scratch/: Falsch platziert, werden bei Clean Restart neu generiert

## Nächste Schritte (Clean Inner Compass Setup)

### S1 — Makerkit Pull (frischer Stand) ✅
- [x] Upstream-Updates: Makerkit v2.23.14 + MCP Server 2.0 (10 Commits, 1 Konflikt in .gitignore gelöst)
- [x] Alte hd_*-Migrations + Worker als Referenz behalten
- [x] Pipeline-Analyse: Anna's Archive → Zwei-Gate-Filtering dokumentiert
- [x] Daten-Entscheidung: Clean Data Restart (keine alten Stubs/Noise migrieren)
- → Erledigt: 2026-02-16

### S2 — Saubere Schema-Migration (sys_* + pgvector von Tag 1) ✅
- [x] 1 Migration: `20260216150000_inner_compass_core.sql` (11 Tabellen)
- [x] pgvector Extension + Embedding-Spalte (vector(1536)) auf sys_kg_nodes
- [x] system + canonical_id auf sys_kg_nodes (Multi-System)
- [x] edge_scope + review_status auf sys_kg_edges
- [x] sys_sources konsolidiert hd_assets + hd_documents + hd_document_files
- [x] RLS-Policies (authenticated + service_role) auf allen Tabellen
- [x] Storage Bucket: sys_uploads_raw (mit RLS + service_role)
- [x] Helper-Schema: ic (inner compass) statt hd
- [x] Job-Queue-Index (status + job_type + created_at WHERE queued)
- [x] 10 alte hd_*-Migrationen → 99_archive_hd/
- → Erledigt: 2026-02-16
- → Nächster Schritt: supabase:web:reset + typegen zum Testen

### S3 — Neuer Worker (sys_*-nativ) ✅
- [x] ic_worker.py (~650 Zeilen) — vollständig sys_*-nativ, alle 6 Job-Typen
- [x] Job Queue Polling mit Prioritäts-Reihenfolge
- [x] extract_text: MinerU (heading-aware) + PyMuPDF Fallback
- [x] classify_domain: Keyword-Heuristik, alle 9 Systeme, Auto-Skip bei confidence < 0.3
- [x] extract_term_mapping: Seed-Rows für HD, BaZi, Astro, Jyotish
- [x] extract_interpretations: 15 Dimensions, process-Feld, life_domain
- [x] text2kg: Interpretations → KG Nodes (Upsert per node_key)
- [x] synthesize_node: Canonical description + 4 Wording-Styles
- [x] --dry-run Modus (expliziter Stub, kein Stub im Produktivbetrieb)
- [x] Retry-Logik: IC_MAX_ATTEMPTS (default 3), auto re-queue bei Fehler
- [x] LLM JSON-Parsing: <think>-Removal, Markdown-Strip, Balanced-Braces
- [x] Env-Vars: IC_* statt HD_* (IC_LLM_URL, IC_USE_MINERU, etc.)
- → Erledigt: 2026-02-16

### S3.5 — Lokaler Smoke-Test (vor S4) ✅
- [x] Supabase start (--ignore-health-check wegen Storage-Timing auf Windows)
- [x] Schema: 11 sys_*-Tabellen korrekt erstellt
- [x] pgvector 0.8.0 aktiv, embedding-Spalte (vector) auf sys_kg_nodes
- [x] Storage Bucket: sys_uploads_raw (private) vorhanden
- [x] Seed: 3 term_mapping + 1 interaction + 1 wording korrekt eingefügt
- [x] TypeScript-Typen generiert (packages + app)
- [x] Worker dry-run: "No queued jobs" — verbindet, pollt, beendet sauber
- [x] Fix: leere Phantom-Migration gelöscht, seed.sql hd_* → sys_* aktualisiert, analytics deaktiviert (Windows)
- → Erledigt: 2026-02-16
- → Hinweis: `supabase start` auf Windows benötigt `--ignore-health-check` (npx supabase start --ignore-health-check)

### S4 — Seed-Script + Strukturbäume ✅
- [x] ic_seed_structure.py (~530 Zeilen) — lädt Deskriptoren, seeded Strukturgraph
- [x] 10 Systeme → sys_systems (inkl. vollständiger Deskriptor als JSONB)
- [x] 832 Nodes → sys_kg_nodes (HD: 526, GK: 64, Jyotish: 60, Astro: 39, Maya: 38, BaZi: 37, Num: 28, Akan: 14, NSK: 14, Enn: 12)
- [x] 698 Edges → sys_kg_edges (part_of, maps_to, rules, produces, controls, integrates_to, disintegrates_to)
- [x] HD komplett: 9 Centers, 64 Gates, 384 Lines, 36 Channels, 12 Profiles, 7 Authorities, 5 Types, 5 Definitions, 4 Circuits
- [x] Cross-System: 64 Gene Keys → HD Gates (maps_to)
- [x] Idempotent (merge-duplicates): wiederholbar ohne Duplikate
- → Erledigt: 2026-02-16

### S5 — Validierung: HD end-to-end durch neue Pipeline ← NÄCHSTER SCHRITT
- [x] PDF-Upload (VM102 → sys_uploads_raw, sys_sources, sys_ingestion_jobs)
- [ ] extract_text (MinerU) → classify_domain → extract_interpretations → text2kg → synthesize_node
- [ ] Ergebnisse prüfen: Landen Interpretationen korrekt auf sys_kg_nodes? Matchen die canonical_ids?
- [ ] Vergleich mit altem Worker (falls Referenzdaten vorhanden)
- [ ] Bei Bedarf: Fehlende Struktur-Nodes demand-driven nachziehen (z.B. Line-Keynotes, PHS-Nodes)
- → Voraussetzung: Spark GPU-Server (MinerU + LLM, nacheinander wegen GPU-Sharing)
- → Runbook: `reference/s5_runbook.md` (Zwei-Phasen: Phase 1 MinerU, Phase 2 LLM)
- → Geschätzt: 1 Tag

### S6 — Anna's Archive Pipeline (sys_*-Update)
- [x] hd_saas_uploader.py: `--sys-mode` für PDF-Upload (sys_sources, sys_ingestion_jobs, sys_uploads_raw)
- [ ] Gate 1: LLM-Vorklassifikation auf Titel+Metadaten (neues Script classify_assets.py in annas-archive-toolkit)
- [ ] Metadata-Collection: Topics auf VM102 mit richtigen Topics durchlaufen (HD, BaZi, Astro, Jyotish, Akan)
- [ ] Download: Relevante PDFs (nach Gate 1) herunterladen
- [ ] Upload: Gefilterte PDFs + assets.jsonl über aktualisierten Uploader nach Supabase (sys_*)
- → Geschätzt: 1-2 Tage
- → Kann teilweise parallel zu S5 laufen (Metadata-Collection + Download auf VM102 unabhängig)

### S7 — Cloud-Deployment
- [ ] Cloud-Supabase: Neues Projekt ODER bestehende DB bereinigen + neue Migration anwenden
- [ ] Worker auf Spark: ic_worker.py deployen (systemd Service, IC_* Env-Vars)
- [ ] E2E-Test: Upload → Worker → KG Nodes in Cloud-DB
- → Geschätzt: 0.5-1 Tag

### Danach

### Deep Structure — Demand-Driven (kein Block!)
- Strukturvertiefung passiert WENN die Pipeline Nodes vermisst, nicht vorab
- HD zuerst (bei S5-Validierung), andere Systeme wenn ihre PDFs verarbeitet werden
- Vollständiger Backlog: `reference/deep_structure_plan.md`
- Trigger-Beispiele:
  - Worker findet "Incarnation Cross of Planning" in PDF aber kein Node → Crosses nachseedeen
  - PHS-Thema in PDF, kein Color-Node → 17 PHS-Nodes hinzufügen
  - BaZi-PDFs in P2 → Jiazi, Hidden Stems, Branch-Interaktionen nachziehen

### P1 — HD-Vertiefung + Staffel-1-Systeme (nach S7)
- [ ] HD Deep Structure nachziehen (Crosses, PHS, Partners — was bei S5 gefehlt hat)
- [ ] BaZi: Deep Structure + 10+ PDFs
- [ ] Westl. Astrologie: Deep Structure + 10+ PDFs
- [ ] Maya: Deep Structure + 5+ PDFs + Dreamspell-Daten
- [ ] Validierung: Funktioniert der erweiterte Contract für alle 4?
- → Geschätzt: 2-4 Wochen

### P3 — Chart-Engines integrieren
- [ ] HD: hdkit (JS) oder SharpAstrology
- [ ] BaZi: alvamind (TS/npm) oder bazica (Go)
- [ ] Astro: pyswisseph + immanuel-python
- [ ] Maya: tzolkin-calendar (Python)
- → Details: engines.md

### P4 — Cross-System-Infrastruktur
- [ ] Embeddings generieren (text-embedding-3-large oder lokal)
- [ ] 50 manuelle Cross-System-Mappings als Startpunkt
- [ ] extract_cross_mappings Job (Embedding-Similarity + LLM-Validierung)
- [ ] generate_meta_nodes Job (Clustering + LLM-Benennung)
- [ ] Review-Workflow für Mapping-Kandidaten
- → Geschätzt: 2-4 Wochen

### P5 — App + Visualisierung
- [ ] Mandala/Kompass-Visualisierung (10 Segmente, Kern-Dimensionen als Ringe)
- [ ] Handbuch-Generator (4 Tiefenschichten pro Lebensbereich)
- [ ] System-Filter (Linsen-Umschalter)
- [ ] Zeitlinie (dynamische Aktualisierung)
- [ ] Chat/Voice Agent mit RAG auf KG
- [ ] Fluss-Diagramm (Phase 2-3, braucht Schicht D)

## Entscheidungs-Log (Kurzform)

Vollständig: `reference/decisions.md`

| Datum | Entscheidung | Begründung |
|-------|-------------|------------|
| 2026-02 | 15 statt 12 Dimensionen | +elemental_quality, temporal_phase, destiny_pattern für Multi-System |
| 2026-02 | 10 statt 8 Lebensbereiche | Sexualität ≠ Partnerschaft, Community ≠ Familie |
| 2026-02 | Mandala statt Radar-Chart | Einzigartige Signatur, SM-teilbar, kein Bewertungscharakter |
| 2026-02 | Keine Entwicklungsstufen (anti-AQAL) | Systeme beschreiben Qualitäten, nicht Hierarchien |
| 2026-02 | Drei Sprachebenen (System/Meta/Handbuch) | Copyright + Verständlichkeit + Synthese |
| 2026-02 | Postgres+pgvector statt ArangoDB | Supabase-Ökosystem, kein separater Graph-DB-Server |
| 2026-02 | Strukturbäume aus Deskriptoren, nicht PDFs | Struktur ist deterministisch, PDFs liefern nur Interpretationen |
| 2026-02 | Deep Structure = Backlog, nicht Sprint | 832 Nodes reichen für S5; Pipeline validieren VOR Daten-Kuration |
