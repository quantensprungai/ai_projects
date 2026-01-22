<!-- Reality Block
last_update: 2026-01-21
status: stable
scope:
  summary: "Scratch = lokale Zwischenablage für lose Notizen/Exports, die von LLM/Agent zu Doku promotet werden."
  in_scope:
    - inbox workflow
    - file naming conventions
    - promote rules
  out_of_scope:
    - sensitive secrets
notes: []
-->

## Scratch (Inbox) – Workflow

`scratch/` ist deine **Zwischenablage** für:
- lose `keep*` Notizen
- Exporte wie `assets.jsonl`
- Transkripte/Logs, die “erstmal nur abgelegt” werden

**Wichtig:** `scratch/` ist per `.gitignore` ausgeschlossen. Nichts hier wird versehentlich committed.

## So arbeitest du damit (kurz)

- **1) Reinwerfen**: Lege neue Roh-Notizen unter `scratch/` ab (z. B. `scratch/keep_spark_2026-01-21.md`).
- **2) “Promote”**: Wenn es “wertvoll und stabil” ist, wird es von uns in die echte Doku überführt:
  - Spark/Infra → `infrastructure/...`
  - HD‑SaaS Produkt/Specs → `projects/hd_saas/...`
  - ReST → `projects/rest_data_platform/...`
- **3) Archivieren/Löschen**: Nach dem Promote kann die Scratch-Datei bleiben (lokal) oder gelöscht werden.

## Inbox vs Wissen vs Logs (empfohlen)

Du kannst `scratch/` zusätzlich strukturieren, damit du schneller “promoten” kannst:

- **`scratch/inbox/`**: Rohmaterial, ungefiltert (Transkripte, Chat-Exports, Linksammlungen)
- **`scratch/wissen/`**: kuratierte Notizen, die schon “fast Doku” sind (kurz, strukturiert, ohne Ballast)
- **`scratch/logs/`**: technische Logs/Outputs (z. B. curl/ssh/journalctl), die nur als Belege dienen

Minimal-Regel: **Rohmaterial bleibt Rohmaterial**. “Source of Truth” wird **nur** durch Promote in `projects/` oder `infrastructure/`.

## Naming (empfohlen)

- `scratch/<topic>_<yyyy-mm-dd>_<short>.md`
- Beispiele:
  - `scratch/spark_benchmarks_2026-01-21_keep11.md`
  - `scratch/hd_sources_2026-01-21_assets.jsonl`

## “Promote” Pattern (praktisch)

Wenn du ein langes Roh-Transkript hast (z. B. `scratch/inbox/infrastructure/cursor_insights.md`):

- Lass die Rohdatei in `scratch/` (kein Commit, nur lokale Ablage)
- Erstelle **eine kuratierte Kurzfassung** als neue Repo-Datei, z. B.:
  - `infrastructure/dev_environment/cursor_workflow.md`
- Verlinke die Rohquelle als “Quelle”, aber mache klar: **die Kurzfassung ist Source of Truth**

## Minimal-Regel

**Alles, was “Source of Truth” werden soll, muss in `projects/` oder `infrastructure/` landen.**

