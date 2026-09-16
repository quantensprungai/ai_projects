<!--
Reality Block
last_update: 2026-09-15
scope: Phasen-Plan 4 — Cross-Kanten in einer Domäne
in_scope: Familie 4 auf self_identity, Enum, kuratierter Seed, Tiefe-2-Satz aus Kanten, Browser-Beleg
out_of_scope: Jiazi/60 Pillars, text2kg, extract_relationships, Familie-2-Nutzung, Mandala, 12 Bereiche, Transite/Luck Pillars, generate_meta_nodes, Werkstatt-Seite
-->

# Plan 04 — Cross-Kanten

Selbsttragend. Warum jetzt: Vier natal Quellen stehen auf `self_identity`. Tiefe 2 („Wo sich die Quellen treffen“) hängt noch am Status-Gate „zwei UI-taugliche Quellen“, nicht an Kanten. Nordstern-Fuß 2 (Konvergenz) ist damit nicht gebaut.

Verträge: [../vertraege/](../vertraege/) — Leitvertrag [kanten.md](../vertraege/kanten.md). Decision 2026-09-13: Jiazi-KG kein Blocker.

Code-Repo: `code/inner_compass_app` (eigenes Git, Branch `cursor/astro-natal`).

## Was das nicht ist

| Verwechslung | Klarstellung |
|---|---|
| Familie 3 vs. 4 | Familie 3 = `belongs_to_domain` (Element → Lebensbereich). Liegt. Familie 4 = Treffen **zwischen** Elementen **in** einer Domäne. |
| Chunks / 60 Pillars | Literatur-Atome für `bazi.jiazi.*`. Nicht nötig, um zwei Lage-Sätze zu kanten. |
| Transit vs. Natal | Phase 4 = **Natal**-Knoten der Person in einer Domäne. Transite, 流年, Luck Pillars, ZEIT = später (Roadmap Phase 6/7). |
| Familie 2 | `amplifies`/`clashes_with` intra HD. Bleibt stumm (Fan-out, Widerspruch). Filter = eigener Slice **vor** Familie-2-Sätzen, nicht Plan 05. |
| Alte `maps_to` | 143 Gene Keys→HD, `intra_system`/`approved`. Die 3 echten `cross_system` sind `amplifies`/`clashes_with` (Ko-Erwähnung). Beides nicht Familie 4. |

## Reihenfolge

1. Bestand lesen (maps_to, Assemble Tiefe 2, Enum) — *(D)* **erledigt 2026-09-15**
2. Methodik + Seed der Paare für `self_identity` — *(S)* **klassifiziert 2026-09-15**, Datei da; Write in die DB = Todo 3
3. Enum + Assembler liest Familie 4 — *(D / S)* **erledigt 2026-09-15** (DB-Spalte `text`, kein CHECK; Seed-Skript + Assemble)
4. Browser auf der Login-Person — *(D)* **belegt 2026-09-15** (Projector+Yi Treffen; Generator+Bing Leerfall)
5. Phasen-Review 4 — *(S)* **2026-09-15:** Rollen-Kanten alle Typen × Eingang/Lebensort; Jiazi nicht vor Plan 05. Siehe [decisions.md](../../reference/decisions.md).

## 1) Bestand — *(D)* — **gelesen 2026-09-15**

Live-DB (lokal), Code `domain-assemble.ts` / `handbook-voice.ts`. Nichts geseedet.

### Familie 3 — nicht nur BaZi

| System | `belongs_to_domain` | Was |
|---|---|---|
| HD | 30 `approved` | Typ, Strategie, Autorität, Profil → `self_identity` |
| HD | 418 `candidate` | Inhaltlich aus `payload.life_domain`. Assemble nimmt `approved` zuerst — ungenutzt auf der Seite |
| Astro | 13 `approved` | 12 Häuser, Haus 8 doppelt |
| Ziwei | 12 `approved` | 12 Paläste |
| BaZi | 10 `approved` | nur Day Master |
| Jyotish / Maya / … | 0 | kein Nachzug in Phase 4. Erst wenn diese Systeme eine Bereichsseite speisen (Phase 6) |

