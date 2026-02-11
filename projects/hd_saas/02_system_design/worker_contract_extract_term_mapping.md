<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Worker-Contract fuer extract_term_mapping (Normalisierung auf canonical_id)."
  in_scope:
    - Inputs (hd_interpretations + optional vorhandenes term_mapping)
    - Output (hd_term_mapping)
    - Idempotenz und Konflikte
  out_of_scope:
    - KG / Synthesis
notes:
  - "Term-Mapping ist Pflicht vor text2kg."
-->

# Worker Contract – extract_term_mapping

## 1) Zweck

Normalisiert Begriffe und Synonyme auf **canonical_id** und befuellt `public.hd_term_mapping`. Das ist **Pflicht** vor `text2kg`, damit stabile Node Keys entstehen und Synonym-Duplikate vermieden werden.

## 2) Input

### Tabellen
- `public.hd_interpretations`
  - `system`, `element_type`, `element_id`
  - `payload` (source, textfelder)
- Optional: bereits existierende `public.hd_term_mapping` (zum Mergen)

### Job-Payload (hd_ingestion_jobs.debug)
```
{
  "account_id": "...",
  "scope": "asset|document|full"
}
```

## 3) Output

### Tabelle: `public.hd_term_mapping`

Pflichtfelder (Schema siehe Migration `20260131170000_hd_term_mapping_interactions_synthesis_wordings.sql`):
- `account_id`
- `system` (z. B. `hd`, `bazi`)
- `canonical_id` (z. B. `hd.type.generator`)
- `term` (z. B. `Generator`)
- `language` (z. B. `de`, `en`)
- `school` (optional)
- `source` (optional)
- `synonyms` (optional, text[])
- `confidence` (optional)
- `evidence` (jsonb)
- `metadata` (jsonb)

## 4) Pflichtlogik

1. **canonical_id bestimmen**
   - Falls Mapping existiert: verwenden.
   - Sonst: `{system}.{element_type}.{normalized(element_id)}`.

2. **term/synonyms erweitern**
   - `term` ist der primäre Begriff (oft `element_id` oder extrahierter Begriff).
   - Varianten landen in `synonyms`.

3. **evidence/metadata**
   - In `evidence`: chunk_ids / interpretation_ids / source_ref.
   - In `metadata`: Konflikte oder alternative Zuordnungen.

## 5) Idempotenz

Eintrag ist eindeutig ueber:
```
(account_id, system, language, coalesce(school,''), lower(term))
```
(Unique-Index ist in der Migration gesetzt)

Bei Konflikt: **merge** von synonyms, evidence und metadata.

## 6) Fehlerfaelle

- Unvollstaendige `system/element_type/element_id` -> skip + debug.
- Synonym-Kollisionen -> metadata.conflicts erfassen.
