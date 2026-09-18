<!--
Reality Block
last_update: 2026-09-18
scope: Phasen-Plan 13 — Astro Aszendent durch die Checkliste
in_scope: Chart-State, Astro-Hit, Facetten, Formulierer v2 auf self_identity; HandbookInput systemneutral
out_of_scope: Astro-Literaturlauf (13a), Descendant/love, Ziwei/BaZi, HD-Welle, Transit
-->

# Plan 13 — Astro Aszendent durch die Checkliste

Selbsttragend. Warum jetzt: Plan 12 hat die Leser-Kette an HD `self_identity` einmal durch. Die Checkliste ist nur systemneutral, wenn ein zweites System dieselben Schritte geht. BaZi ohne Jiazi-Interps nicht wählbar → Astro Aszendent / Haus 1.

**Matrix-Zelle:** Astro × `self_identity` (Aszendent). Literatur bleibt `[]` bis Plan 13a. Stimme: [../vertraege/handbuch_stimme.md](../vertraege/handbuch_stimme.md). Tiefe: [../vertraege/tiefe.md](../vertraege/tiefe.md).

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`.

## Festlegungen

- Hit-Rang: AC-Konjunktion (Orb ≤ 3°) → Planet in Haus 1 → AC-Zeichen. Chart-Ruler nur in `condition.ruler`.
- Facetten an Katalog-Nodes (`astro.sign.*`, `astro.angle.ascendant`, `astro.planet.*`, `astro.house.1`). Instanz-Nodes existieren nicht (71 Katalog-Nodes).
- `HandbookInput.system` `hd` | `astro`. `identityHit` = `HandbookHit` mit `facetNodeIds`.
- Formulierer v2: System-Jargonliste, Regel gegen Mechanik-Zustände (definiert/geschlossen/in Haus). Cache-Key inkl. `system`. HD-Cache v1 wird neu gefüllt.
- Astro `literature[]` = leer. Kein Hypothese-Zusatz.

## Messung (Schritt 0, 1978)

Cancer-Aszendent, keine Planeten in Haus 1, keine AC-Konjunktion → Hit `asc_sign` / `astro.ascendant.cancer`, Ruler Mond.

| Node | linked Interps | primary | gift/shadow/trap nicht-leer |
|---|---|---|---|
| `astro.sign.cancer` | 94 | 6 | 94/94/94 |
| `astro.angle.ascendant` | 48 | 6 | 48/48/48 |
| `astro.house.1` | 116 | 6 | 116/116/116 |

Abbruchkriterium (0 Füllung) nicht erfüllt.

## Nicht

Astro-Literaturlauf, Handler auf `system_id=astro`, Descendant/`love_partnership`, Ziwei/BaZi, HD-Welle, Transit, `_JOB_PRIORITY`, `db reset`.

## Ist nach Lauf

- `lib/astro/astro-mechanical-hits.ts`: Rang Konjunktion > Haus 1 > Zeichen.
- `HandbookInput` systemneutral; `hitFromHd` / `hitFromAstro`; `facetsForHit(facetNodeIds[])`.
- Formulierer `handbook-formulator-v2`; `resolveHandbookText` liest `system`. Astro-Card `translate` DE; HD-Card neu ohne „geschlossen/definiert“.
- Nachweis: `check_handbook_astro.ts` (Hit-Rang, 1978 Cancer-Facetten, DE ohne Astro-Jargon, Cache-Key ≠ HD, Cache-Hit). Regression `check_handbook_input.ts`, `check_handbook_formulator.ts`, `check_handbook_literature.ts` grün.
- Fläche: Browser-Automation in dieser Session nicht verfügbar — Reload `/home/karte/bereich/self_identity` zeigt Astro-`translate` aus Cache (`ic_handbook_texts` system=astro) und HD v2.

**Nächster Plan:** 13a — Astro-Literaturlauf (`extract_relationships` für `system_id=astro`, `condition`-Vokabular für Astro). Danach Ziwei oder HD-Welle, nicht Transit.
