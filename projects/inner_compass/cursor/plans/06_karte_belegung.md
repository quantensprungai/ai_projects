<!--
Reality Block
last_update: 2026-09-16
scope: Phasen-Plan 6 — KARTE-Belegung (12 Segmente dieser Person)
in_scope: Hub statt Mandala-Platzhalter, Occupancy = Natal ∩ belongs_to_domain, Worker-Enums 10→12 ohne Re-Synth, elf Segmente ehrlich „noch nicht“
out_of_scope: elf volle Tiefe-1/2/4-Seiten, Familie-4-Wiederholung, Jiazi/text2kg, Mandala-Share, SVG-Perfektion, ZEIT/Luck, extract_pattern_traps, Familie-2-Sätze
-->

# Plan 06 — KARTE-Belegung

Selbsttragend. Warum damals: Vertikal auf **Selbst & Identität** war der Nordstern-Satz da. Review 5: nächster Plan dieser, nicht Jiazi. Die KARTE war ein Link plus Quellen-Linsen und Mandala-Platzhalter.

**Ist (nach Review 6):** Occupancy-Rad + 12-Zeilen-Legende. Belegung = Natal ∩ `approved` `belongs_to_domain`. Nur `self_identity` Handbuch. Worker 12 Enums. Code: `lib/ic/karte-occupancy.ts`, `ic-karte-occupancy-wheel.tsx`.

Verträge: [../vertraege/](../vertraege/) — **Leitvertrag** [domaene.md](../vertraege/domaene.md). Occupancy-Haltung [nordstern.md](../nordstern.md) („Inhaltsverzeichnis vor Inhalt“). Bereichsseiten bleiben [handbuch_stimme.md](../vertraege/handbuch_stimme.md) / [kanten.md](../vertraege/kanten.md); Werkstatt bleibt [werkstatt.md](../vertraege/werkstatt.md) auf einer Domäne.

Code-Repo: `code/inner_compass_app` (eigenes Git, Branch `cursor/astro-natal`). Pfade relativ zu `apps/web/`, wo Code.

## Was das nicht ist

| Verwechslung | Klarstellung |
|---|---|
| Katalog-Occupancy | „Überall liegt Struktur im Katalog“ ≠ „dieser Mensch hat hier etwas“. Belegung = **Natalknoten ∩ `belongs_to_domain`**. Leeres Segment ist ehrlich. |
| Elf Handbuch-Kapitel | Route `karte/bereich/[domain]` existiert schon. Außer `self_identity` bleibt Kernfrage + „noch nicht“. **`domain-assemble.ts` für die elf nicht anfassen.** Keine Familie-4-Wiederholung, keine elf Werkstätten. |
| Mandala-Share / SVG-Feinschliff | Teilbar denken ja. Share = Phase 7. 06 hat ein schlichtes Occupancy-Rad, keine Pixeljagd. |
| Routing-Nachzug als Inhalt | BaZi nur Tagstamm → `self_identity`; HD-OS nur Identität. Ohne Nachzug bleiben andere Bereichs-*Seiten* dünn (Review 4). 06 zeigt das auf dem Hub, füllt die Seiten nicht. |
| Jiazi / 60 Pillars | Eigener Content-Schnitt. Kein Blocker, nicht parallel zum ersten 06-Bau. |
| Worker-Re-Synth | Enums 10→12 im Prompt (`scripts/ic_worker.py`), damit neue Extracts die zwei fehlenden Tags kennen. **Kein** Re-Synth, kein Payload-Backfill. |

## Reihenfolge

1. Bestand lesen — *(D)* **gehalten** (Hub, Enums, Assemble-Gate, Worker)
2. Methodik — *(S)* **gehalten** (Natal ∩ approved; Rad + Liste)
3. Hub-Belegung + Worker-Enums — *(D / S)* **erledigt 2026-09-15**
4. Browser — *(D)* **teilweise:** DB-Occupancy 10/12 auf 1978-11-10; Automation-Login blockiert (Auth-Netz + Hydration)
5. Phasen-Review 6 — *(S)* **2026-09-15** — siehe [decisions.md](../../reference/decisions.md)

Neuer Chat: Roadmap → [07_love_partnership.md](07_love_partnership.md). Review 6 bleibt in [decisions.md](../../reference/decisions.md).

## 1) Bestand — *(D)* — **vor dem Bau; Ist siehe Review 6**

Hub vorher: Mandala-Platzhalter, ein Link `self_identity`, Quellen-Linsen. **Ist:** Rad + 12 Zeilen, Occupancy serverseitig (`assembleKarteOccupancy`), HD-Gloss bleibt Signatur.

Worker **Ist:** Prompt-Liste 12 Enums inkl. `exchange_learning` / `transformation_renewal`. Kein Re-Synth.

