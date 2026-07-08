---
last_update: 2026-07-08
scope: S5/S6 Pipeline Learnings — Life Force, elements, Spark, VM105, Channel-Linking, Worker-Betrieb
in_scope: Betriebswissen, Fixes, Skripte, typische Fehler, Worker-Failure-Analyse
out_of_scope: Produkt-Philosophie, App-UX
---

# S6 Pipeline Learnings (Life Force / Elements-Rerun)

> **Kontext:** S5-Testphase — nach S5b (Gates) und S5c (Gene Keys) HD-Welle mit *The Life Force — The Channels* + `elements`-Feld im Worker.
>
> **Status 2026-07-08:** ✅ **S6 Life Force abgeschlossen** — 36/36 Kanon-Channels linked+syn, Orphan-Nodes bereinigt.

## Kurzfassung

| Thema | Learning |
|-------|----------|
| **Chunk-Profil vs. elements** | Gates: `IC_CHUNK_PROFILE=rave_iching_gates`. Channels/Life Force: generisches Chunking + **`elements`** + **Katalog-normalisierte** `hd.channel.*` IDs. |
| **Channel canonical_id** | Immer **`hd_catalog_v0.json`-Reihenfolge** (z.B. `20_34`, nicht `34_20`). Lookup: `ic_hd_channel_lookup.py`. |
| **Bare Gate-Paare im Text** | Buch schreibt oft `39/55` oder `64/47` **ohne** „channel“ — Worker braucht Katalog-validierte Bare-Patterns + Channel-Heuristik **auch wenn** `elements` Gates enthält. |
| **Supabase VM105 vs. Cloud** | Worker auf Spark **muss** `SUPABASE_URL=http://100.70.238.41:54321` setzen — `.env.vm105` allein reicht nicht (Cloud-URL → DNS-Fehler). |
| **LLM / Synthesis** | **`synthesize_node` nur auf Spark** (LLM `127.0.0.1:30001`). Lokal auf Windows: Prep/Status-Skripte ok, **kein** Worker-Loop für LLM-Jobs. |
| **414 PostgREST** | Große `in.(uuid,...)`-Queries → batched fetch/delete (`IC_REST_ID_BATCH`, `_fetch_source_chunks_paged`). |
| **Synthesis 1000-Limit** | `sys_kg_nodes` >1000 → alter Worker lud nur 1000 → fehlende Channels unsichtbar. Fix: paginiertes Fetch + gezielter Fetch bei `only_canonical_ids`. |
| **text2kg 500-Limit** | Alter Handler lud account-weit max. 500 Interpretationen — kippt ab ~3. HD-Source. Fix: `_fetch_interpretations_for_source()` via `chunk_id`-Batches. |
| **Job-Doppel-Claim** | Read-then-PATCH erlaubte parallele Worker auf demselben Job. Fix: `_claim_next_job()` — PATCH nur wenn `status=queued`. |
| **Reverse-Duplikate** | Seed 36 Kanon + 34 Reverse-Keys; nach Migration leere Extras löschen: `ic_s6_orphan_channel_cleanup.py`. |

---

## Worker-Failures (Post-Mortem 2026-07-07)

Drei unabhängige Ursachen erzeugten **`Synthesized 0 nodes`** trotz queued Jobs:

### 1. Lokale Windows-Worker griffen Jobs ab

- Mehrere `ic_worker.py --loop` auf `win11pro105` liefen parallel (teils ohne Output, Exit -1).
- Jobs wurden als `completed` markiert mit `worker_host: win11pro105`.
- LLM von Windows aus (`100.96.115.1:30001`) oft **nicht erreichbar** → alle Syntheses skipped, Job trotzdem „completed“.

**Regel:** Vor Spark-Lauf alle lokalen Worker killen:

```powershell
Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
  Where-Object { $_.CommandLine -like '*ic_worker.py*' } |
  ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
```

### 2. PostgREST `limit=1000` bei Synthesis

- Account hat **1042** `hd.*`-KG-Nodes (Gates + Channels + Seed).
- `_handle_synthesize_node` lud nur 1000 → die 5 fehlenden Kanon-Channels lagen **außerhalb** des Resultsets.
- Symptom: Job completed in Sekunden, `Synthesized 0`, keine LLM-WARNs.

