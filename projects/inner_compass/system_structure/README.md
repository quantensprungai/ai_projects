# system_structure

Hier liegen **Struktur-Artefakte** pro System (Kataloge, später vollständige Bäume), getrennt von den **Deskriptoren** in `../system_descriptors/`.

| Datei | Inhalt |
|-------|--------|
| `ziwei_catalog_v0.json` | **Schritt 1:** iztro — Locales, Sterne, **`heavenlyStems` / `earthlyBranches`** (冲, 命主身主, 四化, …), `schema_version` ≥ 1.1. `extract:ziwei-catalog` |
| `ziwei_structure_v0.json` | **Schritt 2:** Ebenen + Kanten inkl. **干冲/支冲**, **命主/身主→Stern**, **stem_mutagen_***, Palast-Ring, 五虎遁/五鼠遁, `life_domain_map`. `build:ziwei-structure` |
| — | **Schritt 3:** Vitest prüft `computeZiweiChart().nodes` gegen den Katalog (`ziwei-catalog-validation.test.ts`). |
| `bazi_catalog_v0.json` | **Schritt 1:** `@yhjs/bagua` + **`shensha_aux`** (驿马/天乙贵人/旺相休囚死, Spiegel `@yhjs/bazi`). `schema_version` ≥ 1.2. `extract:bazi-catalog` |
| `bazi_structure_v0.json` | **Schritt 2:** Ebenen + Kanten-Kette 年→月→日→时. Neu: `pnpm --filter @ic/engines run build:bazi-structure` |
| — | **Schritt 3 (BaZi):** `validateBaziNodesAgainstCatalog` (`bazi-catalog-validation.test.ts`). |

Siehe `cursor/engines.md` §15–16, **`reference/engine_integration_playbook.md`** (Phase-1-Ablauf; **§7** = Grenze Kit-Extraktion vs. Laufzeit, Ziwei/BaZi) und `reference/structure_descriptor_seed.md`.
