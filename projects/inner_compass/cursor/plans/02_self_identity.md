<!--
Reality Block
last_update: 2026-09-04
scope: Phasen-Plan 2 — self_identity vertikal
in_scope: Kanten, Status-Gate, Resonanz, Handbuch-Stimme, eine Route, Werkstatt-Tor
out_of_scope: Mandala-SVG, 12 Seiten, Cross-Kanten, Werkstatt-Seite, Re-Synth
-->

# Plan 02 — self_identity vertikal

Selbsttragend. Verträge: [../vertraege/](../vertraege/). Warum eine Domäne: teuer nachzurüsten sind Verträge und Datenform, nicht Content. `self_identity` ist der einzige Bereich mit Material aus allen drei Live-Systemen (HD-OS, 命宫, Haus 1/AC) und mit existierender Handbuch-Stimme (HD-Keil).

Code-Repo: `code/inner_compass_app` (eigenes Git, Branch `cursor/astro-natal`). Pfade unten relativ zu `apps/web/`.

## Reihenfolge

1. Domäne + Routing-Kanten (Substrat)
2. Wirkungskanten sichten (nur lesen)
3. Resonanz-Tabelle
4. Handbuch-Stimme
5. Route + Assembler
6. Browser, dann 3–5 echte Charts
7. Phasen-Review 2

## 1) Domäne und Routing-Kanten — *(D strukturell / S Schwelle)*

**`lib/ic/life-domains.ts`** (neu): 12 Enums, Label, Kernfrage, Ring, gespiegelt aus `projects/inner_compass/cursor/contracts.md` §2 Z. 143–176. Einziger Code-Ort.

**`scripts/ic_seed_structure.py`**:
- Neue Funktion `build_life_domains`: 12 Knoten `ic.life_domain.{enum}`, `system='meta'`, Label/Kernfrage/Ring in Metadata. Kein LLM.
- Strukturell: Ziwei-Schleife (~Z. 675–696) und Astro (~Z. 756–782) schreiben zusätzlich Kanten `belongs_to_domain` → `ic.life_domain.*`, `review_status='approved'`, `edge_scope='intra_system'`, Evidence = Katalogdatei + Zeile. Haus 8 → zwei Kanten. Node-Metadata bleibt stehen.
- `projects/inner_compass/system_structure/hd_structure_v0.json`: minimale `life_domain_map` — `hd.type.*`, `hd.strategy.*`, `hd.authority.*`, `hd.profile.*` → `self_identity`. `build_hd` liest sie analog. Nicht Tore/Zentren spraying.

**`scripts/ic_domain_edges_from_payload.py`** (neu, inhaltlich): aggregiert `sys_interpretations.payload.life_domain` pro Node (nur HD zuerst). `--dry-run` gibt Report: Node, Domäne, Anzahl Interps, Anteil. Schwelle *(S)* danach festlegen (Vorschlag ≥3 Interps und ≥30 %). `--apply` schreibt `belongs_to_domain` mit `review_status='candidate'`, Evidence = Interp-IDs. Idempotent.

Prüfung in Studio: 12 Knoten `ic.life_domain.*`; Kanten je Domäne; `sexuality_intimacy` strukturell genau eine Kante (Astro Haus 8). Nicht kosmetisch auffüllen.

Kein `supabase db reset`, kein Re-Synth, kein Relink.

## 2) Wirkungskanten sichten — *(D)*

Nur lesen: `sys_kg_edges` mit `amplifies` / `clashes_with` / `modifies` / `depends_on` zwischen den `self_identity`-Elementen der Login-Person (Typ, Autorität, Profil, definierte Zentren). Zahlen und drei Beispiele in `vertraege/kanten.md` unter „Bestand self_identity“ eintragen. Nichts extrahieren.

## 3) Resonanz — *(D)*

Migration `supabase/migrations/<ts>_ic_resonance.sql`: Tabelle `ic_resonance` (`id`, `account_id`, `card_key` text, `domain` text, `system` text, `canonical_ids` text[], `answer` enum `yes|partly|no`, `wording_version` text, `created_at`). RLS: Account liest/schreibt nur eigene Zeilen. `card_key` grob (`hd.type`, `hd.strategy`, `astro.asc_house1`, `ziwei.life_palace`), nicht pro Tor.

Server Action `app/[locale]/home/(user)/karte/bereich/_lib/resonance-action.ts`. Onboarding (`app/[locale]/home/_components/ic-spaces/ic-onboarding-view.tsx`, bisher UI-State) schreibt in dieselbe Tabelle.

## 4) Handbuch-Stimme — *(S)*