**Fix (2026-07-07):** `_fetch_kg_nodes_for_synthesis()` — paginiert oder `canonical_id=in.(...)` wenn `only_canonical_ids` gesetzt.

### 3. Spark-Shell CRLF

- `spark_s6_phase2.sh` mit Windows-Zeilenenden auf Spark → `set: pipefail: Ungültiger Optionsname`.
- Worker startete nicht.

**Fix:** Beim Deploy `sed -i 's/\r$//' *.sh` auf Spark; lokal `.gitattributes` für `*.sh text eol=lf`.

### Nebenbefund: Job-Debug überschrieben

- Beim Job-Start wurde `debug` durch nur `_worker_meta()` ersetzt (Historie in DB verloren).
- **Fix:** `{**prior_debug, **_worker_meta()}` — Handler nutzt weiterhin in-memory-`job` mit vollem Debug.

### Fix 2026-07-08: text2kg source-scoped + atomisches Claiming

- **text2kg:** Interpretationen nur noch für die Job-`source_id` (über Chunk-IDs), nicht account-weit mit `limit=500`.
- **Job-Claiming:** `_claim_next_job()` patcht `running` nur wenn `status=queued` — verhindert Windows+Spark-Doppelverarbeitung.

---

## Infrastruktur-Topologie

```
PDF (Storage/VM105) → Spark: MinerU + LLM (extract_interpretations, synthesize_node)
                   → VM105 oder lokal: text2kg (REST only, kein LLM nötig)
                   → Supabase DB: http://100.70.238.41:54321 (VM105, Tailscale)
                   → LLM: http://100.96.115.1:30001 (Spark SGLang, nur von Spark localhost)
```

**Nicht:** Cloud-Supabase (`*.supabase.co`) vom Spark ohne Internet/DNS.

### Spark (`~/srv/hd-worker/`)

| Datei | Zweck |
|-------|--------|
| `spark_s6_phase2.sh` | Volle LLM-Phase Life Force |
| `spark_s6_synth_only.sh` | **Nur** `synthesize_node` (Rest-Channels / Cleanup) |
| `spark_s5b_synth.sh` | Synthesis-only Gates |
| `spark_s5d_extract.sh` | BaZi-Test |
| `.env.vm105` | Keys; **immer** `export SUPABASE_URL=http://100.70.238.41:54321` danach |

Deploy nach Code-Änderung:

```bash
scp -P 2222 ic_worker.py ic_hd_channel_lookup.py sparkuser@100.96.115.1:~/srv/hd-worker/
ssh sparkuser@100.96.115.1 "sed -i 's/\r$//' ~/srv/hd-worker/*.sh"
```

Synthesis starten (Spark):

```bash
ssh sparkuser@100.96.115.1 "cd ~/srv/hd-worker && nohup bash spark_s6_synth_only.sh >> logs/s6_synth_only.log 2>&1 &"
```

### Lokal (Windows) — erlaubt vs. verboten

| Erlaubt | Verboten |
|---------|----------|
| `ic_s6_channel_report.py`, `ic_s6_synth_resume.py`, `ic_s6_life_force_cleanup.py` | `ic_worker.py --loop` mit `synthesize_node` / `extract_interpretations` |
| `ic_s6_orphan_channel_cleanup.py`, Migration-Skripte | Paralleler Worker neben Spark |
| `$env:SUPABASE_URL="http://100.70.238.41:54321"` für REST-Skripte | LLM-URL von Windows erwarten |

Service-Role-Key für VM105-Skripte: `pnpm exec supabase status -o json` (web/) **oder** Key aus Spark `.env.vm105`.

---

## Pipeline: `elements`-Feld (ab 2026-07-06)

**Problem:** Generisches Chunking verlinkt nicht zu Seed-Nodes (Channels, BaZi Stems, …).

**Lösung:** LLM liefert pro Interpretation:

```json
"elements": [
  {"element_type": "channel", "element_id": "34-20", "canonical_id": "hd.channel.20_34"}
]
```

**text2kg:** Multi-Link — alle `elements` + Text-Heuristik → `sys_kg_nodes.metadata.interpretation_ids`.

**Wichtig:** Channel-Text-Heuristik (`39/55`, `64/47`) muss **zusätzlich** zu `elements` laufen — früher Early-Return bei vorhandenen Gate-`elements`.

**HD Channels:** Gate-Paare über `ic_hd_channel_lookup.channel_canonical_id(g1,g2)` normalisieren.

