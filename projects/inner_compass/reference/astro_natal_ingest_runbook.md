---
last_update: 2026-09-02
status: active
scope:
  summary: "Westliche Astrologie — Extract-ahead, Natal-KG-Welle (Langdock), Relink/scoped Synth, KARTE First Cut."
in_scope:
  - Lokale Werke, Duplikate, Spark-MinerU extract_text
  - Wellen-Tags analog HD-Transit / Ziwei-流年
  - K2-Seed + Typ-Whitelist, Mixed-Skip, Relink, scoped Ground-Synth
  - KARTE `/home/karte/astro` (Rad, Big Three, Selektion-Linien, Typ-Atome)
  - Interpret/text2kg-Queue (Jobs ≠ Chunks; HD-Zombie)
out_of_scope:
  - Overlay-LLM / Mandala
  - Katalog-houses[].life_domain umschreiben
  - Jyotish parallel
---

# Astro-Natal Ingest

SoT: `reference/decisions.md` 2026-08-31 Extract-ahead + 2026-09-01 Katalog-Seed + 2026-09-02 KARTE-Rad.
Playbook: `cursor/reference/k2_foundation_wave_playbook.md` §4a + Knopf Astro.

**Jetzt (2026-09-02 Abend):** KARTE-Rad First Cut liegt. Interpret-Welle durch (~3217 Astro-Interps). **14/14 text2kg completed.** Relink `astro_natal_relink_v1` 58/58 **apply nach t2k.** Erster Ground-Synth 25 EN lag (Häuser+7 Planeten+5 Majors+MC); **Nachzug 16 EN** (12 Häuser + AC/DC/IC/MC). AC/DC/IC nicht mehr Stub. 7 Planeten nicht re-synched. Spark nur `extract_text` (MinerU). Windows-Langdock `ic_start_langdock_worker.py` = classify / term_mapping / interpret / text2kg (`gpt-5-mini`, `IC_TEXT2KG_AUTO_SYNTH=false`). Later-PDFs (Paulus, Hephaistio II, Anonymous 379) nicht classify. HD-Zombie `5ba2f841` nicht anfassen.

## Split (logisch, nicht weil der Plan es sagt)

| Band | `wave` | Warum | Analog |
|---|---|---|---|
| Hellenistisch/traditionell natal | `astro_natal` | 12 Häuser + Planeten/Zeichen/Würden = KARTE-Rad | Ziwei-Paläste, HD Type |
| Transite | `astro_transit` | Zeit, nicht Geburt. Würde Natal-Atome mit „wenn Saturn über…“ füllen | HD-Transit, 流年 |
| Horary | `astro_horary` | Fragen-Chart, kein Geburtshoroskop | — (kein HD-Pendant) |
| Psychologisch/humanistisch | `astro_psychological` | Andere Schule als Ptolemy/Lilly/George | Ziwei 三合/飞星 draußen |

Lilly *Christian Astrology* 3 Bände: Book I+III natal, **Book II Horary im selben PDF**. Extract als natal. Standalone-Book-II (`c43f8b59`) **nicht** extra MinerU (Subset). Horary-KG später dieselben Chunks (Seitenrange) oder das Book-II-PDF mit `wave=astro_horary` — kein zweites MinerU auf den 3-vol.

**Kein physisches Split, nichts löschen.** MinerU schreibt alle Seiten in `sys_source_chunks`. Was „Skip“ heißt:

| Ebene | Was passiert | Transit/Horary weg? |
|---|---|---|
| Extract | ein Lauf, ganzer Band | nein, Text liegt |
| Natal-KG-Welle (First Cut) | nur natal-Kapitel an Haus/Planet-Typen; Mixed-Kapitel **nicht** an Natal-Atome | nicht weg, nur nicht verdrahtet |
| Spätere Welle `astro_transit` / `astro_horary` | **dieselben Chunks**, anderer Filter / `wave` | dann erst Atome dafür |