Strukturelles Routing der **vier Live-Linsen** ist fertig. Kein flächendeckendes Nacharbeiten.

### Familie 2 — die 445

Login-OS-Set: `hd.type.projector`, `hd.authority.splenic`, `hd.profile.3_5`, `hd.center.g`, `hd.center.spleen`.

| Schnitt | Zahl (heute = 2026-09-04) |
|---|---|
| beide Enden im Set | **11** |
| inzident (ein Ende im Set) | **445** |

Quelle: Backfill 2026-08-05 aus `payload.interactions` (`ic_kg_edges_backfill_from_interactions.py`). Alle `candidate`, `intra_system`. Gesamtkorpus: ~13k `amplifies`/`depends_on`/`clashes_with`. **Nicht löschen.** Mechanisch korrekt als „das LLM hat im HD-Text Verweise gesehen“. Unbrauchbar als Handbuch-Satz: Fan-out, G↔Milz gleichzeitig `amplifies` und `clashes_with`. Geplant war Read-Time-Overlay, nie gebaut. Filter = Phase 5, nicht Phase 4.

Die 11 internen (ohne Interp-ID in `metadata`): Milz hub; Typ nur als Ziel von `spleen amplifies projector`; `spleen clashes_with g` parallel zu `amplifies` beide Richtungen.

### Familie 4 / `maps_to`

- `converges` / `complements` / `contradicts`: **0**. Enum in `contracts.md` §5 noch ohne diese Typen.
- `maps_to`: **143**, alle `genekeys`→`hd`, `approved`, fälschlich `edge_scope=intra_system`. Nicht anfassen in diesem Plan.
- Echte `cross_system` (3, `candidate`): `bazi.ten_god.zhengcai`/`piancai` —`amplifies`→ `hd.center.throat`; `hd.gate.46` —`clashes_with`→ `gk.gene_key.64`. Ko-Erwähnung, keine Methodik.

### Assemble / Login-Person

Eine Karte pro System. HD-Rang: Typ vor Strategie/Autorität/Profil. Astro: `house.1`. Ziwei: `soulPalace`. BaZi: `day_master.*`.

`uiReady` = DE-Wording **oder** HD-Keil (`hd.type.*` / `hd.strategy.*`). Astro/Ziwei/BaZi ohne DE-Atom → nicht uiReady. `composeMeetingSentence` braucht ≥2 uiReady → auf dieser Person **heute null**, ein hartkodierter Satz ohne Kantenart.

Tiefe 2 liest **keine** `sys_kg_edges` außer Familie 3 (Routing).

Nächster Schritt: [05_werkstatt.md](05_werkstatt.md).

## 2) Methodik + Seed — *(S / D)* — **Paare 2026-09-15, Write = Todo 3**

**Einheit:** Katalog-Knoten, beide strukturell in `self_identity`. Sichtbar nur wenn **beide** Enden im Natal-Chart liegen. Die Login-Person ist der **erste Schnitt** (vier Live-Quellen), nicht der einzige Graph. Andere Typ×Tagstamm-Paare fehlen absichtlich — leeres Treffen, bis klassifiziert.

**Genealogie (Gewicht, nicht die Kantenart):**

| Paar-Wurzel | `strength` |
|---|---|
| HD ↔ Astro (tropisches Rad unter HD) | `low` |
| Astro ↔ Ziwei (beide 12-Teilung) | `low` |
| HD ↔ Ziwei, alles mit BaZi | `strong` |

HD sitzt **nicht** auf dem Palastkreis. Frühere Zeile „HD-OS wie Astro-Zwölfteilung“ war falsch.

**Klassifikation an den Handbuch-Sätzen (v1), nicht an Atomen:**

