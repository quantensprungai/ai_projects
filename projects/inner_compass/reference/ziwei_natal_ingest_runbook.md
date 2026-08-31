---
last_update: 2026-08-31
status: active
scope:
  summary: "Ziwei-Natal Ingest — Staffel-1 plus Welle 1b (四书/安星/谈斗数), Spark nur MinerU, LLM Langdock."
in_scope:
  - MinerU-Env, Staffelung, 流年 parken, 深造 eigenes Fenster
  - OCR-Wörterbuch-Nachkorrektur vor text2kg (alle Natal-Werke)
  - Have/Missing 中州-Natal (nicht Juli-CSV umschreiben)
  - Stand 2026-08-29 Natal-First-Cut + Qualität/Nacharbeit
  - KARTE-Stand 2026-08-31 (dichte Platte, Chrome DE, Zusammenschau v3, Palast-Re-Synth)
out_of_scope:
  - Spark-Qwen Interpret/Synth
  - 大限/流年-UI
  - 三合/飞星, 玄空, Motivations-格局
---

# Ziwei-Natal Ingest

SoT: `reference/decisions.md` 2026-08-27 Ziwei-Natal-Parität.

## Reihenfolge (nicht verhandelbar)

1. `python scripts/ic_seed_structure.py --system ziwei` (K2 inkl. `belongs_to_domain` candidate in Palace-Metadata).
2. Whitelist: `IC_TEXT2KG_STRICT=true`, `IC_TEXT2KG_STRICT_ZIWEI=true`, `IC_TEXT2KG_AUTO_SYNTH=false`.
3. MinerU auf Spark, **LLM aus** (kein SGLang). Staffel 1: 初级 → 星曜 → 深造 (eigenes Fenster) → 补注 → 全集.
4. OCR-Wörterbuch gegen K2 **über alle Natal-Quellen** (`wave=ziwei_natal`), **vor** text2kg. Nicht über 流年. Skript: `apps/web/scripts/ic_ziwei_ocr_dict_correct.py`.
5. Langdock nur Natal-KG: Classify darf 流年 als `ziwei` taggen, **enqueue interpret/text2kg nicht** (`skip_natal_text2kg` / `wave=ziwei_liunian`). Worker: `_parks_kg_downstream`. Node-`metadata` PATCH als Dict (nicht `json.dumps`).
6. Unwrap `sys_kg_nodes.metadata` falls `jsonb_typeof = string`. Alias-Normalize (`zw.star.wuqu` → `ziwei.star.wuquMaj`) + `ic_relink_strict.py`. Audit `ic_ziwei_natal_audit.py` (12 Paläste + 14 `*Maj`, 流年-Mix, Essences). Dann Relink `ic_ziwei_natal_relink.py` (`link_role`, Primary-Cap 6).
7. **Welle 1b erst nach** Audit+Relink Staffel 1: 安星法 → 谈斗数 → 八喜楼/格局 → 骨髓赋 → 太微赋-Kurznote. MinerU → OCR → Langdock. Scoped Synth **nach** Welle-1b-Relink.
8. **Homophone:** Catalog `ziwei.star.tianfu` = 天福 (Nebenstern), `tianfuMaj` = 天府. Nicht pinyin-gleichsetzen. Repair: `ic_ziwei_homophone_repair.py`. Synth-Sprache = **en** (Zwischenstand); DE später zweite `wordings.language`-Zeile, nicht im Extract.

## MinerU (Spark)

```bash
cd ~/srv/hd-worker
export IC_USE_MINERU=true
export IC_MINERU_LANG=ch
export IC_MINERU_PAGE_BATCH=50
export IC_MINERU_BACKEND=pipeline
export IC_MINERU_TIMEOUT=7200
export IC_WORKER_JOB_TYPES=extract_text
# NICHT: IC_CHUNK_PROFILE=rave_iching_gates
# NICHT: IC_LLM_URL auf :30001
# NICHT: hybrid-auto-engine / VLM (2026-08-27: kein .md, CUDA 12.1 Warnung)
.venv/bin/python3 ic_worker.py --loop --sleep 5
```

Smoke: `python ic_ziwei_natal_upload.py --staffel smoke`. 三合/飞星 bleiben draußen. 流年: Extract mit `wave=ziwei_liunian` (nicht `--allow-liunian` in den Natal-text2kg-Lauf).

