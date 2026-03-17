# Glossary

<!-- Reality Block
last_update: 2026-02-16
status: stable
scope:
  summary: "Zentrale Begriffe (Repo-weit), um Terminologie stabil zu halten."
  in_scope:
    - core concepts
    - project-level terms
    - technical terms
  out_of_scope:
    - deep implementation details
notes: []
-->

## Repository-Begriffe

- **Projekt**: Produkt-/App-/Pipeline-Vorhaben unter `projects/`.
- **cursor/**: Lean-Docs die Cursor automatisch liest (< 300 Zeilen pro Datei).
- **reference/**: Mensch-Kontext (PRD, Entscheidungen, Ideen). KI liest nur bei Bedarf.
- **Rule (.mdc)**: Cursor-Konfigurationsdatei, automatisch geladen via globs/alwaysApply.
- **Scratch**: Rohe Notizen, Inbox, Legacy — keine Source of Truth.

## Infrastruktur-Begriffe

- **Spark**: Inferenz-/Infra-Server (GPU, Modelle, Container, Serving). Kein Repo, kein Cursor.
- **SGLang**: High-speed Runtime für interaktive Chat-/Agent-Workloads.
- **vLLM**: High-throughput Serving Engine (OpenAI-kompatibles API).
- **MinerU**: Open-Source PDF-Parsing (GPU-beschleunigt, heading-aware).
- **TP (Tensor Parallelism)**: Aufteilung eines Modells über mehrere GPUs.

## KI/ML-Begriffe

- **Agent**: (Semi-)autonomer Prozess mit LLM-Reasoning und Tools.
- **Pipeline**: Sequenz aus Agenten/Tools/Funktionen (Input → Output).
- **RAG**: Retrieval Augmented Generation — Abruf aus Wissensquellen + LLM.
- **Embeddings**: Textvektoren für Ähnlichkeitssuche (pgvector, cosine similarity).
- **Knowledge Graph (KG)**: Nodes + Edges in Postgres (sys_kg_nodes, sys_kg_edges).

## Inner Compass — Begriffe

- **Dimension**: Eine von 15 Bedeutungsachsen (shadow, gift, role, archetype, ...). Siehe contracts.md.
- **Lebensbereich**: Eine von 10 User-facing Kategorien (Selbst, Liebe, Beruf, ...). Siehe contracts.md.
- **Datenschicht (A-E)**: A=Rohmechanik, B=Bedeutungen, C=Dynamiken, D=Cross-System, E=Meta-Knoten.
- **Canonical ID**: Eindeutige Kennung im Format `{system}.{element_type}.{element_id}`.
- **System-Deskriptor**: JSON-Datei die Struktur und Metadaten eines Wissenssystems beschreibt.
- **Cross-System-Mapping**: Edge zwischen Elementen verschiedener Systeme (Schicht D).
- **Meta-Knoten**: Systemübergreifender Archetyp, emergent aus 3+ Mappings (Schicht E).
- **Mandala/Kompass**: Hauptvisualisierung — 10 Segmente × Dimensionsringe.
- **Staffel**: Release-Phase (Staffel 1: HD/BaZi/Astro/Maya, Staffel 2: Jyotish/GK/Numerologie).
- **Linse (Filter)**: User kann zwischen "Alle Systeme" und Einzelsystem-Ansicht wechseln.
