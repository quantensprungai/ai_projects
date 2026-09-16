<!--
Reality Block
last_update: 2026-09-16
scope: Phasen-Plan 7 — zweite Bereichsseite love_partnership
in_scope: Enum freeze, Gate + Assemble für dieses Enum, zwei Lage-Quellen Haus 7 / 夫妻宫, Vertrag HD vs. Domänen
out_of_scope: elf Seiten, Jiazi, Familie-4 auf Liebe, Candidate-418 einschalten, Sex-Manual als Kapitel, neue Werkstatt, DE-Atome, Occupancy-Regel ändern
-->

# Plan 07 — Liebe & Partnerschaft

Selbsttragend. Warum jetzt: Phase 6 hat Occupancy. Belegte Keile außer Identität sind Stubs. Review 6: nächster Schnitt = **eine** weitere Bereichsseite, nicht Jiazi, nicht elf Kapitel.

**Enum (fest):** `love_partnership` (Label „Liebe & Partnerschaft“, Kernfrage „Wie liebe ich?“, Ring Nah). Struktur-Lagen: 7. Haus (`astro.house.7`) und 夫妻宫 (`ziwei.palace.spousePalace`). Nicht `sexuality_intimacy` (strukturell nur Haus 8, Occupancy Login-Person leer). Nicht `relationships_community` nur weil HD-Payload dort laut ist.

Verträge: [../vertraege/](../vertraege/) — **Leitvertrag** [domaene.md](../vertraege/domaene.md). Stimme [handbuch_stimme.md](../vertraege/handbuch_stimme.md). Status-Gate [status.md](../vertraege/status.md). Occupancy bleibt [06](06_karte_belegung.md) (Natal ∩ `approved`).

Code-Repo: `code/inner_compass_app` (eigenes Git, Branch `cursor/astro-natal`). Pfade relativ zu `apps/web/`, wo Code.

## These: HD vs. Domänen (nicht nur Chat)

Sonst wirkt dieser Plan so, als wäre HD für immer nur Identität. Das widerspricht dem Vertrag.

**Jedes System spricht in jeden Bereich**, nur nicht jedes als Strukturkonzept. Die 12 Enums sind **Navigation** (Zwölfteilung Häuser / Bhavas / Paläste, Ringe Kern/Nah/Feld), nicht HD-Ontologie. Multi-Map ist die Regel (Haus 8 zwei Domänen; Ziwei 10/12; Jyotish später oft ein Bhava → mehrere). HD und BaZi haben **kein** 12-Rad.

**„HD nur `self_identity`“ ist ein Seed-Artefakt**, kein Produktziel. [`hd_structure_v0.json`](../../system_structure/hd_structure_v0.json) `life_domain_map` mappt absichtlich nur OS (Typ / Strategie / Autorität / Profil) → Identität. Tore und Zentren nicht sprayen war Plan 02. Inhaltlich ist HD in allen 12 erfahrbar (`payload.life_domain` an Interpretations ~99 %). SoT: [domaene.md](../vertraege/domaene.md); Decision 2026-09-04 (Nordstern) und 2026-08-27 (Katalog-Stand).

**Zwei Wege `belongs_to_domain`:**

| Weg | Status | Liebe heute |
|---|---|---|
| Strukturell (Katalog-Map) | `approved` | Astro Haus 7, Ziwei Spouse-Palast. HD-OS **nicht** hier. |
| Inhaltlich (`payload.life_domain` aggregiert) | `candidate` | ~418 Paare katalogweit (Schwelle ≥3 Interps und ≥30 %). Lautester Cluster `relationships_community` (~199) = Sammelbecken. |

**Kommt HD-Nacharbeit auf diese Seite?** Ja. Dieselbe Pipeline: Natal ∩ `belongs_to_domain` → `assembleDomainPage({ domainId: 'love_partnership' })`. Kein zweites Produkt. Occupancy-Hub zündet erst bei `approved` (Review 6). Assemble rangiert `approved` vor `candidate`. Promote oder kuratierte Katalog-Zeilen in Schlange **#4** erscheinen hier.

