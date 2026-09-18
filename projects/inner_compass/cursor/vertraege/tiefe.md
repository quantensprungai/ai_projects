<!--
Reality Block
last_update: 2026-09-18
scope: Zielbild Tiefe — Schema, Matrix, Leser
in_scope: level_tag, condition, Provenienz, Hypothese-Flag, Cache, Bereitschafts-Matrix
out_of_scope: Jiazi, 418-Spray, Formulierer-Prompt
-->

# Vertrag: Tiefe

**Regel:** Jeder Plan nennt die Matrix-Zelle, die er füllt. „Fertig“ heißt: die Zelle ist ehrlich abgehakt, nicht dass alle 14 Systeme voll sind.

Leit-Decision: [decisions.md](../../reference/decisions.md) „Tiefe statt Färbung“. Stimme: [handbuch_stimme.md](handbuch_stimme.md). Kanten: [kanten.md](kanten.md).

## Leser-Kette (Reihenfolge)

1. Chart-State (K1, Engine) — definiert / offen / aktiviert.
2. Mechanik-Kanten mit `condition` (Familie 2 Schicht 1) — Regeln, `approved`.
3. Facetten am Element (`mechanical` / `gift` / `shadow` / `process.*`) — **Input**, nicht Handbuch-Prosa. EN = Rohstoff (Plan 10). DE erst Formulierer (Plan 11).
4. Routing `belongs_to_domain` — welche Elemente diese Bereichsseite sieht.
5. Formulierer — einmal pro Chart-Hash + Stimme-Version, gecacht. Hypothese-Flag, wenn gelesene Literatur `candidate` ist oder Schicht 3. **Ist Plan 13a:** HD + Astro `self_identity` DE v2; Astro liest `plan_13a`.
6. Färbungskarte in `handbook-voice.ts` — Fallback und Few-Shot, wenn (3) oder (5) fehlen.

## Sprache

**EN ist Rohstoff, DE wird formuliert.** DB-Atome und Facetten sind EN. Deutsch gibt es nur im HD-Keil, in den Färbungskarten und vereinzelt in `experiment_seed`.

- Nicht auf EN umstellen. Nicht übersetzen. Keine EN-Prosa auf Handbuch-Flächen (Bereichsseite, Werkstatt).
- Ein DE-Gate auf Facetten bleibt fast immer stumm und beweist nichts.
- Bis Plan 11 dürfen EN-Facetten nur als Daten / Inspector sichtbar sein, klar als Rohstoff.
- Formulierer schreibt DE aus `HandbookInput` + Stimme-Regel + gelesene Schicht-2-Belege. **Ist:** HD- und Astro-Card `translate` auf `self_identity`; Locate-Zusatz bei Hypothese nur wenn Literatur `candidate` (HD).

## Schema (eingefroren Plan 12)

Pflichtfelder der Leser-Kette. `level_tag` bleibt Nachzug beim nächsten Structure-Seed, nicht Teil der Formulierer-Pflicht.

| Feld | Wo | Pflicht |
|---|---|---|
| `condition` | Wirkungskante Metadata (Chart-State: defined/undefined, Split, hanging, none) | ja (Plan 09 / 10a) |
| Evidence | Kante: Regel+Datei **oder** Interp-ID + Chunk-Zitat | ja (Plan 09 / 10) |
| Hypothese-Flag | Formulierer-Output; Fläche: Locate-Zusatz | ja (Plan 11 / 12) |
| Cache-Key | Stimme-Version + Formulierer-Version + `system` + Chart + Hit + Facet-interp_ids + literature edgeIds | ja (Plan 13) |

`synth_draft` bleibt Lage + Hinweis, nie Handbuchabsatz ([status.md](status.md)).

## Familie 2 — drei Schichten

| Schicht | Quelle | Status | Liest das Handbuch? |
|---|---|---|---|
| 1 Mechanik | Katalog / Structure (Kanal aus Toren, Zentrum, Split, 生剋, Aspekte) | `approved` | ja auf `self_identity` HD (Plan 09, Runtime, nicht DB) |
| 2 Literatur | Chunk + Interp, eine Kante pro Beleg, mit `condition` | `approved` nach Review sonst `candidate` | **Plan 12:** `run=plan_10a` am Identitäts-Hit gelesen (Cap 6, Leseregel). Backfill weiter ungelesen |
| 3 Synthese | LLM sieht Chart + 1 + 2 | Hypothese, gecacht | Plan 11–13 (`handbook-formulator-v2`) |

**Backfill 2026-08-05:** ~13k `amplifies`/`depends_on`/`clashes_with`, alle `candidate`, ohne Interp-ID in Metadata, ohne `condition`. Skript nicht im Repo. Roh-`payload.interactions` (~64 % nicht-leer) bleibt. Nicht wipen, nicht lesen.

