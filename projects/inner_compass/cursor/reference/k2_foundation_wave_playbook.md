# K2 Foundation Wave — Playbook

last_update: 2026-08-29
scope: Wiederholbares Vorgehen pro System (K2-Welle + Literatur)
in_scope: Seed → strict → Extract → Relink → scoped Synth; Schienen vs. System-Knöpfe (HD/BaZi/Ziwei)
out_of_scope: App-Implementierung (Phase 4); systemeigene Runbooks ersetzen

## Welle-Standard 2026-08-29 (HD + BaZi + Ziwei)

Ein Ablauf, **Knöpfe pro System**. Kein drittes Parallel-Dokument — Ziwei-Details bleiben im Natal-Runbook, HD-Canon in `synthesis_canon_first.md`, BaZi-Wildwuchs in `s5d_pipeline_learnings.md`.

### Schienen (jedes System)

1. **Karte vor Literatur.** Ground / Extra / Mechanik / Timing analog mappen (HD Type↔Ziwei Palast+Maj; Environment↔来因 extra-leer ok; Channels↔辅星; Lines↔四化; Transit↔流年). Timing-Werke **parken**, nicht in natal-text2kg.
2. **Seed vor PDF.** Ohne Seed erfindet text2kg Nodes (BaZi 460 statt 37). `ic_seed_structure.py --system {id}` zuerst.
3. **Strict + Whitelist.** `IC_TEXT2KG_STRICT=true` + `IC_TEXT2KG_STRICT_{SYSTEM}`. 0 neue Nodes. Alias/Homophone im Katalog, nicht im LLM (`normalize_*`, 天府≠天福).
4. **Spark nur MinerU.** Interpret/text2kg/Synth = **Langdock**. Kein Qwen, kein `IC_LLM_URL=:30001`, kein I-Ching-Chunk-Profil auf fremde PDFs.
5. **Reihenfolge fest:** Extract → (OCR/Term-Dict wenn Skript) → classify → interpret → text2kg → Unwrap/Alias → **Relink `link_role`** → **scoped Synth**. `IC_TEXT2KG_AUTO_SYNTH=false`. Nie Full-Synth.
6. **Relink ≠ text2kg.** text2kg hängt nur an. Relink setzt primary/contrast/mention. Synth liest primary (+ contrast wenn Rollen da). **Mentions nicht „reparieren“.** Kein Label-Spray / Blanket-Keyword-Attach (安星法-Hänger).
7. **Lexikon → Überblick → Spezial.** Re-Synth nur `--only-id` der betroffenen Schicht. Token-Budget für Reasoning-Modelle hoch genug (`IC_LLM_MAX_TOKENS=8000`; 2000 = leerer Content).
8. **First Cut ≠ verified.** UI liest Atom/`primary`, keinen Interp-Dump. `job.debug.text2kg_unmatched` ist oft stale/capped — nicht als Miss-Rate lesen.
9. **Eine Tradition zuerst.** Schulen nicht in denselben Wording-Topf. Zwischensprache der Atome ist eine Decision (Ziwei = en; DE = zweite `wordings.language`-Zeile, nicht Extract-Rewrite).
10. **Metadata erhalten.** Re-Seed darf `interpretation_ids` nicht wischen. Node/Chunk-`metadata` PATCH als Dict, nicht `json.dumps`.

### Knöpfe (pro System, nicht raten)

| Knopf | HD | Ziwei | nächstes System |
|---|---|---|---|
| MinerU-Lang / Profil | latin, ggf. `rave_iching_gates` | `ch`, **kein** I-Ching-Profil | aus TOC/Skript |
| Whitelist-Modul | `ic_hd_k2_catalog.py` | `ic_ziwei_k2_catalog.py` | `ic_{sys}_k2_catalog.py` |
| OCR/Term | `sys_term_mapping` | `ic_ziwei_ocr_dict_correct.py` vor text2kg | wenn Scan/Skript das verlangt |
| Relink-Heuristik | Facet/Defined-C/Channel-Skripte | Palast-v2 (voller Name+宫), Sibling-Cap, 流日→mention | neu schreiben, nicht HD kopieren |
| Extra-Slot | Environment | 来因 — leer ok | bewusst leer lassen dürfen |
| Geparkt | Transit-UI | 流年-Buch (`wave=…_liunian`) | Timing-Band analog |
| Canon | `hd_auth_def_canon_v1.yaml` | First-Cut EN, kein YAML | erst wenn Mechanik-Wahrheit ≠ Literatur |

### Fallen (nicht wiederholen)

