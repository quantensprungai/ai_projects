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
│   ├── rest_data_platform/← ASTRA WP 5.2 ReST / IMC-Doku (Code: quantensprungai/astra-imc-platform)
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

### Setup auf neuem Rechner (Clone + Code-Repos)

1. **Gesamt-Repo klonen**
   ```bash
   git clone https://github.com/quantensprungai/ai_projects.git
   cd ai_projects
   ```
   Oder per SSH (wenn SSH-Key bei GitHub hinterlegt):  
   `git clone git@github.com:quantensprungai/ai_projects.git`  
   Danach hast du Docs + Infra; der Ordner `code/` ist leer.

2. **Code-Repos separat klonen** (in `code/`):
   ```bash
   cd code
   git clone git@github.com:quantensprungai/hd-saas-app.git hd_saas_app
   git clone git@github.com:quantensprungai/annas-archive-toolkit.git annas-archive-toolkit
   # optional: git clone <url> trading-bot
   ```
   Ohne SSH: URLs mit `https://github.com/quantensprungai/...` nutzen; Zugriff dann über Git Credential Manager / Token.  
   **SSH einrichten:** Key erzeugen (`ssh-keygen -t ed25519 -C "github"`), öffentlichen Key unter https://github.com/settings/ssh/new eintragen.

3. **Workspace:** `ai_projects.code-workspace` öffnen (Multi-Root) — dann siehst du Docs + Infra + Code zusammen.

## Einstiegspunkte

| Frage | Datei |
|-------|-------|
| Was gibt es für Projekte? | `projects/_meta/master_map.md` |
| Wie sind Docs organisiert? | `projects/_meta/doc_and_rules_strategy.md` |
| Was bedeutet Begriff X? | `projects/_meta/glossary.md` |
| Inner Compass Status? | `projects/inner_compass/cursor/status.md` |
| Spark/LLM-Infra? | `infrastructure/spark/` |
