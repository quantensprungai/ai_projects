---
last_update: 2026-08-27
status: active
scope:
  summary: "Ziwei-Natal Ingest — 12 中州-PDFs, Spark nur MinerU, LLM Langdock."
in_scope:
  - MinerU-Env, Staffelung, 流年 parken, 深造 eigenes Fenster
out_of_scope:
  - Spark-Qwen Interpret/Synth
  - 大限/流年-UI
---

# Ziwei-Natal Ingest

SoT: `reference/decisions.md` 2026-08-27 Ziwei-Natal-Parität.

## Reihenfolge (nicht verhandelbar)

1. `python scripts/ic_seed_structure.py --system ziwei` (K2 inkl. `belongs_to_domain` candidate in Palace-Metadata).
2. Whitelist: `IC_TEXT2KG_STRICT=true`, `IC_TEXT2KG_STRICT_ZIWEI=true`, `IC_TEXT2KG_AUTO_SYNTH=false`.
3. MinerU auf Spark, **LLM aus** (kein SGLang).
4. Langdock-Worker für classify / term / interpret / text2kg (`ic_start_langdock_worker.py`).
5. Relink `link_role`, scoped Synth via `ic_run_with_langdock.py`.

## MinerU (Spark)

```bash
cd ~/srv/hd-worker
export IC_USE_MINERU=true
export IC_MINERU_LANG=ch
export IC_MINERU_PAGE_BATCH=50
export IC_MINERU_TIMEOUT=7200
export IC_WORKER_JOB_TYPES=extract_text
# NICHT: IC_CHUNK_PROFILE=rave_iching_gates
# NICHT: IC_LLM_URL auf :30001
.venv/bin/python3 ic_worker.py --loop --sleep 5
```

Smoke zuerst: **初级讲义**. Chunk-Profil `ziwei_stars_palaces` erst nach TOC-Stichprobe.

## Werke

Lokal unter `ziwei/` (Inventar `literature_local_inventory_2026-07-18.csv`). Upload: `apps/web/scripts/ic_ziwei_natal_upload.py`.

| Staffel | Werk | Hinweis |
|---|---|---|
| 1 Smoke | 初级讲义 + 星曜性质 | klein |
| 2 | 深造讲义 | ~158 MB Scan — eigenes Fenster, nicht skippen |
| 3 | 讲义补注 上/中/下 | |
| 4 | 全集 一–六 | nicht ein Job |
| parken | 流年凶灾详析 | Jahres-Timing |

## Langdock (nach Extract)

`ic_start_langdock_worker.py` mit `IC_TEXT2KG_STRICT_ZIWEI=true`. Synth nur scoped, nie Full-System.
