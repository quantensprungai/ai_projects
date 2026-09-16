<!--
Reality Block
last_update: 2026-09-13
scope: Phasen-Plan 3 — BaZi als unabhängige Stimme
in_scope: Bestand K2, strukturelles Routing, First-Cut-Chart, Unabhängigkeitsbeleg auf self_identity, Jiazi-KG nur nach Chunks
out_of_scope: Mandala, 12 Bereichsseiten, Werkstatt-Seite, Cross-Kanten, Luck-Pillar-UI, Re-Synth Destiny Code, Spark-Qwen, MinerU-Jobs (Plan 03a)
-->

# Plan 03 — BaZi

Selbsttragend. Warum BaZi jetzt: Ziwei sitzt auf derselben Zwölfteilung wie Astro — das testet Konvergenz nicht. BaZi (4 Pfeiler / 60 Jiazi) hat kein 12-Rad. Decision 2026-09-04 Punkt 5 und Review 2: nächste Content-Welle = BaZi.

Verträge: [../vertraege/](../vertraege/). Learnings: [../reference/s5d_pipeline_learnings.md](../reference/s5d_pipeline_learnings.md). Welle-Standard: [../reference/k2_foundation_wave_playbook.md](../reference/k2_foundation_wave_playbook.md).

Code-Repo: `code/inner_compass_app` (eigenes Git, Branch `cursor/astro-natal`).

## Reihenfolge

1. Bestand lesen — kein Blind-Seed — **erledigt 2026-09-11 (kein Re-Seed)**
2. Strukturelles Routing (Day Master → `self_identity`) — **erledigt 2026-09-11**
3. Chart-First-Cut `/home/karte/bazi` — **erledigt 2026-09-13** (Chrome + Inspector, kein Atom-Text)
4. Unabhängigkeitsbeleg auf der Bereichsseite — **belegt 2026-09-13** (Login-Person, Ji-Lage + Entwurf, kein Palast-/Haus-Label)
5. Jiazi-KG nur nach Extract-ahead (Chunks in 03a) — **nicht in diesem Plan text2kg**. Chunks da (03a).
6. Phasen-Review 3 — **erledigt 2026-09-13**

**Parallel:** MinerU-Klassiker laufen in [03a_bazi_extract_ahead.md](03a_bazi_extract_ahead.md) (`extract_text` + `extract_ahead=true`). Classify/interpret/text2kg bleiben aus, bis die Fläche steht. Playbook §4a.

## 1) Bestand — *(D)* — **gelesen 2026-09-11, kein Re-Seed**

Nicht `ic_seed_structure.py --system bazi` ausführen, bevor ein Audit das verlangt. Historisch (2026-07): 97 Nodes (37 Kern + 60 Jiazi), strict text2kg, Destiny Code `cbe86636` mechanisch durch, Wildwuchs 460→37.

Prüfen: `ic_k2_state_audit.py` (oder Studio) auf `system=bazi`. Engine `@yhjs/bazi` / `@ic/engines` wie in `cursor/status.md` — Pfad im Code-Repo verifizieren, nichts erfinden. Hub-Linse `bazi` ist `soon`.

Kein `supabase db reset`. Re-Seed nur wenn Metadata-Wipe oder 0 Kern-Nodes.

### Ist (2026-09-13)

| Schicht | Stand |
|---|---|
| Katalog / K2 | unverändert: 97 Nodes, `life_domain_map` nur 10 Day Master → `self_identity`. Kein Re-Seed. |
| Synthese | 37 EN-Kern. Jiazi 0. Inspector auf der Karte: „kein Atom-Text“ — erwartet. |
| Literatur | Destiny `cbe86636` (420). Plus Klassiker-Chunks in [03a](03a_bazi_extract_ahead.md) (683, kein Classify). |
| Engine | `@ic/engines/bazi` → `bazi-public.ts` (Turbopack, kein Barrel). Gender aus `user_persons`. |
| API / Persist | `GET`/`POST /api/ic/bazi-chart`, `user_charts.system_id='bazi'`. Stateless `POST /api/bazi/calculate` bleibt. |
| App | Hub `live`. `/home/karte/bazi`: Vier Säulen Chrome DE. Bereich: vierte Quelle (Tagstamm-Lage + Entwurf). |
| Routing | 10 `bazi.day_master.*` → `self_identity` (`approved`). Ten Gods/Stems nicht gesprüht. |

Nächster Bau: Phase 4. Jiazi-KG = Nachzug, kein Blocker.

## 2) Routing — *(D)*

