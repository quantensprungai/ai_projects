# text2kg – Testablauf und erwartete DB-Inhalte

<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Konkrete Schritte zum Testen des text2kg-Jobs (lokal/Spark) und erwartete Tabelleninhalte; Option Term-Mapping für node_key."
  in_scope:
    - Testschritte (lokal, optional Spark)
    - Erwartete Zeilen in hd_kg_nodes, hd_ingestion_jobs.debug
    - Option: canonical_id aus Term-Mapping für node_key
  out_of_scope:
    - Automatisierte E2E-Tests (Code)
notes:
  - "Worker: code/hd_saas_app/apps/web/scripts/hd_worker_mvp.py. Spec: text2kg_spec.md."
-->

## 1) Testablauf (lokal)

Voraussetzung: Supabase lokal läuft (`pnpm supabase:start` in `code/hd_saas_app/apps/web`), ENV `SUPABASE_URL` und `SUPABASE_SERVICE_ROLE_KEY` gesetzt (z. B. aus `.env` im Script-Verzeichnis).

### Variante A: Vollpipeline bis text2kg (automatische Queue)

1. **Bis Chunks + Interpretationen kommen**
   - PDF hochladen (App oder direkter Storage-Upload + Job anlegen).
   - Jobs nacheinander abarbeiten lassen:
     - `extract_text` → `classify_domain` → `extract_term_mapping` → `extract_interpretations`
   - Worker mehrfach ausführen bis alle erledigt:
     ```bash
     cd code/hd_saas_app/apps/web/scripts
     python hd_worker_mvp.py --once   # wiederholen bis "no queued jobs" oder text2kg completed
     ```
   - Nach Abschluss von `extract_interpretations` wird **automatisch** ein Job `text2kg` mit gleichem `debug.asset_id` eingereiht.

2. **text2kg ausführen**
   - Ein weiterer `--once`-Lauf verarbeitet den text2kg-Job (oder im `--loop`-Betrieb passiert es direkt danach).

3. **Prüfen**
   - Siehe Abschnitt 2 (erwartete DB-Inhalte).

### Variante B: Direkt weitermachen (Pipeline bis Interpretations schon durchgespielt)

Wenn ihr **bereits** PDF-Upload, MinerU, Domain Classification, Term Mapping und **extract_interpretations** durchgespielt habt:

1. **asset_id ermitteln**  
   Ein Asset, zu dem Interpretationen existieren (z. B. aus `hd_interpretations` eine Zeile nehmen → `chunk_id` → in `hd_asset_chunks` nachschauen → `asset_id`; oder aus dem letzten extract_interpretations-Job in `debug.asset_id`).

2. **text2kg-Job**  
   - **Falls** nach eurem letzten extract_interpretations-Lauf schon ein **text2kg**-Job eingereiht wurde (Worker-Version mit Auto-Queue): in `hd_ingestion_jobs` nach `job_type=text2kg`, `status=queued` suchen. Wenn vorhanden: nur noch Worker laufen lassen.  
   - **Falls nicht** (z. B. Lauf war vor der text2kg-Implementierung): Job manuell anlegen:
     - `account_id` = eure Account-UUID (wie bei den Interpretationen)
     - `job_type` = `text2kg`
     - `status` = `queued`
     - `debug` = `{"asset_id": "<uuid des gewählten Assets>"}`

3. **Worker ausführen**
   ```bash
   cd code/hd_saas_app/apps/web/scripts
   python hd_worker_mvp.py --once
   ```

4. **Prüfen**  
   Siehe Abschnitt 2.

**HD vs. BaZi:** Für den text2kg-Test egal – beide funktionieren. Nehmt das Asset, zu dem ihr die Interpretationen habt (HD oder BaZi).  
**Stub vs. LLM:** `payload.source` = **Herkunft der Extraktion:** `mvp_stub` (Platzhalter) oder `llm_extraction` (echte LLM-Extraktion). Das **System** (hd, bazi, …) steht in `hd_interpretations.system`, nicht in source. In den Nodes erscheint `metadata.source` 1:1 aus dem Payload – damit seht ihr, ob die Node aus Stub oder LLM stammt.

### Variante C: Nur text2kg testen (beliebiges Asset mit Interpretationen)

1. **Asset mit Interpretationen voraussetzen**
   - Es gibt mindestens ein Asset, für das bereits `hd_asset_chunks` und `hd_interpretations` gefüllt sind (z. B. nach einem früheren extract_text + extract_interpretations Lauf).