Storage-Keys nur ASCII (`{hash}.pdf`). Job-Overrides liegen in `sys_ingestion_jobs.debug` (`mineru_lang=ch`, `page_batch=50`), nicht in einer `payload`-Spalte.

**Spark 2026-08-27:** GPU da, `ic_worker.py` liegt unter `~/srv/hd-worker`. Cloud-Supabase-Host aus `.env` löst auf Spark **nicht** auf (DNS). Extract-Jobs deshalb lokal queued (初级 + 星曜). MinerU-Loop starten, sobald Spark den Rest-Host wieder auflöst; **kein** SGLang/`IC_LLM_URL`. 深造 (~158 MB) erst nach Storage-Limit 250 MiB (config gesetzt, Stack-Restart nötig) oder `IC_LOCAL_PDF_PATH`.

Danach Langdock-Worker (`ic_start_langdock_worker.py`), nicht Spark-Qwen. Chunk-Profil `ziwei_stars_palaces` erst nach TOC-Stichprobe der 初级.

## Werke — Have / Missing

Juli-Inventar (`literature_have_vs_need_2026-07-18.csv`: „13 Werke — 中州派-Kern komplett“) = die 13 lokalen PDFs. **Nicht** der volle 中州-Natal-Kanon (格局-Namen, 安星-Prosa, 四书 fehlten). CSV bleibt Snapshot; Stand hier.

Ordner: `Downloads/Literatur/ziwei/` (Staffel 1) und `ziwei/neu/` (Welle 1b). Duplikate/Müll nicht ingestieren.

### Staffel 1 — Extract + Interpret + text2kg + Relink (2026-08-28)

Metadata-Unwrap (220 Nodes object). Alias-Relink `ic_relink_strict.py` nach `zw.*`/`wuqu`→`wuquMaj`. Audit OK: 12 Kern-Paläste belegt, 14 Hauptsterne belegt, 流年-Mix none. 来因 leer (Warn). Relink `ziwei_natal_relink_v1`: primary 160 / contrast 361 / mention 1675 (Cap 6). Skripte: `ic_ziwei_natal_audit.py`, `ic_ziwei_natal_relink.py`. Worker: Node/Chunk-`metadata` als Dict.

| Werk | Datei | Chunks (Extract) | KG |
|---|---|---|---|
| 初级讲义 | Hash `c608a514` | 125 | Interpret/text2kg |
| 星曜性质 (Fudan, ISBN 9787309094718) | `b2f52930` | 45 | Interpret/text2kg |
| 深造讲义 | `09f1ff5b` | 148 | Interpret/text2kg |
| 补注 上/中/下 | `922e` / `d35e` / `93e8` | 19 / 2 / 2 | Tabellenlastig, behalten |
| 全集 一–六 | ixinzhi-Hashes | 47, 50, 23, 65, 15, 10 | 五/六 tabellenlastig |
| 流年凶灾详析 | `eb1dd24d` | 49 | **parken** (`wave=ziwei_liunian`) |

### Welle 1b — Interpret/text2kg durch, Relink nachgezogen (2026-08-29)

Upload `--staffel welle1b`. Spark MinerU, OCR, Langdock classify/interpret/text2kg (kein Qwen, kein Auto-Synth).

| Werk | Chunks / Interps |
|---|---|
| 安星法及推断实例 | 86 |
| 王亭之谈斗数 | 32 |
| 古诀今注 八喜楼与格局 | 34 |
| 骨髓赋与女命骨髓赋 | 28 |
| 王亭之注太微赋 | 5 |

## Stand 2026-08-29 — Natal-First-Cut + KARTE-Gitter

HD-Analogie (fest): Paläste+14 Maj+身 = Ground wie Type/Strategy/Authority. 来因 = Extra-Slot wie Environment (leer ok). 辅星 = analog Channels. 四化 = analog Lines/Color. 流年 = analog Transit (eigene Welle).

**Pipeline durch:** Seed → MinerU (ch) → OCR-Wörterbuch → Langdock classify/interpret/text2kg (Staffel 1 + Welle 1b) → Unwrap/Alias → Homophone-Repair → Palast-Relink **v2** → 四化-Relink v1 → 辅星-Relink v1 → scoped Synth EN. **Kein** Full-Synth, kein Qwen, keine DE-Zeile.