| A | B | Art | Gewicht | Warum nicht `converges` |
|---|---|---|---|---|
| `hd.type.projector` | `astro.house.1` | `complements` | low | Einladung vs. Eingang |
| `hd.type.projector` | `ziwei.palace.soulPalace` | `complements` | strong | Einladung vs. Lebensort |
| `hd.type.projector` | `bazi.day_master.ji` | `complements` | strong | Sehen-wenn-gemeint vs. tragen aus dem Vorhandenen (Ji-Personen) |
| `hd.type.projector` | `bazi.day_master.yi` | `complements` | strong | Sehen-wenn-gemeint vs. biegsam umgehen (diese Testdaten) |
| `astro.house.1` | `ziwei.palace.soulPalace` | `complements` | low | Eingang vs. Lebensort; zwei Meta-Begriffe |
| `astro.house.1` | `bazi.day_master.ji` | `complements` | strong | Eingang vs. Tagstamm |
| `astro.house.1` | `bazi.day_master.yi` | `complements` | strong | Eingang vs. Tagstamm Holz |
| `ziwei.palace.soulPalace` | `bazi.day_master.ji` | `complements` | strong | Lebensort vs. Tagstamm |
| `ziwei.palace.soulPalace` | `bazi.day_master.yi` | `complements` | strong | Lebensort vs. Tagstamm Holz |

Kein `contradicts` in diesem Schnitt (nicht erzwingen). Kein `converges`: dieselbe Domäne ≠ dieselbe Aussage. Das ist die Antwort auf „es gibt immer Ähnlichkeiten“ — Art und Gewicht trennen Klumpen von Versatz und von billiger Rad-Verwandtschaft.

Datei: [../../system_structure/self_identity_cross_v0.json](../../system_structure/self_identity_cross_v0.json). In die DB erst mit Todo 3 (Enum muss existieren). Evidence = Datei+Zeile + `handbook-voice-v1`.

Muster für später: **pro Domäne** (Phase 6), nicht pro System-Welle. Jyotish kommt dazu, wenn es eine Bereichskarte speist.

## Klärungen (2026-09-15)

**445 / Fan-out:** Der Interactions-Backfill ist **katalogweit** (~13k). „11 / 445“ ist nur der Schnitt der Login-OS-Knoten. Jede Person mit denselben HD-OS-Knoten sieht denselben Ausschnitt. Entstanden: eine Interp nennt mehrere `elements[]` / `interactions` → viele Kanten; Prompt erzwingt keine Gegenseitigkeit. G↔Milz `amplifies` und `clashes_with` kann in HD-Text beides vorkommen. Reparatur = Filter beim Lesen (Phase 5), kein Massen-Delete.

**Haus 8 doppelt:** Absicht — und **Muster, keine Anomalie**. Die 12 Enums sind kein System-Rad. Astro: Haus 8 → zwei Domänen, Häuser 8+12 → dieselbe Domäne. Ziwei: je zwei Paläste → `family_home` / `exchange_learning`, zwei Domänen ohne Palast. Jyotish (später): ein Bhava → oft drei Domänen. HD/BaZi: kein Rad. Multi-Map ist die Regel (Decision 2026-09-04); Haus 8 ist nur der Fall, der als „13“ auffällt.

**418 `candidate`:** Inhaltliches HD-Routing in alle 12. Nicht säubern in Phase 4. Braucht Phase 6. Stichprobe später ok, kein Wipe.

**`maps_to` 143 GK→HD:** Klasse **definitional** (gleiche Hexagramm-Nummer), nicht Konvergenz. `edge_scope=intra_system` ist falsch beschriftet — stehen lassen, bis ein Hygiene-Slice nur den Scope dreht. Nicht als Familie 4 lesen.

**3 Ko-Erwähnungen:** Nebenprodukt des Backfills, nicht der geplante KG-Overlay. Der Overlay ist Familie 4 + später Meta-Knoten. Embedding auf Synth-Text ist in [cross_system_mapping_methodology_review.md](../../reference/cross_system_mapping_methodology_review.md) verworfen (alles klingt nach shadow/flow). v0 = kuratierte Paare + Genealogie-Gewicht.

