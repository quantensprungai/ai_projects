<!--
Reality Block
last_update: 2026-09-19
scope: Phasen-Plan 14 — love_partnership durch die Kette für HD + Astro
in_scope: Domain-Hit-Regel HD/Astro, Formulierer v3 Label+Frage, Assemble ohne love-Guard, Proof 1978 Liebe, optional DC-Literaturlauf
out_of_scope: zwölf Domänen füllen, Ziwei/BaZi formulieren, 418-candidate, Sex-Manual, Transit, HD-Welle, Jiazi, _JOB_PRIORITY, Wipe, db reset
-->

# Plan 14 — Zweite Domäne: Liebe durch die Kette

Folgt auf [Plan 13a](13a_astro_literatur.md). Warum jetzt: Die Kette ist bis auf Hit-Wahl, Formulierer-Prompt und den `love ? null : hit`-Guard domänenneutral. Eine zweite Domäne beweist, dass jede weitere nur eine Hit-Regel pro System plus Label im Prompt kostet — bevor die Tabelle über alle zwölf gefüllt wird (Spray-Risiko, Plan 07).

**Matrix-Zelle:** HD × `love_partnership` und Astro × `love_partnership` — Hit, Facetten, Literatur (Bestand), Formulierer. Ziwei/BaZi bleiben Färbung.

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`.

## Ausgangslage (gemessen 2026-09-19)

- 1978 Astro: AC Cancer, DC Capricorn (280.67°). Ruler des DC-Zeichens: Saturn. **Keine Planeten in Haus 7.** Keine gespeicherten Aspekte zum Descendant. Erwarteter Liebe-Hit: `dsc_sign` `astro.descendant.capricorn`, `facetNodeIds=[astro.sign.capricorn, astro.angle.descendant]`, `condition.ruler=saturn`.
- KG-Nodes (Katalog-Account `5deaa894…`): `astro.angle.descendant` 24 Interps / 4 primary; `astro.house.7` 119 / 6; `astro.sign.capricorn` 96 / 6; `astro.planet.saturn` 430 / 6. `astro.descendant.capricorn` existiert nicht als KG-Node (nur Chart-Node).
- Bestand `plan_13a` an DC-Scope (nicht 0 — Lauf 13a hat über AC-Scope hinaus geschrieben): descendant 7, house.7 18, saturn 50, capricorn 8.
- 1978 HD: `hd.channel.6_59` (Katalog `59_6`). Interps 75 / 3 primary. Bestand `plan_10a`: 102 Kanten am Kanal, 14 an `hd.gate.59`, 12 an `hd.gate.6`.
- Assemble: `love ? null : hit` in `domain-assemble.ts` schaltet die Kette auf Liebe ab. Formulierer-Prompt hart „für Selbst & Identität“. Astro-Hits nur AC/Haus 1. HD-Hits nur Identitäts-Rang (G-Kanal zuerst).

## These

Jede weitere Domäne kostet eine Hit-Regel pro System + Domänen-Label im Prompt. `DOMAIN_HIT_RULES[system][domainId]` ist die Form; Identität und Liebe gefüllt, der Rest `null` (still). Literatur kein neuer Lauf, solange der Leser am Liebe-Hit Bestand trifft.

## Entscheidungen (Review prüft)

**Astro-Hit Liebe** (Spiegel von Identität an der DC/Haus-7-Achse): Planet in Haus 7 → DC-Konjunktion (Orb ≤ 3°) → DC-Zeichen. `facetNodeIds`: `[astro.planet.X, astro.house.7]` bzw. `[astro.sign.<dc>, astro.angle.descendant]`. `condition.ruler` = Herrscher des DC-Zeichens.

**HD-Hit Liebe:** Rang Kanal aus Bindungs-Liste (`59_6`, `40_37`, `19_49`, `44_26`, `32_54`, `27_50`) → Kanal an Solarplexus/Sakral → hängendes Tor aus der Liste → null (still). Liste im Plan dokumentiert, nicht aus Content abgeleitet. 1978 hat `59_6`.

**Hit-Regel-Tabelle als Form:** `DOMAIN_HIT_RULES` in je einer Datei pro System; `bestHitForDomain(hits, domainId)`. Identität = bestehende Ränge, Liebe = neu, alle anderen Domänen = `null`. Nicht füllen.

**Prompt:** `systemPrompt(system, domainId)` mit Label + Kernfrage aus `life-domains.ts`. Formulierer-Version → `v3`. Jargon-Gates unverändert.

**Literatur:** kein neuer Worker-Lauf, wenn der Leser am Liebe-Hit Bestand `plan_10a` / `plan_13a` trifft. Optionaler Schritt: Worker-Lauf Scope `astro.sign.<dc>`, `astro.angle.descendant`, `astro.house.7`, `astro.planet.<ruler>` mit `run=plan_14` — nur wenn Astro-Literatur 0 und die Card ohne Literatur dünn ist.

**Locate:** `LOCATE_LOVE.*` bleibt; Hypothese-Suffix wie bisher.

## Nicht

Zwölf Domänen jetzt, Ziwei/BaZi formulieren, 418-`candidate` einschalten, Sex-Manual, neue Werkstatt, Transit, HD-Welle, Jiazi, `_JOB_PRIORITY`, Wipe, `db reset`.

## Ist (2026-09-19)

Schritt 0: AC Cancer, DC Capricorn, Ruler Saturn. Keine Planeten in Haus 7, keine DC-Aspekte. Nodes: descendant 24/4 primary, house.7 119/6, capricorn 96/6, saturn 430/6. Bestand `plan_13a` an DC-Scope unerwartet nicht 0 (descendant 7, house.7 18, saturn 50, capricorn 8 — Spillover aus AC-Lauf). HD `6_59` / Katalog `59_6`: 75 Interps / 3 primary, `plan_10a` 102 Kanten.

Astro-Hits: `dsc_conjunction` / `planet_h7` / `dsc_sign`. `bestAstroHitForDomain`; Identity-Alias unverändert (nur AC-Kinds). HD: `bestMechanicalHitForDomain` mit Bindungs-Liste; Identität G-Kanal-Rang unverändert. Andere Domänen `null`.

Formulierer `handbook-formulator-v3`: `systemPrompt(system, domainId)` mit Label + Kernfrage. Jargon-Gates unverändert.

Assemble: `love ? null : hit` raus. Hit über Domain-Regel. Partnership-Voice bleibt Fallback. `collectAstroIds` nimmt Haus 7 + Descendant + Liebe-Hit mit.

Proof `check_handbook_love.ts`: 1978 HD `hd.channel.59_6`, Astro `dsc_sign` `astro.descendant.capricorn`. Facetten gefüllt. HD-Literatur 6, Astro-Literatur 6 (Cap), beide `hypothesis=true`. DE ohne Jargon. Cache-Key ≠ Identität. Regression Formulierer / Literatur / Input / Astro grün.

**Kein Worker-Lauf `plan_14`:** Astro-Literatur am DC-Hit = 6, Card nicht leer. Texte ziehen Saturn/Capricorn-Spillover aus 13a (u. a. praktische Fürsorge; einzelne Belege thematisch weit). Ehrlich gelesen, nicht nachgelegt.

Cache `ic_handbook_texts` 1978: `love_partnership` hd+astro v3. Identität v3-Cache neu (Formulierer-Version). UI-Route `/home/karte/bereich/love_partnership` antwortet 307 → Login; Browser-Login in Automation nicht verifiziert (wie 13a).

## Nicht (gehalten)

Zwölf Domänen gefüllt, Ziwei/BaZi formuliert, 418, Sex-Manual, Transit, HD-Welle, Jiazi, `_JOB_PRIORITY`, Wipe, `db reset`.