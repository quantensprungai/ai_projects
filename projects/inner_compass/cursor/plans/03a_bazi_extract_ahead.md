<!--
Reality Block
last_update: 2026-09-13
scope: Parallel-Track zu Plan 03 — BaZi-Literatur extract-ahead (MinerU), keine KG-Welle
in_scope: Disk-Inventur, Staffeln, Spark-MinerU extract_text, wave-Tags, Classify-Parken
out_of_scope: classify, interpret, text2kg, Relink, Synth, Re-Extract Destiny Code, Spark-Qwen, Chart-UI (liegt in 03)
-->

# Plan 03a — BaZi Extract-ahead

Begleittrack zu [03_bazi.md](03_bazi.md). Fläche (Routing, Chart, Unabhängigkeitsbeleg) und MinerU laufen **parallel**. Die KG-Kette nicht.

SoT: Playbook [k2_foundation_wave_playbook.md](../reference/k2_foundation_wave_playbook.md) §4a. Muster: [astro_natal_ingest_runbook.md](../../reference/astro_natal_ingest_runbook.md). Spark-Knöpfe: [ziwei_natal_ingest_runbook.md](../../reference/ziwei_natal_ingest_runbook.md). Queue-Snapshot: `reference/literature_content_wave_queue_2026-07-18.csv` (nicht umschreiben).

## Was dagegen spricht — und was nicht

| Parallel zu Plan 03 | Urteil |
|---|---|
| MinerU `extract_text` + `extract_ahead=true` | **ja.** Chunks liegen, Classify wird nicht gezogen. |
| Seed / `life_domain_map` / Chart-First-Cut | **ja.** Seed vor text2kg, nicht vor Extract. |
| classify / interpret / text2kg / Relink / Synth | **nein.** Eine System-Welle, Langdock, `IC_TEXT2KG_AUTO_SYNTH=false`. Nach Extract anfallende Classify-Jobs verwerfen. |
| Spark-Qwen / `IC_LLM_URL=:30001` | **nein.** SGLang bleibt aus. |
| Alle 52 Dateien in einen Lauf | **nein.** Duplikate + K4 + azw3/epub. |

Inventur 2026-09-11: 60 Jiazi-Knoten, 0 Interps. Extract füllt das nicht allein. Review 3 (2026-09-13): Jiazi-KG **nicht jetzt** — Nachzug, kein Blocker für Phase 4. Destiny-Chunks auf `bazi.jiazi.*` relinken bleibt PDF-freier Hebel für diesen Nachzug.

## Ist (2026-09-11)

**Disk:** `C:\Users\Admin105\Downloads\Literatur\bazi` (`K2+K3`, `K3`, `klassisch`, Root). 52 PDF + 4 epub + 4 azw3. Dateinamen-Hash: **29 unique**, Rest Anna’s-Archive-/Ordner-Duplikate. `Downloads\bazi_pdfs` ist Nebenkopie — Source of Truth ist `Literatur\bazi`.

**KG:** Destiny Code `cbe86636` schon `text_extracted` (420 Chunks). Nicht nochmal MinerU.

**Spark** (`spark-56d0` / `100.96.115.1:2222`): GPU GB10 da. `ic_worker.py` extract_text **läuft**. systemd-MVP weiter crash-loop (`sudo` nötig). SGLang down.

**Staffel 1 (2026-09-12, fertig):** 三命通会 上 145, 下 151, 渊海子平 48, 滴天髓 67 Chunks — alle `text_extracted`, kein Classify. 滴天髓-Retry mit `pipeline` / Batch 20.

**Staffel 1b (2026-09-12, fertig):** 阐微 144 Chunks, 穷通宝鉴 74. Kein Classify.

**Staffel 1c (2026-09-12, fertig):** 秘本子平真诠 54 Chunks. Klassiker 1+1b+1c = 683 Chunks, kein Classify. Staffel 2 (*60 Pillars*, `latin`) nur zusammen mit der Jiazi-KG-Welle, nicht parallel zu Phase 4.

**Gate vor dem ersten Job:** Worker-Env prüfen. Nur starten, wenn `IC_WORKER_JOB_TYPES=extract_text`, `IC_USE_MINERU=true`, `IC_MINERU_LANG=ch` (Job-Debug darf das Env überschreiben — Astro-Falle: Env `ch`, Job `latin`). Kein `IC_CHUNK_PROFILE=rave_iching_gates`. Kein `IC_LLM_URL`.

