<!--
Reality Block
last_update: 2026-09-17
scope: Phasen-Plan 10 — Facetten als Formulierer-Input, Schicht-2-Schema ohne Lauf
in_scope: Facetten-Leser am Mechanik-Hit, HandbookInput-Typ, Inspector EN als Rohstoff, extract_relationships Spec, Sprachregel
out_of_scope: LLM-Lauf (Plan 10a), Formulierer-Aufruf (Plan 11), DE-Gate, EN auf Handbuch-Flächen, Backfill-Wipe, Jiazi, 418, Liebe
-->

# Plan 10 — Facetten lesen, Schicht 2 spezifizieren

Selbsttragend. Warum jetzt: Plan 09 liefert den natalen Hit. Facetten (`gift`/`shadow`/`trap`) liegen im Payload und sind ungelesen. Ein DE-Gate darauf wäre fast immer stumm — Atome sind EN. Schicht 2 braucht Schema, bevor irgendwer extrahiert.

**Matrix-Zelle:** HD × Facetten gelesen (als Input, nicht Anzeige) und HD × Schicht-2-Schema. Vertrag: [../vertraege/tiefe.md](../vertraege/tiefe.md). Sprache: EN = Rohstoff, DE wird formuliert.

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`. Pfade relativ zu `apps/web/`.

## These

Facetten sind der Rohstoff des Formulierers, nicht Handbuch-Prosa. Plan 10 baut `HandbookInput` (Chart-State, Mechanik-Hit mit `condition`, Facetten EN mit Provenienz, Fallback-Karte) — befüllt, ohne LLM. Bereichsseite und Werkstatt bleiben, wie sie sind, bis Plan 11 DE schreibt.

Schicht 2 (`extract_relationships`) wird **spezifiziert**. Lauf = **Plan 10a**. Backfill bleibt `candidate`, ungelesen.

## Was das nicht ist

| Verwechslung | Klarstellung |
|---|---|
| DE-Gate auf Facetten | stumm, beweist nichts |
| EN auf Bereichsseite / Werkstatt | Inspector/Debug nur, klar als Rohstoff |
| Atome übersetzen | Formulierer Plan 11 |
| `extract_relationships` jetzt laufen | Plan 10a |
| Backfill auf `approved` | bleibt `candidate` |
| `extract_pattern_traps` / `sys_dynamics` | geparkt |
| Liebe / Jiazi / 418 | unverändert |

## Reihenfolge

1. Methodik — *(S)* Sprachregel + Leser + Input-Typ
2. Schreiben — *(D / S)* Facetten-Leser, `HandbookInput`, Assemble befüllt, keine UI-Änderung auf Fläche
3. Schicht-2-Spec — *(S)* Job-Vertrag in diesem Plan / `pipeline.md` Verweis
4. Nachweis — *(D)* Fixture 1978 + 1980: Input hat Hit + mindestens eine Facette mit `interp_id`
5. Review 10 — *(S)*

## 2) Methodik — *(S)*

- **Leser:** am Mechanik-Hit (Kanal/Tor, Aliase `channelIdAliases`). Reihenfolge `payload.facets` → `dimensions` → `process`, erster Treffer, keine Stapelung (wie Overlay `payloadSlots` in `hd-center-facets.ts` — der Overlay-Leser bleibt Zentrum-only).
- **Kein DE-Gate.** `looksLikeHandbookGerman` gilt weiter nur für bestehende Werkstatt-Seeds (Typ/Strategie), nicht für Facetten.
- **`HandbookInput`:** `chart` (State), `hits[]` mit `condition`, `facets` EN + `interp_id` / `chunk_id` wo da, `fallback` = Keil/Färbung. Gebaut und befüllt, kein Formulierer-Aufruf.
- **Sicht:** Inspector/Debug darf EN zeigen, beschriftet als Rohstoff. Bereichsseite und Werkstatt unverändert.
- **Schicht 2 Job `extract_relationships`:** Input Chunk + `elements[]`. Output je Kante `from`, `to`, `relation_type` (bestehender Enum), `metadata.condition` (`defined` / `undefined` / `hanging` / `split` / `none`), `metadata.interp_id`, `evidence.chunk_id` + Zitat, `review_status=candidate`. Eine Kante pro Beleg, keine erzwungene Gegenseitigkeit. Lesen: `amplifies` und `clashes_with` gleiches Paar → beide stumm. Backfill nicht anfassen. Worker hat den Job noch nicht (`_JOB_PRIORITY` in `ic_worker.py`).

## 3) Schreiben — *(D / S)*

- Helfer neben `hd-mechanical-hits.ts` oder `lib/ic/`: `facetsForHit(canonicalId) → { gift, shadow, trap, interpId }`.
- Assemble: Input bauen wenn `self_identity` + Hit; nicht in `composeHdVoice` / Partnership / Workshop-Felder schreiben.
- Optional: bestehendes Debug/Inspector-Feld, keine neue öffentliche Fläche.

## 4) Nachweis — *(D)*

Login-Personen 1978-11-10 Generator und 1980-11-18 Projector: Skript/Fixture zeigt Hit + Facette. Bereichsseite gleich wie nach Plan 09. Auth oft blockiert → Fixture reicht.

## Plan 10a (nicht dieser Cut)

Lauf auf HD-Chunks der Login-OS-Knoten + Mechanik-Hit, 3–5 Charts, Langdock `gpt-5.4-mini`. Eigene Datei, eigener Review.

## Erwartetes Ergebnis

`HandbookInput` existiert und ist für zwei Charts befüllt. Schema Schicht 2 liegt. Fläche unverändert. Sprachregel in `tiefe.md`.

## Nicht

LLM-Lauf, Übersetzen, EN-Handbuch, Umstellung auf EN, Merge `main`, Force-Push, `supabase db reset`, Jiazi, 418, Liebe.