`ingest_note` und `skip_first_cut_text2kg` sind Merker. `skip_first_cut_text2kg` filtert `ic_astro_natal_kg_start.py` (kein Classify). Mixed-Kapitel: Source-Flag `skip_mixed_chapters_natal` + `mixed_skip_profile` (`lilly_3vol` / `carmen` / `valens_b23`). Worker `ic_astro_mixed_skip.py` hält eine Zone (Lilly Book II bis Book III, Carmen IV–V bis Ende, Valens Book III Length of Life). Chunks bleiben. 3/915 Topic-only war zu dünn — sequenziell nachschärfen, nicht Chunks löschen. Ganzes Werk Timing (Hand, Teachings `921e728e`): Source-`wave=astro_transit` → `_parks_kg_downstream`, kein natal-text2kg.

Erste Tradition für spätere Atome = **hellenistic / medieval** (Ptolemy, Dorotheus, Lilly natal, George Vol I+II). Rudhyar nicht in denselben Topf.

## Disk — unique, MinerU

Pfad: `Downloads/Literatur/astro/` plus George Vol I in `archiv/`.

| Key | Werk | S. | MB | Staffel | `wave` |
|---|---|---|---|---|---|
| ptolemy_b1 | Tetrabiblos Book I (Schmidt/Hand 1994) | 80 | 2.5 | smoke | natal |
| dorotheus | Dorotheus / Orpheus / Anubio / Pseudo-Valens (Hand 1995) | 84 | 27.5 | parked | **transit** (Greek Track IX, nicht Carmen) |
| lilly_3vol | Lilly Christian Astrology 3 Bände | 923 | 12.3 | natal | natal (Book II mixed) |
| george_v1 | George *Ancient Astrology* Vol I (2019, archiv) | 628 | 41.3 | natal | natal |
| george_v2 | George Vol II *Delineating Planetary Meaning* (2022) | 704 | 56.5 | natal | natal |
| clark_epitome | Clark Tetrabiblos 2006 | 116 | 1.3 | natal | natal / `modern_epitome` |
| hand_transit | Hand *Planets in Transit* | 540 | 14.7 | parked | **transit** |
| rudhyar_personality | Rudhyar *Astrology of Personality* | 463 | 5.5 | parked | **psychological** |

**Nicht MinerU (Duplikat):** Lilly Book II allein; `astro/K2/` Ptolemy = root; `astro/K4/` Clark = root.

## Disk — `astro/neu/` (2026-09-01)

pypdf-Stichprobe (erste Seiten). Tompkins: Windows-Langpfad, 8.3 `ASPECT~1.PDF`.