## Staffeln (unique Hash, eine Datei)

Pfad-Präferenz: `K2+K3/` bzw. `K3/` ohne „Anna’s Archive“-Suffix.

### Staffel 1 — Klassiker, `wave=bazi_classics`, `IC_MINERU_LANG=ch`, `PAGE_BATCH=50`

| Key | Hash | Werk | Lage |
|---|---|---|---|
| sanming_shang | `5793f92a` | 三命通会 上 (2008, 中医古籍) | `K2+K3/` + Root-AA (dup) |
| sanming_xia | `2d19933b` | 三命通会 下 | dto. |
| yuanhai | `0b74d33a` | 渊海子平大全 (华龄 2014) | dto. Hash in einem Dateinamen 30stellig |
| ditiansui | `af1a8690` | 滴天髓 (中州 1994) | `K3/` |

**1b, nach Staffel-1-Chunks, gleiches wave:**

| Key | Hash | Werk |
|---|---|---|
| ditiansui_chanwei | `caed818f` | 秘授滴天髓阐微 |
| qiongtong | `4f8bd8e2` | 穷通宝鉴评注 |

**Lücke:** 子平真诠 steht in Registry und Welle-Text, **liegt nicht** unter `Literatur\bazi` und **fehlt in der Juli-Queue**. Extract-ahead startet ohne sie. Vor der KG-Welle nachziehen, nicht die vier vorhandenen blockieren.

### Staffel 2 — Jiazi, `wave=bazi_jiazi`, `latin` (Joey Yap *60 Pillars*)

Nur PDF. azw3/epub nicht durch MinerU.

Lokal als PDF: Ding `b73f785a`, Ren `da050c3c`, Yi `5f493a40`, Gui `e74b93a3`, Wu `e1171a1b` **oder** `5ceb77b0` (zwei Ausgaben, eine wählen), Xin/Zin `834984fb`.

Fehlt als PDF: Bing (nur azw3 `b3d035c1`), Jia (nur azw3 `866fc99a`), Ji (nur epub `17f3eed7`).

### Parken — nicht in diesen Lauf

- Destiny Code `58c78ecd` (und die verkürzte K2+K3-Kopie)
- Ten Day Masters (10 Hashes, Root = `klassisch/K4`) — K2/K4-Duplikat der Stems
- *Power of X* (3 Bände, Ten Gods) — eigene Welle
- Spark-Leftover Geng
- Timing/Dayun-UI-Literatur

## Ablauf

1. Worker-Gate (siehe Ist). SGLang bleibt aus.
2. Unique-PDFs Staffel 1 nach Spark: `~/srv/hd-worker/literature/bazi/{hash}.pdf` (ASCII-Key, große Scans `IC_LOCAL_PDF_PATH`).
3. Source + Job `extract_text`, `debug`: `wave=bazi_classics`, `extract_ahead=true`, `mineru_lang=ch`, `page_batch=50`. Storage-Key ASCII.
4. Classify-Jobs, die der Worker trotzdem enqueued, **canceln/parken** — nicht Langdock anwerfen.
5. Staffel 1b, dann Staffel 2 (latin, anderes wave).
6. KG-Kette erst wenn Plan 03 Fläche steht **und** Chunks da sind: Seed liegt (97 Nodes, kein Re-Seed), strict, Langdock, scoped Synth `--only-id`. Destiny nicht full-synthen.

Upload-Skript analog Astro/Ziwei neu, falls keins ohne Destiny-Hardcode existiert. `spark_s5d_extract.sh` nicht anfassen (latin + Qwen).

## Todos

1. Worker-Env auf Spark verifizieren *(D)*
2. Staffel 1 scp + enqueue *(D)*
3. Chunk-Counts / Source-Status prüfen, Classify verwerfen *(D)*
4. 子平真诠 lokal beschaffen (nicht blockierend) *(D)*
5. Staffel 1b + 60-Pillars-PDFs (fehlende Stem-Bände) *(D, nach 1)*
6. KG-Welle **nicht** in diesem Plan

## Nicht

52-Datei-Blindflug, Re-MinerU Destiny Code, azw3/epub durch MinerU, text2kg/Synth, Spark-Qwen, `supabase db reset`, I-Ching-Chunk-Profil, Juli-CSV als Live-Queue umschreiben, Plan-03-UI blockieren.
