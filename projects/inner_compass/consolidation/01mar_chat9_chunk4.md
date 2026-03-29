# IC Extraktion — Chat 9, Chunk 4/4: Projektplan + Meta-Analysis Review + Grüne Wiese

> **Chunk-Scope:** IC_Projektplan v0.1, System-Taxonomie v0.1, Meta-System-Analysis Review (was gut/veraltet aus Feb-13-Dokument), Phase-0-Architektur-Entscheidungen, 4 unveränderliche Kernprinzipien
> **Kürzel:** WL9

---

## SCHICHT A — SUBSTANZ

---

### A-WL9-28: Gesamtprojektplan v0.1 — 3 Phasen definiert
**Inhalt:** Phase 0 (aktuell): Architektur — Taxonomie, Coverage-Matrix, KG-Schema, Projektplan. BEVOR erste Quellen gesammelt werden. Phase 1: HD-Kern + Ur-Systeme — alle 64 Gates belegt, Ra-Kanon + IHDS + Sekundärautoren, I Ching + Kabbala + Chakra als eigene Äste, erste Cross-System-Edges (HD.Gate↔IChg.Hexagram), erster RAG-Test. Qualitätskriterium: Jedes Gate hat 3+ Interpretationen + I Ching Ursprung + 1 Gene Keys Referenz. Phase 2: Gene Keys, BaZi, Cross-System-Matching-Algorithmus, erste Meta-Nodes, Themen-Layer. Phase 3: Jyotish, Enneagram, vollständige Themen-Coverage, API + LLM-Synthese, neue systemfreie Sprache.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** IMPLEMENTIERT (als IC_Projektplan_v01.md)
**Ziel-Bereich:** IC_Projektplan
**Herkunft:** ARTEFAKT

---

### A-WL9-29: System-Taxonomie v0.1 — 9 Systeme mit Typ/Klassen/Schichten
**Inhalt:** JSON mit 9 Systemen: Ur-Systeme (iching, kabbalah, chakra, astrology_western), Synthese-Systeme (hd, gene_keys), Parallel-Systeme (bazi, jyotish, enneagram). Pro System: system_id, label, type (ur/synthesis/parallel), node_classes (mit count), historical_layers (mit layer_id, era, label, language), schools. HD hat 14 node_classes (type→incarnation_cross), 11 thematic_layers, 5 schools. I Ching hat 5 node_classes, 6 historical_layers (L1=~1200 BCE → L6=Gene Keys 1999).
**Tag(s):** [SCHEMA]
**Reifegrad:** IMPLEMENTIERT (als system_taxonomy_v01.json)
**Ziel-Bereich:** KG-Schema, Coverage-Matrix
**Herkunft:** ARTEFAKT

---

### A-WL9-30: Coverage-Matrix v0.1 — 21 Seed-Zeilen, Ziel >800
**Inhalt:** CSV mit Spalten: node_id, system, node_class, example_element, cov_definition, cov_keywords, cov_shadow_challenge, cov_topic_partnership/parenting/career/health/timing/spirituality/psychology, sources_count, source_ids, schools_represented, historical_layers_count, oldest_source_era, cross_system_refs, gaps_noted, priority, status. 21 Seed-Zeilen (HD types/authorities/centers/gates/channels/profile_lines + I Ching hexagramme + Kabbala sephiroth + Chakra + BaZi). Alle status="empty". Wird über Open-Source-Kit-Extraktion auf >800 Zeilen erweitert.
**Tag(s):** [SCHEMA]
**Reifegrad:** IMPLEMENTIERT (als coverage_matrix_v01.csv)
**Ziel-Bereich:** Vollständigkeitsprüfung, Quellensteuerung
**Herkunft:** ARTEFAKT

---

### A-WL9-31: Meta-System-Analysis Review — was weiterhin gilt
**Inhalt:** Aus dem Feb-13-Dokument (3 Teile, ~45 Seiten) bleiben gültig: (1) Strukturbaum VOR PDF-Extraktion. (2) 4 Extraktionsebenen statt Monolith-Prompt (entities/meanings/relationships/processes). (3) Embeddings fundamental (pgvector, kein ArangoDB). (4) Cross-System-Mapping via Embeddings+LLM (kein manuelles Kuratieren). (5) Meta-Knoten emergent aus Clustering. (6) Schema-as-you-go mit jsonb. (7) Triple-Extraktion adaptiert von NVIDIA txt2kg. (8) Engine vs. KG Trennung (Engine=Berechnung, KG=Wissen).
**Tag(s):** [EVALUATION]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** IC_Projektplan, cursor/architecture.md
**Herkunft:** CHAT

---

### A-WL9-32: Meta-System-Analysis Review — was veraltet/falsch ist
**Inhalt:** (1) hd_-Prefix überall → muss system-agnostisch werden (kg_nodes statt hd_kg_nodes). (2) Ur-Systeme fehlen komplett als eigenständige Entitäten. (3) Historische Schichten fehlen als Dimension. (4) Staffel-Logik war Produkt-first statt System-first. (5) Dimensions-Keys (12+3=15) wurden zu früh finalisiert — erst nach Clustering möglich. (6) Gene Keys als "Berechnungsderivat" unterbewertet — ist eigenständige Ontologie (Shadow/Gift/Siddhi-Layer). (7) Maya Tzolkin in Staffel 1 wegen "viral" statt nach Ontologie-Tiefe. (8) Coverage-Matrix fehlte — Vollständigkeit nicht messbar.
**Tag(s):** [EVALUATION]
**Reifegrad:** ARGUMENTATION
**Beziehung:** SUPERSEDES Teile des Meta-System-Analysis Feb-13
**Ziel-Bereich:** IC_Projektplan
**Herkunft:** CHAT

