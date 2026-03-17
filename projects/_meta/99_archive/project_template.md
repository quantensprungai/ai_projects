> **ARCHIVIERT** (2026-02-16). Inhalt wurde in Cursor Rules (.cursor/rules/) oder doc_and_rules_strategy.md überführt.

# Project Template (für neue Projekte)

<!-- Reality Block
last_update: 2026-01-29
status: draft
scope:
  summary: "Template für neue Projekte in `projects/` inkl. Minimalstruktur, Reality Blocks und Link-Regeln."
  in_scope:
    - recommended folder structure
    - required minimal docs (README, scope, decisions)
    - reality block template
    - linking rules between projects/ code/ infrastructure/
  out_of_scope:
    - per-project implementation details
    - coding standards inside code/<repo> (liegt im jeweiligen Repo)
notes: []
-->

## Zweck

Dieses Template macht neue Projekte in `projects/` konsistent: gleiche Basisseiten, gleiche Benennung, gleiche "Decision / Rationale / Consequences" Struktur.

## Minimalstruktur (empfohlen)

Lege ein neues Projekt unter `projects/<projekt_name>/` an (siehe Naming Conventions).

```
projects/<projekt_name>/
├── README.md
├── 00_overview/
│   ├── scope.md
│   ├── mvp.md
│   └── risks.md
├── 01_product/
│   ├── prd.md
│   └── stakeholders.md
├── 02_specs/
│   └── api_and_data_contracts.md
├── 03_architecture/
│   ├── architecture.md
│   └── security.md
├── 04_roadmap/
│   └── roadmap.md
├── 05_meetings/
│   └── 2026-01-29_kickoff.md
└── decisions/
    └── ADR-2026-01-29_initial-scope.md
```

Hinweise:
- **Ordner sind nummeriert**, damit die Navigation stabil bleibt.
- **`decisions/`** ist Pflicht, sobald es echte Trade-offs gibt.
- **Meeting-Notizen** gehen immer in `05_meetings/` (mit Datum im Dateinamen).

## Projekt-README (Pflichtinhalt)

In `projects/<projekt_name>/README.md` stehen immer:
- **1–3 Sätze Zweck**
- **Status** (draft/active/stable/paused/archived)
- **Links**:
  - Code-Repo: `../../code/<repo>/` (falls vorhanden)
  - Infra: relevante Pfade unter `../../infrastructure/...`
  - zentrale Meta-Regeln: `../_meta/rules.md`

Beispiel-Linkblock:

```md
## Links
- Meta-Regeln: ../_meta/rules.md
- Code-Repo: ../../code/<repo>/
- Infra: ../../infrastructure/<bereich>/
```

## Reality Block (Pflicht in jeder Datei)

Direkt unter den Titel kommt dieser Block (kopieren und anpassen):

```md
<!-- Reality Block
last_update: YYYY-MM-DD
status: draft
scope:
  summary: "Worum geht es in dieser Datei?"
  in_scope:
    - was KI hier ändern darf
  out_of_scope:
    - was KI hier nicht ändern darf
notes: []
-->
```

## Decision Record (ADR) – Template

Lege ADRs in `projects/<projekt_name>/decisions/` an.

```md
# ADR-YYYY-MM-DD_kurzer-titel

<!-- Reality Block
last_update: YYYY-MM-DD
status: draft
scope:
  summary: "Entscheidungsvorlage (ADR) für dieses Projekt."
  in_scope:
    - decision record content
  out_of_scope:
    - implementation details
notes: []
-->

## Decision

Kurz: Was wird entschieden?

## Context

Warum ist die Entscheidung nötig? Welche Constraints gibt es?

## Options

- Option A
- Option B

## Rationale

Warum wurde die gewählte Option bevorzugt?

## Consequences

Was bedeutet das für Betrieb, Kosten, Sicherheit, Wartung?
```

## Quickstart-Checkliste (neues Projekt)

- `projects/<projekt_name>/README.md` erstellt und verlinkt
- Minimalstruktur angelegt (00_overview/…)
- `scope.md` + `mvp.md` initial gefüllt (Scope Shield explizit)
- erstes ADR für die Kernentscheidung(en)
- Eintrag in `projects/_meta/master_map.md` ergänzt
