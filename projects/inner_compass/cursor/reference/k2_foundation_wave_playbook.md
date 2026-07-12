# K2 Foundation Wave — Playbook

last_update: 2026-07-12
scope: Wiederholbares Vorgehen pro System vor Content-PDFs
in_scope: Seed → strict → Test-PDF → QA → Skalierung
out_of_scope: App-Implementierung (Phase 4)

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
| 4 | Astro, Ziwei, Jyotish | Minimal-Skeleton — Welle startet erst vor 1. PDF |

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
