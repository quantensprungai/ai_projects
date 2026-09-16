<!--
Reality Block
last_update: 2026-09-15
scope: Phasen-Plan 5 — Werkstatt auf einer Domäne
in_scope: Tiefe 3–4 aus payload.process, eine Werkstatt-Seite, Einstieg von resonierter Karte, self_identity
out_of_scope: extract_pattern_traps, Jiazi/60 Pillars, Mandala, 11 Bereiche, Familie-2-Sätze, Therapie, ZEIT/Gezeiten
-->

# Plan 05 — Werkstatt

Selbsttragend. Warum jetzt: Nordstern-Fuß 3 (Prozess) ist nur ein **Tor**. Tiefe 1+2 auf `self_identity` liegen (Spiegel, Treffen). Die App beschreibt und fragt — sie zeigt noch nicht, **was du damit tun kannst**. Review 4: nächster Plan ist dieser, nicht Jiazi.

Verträge: [../vertraege/](../vertraege/) — Leitvertrag [werkstatt.md](../vertraege/werkstatt.md). Stimme [handbuch_stimme.md](../vertraege/handbuch_stimme.md). Einstieg [resonanz.md](../vertraege/resonanz.md). Safety [status.md](../vertraege/status.md).

Code-Repo: `code/inner_compass_app` (eigenes Git, Branch `cursor/astro-natal`). Pfade relativ zu `apps/web/`, wo Code.

## Was das nicht ist

| Verwechslung | Klarstellung |
|---|---|
| Tor vs. Seite | Phase 2: ein Satz „Ein Experiment dazu“ auf der Bereichsseite. Phase 5: Screen **WERKSTATT** (`/home/werkstatt`), von einer Karte aus, die du erkannt hast. |
| Brunnen/Leiter im UI | Produktstruktur intern. UI-Wörter erst nach Testern — Seite formuliert (Handbuch), keine Team-Labels Prisma/5D. |
| `extract_pattern_traps` | Neue Extract-Welle. Nicht dieser Plan. Material ist `payload.process.*` das schon liegt. |
| Familie 2 | `amplifies`/`clashes_with` weiter stumm. Filter = eigener Slice, nicht Werkstatt. |
| Jiazi / 60 Pillars | Content-Nachzug, eigener Schnitt nach Phase 5. Chunks liegen; 0 Interps. |
| Therapie | Anker = Körper / Sitzen-mit, kein Behandlungsanspruch. |

## Reihenfolge

1. Bestand lesen — *(D)* **erledigt 2026-09-15** (Tor, Stub-Page, `payload.process`, Resonanz)
2. Methodik — *(S)* **gehalten** (eine Domäne, formulieren, Safety, Resonanz als Einstieg)
3. Assemble + Route `/home/werkstatt` — *(D / S)* **erledigt 2026-09-15**
4. Browser Login-Person + zweite Geburt — *(D)* **belegt 2026-09-15** (Generator-Identität; Resonanz öffnet Versuch; Tor gekürzt)
5. Phasen-Review 5 — *(S)* **2026-09-15** — siehe [decisions.md](../../reference/decisions.md)

## Review-Check (2026-09-15, bestanden)

Tor auf der Bereichsseite, Versuch auf `/home/werkstatt`. EN-Prozess nicht als Absatz. Anker formuliert. Trap/Gift oft leer (Payload). Nächster Chat: Roadmap → Plan 06, nicht Jiazi parallel.

## 1) Bestand — *(D)*

Live: `lib/ic/domain-assemble.ts` (Workshop-Gate: Typ → Strategie → Autorität, EN-Seed → deutscher Entwurf). UI: `ic-domain-bereich-view.tsx` Abschnitt `ic-domain-workshop`. Vertragsweg `IC_SPACES.space_workshop` = `/home/werkstatt` — **keine Page**. Space-Copy: Vertiefen später, nicht von diesem Screen starten.

`payload.process.{trap, gift_activation, experiment_seed}` in HD-Interps. Anker hat **kein** Payload-Feld — Haltung/Copy, nicht Extract.

`ic_resonance`: Einstieg „von einer resonierten Karte“ = mindestens eine Antwort auf `self_identity` (Onboarding oder Bereich). Ohne Resonanz: ehrlicher Leerfall, kein erzwungenes Experiment.

