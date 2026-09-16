<!--
Reality Block
last_update: 2026-09-16
scope: Zielbild Tiefe — Schema, Matrix, Leser
in_scope: level_tag, condition, Provenienz, Hypothese-Flag, Cache, Bereitschafts-Matrix
out_of_scope: Implementierung Plan 09, Jiazi, 418-Spray, Formulierer-Prompt
-->

# Vertrag: Tiefe

**Regel:** Jeder Plan nennt die Matrix-Zelle, die er füllt. „Fertig“ heißt: die Zelle ist ehrlich abgehakt, nicht dass alle 14 Systeme voll sind.

Leit-Decision: [decisions.md](../../reference/decisions.md) „Tiefe statt Färbung“. Stimme: [handbuch_stimme.md](handbuch_stimme.md). Kanten: [kanten.md](kanten.md).

## Leser-Kette (Reihenfolge)

1. Chart-State (K1, Engine) — definiert / offen / aktiviert.
2. Mechanik-Kanten mit `condition` (Familie 2 Schicht 1) — Regeln, `approved`.
3. Facetten am Element (`mechanical` / `gift` / `shadow` / `process.*`) — nur `verified` / `canon_fallback` als Prosa.
4. Routing `belongs_to_domain` — welche Elemente diese Bereichsseite sieht.
5. Formulierer — einmal pro Chart-Hash + Stimme-Version, gecacht. Hypothese-Flag, wenn Schicht 3 (Schluss, nicht Literatur).
6. Färbungskarte in `handbook-voice.ts` — Fallback und Few-Shot, wenn (3) oder (5) fehlen.

## Schema (Soll, Plan 09 legt Felder an, Plan 12 friert ein)

| Feld | Wo | Pflicht ab |
|---|---|---|
| `level_tag` 1–7 | Knoten-Metadata | nächster Structure-Seed / Plan 12 |
| `condition` | Wirkungskante Metadata (Chart-State: defined/undefined, Split, …) | Plan 09 |
| Evidence | Kante: Regel+Datei **oder** Interp-ID + Chunk-Zitat | Plan 09 / 10 |
| `confidence`, `human_review_required` | Formulierer-Output / Schicht D–E | Plan 11 |
| Hypothese-Flag | Personen-Synthese | Plan 11 |
| Cache-Key | `chart_hash` + `handbook-voice` Version | Plan 11 |

`synth_draft` bleibt Lage + Hinweis, nie Handbuchabsatz ([status.md](status.md)).

## Familie 2 — drei Schichten

| Schicht | Quelle | Status | Liest das Handbuch? |
|---|---|---|---|
| 1 Mechanik | Katalog / Structure (Kanal aus Toren, Zentrum, Split, 生剋, Aspekte) | `approved` | ja, sobald Assemble sie nimmt (Plan 09 HD) |
| 2 Literatur | Chunk + Interp, eine Kante pro Beleg, mit `condition` | `approved` nach Review sonst `candidate` | nach Plan 10 |
| 3 Synthese | LLM sieht Chart + 1 + 2 | Hypothese, gecacht | Plan 11 |

**Backfill 2026-08-05:** ~13k `amplifies`/`depends_on`/`clashes_with`, alle `candidate`, ohne Interp-ID in Metadata, ohne `condition`. Skript nicht im Repo. Roh-`payload.interactions` (~64 % nicht-leer) bleibt. Nicht wipen, nicht lesen.

## Bereitschafts-Matrix (Ist 2026-09-16)

Zelle = Engine · Katalog · Struktur-Kanten · Routing · Atome · Facetten gelesen · Mechanik-Kanten · DE-Wordings.

| System | Engine | Katalog | Struktur | Routing | Atome | Facetten gelesen | Mechanik-Kanten | DE-Wordings |
|---|---|---|---|---|---|---|---|---|
| HD | ja | ja | `part_of` ja | OS approved; 418 candidate | Gates/Channels/Lines/OS EN | Overlay/Inspector ja; Handbuch nein (nur OS) | Backfill candidate, keine `condition` | Keil + Färbung |
| Astro | ja | ja | Haus-Map | Haus 1/7 inject | Natal EN-Draft | Inspector dünn | nein | Färbung AC/DC |
| Ziwei | ja | ja | Palast-Map | Paläste 10/12 | Natal-Cut EN | Inspector | nein | Färbung Lebensort/Spouse |
| BaZi | ja | ja | Tagstamm-Map | Tagstamm → Identität+Liebe JSON | Day Master EN; Jiazi 0 Interps | nein | nein | Färbung Stamm |
| Jyotish | Engine ja | Katalog dünn | nein | nein | nein | nein | nein | nein |
| Maya | Engine ja | Katalog dünn | nein | nein | nein | nein | nein | nein |

**HD ungelesen (nicht verwerfen):** übrige `dimensions.*`, `hd.concept.open_center`, PHS/Variable-Wordings, Quarter-Atome, Planet-Beispiele, Type-4-Kanäle, `maps_to` GK 143. **Nie gebaut:** `extract_relationships`, `sys_dynamics` (0 Zeilen), `extract_pattern_traps`, `generate_meta_nodes`, `tag_ic_metadata`. Pro Zelle später: bauen oder parken.

**Launch-Umfang:** vier rechnende Systeme. Jyotish/Maya/GK/Enneagramm = nach Matrix-Freeze, eigene Content-Welle.
