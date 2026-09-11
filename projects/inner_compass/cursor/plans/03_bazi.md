<!--
Reality Block
last_update: 2026-09-11
scope: Phasen-Plan 3 — BaZi als unabhängige Stimme
in_scope: Bestand K2, strukturelles Routing, First-Cut-Chart, Unabhängigkeitsbeleg auf self_identity, Jiazi nur wenn Inventur es verlangt
out_of_scope: Mandala, 12 Bereichsseiten, Werkstatt-Seite, Cross-Kanten, Luck-Pillar-UI, Re-Synth Destiny Code, Spark-Qwen
-->

# Plan 03 — BaZi

Selbsttragend. Warum BaZi jetzt: Ziwei sitzt auf derselben Zwölfteilung wie Astro — das testet Konvergenz nicht. BaZi (4 Pfeiler / 60 Jiazi) hat kein 12-Rad. Decision 2026-09-04 Punkt 5 und Review 2: nächste Content-Welle = BaZi.

Verträge: [../vertraege/](../vertraege/). Learnings: [../reference/s5d_pipeline_learnings.md](../reference/s5d_pipeline_learnings.md). Welle-Standard: [../reference/k2_foundation_wave_playbook.md](../reference/k2_foundation_wave_playbook.md).

Code-Repo: `code/inner_compass_app` (eigenes Git, Branch `cursor/astro-natal`).

## Reihenfolge

1. Bestand lesen — kein Blind-Seed
2. Strukturelles Routing (Day Master → `self_identity`)
3. Chart-First-Cut `/home/karte/bazi`
4. Unabhängigkeitsbeleg auf der Bereichsseite
5. Jiazi-Literatur nur nach Inventur
6. Phasen-Review 3

## 1) Bestand — *(D)*

Nicht `ic_seed_structure.py --system bazi` ausführen, bevor ein Audit das verlangt. Historisch (2026-07): 97 Nodes (37 Kern + 60 Jiazi), strict text2kg, Destiny Code `cbe86636` mechanisch durch, Wildwuchs 460→37.

Prüfen: `ic_k2_state_audit.py` (oder Studio) auf `system=bazi`. Engine `@yhjs/bazi` / `@ic/engines` wie in `cursor/status.md` — Pfad im Code-Repo verifizieren, nichts erfinden. Hub-Linse `bazi` ist `soon`.

Kein `supabase db reset`. Re-Seed nur wenn Metadata-Wipe oder 0 Kern-Nodes.

## 2) Routing — *(D)*

`system_structure/bazi_structure_v0.json`: minimale `life_domain_map`. Day Master / Day Stem → `self_identity`. Nicht alle Ten Gods in alle 12 sprühen. `ic_seed_structure.py --only-domain-routing` analog HD-OS. Kanten `belongs_to_domain`, `approved`, Evidence = Datei+Zeile.

BaZi hat kein 12-Rad — fehlende Domänen bleiben ohne strukturelle Kante. Inhaltliche Kanten nicht in diesem Plan.

## 3) Chart-First-Cut — *(S Gate / D)*

Route `app/[locale]/home/(user)/karte/bazi`. Vier Säulen, Chrome DE, Inspector darf EN-Atome zeigen (wie Astro). Kein Overlay, keine Luck Pillars auf dem Screen, keine 流年-Analogie.

Hub-Linse von `soon` auf `live`. System-Chart darf dichter sein als die Bereichsseite.

## 4) Unabhängigkeitsbeleg — *(S)*

Auf `self_identity` eine vierte Quelle: BaZi als Lage-Satz (Day Master in Alltagsworten) + Entwurfs-Hinweis, solange kein DE-Handbuchabsatz existiert. `handbook-voice.ts` erweitern, nicht Atome übersetzen.

Beleg ist erfüllt, wenn dieselbe Person HD + Astro/Ziwei (Häuser-Stamm) **und** BaZi (Pfeiler) auf einer Seite hat, ohne dass BaZi die Palast-/Haus-Labels kopiert.

ZEIT-Seite bleibt Platzhalter. Höchstens notieren, dass die Engine Luck Pillars kann — nicht bauen.

## 5) Jiazi-Literatur — *(D, optional)*

Nur wenn Inventur zeigt: 60 `bazi.jiazi.*` ohne brauchbare Interps. Dann Playbook: Seed liegt schon, strict, Spark nur MinerU, Interpret/text2kg/Synth = Langdock, `IC_TEXT2KG_AUTO_SYNTH=false`, scoped Synth `--only-id`. Destiny Code nicht full re-synthen.

## 6) Phasen-Review 3 — *(S)*

Verträge gegen Code. Decision: Unabhängigkeit ja/nein, Jiazi-Welle nötig ja/nein. Offenes in `roadmap.md`. Plan 04 (Cross-Kanten in *einer* Domäne) erst danach.

## Erwartetes Ergebnis

Eine Person sieht BaZi als eigene Stimme, nicht als Ziwei-Klon. Seed bleibt die Whitelist. Keine zwölf Seiten.

## Nicht

Mandala, zwölf Bereiche, Werkstatt-Seite, `converges`/`complements`/`contradicts`, Luck-Pillar-UI, ZEIT-Screen füllen, Spark-Qwen, Full-Synth Destiny Code, `supabase db reset`, Merge `main`, Force-Push, `.env*`/`_tmp_*`, Jyotish/Maya-UI, next-intl-Welle.
