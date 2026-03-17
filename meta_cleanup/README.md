# ai_projects (Multi-Projekt Repository)

<!-- Reality Block
last_update: 2026-02-16
status: stable
scope:
  summary: "Repo-Root: Überblick, Struktur und harte Trennregeln."
  in_scope:
    - repository structure
    - separation rules
  out_of_scope:
    - project specs
    - infrastructure implementation
notes: []
-->

Entwicklungs- und Dokumentations-Basis für alle Projekte und Infrastruktur-Doku.

## Struktur

```
ai_projects/
├── projects/              ← Projekt-Dokumentation
│   ├── inner_compass/     ← Geburtsbasiertes Meta-System (Aktiv)
│   ├── trading_bot/       ← Trading Bot (Aktiv)
│   ├── rest_data_platform/← ReST Data Platform (Planung)
│   ├── [weitere]/         ← Siehe _meta/master_map.md
│   └── _meta/             ← Globale Konventionen, Glossar, Landkarte
│
├── infrastructure/        ← Infra-Doku (Spark, Proxmox, Tailscale, ...)
│
├── code/                  ← Separate Code-Repos (eigene Git-Repos)
│   ├── hd_saas_app/       ← Inner Compass Code (Makerkit + Supabase)
│   └── [weitere]/
│
├── scratch/               ← Inbox, Wissen, Legacy (keine Source of Truth)
│
└── .cursor/rules/         ← Cursor Rules (automatisch geladen)
```

## Trennregeln

- `projects/` beschreibt **was/warum/wie** (Specs, Architektur, Roadmap)
- `code/` enthält **ausführbaren Code** (je Projekt eigenes Git-Repo, via .gitignore ignoriert)
- `infrastructure/` beschreibt **wie betrieben** (Serving, VMs, Netzwerk)

## Cursor Workspace

Öffne `ai_projects.code-workspace` (Multi-Root) — damit sieht die KI Code + Docs + Infra zusammen.

## Git-Strategie

Dieses Root-Repo ist **Docs/Infra only**. Jedes Code-Repo unter `code/` ist ein eigenes Git-Repo.

## Einstiegspunkte

| Frage | Datei |
|-------|-------|
| Was gibt es für Projekte? | `projects/_meta/master_map.md` |
| Wie sind Docs organisiert? | `projects/_meta/doc_and_rules_strategy.md` |
| Was bedeutet Begriff X? | `projects/_meta/glossary.md` |
| Inner Compass Status? | `projects/inner_compass/cursor/status.md` |
| Spark/LLM-Infra? | `infrastructure/spark/` |
