> **ARCHIVIERT** (2026-02-16). Inhalt wurde in Cursor Rules (.cursor/rules/) oder doc_and_rules_strategy.md überführt.

# Naming Conventions (Repo-weit)

<!-- Reality Block
last_update: 2026-01-29
status: draft
scope:
  summary: "Benennungsregeln für Projekte, Ordner, Dateien und Links im Multi‑Projekt‑Repo."
  in_scope:
    - directory and file naming conventions
    - date-based naming for meetings/decisions
    - naming rules for code repo folder under code/
    - link hygiene rules (relative links)
  out_of_scope:
    - naming inside specific applications (handled per code repo)
notes: []
-->

## Ziel

Einheitliche Namen reduzieren Suchkosten, verhindern "Drift" und machen Automation (Indexing, Export, Generierung) einfacher.

## Allgemeine Regeln

- **Kleinbuchstaben**, keine Leerzeichen.
- **ASCII bevorzugt** (ä/ö/ü/ß vermeiden), sonst konsistent umschreiben (`ae/oe/ue/ss`).
- **Stabilität vor Perfektion**: bestehende Ordner nicht leichtfertig umbenennen (Links brechen).
- **Relative Links** im Repo (siehe `rules.md`).

## Ordnernamen

### `projects/<projekt_name>/`

- Format: **`lower_snake_case`**
- Beispiele:
  - `rest_data_platform`
  - `trading_bot`
  - `hd_saas`

### `infrastructure/<bereich>/`

- Format: **`lower_snake_case`** (oder bestehende Konvention beibehalten)
- Beispiele:
  - `spark`
  - `networking`

### `code/<repo>/`

- Format (empfohlen): **`lower-kebab-case`** (typisch für Repos)
- Bestehende Ausnahmen (z. B. `hd_saas_app`) **nicht** zwangsumbenennen; wichtig ist die saubere Verlinkung aus `projects/<name>/README.md`.

## Markdown-Dateinamen (Docs)

- Format: **`lower_snake_case.md`**
- Beispiele:
  - `architecture_overview.md`
  - `naming_conventions.md`
  - `scope_shield.md`

### Meetings

- Format: **`YYYY-MM-DD_<topic>.md`**
- Ordner: `projects/<name>/05_meetings/`
- Beispiel: `2026-01-29_kickoff.md`

### Entscheidungen (ADRs)

- Format: **`ADR-YYYY-MM-DD_<short-title>.md`**
- Ordner: `projects/<name>/decisions/`
- Beispiel: `ADR-2026-01-29_initial-scope.md`

## Dokument-Titel

- Titel im Dokument darf "schön" sein, Dateiname bleibt technisch.
- Beispiel:
  - Datei: `mvp.md`
  - Titel: `# MVP (Pilot WP2.1)`

## Nummerierte Ordner (optional, empfohlen)

Wenn ein Projekt wächst, nutzt nummerierte Ordner für stabile Navigation:

- `00_overview/` (Scope, MVP, Risiken)
- `01_product/` (PRD, Stakeholder)
- `02_specs/` (Daten-/API-Verträge)
- `03_architecture/` (Architektur, Security)
- `04_roadmap/` (Roadmap)
- `05_meetings/` (Meeting Notes)

## Abkürzungen / Begriffe

- Abkürzungen sparsam verwenden, lieber im Glossar ergänzen: `projects/_meta/glossary.md`
- "WP" (Work Package) ist ok, wenn im Projektkontext etabliert.