`lib/ic/handbook-voice.ts` neben `lib/ic/hd-handbook-gloss.ts` (bleibt Vorbild, nicht umbauen). Regel als Kommentar + Helfer: kein Systemjargon im Benennen, Systemname erst im Verorten, keine Canonical-IDs, keine Quelltitel, zweite Person, kein Urteil, keine Stufen. Sprache v0 vorgegeben. Meta-Begriffe, die dabei entstehen, in `vertraege/handbuch_stimme.md` notieren, nicht in die DB.

## 5) Route und Assembler — *(S Gate / D Umsetzung)*

**`lib/ic/domain-assemble.ts`** (neu): liest `belongs_to_domain`-Kanten, schneidet gegen Chart-Elemente der Person aus den bestehenden `GET /api/ic/hd-chart`, `/api/ic/ziwei-chart` (bzw. `/api/ziwei/calculate`), `/api/ic/astro-chart`. Pro Quelle max. eine Karte, `approved` vor `candidate`.

Status-Gate (siehe `vertraege/status.md`): `sys_synthesis_wordings` hat keine Statusspalte. UI-tauglich = `language='de'` **oder** Allowlist der genutzten Canonical-IDs (HD-Keil zählt als DE). EN-Atome → Lage-Satz + Entwurfs-Hinweis, nie Absatz. Nichts → Leerfall-Satz. Die Assemble-Dateien der System-Charts (`lib/hd/hd-chart-assemble.ts`, `lib/ziwei/ziwei-chart-assemble.ts`, `lib/astro/astro-chart-assemble.ts`) nicht ändern.

**Route** `app/[locale]/home/(user)/karte/bereich/[domain]/page.tsx`: dynamisch, aber nur `self_identity` frei; andere Enums ehrlicher „noch nicht“-Hinweis.

Aufbau: Kopf (Bereichsname, Kernfrage) → Filter-Chips (alle / Human Design / Astrologie / Ziwei) → Tiefe 1 je Quelle mit *Benennen / Übersetzen / Verorten*, Herkunfts-Chip, Ja/Teilweise/Nein → Tiefe 2 „Wo sich die Quellen treffen“ nur bei zwei UI-tauglichen Quellen → **Werkstatt-Tor**: ein Satz aus `payload.process.experiment_seed` des stärksten HD-Elements („Ein Experiment dazu“), keine eigene Seite. Leerfall pro Quelle: wer schweigt und warum.

Hub `app/[locale]/home/_components/ic-spaces/ic-karte-hub-view.tsx`: Einstieg „Selbst & Identität“ ergänzen; Engine-Englisch aus `hdSnippet` (~Z. 74–81, 167–170) entfernen. Mandala-Platzhalter bleibt.

## 6) Browser — *(D)*

Voraussetzungen: Docker Desktop, Supabase lokal (`:54321`), HD-Service `docker compose -f services/hd/docker-compose.yml up -d` (`:8002`), `pnpm --filter web exec next dev --port 3000`. Login `test@makerkit.dev` / `testingpassword`, Person 1980-11-18 19:20 Berlin (AC Krebs, Sonne Skorpion H5, Mond Widder H10).

Fragen: Liest sich das wie ein Handbuch oder wie drei geklebte Inspector-Zeilen? Irgendwo EN, Canonical-ID, Engine-Label, Quelltitel? Leerfall lesbar? Resonanz landet in `ic_resonance`? Werkstatt-Satz sinnvoll? JETZT, Onboarding, System-Charts unverändert? Kein E2E in diesem Cut. Danach 3–5 echte Menschen mit eigenem Chart, qualitativ.

## Erwartetes Ergebnis

HD-Karte echt (Keil), Astro und Ziwei als Lage-Sätze mit Entwurfs-Hinweis, ein Werkstatt-Satz. Beziffert die DE-Arbeit pro Domäne, bevor zwölf geplant werden.

## 7) Phasen-Review 2 — *(S)*

Verträge gegen Code; Offenes in `roadmap.md`; Decision-Eintrag (Schwelle inhaltliche Kanten, Meta-Begriffe, Befund Werkstatt-Tor); Plan 03 (BaZi) ausarbeiten.

## Nicht

Zwölf Seiten, Mandala-SVG, Cross-Kanten (`maps_to`/`converges`), Werkstatt-Seite, Re-Synth/Full-Synth, DE-Atome-Welle, `tag_ic_metadata`, `extract_relationships`, Assemble der System-Charts umbauen, Statusspalte erfinden, next-intl-Welle, Freemium-Code, Onboarding-Umbau, `supabase db reset`, Merge `main`, Force-Push, `.env*`/`_tmp_*` committen, Spark-Qwen, HD-Zombie `5ba2f841`.
