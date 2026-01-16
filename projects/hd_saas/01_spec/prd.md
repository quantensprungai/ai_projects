<!-- Reality Block
last_update: 2026-01-16
status: draft
scope:
  summary: "PRD für HD-SaaS (Content → Knowledge → Reading/Chat)."
  in_scope:
    - goals
    - target users
    - success metrics
  out_of_scope:
    - implementation plan
notes: []
-->

# PRD – HD‑SaaS

## Problem

HD‑Wissen ist verteilt über Bücher/Talks/Schulen, teils widersprüchlich, selten maschinenlesbar. Klassische Tools liefern statische Texte, aber kein robustes Verständnis von:
- **Abhängigkeiten/Interdependenzen**
- **Prozessen/Dynamiken** (Phasen, Fallen, Wege)
- **Kontext/Zeit** (Konditionierung, Lebensphase, Zyklen)

## Ziel

Ein System, das geburtsdatenbasierte Modelle (Start: Human Design) **als strukturierte Wissensbasis** verwaltet und daraus **kontextbezogene, nachvollziehbare** Antworten/Readings erzeugt.

## Zielgruppen

- **Builder/Research**: du (Ops/Dev), die Pipeline + Wissensmodell aufbauen
- **Power User**: Nutzer:innen, die Readings/Erklärungen wollen (später)
- **Admin/Curator**: Quellen pflegen, Ergebnisse prüfen, Versionen steuern

## In Scope (v1)

- **Content Library**: ingest von Collections (z. B. `assets.jsonl`) + Asset‑Browser
- **Interpretations‑Repository**: Extraktion/Strukturierung von Aussagen aus Text (chunked)
- **Knowledge Graph (KG)**: Nodes/Edges für HD‑Elemente + qualitative Relationen (z. B. `modulates`, `overrides`)
- **Dynamics Engine (minimal)**: Dynamics‑Objekte mit Phasen/Traps/Growth Paths für ausgewählte Themen (Start: Profile/Linien)
- **Synthesis**: kanonische Kurzbeschreibung pro Element aus Quellen ableiten (versioniert)
- **Query/Chat (MVP)**: Q&A über KG + Interpretationen (mit Quellenreferenzen)
- Anleitung/Automatisierung zur Beschaffung Inhalte

## Out of Scope (v1)

- Vollständige Multi‑System‑Integration (BaZi/Astro etc.) als Produktfeature (nur als Datenmodell‑Kompatibilität)
- Vollautomatische “Wahrheitsfindung” zwischen Schulen


## Erfolgsmessung

- **Qualität**: Stichproben zeigen nachvollziehbare Antworten mit Quellenlink (Chunk/Asset‑ID)
- **Konsistenz**: gleiche Frage + gleicher Kontext → gleiches Ergebnis (bis auf Sampling)
- **Durchsatz**: Pipeline kann eine Collection (z. B. 1–2k Assets) als Batch verarbeiten
- **Operabilität**: reproduzierbare Runs (Logs, Resume/Checkpoint)

## Input/Output Contract (MVP)

- **Input**: `assets.jsonl` (aus Anna’s Archive Toolkit) als primärer Ingest‑Contract.
- **Output**:
  - gespeicherte Assets/Chunks/Interpretationen (Supabase)
  - KG Nodes/Edges (Supabase, später ggf. Graph‑DB)
  - kanonische Texte + Dynamics‑Objekte (JSONB)


