<!--
Reality Block
last_update: 2026-09-18
scope: Phasen-Plan 13a — Astro Schicht-2-Literaturlauf und Lesen am AC-Hit
in_scope: extract_relationships system_id=astro, Astro-condition-Vokabular, Leser systemneutral, 1978 + bis zu 2 Charts, Hypothese auf der Astro-Card
out_of_scope: Jiazi, HD-Welle, Transit, Descendant/Liebe, andere Bereichsseiten, Backfill auf approved, _JOB_PRIORITY dauerhaft, db reset
-->

# Plan 13a — Astro Literatur

Folgt auf [Plan 13](13_zweites_system.md). Warum jetzt: Die Astro-Kette auf `self_identity` formuliert aus Hit + Facetten, `literature[]` ist leer. `_handle_extract_relationships` wirft bei `system_id != hd`. Damit fehlt Astro die letzte Zelle der Checkliste, die HD in Plan 10a/12 bekommen hat.

**Matrix-Zelle:** Astro × Schicht-2-Literaturkanten (`candidate`, `condition` + Interp-ID) + Leser am AC-Hit. Vertrag: [../vertraege/tiefe.md](../vertraege/tiefe.md). Spec: [../pipeline.md](../pipeline.md) `extract_relationships`.

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`.

## Ausgangslage (gemessen 2026-09-18)

- 71 Astro-Katalog-Nodes, alle mit 6 `primary`-Rollen. Interps: Planeten 345–430, Häuser 111–158, `astro.house.1` 116, `astro.sign.cancer` s. Schritt 0.
- 148 Astro-Kanten in `sys_kg_edges`, alle `approved`, ohne `metadata.run` — Backfill/Seed. 0 Kanten mit `condition` + `interp_id`. Leser liest davon nichts (Filter `run`).
- 1978-Hit: `astro.ascendant.cancer`, `kind=asc_sign`, `facetNodeIds=[astro.sign.cancer, astro.angle.ascendant]`, `condition.ruler=moon`, keine Haus-1-Planeten.
- Worker-Handler ist HD-only in drei Stellen: Guard `system_id != "hd"`, System-Prompt (HD-ID-Whitelist), `_rel_element_canonicals` → `_element_spec_to_canonical_id("hd", …)`, `_REL_CONDITIONS` = HD-Zustände.
- Leser `loadLiteratureEdges(db, hit: MechanicalHdHit, chart)` — Typ HD, Canonicals via Kanal/Tor-Aliase, `conditionMatchesChart` kennt defined/hanging/split/undefined.

## These

Eine Kante pro Beleg, Astro-IDs aus dem Katalog, `condition` beschreibt was die Passage voraussetzt und ist am Runtime-Hit prüfbar. Sonst wie 10a: `candidate`, `metadata.run=plan_13a`, nicht der Backfill, nicht die Fläche.

## Entscheidungen (vor dem Bau festzulegen, Review prüft)

**condition-Vokabular Astro** (ersetzt defined/undefined/hanging/split):

| condition | Passage setzt voraus | Leser: wahr wenn |
|---|---|---|
| `angular` | Element steht an einer Achse (AC/MC/DC/IC) | immer am Identity-Hit (alle drei Hit-Arten sind AC-nah) |
| `placement` | Planet in Zeichen/Haus | Kante berührt ein `facetNodeIds`-Element des Hits |
| `rulership` | Herrscher-Beziehung | Kante berührt `astro.planet.<condition.ruler>` |
| `aspect` | Kontakt zweier Planeten | `hit.kind === 'asc_conjunction'` |
| `none` | nichts | immer |

Nicht: Sect-, Dignitäts-, Transit-Bedingungen. Kommt später, wenn ein Hit sie testen kann.

**Scope-Nodes 1978:** `astro.sign.cancer`, `astro.angle.ascendant`, `astro.house.1`, `astro.planet.moon`. Cap 15 Chunks/Node → ≤ 60 Chunks, ~180 LLM-Calls wie 10a.

**Charts:** 1978 (`user_charts`) verbindlich. 1980 Berlin / 1990 Berlin nur, wenn ein Astro-Chart ohne Handarbeit berechenbar ist (Astro-Service oder `parseStoredAstroChart` auf vorhandenen Daten). Sonst 1 Chart, und das steht so im Ist.

**Leser-Mute** bleibt: `amplifies` + `clashes_with` gleiches Paar, gleiche `condition` + `interp_id` → beide stumm. Cap 6. Rang produces → amplifies → clashes_with → modifies → depends_on → controls.

## Reihenfolge

0. **Messen:** `astro.sign.cancer` / `astro.angle.ascendant` / `astro.planet.moon` Interp-Zahl + `primary`. `payload.elements[]`-Format eines Astro-Interps (hat es `canonical_id` oder `element_type`/`element_id`?). Abbruch, wenn < 5 `primary`-Chunks je Scope-Node — dann Plan anpassen, nicht raten. — *(D)*
1. **Worker:** `_handle_extract_relationships` systemneutral. `_REL_SYSTEM_PROFILES = {hd: {conditions, id_regex, prompt_hint}, astro: {…}}`. Guard: unbekanntes `system_id` → Fehler. `_rel_element_canonicals(payload, system_id)`. `_REL_RUN` aus `debug.run` (Default `plan_10a`, Lauf setzt `plan_13a`). HD-Pfad byte-gleich (Dry-Run 1978 HD vor/nach vergleichen). — *(D)*
2. **Dry-Run** `system_id=astro` 1978: Units > 0, Stub-Kante schreibt nicht, Log zeigt 4 Nodes. — *(D)*
3. **Lauf:** Job `extract_relationships` mit `debug={system_id:'astro', run:'plan_13a', chart_label:'1978-11-10 astro', canonical_ids:[4 Nodes], conditions:{}}`, `IC_WORKER_JOB_TYPES=extract_relationships`, Langdock `gpt-5.4-mini`. Danach optional 1–2 weitere Charts. — *(D)*
4. **Stichprobe SQL:** Bestand `run=plan_13a` nach `relation_type` / `condition`; fehlende `condition`/`interp_id`/`chunk_id`/Zitat = 0; 10 Zitate gegen Chunk; IDs alle im Katalog (kein `astro.placement.*`, kein erfundenes Haus). Paare `amplifies`+`clashes_with` zählen. — *(D)*
5. **Leser:** `loadLiteratureEdges(db, hit: HandbookHit, system, chart)`. Canonicals: HD wie bisher (Aliase + Tore), Astro = `facetNodeIds` + `astro.planet.<ruler>`. `conditionMatchesChart` pro System (Tabelle oben). `LITERATURE_RUN` → `LITERATURE_RUNS = {hd:'plan_10a', astro:'plan_13a'}`. — *(D)*
6. **Assemble:** `domain-assemble.ts` lädt Literatur für den Astro-Hit, `astroHandbookInput.literature` gefüllt. Hypothese-Zusatz erscheint auf der Astro-Card, Cache-Key kippt durch Edge-IDs von selbst. Formulierer unverändert (v2). — *(D)*
7. **Proof:** `check_handbook_astro.ts` erweitern — 1978 ≥ 1 Literatur-Kante, alle `candidate`, `hypothesis === true`, Text ohne Astro-Jargon, Cache-Key ≠ ohne Literatur. Unit: `conditionMatchesChart` Astro-Tabelle, Mute, Cap. Regression `check_handbook_formulator.ts`, `check_handbook_literature.ts`, `check_handbook_input.ts` grün. UI `self_identity`: Astro-Card zeigt formulierten Text + „Teile davon sind noch Hypothese.“, HD-Card unverändert. — *(D)*
8. **Docs + Review 13a:** Ist hier, `tiefe.md` Matrix Astro-Literatur, `pipeline.md` `extract_relationships` systemneutral, `roadmap.md` 13a zu + nächster Schnitt, `handover.md`, `decisions.md` Review 13a. Commits beide Repos. — *(S)*

## Abbruch / Rückweg

- Schritt 0 unter Schwelle → Plan-Ist „nicht gebaut, weil …“, Roadmap-Schnitt neu bewerten (Jiazi oder Descendant).
- Lauf schreibt > 30 % Kanten mit IDs außerhalb des Katalogs → Prompt nachschärfen, Kanten des Laufs per `run=plan_13a` löschen, erneut. Kein Wipe außerhalb `run=plan_13a`.
- Leser-Umbau bricht HD-Regression → HD-Pfad als eigene Funktion lassen, Astro parallel. Nicht generisch erzwingen.

## Nicht

Descendant/Liebe, Sect/Dignität als `condition`, Jiazi, HD-Welle, Transit, Backfill auf `approved`, `_JOB_PRIORITY` dauerhaft, Formulierer v3, Wipe, `db reset`, EN auf der Fläche.

## Ist (2026-09-18)

Schritt 0: `astro.sign.cancer` 94 Interps / 6 primary; `astro.angle.ascendant` 48 / 6; `astro.house.1` 116 / 6; `astro.planet.moon` 383 / 6. Abbruch nicht greifend. Erste Interps oft `elements[]` leer; Kandidaten kommen von Node-canonical + Job-Scope.

Worker `_handle_extract_relationships` systemneutral (`_REL_SYSTEM_PROFILES` hd/astro). `debug.run` (Default `plan_10a`). Interp-Fetch: Account zuerst, Lücken unscoped (Katalog-Account `5deaa894…` ≠ Personen-Account). HD-Prompt unverändert. Nicht in `_JOB_PRIORITY`.

Dry-Run 1978 astro: `nodes=4 units=59 written=56 rejected=3 llm_fail=0 dry_run=True` — keine Writes.

**Job (completed, 0 LLM-Fail):** `0b12d8f7-5af8-46f1-a53d-1733eea1505a` 1978 astro — 59 Chunks, written 448, skipped 36, rejected 46. Langdock `gpt-5.4-mini`.

**Bestand `metadata.run=plan_13a`:** 448 Kanten, alle `candidate`. `controls` 132, `amplifies` 107, `depends_on` 89, `clashes_with` 70, `modifies` 25, `produces` 25. `condition`: none 132, placement 85, rulership 83, aspect 75, angular 73. Fehlende `condition` / `interp_id` / `chunk_id` / Zitat: 0. IDs außerhalb Astro-Katalog / `astro.placement.*`: 0. `amplifies`+`clashes_with` gleiches Paar+condition+interp: 2 (Leser stumm). Stichprobe 10: 10/10 Zitate wörtlich im Chunk.

Nur 1 Astro-Chart in `user_charts` — kein 1980/1990-Lauf.

Leser `loadLiteratureEdges(hit, chart, system)`. 1978 AC-Hit: 6 Kanten (Cap), alle `candidate`, Formulierer `hypothesis=true`, Cache-Key ≠ ohne Literatur. `applyFormulated` hängt „Teile davon sind noch Hypothese.“ an Locate. Proof `check_handbook_astro.ts` + Regression Formulierer / Literatur / Input grün. Browser-Login in Automation nicht verifiziert.