| Schicht | Relink | Synth EN | Hinweis |
|---|---|---|---|
| 12 Paläste | v2 (`ziwei_natal_relink_v2`) | 命/财/官 (29. Aug) + übrige 9 + 身 (31. Aug scoped `--force`) | 来因 leer; Atome weiter EN `draft` |
| 14 Hauptsterne | v1 dann v2-Nachlauf | 14/14 (erster Cut 27. Aug, vor Palast-v2) | nicht nochmal synched nach v2 |
| 身宫 | v2 | scoped Re-Synth 31. Aug (im 10er-Batch mit den 9 Palästen) | |
| 四化 化禄权科忌 | `ziwei_mutagen_relink_v1` je 6 primary | **4/4**; 化权 Re-Synth 31. Aug | First Cut `draft` |
| 辅星 辅弼昌曲禄马魁钺 | `ziwei_minor_relink_v1` 8/8 | **8/8** | 天钺 2 primary, 左辅 3 — dünn, synched |
| 来因 `originalPalace` | — | — | extra-leer, nicht diese Welle |
| 煞 羊陀火铃空劫 | — | — | nicht diese Welle |
| 流年-Buch | Extract `wave=ziwei_liunian` | — | kein natal-text2kg |

Homophone: Catalog `tianfu` = 天福, `tianfuMaj` = 天府. Repair 190 天福→天府, 36 天月→天钺. 天府 **382** Anhänge.

Welle 1b Interps: 安星法 86 · 谈斗数 32 · 八喜楼 34 · 骨髓赋 28 · 太微赋 5 = **185**.

**KARTE 2026-08-29:** `/home/karte/ziwei` 4×4 地支-Plate + Inspector. Atome EN First Cut → `draft`, sonst `canon_fallback`. 辅星 (8) und 四化 aus iztro `mutagen`.

**KARTE 2026-08-31 (aktuell):** Dichte Platte — Kleinsterne als Position plus First-Cut-Lexikon wo Relink Primaries hat. Chrome DE (`ziwei-chrome-de.ts`). Fixture-Test **5/5**. Zusammenschau `ziwei_overlay_v3` (Lebenssatz+Belege, DE, keine EN-Buchdumps). **Langdock-URL** in `.env.development`; Key in `.env.development.local`. Paläste+身 scoped Re-Synth nach v2; 命宫/化权/天钺 nachgezogen.

**Kleinstern-Lexikon (Welle, 2026-08-31):** Relink `ic_ziwei_sha_adj_relink.py` (`ziwei_sha_adj_relink_v1`) über 六煞 + Platten-杂曜 (kein 长生-Zyklus, kein 流年). Scoped Synth EN für 20 Nodes mit primary (六煞 vollständig + u. a. 天刑/天喜/华盖/咸池). Rest ohne primary bleibt Inspector-Hinweis „nur die Position“. Nicht DE-Atome, nicht 来因.

**Zusammenschau (`ziwei_overlay_v3`):** HD-Overlay-Analog, nicht Handbuch-Generator. Erst der Lebenssatz dieser Platte, dann Belege (Helligkeit und Wandlungen mitgelesen, Beruf × Partnerschaft). Leer 命宫 → Reise/迁移 im Satz. Langdock gpt-5-mini, deutscher Chrome, **keine** EN-Buchzitate im Overlay (Inspector bleibt Lookup). Cache `user_charts.overlay` Ruleset `ziwei_overlay_v3`. GET ohne LLM-Wait (Cache oder Lage-Template). POST rechnet die Lesung. Kleinsterne in der Zusammenschau nicht erfinden. Overlay-Alltagssprache für Leser = spätere Welle.

**Nächste Ingest-Welle:** nichts Geparktes nachziehen unless asked.

## Offen / geparkt (nicht diese KARTE-Welle)

| Thema | Status | Wann |
|---|---|---|
| Overlay-Alltagssprache (Himmelsmaschine, gefallen, …) | First Cut bewusst kryptisch | eigene Produktwelle |
| DE-Atome `wordings.language=de` | Locale, nicht Extract-Rewrite | wenn alle Systeme EN-First-Cut haben |
| 来因 `originalPalace` | Extra-Slot leer (HD-Environment-Analog) | nicht ohne Quelle |
| 流年-KG / 大限-Essays | Extract `wave=ziwei_liunian` liegt; kein natal-text2kg | Timing-Welle, analog HD-Transit |
| 27 Kleinsterne ohne primary | Position-only | nicht Label-Spray |
| 安星法 Mention-Bloat | lassen; Synth liest primary | nicht reparieren |
| `verified`-Gate | UI zeigt `draft` | nicht Ziwei-First-Cut |
| 四书 Band 1, 化权-Feile 2, 天钺 EN-Pinyin | dünn / Locale | unless asked |
| 三合/飞星, Mandala, Handbuch-Generator | out of scope | — |

