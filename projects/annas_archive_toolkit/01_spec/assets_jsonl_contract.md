<!-- Reality Block
last_update: 2026-01-29
status: draft
scope:
  summary: "Verbindlicher Ingest-Contract `assets.jsonl` (metadata-only), erzeugt vom Anna's Archive Toolkit und konsumiert von HD-SaaS."
  in_scope:
    - JSONL schema (fields + semantics)
    - idempotency key
  out_of_scope:
    - acquire/download automation
    - worker implementation details
notes: []
-->

# `assets.jsonl` Contract (metadata-only)

## Zweck

`assets.jsonl` ist der **metadata-only Ingest-Contract** zwischen:

- **Anna’s Archive Toolkit** (Collect/Select/Publish metadata) und
- **HD‑SaaS** (Ingestion/Knowledge Tables)

“Acquire/Download” ist davon getrennt.

## Format

- **JSONL**: 1 JSON-Objekt pro Zeile
- **Encoding**: UTF‑8
- **Idempotency Key**: `source_ref` (für Toolkit i. d. R. die **MD5**)

## Top-Level Felder (pro Zeile)

### Pflicht

- `title` (string)
- `source_type` (string; Beispiel: `book`)
- `source_ref` (string; **eindeutiger Identifier**, i. d. R. MD5)
- `metadata` (object; JSONB-kompatibel)

### Semantik

- `source_ref` ist der stabile Schlüssel für Upserts/Dedupe im Downstream:
  - HD‑SaaS nutzt `(account_id, source_ref)` als Unique-Key.

## `metadata` Felder (Toolkit-Output)

Die Referenz-Implementierung im Toolkit ist `code/annas-archive-toolkit/src/export_assets.py` und erzeugt typischerweise:

- `profile_id` (string)
- `topic` (string|null)
- `authors` (string[]|null)
- `year` (number|null)
- `language` (string|null)
- `size_mb` (number|null)
- `md5` (string)
- `source_url` (string|null)
- `collected_at` (string, ISO timestamp)
- `raw` (object) – freie Rohdaten/Scoring (z. B. `tier`, `priority`, `category_desc`, `survival_value`, `aa_detail`)

## Beispiel

```json
{"title":"Some Book","source_type":"book","source_ref":"00beee02dec734cfe504204bc6b76218","metadata":{"profile_id":"hd_content","topic":"human design","authors":["A. Author"],"year":2002,"language":"en","size_mb":8.0,"md5":"00beee02dec734cfe504204bc6b76218","source_url":"https://annas-archive.org/md5/00beee02dec734cfe504204bc6b76218","collected_at":"2026-01-28T12:35:14.127041","raw":{"tier":1,"priority":1}}}
```