| Key | Werk | MB | pypdf | Staffel | `wave` |
|---|---|---|---|---|---|
| robbins_en | Tetrabiblos Robbins **English-only** (`7b9ba633`, 0.5 MB, 120 S.) | 0.5 | **text-layer, sauber** | **neu-must** | natal — **Ptolemy-SoT**, ersetzt Greek Track B1 |
| carmen | Dorotheus *Carmen Astrologicum* Pingree 2005 (`91aeb0ee`) | 19.5 | text-layer; Titel OCR, **Körper lesbar** | **neu-must** | natal — **die fünf Bücher**; B.4 Profection/Timing, B.5 Interrogationen → `ingest_note` |
| houlding | *The Houses* (2006) | 5.6 | text-layer | **neu-must** | natal |
| tompkins | *Aspects in Astrology* (2002) | 2.1 | text-layer (Cover gesperrt) | **neu-must** | natal |
| arroyo_handbook | *Chart Interpretation Handbook* | 3.8 | text-layer | **neu-must** | natal (modern, Outer-Planets-Gerüst) |
| arroyo_karma | *Astrology, Karma & Transformation* (1992) | 5.2 | text-layer | **neu-must** | natal (Uranus/Neptun/Pluto natal, nicht Transit-Welle) |
| brennan | Brennan *Hellenistic Astrology* (2017, `75b77c06`) | 9.8 | Cover OCR, **Körper digital-sauber** (698 S.) | **neu-must** | natal — hellenistic Lehrbuch, K2 neben George |
| valens_b1 | Valens *Anthology* Book I (`c3f6ceed`) | 2.7 | **text-layer, sehr sauber** (172 S.) | **neu-must** | natal — Sterne/Zeichen/Lots |
| valens_b23 | Valens Book II (concl.) & III Schmidt/Hand (`01c2dfac`) | 30.8 | Scan-OCR lesbar (wie Carmen) | **neu-must** | natal Topics + Lebenslänge; Timing-Kapitel analog Carmen IV |
| loeb_scan | Loeb L435 Robbins 1–4 Scan | 48.5 | OCR-Matsch, Griechisch gegenüber | **skip** | dieselbe Übersetzung, schlechtere Datei |
| ashmand_1936 | Ashmand Quadripartite Scan | 11.3 | image-scan | **skip** | Proklos-Paraphrase |
| ashmand_2018 | Fb&c Reprint Ashmand | 12.1 | gesperrtes OCR | **skip** | dasselbe, nicht Robbins |
| paulus | Paulus *Introductory Matters* GH Vol I | 2.6 | text-layer | **later-extract** | natal hellenistic primer; `skip_first_cut_text2kg` |
| hephaistio_ii | Hephaistio Apotelesmatics II | 6.5 | text-layer (leicht OCR) | **later-extract** | Topics/Lebenslänge; `skip_first_cut_text2kg` |
| anonymous_379 | Anonymous 379 Bright Fixed Stars | 0.7 | text-layer | **later-extract** | Fixsterne; `skip_first_cut_text2kg` |
| hephaistio_i | Hephaistio Book I GH | 30.9 | **image-scan, 0 Text** | skip jetzt | erst Ersatz-PDF, nicht MinerU auf Blindscan |

**Ptolemy:** SoT = Robbins 0.5 MB. Greek Track B1 bleibt im Corpus, **kein** text2kg-Primary. Loeb-Scan und Ashmand nicht extra MinerU.

**Dorotheus:** Die fünf natalen Bücher **liegen** (Pingree *Carmen*). Das alte PDF „Teachings on Transits“ (Greek Track IX, `921e728e`) ist **nicht** Carmen — `wave=astro_transit` + `skip_natal_text2kg` gesetzt 2026-09-01, nicht nochmal MinerU.

**Zwei Eimer, nicht ein „schlecht“:**
- **skip / nicht MinerU** = Qualität oder schlechtere Duplikat-Edition (Loeb-Scan = Robbins nochmal matschig; Ashmand = Proklos-Paraphrase; Hephaistio I = Blindscan, 0 Text).
- **later** = Inhalt/Priorität. Qualität reicht, First Cut 12-Häuser ist aber schon durch Ptolemy/Dorotheus/George/Brennan/Houlding gedeckt: Paulus (Primer), Hephaistio II (Topics/Lebenslänge-Kommentar), Anonymous 379 (30 Fixsterne, kein Häuser-Rad).

**Registry, nicht Blocker:** Sasportas (Houlding deckt Häuser). George *Authentic Self* entfällt — Vol I+II sind die bessere K2-Technik. Brennan + Valens I–III liegen in `astro/neu`.

`life_domain_map` in `astro_structure_v0.json` nutzt `contracts.md` §2. Katalog-`houses[].life_domain` bleibt Drift — nicht umschreiben, bis UI die Katalog-Felder liest. Decision 2026-09-01.

## MinerU (Spark)

Worker schon: `IC_WORKER_JOB_TYPES=extract_text`, `SUPABASE_URL=http://100.70.238.41:54321`.
Job-Debug **überschreibt** Env `IC_MINERU_LANG=ch` → `latin`. `extract_ahead=true` → kein classify.

```powershell
cd C:\Users\Admin105\ai_projects\code\inner_compass_app\apps\web
python scripts/ic_astro_natal_upload.py --staffel all --dry-run
python scripts/ic_astro_natal_upload.py --staffel all --scp
python scripts/ic_astro_natal_upload.py --staffel neu --dry-run
python scripts/ic_astro_natal_upload.py --staffel neu --scp
```

