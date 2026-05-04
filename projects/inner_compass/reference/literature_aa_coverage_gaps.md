---
last_update: 2026-04-20
status: draft
scope:
  summary: "Welche geplanten Werke fehlen auf Anna's Archive (oder nur in schlechter Qualität); legale Alternativen; Reconciliation."
  in_scope:
    - gap log template and status values
    - reconciliation workflow pointer
  out_of_scope:
    - illegale Beschaffung
    - vollständige Curriculum-Tabelle (eigener Agent / Tabelle)
notes:
  - "AA = Beschaffungskanal, nicht Vollständigkeits-Garantie."
---

# Literatur: AA-Abdeckung vs. Ziel — Lücken-Log

**Zweck:** Anna’s Archive ist oft **praktisch**, aber **nicht vollständig** für eure **Ziel-Werklandschaft** (Registries, Curriculum). Diese Datei ist der **einfache, versionierbare Abgleich**: *Was wollten wir? Was hat AA (nicht) geliefert? Was tun wir stattdessen (legal)?*

## Status-Werte (pro Werk / pro Suchlauf)

| `aa_coverage_status` | Bedeutung |
|----------------------|-----------|
| `found` | Auf AA beschafft (MD5/Link in `assets.jsonl` notieren) |
| `not_found` | Suche/Queue ohne Treffer oder dauerhaft leer |
| `wrong_edition` | Nur falsche Ausgabe/Sprache/Scan-Qualität — nicht Zieltext |
| `deferred` | Bewusst zurückgestellt |
| `alternate_legal` | Über anderen **legalen** Kanal (Kauf, Bibliothek, OA-Verlag, Autor-Seite) |

## Log-Spalten (eine Zeile pro relevantem Werk)

Empfohlene Spalten (Copy/Paste als Tabelle oder später CSV):

- `curriculum_id` — interne ID oder Registry-Referenz (Autor+Werk Kurz)
- `system_id`
- `priority_k3_k4` — z. B. `K3`, `K4`, `both`
- `target_title` / `target_author` / `isbn_optional`
- `aa_last_search` — Datum; ggf. genutzter Suchbegriff
- `aa_coverage_status` — siehe oben
- `evidence_note` — kurz: „kein Treffer“, „nur Hörbuch“, „nur Französisch“, …
- `fallback_plan` — z. B. `purchase`, `library`, `oa_url`, `scan_own`, `omit_v0`
- `resolved_at` — wenn eingespielt in IC (`sys_sources` o. Ä.)

## Reconciliation (wann abgleichen)

- **Nach jedem größeren Download-Batch:** Kurz prüfen, ob geplante Registry-Werke mit `found` enden oder als Lücke landen.
- **Periodisch (z. B. monatlich):** Alle `not_found` / `wrong_edition` durchgehen — Priorität nach `system_id` und K3/K4.
- **Vor Release/Meilenstein:** „Ist die Literaturbasis für System X ausreichend für K4?“ — rein inhaltlich, nicht technisch.

## Verknüpfung mit IC

- Erfolgreich eingespielte Werke: idealerweise **`sys_sources.metadata`** oder eure Curriculum-Tabelle mit **`curriculum_id`** / MD5 verknüpfen (mittelfristig technisch nachziehbar).
- Diese Datei bleibt die **planerische Lückenliste**; die **technische Wahrheit** ist **DB + Storage**.

## Start (leer)

| curriculum_id | system_id | priority_k3_k4 | target_author | target_title | isbn_optional | aa_last_search | aa_coverage_status | evidence_note | fallback_plan | resolved_at |
|---------------|-----------|----------------|---------------|--------------|---------------|----------------|-------------------|---------------|---------------|-------------|
| *(Beispiel)* | hd | both | Ra Uru Hu | Rave I'Ching | | | | | | |

Siehe auch: [literature_acquisition_ic_aa.md](literature_acquisition_ic_aa.md) Abschnitt „AA-Vollständigkeit“.