---

### A-WL9-33: 4 unveränderliche Kernprinzipien des KG-Aufbaus
**Inhalt:** Diese 4 gelten in beiden Versionen (Feb 13 + aktuell) und bilden die Basis: (1) STRUKTUR vor BEDEUTUNG — Deskriptor-Seeding dann PDF-Extraktion. (2) SYSTEM-INTERN vor CROSS-SYSTEM — Intra-System-Edges vollständig dann maps_to. (3) EMERGENZ vor DEFINITION — Meta-Knoten entstehen aus Daten nicht vorab gesetzt. (4) SCHICHT vor MITTELUNG — Widersprüche zwischen Quellen sind Daten nicht weggemittelt.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** IC_Projektplan, IC_Gesamtwerk
**Herkunft:** CHAT

---

### A-WL9-34: Grüne-Wiese-Perspektive — Taxonomie VOR Quellensammlung
**Inhalt:** "Wenn ich von vorne anfangen würde": Phase 0 = system_taxonomy.json (was gibt es, welche Typen, welche Schulen, welche historischen Schichten). Phase 1 = coverage_matrix (alle Knoten-Typen × Themen-Dimensionen, bereit zum Befüllen). Erst wenn beide existieren, weiß man präzise welche Quellen man braucht — und für welchen Zweck. Nicht: "Welche Bücher gibt es?" → dann schauen was drin ist. Sondern: "Welche Lücken hat die Matrix?" → dann gezielt suchen.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** IC_Projektplan Phase 0
**Herkunft:** CHAT

---

### A-WL9-35: System-Typen bestimmen Quellen-Strategie
**Inhalt:** 3 fundamentale System-Typen was die Quellenlage angeht: Typ A (Autor-zentriert): HD, Gene Keys, Quantum HD — Suche via Autoren-Name. Typ B (Schul-zentriert): BaZi (viele Schulen, wenige Hauptautoren) — Suche via Schulname + Lehrer. Typ C (Tradition-zentriert): Jyotish, I Ching, Kabbalah (altes Wissen, Kommentatoren) — Suche via Textname + Kommentator. Für jeden Typ andere Recherche-Logik, anderes Entity-Registry-Template.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** entity_registry pro System
**Herkunft:** CHAT

---

### A-WL9-36: Sprachunabhängigkeit des KG bestätigt — jede Quellsprache gleichwertig
**Inhalt:** MinerU parst jede Sprache (Layout-erhaltend). LLM extrahiert → IMMER auf Englisch → sprachneutraler KG. Chinesische BaZi-Klassiker, deutschsprachige Ra-Materialien, russische Übersetzungen, Sanskrit-Jyotish — alle landen als englische Interpretationen im gleichen Schema. Die Sprache der Quelle ist vollständig irrelevant für den KG. Nur die Sprachkompetenz des LLMs zählt (DE/EN/ZH/FR = zuverlässig, Sanskrit/altes Hebräisch = braucht Zwischenschritt).
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** cursor/pipeline.md
**Herkunft:** CHAT

---

## SCHICHT E — SYNTHESE-ÜBERSCHUSS (Artefakte)

### E-WL9-01: system_taxonomy_v01.json (16 KB)
**Typ:** JSON-Schema mit 9 Systemen, node_classes, historical_layers, schools
**Qualität:** WERTVOLL — erstes vollständiges Systemregister
**Im Ist-Stand?:** JA — als Datei erzeugt

### E-WL9-02: coverage_matrix_v01.csv (2 KB)
**Typ:** CSV mit 21 Seed-Zeilen, 23 Spalten
**Qualität:** WERTVOLL — Scaffold für Vollständigkeitsprüfung
**Im Ist-Stand?:** JA — als Datei erzeugt

### E-WL9-03: IC_Projektplan_v01.md (11 KB)
**Typ:** Gesamtprojektplan mit 10 Sektionen
**Qualität:** WERTVOLL — erste Gesamtbeschreibung was wir machen und warum
**Im Ist-Stand?:** JA — als Datei erzeugt

### E-WL9-04: entity_registry_hd_v01.json (6 KB)
**Typ:** JSON mit 8 Autoren-Einträgen als Seed
**Qualität:** WERTVOLL — Grundlage für Entity-first Quellenakquise
**Im Ist-Stand?:** JA — als Datei erzeugt

### E-WL9-05: HD_Werklandschaft Sessions 1–5 (5 MD-Dateien, ~95 KB gesamt)
**Typ:** Kumulatives Recherche-Dokument
**Qualität:** WERTVOLL — vollständigste HD-Bibliografie die existiert
**Im Ist-Stand?:** JA — als MD-Dateien erzeugt

---

## ZUSAMMENFASSUNG CHUNK 4

| Schicht | Einträge |
|---------|----------|
| A — Substanz | 9 |
| E — Synthese-Überschuss | 5 |
| **Gesamt** | **14** |

**Top-3 Erkenntnisse:**
1. **Taxonomie VOR Quellensammlung** (A-34) — das Grüne-Wiese-Prinzip: Erst wissen was existiert, dann gezielt suchen. Umkehrung der bisherigen Logik.
2. **4 unveränderliche Kernprinzipien** (A-33) — Struktur vor Bedeutung, System-intern vor Cross-System, Emergenz vor Definition, Schicht vor Mittelung. Gelten in allen Versionen der Architektur.
3. **Meta-System-Analysis Feb-13 Review** (A-31/32) — 8 Dinge die weiterhin gelten, 8 Dinge die veraltet sind. Das alte Dokument bleibt als "Infrastruktur-Referenz" gültig, ist aber "veraltet bezüglich Systemarchitektur."