Große PDFs (>40 MB: George I+II) nur über `local_pdf_path` auf Spark:
`/home/sparkuser/srv/hd-worker/literature/astro/{md5}.pdf`

Nach Worker-Code-Deploy:

```bash
scp -P 2222 apps/web/scripts/ic_worker.py sparkuser@100.96.115.1:~/srv/hd-worker/ic_worker.py
sudo systemctl restart hd-worker   # auf Spark; Filter extract_text behalten
```

Seed **während Extract ok.** `ic_seed_structure.py --system astro` + Whitelist `apps/web/scripts/ic_astro_k2_catalog.py`. Langdock-Worker braucht die Datei vor text2kg (`IC_TEXT2KG_STRICT_ASTRO`). Spark-Extract-Worker nicht.

Natal-KG nach Brennan + Valens I + Valens II/III extract:

```powershell
python scripts/ic_astro_natal_kg_start.py --wait-brennan-valens --start-worker
```

First Cut: `wave=astro_natal`, kein `skip_first_cut_text2kg`, kein parked. Mixed-Kapitel: `skip_mixed_chapters_natal` + `mixed_skip_profile` + sequenzielle Zone in `ic_astro_mixed_skip.py`. Chunks bleiben.

Nach text2kg (nicht vorher):

```powershell
python scripts/ic_astro_alias_unwrap.py --dry-run
python scripts/ic_astro_natal_audit.py
python scripts/ic_astro_natal_relink.py --dry-run
python scripts/ic_run_with_langdock.py ic_astro_natal_synth.py --dry-run
```

Relink ist kein Palast-Skript: Häuser brauchen vollen Namen (`first house`), Timing/Horary → mention, Arroyo/Tompkins → mention (anderer Wording-Topf). Extra-Slot leer. Mentions nicht reparieren. Erster Synth: Ground `--only-id` (`ic_astro_natal_synth.py`, `IC_LLM_MAX_TOKENS=8000`, EN). Nachzug Häuser/Achsen: `ic_k2_synth_batch.py --force` mit 16 `--only-id` — **nicht** `ic_astro_natal_synth.py --force` (das syncht die 7 Planeten mit).

KARTE: `/home/karte/astro` — tropisch + Whole Sign (Engine **celestine**, nicht sidereal). AC links (Haus 1 = Screen-270°). Big Three (Sonne/Mond/AC) + Rad. Körper auf ekliptikaler Länge 0–360, Collision-Offset. **Klick auf Körper:** nur seine Major-Aspekte (Filter `conjunction|sextile|square|trine|opposition`, Slice 24). Hausklick = keine Linien. Konjunktion im selben Haus = Mini-Chord zwischen zwei Glyphs — wirkt wie „keine Linien“ (chart-spezifisch, kein Zeichen-Filter). AC/DC/IC/MC Atome EN nach Nachzug-Synth 2026-09-02 Abend (nicht mehr Stub). Inspector = Typ-Atome, Chrome DE (`astro-chrome-de.ts`), kein Overlay, keine `astro.placement.*`. Verifiziert 2026-09-02: Login-Geburt 1980-11-18 19:20 Berlin (AC Krebs, Sonne Skorpion H5, Mond Widder H10). Same-Birth-Test: `packages/engines/src/natal-same-birth-coverage.test.ts` (1990-06-15 14:30, nicht die App-Person). Playwright `apps/e2e/tests/ic/karte-astro.spec.ts` — Login/SSR `factors` oft flaky, separates App-Thema.

### Natal-KG-Korpus (Account `5deaa894-…`, Stand 2026-09-02 Abend)

14 Werke `wave=astro_natal`, kein `skip_first_cut_text2kg`. Chunks (Extract): Lilly 918 · George II 558 · George I 383 · Valens I 363 · Tompkins 312 · Arroyo Karma 312 · Carmen 181 · Houlding 141 · Clark 135 · Robbins 135 · Arroyo Handbook 112 · Valens II/III 73 · Tetrabiblos B1 Schmidt 35 · Brennan Count-500. Mixed-skip interpret: Lilly 267 / Carmen 103 / Valens B2–3 21.

