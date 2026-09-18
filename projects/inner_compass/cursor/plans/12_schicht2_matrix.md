<!--
Reality Block
last_update: 2026-09-18
scope: Phasen-Plan 12 — Schicht-2 lesen + Matrix einfrieren, HD self_identity
in_scope: literature[] aus plan_10a, Leseregel, Formulierer v1, Schema-Freeze, System-Checkliste
out_of_scope: Jiazi, 418, Backfill auf approved, Astro/Ziwei/BaZi formulieren, Transit
-->

# Plan 12 — Schicht 2 lesen + Matrix einfrieren

Selbsttragend. Warum jetzt: Plan 11 formuliert DE aus Hit + Facetten. 869 Plan-10a-Kanten lagen ungelesen. Die Leser-Kette braucht den Literatur-Schritt an **einem** Element, bevor das Schema einfriert.

**Matrix-Zelle:** HD × Schicht-2-Literatur auf `self_identity` (Leser-Kette 2b / Checkliste-Schritt Literatur). Stimme: [../vertraege/handbuch_stimme.md](../vertraege/handbuch_stimme.md). Tiefe: [../vertraege/tiefe.md](../vertraege/tiefe.md).

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`.

## Festlegungen

- Quelle: `sys_kg_edges` `metadata.run=plan_10a`, `review_status=candidate`, Endpunkt = Identitäts-Hit (Kanal-Aliase) oder dessen Tore. Backfill ungelesen.
- Leseregel: `amplifies` + `clashes_with` auf demselben Paar nur dann **beide stumm**, wenn dieselbe `condition` **und** dieselbe `interp_id`. Verschiedene Bedingungen → beide, mit Bedingung. `condition` muss zum Chart passen (`defined` bei definiertem Kanal, `none` immer, `split`/`hanging`/`undefined` nur wenn State passt).
- Cap 6, Rang `produces` > `amplifies` > `clashes_with` > `modifies` > `depends_on` > `controls`, dann Zitatlänge.
- Formulierer v1 sieht `{ relationType, to, condition, quote }`. Quote = EN-Rohstoff. `hypothesis=true` bei `candidate`. Locate-Zusatz: „Teile davon sind noch Hypothese.“
- Cache-Key inkl. sortierter `edgeId`s. Version `handbook-formulator-v1`. v0-Zeilen bleiben liegen.

## Nicht

Backfill lesen, Kanten auf `approved`, Jiazi, 418, Astro/Ziwei/BaZi formulieren, andere Bereichsseiten, `_JOB_PRIORITY`, `db reset`.

## Ist nach Lauf

- `lib/ic/handbook-literature.ts`: `selectLiterature` + `loadLiteratureEdges`.
- Formulierer `handbook-formulator-v1`; Assemble füllt `literature[]`.
- Nachweis 1978 `59_6`: 6 Kanten (alle `produces`/`defined`), Mute-Regel Unit-Test, Texte mit vs. ohne Literatur verschieden, `hypothesis=true`, Jargon-Gate grün, Cache-Keys verschieden.
- Fläche: HD-Card `translate` neu (v1-Cache); Locate-Zusatz bei Hypothese. Browser-Automation in dieser Session nicht verfügbar — Nachweis über Skript + 1978-Kanten in der DB.

**Nächster Plan:** 13 — ein zweites System durch die Checkliste (Vorschlag Astro Aszendent). HD-Welle (PHS/Quarter/Planeten/Type-4) und Transit **danach**.