## Qualität / Nacharbeit (nicht 100 %)

Nicht von allein nachziehen — nur wenn gefragt. Synth liest **primary** (+ contrast wenn `interpretation_link_roles` da sind), nicht Mentions.

**Atome / Relink**

- **命宫** 2026-08-31 scoped Re-Synth: „Life Palace“ statt Soul-Palace-Branding. Atom bleibt generisch (Tianji/Taiyin als Typ-Paar, nicht diese Platte).
- **化权** 2026-08-31 scoped Re-Synth: Authority-Transform, nicht mehr Tianfu/化科-Mitte.
- **天钺** (`tianyueMin`) 2026-08-31 scoped Re-Synth: Patronage/贵人; EN sagt weiter Pinyin „Tianyue“ (Chrome = Himmelsbeil). 天月 (`tianyue`) unberührt.
- **9 Paläste + 身** 2026-08-31 scoped Re-Synth nach v2 (`ic_k2_synth_batch.py --force`, 10/10). Weiter EN First Cut / `draft`, nicht `verified`.
- Palast v2: **仆役** nur 5 Primaries (Cap 6). 辅星: **天钺** 2, **左辅** 3 — dünn, aber synchbar.
- **安星法 Mention-Bloat nicht reparieren.** Blanket label-hit + `ic_relink_strict --natal-wave` auf 安星法 abgebrochen (~48 min, 命宫 Mentions n=429). Nur 5/139 Primaries aus dem Buch. Mentions bewusst aufgebläht lassen.
- Full-Audit „liunian“ in Wordings = **False Positive** (中州 liest natal durch 大限/流年-Linse in EN-Prosa, nicht das geparkte 流年-Buch).
- Full-Audit Palast-primary `hits=0` unterzählte, weil nur Essence ohne Chunk-Text; Relink nutzt Blob+Chunk.
- Full-Audit **天钺 n=0** lag am Fetch-Set ohne `tianyueMin`; Repair hat 36 verschoben. Nächstes Audit muss `tianyueMin` listen.
- Worker `job.debug.text2kg_unmatched` ist **stale/capped** (erfundene IDs wie `ziwei.author…`). Nicht aktuelle Miss-Rate.

**Korpus**

- 八喜楼 270 S. → 34 Chunks (MinerU/Tabellen).
- 太微赋-Note 5 Chunks (11 S., **nicht** 四书 Band 1).
- 补注 / 全集 五–六 tabellenlastig.
- Fehlt, nicht Blocker: 四书 Band 1; 斗数谈星/古学拾零; 斗数四化断诀 (王亭之).
- Skip: 别序, DuXiu-安星法, 谈斗数-Stummel, 飞星/三合, 中州古籍出版社-Archäologie.

**Prozess**

- Synth: `ic_run_with_langdock.py` default Langdock-URL, mappt `SUPABASE_SECRET_KEY`, `IC_LLM_MAX_TOKENS=8000` (2000 = nur Reasoning, leerer Content), `IC_EXTRACTION_LANG=en`.
- Worker `_prioritize_synthesis_payloads` lässt primary+contrast zu, wenn Rollen existieren. Node/Chunk-`metadata` PATCH als **Dict**.
- Langdock-Loop-PID nach Welle 1b oft idle; Synth in-process via `ic_k2_synth_batch.py`.
- Label-Hit in `apply_ziwei_text2kg_ids` ist entfernt. Nicht wieder einschalten.

Skripte (`apps/web/scripts/`): `ic_ziwei_k2_catalog.py`, `ic_ziwei_ocr_dict_correct.py`, `ic_ziwei_natal_audit.py`, `ic_ziwei_natal_full_audit.py`, `ic_ziwei_natal_relink.py`, `ic_ziwei_homophone_repair.py`, `ic_ziwei_mutagen_relink.py`, `ic_ziwei_minor_relink.py`, `ic_ziwei_natal_upload.py`, `ic_relink_strict.py --natal-wave`, `ic_run_with_langdock.py` + `ic_k2_synth_batch.py`.

