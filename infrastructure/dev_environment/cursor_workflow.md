<!-- Reality Block
last_update: 2026-01-22
status: draft
scope:
  summary: "Praktischer Cursor-Workflow für unser Multi-Repo Setup (Docs/Infra + Code-Repos) inkl. Agent/Plan-Mode Disziplin."
  in_scope:
    - prompt/workflow conventions
    - rules & slash-commands conventions
    - multi-repo usage (root vs code repo)
    - troubleshooting patterns (high level)
  out_of_scope:
    - Cursor account/billing
    - model hosting specifics (siehe Spark-Doku)
notes:
  - "Quelle: Roh-Transkript in scratch (nicht Source of Truth). Diese Datei ist die kuratierte Version."
-->

# Cursor Workflow (ai_projects)

## Ziel

Ein gemeinsamer, reproduzierbarer Workflow für Cursor in unserem Setup:
- **Root-Repo** `ai_projects/` (Docs/Infra/Meta)
- **Code-Repos** unter `code/<repo>/` (jeweils eigenes Git/Remote)

## Grundprinzipien (die wirklich wirken)

- **Neue Chats pro Task**: pro klarer Aufgabe (1 Bug, 1 Feature, 1 Refactor) ein neuer Chat. Lange “Append-only” Chats degradieren Qualität.
- **Plan-Mode für größere Änderungen**: alles, was mehr als ~1–2 Dateien/Schritte betrifft, zuerst als Plan formulieren lassen.
- **Kontext bewusst füttern**: relevante Dateien explizit hinzufügen; kein “alles lesen” als Default. Lieber iterativ.
- **Guardrails (Lint/Format/Tests)**: Agenten sind besser, wenn sie automatische Checks “sehen” und selbst korrigieren können.

## Empfohlenes Setup (für uns)

### Workspace-Strategie

- **Doku/Infra-Arbeit**: Workspace = `ai_projects/` (Root)
- **Implementierung in einem Projekt**: Workspace = `code/<repo>/` (fokussiert)
- **Crosslinks**: In Code-Repos kurze “Docs live here” Sektion (siehe `projects/_meta/rules.md`)

### Regeln & Slash Commands

Wir nutzen Rules/Commands, um wiederkehrende Arbeit zu standardisieren:

- **Review** (vor Merge/Release):
  - “Code Review”: Edgecases, Ladezustände, Fehlerpfade
  - “Security Review”: Auth/RLS/Secrets
- **Docs**:
  - “Doku Vibe Check”: Klarheit, keine Marketing-Floskeln, konkrete Schritte

Wenn wir Inhalte daraus “verallgemeinern”, landen sie in `projects/_meta/` oder `infrastructure/dev_environment/`.

## Praktische Prompt-Patterns

- **Klein & direkt**:
  - “Füge X hinzu”, “Entferne Y”, “Fixe Z”, plus *Akzeptanzkriterium*
- **Wenn du Fehler/Logs hast**:
  - 1) Symptom, 2) exakte Fehlermeldung, 3) wo (URL/Command), 4) Erwartung
- **Wenn es um Struktur geht**:
  - erst Zielzustand beschreiben (Ordner/Docs), dann Migration (Schritte), dann Link-Fixes

## Scratch ↔ Doku (wie wir Rohmaterial verwerten)

Rohmaterial (Chats, Transkripte, Exporte) bleibt in `scratch/` und wird **nicht** committed.
Was “Source of Truth” werden soll, wird **kuratiert** und dann promotet:

- Infra/Runtime → `infrastructure/...`
- Projektwissen/Specs → `projects/...`
- Code → `code/...` (im jeweiligen Repo)

## Quelle

- Roh-Transkript: `scratch/inbox/infrastructure/cursor_insights.md`