## System-Checkliste (eingefroren Plan 12)

Sechs Schritte, einmal an HD `self_identity` durchlaufen. Nächstes System: dieselbe Checkliste, eine Zelle.

| System × Zelle | Chart-State | Mechanik-Hit | Facetten | Routing | Literatur | Formulierer |
|---|---|---|---|---|---|---|
| HD `self_identity` | ja | Runtime Kanal/Tor + `condition` | EN im `HandbookInput` | OS approved | Plan-10a am Hit, Cap 6, `candidate`→Hypothese | v2 DE, Cache `ic_handbook_texts` |
| Astro Aszendent | ja | Runtime `asc_conjunction` / `planet_h1` / `asc_sign` | EN im `HandbookInput` (Katalog-Nodes) | Haus 1 inject | Plan-13a am Hit, Cap 6, `candidate`→Hypothese | v2 DE, Cache `system=astro`; Färbung Fallback |
| Ziwei Lebensort | ja | nein | Inspector | Palast 10 | nein | Färbung |
| BaZi Tagstamm | ja | nein | nein (Jiazi 0 Interps) | Tagstamm JSON | nein | Färbung |

Reihenfolge: eine Domäne HD → eine Domäne zweites System (**Plan 13+13a Astro**, Checkliste durch) → Breite (Bereiche, HD-Welle PHS/Quarter/Planeten/Type-4) oder Jiazi/Ziwei → Transit/ZEIT (eigene Achse, Tages-Cache-Key).

## Bereitschafts-Matrix (Ist 2026-09-18)

Zelle = Engine · Katalog · Struktur-Kanten · Routing · Atome · Facetten gelesen · Mechanik-Kanten · DE-Wordings.

| System | Engine | Katalog | Struktur | Routing | Atome | Facetten gelesen | Mechanik-Kanten | DE-Wordings |
|---|---|---|---|---|---|---|---|---|
| HD | ja | ja | `part_of` ja | OS approved; 418 candidate | Gates/Channels/Lines/OS EN | Overlay/Inspector ja; **HandbookInput** EN-Rohstoff | Runtime Schicht 1; Schicht 2: 869 `candidate` (Plan 10a), **am Identitäts-Hit gelesen** (Plan 12); Backfill weiter ungelesen | **Plan 13:** Formulierer v2 DE; Keil bleibt `name`; Hypothese-Zusatz im Locate; Jargon-Gate inkl. definiert/geschlossen |
| Astro | ja | ja (71 Nodes) | Haus-Map | Haus 1/7 inject | Natal EN-Draft | **HandbookInput** EN an Katalog (Sign/AC/Planet/Haus 1); Inspector bleibt | Runtime Hit; Schicht 2: 448 `candidate` (Plan 13a), **am AC-Hit gelesen** | **Plan 13a:** Formulierer v2 DE am AC + Literatur; Hypothese-Zusatz; Färbung Fallback |
| Ziwei | ja | ja | Palast-Map | Paläste 10/12 | Natal-Cut EN | Inspector | nein | Färbung Lebensort/Spouse |
| BaZi | ja | ja | Tagstamm-Map | Tagstamm → Identität+Liebe JSON | Day Master EN; Jiazi 0 Interps | nein | nein | Färbung Stamm |
| Jyotish | Engine ja | Katalog dünn | nein | nein | nein | nein | nein | nein |
| Maya | Engine ja | Katalog dünn | nein | nein | nein | nein | nein | nein |

**HD ungelesen (nicht verwerfen, Content-Welle nach den Systemen):** übrige `dimensions.*`, `hd.concept.open_center`, PHS/Variable-Wordings, Quarter-Atome, Planet-Beispiele, Type-4-Kanäle, `maps_to` GK 143. **Ersetzt / gestrichen:** `sys_dynamics` + `extract_processes` (Facetten `process.*`/`trap` + Schicht-2 `condition`); `generate_meta_nodes`, `tag_ic_metadata` (Stimme-Vertrag + Formulierer-Prompt). **Offen nach zwei Systemen:** `extract_pattern_traps` (Kombi-Fallen über Systeme, Tiefe 2). **`extract_relationships`:** Handler systemneutral (HD + Astro). 869 `candidate` Plan 10a am HD-Hit gelesen; 448 `candidate` Plan 13a am AC-Hit gelesen. Backfill 13k: messen, nicht lesen.

**Launch-Umfang:** vier rechnende Systeme. Jyotish/Maya/GK/Enneagramm = nach Matrix-Freeze, eigene Content-Welle.
