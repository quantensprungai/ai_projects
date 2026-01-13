# Rules (global)

<!-- Reality Block
last_update: 2026-01-13
status: stable
scope:
  summary: "Repo-Regeln für Struktur, KI-Änderungen, Linking und Versionierung."
  in_scope:
    - structure rules
    - AI change constraints
    - cross-file linking rules
    - versioning conventions
  out_of_scope:
    - per-project implementation details
notes: []
-->

## Struktur-Regeln

- **Repo Root** ist `ai_projects/`
- **Projekte** liegen unter `projects/`
- **Infrastruktur-Doku** liegt unter `infrastructure/`
- **Code-Repositories** liegen unter `code/` (je Repo eigenes Git)
- **Spark-Dokumentation** liegt unter `infrastructure/spark/` (nur definierte Dateien)

## Doku ↔ Code ↔ Infra (Verlinkungs-Regel)

- **`projects/<name>/`** beschreibt *was/warum/wie* (PRD, Specs, Architektur, Roadmap).
- **`code/<repo>/`** enthält den ausführbaren Code (*wie genau implementiert*).
- **`infrastructure/`** beschreibt Laufzeit/Stack (VMs, Ports, Backups, Serving).

Konvention:
- Jedes Projekt in `projects/<name>/README.md` verlinkt auf sein Code‑Repo unter `code/<repo>/` (falls vorhanden).
- Jedes Code‑Repo enthält eine kurze “Docs live here” Sektion mit Links auf:
  - `../../projects/<name>/` (kanonische Doku)
  - relevante `../../infrastructure/...` Dateien (Runtime/Ports)

## Inhaltliche Konventionen

- Jede Datei startet mit einem klaren Zweck (1–3 Sätze).
- Entscheidungen werden als “Decision / Rationale / Consequences” dokumentiert.
- Links immer relativ im Repo (`../`), keine absoluten Pfade.

## KI-Änderungsregeln (Reality Blocks)

- Jede Markdown-Datei enthält einen Reality‑Block (HTML Kommentar) **direkt unter dem Titel**.
- KI ändert nur Inhalte, die im Reality‑Block unter `in_scope` liegen.
- Bei größeren Änderungen: `last_update` aktualisieren und relevante Querverweise pflegen.

## Git-Strategie (Multi-Repo)

- **Root Repo (`ai_projects/`)**: Docs/Infra/Meta (dieses Repository).
  - Enthält: `projects/`, `infrastructure/`, Root-`README.md`, Meta-Dateien.
  - Ignoriert: `code/` (Code-Repos werden **nicht** im Root committed).
- **Code-Repos (`code/<repo>/`)**: pro Projekt ein eigenes Git-Repo (eigener Remote, eigener Release-Zyklus).

Konsequenzen:
- Du kannst in Cursor entweder den **gesamten Workspace** öffnen (Kontext) oder **nur ein Code-Repo** als Workspace (fokussiert), ohne dass Git “alles” mischt.
- Optional (wenn du im Root definierte Code-Versionen referenzieren willst): **Git Submodules** für `code/<repo>/`.