2. **text2kg-Job manuell anlegen**
   - In `hd_ingestion_jobs` eine Zeile einfügen (z. B. über Supabase Studio oder SQL):
     - `account_id` = passende Account-UUID
     - `job_type` = `text2kg`
     - `status` = `queued`
     - `debug` = `{"asset_id": "<uuid des Assets>"}`

3. **Worker ausführen**
   ```bash
   python hd_worker_mvp.py --once
   ```

4. **Prüfen**
   - Siehe Abschnitt 2.

---

## 2) Erwartete DB-Inhalte nach text2kg

### hd_ingestion_jobs (der text2kg-Job)

- `status` = `completed`
- `error` = `null`
- `debug` enthält u. a.:
  - `text2kg_nodes`: Anzahl der verarbeiteten Interpretationen (und damit upserteten Nodes)
  - `asset_id`, ggf. `source_job_id`, `system_id` (wenn aus Pipeline übernommen)
  - `worker_host`, `worker_pid` (durch _update_job ergänzt)

### hd_kg_nodes

Pro Interpretation (pro Chunk bei aktueller Stub/LLM-Logik) **eine** Node-Zeile (oder eine pro eindeutigem `node_key` bei Mehrfachtreffern):

- **account_id:** wie im Job
- **node_key:** `{system}.{element_type}.{element_id}` (sanitized), z. B. `hd.asset_chunk.<asset_uuid>_0`
- **node_type:** aus `element_type`, z. B. `Asset Chunk`
- **canonical_description:** `NULL` (bleibt für Synthesis leer)
- **metadata (jsonb):**
  - `interpretation_ids`: Array mit einer UUID (die Interpretation)
  - `chunk_ids`: Array mit einer UUID (der Chunk)
  - `source`: z. B. `llm_extraction` oder `mvp_stub` oder `text2kg`
  - `dimensions`: Objekt (falls im Interpretation-Payload vorhanden)
  - `interactions`: Objekt (falls im Interpretation-Payload vorhanden)

**Idempotenz:** Gleicher Job nochmal ausgeführt → gleiche `(account_id, node_key)` → **Update** (metadata wird gemergt: `interpretation_ids`/`chunk_ids` werden angehängt, `dimensions`/`interactions` überschrieben).

### Schnellprüfung (SQL)

```sql
-- Anzahl Nodes pro Account nach letztem text2kg-Lauf
SELECT account_id, COUNT(*) FROM public.hd_kg_nodes GROUP BY account_id;

-- Eine Node inkl. metadata ansehen
SELECT id, account_id, node_key, node_type, canonical_description, metadata
FROM public.hd_kg_nodes
LIMIT 1;
```

---

## 3) Optional: Term-Mapping für node_key (canonical_id)

Aktuell wird **node_key** aus Fallback gebildet: `{system}.{element_type}.{element_id}` (sanitized). Um synonym-sichere, stabile Keys zu nutzen, kann **canonical_id** aus `hd_term_mapping` verwendet werden.

### Wo einbauen (Worker)

- **Stelle:** In der text2kg-Branch, **bevor** `node_key = f"{system}.{element_type}.{element_id}"` gesetzt wird.
- **Schritt 1:** Einmalig pro Job (oder pro Account) Term-Mapping laden:
  - Abfrage: `hd_term_mapping` für `account_id`, optional gefiltert nach `system` (aus den Interpretationen).
  - Daraus eine Lookup-Map bauen: z. B. `(system, lower(term)) -> canonical_id`; bei `synonyms` jedes Synonym ebenfalls eintragen.
- **Schritt 2:** Pro Interpretation:
  - Kandidaten für Lookup: `element_id`, ggf. erste Zeile/Stichwort aus `payload.essence` oder einem Label-Feld.
  - Lookup: zuerst `(system, element_id.lower())`, falls nicht gefunden z. B. `(system, essence_snippet.lower())`.
  - Wenn Treffer: `node_key = canonical_id` (evtl. sanitizen).
  - Wenn kein Treffer: wie bisher Fallback `node_key = f"{system}.{element_type}.{element_id}"`.

### Erwartung

- Wenn das LLM z. B. `element_type=type`, `element_id=Generator` liefert und in `hd_term_mapping` der Eintrag `term=Generator` → `canonical_id=hd.type.generator` existiert, wird **node_key = hd.type.generator** gesetzt. Mehrere Chunks/Interpretationen zum gleichen Begriff landen dann in **einer** Node (gewünschte Normalisierung).

Referenz: `text2kg_spec.md` (Sektion Term-Mapping Pflicht), `worker_contract_extract_term_mapping.md`.
