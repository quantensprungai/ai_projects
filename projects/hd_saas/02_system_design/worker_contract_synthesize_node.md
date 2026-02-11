<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Worker-Contract fuer synthesize_node (Synthesis von KG + Interpretations)."
  in_scope:
    - Inputs (hd_kg_nodes, hd_interpretations, hd_term_mapping)
    - Output (hd_syntheses + optional hd_synthesis_wordings)
    - canonical_description vs canonical_wording
  out_of_scope:
    - KG-Edges aendern
    - Dynamics erzeugen
notes:
  - "canonical_description wird NICHT in text2kg gesetzt, sondern hier."
-->

# Worker Contract – synthesize_node

## 1) Zweck

Erzeugt **kanonische Beschreibungen** und **user-facing Wording** fuer KG-Knoten auf Basis von Interpretations, Term-Mapping und optional Dynamics.

## 2) Input

### Tabellen
- `public.hd_kg_nodes` (node_key, node_type, metadata)
- `public.hd_interpretations` (payload)
- `public.hd_term_mapping` (canonical_id, synonyms, source)
- optional: `public.hd_dynamics`

### Job-Payload (hd_ingestion_jobs.debug)
```
{
  "asset_id": "...",     // Pflicht im MVP: Scope = alle Nodes mit Interpretations aus diesem Asset
  "node_key": "...",     // optional: gezielter Run (später)
  "language": "en",      // default (international); kann User-Locale/Account sein
  "styles": ["natural", "coaching", "poetic", "technical"]
}
```
**Trigger:** Wird nach `text2kg` automatisch mit gleichem `asset_id` gequeued. Implementierung: `hd_worker_mvp.py`. **Optional LLM:** Wenn `HD_LLM_SYNTHESIS_URL` (OpenAI-kompatibel) gesetzt ist, wird pro Node ein LLM-Aufruf gemacht (canonical_description, canonical_wording, Styles natural/coaching/poetic/technical); sonst Stub-Aggregation aus essence/mechanics/expression. Env: `HD_LLM_SYNTHESIS_URL`, `HD_LLM_SYNTHESIS_MODEL`, `HD_LLM_API_KEY`.

## 3) Output

### Tabelle: `public.hd_syntheses`

Minimal: `payload` enthaelt die erzeugten Texte.
Empfohlenes Payload-Shape:
```
{
  "canonical_id": "hd.type.generator",
  "canonical_description": "...",
  "canonical_wording": "...",
  "styles": {
    "natural": "...",
    "coaching": "...",
    "poetic": "...",
    "technical": "..."
  },
  "evidence": {
    "interpretation_ids": [...],
    "chunk_ids": [...]
  }
}
```

### `public.hd_synthesis_wordings` (MVP-Output)

User-facing Wording wird hier gespeichert (Upsert pro node_id + language + version=1):
- `canonical_description`, `canonical_wording`, `styles` (natural, coaching, poetic, technical)
- `language`, `version`

### Optional: `public.hd_kg_nodes.canonical_description`

Nur hier setzen (nicht in text2kg). Technischer Kanon, kurz und strukturell.

## 4) Synthese-Logik (High-Level)

1. **Aggregation** aus Interpretations:
   - merge essence/mechanics/expression
   - dimensions (non-null bevorzugt)
   - challenges/growth in Clustern
2. **canonical_description** generieren:
   - kurz, technisch, systemtreu
3. **canonical_wording / styles** generieren:
   - natural/coaching/poetic/technical
4. **Speichern** in `hd_synthesis_wordings` (MVP) und PATCH `hd_kg_nodes.canonical_description`; optional `hd_syntheses.payload` später.

## 5) Idempotenz

Pro `(account_id, node_id, language, version)` bzw. `(account_id, canonical_id, language, version)` upserten.

## 6) Fehlerfaelle

- Keine Interpretations fuer Node -> skip + debug.
- Unvollstaendiger Payload -> skip + metadata.flag.

---

## 7) Styles, Sprache, Env (Abgleich mit App)

### Styles: vier Slots; mystical vs. poetic

Die **vier Styles** (natural, coaching, poetic, technical) sind im HD-Descriptor und im Schema (`hd_synthesis_wordings.styles` jsonb) festgelegt. **Mystical vs. poetic:** Inhaltlich nicht dasselbe – „poetic“ = bildhaft, evozierend; „mystical“ = transzendent, spirituell, zielgruppenspezifisch (z. B. Gene Keys, Mayan Tzolkin). Statt Schema und UI um einen fünften Slot zu erweitern, **Mapping:** Systeme mit `allowed_styles` wie „mystical“ oder „spiritual“ speichern ihr Wording im Slot **poetic** (technisch); die App kann für diese Systeme das Label „poetic / mystical“ oder „mystical“ anzeigen (z. B. über Descriptor oder Namespace). So bleiben vier Slots, unterschiedliche Zielgruppen werden über Anzeige-Label und default_style abgedeckt. Optional später: eigener fünfter Slot „mystical“, wenn gewünscht.

### Sprachen: Englisch als Basis, viele Sprachen für internationale App

- **Verbindliches Sprachmodell:** `projects/hd_saas/00_overview/language_and_pipeline_overview.md` Abschnitt **0)** – Interpretations quellenbasiert, KG neutral, **Synthesis = einzige multilinguale Schicht** (eine Zeile pro Sprache); keine Interpretationen in allen Sprachen.
- **Geplant:** **Englisch** als kanonische technische Basis und Default; **möglichst viele Sprachen** über Synthesis – das ist der Clou der App.
- **App (Makerkit i18n):** UI in beliebig vielen Sprachen – in `i18n.settings.ts` Sprachen eintragen, unter `public/locales/<code>/` JSON anlegen; LanguageSelector + Cookie. Keine Backend-Änderung nötig.
- **Content intern (Interpretations, Synthesis):** (1) **Default:** `HD_LLM_EXTRACTION_LANG=en`, Job `debug.language` Default **en**. (2) **Mehrsprachigkeit:** `hd_synthesis_wordings` hat Spalte **language** – pro (node_id, language) eine Zeile; Pipeline mit `debug.language=fr` (oder User-Locale) erzeugt Inhalte in dieser Sprache. So können viele Sprachen abgebildet werden (EN, DE, FR, ES, …), ohne Architektur zu ändern. (3) App beim Anlegen der Pipeline: **User-Locale** oder Account-Sprache in `debug.language` übergeben, damit Extraktion und Synthesis in der gewünschten Sprache laufen.

### Env (Spark / LLM)

Alle LLM-Endpoints kommen aus der **Umgebung**; nichts ist im Code fest verdrahtet. Typisch auf Spark:

- **Extraction:** `HD_LLM_EXTRACTION_URL=http://spark:30001/v1/chat/completions` (oder Port 8000, je nach Deployment)
- **Synthesis:** `HD_LLM_SYNTHESIS_URL=http://spark:30001/v1/chat/completions` (kann derselbe Endpoint wie Extraction sein)
- **API-Key:** `HD_LLM_API_KEY` (wenn noetig, fuer beide genutzt)

Wenn die Env bereits hinterlegt ist (z. B. in `.env` auf Spark), aendert der Worker nichts – er liest nur die genannten Variablen. Port 30001 (oder 8000) ist reine Konfigurationssache in der Env.
