<!--
Reality Block
last_update: 2026-09-18
scope: Laufender Anker — Phasen, Status, nächster Plan, Warteschlange
in_scope: Reihenfolge, Status, Links, geordnetes Offenes
out_of_scope: Implementierungsdetails (stehen im Phasen-Plan)
-->

# Roadmap

Jeder neue Chat liest zuerst diese Datei, dann den verlinkten Phasen-Plan. Cursor-Plan-Dateien unter `.cursor/plans/` sind Duplikate.

**Arbeitsweise:** Ein Schnitt, dann Review, dann der nächste Plan — nicht zwei Wellen parallel. Innerhalb einer Phase Todos *(D)* / *(S)*. Offenes steht **nummeriert** (Warteschlange), nicht nur im Chat. **Jeder Plan nennt seine Matrix-Zelle** in [vertraege/tiefe.md](vertraege/tiefe.md).

| Phase | Status | Ziel | Plan |
|---|---|---|---|
| 0 Git-Hygiene | abgeschlossen 2026-09-04 | Auth-Docs + Relink-Skript auf `cursor/astro-natal`. HD-Pipeline-Skripte untracked. | — |
| 1 Nordstern + Rules | abgeschlossen 2026-09-04 | Dünnes Set, Rules, Handover | [plans/01_nordstern.md](plans/01_nordstern.md) |
| 2 `self_identity` vertikal | abgeschlossen 2026-09-11 | Eine Domäne echt | [plans/02_self_identity.md](plans/02_self_identity.md) |
| 3 BaZi-Content | abgeschlossen 2026-09-13 | Unabhängigkeit ja. Jiazi-KG Nachzug. | [plans/03_bazi.md](plans/03_bazi.md) · [03a](plans/03a_bazi_extract_ahead.md) |
| 4 Cross-Kanten | abgeschlossen 2026-09-15 | Familie 4; Jiazi bleibt Nachzug | [plans/04_cross_kanten.md](plans/04_cross_kanten.md) |
| 5 Werkstatt | abgeschlossen 2026-09-15 | Tor + `/home/werkstatt`. Resonanz = Tür. | [plans/05_werkstatt.md](plans/05_werkstatt.md) |
| 6 KARTE-Belegung | abgeschlossen 2026-09-15 | Occupancy-Rad. Nur `self_identity` Handbuch. | [plans/06_karte_belegung.md](plans/06_karte_belegung.md) |
| 7 `love_partnership` | abgeschlossen 2026-09-16 | Zweites Kapitel: Haus 7 + 夫妻宫. HD bewusst still. | [plans/07_love_partnership.md](plans/07_love_partnership.md) |
| 8 HD/BaZi auf Liebe | abgeschlossen 2026-09-16 | OS + Tagstamm färben Liebe; 418 still | [plans/08_hd_routing_love.md](plans/08_hd_routing_love.md) |
| 9 Mechanik-Kanten HD | **abgeschlossen 2026-09-16** | Familie 2 Schicht 1 Runtime + `condition`; Identität liest Tor/Kanal | [plans/09_tiefe_hd.md](plans/09_tiefe_hd.md) |
| 10 Facetten + Schicht-2-Spec | **abgeschlossen 2026-09-17** | Facetten als `HandbookInput` (EN Rohstoff); Job-Spec, Lauf = 10a | [plans/10_facetten_schicht2.md](plans/10_facetten_schicht2.md) |
| 10a Relationships-Lauf | **abgeschlossen 2026-09-17** | `extract_relationships` auf HD-Chunks, 3 Charts, 869 `candidate` | [plans/10a_relationships_lauf.md](plans/10a_relationships_lauf.md) |
| 11 Formulierer v0 | **abgeschlossen 2026-09-17** | einmal pro Chart, HD-Identität, DE aus Input | [plans/11_formulierer.md](plans/11_formulierer.md) |
| 12 Schicht 2 / Matrix | **abgeschlossen 2026-09-18** | literature[] am Hit + Schema eingefroren | [plans/12_schicht2_matrix.md](plans/12_schicht2_matrix.md) |
| 13 Zweites System | **abgeschlossen 2026-09-18** | Checkliste an Astro Aszendent; Formulierer v2 | [plans/13_zweites_system.md](plans/13_zweites_system.md) |
| 13a Astro-Literatur | geplant | `extract_relationships` für astro, condition-Vokabular, Lesen am AC-Hit | [plans/13a_astro_literatur.md](plans/13a_astro_literatur.md) |
| Verbreitung | offen, nach Fläche | Mandala-Share, Serie, Agents | nicht Plan-Nummer |

