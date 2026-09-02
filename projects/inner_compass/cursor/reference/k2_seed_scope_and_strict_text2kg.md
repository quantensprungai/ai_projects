# K2-Seed — Scope, Lücken, strict text2kg

last_update: 2026-09-02
scope: Inner Compass — wann Seed vollständig sein muss, was fehlt, strict mode
in_scope: BaZi/HD/Ziwei/Astro Seed-Gaps, Pipeline-Regeln, text2kg_unmatched Audit
out_of_scope: Vollimplementierung aller Seeds (→ deep_structure_plan.md, ic_seed_structure.py)

## Kernregel (aus S5d gelernt)

**Reihenfolge pro System-Welle — nicht verhandelbar:**

1. **K2-Seed** in DB (`ic_seed_structure.py` aus `system_structure/*_catalog_v0.json`)
2. **Term-Mapping** (Seed-Begriffe + Entity-Aliases)
3. **PDF / Content-Pipeline** (extract → interpret → text2kg → synthesize)
4. **Qualitäts-Gate** (Inventur, Stichproben)

Ohne Schritt 1 erfindet text2kg Nodes → Wildwuchs (BaZi: 460 statt 37).

Literatur-PDFs liefern **K3/K4** (Interpretation + Synthese), **nicht** neue K2-Atomtypen — außer der Katalog sieht sie vor und sie werden bewusst geseedet.

## Warum nur „ein Teil“ geseedet ist?

`ic_seed_structure.py` (Phase 0/S4) seedete ein **Minimal-K2-Skeleton** für Pipeline-Tests — nicht den vollen Deep-Structure-Baum.

| System | In DB (Minimal) | Katalog/Plan (Ziel) | Quelle |
|--------|-----------------|---------------------|--------|
| **HD** | ~810 Seed-Nodes, Katalog **195/195** | 195 Katalog + Crosses/Lines | `ic_hd_k2_catalog.py`, `ic_hd_wildwuchs_cleanup.py` |
| **BaZi** | **97** (Kern 37 + 60 Jiazi, 2026-07-11) | **~130** Deep (Hidden Stems, Interaktionen, …) | `bazi_catalog_v0.json`, Whitelist: `ic_bazi_k2_catalog.py` |
| **Astro** | Katalog-Typen (~71) | ~71 Typen; Instanzen runtime | `astro_catalog_v0.json`, Whitelist: `ic_astro_k2_catalog.py` |
| **Jyotish** | 60 Platzhalter | ~500–700 | `jyotish_catalog_v0.json` |
| **Gene Keys** | 64 | 64 ✅ | `gk_catalog_v0.json` |
| **Andere** | Skeleton | siehe `deep_structure_plan.md` | teils nur Deskriptor |

**Astro — was in DB ist:** Katalog-Typen aus `astro_catalog_v0.json` (71 Nodes). Ground-Synth 25 EN + Nachzug 16 (12 Häuser + AC/DC/IC/MC) 2026-09-02. 7 Planeten nicht re-synched. **Nicht** Chart-Instanzen (`astro.placement.*`, `astro.aspect.sun__moon__trine`). Skeleton-`astro.aspect.*` gelöscht 2026-09-01 (Alias bleibt).

**Astro — nicht seeden:** Placement × Zeichen/Haus, Körperpaar-Aspekte, Progression, Synastrie, `maps_to_element` nach `we.element.*`.

**BaZi — noch nicht geseedet (Deep-Backlog):**

| Block | Anzahl | canonical_id-Muster | Wann seeden? |
|-------|--------|----------------------|--------------|
| Hidden Stems / 藏干 | TBD | — | Deep-Structure-Backlog |
| Branch-Interaktionen (合冲刑害) | TBD | — | Deep-Structure-Backlog |
| Luck Pillars / 大运 | Konzept | `bazi.concept.*`, `bazi.element.da_yun` | Vor Da Yun-PDFs |
| Day Master / Useful God | Konzept | `bazi.concept.ri_zhu`, `yong_shen` | optional vor Fach-PDFs |

**HD — Gap-Audit (2026-07-11):** Katalog **195/195 (100 %)** · Wildwuchs Dry-Run: **237 Extras** löschbar (v. a. `hd.asset_chunk.*`) · strict: `IC_TEXT2KG_STRICT_HD=true`

**HD-Vergleich:** Gates/Channels waren geseedet **bevor** Rave I'Ching lief → sauber. BaZi Destiny Code lief **ohne** Kern-Seed → Wildwuchs → Sanierung 2026-07-10.

