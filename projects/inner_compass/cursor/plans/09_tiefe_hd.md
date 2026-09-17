<!--
Reality Block
last_update: 2026-09-16
scope: Phasen-Plan 9 — HD Mechanik-Kanten mit Bedingung
in_scope: Schicht 1 Familie 2 aus hd_structure_v0, condition am Chart-State, Assemble liest Tore/Kanäle auf self_identity
out_of_scope: LLM, Backfill-Wipe, extract_relationships (Plan 10), Formulierer (Plan 11), 418, Jiazi, neue Bereichsseiten
-->

# Plan 09 — Tiefe HD: Mechanik-Kanten

Selbsttragend. Warum jetzt: Färbung ist Fallback. Tiefe 1 ohne Tore/Kanäle ist Typologie. Familie 2 braucht `condition`, bevor Literatur neu extrahiert wird.

**Matrix-Zelle:** HD × Mechanik-Kanten (und Assemble-Lesen auf `self_identity`). Vertrag: [../vertraege/tiefe.md](../vertraege/tiefe.md).

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`. Pfade relativ zu `apps/web/`.

## These

Mechanik ist deterministisch und vorgebbar. HD-Struktur sagt bereits: Kanal aus zwei Toren, Tor gehört zu Zentrum, Typ→Strategie. Was fehlt: dieselben Kanten **pro Chart** mit Zustand (definiert / offen / hängend / Split-Brücke) und ein Assemble, der Natal-Tore und -Kanäle der Domäne als Karten wählt — nicht nur `hd.type.*`.

Schicht 2 (Re-Extraktion) ist **Plan 10a**. Schema in [10_facetten_schicht2.md](10_facetten_schicht2.md).

## Was das nicht ist

| Verwechslung | Klarstellung |
|---|---|
| Backfill auf `approved` heben | bleibt `candidate` |
| `extract_relationships` | Plan 10a (Spec in 10) |
| Formulierer / DE-Atome | Plan 11 |
| 418 Domain-Candidates | unangetastet |
| Farbe/Ton/Base im Spiegel | PHS bleibt Werkstatt/geparkt |
| Alle 12 Bereiche | nur `self_identity` lesen; Liebe unverändert Färbung |

## Reihenfolge

1. Bestand — *(D)* Structure-Kanten vs. Chart-Nodes vs. Assemble-Pick
2. Methodik — *(S)* `condition`-Felder, welche Mechanik-Kanten, Ranking Tore/Kanäle
3. Schreiben — *(D / S)* Generator aus `hd_structure_v0.json` + Chart-State; Assemble-Pick
4. Browser Login-Person (1978 Generator + 1980 Projector) — *(D)*
5. Review 9 — *(S)*

## 2) Methodik — *(S)* — vor dem Bau

- **Quelle der Regeln:** Code `apps/web/lib/hd/hd-channel-centers.ts` (36 Paare). [hd_structure_v0.json](../../system_structure/hd_structure_v0.json) hat `belongs_to_center` und Channel→Circuit; die JSON-Beschreibung „channel→center_pair ×36“ ist falsch (keine solchen Kanten). Evidence = Katalogdatei. Runtime, nicht DB.
- **`condition`:** Chart-State aus `normalize-hd-chart` (defined/undefined Center, aktiviertes Tor, voller Kanal vs. hängend, Split). Ohne passenden State gilt die Kante für diese Person nicht.
- **Pro Quelle weiter max. eine Tiefe-1-Karte** plus: HD darf auf Identität **eine OS-Karte und eine Mechanik-Karte** (stärkstes aktiviertes Element in der Domäne) — sonst bleibt das Bild Typologie. Ranking: definierter Kanal vor hängendem Tor vor OS. Wenn unklar: OS behalten, Mechanik schweigt ehrlich.
- **Kein LLM.** Kein Worker-Re-Synth. Kein `supabase db reset`. Persistenz: entweder Laufzeit aus Chart+Structure (bevorzugt, keine 13k Duplikate) oder schmale `approved`-Zeilen nur für Regeltypen, nicht pro Person.
- **Bevorzugt Laufzeit:** Person-Kanten nicht in `sys_kg_edges` materialisieren, wenn sie sich aus Natal ∩ Structure ergeben. DB-Kanten bleiben Katalog/Literatur.

## 3) Schreiben — *(D / S)*

- Helfer neben `domain-assemble.ts` (oder `lib/hd/`): `mechanicalHdHits(chart) → { canonicalId, condition }[]`.
- `pickEdge` / HD-Karte auf `self_identity`: OS wie bisher **und** ein Mechanik-Hit, Stimme vorerst Fallback (Färbung/Keil) oder bestehendes DE-Keil-Wording; volle Formulierer-Prosa = Plan 11.
- Familie-2-Backfill weiter ungelesen.
- System-Chart-Assemble / Overlay nicht umbauen, außer ein klarer Shared Helper für State.

## 4) Browser — *(D)*

Login `test@makerkit.dev`. 1978-11-10 Generator und 1980-11-18 Projector: Identität zeigt neben Typ einen Satz, der von **diesem** Chart kommt (Kanal oder Tor), nicht denselben Generator-Satz für alle. Liebe unverändert. Auth-Automation oft blockiert.

## Erwartetes Ergebnis

`self_identity` HD: Typ/Strategie plus ein natales Mechanik-Element mit `condition`. Schema für Plan 10 liegt. Backfill unangetastet.

**Ist (2026-09-16):** gebaut. Runtime `hd-mechanical-hits.ts`. Stimme ein nataler Satz ohne 36er-Map. Review 9 in `decisions.md`. Fixture: Kanal 8–1 vs. hängendes Tor 1. Browser-Auth oft blockiert.

## Nicht

LLM, Jiazi, 418, Merge `main`, Force-Push, PHS-Prosa, elf Seiten.
