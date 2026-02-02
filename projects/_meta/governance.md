# Governance (Multi-Projekt-Repo)

<!-- Reality Block
last_update: 2026-01-29
status: draft
scope:
  summary: "Entscheidungs-, Review- und Ownership-Prozess für `ai_projects/` (Docs/Infra/Meta)."
  in_scope:
    - decision flow for meta and project docs
    - ownership roles and responsibilities
    - review cadence and change categories
    - how to record decisions (ADR)
  out_of_scope:
    - detailed engineering process inside individual code repos
notes: []
-->

## Zweck

Diese Governance hält das Multi‑Projekt‑Repo wartbar: klare Verantwortlichkeiten, nachvollziehbare Entscheidungen, feste Review‑Rhythmen.

## Rollen (leichtgewichtig)

- **Repo Steward (Meta Owner)**: Verantwortlich für `projects/_meta/` (Konventionen, Templates, globaler Rahmen).
- **Project Owner**: Verantwortlich für `projects/<name>/` (Inhalt, Scope, Roadmap, Entscheidungen).
- **Infra Owner**: Verantwortlich für `infrastructure/` (Betrieb, Serving, Security/Ports).
- **Reviewer (rotierend)**: Zweites Paar Augen für Änderungen mit breiter Wirkung.

Faustregel: Jede Datei soll im Reality Block implizit einem Owner-Bereich zuordenbar sein (Meta/Projekt/Infra).

## Änderungs-Kategorien

### Kategorie A — “Safe edits”

Kleine Korrekturen ohne Auswirkungen auf Scope oder Schnittstellen:
- Typos, Struktur/Lesbarkeit, Links reparieren
- Klarere Formulierungen ohne semantische Änderung

Prozess: direkt ändern, `last_update` aktualisieren.

### Kategorie B — “Behavior / Scope / Contract”

Änderungen, die Erwartungen oder Verbindlichkeit verändern:
- Scope Shield, MVP-Definitionen
- Daten-/API-Verträge, Integrationspunkte
- “Source of truth” Verschiebungen (z. B. von `projects/` nach `code/`)

Prozess:
- ADR erstellen/aktualisieren (oder Abschnitt “Decision / Rationale / Consequences” in der Datei)
- Kurzreview durch Reviewer (asynchron reicht)

### Kategorie C — “Infra / Security / Compliance”

Änderungen mit Betriebs- oder Sicherheitswirkung:
- Ports, Public Exposure, Auth, Secrets, Backups
- neue externe Abhängigkeiten/Services

Prozess:
- ADR + Review durch Infra Owner
- wenn nötig: Security Check (kurzer Threat-Check als Textabschnitt)

## Decision Flow (Standard)

1. **Propose**: kurze Beschreibung + Kontext + Optionen (in PR/Commit oder als Abschnitt).
2. **Decide**: Entscheidung festhalten (ADR bevorzugt).
3. **Record**: Links setzen:
   - aus betroffenen Dokumenten auf das ADR
   - im ADR auf die betroffenen Dokumente
4. **Apply**: Änderungen umsetzen.
5. **Review**: “Did we break the map?” (Links, Zuständigkeiten, Scope Shield).

## Review-Rhythmus (minimal)

- **Wöchentlich (15 min)**: “Docs sanity” (Kaputte Links, neue Projekte, offene ADRs).
- **Monatlich (30–60 min)**: Meta-Review (`projects/_meta/*`):
  - passen Templates noch?
  - driftet Naming/Struktur?
  - gibt es doppelte/konkurrierende Doku?

## Wo Entscheidungen leben

- **Meta-Entscheidungen**: idealerweise unter `projects/_meta/` (z. B. ADRs in einem `decisions/`-Ordner, falls ihr das einführen wollt).
- **Projekt-Entscheidungen**: unter `projects/<name>/decisions/` (siehe `project_template.md`).
- **Infra-Entscheidungen**: nahe bei den betroffenen Infra-Dokumenten, zusätzlich verlinkt aus `projects/_meta/master_map.md` wenn global relevant.

## “Source of truth” Regeln (kurz)

- `projects/`: **was/warum/wie auf hoher Ebene** (PRD/Scope/Architektur/Entscheidungen)
- `code/`: **wie genau implementiert** (laufender Stand, APIs, Tests)
- `infrastructure/`: **wie betrieben** (Serving, Backups, Netzwerk)

Wenn sich die Source of truth verschiebt: Kategorie B (ADR + Review).