| Falle | Wo gelernt |
|---|---|
| PDF vor Seed | BaZi S5d |
| Auto-Synth / Full-Synth | HD + Ziwei |
| Spark-Qwen als Default | Ziwei-Decision |
| Alias/Homophone dem LLM überlassen | Ziwei 天府/天福, BaZi 戊/午 |
| Mentions als Qualitätsproblem behandeln | Ziwei 安星法 |
| Timing-Buch in Natal-Atome | 流年 / HD-Transit-Analog |
| Synth-Budget zu klein (Reasoning) | Ziwei 2000→8000 |
| Audit nur Essence, ohne Chunk-Text | Ziwei Palast `hits=0` |
| UI-Gitter vor Atomen | Decision 2026-08-27 |

### Abschluss einer Welle

Nicht „jede Interp-Node hat Synth“ (Playbook Juli — zu grob). Sondern: Ground-Schicht scoped synched; Extra/Timing dokumentiert leer oder geparkt; Qualitätsschulden im **System-Runbook**; `ic_k2_state_audit.py` auf Wildwuchs=0. Product-Schritt (KARTE) ist ein anderes Paket.

## Wann anwenden?

**Vor jedem Content-Lauf** (PDF-Upload + Pipeline) für ein `system_id`.

Nicht: alle 14 Systeme gleichzeitig auf Deep-100% seeden.  
Sondern: **Wellen** — pro System nur die K2-Tiefe, die die **nächsten geplanten PDFs** brauchen.

## Ablauf (5 Schritte)

### 1. Katalog-Inventur

- Quelle: `projects/inner_compass/system_structure/{system}_catalog_v0.json`
- Skript: `ic_{system}_seed_gap_audit.py` (HD: `ic_hd_seed_gap_audit.py`)
- Output: `missing in DB` vs. Katalog

### 2. Seed

```bash
python ic_seed_structure.py --system {system_id}
```

- Idempotent (upsert auf `account_id,node_key`)
- BaZi Kern: 37 Nodes · BaZi + Jiazi: 97 Nodes

### 3. strict text2kg aktiv

| Env | Default |
|-----|---------|
| `IC_TEXT2KG_STRICT` | true — kein Node-Create |
| `IC_TEXT2KG_STRICT_BAZI` | true — Whitelist `ic_bazi_k2_catalog.py` |
| `IC_TEXT2KG_STRICT_HD` | true — Whitelist `ic_hd_k2_catalog.py` |
| `IC_SYNTHESIS_MAX_INTERPS` | 8 — max. Interps im LLM-Prompt |
| `IC_SYNTHESIS_LOAD_INTERPS` | 15 — max. geladene Interps |

Nach text2kg: `debug.text2kg_unmatched[]` im Job prüfen → Seed-Backlog.

### 4. Ein Test-PDF (QA-Gate)

1. Upload + Pipeline E2E
2. Inventur (Wildwuchs = 0)
3. **10–15 Synthesis-Stichproben** lesen — spezifisch genug?
4. Coverage: welche Katalog-Nodes haben `interpretation_ids`?

### 5. Skalierung

- Weitere PDFs (Überblick + fokussiert)
- Re-Synthese nur betroffene Nodes (`ic_k2_synth_batch.py --system bazi --force --top-by-interps 10`)
- Kein neuer Seed nötig, solange PDFs bestehende Atomtypen füttern

### 6. Abschluss-Gate (Pflicht)

```bash
python ic_k2_state_audit.py
```

- **0 offene Jobs** (queued/running)
- **0 Wildwuchs** (Extras vs. Whitelist/Katalog)
- **Jede Interp-Node hat Synthese** (oder bewusst ausgenommen dokumentieren)
- Interp-Count **darf nach Seed nicht sinken** (Metadata-Erhalt prüfen)

→ Sanierungs-Runbook bei Verstoß: `reference/k2_sanierung_learnings.md`

## K1 vs. K2 — was wird geseedet?

| Schicht | Was | Wo | KG-Node? |
|---------|-----|-----|----------|
| **K1** | Chart-Berechnung (Positionen, Pillars, Gates zur Laufzeit) | `@ic/engines`, HD/Jyotish-Services | **Nein** (Ergebnis am Chart) |
| **K2** | Struktur-Katalog (atomare Bedeutungstypen) | `ic_seed_structure.py` → `sys_kg_nodes` | **Ja** |
| **K3** | Interpretationen aus Literatur | `sys_interpretations` | verlinkt auf K2 |
| **K4** | Synthese | `canonical_description`, wordings | auf K2-Node |

**K2-Nodes kommen aus Katalogen/Engines-Konstanten, nicht aus PDFs.**  
Engines liefern K1 zur Laufzeit; ihre **Konstanten** (64 Gates, 10 Stems, …) fließen in K2-Kataloge → Seed.

## Synthesis-Qualität (was „bessere Logik“ meint)

Aktuell: bis zu 20 Interpretationen → LLM → ein Text. Bei 100+ heterogenen Interps wird das **generisch**.

Verbesserungen (Backlog, nicht implementiert):

