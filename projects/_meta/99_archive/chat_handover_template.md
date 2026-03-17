> **ARCHIVIERT** (2026-02-16). Inhalt wurde in Cursor Rules (.cursor/rules/) oder doc_and_rules_strategy.md überführt.

<!-- Reality Block
last_update: 2026-02-07
status: draft
scope:
  summary: "Wiederverwendbare Chat-Handover-Schablone für dieses Multi-Projekt-Repo: global + pro Projekt + optional pro Thema."
  in_scope:
    - what to paste when switching chats
    - doc structure to avoid bloat
  out_of_scope:
    - project-specific specs (die liegen in den jeweiligen Projektdossiers)
notes: []
-->

# Chat Handover – Schablone (Multi‑Projekt)

Ziel: Beim Chatwechsel **schnell auf 80% Kontext** kommen, ohne Doku zu duplizieren oder aufzublähen.

## Prinzip (damit die Doku nicht explodiert)

- **Ein Global-Handover** (dieses Template) + **ein Per‑Projekt „Current Status“** als Single Source of Truth.
- **Themen-/Incident-Handover nur dann**, wenn ein Thema operative Handgriffe/Runbooks braucht (z. B. Spark Worker, Migrationen).
- Handover-Dateien sind **Index + aktuelle Lage + Next Steps**. Keine Spez/Architektur wiederholen – nur **Links**.

## Ablageorte (Konvention)

- **Global / Repo-Landschaft**: `projects/_meta/master_map.md`, `README.md`
- **Pro Projekt**: `projects/<projekt>/README.md` + `projects/<projekt>/00_overview/current_status*.md`
- **Cross‑cutting Infra**: `infrastructure/<thema>/...` (z. B. Spark unter `infrastructure/spark/`)
- **Themen-Handover (optional, klein halten)**: `infrastructure/<thema>/<TOPIC>_HANDOVER.md` oder `projects/<projekt>/00_overview/<topic>_handover.md`

## Was du in einen neuen Chat kopierst (Copy/Paste Block)

### 1) Kontext: „In welchem Universum sind wir?“

- **Workspace**: `ai_projects.code-workspace` (Multi‑Root: `projects/`, `infrastructure/`, `code/`)
- **Aktives Projekt**: `<PROJECT_NAME>`
- **Ziel / Outcome**: `<1 Satz – was soll am Ende stehen/laufen?>`
- **Nicht‑Ziele / Guardrails**: `<z. B. keine Secrets in Logs/Terminal, keine Client‑Exposure, keine Scope‑Ausweitung>`

### 2) Repo-Orientierung (wichtig im Multi‑Repo Setup)

- **Docs/Infra** liegen im Root‑Repo: `projects/`, `infrastructure/`
- **Code** liegt in separaten Git-Repos unter: `code/<repo>/` (nicht Teil des Root‑Repos)

### 3) Aktueller Zustand (nur „was ist gerade wahr?“)

- **Status**: `<running / broken / partially working>`
- **Letzte bestätigte gute Version / Zeitpunkt**: `<Datum + kurze Notiz>`
- **Blocker / Fehlerbild**:
  - `<Symptom>`
  - `<Repro Steps oder Job-ID/Asset-ID>`
  - `<Logs/Debug Pointer>`

### 4) Architektur-Schnittstellen (nur die, die man zum Debuggen braucht)

- **Control Plane**: `<z. B. Supabase Cloud Project X>`
- **Data Plane**: `<z. B. Spark Worker / VM102 Worker>`
- **Speicher/Queues**: `<Buckets, Tabellen, Queues>`
- **Endpoints**: `<LLM serving URLs/Ports, falls relevant>`

### 5) Aktive Arbeits-Hypothese

- `<1–2 Sätze: wovon gehen wir aus und was testen wir als Nächstes?>`

### 6) Nächste Schritte (max. 5, „hands-on“)

1. `<konkreter Schritt>`
2. `<konkreter Schritt>`
3. `<konkreter Schritt>`
4. `<konkreter Schritt>`
5. `<konkreter Schritt>`

### 7) Kanonische Links (damit niemand Spez dupliziert)

- **Global Map**: `projects/_meta/master_map.md`
- **Projekt Index**: `projects/<projekt>/README.md`
- **Current Status**: `projects/<projekt>/00_overview/current_status_*.md`
- **Infra/Runbooks**: `infrastructure/<...>/...`
- **Code Entry Points**: `code/<repo>/...`

### 8) „Sicherheits“-Hinweise (immer!)

- **Keine Secrets tippen** (History/Logs/Scrollback). Nur env‑files / systemd `EnvironmentFile`.
- **Nie Service Role Keys im Browser/Client**.
- Bei Key-Leak: **rotieren**.

## Wann lohnt sich ein eigenes Themen-Handover?

Nur wenn mindestens eins zutrifft:

- Es gibt **operative Schritte** (SSH, systemd, Ports, Requeue), die nicht in „Current Status“ gehören.
- Es gibt **wiederkehrende Fehlerbilder** (z. B. MinerU „no .md“) mit Debug-/Fix-Playbook.
- Mehr als **2 Personen/Chats** müssen das Thema unabhängig debuggen können.

Wenn nein: lieber nur im `current_status*.md` einen Abschnitt „Blocker“ pflegen und auf die eigentliche Doku verlinken.
