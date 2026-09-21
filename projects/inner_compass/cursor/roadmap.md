<!--
Reality Block
last_update: 2026-09-21
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
| 13a Astro-Literatur | **abgeschlossen 2026-09-18** | `extract_relationships` astro, 448 `candidate`, gelesen am AC-Hit | [plans/13a_astro_literatur.md](plans/13a_astro_literatur.md) |
| 14 Zweite Domäne | **abgeschlossen 2026-09-19** | `love_partnership` durch die Kette (HD + Astro), Formulierer v3 | [plans/14_zweite_domaene.md](plans/14_zweite_domaene.md) |
| 14b Methodik Liebe | **abgeschlossen 2026-09-20** | OS-Erstlage + Bindungs-Zusatz; Venus sekundär; Formulierer v4 | [plans/14b_methodik_liebe.md](plans/14b_methodik_liebe.md) |
| 15 Kapitel-Modell | **abgeschlossen 2026-09-21** | Form einmal: primary / secondary[] / overlay[] / highlight; Regeln als Daten; Formulierer v5; Inventar | [plans/15_hit_regel_tabelle.md](plans/15_hit_regel_tabelle.md) |
| 16 Beruf | offen | erste Domäne nur als Tabelleneintrag + Fixtures + Seed; Test des Modells | [plans/16_beruf.md](plans/16_beruf.md) |
| Verbreitung | offen, nach Fläche | Mandala-Share, Serie, Agents | nicht Plan-Nummer |

**Empfehlung:** Track Tiefe. Phase 15 zu. Nächster Schnitt: [Plan 16](plans/16_beruf.md) Beruf als Eintrag im Kapitel-Modell (kein Code-Umbau). Overlay füllen = 10b, Stimme-Register = 13, HD-Welle = 10. Jiazi/Ziwei dahinter, nicht Transit.

**Nächster Bau:** Plan 16 — [plans/16_beruf.md](plans/16_beruf.md).

### Track Tiefe

Vertikal einmal an HD `self_identity`, dann Schema einfrieren, dann die vier rechnenden Systeme. Färbungskarte bleibt Fallback. Formulierer ist Schritt 11, nicht 09.

### Warteschlange (nichts vergessen)

Review darf umsortieren; streichen nur nach Decision. Details in den verlinkten Plänen.

| # | Schnitt | Warum es liegt | Nicht verwechseln mit |
|---|---|---|---|
| 1 | ~~Plan 13a Astro-Literatur~~ | **erledigt 2026-09-18** | HD-Welle zuerst |
| 1b | ~~Plan 14 Liebe durch die Kette~~ | **erledigt 2026-09-19** | zwölf Domänen auf einmal |
| 1c | ~~Plan 14b Methodik Liebe~~ | **erledigt 2026-09-20** | Pflicht-Hit / Disjunktheit |
| 2 | ~~Plan 15 Kapitel-Modell~~, dann 16 Beruf | **15 erledigt 2026-09-21.** 16 = erste Domäne nur als Eintrag ([16](plans/16_beruf.md)) | Spray / alle zwölf; Overlay füllen (10b) |
| 3 | Jiazi-KG | 60 Knoten, 0 Interps; Klassiker **683 Chunks** ohne Classify ([03a](plans/03a_bazi_extract_ahead.md)); Destiny-Relink | *60 Pillars* zuerst; parallel zu Tiefe |
| 4 | Staffel 2 *60 Pillars* | nur **mit** Schnitt Jiazi | parallel zu Fläche |
| 5 | ~~Routing HD/BaZi über OS/Tagstamm~~ | **erledigt Plan 08** | 418-Spray |
| 6 | Weitere Bereichsseiten | einzeln über Plan 15, **nach** zweitem System sonst Typologie | Mandala-Share |
| 7 | ~~Familie-2-Filter~~ | **aufgelöst in Track:** Schicht 1 = Phase 9, Schicht 2 = Phase 10/12 | Backfill auf approved heben |
| 8 | ~~Trap/Gift DE~~ | **Plan 10–14** Facetten + Literatur als Input, Formulierer DE | `extract_pattern_traps` (Kombi über Systeme = nach 13a) |
| 9 | ~~DE-Atome / Formulierer HD Identität~~ | **Phase 11–14** | EN-Atome übersetzen / Re-Synth |
| 10 | HD-Content-Welle (PHS, Quarter, Planeten, Type-4) | **nach** den Systemen durch die Checkliste **und** Plan 15, nicht davor. Färbt **jeden** Bereich, nicht nur Gesundheit. Inventar: [15](plans/15_hit_regel_tabelle.md) | Checkliste wiederholen |
| 10b | Overlay in jedem Kapitel (Autorität, Profil, Definition, alle offenen Center) | Form da (Plan 15 `overlay[]`). Inhalt minimal (Labels, Center-Zustand). Facetten/Wordings füllen = diese Warteschlange. Inventar in [15](plans/15_hit_regel_tabelle.md) | 418; Center als Ersatz-Kanal |
| 11 | ZEIT / Luck / Transite | eigene Achse, Tages-Cache-Key; nach Natal in ≥2 Systemen | Occupancy war Phase 6 |
| 13 | Stimme-Register (originär ↔ IC, Coaching, …) | Umschalten = zwei Flächen (Inspector vs. Kapitel), nicht Ton-Schalter. Weitere Töne = Cache-Dimension `stimme` nach Plan 15 (zu). Vertrag: [tiefe.md](vertraege/tiefe.md) „Drei Flächen“ | Formulierer-Ton in 16 ändern |

**Ops (kein Phasen-Plan):** Login oft 1978-11-10; Langdock-Pin `gpt-5.4-mini`; 3–5 qualitative Charts; Browser-Auth in Automation. Utopia: [ideas.md](../reference/ideas.md), nicht diese Schlange.

**Nicht-Ziele:** Merge `main`, Force-Push, `supabase db reset`, Re-Synth, Spark-Qwen als Interpret, HD-Zombie `5ba2f841`, Flora/`.env`/`_tmp_*`, next-intl-Welle, Jyotish/Maya-UI bevor eine Seite sie speist, zwei Content-Wellen parallel, elf Handbuch-Seiten in einem Plan, SVG-Feinschliff, Mandala-Share vor Fläche, Big-Bang „alle Systeme fertig dann Formulierer“.

**Nordstern:** [nordstern.md](nordstern.md). **Verträge:** [vertraege/](vertraege/). **Tiefe:** [vertraege/tiefe.md](vertraege/tiefe.md).