**ohne DE / uiReady:** Handbuch-Lage ist schon DE und sichtbar. `uiReady` meint DE-**Atom** oder HD-Keil. Fertigmachen in Phase 4 = Lage-Sätze ins Treffen lassen (Todo 3), **keine** DE-Re-Synth-Welle. Mix Atome EN / Chrome+Handbuch DE bleibt Vertrag.

**Nie gebaut (nicht nachholen in 04):** `extract_relationships`; Overlay-Retrieval; `extract_pattern_traps` / `sys_dynamics`; `generate_meta_nodes`; Embedding-`maps_to`; Familie-2-Filter; Jiazi-text2kg; Luck/ZEIT; Mandala; 11 weitere Bereichsseiten. Catch-up nur nach Phasen-Review.

**Review vor Bau (2026-09-15, S):**
- *Skelett ≠ Kernmoment.* Familie-4-Kanten sind personenunabhängige Katalog-Struktur. Der Nordstern-Moment „drei Traditionen sehen dasselbe bei *dir*“ braucht zusätzlich Read-Time über konkrete Aktivierungen + Evidence-Zitate (Decision 2026-08-05, nie gebaut). Plan 04 baut das Skelett. Nicht als „Konvergenz fertig“ lesen.
- *`converges` wird auf OS-Ebene selten feuern.* Typ, Eingang, Lebensort, Tagstamm messen Verschiedenes → v0 ist fast nur `complements`. Ehrlich, aber das Versprechen „Klumpen“ lebt erst mit feinerer Körnung (Tor × Stellung) oder Literatur. Im Browser nicht so tun, als wäre Versatz der Klumpen.
- *`strength` ist semantisch geliehen* (gebaut für Wirkungsstärke intra-system). Für Familie 4 = Unabhängigkeit der Wurzeln. Zusätzlich `metadata.independence` schreiben, damit die Bedeutung nicht in der Spalte verschwindet.
- *Astro↔Ziwei `low`* ist ein Urteil, keine Genealogie: Paläste rechnen aus Mondmonat/Stunde, nicht aus der Ekliptik. Gemeinsam ist nur die Zwölfteilung als Form. Bei Review 4 prüfen, ob `medium` ehrlicher ist.
- *Sechs Kanten decken eine Kombination.* Ein Generator mit Jia sieht ein leeres Treffen. Todo 4 muss eine **zweite Person** zeigen, damit der Leerfall sichtbar wird. Review-4-Decision: Wildcard-/Rollen-Kanten (Typ-Klasse ↔ Haus 1) vs. weiter kuratieren. Kein Spray vorher.
- *Phase 6 wird dünn ohne Routing-Nachzug:* BaZi hat nur Day Master → `self_identity`; HD nur OS. Für `money_resources` etc. spricht BaZi strukturell nicht. Vor Wiederholung des Familie-4-Musters pro Domäne: Ten Gods/Wealth-Sterne bzw. HD-Content-Kanten routen. In Roadmap Phase 6 notiert.
- *Reihenfolge stimmt.* Erst Mechanik (Kante → Satz) auf einer Domäne, dann Content, dann Breite. Es geht nichts verloren, solange 445/418/143 stehen bleiben und Jiazi-Chunks liegen.

**Sprache nicht auf EN zurückdrehen.** KG bleibt Quellsprache. UI/Handbuch formulieren in der App-Locale. Weitere Sprachen = Chrome-Locale + Formulierung, kein zweiter KG.

## 3) Enum + Assembler — *(D / S)*