Login: `test@makerkit.dev` / `testingpassword`. Geburten im Slice: 1980-11-18 19:20 Berlin (Projector+Yi), 1978-11-10 19:20 Berlin (Generator+Bing). Next `:3000`, Supabase `:54321`, HD `:8002`. DB-Schnitt 1978-11-10: 10/12 Domänen belegt (`sexuality_intimacy`, `transformation_renewal` leer).

## 2) Methodik — *(S)* — vor dem Bau festhalten

- **Eine Occupancy-Regel:** Ein Segment gilt als belegt, wenn mindestens ein **Natal-Knoten dieser Person** eine `belongs_to_domain`-Kante auf `ic.life_domain.{enum}` hat (`approved` vor `candidate`, wie Assemble). Katalog-Treffer ohne Natal zählen nicht.
- **Zwei Zustände auf dem Hub, nicht drei Füllstände:** belegt (Link, Label, Kernfrage; Identität zusätzlich „Handbuch live“) vs. nicht belegt oder Bereich noch nicht frei (Kernfrage + ehrlich „noch nicht“). Kein Prozent, kein Katalog-Zähler.
- **Nur Identität ist Kapitel.** Klick auf die anderen 11 darf die existierende Stub-Route treffen. Keine neuen Assemble-Zweige, keine Familie-4-Seeds für andere Domänen.
- **HD/BaZi-Dünne ist sichtbar, nicht versteckt.** Segmente ohne Natal-Schnitt bleiben leer, auch wenn der Katalog Häuser/Paläste kennt — das ist die Aussage des Schnitts.
- **Kein `generate_meta_nodes`.** Keine neuen Meta-Wörter auf dem Hub (kein „Occupancy“, kein „Mandala-Score“).
- **Worker:** Liste auf 12 Enums erweitern. Bestehende Interps nicht neu synth.

## 3) Hub-Belegung + Worker-Enums — *(D / S)*

- Worker-Prompt in `scripts/ic_worker.py`: die zwei Enums ergänzen. Kein Re-Synth, keine Pipeline-Welle.
- Hub: Mandala-Platzhalter ersetzen durch 12 Segmente aus `LIFE_DOMAINS` / `LIFE_DOMAIN_IDS`. Belegung serverseitig oder über eine schmale API aus Natal ∩ Familie-3; nicht clientseitig den HD-Gloss als Occupancy missbrauchen.
- `self_identity` bleibt der live-Handbuch-Einstieg (wie heute).
- Elf andere: Link zur bestehenden Route oder Text „noch nicht“ — **page.tsx-Gate und `domain-assemble.ts` unverändert** für diese elf.
- System-Chart-Assemble (`lib/hd|astro|ziwei|bazi/*-assemble.ts`) nicht anfassen.
- `life-domains.ts` nur anfassen, wenn ein Label/eine Frage nachweislich driftet — keine neuen Felder „fürs Mandala“.

## 4) Browser — *(D)*

Wie Plan 02/04/05: Docker, Supabase `:54321`, HD `:8002`, Next `:3000`. Login wie oben. Beide Geburten im Slice (Geburt ändern / `?neu=1`).

Fragen: Sieht die KARTE nach **dieser** Person aus oder nach einem Katalog-Rad? Bleibt Identität das einzige Kapitel? Bleiben die elf Stubs ehrlich? Ändert Generator vs. Projector die Belegung dort, wo Natal × Routing sich unterscheidet — und nicht, wo nur der Katalog voll ist? Worker-Datei 12 Enums, keine neue Synth-Welle in der DB?

Kein E2E. Desktop + schmal laut Handbook-UI. Login kann noch auf 1978-11-10 stehen — bewusst umschalten.

## 5) Phasen-Review 6 — *(S)* — **2026-09-15, geschrieben**

Volltext: [decisions.md](../../reference/decisions.md) „Phasen-Review 6“. Occupancy-Rad + Liste live. Nur Identität Handbuch. Nächster Schnitt: erste weitere Bereichsseite oder Jiazi, nicht elf Seiten.

## Erwartetes Ergebnis

Auf `/home/karte`: 12 Segmente **dieser Person**. Identität führt ins Handbuch. Die anderen elf sagen die Kernfrage und „noch nicht“. Worker kennt 12 Enums. Kein Re-Synth. `domain-assemble` für die elf unangetastet.

## Nicht

Elf volle Tiefe-1/2/4-Seiten, Familie-4 auf anderen Domänen, Jiazi-text2kg, Staffel 2 *60 Pillars*, `extract_pattern_traps`, Familie-2-Sätze, Mandala-Share, SVG-Perfektion, ZEIT/Luck/Transite, DE-Atome-Welle, Spark-Qwen, `supabase db reset`, Merge `main`, Force-Push, `.env*`/`_tmp_*`.
