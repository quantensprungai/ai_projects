<!--
Reality Block
last_update: 2026-09-16
scope: Phasen-Plan 8 — HD/BaZi-Routing auf love_partnership über OS/Tagstamm
in_scope: Färbungskarte Typ/Strategie und Tagstamm auf Liebe, Assemble-Inject, Katalog-Map-Zeilen Typ/Strategie/Tagstamm → Liebe
out_of_scope: 418-Spray, Sex-Manual, Jiazi, Familie-4 auf Liebe, neue Werkstatt, Occupancy auf candidate, elf Seiten, DE-Atome
-->

# Plan 08 — HD/BaZi auf Liebe (OS / Tagstamm)

Selbsttragend. Warum jetzt: Phase 7 hat Liebe als Kapitel, HD/BaZi bewusst still. Vertrag: jedes System spricht in jeden Bereich, HD hat kein 12-Rad. Seed „OS nur Identität“ bleibt für Occupancy-Struktur; **Tiefe 1** färbt denselben Typ/Tagstamm in die Bindung. Nicht Jiazi, nicht 418.

Verträge: [../vertraege/domaene.md](../vertraege/domaene.md), [handbuch_stimme.md](../vertraege/handbuch_stimme.md), [status.md](../vertraege/status.md). Occupancy bleibt [06](06_karte_belegung.md) (Natal ∩ `approved`). Vorarbeit: [07](07_love_partnership.md).

Code-Repo: `code/inner_compass_app`, Branch `cursor/astro-natal`. Pfade relativ zu `apps/web/`, wo Code.

## These

HD und BaZi kommen auf Liebe **über die Betriebssystem-Lage** (Typ + Strategie, Tagstamm), nicht über Tore/Kanäle und nicht über `payload.life_domain`. Dieselbe Person, andere Färbung: Identität sagt, wie du startest; Liebe sagt, wie das in Bindung wirkt.

**Inject wie Haus 7:** Chart hat Typ und Tagstamm schon. `pickEdge` fand auf Liebe nichts, weil die Map nur `self_identity` kennt. Assemble spricht trotzdem, sobald Typ/Stamm bekannt sind — `uiReady`, wenn die Färbungskarte greift. Katalog-Zeilen OS→Liebe sind SoT für späteres Occupancy/Seed, **kein** Re-Seed in diesem Schnitt (`supabase db reset` bleibt verboten).

**418 bleiben `candidate`.** Kreuze/Quarter Duality nicht promote.

## Was das nicht ist

| Verwechslung | Klarstellung |
|---|---|
| Candidate-418 / Sex-Manual | Eigene Methodik, nicht dieser Plan. |
| HD-Tore nach Liebe mappen | Occupancy-Regel unverändert. |
| Familie-4 auf Liebe | Treffen bleibt Identität, bis eigene Liebe-Kanten existieren. |
| Werkstatt auf Liebe | Tor bleibt Identität. |
| Jiazi / 60 Pillars | Schlange **#2**. |
| Alle OS-Knoten (Autorität, Profil) | Nur was die Stimme braucht: Typ+Strategie, Tagstamm. |

## Reihenfolge

1. Methodik — *(S)* **gehalten 2026-09-16**
2. Stimme + Assemble — *(D / S)* **erledigt 2026-09-16**
3. Katalog-Map (JSON) — *(D)* **erledigt 2026-09-16** (kein DB-Reset)
4. Docs / Review 8 — *(S)* **2026-09-16**
5. Browser — *(D)* Auth oft blockiert; Login-Person Generator 1978-11-10

## 2) Methodik — *(S)*

- Eine Occupancy-Regel. Hub zündet HD auf Liebe **nicht**, nur weil die Seite spricht (keine neuen `approved` in der DB in diesem Cut).
- Pro Quelle max. eine Karte. HD = Typ+Strategie-Färbung. BaZi = Tagstamm-Färbung.
- Stimme formuliert, kein Typ-Label im Benennen, Systemname erst im Verorten.
- Treffen und Werkstatt unverändert Identität.
- Kein `generate_meta_nodes`. Kein Worker.

## 3) Stimme + Assemble — *(D / S)*

- `handbook-voice.ts`: `composeHdPartnershipVoice`, `composeBaziPartnershipVoice`; `LOCATE_LOVE` für HD/BaZi.
- `domain-assemble.ts`: Love-Skip für HD/BaZi entfernen; Karten wenn Chart da; Meeting/Werkstatt weiter `!love`.
- Identität-Pfad unverändert.

## 4) Katalog-Map — *(D)*

`hd_structure_v0.json`: Typ + Strategie zusätzlich `love_partnership`. `bazi_structure_v0.json`: Tagstämme zusätzlich `love_partnership`. Seed-Skript nicht in diesem Cut.

## Review-Check (2026-09-16, geschrieben)

Volltext: [decisions.md](../../reference/decisions.md) „Phasen-Review 8“. Liebe Tiefe 1: vier Quellen. 418 unangetastet. Treffen/Werkstatt Identität.

## Erwartetes Ergebnis

`/karte/bereich/love_partnership`: vier Quellen Tiefe 1 (HD, Astro, Ziwei, BaZi) oder ehrlicher Leerfall. 418 unverändert. Identität + Werkstatt unverändert.

## Nicht

418, Jiazi, Merge `main`, Force-Push, `supabase db reset`, Spark-Qwen, `.env*`/`_tmp_*`.