- Types/DB: drei Relationen in Enum aufnehmen (Migration + `contracts.md` §5). Alte `maps_to` bleibt im Enum, ungenutzt.
- `domain-assemble.ts`: Tiefe 2 nur bei **mindestens einer** Familie-4-Kante zwischen zwei auf der Seite sichtbaren Quellen. Nicht mehr „zwei uiReady, also ein Satz“.
- Satz **formulieren** aus den schon gebauten Lage-/Keil-Karten + Kantenart. Kein Atom übersetzen. EN-Absatz weiter Gate.
- `uiReady` nur HD? Dann bleibt der Satz leer, **außer** Lage+Entwurf zählt als sichtbare Quelle fürs Treffen (nicht als Atom-Prosa). Default in diesem Plan: **Lage-Sätze dürfen ins Treffen**, solange kein EN-Absatz. Sonst ist Phase 4 auf dieser Person unsichtbar.
- Filter-Chips unverändert. Eine Karte pro System bleibt.
- Familie 2 nicht lesen. `experiment_seed`-Fallback (Typ→Strategie→Autorität) **nur** wenn diese Datei sowieso angefasst wird — nicht eigener Scope, aber erlaubt als Mitnahme laut Roadmap-Offenes.

`generate_meta_nodes` nicht. Meta-Wörter nur in [handbuch_stimme.md](../vertraege/handbuch_stimme.md), falls ein Treffen-Satz ein fünftes/sechstes braucht.

## 4) Browser — *(D)*

Voraussetzungen wie Plan 02: Docker, Supabase `:54321`, HD `:8002`, Next `:3000`. Login `test@makerkit.dev` / `testingpassword`, Person 1980-11-18 19:20 Berlin.

Fragen: Sieht Tiefe 2 wie ein Handbuch-Treffen aus oder wie ein Graph-Dump? Steht die Kantenart lesbar (gleiche Aussage / andere Facette / Widerspruch) ohne Canonical-IDs? Ist BaZi↔andere Quelle **schwerer gewichtet** bzw. als eigene Wurzel kenntlich, HD↔Astro nicht als Wahrheitsbeweis? Leerfall wenn keine Kante? System-Charts unverändert? Resonanz unangetastet.

**Pflicht: eine zweite Person** mit anderem Typ oder Tagstamm (z. B. Generator, Jia) — der Leerfall des Treffens muss sichtbar sein, sonst ist die Spray-Frage bei Review 4 nicht entscheidbar. Kein E2E. 3–5 fremde Charts darüber hinaus optional.

## 5) Phasen-Review 4 — *(S)* — **2026-09-15**

Sieben Verträge gegen Code. Decision in [decisions.md](../../reference/decisions.md) 2026-09-15.

1. Rollen-Kanten: alle fünf HD-Typen × Eingang und × Lebensort. Leerfall = fehlende Quelle, nicht anderer Typ.
2. Keine 5×10 Tagstämme; BaZi-Paare nur Ji/Yi in v0.
3. Lage darf ins Treffen. Kernmoment ungebaut.
4. Jiazi/60 Pillars nicht vor Plan 05. Nächster Plan = Werkstatt.
5. Astro↔Ziwei `low` bleibt in diesem Cut.

## Review-Check (2026-09-15, bestanden)

Treffen aus Familie 4 auf der Login-Person (Projector+Yi). Generator ohne Typ-Paare war leer, danach Rollen-Kanten. Nächster Chat: [05_werkstatt.md](05_werkstatt.md).

## Erwartetes Ergebnis

Auf `self_identity` ein Treffen-Block, der aus **Familie-4-Kanten** kommt, mit unterscheidbarem Klumpen (`converges`) vs. Versatz (`complements`) vs. Widerspruch. BaZi darf die teure Kante sein. Katalog bleibt klein.

## Nicht

Jiazi-text2kg, Staffel 2 *60 Pillars*, Spark-Qwen, `extract_relationships`, Familie-2-Sätze, Luck-Pillar-UI, ZEIT füllen, zwölf Bereiche, Mandala, DE-Atome-Welle, `supabase db reset`, Merge `main`, Force-Push, `.env*`/`_tmp_*`.