**Jobs ≠ Chunks.** `extract_interpretations` completed **269** (Poll morgen) = Lifetime über **alle** Systeme, nicht Chunks. Ein Job ≤ 50 Chunks (`IC_INTERP_BATCH_SIZE`). Astro-Interpret-Welle **durch** (~3217 Interps). Astro failed 6: je 1–2 Chunks nach 2 LLM-Retries — Rest des Buchs liegt. Übrige Failed = HD/BaZi-Reset/GK-414, nicht diese Welle.

**HD-Zombie** `5ba2f841` (*Definitive Book*, Bunnell/Ra): `running` seit 2026-08-10, Worker `langdock-hd-profiles`. Prozess tot. Astro-Worker claimed nur `queued` → **blockiert Natal nicht**. Nicht canceln unless asked.

**text2kg 14/14 completed** (Catch-up ~16:27–16:30 UTC+2). Unmatched Cap 200 bei Arroyo/Valens I/Tompkins = Whitelist, keine neuen Nodes. Relink `--apply` Abend 58/58: Häuser Cap 6 Primaries; AC 6/10, DC 4/9, IC 6/3, MC 6/8. Scoped Synth 16 Nodes (~5 min). Overlay-Sätze nicht in dieser Welle.

## Offen / geparkt

| Was | Status |
|---|---|
| Extract-ahead Welle 1 (8 unique) | done 2026-08-31 |
| Extract-ahead Welle 2 (9 PDFs) | MinerU; Robbins/Carmen/Houlding/Tompkins done 2026-09-01; Rest Queue |
| Extract-ahead later (Paulus, Hephaistio II, Anonymous 379) | queued 2026-09-01; `skip_first_cut_text2kg`; Hephaistio I skip |
| Altes Dorotheus-Transits-PDF retaggen | done 2026-09-01 `921e728e` → `wave=astro_transit` + `skip_natal_text2kg` |
| Classify / interpret / text2kg | Interpret durch (~3217 Astro-Interps). 14/14 text2kg completed 2026-09-02. Later-PDFs nicht enqueue. 269 completed-Jobs = alle Systeme (Jobs ≠ Chunks) |
| Seed + `life_domain_map` + `ic_astro_k2_catalog.py` | done 2026-09-01; 71 Nodes; Skeleton-`astro.aspect.*` gelöscht |
| Mixed-Skip | sequenziell 2026-09-01 (`ic_astro_mixed_skip.py`); Lilly 267 / Carmen 103 / Valens B2–3 21; extra-Profil 733 nur notiert |
| Relink / scoped Synth | apply Abend 2026-09-02 `astro_natal_relink_v1` 58/58 nach t2k; Ground-Synth 25 EN + Nachzug 16 (Häuser+AC/DC/IC/MC). 7 Planeten nicht `--force` |
| Horary-Welle (Lilly Book II) | PDF liegt; nicht extra extractet; Book II im 3-vol-Extract, Skip bei interpret |
| Transit-KG (Hand + Teachings on Transits) | Extract ok; kein natal-text2kg |
| Rudhyar-Atome | Extract ok; andere Schule |
| Paulus / Hephaistio II / Anonymous 379 | lokal, later; `skip_first_cut_text2kg`; kein Classify |
| Hephaistio I Scan / Loeb 48 MB / Ashmand | nicht MinerU |
| Brennan / Valens I–III | in Welle; Interpret+text2kg durch 2026-09-02; Valens II+III mixed Book III |
| HD-Zombie `5ba2f841` | `running` seit 2026-08-10; nicht canceln unless asked; blockiert Astro nicht |
| Astro-KARTE UI | First Cut 2026-09-02: Big Three + Rad, Selektion-Linien, Typ-Atome, Chrome DE. Overlay/Mandala später |
| Jyotish | nicht parallel |

Skript: `apps/web/scripts/ic_astro_natal_upload.py`.
