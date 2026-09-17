<!--
Reality Block
last_update: 2026-09-17
scope: Phasen-Plan 11 — Formulierer v0, HD self_identity, DE aus HandbookInput
in_scope: Cache-Tabelle, Langdock-Call, Stimme-Prompt, Jargon-Gate, Fläche DE, Fallback+draftHint
out_of_scope: Jiazi, 418, Backfill, Schicht-2-Kanten lesen, EN auf der Fläche, andere Bereichsseiten
-->

# Plan 11 — Formulierer v0

Selbsttragend. Warum jetzt: Plan 10 hat `HandbookInput` (EN-Rohstoff). Plan 10a hat Schicht-2-Kanten als `candidate` mit Beleg. Das Handbuch braucht DE, nicht EN-Facetten und nicht den Keil allein.

**Matrix-Zelle:** HD × DE-Wordings auf `self_identity` (Leser-Kette 5). Stimme: [../vertraege/handbuch_stimme.md](../vertraege/handbuch_stimme.md).

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`.

## Festlegungen (vor dem Bau)

- Erster Aufruf ohne Cache: **synchron** formulieren (Langdock `gpt-5.4-mini`, Timeout ~25 s), danach Cache.
- Fehler: **Färbungskarte + `draftHint`** „Dieser Satz ist noch nicht für dein Chart formuliert.“ Fehler landet im Cache (`mode='fallback'`, `error`), Retry beim nächsten Laden.
- Cache: Tabelle `ic_handbook_texts` per Migration (kein `db reset`). Unique `(person_id, domain_id, system, cache_key)`.
- **Keine Schicht-2-Kanten** in v0. `HandbookInput.literature: []` (Plan 12 füllt ihn).

## These

Einmal pro Chart-Hash + Stimme-/Formulierer-Version formulieren, cachen. Input = `HandbookInput` (Chart, Identitäts-Hit, EN-Facetten). Output = DE-Absatz für den HD-`translate`-Beat. Locate bleibt `LOCATE.hd`. Fallback bleibt Färbungskarte.

## Bau

1. Migration `20260917180000_ic_handbook_texts.sql` — RLS an; `authenticated` nur `select`; Writes über Server-Admin.
2. `lib/ic/handbook-formulator.ts` — `handbookCacheKey`, Langdock-Call, Stimme-Prompt, Jargon-Gate.
3. `lib/ic/handbook-text-store.ts` — Cache lesen, Miss formulieren, upsert `llm` oder `fallback`.
4. `domain-assemble.ts` — nur `self_identity` HD; `love`/Astro/Ziwei/BaZi unverändert.
5. View: `draftHint` auch ohne `lage`.
6. Nachweis: `scripts/check_handbook_formulator.ts`.

## Nachweis

- Drei Inputs: 1978 `59_6` emotional, 1980 `10_57` splenic, 1990 `13_33` sacral → drei verschiedene DE-Texte, kein Jargon, unterschiedliche Cache-Keys, ungültiger Key → Fehler.
- Browser: `/home/karte/bereich/self_identity` zeigt den formulierten Satz statt „In dir ist eine Verbindung fest…“.

## Nicht

Jiazi, 418, Backfill wipen/`approved`, EN-Prosa auf der Fläche, andere Lebensbereiche, Astro/Ziwei/BaZi formulieren, `_JOB_PRIORITY`, `db reset`.

## Ist nach Lauf

- Tabelle `ic_handbook_texts` lokal (Unique person/domain/system/cache_key, RLS select, Writes service_role).
- Formulierer v0 (`handbook-formulator-v0` + `handbook-voice-v1`).
- Nachweis-Skript: drei DE-Texte 1978/1980/1990 verschieden, Jargon-Gate, Cache-Hit ohne LLM, ungültiger Key → Fehler. Live-Chart 1978 `59_6` formuliert, nicht der Mechanik-Satz „In dir ist eine Verbindung fest…“.
- Fläche: HD-Card `translate` = DE; `name` Keil; `locate` unverändert; `draftHint` auch ohne `lage`.
- `literature: []` vorbereitet, leer.
- Browser-Login in der Automation hing (Auth „internet connection“ / Overlay). Cache-Zeile für Person 1978 liegt; nächster Login sollte den Satz ohne zweiten LLM-Call zeigen.

**Nächster Plan:** 12 — Schicht-2-Kanten lesen (Leseregel) und/oder Matrix einfrieren.
