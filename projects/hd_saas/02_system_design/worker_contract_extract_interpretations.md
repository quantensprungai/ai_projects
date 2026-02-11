<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Worker-Contract fuer extract_interpretations (LLM-Extraktion von Chunks)."
  in_scope:
    - Inputs (hd_asset_chunks)
    - Output (hd_interpretations)
    - Payload-Contract (Referenz auf interpretations_contract)
    - Idempotenz und Fehlerfaelle
  out_of_scope:
    - Domain-Classification
    - KG / Term-Mapping / Synthesis
notes: []
-->

# Worker Contract – extract_interpretations

## 1) Zweck

Extrahiert **strukturierte Interpretationen** aus `public.hd_asset_chunks.text_clean` und schreibt pro Chunk in `public.hd_interpretations`.

## 2) Input

### Tabellen
- `public.hd_asset_chunks`
  - `id` (chunk_id)
  - `account_id`
  - `asset_id`
  - `chunk_index`
  - `text_clean` (Pflicht)
  - `metadata` (optional: detected_language, source_job_id, etc.)

### Job-Payload (hd_ingestion_jobs.debug)
Minimal:
```
{
  "account_id": "...",
  "asset_id": "...",
  "document_id": "..."
}
```

### LLM-Konfiguration (ENV)
- `HD_LLM_EXTRACTION_URL` (OpenAI-kompatibel; wenn leer, Stub)
- `HD_LLM_EXTRACTION_LANG`
- optional: `HD_LLM_EXTRACTION_MODEL`, `HD_LLM_API_KEY`

## 3) Output

### Tabelle: `public.hd_interpretations`

Pflichtfelder:
- `account_id`
- `chunk_id`
- `system` (z. B. `hd`, `bazi`)
- `element_type` (z. B. `type`, `profile`, `day_master`)
- `element_id` (z. B. `generator`, `3_5`, `geng`)
- `payload` (jsonb)

**Payload-Contract:** siehe `interpretations_contract.md` (Pflichtkeys + dimensions + interactions + evidence).

Minimaler, stabiler Kern im Payload:
- `essence`: string
- `mechanics`: string
- `expression`: string
- `challenges`: string[]
- `growth`: string[]
- `dimensions`: object (Keys immer vorhanden, Werte nullable)
- `interactions`: object (Arrays koennen leer sein)
- `source`: string – **Herkunft der Extraktion:** `llm_extraction` (wenn LLM genutzt) oder `mvp_stub` (Stub). System (hd, bazi, …) steht in der Spalte `system`, nicht in payload.source.
- `evidence`: object|null (chunk_id, quotes, source_ref)

## 4) Idempotenz

Unique-Scope pro Interpretation:
```
(account_id, chunk_id, system, element_type, element_id)
```

Bei Wiederholung: **upsert** und payload aktualisieren.

## 5) Fehlerfaelle

- `text_clean` leer -> Chunk ueberspringen, zaehlen in Debug.
- LLM liefert unparseable JSON -> Chunk ueberspringen, Debug-Fehler zaehlen.
- Kein Element erkennbar -> Chunk ueberspringen, Debug-Info.

Job soll **nicht** durch einzelne fehlerhafte Chunks scheitern; Fehlerzaehler in `hd_ingestion_jobs.debug` protokollieren.