Login-Testdaten: `test@makerkit.dev`. Geburten im Slice: 1980-11-18 19:20 Berlin (Projector) und 1978-11-10 19:20 Berlin (Generator). HD-Service `:8002`, Next `:3000`.

## 2) Methodik — *(S)* — vor dem Bau festhalten

- **Eine Domäne:** `self_identity`. Keine elf weiteren Tore.
- **Reihenfolge auf der Seite:** erst das Experiment (schon im Tor), dann was darunter liegt (Trap → Brunnen-Lesung, Gift → Leiter-Lesung), dann Anker als eine körperliche Einladung. Nicht Prisma, nicht 9 Schritte.
- **Formulieren, nicht übersetzen.** EN in `payload.process` nie als Absatz. Wie Gate: DE-Handbuch oder Entwurfshinweis.
- **Safety vor Tiefe 3–4:** kein Shadow/Trap als Diagnose; zweite Person; kein Urteil. Gate in Assemble (wie Status-Vertrag), nicht im Inspector.
- **Resonanz bleibt Ja/Teilweise/Nein** an der Bereichskarte. Werkstatt speichert keine zweite Scoreschicht.
- **Kein `generate_meta_nodes`.** Keine neuen Meta-Wörter außer Alltag (Experiment, woran du merkst, dass es sitzt).

## 3) Assemble + Route — *(D / S)*

- Page `app/[locale]/home/(user)/werkstatt/page.tsx` + View in `_components/ic-spaces/`. Handbuch-Lesesäule, nicht Dashboard.
- Lesen: dieselben HD-OS-Knoten wie das Tor; `sys_interpretations.payload.process` für das stärkste Element mit Material (Typ → Strategie → Autorität).
- Bereichsseite: Tor verlinkt zur Werkstatt, wenn Resonanz da ist; sonst bleibt der eine Satz.
- Space-Copy in `ic-spaces.ts` anpassen, sobald die Page existiert.
- System-Chart-Assemble (`lib/hd|astro|ziwei|bazi/*-assemble.ts`) nicht anfassen.

## 4) Browser — *(D)*

Wie Plan 02/04: Docker, Supabase `:54321`, HD `:8002`, Next `:3000`. Login wie oben.

Fragen: Liest sich Tiefe 3–4 wie Arbeit mit dir oder wie Inspector-Prozess-JSON? EN/Canonical-IDs? Therapie-Ton? Einstieg ohne Resonanz ehrlich leer? Bereichsseite + Onboarding + Treffen unverändert? Generator und Projector beide betretbar?

Kein E2E. Zweite visuelle Runde (Desktop + schmal) laut Handbook-UI.

## 5) Phasen-Review 5 — *(S)* — **2026-09-15, geschrieben**

Volltext: [decisions.md](../../reference/decisions.md) „Phasen-Review 5“. Kurz:

1. Resonanz = Tür, kein Füllstand. Irgendeine Antwort auf `self_identity` öffnet den Versuch; `no` zählt als erkannt.
2. Tor ≠ Seite. Bereich: ein Satz + Link. Werkstatt: Experiment + Anker; Trap/Gift nur bei brauchbarem `payload.process`.
3. UI-Wörter Alltag (Versuch, Körper). Brunnen/Leiter/Gabel nicht auf der Fläche.
4. Formulieren vor Seed. EN-`experiment_seed` nie als Absatz.
5. Eine Domäne. Weitere Werkstätten erst mit dem jeweiligen Bereich.
6. **Nächster Plan = 06** ([06_karte_belegung.md](06_karte_belegung.md)): KARTE-Belegung, nicht Jiazi parallel, nicht elf Handbuch-Seiten.

Offenes (Jiazi, Familie 2, Worker-Enums, Trap/Gift-DE) bleibt in `roadmap.md` mitgeschleppt.

## Erwartetes Ergebnis

Auf `/home/werkstatt` eine Handbuch-Seite zu `self_identity`: Experiment + darunterliegende Lesung + Anker. Material aus vorhandenem `payload.process`. Tor auf der Bereichsseite bleibt und führt hin.

## Nicht

Jiazi-text2kg, Staffel 2 *60 Pillars*, `extract_pattern_traps`, Familie-2-Sätze, Mandala, zwölf Bereiche, DE-Atome-Welle, Luck-Pillar-UI, ZEIT, Spark-Qwen, `supabase db reset`, Merge `main`, Force-Push, `.env*`/`_tmp_*`.