| Werk | Welche Datei | Rolle |
|---|---|---|
| 安星法及推断实例 (Fudan ISBN 9787309096651) | **IA** `98dd43da` (9,6 MB, 160 S., Textschicht). Datei umbenannt: `anxingfa_9787309096651_98dd43da.pdf` (Windows MAX_PATH). Nicht DuXiu `a0bed327` (Bilder). | Sternsetzung + 24 Palast-Beispiele |
| 王亭之谈斗数 | **81 S.** `8b652393`. Nicht `2df0bc80` (bricht ~S. 122 ab) | 格局论 (日月并明, 杀破狼, …) |
| 古诀今注 八喜楼与格局 | `b6d8bca0` (270 S., 圓方) | 四书 Band 3 |
| 骨髓赋与女命骨髓赋 | `4e7fc49c` (223 S.) | 四书 Band 2 |
| 王亭之注太微赋 | `d40c52a8` (11 S., WPS) | **nicht** 四书 Band 1; 全书/江湖-Note. Behalten |

### Fehlt (nicht Blocker für Welle 1)

| Werk | Status |
|---|---|
| 太微赋与形性赋 (四书 Band 1, 八喜楼-Kommentar) | nicht gefunden. 深造 + 星曜性质 + 11-S.-Note decken den Kern |
| 斗数谈星 / 古学拾零 (复旦-Liste) | nachrangig, überlappt 星曜/谈斗数 |
| 斗数四化断诀 (王亭之, nicht 曹砚明) | nicht in `neu` |

### Nicht ingestieren

别序 yuceweb `864ae41b` · 谈斗数-Stummel `2df0bc80` · DuXiu-安星法 `a0bed327` (Backup ok) · 三合/飞星 · 玄空 · 依婷/紫云/金瑞雪 · Motivations-格局 · 中州古籍出版社-Archäologie.

深造 (~158 MB) braucht Storage-Limit ≥ 250 MiB lokal (`config.toml` `file_size_limit`) oder `IC_LOCAL_PDF_PATH` auf Spark.

| Staffel | Werk | Hinweis |
|---|---|---|
| 1 Smoke | 初级讲义 + 星曜性质 | klein |
| 2 | 深造讲义 | ~158 MB Scan — eigenes Fenster, nicht skippen |
| 3 | 讲义补注 上/中/下 | |
| 4 | 全集 一–六 | nicht ein Job |
| 5 Welle 1b | 安星法 (IA) · 谈斗数 (81 S.) · 八喜楼 · 骨髓赋 · 太微赋-Kurznote | nach Staffel-1-KG |
| extract-only | 流年凶灾详析 | Jahres-Timing. MinerU jetzt ok; **kein** natal-classify/text2kg/Synth (würde 流年-Sätze an 命宫/紫微 kleben). Eigene Welle später. |

## OCR-Wörterbuch (Pflicht, nicht optional vergessen)

**Wann:** nach MinerU **aller** Natal-Werke der Staffel, **vor** text2kg / Relink. Nicht werkweise weglassen — Cover/TOC-Zierschrift trifft jedes Scan-PDF (初级 2026-08-28: `中州液` 1× vs `中州派` 15×; `人门`/`入门`). Fließtext-Kanon (Sterne/Paläste) war brauchbar; Chunk-Größe ist **nicht** die Ursache.

**Was:** deterministische Ersetzung gegen den K2-Katalog (`ic_ziwei_k2_catalog.py` + feste Phrasen: 中州派, 入门, 十四主星, Palast-/Stern-Aliase wie 事业宫↔官禄宫 nur als **Alias-Map**, nicht als Text-Rewrite ins Gegenteil). Ziel = Inbound für `IC_TEXT2KG_STRICT_ZIWEI`, analog HD `sys_term_mapping`.

**Qualität (Staffel 1, 2026-08-28):** Unwrap → Alias (`ic_ziwei_k2_catalog.normalize_ziwei_canonical_id`) → `ic_relink_strict.py` → `ic_ziwei_natal_audit.py` → `ic_ziwei_natal_relink.py`. `job.debug.text2kg_unmatched` bleibt der Altstand vor Alias (Cap 200/Job).

**Nicht:** ganzen Extract wegen Titel-OCR wiederholen; nicht Spark-Qwen; nicht VLM nur für Cover. Skript `ic_ziwei_ocr_dict_correct.py` über alle Natal-Quellen der jeweils abgeschlossenen Extract-Staffel, **vor** deren text2kg.

## Langdock (nach Extract)

`ic_start_langdock_worker.py` mit `IC_TEXT2KG_STRICT_ZIWEI=true`. Synth nur scoped, nie Full-System. Wörterbuch-Pass **davor**.
