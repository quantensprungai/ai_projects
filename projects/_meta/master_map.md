# Global Master Map

<!-- Reality Block
last_update: 2026-01-13
status: stable
scope:
  summary: "Globale Projektlandkarte inkl. Abhängigkeiten und Architektur-Ebenen."
  in_scope:
    - project list
    - cross-dependencies
    - architecture layers
    - risks and opportunities
  out_of_scope:
    - per-project implementation details
notes: []
-->

## Überblick

Dieses Repository bündelt mehrere Projekte in einer gemeinsamen “Landschaft”.

### Projekte

- **HD-SaaS** (`projects/hd_saas`)
- **Trading Bot** (`projects/trading_bot`)
- **IHK SaaS** (`projects/ihk_saas`)
- **Kiosk Agent** (`projects/kiosk_agent`)
- **Super Buddy** (`projects/super_buddy`)
- **Anna’s Archive Toolkit** (`projects/annas_archive_toolkit`)
- **Bot Platform (Clawdbot)** (`projects/bot_platform`)
- **AL Meta** (`projects/al_meta`)
- **AI 2027** (`projects/ai_2027`)
- **Spark Infrastructure (Doku/Stack)** (`infrastructure/spark`)

## Beziehungen (high level)

- Projekte nutzen **lokale Modelle + LLM Serving** (Spark) via definierte Endpoints.
- **Bot Platform** nutzt Spark als LLM‑Backend und steuert (im `ops` Profil) Infrastruktur/Worker‑Ops über allowlisted Tools.
- RAG / Agents / Pipelines werden pro Projekt beschrieben und später konsolidiert.

## Architektur-Ebenen (high level)

- **Layer 1 — Spark (LLM Serving)**: SGLang / vLLM als Inferenz-Backends (Docs im Repo, Ausführung auf Spark).
- **Layer 2 — Shared Data / RAG**: Embeddings, Vector Stores, Ingestion (projekt- oder plattformnah).
- **Layer 3 — Agents / Pipelines**: Tool‑Using Agents, Routing, Workflows.
- **Layer 4 — Applications**: Trading Bot, SaaS Apps, Assistants.

## Globale Risiken

- Kontext-/Terminologie‑Drift zwischen Projekten
- Duplizierte Spezifikationen/Logik
- Unklare Ownership von “shared components”

## Globale Chancen

- Wiederverwendbare Agent‑Patterns & RAG‑Pipelines
- Gemeinsame Infrastruktur/Serving‑Standards
- Konsistente Dokumentations- und Änderungsprozesse

## Prioritäten (Placeholder)

- P0: Infrastruktur‑Stabilität (Serving + Endpoints)
- P0: Eine saubere Projektlandkarte / Konventionen


