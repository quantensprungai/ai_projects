# Gesamtprozess: Batch (200+ PDFs), LLM vs. Stub, Spark (ein Rechner)

<!-- last_update: 2026-02-10 -->

Kurzfassung: **Stub ist nur Fallback** – für echten Betrieb LLM-Env setzen. **LLM läuft auf Spark** (bereits konfiguriert); per **Model-Switcher** wird das LLM ein- bzw. ausgeschaltet. **Jedes Dokument läuft von vorne bis hinten** (extract_text → … → synthesize_node). Optional: zuerst nur `extract_text` auf Spark durchlaufen lassen (LLM aus), dann LLM anschalten und die restlichen Schritte (interpretations → text2kg → synthesis) auf derselben Spark-Instanz abarbeiten.

---

## 1) Stub vs. LLM – „Stub-Problem lösen“

**Stand:** Der Worker nutzt LLM, sobald die passenden Umgebungsvariablen gesetzt sind. Stub wird nur verwendet, wenn **keine** LLM-URL konfiguriert ist.

| Schritt | Env (Beispiel) | Verhalten |
|--------|-----------------|-----------|
| **extract_interpretations** | `HD_LLM_EXTRACTION_URL` (z. B. `http://spark:30001/v1/chat/completions`) gesetzt | LLM extrahiert Interpretationen. |
| | Nicht gesetzt | **Stub:** `_mk_interpretation_payload_stub()` – Platzhalter-Interpretationen, nur für Tests. |
| **synthesize_node** | `HD_LLM_SYNTHESIS_URL` (Fallback: `HD_LLM_EXTRACTION_URL`) gesetzt | LLM erzeugt canonical_description + wordings/Styles. |
| | Nicht gesetzt | **Stub:** `_build_synthesis_stub()` – Aggregation aus Interpretationstexten, keine echten Styles. |

**Was „mit LLM arbeiten“ konkret heißt:**

- **LLM läuft auf Spark** (Env bereits gesetzt: `HD_LLM_EXTRACTION_URL`, `HD_LLM_SYNTHESIS_URL` usw.). Das LLM wird über den **Model-Switcher** ein- bzw. ausgeschaltet – kein separater „Rechner mit LLM“ nötig.
- **Stub „Problem“:** Es gibt keins. Sobald die URLs gesetzt und das LLM per Model-Switcher angeschaltet ist, nutzt der Worker das LLM. Stub nur, wenn LLM aus oder URL nicht erreichbar.

**Fazit:** Stub ist bewusster Fallback. Für euren Ablauf: Env auf Spark setzen, Model-Switcher für LLM-Schritte einschalten (siehe optional zwei Phasen unten).

---

## 2) Ablauf: Jedes Dokument von vorne bis hinten (alles auf Spark)

Die Pipeline ist **pro Asset eine Kette**: ein Job wird abgeschlossen, der nächste wird für **dasselbe** Asset gequeued. **LLM läuft auf Spark** – alles (MinerU, LLM-Extraction, Synthesis) kann auf derselben Instanz laufen; das LLM wird per **Model-Switcher** ein- bzw. ausgeschaltet.

### Wie es aktuell funktioniert

1. Du lädst 200+ PDFs hoch → 200× Asset, 200× Job `extract_text` (queued).
2. Der Worker auf Spark pollt `hd_ingestion_jobs`, führt einen Job aus, schreibt Ergebnis, **enqueued den nächsten Schritt** für dieses Asset.
3. Nach `extract_text` → `classify_domain` (oder direkt `extract_interpretations`) → … → `text2kg` → `synthesize_node`.

**Jedes Dokument läuft von vorne bis hinten.** Wenn das LLM auf Spark per Model-Switcher angeschaltet ist, laufen auch interpretations und synthesis mit LLM auf Spark.

### Optional: Zwei Phasen auf derselben Spark (Ressourcen schonen)

Wenn du **zuerst** nur Text extrahieren willst (MinerU, ohne LLM-Last) und **danach** LLM für die restlichen Schritte nutzen willst:

| Phase | Spark | Was | Anmerkung |
|-------|--------|-----|-----------|
| **Phase 1** | LLM **aus** (Model-Switcher) | Nur **extract_text** (ggf. **extract_text_ocr**) | Worker mit `HD_WORKER_JOB_TYPES=extract_text,extract_text_ocr` – nur diese Jobs abarbeiten. Chunks werden geschrieben; Folgeschritte werden gequeued, liegen in der DB. |
| **Phase 2** | LLM **an** (Model-Switcher) | **classify_domain**, **extract_term_mapping**, **extract_interpretations**, **text2kg**, **synthesize_node** | Filter entfernen (oder Worker ohne Filter), Model-Switcher einschalten. Worker arbeitet die gequeueden Jobs ab; Interpretationen, Nodes, Synthesis werden mit LLM erzeugt. |

**Job-Type-Filter:** Env `HD_WORKER_JOB_TYPES=extract_text,extract_text_ocr` – Worker verarbeitet nur diese Typen. Fehlt die Env, werden alle Typen verarbeitet. So kannst du Phase 1 ohne LLM laufen lassen, dann LLM anschalten und Phase 2 auf **derselben** Spark durchlaufen lassen.

---

## 3) Nodes, Edges, Synthesis, Sprachen

- **Nodes:** text2kg erzeugt **Nodes** (hd_kg_nodes). ✔  
- **Edges:** **Noch nicht implementiert.** text2kg schreibt keine Edges; `payload.relations` / allowed_relation_types sind in Spec/Descriptor vorbereitet. Wenn ihr Edges wollt, kommt das als nächster Schritt nach dem obigen Ablauf.
- **Synthesis:** Pro Node, pro Sprache, pro Style → Zeilen in `hd_synthesis_wordings` + `canonical_description` am Node. Wird vom LLM erzeugt, wenn `HD_LLM_SYNTHESIS_URL` gesetzt ist.
- **Sprachen:** Pro Lauf **eine** Sprache (z. B. `debug.language=de` oder EN als Default). **Verschiedene Sprachen** = mehrere Läufe oder gezielte Batch-Jobs (z. B. synthesize_node für alle Nodes mit `language=de`, dann `language=fr`). Beim ersten Mal mit 200 PDFs: eine Sprache reicht; weitere Sprachen danach gezielt nachziehen.

**Erster Lauf (200+ PDFs):**  
Kann lange dauern: 200 × (extract_interpretations + text2kg + synthesize_node), alles mit LLM. Einmalig; danach sind Interpretationen, Nodes und Synthesis (für die gewählte Sprache) da.

**Neue Quelle / neue School:**  
Gleicher Prozess (Upload → extract_text → … → synthesize_node), nur mit **weniger** Dokumenten → kürzer. Optional: gleiche Pipeline, nur andere `system_id` / Descriptor.

---

## 4) Nächste Schritte (Code/Config)

1. **LLM auf Spark:** Env ist bereits gesetzt; LLM per **Model-Switcher** anschalten, wenn interpretations/synthesis laufen sollen. Stub nur Fallback, wenn LLM aus oder nicht erreichbar.
2. **Optional zwei Phasen:** `HD_WORKER_JOB_TYPES=extract_text,extract_text_ocr` setzen → nur Extraction; danach Filter weglassen und Model-Switcher an → restliche Jobs mit LLM.
3. **Optional:** Warnung im Worker, wenn LLM-Jobs verarbeitet werden sollen, aber keine LLM-URL erreichbar („Stub mode“).

Referenzen: Worker `hd_worker_mvp.py`, Env-Kommentare am Dateianfang; text2kg_spec.md §9; language_and_pipeline_overview.md §0.