**Empfehlung:** Track Tiefe. Phase 13 zu (Astro AC durch die Checkliste, Literatur leer). Nächster Schnitt Plan 13a (Astro-Literaturlauf), nicht HD-Welle, nicht Transit, nicht Jiazi.

**Nächster Bau:** [plans/13a_astro_literatur.md](plans/13a_astro_literatur.md).

### Track Tiefe

Vertikal einmal an HD `self_identity`, dann Schema einfrieren, dann die vier rechnenden Systeme. Färbungskarte bleibt Fallback. Formulierer ist Schritt 11, nicht 09.

### Warteschlange (nichts vergessen)

Review darf umsortieren; streichen nur nach Decision. Details in den verlinkten Plänen.

| # | Schnitt | Warum es liegt | Nicht verwechseln mit |
|---|---|---|---|
| 1 | Plan 13a Astro-Literatur | Handler HD-only; 0 Astro-Kanten Schicht 2 | HD-Welle zuerst |
| 2 | Jiazi-KG | 60 Knoten, 0 Interps; Klassiker **683 Chunks** ohne Classify ([03a](plans/03a_bazi_extract_ahead.md)); Destiny-Relink | *60 Pillars* zuerst; parallel zu Tiefe |
| 3 | Staffel 2 *60 Pillars* | nur **mit** Schnitt 2 | parallel zu Fläche |
| 4 | ~~Routing HD/BaZi über OS/Tagstamm~~ | **erledigt Plan 08** | 418-Spray |
| 5 | Weitere Bereichsseiten | einzeln, **nach** zweitem System sonst Typologie | Mandala-Share |
| 6 | ~~Familie-2-Filter~~ | **aufgelöst in Track:** Schicht 1 = Phase 9, Schicht 2 = Phase 10/12 | Backfill auf approved heben |
| 7 | ~~Trap/Gift DE~~ | **Plan 10–13** Facetten + Literatur als Input, Formulierer DE | `extract_pattern_traps` (Kombi über Systeme = nach 13a) |
| 8 | ~~DE-Atome / Formulierer HD Identität~~ | **Phase 11–13** | EN-Atome übersetzen / Re-Synth |
| 9 | HD-Content-Welle (PHS, Quarter, Planeten, Type-4) | **nach** den Systemen durch die Checkliste, nicht davor | Checkliste wiederholen |
| 10 | ZEIT / Luck / Transite | eigene Achse, Tages-Cache-Key; nach Natal in ≥2 Systemen | Occupancy war Phase 6 |
| 11 | Verbreitung | nach Fläche; Vorlauf = Namen + Handles, keine Posts (Decision 2026-09-16) | Stub-Content; Mandala-Share jetzt |

**Ops (kein Phasen-Plan):** Login oft 1978-11-10; Langdock-Pin `gpt-5.4-mini`; 3–5 qualitative Charts; Browser-Auth in Automation. Utopia: [ideas.md](../reference/ideas.md), nicht diese Schlange.

**Nicht-Ziele:** Merge `main`, Force-Push, `supabase db reset`, Re-Synth, Spark-Qwen als Interpret, HD-Zombie `5ba2f841`, Flora/`.env`/`_tmp_*`, next-intl-Welle, Jyotish/Maya-UI bevor eine Seite sie speist, zwei Content-Wellen parallel, elf Handbuch-Seiten in einem Plan, SVG-Feinschliff, Mandala-Share vor Fläche, Big-Bang „alle Systeme fertig dann Formulierer“.

**Nordstern:** [nordstern.md](nordstern.md). **Verträge:** [vertraege/](vertraege/). **Tiefe:** [vertraege/tiefe.md](vertraege/tiefe.md).
