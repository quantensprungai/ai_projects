<!--
Reality Block
last_update: 2026-09-20
scope: Phasen-Plan 14b — Methodik vor Hit-Regel für love_partnership
in_scope: System-Tabelle Natal-Lagen, HD zwei Lagen, Astro Venus-Zusatz, Routing-Seed Typ/Strategie→Liebe, Literatur-Domänenfilter, Formulierer v4
out_of_scope: Composite, Familie, Transit, Sex Manual verdrahten, BG5, DreamRave, Disjunktheits-Regel, Pflicht-Hit, 418 einschalten, Ziwei/BaZi formulieren, db reset
-->

# Plan 14b — Liebe: Methodik vor Hit-Regel

Korrigiert [Plan 14](14_zweite_domaene.md). Ersetzt den verworfenen Entwurf (Pflicht-Hit, Exclude, offene Center als Ersatz-Kanal).

**Matrix-Zelle:** HD × `love_partnership` (OS-Erstlage + Bindungs-Zusatz + offene Center als Zustand) und Astro × `love_partnership` (Achse + Venus). Formulierer v4. Ziwei/BaZi bleiben Färbung.

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`.

## Befund (2026-09-20)

- Plan 14 hat die Identitäts-Form (ein mechanischer Kanal-Hit) auf Liebe kopiert. HD-Lehre für Beziehung natal ist: Typ/Strategie in Bindung (immer), Bindungsschaltung (falls definiert), offene Center als Konditionierungsfläche (Zustand). Kein Bindungskanal = gültiges Schweigen auf dieser Schicht.
- Identitätstext klang nach Liebe, weil Facetten + Literatur am selben Node gelesen wurden und die Frage im Prompt zu schwach trennt — nicht weil der Kanal doppelt ist.
- `belongs_to_domain → love_partnership` hat 9 Kanten, weil Plan 08 die Zeilen Typ/Strategie → Liebe nur in `hd_structure_v0.json` gelegt, nie geseedet hat, und die inhaltliche Aggregation Beziehungstexte nach `relationships_community` (199) gekippt hat. Pipeline-Artefakt, keine Lehre.
- Composite / Familie / Transit / Sex Manual / BG5 / DreamRave sind andere `chart_context.kind` oder S2-Werke. Heute nur Natal.

## Methodik

Gleiche Lage in zwei Bereichen ist erlaubt. Unterschiedlich sind Frage, Facetten-Auswahl und Literatur. Keine Disjunktheits-Regel. Kein Pflicht-Hit auf der Zusatzlage.

| System | Natal-Erstlage (immer da) | Zusatzlage (falls definiert) | Zustand / Bedingung | Anderer Chart-Kontext (nicht hier) | Schweigen erlaubt? |
|---|---|---|---|---|---|
| HD | Typ + Strategie in Bindung | Bindungsschaltung `59_6`, `40_37`, `19_49`, `44_26`, `32_54`, `27_50` plus hängende Bindungstore | offene Center Emotional / Sakral / G | Composite, Penta, Sex Manual | ja auf Zusatzlage |
| Astro | Haus 7 / Deszendent | Venus (Zeichen, Haus) | — | Synastrie, Transit | nein (Achse immer da) |
| Ziwei | 夫妻宫 | Sterne im Palast (nicht dieser Plan) | — | 合盤 | nein |
| BaZi | Tagstamm in Beziehung (Plan 08) | Spouse-Star / Ehepalast später | — | Branch-Compare | ja |

Plan 15 liest diese Tabelle pro Domäne, bevor eine Hit-Regel gebaut wird.

## Messung

Vorher (2026-09-20, vor Code):

| Check | Ist |
|---|---|
| Fixtures | 6 HD + 4 Astro in `apps/web/scripts/fixtures/handbook-charts.ts` |
| `hd.type.*` / `hd.strategy.*` Interps | Generator 83, Projector 63, Manifestor 61, Reflector 28, MG 17; Strategie wait_to_respond 97, inform 86; Invitation/Lunar 0 über `interpretation_ids` |
| `plan_10a` an OS-Nodes | wait_to_respond 157, generator 121, projector 110, invitation 72, MG 69, manifestor 22, reflector 17; inform/lunar 0 |
| `payload.facets.open_expression` / `mind_when_open` an `hd.center.*` | 0 (Packer liest weiter Essays/`expression`) |
| `belongs_to_domain` Typ/Strategie/Venus → Liebe | 0 (JSON Plan 08 ja, DB nein) |

Nach Seed und Code: siehe `## Ist`.

## Nicht

Composite / Familie / Transit, Sex Manual verdrahten, BG5, DreamRave, Disjunktheits-Regel, Pflicht-Hit, 418 einschalten, Ziwei/BaZi formulieren, `db reset`, Merge `main`.

## Ist

Schritt 0 (2026-09-20): Methodik-Tabelle oben. Decision „Phasen-Review 14b — Methodik statt Ranglisten“.

Schritt 1: Fixtures `apps/web/scripts/fixtures/handbook-charts.ts` (6 HD, 4 Astro). OS-Nodes haben Interps/`plan_10a` (Generator 83/121). `payload.facets.open_expression` an Centern = 0; Packer liest Essays. Routing Typ/Strategie/Venus → Liebe vor Seed = 0.

Schritte 2–5: HD `kind=os` Erstlage, Bindung nur Zusatz (kein Sakral-Fallback). Astro Venus sekundär. Formulierer v4. Literatur-Domänenfilter. Seed `--only-domain-routing` mit `IC_PROJECTS_ROOT` natal: 9 HD-OS + Venus `approved` auf Liebe. Fetch-Timeout erzeugte Dubletten, danach Dedup: `belongs_to_domain` approved 85, candidate 418 unangetastet. Seed bricht bei Fetch-Fehler jetzt ab.

Schritt 6: `check_handbook_love.ts` grün. 1978 HD primary `hd.type.generator`, secondary `59_6`; Identität weiter `59_6`. Astro primary `dsc_sign`, secondary Venus. Regression Input / Literatur / Formulierer / Astro grün. HD-Liebestext antwortet auf Bindung (OS), nicht nur Kanal. Astro-Spillover „Pferde“ bleibt Kurationspunkt (Gegen-Nodes ungeroutet). UI: `/home/karte/bereich/love_partnership` → Sign-in; Browser-Login in Automation nicht verifiziert.