**Muss jedes System in jedem Bereich etwas haben?** Als These ja, als Fill-Rule nein. Schweigen ist ehrlich (leeres Segment, Leerfall-Satz). Nicht kosmetisch auffüllen. In **diesem** Plan bleibt HD auf der Liebe-Seite still.

**Was schon liegt (nicht „nicht extracted“):** 418 `candidate` (nicht wipen, Plan 04). *Sex Manual* im HD-Korpus (ToC partnership/sexuality) — Chunks/Interps, **keine** verdrahtete Lage. 07 schaltet die 418 **nicht** ein.

## Was das nicht ist

| Verwechslung | Klarstellung |
|---|---|
| Elf Handbuch-Kapitel | Nur dieses Enum öffnen. Andere Stubs bleiben. |
| Candidate-418 / Sex-Manual | Spray und Sammelbecken. Nachzug **#4**, eigene Methodik (welche Tore/Kanäle; Promote vs. Katalog-Zeile). |
| HD-Toren nach Liebe mappen | Nicht in 07. Occupancy-Regel bleibt approved-only. |
| Familie-4 auf Liebe | Muster bleibt auf `self_identity`, bis Routing steht. |
| Neue Werkstatt | Tor darf fehlen oder auf Identität verweisen. `/home/werkstatt` bleibt Identität. |
| Jiazi / 60 Pillars | Schlange **#2**, nicht parallel. |
| `career_calling` | Andere zweite Seite. Enum ist Liebe. |

## Reihenfolge

1. Bestand — *(D)* **gehalten 2026-09-16** (`astro.house.7` + `ziwei.palace.spousePalace` `approved`; HD `candidate` auf Liebe: 7 Paare, Kreuze/Quarter, nicht promote)
2. Methodik — *(S)* **gehalten**
3. Gate + Assemble — *(D / S)* **erledigt 2026-09-16**
4. Browser — *(D)* **teilweise:** Auth wie Review 6 blockiert; DB-Natal: kein `astro.house.*` in Nodes, Ziwei hat `spousePalace`
5. Phasen-Review 7 — *(S)* **2026-09-16** — siehe [decisions.md](../../reference/decisions.md)

## Review-Check (2026-09-16)

Gate `isHandbookLiveDomain`. Assemble: Haus 7 wird auf Liebe **injiziert** (Chart speichert keine Häuser, analog Haus 1 auf Identität). HD/BaZi still. Treffen und Werkstatt nur Identität. Occupancy-Formel unverändert; Hub `handbookLive` auch Liebe.

## 1) Bestand — *(D)*

Maps (nicht raten): [`astro_structure_v0.json`](../../system_structure/astro_structure_v0.json) Haus 7 → `love_partnership`; [`ziwei_structure_v0.json`](../../system_structure/ziwei_structure_v0.json) `spousePalace` → `love_partnership`. Katalog-Drift `houses[].life_domain` (`partnerships`) nicht umschreiben.

Code-Ist (vor dem Bau lesen, nicht umbauen in Todo 1):

- Gate: `app/[locale]/home/(user)/karte/bereich/[domain]/page.tsx` — `domain !== 'self_identity'` → Stub.
- [`lib/ic/domain-assemble.ts`](../../../../code/inner_compass_app/apps/web/lib/ic/domain-assemble.ts): `input.domainId` steuert den Kanten-Schnitt; **Ranking und Natal-Force sind identitätslastig:** `edgeRank` bevorzugt `astro.house.1` / `ziwei.palace.soulPalace`; `collectAstroIds` fügt immer Haus 1 + AC hinzu; `collectZiweiIds` immer `soulPalace`; `cardKeyFromCanonical` kennt nur `astro.asc_house1` / `ziwei.life_palace`. Werkstatt-Zweig in Assemble bleibt HD-OS / `self_identity`.
- Occupancy: `lib/ic/karte-occupancy.ts` — `handbookLive: id === 'self_identity'`.
- Enums: `lib/ic/life-domains.ts` hat `love_partnership` schon.

Login: `test@makerkit.dev` / `testingpassword`. Geburten im Slice: 1980-11-18 19:20 Berlin, 1978-11-10 19:20 Berlin. Next `:3000`, Supabase `:54321`, HD `:8002`. Occupancy 1978-11-10 war 10/12; Liebe sollte über Haus/Palast belegt sein — in Todo 1 an der DB prüfen.