---

## S6 Life Force — Source

| Item | Wert |
|------|------|
| Source ID | `2a9272bc-7f9d-4709-a892-43c5e09503ea` |
| Chunks | 175 |
| System | `hd` |

### Skripte (Reihenfolge Bereinigung)

1. `ic_elements_rerun.py --preset life_force` — Interps neu mit elements
2. Worker auf **Spark**: extract → text2kg → synthesize
3. `ic_s6_channel_link_migrate.py` — Reverse-Keys → Kanon
4. `ic_s6_channel_text_relink.py` — Lücken (z.B. `39/55`, `64/47`)
5. `ic_s6_life_force_cleanup.py` / `ic_s6_synth_resume.py` — fehlende Synthesis queue
6. Worker **Spark only** — `spark_s6_synth_only.sh`
7. `ic_s6_orphan_channel_cleanup.py` — 34 Reverse-/Bogus-Nodes löschen
8. `ic_s6_channel_report.py` — **36 Kanon** linked + synthesis

### Erfolgskriterien ✅ (2026-07-08)

- [x] `ic_s6_channel_report.py`: **36/36** linked+syn ok
- [x] `extra hd.channel.* nodes: 0`
- [x] `ic_s6_life_force_cleanup.py --dry-run` → „nothing to queue“

---

## Typische Fehler

| Symptom | Ursache | Fix |
|---------|---------|-----|
| `414 Request-URI Too Large` | Zu viele UUIDs in einer GET | Batched fetch (Worker-Fix) |
| Job `queued` ewig | Kein Worker / falscher SUPABASE_URL | Spark-Worker, VM105-URL |
| Job `running` stuck | Worker abgestürzt | Job cancel + re-queue (`ic_s6_synth_resume.py`) |
| `Synthesized 0 nodes` (schnell) | 1000-Limit **oder** lokaler Worker ohne LLM | Worker-Fix deployen; lokale Worker killen; Spark |
| `Synthesized 0` + `win11pro105` in debug | Lokaler Worker | Alle lokalen `ic_worker.py` beenden |
| Zwei Worker, ein Job | Read-then-PATCH | `_claim_next_job()` (2026-07-08) |
| text2kg linkt unvollständig | account-weit `limit=500` | Worker deployen (source-scoped fetch) |
| `pipefail: Ungültiger Optionsname` | CRLF in `.sh` auf Spark | `sed -i 's/\r$//'` |
| `0/36 Channels` trotz Interps | Kein elements / falsche channel_id | elements-Rerun + Lookup + text_relink |
| `39_55` / `47_64` „nicht im Buch“ | Bare-Paare `39/55`, `64/47` | text_relink + Worker Bare-Patterns |
| `53/70` statt `36/36` | Links auf Reverse-Keys | migrate + orphan_cleanup |
| Synthesis JSON parse error | LLM-Ausgabe | Einzelnode re-queue |
| Gate 18 „fehlt“ | S5b-Wording existiert bereits | Ignorieren |

---

## Testphase vs. Produktion

| Source | Behalten? | Grund |
|--------|-----------|--------|
| S5b Rave I'Ching | ✅ | 64/64 Gate-K4 |
| S5c 64 Ways | ✅ | 64/64 GK-K4 |
| S6 Life Force | ✅ | **36/36 Channel-K4** |
| S5c Opening Doors | Optional löschen | Kein Per-Key-Text |

Kein Full-Rerun nötig — Test **ist** produktive K4 für verlinkte Nodes.

---

## Nächster Schritt nach S6

**S5d BaZi:** 1 PDF (z.B. Destiny Code) → `spark_s5d_extract.sh` → `ic_s5d_bazi_phase2_prep.py` — von Anfang an `elements` + `bazi.stem.*` / `bazi.branch.*` Hints. **Worker-Regeln von S6 beachten** (Spark-only LLM, kein 1000-Limit, LF-Shell).

---

## Verweise

- Pipeline-Jobs: [`../pipeline.md`](../pipeline.md)
- S5 Runbook: [`../../reference/s5_runbook.md`](../../reference/s5_runbook.md)
- Handover S5-Block: [`../handover.md`](../handover.md)
- HD-Katalog: [`../../system_structure/hd_catalog_v0.json`](../../system_structure/hd_catalog_v0.json)