1. **Cap + Priorität** — `IC_SYNTHESIS_MAX_INTERPS=8`, `IC_SYNTHESIS_LOAD_INTERPS=15`; Relevanz-Score nach Node-Key ✅ (2026-07-11)
2. **Entity-Prompt** — „Describe only `{node_key}`“ ✅ (2026-07-11)
4. **`tradition`-Tag** — pro Interpretation Schule/Autor → separate Synthesis-Linsen
5. **Re-Synth nach fokussiertem PDF** — gezielt `--only-id` statt Full-Graph

## System-Priorität K2-Foundation

| Prio | System | Stand (2026-07-12, alle Wellen sauber) |
|------|--------|------------------------|
| 1 | BaZi | ✅ 97 Nodes · 34 Interp-Nodes · **37 Synthese** · Wildwuchs 0 |
| 2 | HD | ✅ 777 Nodes · Katalog 195/195 · **114/114 Interp-Nodes mit Synthese** · Wildwuchs 0 |
| 3 | Gene Keys | ✅ 64 Nodes · **64/64 Interps + Synthese** · Wildwuchs 0 |
| 4 | Ziwei | Natal-First-Cut + KARTE-Gitter 2026-08-29 — Runbook `reference/ziwei_natal_ingest_runbook.md`. Plate-Contract 6/6. Nicht Overlay/DE/来因/煞 unless asked |
| 5 | Astro, Jyotish | Minimal-Skeleton — Welle erst vor 1. PDF, nach diesem Playbook |

**Qualitäts-Gate-Status:** Alle drei aktiven Systeme haben 0 offene Jobs, 0 Wildwuchs, jede Interp-Node hat Synthese (`ic_k2_state_audit.py`).

## Gelernte Regel (2026-07-12)

**Re-Seed ist erst seit dem Metadata-Erhalt-Fix idempotent.** Vorher hat jeder `ic_seed_structure.py`-Lauf `interpretation_ids` + `canonical_description` überschrieben (BaZi + HD betroffen, beides saniert). Nach jedem Seed: `ic_k2_state_audit.py` laufen lassen.

## Werk-Reihenfolge pro System (Strategie, 2026-07-12)

Empirischer Befund aus S5b vs. S5d:

| Werk-Typ | Beispiel | Effekt auf KG |
|----------|----------|---------------|
| **Referenz/Lexikon** (1 Entität = 1 Abschnitt) | Rave I'Ching (Gates) | Saubere 1:1-Links, spezifische Synthese ✅ |
| **Überblick** (Konzepte quer durchs Buch) | Destiny Code (BaZi) | 100+ heterogene Interps auf Kern-Nodes → generische Synthese ⚠️ |
| **Spezialwerk** (ein Thema tief) | z. B. Da-Yun-Buch | Tiefe auf wenigen Nodes, braucht passende K2-Nodes vorab |

**Empfohlene Reihenfolge pro System:**

1. **Referenz-/Lexikonwerk zuerst** → definiert die Node-Essenz (beste Interp-Qualität pro Node)
2. **Überblickswerk danach** → Kontext/Verbindungen; Synthese-Cap + Relevanz-Score fangen die Heterogenität ab
3. **Spezialwerke zuletzt** → gezielte Re-Synthese nur betroffener Nodes (`--only-id`)

**Cap dynamisch?** Ja, per Werk-Typ steuern (kein Code-Automatismus nötig):
- Referenzwerk: Cap irrelevant (wenige, präzise Interps pro Node)
- Überblickswerk: `IC_SYNTHESIS_MAX_INTERPS=8` (Default) + Relevanz-Score
- Nach Spezialwerk: Re-Synth mit `--only-id`, ggf. Cap höher (10–12), weil Interps homogener

## Best-Practice-Abgleich (GraphRAG/Ontology-Research, 2026-07)

Unser Vorgehen deckt sich mit dem Stand der Technik (ontology-guided KG construction):

| Best Practice (Literatur) | Unser Äquivalent |
|---------------------------|------------------|
| Ontology-first, dann Extraktion | **K2-Seed vor PDF** (S5d-Lehre) |
| Post-hoc Type-Checking gegen Schema | **strict text2kg + Whitelists** |
| Entity Resolution mit Alias-Registry | **`*_CANONICAL_ALIASES` + normalize-Funktionen** |
| Schema iterativ erweitern statt Big-Bang | **Wellen-Modell** |
| Hierarchisches Clustering für Synthese | Backlog: cluster-then-merge (erst bei Mehrquellen nötig) |
| Periodisches Voll-Reindexing statt inkrementell | `ic_relink_strict.py` + `ic_k2_synth_batch.py --force` |

Nicht Standard bei uns (bewusst): Kein Embedding-basiertes Entity-Matching (Slugs + Aliases reichen bei geschlossenen Katalogen); Chunks liegen in `sys_source_chunks` statt als Graph-Nodes (gleicher Effekt via `chunk_ids`-Metadata).

→ Detail-Lücken: `reference/k2_seed_scope_and_strict_text2kg.md`, `reference/deep_structure_plan.md`