HD-Hits `candidate` ∩ Natal für `love_partnership` nur Report (Zahl + 2–3 Canonical-IDs). Nicht promote.

## 2) Methodik — *(S)* — vor dem Bau festhalten

- **Eine Occupancy-Regel, zwei Kapitel.** Hub-Regel unverändert. Zweite „Handbuch live“-Zeile = dieses Enum.
- **Pro Quelle max. eine Karte**, `approved` vor `candidate`. Für Liebe: Astro = Haus 7 (nicht Haus 1, auch wenn collect Haus 1 im Natal-Set hat). Ziwei = Spouse-Palast (nicht 命宫). HD = Leerfall-Satz, kein stiller Candidate-Treffer.
- **Ranking domain-sensitiv oder explizite Prefer-Liste** pro Enum — nicht `edgeRank` so lassen, dass Haus 1 Haus 7 schlägt.
- **Resonanz:** neue grobe Keys analog Identität (`astro.house7`, `ziwei.spouse_palace`), nicht die Identitäts-Keys wiederverwenden. Onboarding bleibt `self_identity`.
- **Stimme:** Benennen / Übersetzen / Verorten; Systemname erst im Verorten; keine Canonical-IDs; Lage-Satz + Entwurf wenn Atom EN.
- **Treffen:** nur wenn zwei UI-taugliche Quellen auf **dieser** Seite. Keine neuen Familie-4-Seeds für Liebe.
- **Werkstatt:** kein neues Experiment aus HD-OS auf der Liebe-Seite. Tor weglassen oder ein Satz „Versuch bleibt am Kapitel Selbst“.
- **Kein `generate_meta_nodes`.** Kein Spray in `life_domain_map` HD.

## 3) Gate + Assemble — *(D / S)*

- Gate in `page.tsx`: frei wenn `domain === 'self_identity' || domain === 'love_partnership'`. Stub-Text der anderen zehn nicht anfassen.
- `assembleDomainPage`: Kartenwahl und Lage-Sätze für Haus 7 / Spouse. Identitäts-Pfad unverändert (Regression).
- Hub-Legende / Occupancy-View: `handbookLive` auch für `love_partnership`.
- System-Chart-Assemble (`lib/hd|astro|ziwei|bazi/*-assemble.ts`) nicht anfassen.
- `life-domains.ts` nur bei nachgewiesenem Label-Drift.
- Kein Worker-Re-Synth, kein Payload-Backfill, kein Seed-Spray.

## 4) Browser — *(D)*

Wie 02/06: Docker, Supabase `:54321`, HD `:8002`, Next `:3000`. Login wie oben. Beide Geburten im Slice.

Fragen: Liest sich Liebe wie ein zweites Kapitel oder wie Inspector? Stehen Haus 7 / Ehepalast, nicht AC / 命宫? HD ehrlich still? Identität (Spiegel, Treffen, Werkstatt-Tor) unverändert? Hub: zwei Handbuch-Zeilen, restliche Stubs? Desktop + schmal laut Handbook-UI. Kein E2E.

## 5) Phasen-Review 7 — *(S)* — **2026-09-16, geschrieben**

Volltext: [decisions.md](../../reference/decisions.md) „Phasen-Review 7“. Muster kopierbar; HD-Seed bleibt bis #4; Jiazi #2.

## Erwartetes Ergebnis

Route `/karte/bereich/love_partnership` ist Handbuch mit zwei Lagen (Astro + Ziwei) oder ehrlichem Leerfall. HD schweigt bewusst. Hub zeigt das zweite Kapitel. 418 unverändert `candidate`. Identität und Werkstatt unverändert.

## Nicht

Elf Seiten, Jiazi-text2kg, Staffel 2, Candidate-418 einschalten, HD-Tore sprayen, Sex-Manual als Kapitel, Familie-4 auf Liebe, neue Werkstatt, DE-Atome-Welle, Occupancy auf candidate umstellen, Spark-Qwen, `supabase db reset`, Merge `main`, Force-Push, `.env*`/`_tmp_*`.