## strict text2kg (ab 2026-07-10)

| Env | Default | Wirkung |
|-----|---------|---------|
| `IC_TEXT2KG_STRICT` | **true** | **Kein** `created` — nur Link auf existierende Seed-Nodes (alle Systeme) |
| `IC_TEXT2KG_STRICT_BAZI` | **true** | Zusätzlich: canonical_id muss in `ic_bazi_k2_catalog.BAZI_K2_STRICT_IDS` (Kern + 60 Jiazi) |
| `IC_TEXT2KG_STRICT_HD` | **true** | Whitelist + Aliase via `ic_hd_k2_catalog.py` |
| `IC_TEXT2KG_STRICT_ZIWEI` | **true** | Whitelist via `ic_ziwei_k2_catalog.py` (Paläste, Sterne, Stems/Branches, …). Decision 2026-08-27. |
| `IC_TEXT2KG_STRICT_ASTRO` | **true** | Typ-Whitelist via `ic_astro_k2_catalog.py`. `astro.aspect.*` → `aspect_type`; Placement/Paar-Aspekt reject. Decision 2026-09-01. |

**Seed-Regel (2026-07-11):** `ic_seed_structure.py` erhält bei Re-Seed `interpretation_ids`, `chunk_ids` und `canonical_description` — Upsert überschreibt K3/K4 nicht mehr.

**Audit:** text2kg schreibt `debug.text2kg_unmatched[]` auf den Job (max 200 Einträge):

- `not_in_bazi_k2_whitelist` — LLM/Resolver fand ID außerhalb K2-Kern
- `no_seed_node` — ID ok, aber Node fehlt in DB → **Seed-Lücke**
- `unresolved` — keine canonical_id auflösbar

→ Regelmäßig prüfen: häufige `no_seed_node`-Einträge = **Seed nachziehen**, nicht PDF nochmal laufen lassen.

## Nächste PDFs (z. B. Jia-spezifisch)

- **K2:** unverändert (`bazi.stem.jia` existiert bereits)
- **K3:** neue Interpretationen → mehr `interpretation_ids` auf demselben Node
- **K4:** Re-Synthese nur für betroffene Nodes (`ic_s5d_bazi_synth_batch.py`)
- **Kein** neuer Struktur-Wildwuchs bei strict mode an

## Offene Implementierung

- [x] `ic_seed_structure.py`: BaZi **60 Jiazi** aus `bazi_catalog_v0.json` (2026-07-11)
- [x] `ic_hd_seed_gap_audit.py` — Katalog vs. DB
- [x] `ic_hd_k2_catalog.py` — Aliase + strict Whitelist (2026-07-11)
- [x] HD Seed: Katalog-IDs (`*_def`, awareness_stream, authorities aus Katalog)
- [x] HD Wildwuchs-Cleanup: **260 Extras** gelöscht (2026-07-11)
- [x] `ic_gk_seed_gap_audit.py` — minimal 64/64 ✅
- [x] `ic_k2_synth_batch.py` — generische Re-Synthese
- [x] `ic_text2kg_unmatched_report.py` — Seed-Backlog aus Jobs
- [x] Seed: Metadata-Erhalt bei Re-Seed (interpretation_ids)
- [x] **Sanierung 2026-07-12** (Re-Seed hatte K3/K4-Metadata überschrieben):
  - `ic_relink_strict.py` (generisch) — HD 136+542 Links wiederhergestellt
  - `ic_restore_desc_from_wordings.py` — 32 BaZi + 105 HD Descriptions aus `sys_synthesis_wordings` (ohne LLM)
  - `ic_hd_alias_remap.py` — 8 Alias-Nodes remapped (`g_center`→`g`, `outer`→`mental`, …), 10 gelöscht
  - `ic_gk_wildwuchs_cleanup.py` — 167 `genekeys.asset_chunk.*` gelöscht
  - `ic_k2_state_audit.py` — One-Shot-Audit (Nodes/Interps/Synthese/Jobs)
  - 3 Zombie-Jobs geschlossen (synthesize_node queued/running)
- [x] `ic_ziwei_k2_catalog.py` + Seed `build_ziwei` + `IC_TEXT2KG_STRICT_ZIWEI` (Decision 2026-08-27)
- [x] `ic_astro_k2_catalog.py` + Seed `build_astro` aus Katalog + `IC_TEXT2KG_STRICT_ASTRO` (Decision 2026-09-01)

→ Master-Backlog: `reference/deep_structure_plan.md`