`system_structure/bazi_structure_v0.json`: minimale `life_domain_map`. Die 10 Day Master sind **eine Rolle** (日主), zehn Färbungen — analog HD-Typen, alle → `self_identity`. Nicht die 10 Stems in Jahr/Monat/Stunde, nicht Ten Gods in die 12 sprühen. `ic_seed_structure.py --only-domain-routing` analog HD-OS. Kanten `belongs_to_domain`, `approved`, Evidence = Datei+Zeile.

BaZi hat kein 12-Rad — fehlende Domänen bleiben ohne strukturelle Kante. Inhaltliche Kanten nicht in diesem Plan.

## 3) Chart-First-Cut — *(S Gate / D)*

Route `app/[locale]/home/(user)/karte/bazi`. Vier Säulen, Chrome DE, Inspector darf EN-Atome zeigen (wie Astro). Kein Overlay, keine Luck Pillars auf dem Screen, keine 流年-Analogie.

Hub-Linse von `soon` auf `live`. System-Chart darf dichter sein als die Bereichsseite.

## 4) Unabhängigkeitsbeleg — *(S)*

Auf `self_identity` eine vierte Quelle: BaZi als Lage-Satz (Day Master in Alltagsworten) + Entwurfs-Hinweis, solange kein DE-Handbuchabsatz existiert. `handbook-voice.ts` erweitern, nicht Atome übersetzen.

Beleg ist erfüllt, wenn dieselbe Person HD + Astro/Ziwei (Häuser-Stamm) **und** BaZi (Pfeiler) auf einer Seite hat, ohne dass BaZi die Palast-/Haus-Labels kopiert.

ZEIT-Seite bleibt Platzhalter. Höchstens notieren, dass die Engine Luck Pillars kann — nicht bauen.

## 5) Jiazi-Literatur — *(D, nach 03a)*

Inventur 2026-09-11: 60 `bazi.jiazi.*` **ohne** Interps. Extract-ahead der Klassiker + 60 Pillars liegt in [03a](03a_bazi_extract_ahead.md). In **diesem** Plan keine KG-Kette. Wenn Chunks da sind: Seed liegt schon, strict, Interpret/text2kg/Synth = Langdock, `IC_TEXT2KG_AUTO_SYNTH=false`, scoped Synth `--only-id`. Destiny Code nicht full re-synthen.

## 6) Phasen-Review 3 — *(S)* — **erledigt 2026-09-13**

Verträge gegen Code. Decision: [../../reference/decisions.md](../../reference/decisions.md) 2026-09-13.

## Review-Check (2026-09-13, bestanden)

| Vertrag | Befund |
|---|---|
| Domäne | Vierte Quelle auf `self_identity`. Nur Day Master strukturell geroutet. Kein 12-Rad-Spray. |
| Handbuch-Stimme | Tagstamm im Benennen/Locate. Lage + Entwurf, kein Atom-Übersetzen. Palast/Haus nicht kopiert. |
| Status | Gate hält. Karte darf EN-IDs + „kein Atom-Text“. Bereich: kein EN-Absatz. |
| Sprache | Chrome DE, Atome EN/leer — bewusst. |
| Resonanz | `card_key=bazi.day_master` in `resonance.ts`. Nicht im Browser neu gedrückt, Schema steht. |
| Kanten | Familie 3: 10 Day-Master-Kanten. Familie 4 unangetastet. |
| Werkstatt | Unverändert Phase-2-Tor. BaZi speist kein Experiment. |

**Jiazi:** 60 Katalog-Knoten, 0 Interps. Nicht nötig für den Unabhängigkeitsbeleg. Welle später (strict, Langdock, kein Auto-Synth). Staffel 2 (*60 Pillars*) hängt an dieser Welle, nicht an Plan 04.

Abweichungen (bewusst): 3–5 fremde Charts weiter offen; Resonanz-Klick BaZi nicht verifiziert; systemd-MVP auf Spark weiter crash-loop (`sudo`); `bazi-public.ts` dupliziert Slugs/TZ für Turbopack.

## Erwartetes Ergebnis

Eine Person sieht BaZi als eigene Stimme, nicht als Ziwei-Klon. Seed bleibt die Whitelist. Keine zwölf Seiten.

## Nicht

Mandala, zwölf Bereiche, Werkstatt-Seite, `converges`/`complements`/`contradicts`, Luck-Pillar-UI, ZEIT-Screen füllen, Spark-Qwen, Full-Synth Destiny Code, `supabase db reset`, Merge `main`, Force-Push, `.env*`/`_tmp_*`, Jyotish/Maya-UI, next-intl-Welle.
