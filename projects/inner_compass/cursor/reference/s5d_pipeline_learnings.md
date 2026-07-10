# S5d BaZi Pipeline — Learnings (Joey Yap Destiny Code)

last_update: 2026-07-10
scope: S5d BaZi E2E auf VM105 + Spark
in_scope: MinerU 648p, Phase-2-Batches, Wu-Relink, Recovery, Qualitäts-Gate/Wildwuchs
out_of_scope: BaZi Deep-Structure-Seed (→ deep_structure_plan.md)

## Source

- **Title:** S5d BaZi — The Destiny Code (Joey Yap)
- **Source ID:** `cbe86636-1d7b-4a62-8c0a-221ce5f65b5f`
- **Ergebnis (2026-07-10):** 420 Chunks · 420 Interpretationen · text2kg ✅ · synthesize ✅ (393+ wordings)

## MinerU — große PDFs

- **648 Seiten:** Single-run MinerU → CUDA OOM (384-page internal batch).
- **Fix:** `IC_MINERU_PAGE_BATCH=50` in `ic_worker.py` — sequentielle `-s`/`-e`-Runs, MD concat.
- **Timeout:** `IC_MINERU_TIMEOUT=2400` pro Batch (~1–2 min/Batch → ~15–25 min gesamt).
- **Shell:** `spark_s5d_extract.sh` / `spark_s5d_extract_only.sh` (nur extract_text).

## Worker-Bugs (behoben)

- **`attempts` undefined** in `process_one_job` except → Jobs hingen auf `running`.
- **`text2kg` nach Partial-Batch:** `enqueue_text2kg` nur wenn `only_chunk_ids` leer oder `debug.enqueue_text2kg`.

## Phase 2 — Interpretationen

- **420 Chunks in einem Job** → hängt bei VM105-Timeouts / Zombie-`running`.
- **Fix:** `ic_s5d_bazi_recover.py` — Batches à 40, letzter Batch setzt `enqueue_text2kg`.
- **Spark LLM:** `127.0.0.1:30001` — Read-Timeouts 240s einzeln ok, Retry via `IC_INTERP_MAX_RETRIES`.

## Wu Branch (午) — Text-Relink

- **Problem:** `bazi.branch.wu_b` 0 Links — LLM verwechselt 戊 Stem vs. 午 Branch.
- **Fix:** `ic_s5d_bazi_branch_relink.py` — Text-Heuristik (午, Wu 午 (Horse), Peach Blossom, …) → 43 Interps verlinkt.
- **Synthesis:** gezielter `synthesize_node` mit `only_canonical_ids: [bazi.branch.wu_b]`.

## Qualitäts-Gate (2026-07-10) — WICHTIGSTES LEARNING

- **Inventur (`ic_s5d_bazi_node_inventory.py`): 460 bazi-Nodes, Katalog-Kern wären ~37.**
- **Ursache:** text2kg lief **ohne BaZi-K2-Seed** — der Worker erfindet dann frei Node-Keys:
  - Typo-Namespaces: `b_azi.*`, `basi.*`, `bli.branch.*`, `b.azi.*`, `bazi.tengod.*` (statt `ten_god`)
  - 66 `bazi.asset_chunk.*` Fallback-Nodes
  - 120 Ten-God-Extras, Duplikat-Slugs desselben Konzepts (`jiecai` / `rob_wealth` / `7_killings` / `7killings`)
  - Unsinn-Keys (`bazi.branch.0`, `bazi.stem.jia_yi_bing_ding_wu_ji_geng_xin_ren_gui`)
  - `fengshui.*`-Nodes unter `system='bazi'`
- **Synthesis-Qualität:** Katalog-Nodes mit vielen Interps (z. B. `jia`: 105) bekommen **generische**
  BaZi-Beschreibungen ohne Node-Spezifik — zu viele heterogene Interps pro Node verwässern die Synthese.
- **Was sauber ist:** 420 Chunks + 420 `sys_interpretations` (K3-Rohmaterial) — wiederverwendbar für Re-Link.
- **Vergleich HD:** S5b/S6 waren sauber, **weil** der HD-Seed vor den PDFs existierte. Der Unterschied ist der Seed, nicht die Pipeline.

### Konsequenz — Regel für alle weiteren Wellen

1. **Kein Content-Lauf ohne K2-Seed** des Zielsystems (`ic_seed_structure.py` aus `system_structure/*_catalog_v0.json`).
2. **text2kg strict mode** (zu bauen): canonical_id nur gegen Seed-Whitelist auflösen; kein Match → Review-Queue statt Node-Erfindung.
3. **BaZi-Sanierung:** Seed → Wildwuchs-Cleanup (analog `ic_s6_orphan_channel_cleanup.py`) → Re-Link aus bestehenden Interpretationen → Re-Synthese.

## Skripte

| Skript | Zweck |
|--------|--------|
| `ic_s5d_bazi_node_inventory.py` | Node-Inventur: Katalog vs. Wildwuchs |
| `ic_s5d_bazi_upload.py` | PDF → sys_sources + extract_text job |
| `ic_s5d_bazi_phase2_prep.py` | system_id + term_mapping + interpretations queue |
| `ic_s5d_bazi_status.py` | Coverage stems/branches/ten_gods/synth |
| `ic_s5d_bazi_recover.py` | Zombie-Jobs reset + Interpret-Batches |
| `ic_s5d_bazi_branch_relink.py` | Fehlende Branch-Links aus Text |
| `spark_s5d_extract_only.sh` | Spark: nur extract_text |
| `spark_s5d_phase2.sh` | Spark: LLM-Kette ohne extract |

## Betrieb

- **LLM/MinerU nur auf Spark** — lokale Windows-Worker killen vor Start.
- **VM105 erreichbar** prüfen (`curl http://100.70.238.41:54321/rest/v1/` von Spark).
