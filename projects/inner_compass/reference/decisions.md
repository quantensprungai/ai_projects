# Inner Compass — Design-Entscheidungen

## 2026-09-02: Astro Relink nach text2kg + scoped Häuser/Achsen-Synth

**Kontext:** 14/14 natal text2kg completed. Erster Ground-Synth (25 EN) hatte MC, nicht AC/DC/IC. text2kg erweiterte `interpretation_ids`, setzte `interpretation_link_roles` nicht. Dry-Relink: alle Ground-Nodes würden sich ändern. Achsen-Stubs (`"AC"`). 7 Planeten schon Cap-6 Primaries + Wordings.

**Decision:**

1. Relink `--apply` auf das **ganze** Relink-Set (`astro_natal_relink_v1` 58/58), nicht nur Ground.
2. Scoped Synth **nur 16 IDs:** 12 Häuser + `astro.angle.ascendant|descendant|midheaven|imum_coeli` via `ic_k2_synth_batch.py --force --only-id` (Langdock gpt-5-mini, EN). **Nicht** `ic_astro_natal_synth.py` — das syncht alle 28 Ground-IDs inkl. Planeten.
3. **7 Planeten nicht `--force`.** Inspector funktioniert; Re-Synth wäre Würfeln.
4. AC/DC/IC/MC Atome EN First Cut (desc 433–587, Wordings 776–904). DC 4 Primaries (dünneres Material). Häuser Cap 6.

**Nicht:** Full-Synth, Overlay, DE-Atome, Planeten-Re-Synth, later-PDFs classify, Merge `main`.

---

## 2026-09-02: Astro-KARTE Rad — Körper-Selektion, Jobs ≠ Chunks

**Kontext:** Seed 71, Relink `astro_natal_relink_v1`, Ground-Synth 25 EN lagen. Rad zeigte Linien bei Mond-in-Widder, kaum bei Sonne-in-Skorpion / AC-in-Krebs. Queue-Zähler „269“ klang nach Chunks.

**Decision:**

1. **Rad.** Tropisch + Whole Sign, Engine **celestine** (nicht sidereal). AC links. Körper auf ekliptikaler Länge. **Klick auf Körper** → nur seine Major-Aspekte (Slice 24). Hausklick = keine Linien. Konjunktion im selben Haus = Mini-Chord, kein Bug. AC-Atom bleibt dünn (Ground-Synth: MC, nicht AC). Inspector = Typ-Atome, Chrome DE, **kein Overlay**.
2. **269** = completed `extract_interpretations`-**Jobs** über alle Systeme, nicht Chunks. Batch 50. Astro-Soll ≈ 14 Natal-Werke / ~3,6k+ Chunks minus mixed-skip.
3. **HD-Zombie** `5ba2f841` (Bunnell *Definitive*, `running` seit 2026-08-10) nicht canceln unless asked. Blockiert den Astro-Worker nicht.
4. **SoT:** `reference/astro_natal_ingest_runbook.md`. Branch `cursor/astro-natal`.

**Nicht:** Linien fürs ganze Rad oder per Zeichen; Overlay/Mandala; Jyotish parallel; DE-Atome; Full-Synth; Spark-Qwen; later-PDFs classify.

---

## 2026-09-01: Astro K2 aus Katalog — Typen seeden, Instanzen nicht

**Kontext:** Extract-ahead (MinerU) läuft. Skeleton-Seed war 39 hardcoded Nodes (`astro.aspect.conjunction` statt Katalog `astro.aspect_type.*`). Playbook sagt Seed aus `*_catalog_v0.json` vor text2kg. Frage: Katalog vs Engine-Instanz vs First Cut.

**Decision:**

1. **Drei Schichten.** (1) `astro_catalog_v0.json` = endliches Typ-Lexikon für Literatur/text2kg (~71 IDs: Körper/Punkte, Achsen, Zeichen, Häuser, Aspekt-*Arten*, Würden, Freuden, Sekte). (2) Engine-Instanz (`computeAstroChart`) erzeugt Placement/Paar-Aspekt/Chart-Ruler zur Laufzeit — **nicht** seeden. (3) First Cut = Produktfläche + Atomqualität, kein halber Katalog.
2. **Seed jetzt aus Katalog.** `build_astro` liest Catalog + intra-Kanten aus `astro_structure_v0.json`. Whitelist `ic_astro_k2_catalog.py`, `IC_TEXT2KG_STRICT_ASTRO=true`. Aliase `astro.aspect.*` → `astro.aspect_type.*`. Reject: `astro.placement.*`, `astro.aspect.*__*`, Progression/Synastrie.
3. **life_domain_map** in `astro_structure_v0.json` mit **contracts.md §2-Enums** (wie Ziwei). Katalog-`houses[].life_domain` bleibt Drift (nicht umschreiben). Haus 8 → `sexuality_intimacy` + `transformation_renewal`; Haus 12 → `transformation_renewal`. `maps_to_element` → `we.element.*` nicht seeden (cross-system, Ziel nicht im Astro-Seed).
4. **Alte 5 `astro.aspect.*`-Skeleton-Nodes** gelöscht 2026-09-01 (0 Interps). Alias `astro.aspect.*` → `aspect_type` bleibt in der Whitelist.
5. **Kein physisches PDF-Split.** Ein Extract, alle Chunks bleiben. Natal-First-Cut verdrahtet Mixed-Kapitel (Lilly II, Carmen IV/V) **nicht** an Natal-Atome. Transit/Horary = **zweite KG-Welle auf denselben Chunks**, kein zweites MinerU. Ganzes Timing-Werk: `wave` retaggen (Teachings `921e728e`). `ingest_note` ist Merker, kein Filter.

**Nicht:** Kombinations-Nodes (`sun_aries`, `sun__moon__trine`), Katalog-Enum-Rewrite, MinerU unterbrechen, Spark-Worker für Whitelist neu deployen (Extract braucht das File nicht), Bücher in Natal/Transit-PDFs zerschneiden.

---

## 2026-08-31: Astro nächste KARTE — Extract-ahead, Transit/Horary/Psychologie getrennt

**Kontext:** Ziwei-KARTE First Cut geschlossen. Nächste **App-Fläche** = westliches 12-Häuser-Rad (Astro), nicht BaZi-UI und nicht Jyotish. Frage: welche lokalen Werke durch MinerU, was analog HD-Transit / 流年 draußen bleibt.

**Decision:**

1. **Extract-ahead jetzt, volle KG-Kette nicht.** Acht unique PDFs → Spark MinerU `extract_text`, `extract_ahead=true`, kein classify/text2kg/Relink/Synth. Seed+Whitelist+Katalog-Drift erst vor der Astro-System-Welle / KARTE-UI.
2. **Drei Park-Wellen neben Natal:** `astro_transit` (Hand *Planets in Transit*), `astro_psychological` (Rudhyar), `astro_horary` (Lilly Book II — PDF liegt, nicht extra extractet, steckt in den 3 Bänden). Worker `_parks_kg_downstream`. Gleiche Begründung wie 流年: Timing- oder Fremdschul-Sätze dürfen nicht an Haus/Planet-Natal-Atome.
3. **Erste Tradition = hellenistic/medieval** (Ptolemy Book I, Dorotheus, Lilly natal, George Vol I+II). Clark 2006 = Epitome-Tag, kein zweiter Primärtext. 三合-Analog: Rudhyar nicht in denselben Wording-Topf.
4. **Duplikate nicht nochmal MinerU:** Lilly Book II standalone; `astro/K2/` = Ptolemy root; `astro/K4/` = Clark root. George 2019 in `archiv/` ist **Vol I**, 2022 in `astro/` ist **Vol II** — beide.
5. **Registry-Lücken nicht in dieser Welle beschaffen** (Brennan, Houlding, Sasportas, Tompkins, Arroyo, Valens, …).
6. **SoT:** `reference/astro_natal_ingest_runbook.md`. Skript `ic_astro_natal_upload.py`.

**Nicht:** Astro-UI, Enum-Rewrite prophylaktisch, Jyotish parallel, Horary-KG, Transit-UI, Full-Synth, Spark-Qwen.

---

## 2026-08-31: Agent-Schichten getrennt — FLOP nicht Produktwährung

**Kontext:** Überlegung, FLOP (Hayes) und „Agent Protocol“ (Cloudflare/Isenberg) in IC zu ziehen: User, fremde Agents, eigene Protagonisten-Agents, Airdrop-Testnet. Vision §7 (MCP-Readiness 2027) existiert schon; Makerkit-MCP ist Dev, nicht Produkt.

**Decision:**

1. **Vier Leitungen, nicht ein Token.** (1) Mensch zahlt IC. (2) Fremder Agent zahlt für KG/Tools (MCP + metering). (3) Mensch spricht mit IC-Protagonist. (4) IC-Agent kauft Compute. FLOP gehört höchstens zu (4), Cloudflare/MCP zu (2), Virtuals-artig zu (3).
2. **Produkt-MCP ist die echte „Protocol-Readiness“** — saubere Tools auf Chart/Synthesis/Zyklen, frei/bezahlt/blockiert, später Wallets. Nicht bauen, bevor eine öffentliche, nicht-private Ressource existiert (KARTE/Handbuch zuerst, Decision 2026-08-27).
3. **FLOP bleibt Lab.** Testnet/Airdrop darf als Adapter-Experiment gegen Langdock laufen. Kein FLOP in Schema, Billing, Onboarding, Login.
4. **Protagonisten** (Aria/Jian/…) erst auf echtem KG; Tokenisierung/Anteile nicht vor nachweisbarer Tool-Nutzung.
5. **SoT:** `reference/agent_surface_and_monetization.md`. Zeitenwende-Geopolitik (Hayes YCC) bleibt dort.

**Nicht:** FLOP-native App, Character-Coin ohne Inhalt, Dev-MCP als Agent-Tür verkaufen, Pay-per-Crawl vor öffentlicher Resource-Schicht.

---

## 2026-08-27: Ziwei-Natal wie HD — nicht UI-first

**Kontext:** Nach dem HD-Handbuch-Keil (C→B) lag der Impuls nahe, ein leeres 12-Palast-Gitter als „Basis“ zu bauen. Genau das Slice-Problem: KI setzt auf halbem Gerüst auf. 13 中州-PDFs sind lokal inventarisiert und queued, **0 ingestiert**. HD/BaZi-Pipeline-Fallen (Seed nach PDF, Auto-Synth, Interp-Dump in die UI, Spark-Qwen als Default) waren im ersten Ziwei-Schnitt zu weich.

**Decision:**

1. **Pfad A — Natal-Parität.** Nicht B (大限/流年 vor UI). Nicht C (HD-Transit zuerst). Compute = iztro, ein `ziwei.*`-Baum. Kit ≠ Ontologie.
2. **Erste Tradition = 中州 / 王亭之** (`tradition=zhongzhou` auf den 13). 三合/飞星 = Tags, nicht zweite Engine. Tu Vi = Locale, gleiches `system_id`.
3. **13 lokale Werke = Staffel 1**, Queue-CSV Zeilen 121–133. **12 Natal ingestieren, 流年凶灾详析 parken** (Jahres-Timing, analog HD-Transit). **深造讲义 ist Natal-wichtig** (进阶-Paar zur 初级); ~158 MB = Scan-Gewicht, eigenes MinerU-Fenster mit `PAGE_BATCH`, nicht wie 流年 behandeln. Juli-CSV „中州派-Kern komplett“ war **zu früh** — 四书/安星-Prosa/格局-Namen fehlten. **Welle 1b** (lokal `ziwei/neu/`): 安星法, 谈斗数, 八喜楼与格局, 骨髓赋, 太微赋-Kurznote. 四书 Band 1 (太微+形性 Satz) nicht Blocker. Have/Missing: `reference/ziwei_natal_ingest_runbook.md`.
4. **Staffel:** Seed+Whitelist → 初级+星曜性质 (Smoke) → 深造 (eigenes Extract) → 补注 → 全集. Nicht alle 13 als P0 dumpen.
5. **HD-Gates Pflicht:** K2-Seed **vor** PDFs; `IC_TEXT2KG_STRICT=true`; **`IC_TEXT2KG_STRICT_ZIWEI`** (Whitelist `ic_ziwei_k2_catalog.py`); `IC_TEXT2KG_AUTO_SYNTH=false`; Relink `link_role`; scoped Synth, Canon-first. UI liest Atom/`primary`, kein Interp-Dump.
6. **LLM-Standard = Langdock** (`gpt-5-mini`, `ic_start_langdock_worker.py` / `ic_run_with_langdock.py`). Spark nur MinerU/`extract_text`. `IC_LLM_URL` nicht auf Spark `:30001` / Qwen. SGLang für diese Welle nicht starten.
7. **MinerU:** `IC_MINERU_LANG=ch` (nicht `latin`). `IC_MINERU_PAGE_BATCH=50`. **Kein** `IC_CHUNK_PROFILE=rave_iching_gates`. Spezialprofil `ziwei_stars_palaces` erst nach TOC-Smoke. Classify-Tag = `ziwei`.
8. **Zeitvertrag:** iztro `bySolar(gregorianisches Wanddatum, 时辰-Index, Geschlecht)` — Geo/TZ ignoriert. Berlin und Shanghai 09:00 gleiches Kalenderdatum → gleiches Plate. `isoDateToSolarString` nur `YYYY-MM-DD`, kein `Date()`-Fallback. Unbekannt 12:00 = 午时, kommunizieren. 真太阳时 später.
9. **Geschlecht** in `user_persons` ist Blocker: ohne 男/女 kein Plate.
10. **Git:** HD-Slice auf bestehendem Docs-Branch einfrieren. Ziwei-Arbeit auf `cursor/ziwei-natal` (Docs vom Freeze-Tip, Code von `cursor/makerkit-v4`). **Nicht** zuerst auf `main` mergen (Makerkit 4 / KARTE liegen nicht auf Code-`main`).
11. **UI** `/home/karte/ziwei` erst wenn Palast/Hauptstern-Atome `verified` oder bewusster `canon_fallback`. Hub-Linse live.

**Nicht:** Mandala, Handbuch-Generator, 大限/流年-UI, BaZi-Klassiker-Ingest parallel, Jyotish-UI, HD-Transit-UI, `classify_domain` umbenennen, Spark-Qwen als Interpret/Synth, 深造 wegen MB skippen.

**Nachtrag 2026-08-28:** 初级-Smoke (pipeline, Qwen/SGLang aus) lieferte 125 Chunks. Cover/TOC-OCR (`液`/`人`) ist Scan, nicht Chunk-Größe. **Wörterbuch-Nachkorrektur gegen K2 für alle Natal-Werke, vor text2kg** — Details `reference/ziwei_natal_ingest_runbook.md`. Extract-Staffel bleibt: 星曜 → 深造 eigenes Fenster → 补注 → 全集; nicht alle PDFs parallel.

**流年 2026-08-28:** Das 13. Werk darf MinerU jetzt mitlaufen (`wave=ziwei_liunian`), damit der Scan nicht später fehlt. **Nicht** in natal-text2kg/Relink/Synth — gleiche `ziwei.*`-Whitelist würde Jahres-Timing in Palast/Stern-Atome mischen (HD-Transit-Analog). Classify-Job nach Extract verwerfen, bis eine 流年-Welle existiert.

**Welle 1b 2026-08-28:** Nach Korpus-Lücken (格局-Namen, 安星-Prosa) nachgelegt, nicht weil die 13 falsch waren. Ingest **nach** Staffel-1 Interpret/text2kg, nicht parallel. 别序/yuceweb und Motivations-格局 nicht ingestieren.

**Nachtrag 2026-08-29 — Natal-First-Cut + KARTE-Gitter liegen:** Staffel 1 + Welle 1b sind durch (Extract/OCR/Langdock/text2kg, Homophone, Palast v2, 四化, 辅星 Relink, scoped Synth EN). Atome sind First Cut / `synth_draft`, nicht `verified`. **Qualitätsschulden und was nicht nachziehen:** `reference/ziwei_natal_ingest_runbook.md` § Stand + Qualität. Gitter: `/home/karte/ziwei`. Nicht von allein: 来因, Band 1, restliche Palast-Re-Synth, DE-Atome, 流年-KG, Mention-Bloat-Repair, Full-Synth.

**Nachtrag 2026-08-31 — dichte Platte + Zusammenschau v3 + Kleinstern-Lexikon + Palast-Re-Synth:** Chrome DE; Overlay `ziwei_overlay_v3` (Lebenssatz+Belege, keine EN-Buchdumps). Langdock: Key in `.env.development.local`, BASE_URL+Modell in `.env.development`. Kleinstern: 20 EN mit primary. Paläste+身 scoped Re-Synth; 命宫 „Life Palace“; 化权 Authority; 天钺 Patronage (`tianyueMin`; EN-Pinyin bis DE). **Extract-ahead 2026-08-31:** MinerU darf PDFs weiterer Systeme scannen (`extract_text` + `wave=`), während ein System KARTE/KG macht. Volle Kette (classify→text2kg→relink→synth) bleibt **ein System nach dem anderen**; Seed+Whitelist vor text2kg; Classify nach Extract parken. SoT: `cursor/reference/k2_foundation_wave_playbook.md` §4a.

---
## 2026-08-27: Domänen-Routing, Katalog-Drift, nächstes Ziel

**Kontext:** Handbuch-Keil (C→B) ist dünn. Frage war, ob `life_domain` ein DB-/Chunk-Durchlauf wie Edges werden soll, ob Launch 12×Tiefe 4 braucht, und welches System als Nächstes kommt. Staffeln (PRD/Leitdokument „Vier Spiegel“) sind frühe Produkt-Verpackung — Engines für Ziwei/Jyotish/BaZi/Astro/Maya rechnen bereits; Content außer HD fast leer.

**Decision:**

1. **Staffeln sind historisch.** Sie diktieren nicht mehr die technische Reihenfolge. Reihenfolge folgt: was testet die IC-Wette (12 Lebensbereiche als Navigation), und was hat schon Engine+Katalog.
2. **Routing = Kanten, nicht Singular-Index.** `belongs_to_domain` (multi, `candidate`/`approved`, evidence). `payload.life_domain` darf bleiben, ist nicht der Abruf. Plural `life_domains[]` weiter nur dokumentieren, bis Kanten existieren (`hd_state_contract.md`).
3. **Zwei Ebenen:** Katalog-v0 (deterministisch, Haus/Palast/Bhava/OS-Feld → Domäne) vs. Literatur-Pass (welche Absätze in welcher Domäne; erst wenn ein Leser da ist). Kein neuer LLM-Job jetzt. Backfill 2026-08-05 hat Element↔Element, **nicht** Element↔Domäne.
4. **`classify_domain` nicht umbenennen.** Job-Typ bleibt (Queue/Spark-Worker). Semantik = Chunk → `system_id`. Alias in `cursor/pipeline.md`. Rename erst bei Worker-Touch, mit Alias.
5. **WO/WANN ist Dramaturgie, kein Routing.** Leitdokument VI.2 (Astro=WO, BaZi=WANN) gilt für Serie/Onboarding-Ton. 12-Räder (Häuser/Bhavas/Paläste) sind alle WO. Timing (Luck Pillars, Dashas, Transite) ist WANN in mehreren Systemen.
6. **Nächstes Ziel: 12-Rad-Overlay, nicht Handbuch-Generator, nicht Staffel-1-Korpus zuerst.** Dünne zweite KARTE-Quelle = **Ziwei** (Map schon in IC-Enums, anderes Kulturkreis als HD, Playbook-Referenz, unabhängig von Astro↔Jyotish). Katalog-v0-Dateien parallel (HD-OS → Selbst; Ziwei-Map liegt). BaZi-Klassiker bleiben die nächste *Literaturwelle* auf Spark, nicht die nächste App-Fläche. Jyotish nicht als zweites UI (Staffel-2-Label egal; Überlappung mit Astro). Kein Mandala-SVG, keine Tiefe 3–4, kein `tag_ic_metadata`.

**Katalog-Stand (nicht raten, Dateien lesen):**

| System | 12-Rad? | Map vs. `contracts.md` §2 | Lücken |
|---|---|---|---|
| HD | nein (Typ/Zentren/Tore) | Leitdokument V.5: Typ+Autorität+Profil → Selbst | Sex/Geld/Austausch schwach natal |
| Ziwei | 12 Paläste | `ziwei_structure_v0.json` `life_domain_map` = §2-Enums | Sex + Wandlung ohne Palast (Z3: 10/12) |
| Jyotish | 12 Bhavas | `karakatva[]`, **kein** `life_domain` | ein Bhava → oft mehrere Domänen (Bhava 2 = Geld+Familie+Rede) |
| Astro | 12 Häuser | `astro_structure_v0.json` `life_domain_map` = §2-Enums (Katalog-`houses[].life_domain` bleibt Drift) | Haus 8 mischt Sex/Wandlung (zwei Map-Zeilen) |
| BaZi | nein (4 Pfeiler) | Struktur ohne Domain-Map | schlecht als Mandala-Test; gut als HD-Komplement |
| I Ging | nein (64) | Hexagramm = HD-Tor (faktisch) | 8 Trigramme ≠ 12 Domänen |

**Prüfpunkte** (hier nachschlagen, nicht vorher „fixen“):

| Wenn ihr hier seid | Prüfen |
|---|---|
| Astro-UI oder Astro-Katalog anfassen | Map liegt (`life_domain_map`). Katalog-Strings nicht umschreiben, bis UI sie liest. |
| Jyotish-UI / Bhava-Routing | Multi-Map aus `karakatva` schreiben; nicht 1:1 erzwingen. |
| Ziwei-KARTE | Vorhandene Map nutzen; Sex/Wandlung über Sterne, nicht Palast erfinden. |
| BaZi-UI oder BaZi-Ingest | Kein 12-Rad erwarten. Pfeiler ≠ Häuser. |
| I-Ging-Ingest | 64 = `hd.gate.N`, kein Domänen-Rad. |
| Worker-Rewrite | `classify_domain` → `classify_system` plus Alias auf den alten Job-Typ. |
| Handbuch-Generator / `/karte/[domain]` | Abruf über `belongs_to_domain`, nicht über `payload.life_domain`. Stimme `handbook_level`. L-Form: Breite Tiefe 1, eine Spalte tiefer — Content-Ökonomie, nicht Staffel. |
| Phase-3 `maps_to` | Astro↔Jyotish genealogisch nah (~70–80 % in VI.3). Ziwei unabhängiger Test. Methodik weiter `cross_system_mapping_methodology_review.md`. |
| Mandala-SVG | Erst wenn ein zweites 12-Rad in der UI liegt. |
| Launch Tiefe 4 / Werkstatt | Tiefe 3–4 = Werkstatt + Safety-Gate. 12×Tiefe 4 nicht füllen. |

**Nicht:** Job-Rename, Handbuch-Generator, `extract_relationships` neu, `tag_ic_metadata`, Mandala, Jyotish als zweite Graph-UI, Astro-Enum-Rewrite ohne Astro-UI, Staffel-1 als Blocker.

**Klarstellung (gleicher Tag, Nachfragen):**

- **Spark läuft nicht.** Es gibt keinen offenen BaZi-Klassiker-Job. S5d (*Destiny Code*, modern) ist durch. Die Klassiker (子平真诠 / 滴天髓 / 三命通会 / 渊海子平) sind in der Welle **geplant und nicht angefasst**. „Kann auf Spark weiterlaufen“ hieß: *optionaler Literatur-Track später*, kein „jetzt fertigstellen“. Nicht als Blocker vor der nächsten KARTE-Quelle starten.
- **„Ziwei dünn“ = erster UI-Schnitt, nicht dünne Literatur.** Wie HD: zuerst Natal-Chart als KARTE-Quelle (12-Palast-Gitter, Lookup, Freeze). Schulen/Werke danach in Wellen, ein `ziwei.*`-Baum, `tradition`-Tags (中州 / 三合 / 飞星), Compute-Default = iztro (analog jovian). Kein paralleles KG. Tu Vi = Locale, gleiches `system_id`. Große Limite/流年 nicht im ersten Slice (wie HD-Transit).
- **HD Natal bleibt freeze.** Engine-Transit (`/transit/daily`) existiert, App-UI nicht. Type-4-Kanäle bewusst ungelesen. Sidereal/Hybrid/Composite-UI offen. Das ist nicht „HD unfertig also blockiert alles“ — Vollausbau (ZEIT, JETZT-Radar, restliche Bücher) ist ein anderes Ziel. Transit bauen, wenn JETZT/ZEIT das Ziel ist, nicht als HD-Komplettismus vor dem zweiten System.
- **Jyotish ist das nächste Schwere, nicht das nächste Richtige.** Engine (PyJHora, D1–D9, Dashas, 16 Vargas) und Korpus sind größer. Derselbe 12-Haus-Gedanke wie westl. Astro (~70–80 % in VI.3) — wenig Overlay-Lernen, HD-skaliger Aufwand. Ziwei zuerst, weil natives 12-Rad, Map schon in §2-Enums, anderer Kulturkreis, TS-Playbook fertig.

---
## 2026-08-27: HD-Handbuch-Keil — C dann B

**Kontext:** JETZT zeigte Engine-Labels (`Projector · Wait for the Invitation`). SoT ist Alltagssprache auf der Handbuch-/KARTE-Ebene (Leitdokument XVII, UX §5) und ein Onboarding-Aha (UX §3). Launch-MVP (Mandala, Vier Spiegel, Transite, Schicht E) fehlt noch.

**Decision:**
1. **Keil, nicht Ersatz.** Dieselben Slots wie im UX-Konzept; schmal, weil Material fehlt.
2. **C vor B.** Eine Landkarte-Karte in Handbuch-Sprache (HD Typ×Strategie, deterministisch DE). Danach ein Insight nach Chart-POST mit Resonanz Ja/Teilweise/Nein, ohne Persistenz. Weiter → `/home/karte`.
3. **JETZT bleibt Radar-Stub** („Heute nichts Dringendes“), kein Natal-Essay.
4. **Kein Overlay-Dump**, keine i18n-Welle, keine anderen Engines, kein Mandala-SVG.

**Nicht:** Top-3, Schicht-E-Meta-Wörter, Resonanz in der DB, Transit-JETZT.

---
## 2026-08-26: Makerkit v4 zuerst (4.0.6)

**Kontext:** Kit war 3.1.3 / Next 16.2.2. Die HD-KARTE ist schwer; leere Space-Shells liefen billig mit. Offizielle Tags, kein Fresh Clone. Branch `cursor/makerkit-v4` vom Checkpoint `cursor/engine-api-integration-checkpoint`.

**Decision:**
1. v3-LTS zuerst (Next **16.3.3**), dann die 9 `v4-step/*`-Tags, dann `upstream/main` → **4.0.6**.
2. Bei Konflikten Kit-Hülle, IC-Inhalt: KARTE/Engines/`optimizePackageImports` ohne `@ic/engines`, Catalog `iztro`/`@yhjs/*`/`celestine`.
3. Design-Tag gemerged — er hat HD-Palette/Geometrie nicht angefasst.
4. pnpm 11 braucht **Node ≥ 22.13**.
5. Spaces bleiben leer bis Onboarding-Gate. **Erledigt:** Gate + JETZT-Start (Decision 2026-08-26 Onboarding-Gate).

**Nicht:** Fresh Clone, `supabase db reset`, i18n, Mandala, Dynamics-Jobs, Force-Push auf `main`.

---
## 2026-08-26: Dynamiken — drei Höhen, nicht nur Cross-System

**Kontext:** `sys_kg_edges` „weitgehend da“ klang so, als lägen Zyklen/Fallen schon. Die KARTE (Natal-Inspector) ist eine **System-Linse**, nicht die Dynamik-Schicht. `payload.process` ist Trap/Experiment *eines* Elements. `sys_dynamics` war in der Pipeline (`extract_processes`) systemintern gedacht: Zyklen, Spektren, Wachstumspfade, Fallen über **mehrere Elemente**. Die Decision 2026-08-05 hat die Tabelle auf 2+ Systeme verengt — das ist nur die *obere* Stufe.

**Decision:**
1. **Atom-Prozess** — `payload.process` (trap / gift_activation / experiment_seed) am Einzel-Node. ~100 % befüllt, ungelesen bis Werkstatt. Kein Backfill.
2. **System-Dynamik** — `sys_dynamics` mit `system_id` (intra): HD-interne Zyklen, Type×Center-Fallen, Life Cycles, Spektren. Tabelle 0 Zeilen. Eigene Komponente, analog zur Cross-Stufe. Job = `extract_processes` (nie gebaut), nicht Relink-Q.
3. **Cross-Dynamik** — dieselbe Tabelle, kombinatorisch 2+ Systeme × Domäne (`extract_pattern_traps`). Später, wenn mehr Systeme Content haben.
4. **Graph-Kanten** — `sys_kg_edges`: Struktur-Seed + Interp-Backfill intra HD **weitgehend da**; `maps_to` cross_system **nicht**. Kante ≠ Zyklus.

KARTE/Overlay bleiben Lookup + eine Lesung. Dynamiken erscheinen in WERKSTATT/ZEIT (und später JETZT-Highlight), nicht als Inspector-Stopfen.

**Nicht jetzt:** Dynamics-Jobs füllen; Relink-Q; Mandala.

---
## 2026-08-26: App-Spaces + Onboarding; Begleiter-Tür reserviert

**Kontext:** HD-KARTE freeze. Nächster Lerngewinn = App-Rahmen, nicht Corpus. UX: 4 Spaces. Vision: später Voice-first + visuell (`vision_and_story.md` §7), Inhalte vor Chat.

**Decision:**
1. Spaces unter Makerkit `/home`: **JETZT** `/home` · **KARTE** `/home/karte` · **WERKSTATT** `/home/werkstatt` · **ZEIT** `/home/zeit`. IDs `space_*` bleiben. HD bleibt `/home/karte/hd`.
2. Leere Shell zuerst. Kein hartes Onboarding-Gate (bestehende Test-Charts). JETZT verweist auf `/home/onboarding` wenn keine Signatur.
3. **Zwei Türen, ein Ziel.** Formular ist live. `data-ic-entry="companion"` = visuelles Feld rechts/unten für späteren Begleiter (Sprache + Bild). Kein Chat, kein TTS, kein Avatar in diesem Slice. Formular wird nicht durch den Agenten ersetzt.
4. Ungefähr/unbekannte Geburtszeit = später (UX-Konzept §3). Engine braucht weiter eine Uhrzeit.
5. Bottom-Nav laut UX kommt, wenn die Shell sitzt — jetzt Makerkit-Nav mit den vier Labels.

**Nicht:** Mandala-SVG, Transit-UI, Composite, Voice-Agent, volles UX-§3 (unbekannte Geburtszeit).

---
## 2026-08-26: Onboarding-Gate in der App, nicht auf Marketing

**Kontext:** Makerkit v4. UX §3 Warm Welcome = Marketing-Versprechen; Aha nach Account. Architecture §14: `/onboarding` unter `/home`. Freemium: Signatur frei, viral via Mandala-Share später.

**Decision:**
1. Kein Geburtsformular auf der Marketing-Site.
2. Nach Signup: keine Person `role=self` → Redirect `/home/onboarding`. Settings/Billing bleiben erreichbar. `test@makerkit.dev` ist ausgenommen.
3. JETZT ist die Startseite nach der Signatur (Typ · Strategie · Profil + CTA KARTE). Andere Spaces bleiben leer.
4. Unbekannte Geburtszeit und Mandala-Reveal bleiben ein späteres Paket.

**Nicht:** Öffentlicher Chart-Teaser, Onboarding in der Nav, Fan-out aller Engines in diesem Slice.

---
## 2026-08-26: Locale — Graph, Terms, Wordings; kein Display aus term_mapping

**Kontext:** KARTE-Chrome ist DE, Atomtexte EN. Frage: `sys_term_mapping` jetzt als Label-Katalog für alle Systeme füllen? Graph-Namen (Kopf, Sonne) nachziehen? Extra-DB-Spalte je Sprache?

**Decision:**
1. **Eine App-Locale** (`[locale]`, später Profil-Default). Graph, Chrome und Texte folgen derselben Locale. Kein zweiter Sprachen-Schalter am Chart.
2. **Vier Töpfe, keine neue Spalte:**
   - **Invariant:** Zahlen, Glyphen, Geometrie, Canonical-IDs. Unabhängig von Locale.
   - **Chrome:** Buttons, „Design“, „definiert“, Zentrumsnamen auf dem Graph — `next-intl`. Nicht KG.
   - **Essays:** `sys_synthesis_wordings` — **eine Zeile** je `(canonical_id, language, version)`; Styles (natural/coaching/…) liegen **in derselben Zeile** (`styles` jsonb), nicht als Extra-Spalte. Zweite Sprache = zweite Zeile, kein Überschreiben.
   - **Aliases (Pipeline):** `sys_term_mapping` existiert und ist produktiv. Viele Synonyme → eine ID („Power Gate“ / „Kraft-Tor“ → `hd.gate.34`). Das ist **Inbound für text2kg**, nicht das Display-Label auf dem Graph.
3. **term_mapping nicht zum UI-Katalog umbauen.** Viele-zu-eins. Ein Graph braucht **ein** Vorzugswort je `(canonical_id, language)`. Dafür später entweder next-intl (kleine Mengen) oder eine eigene Label-Zeile mit Unique `(canonical_id, language)` — nicht synonym-rows recyceln. Andere Systeme bekommen Aliase, wenn ihre PDFs `extract_term_mapping` laufen; das füllt die Pipeline, nicht die Chart-UI.
4. **Graph-Namen jetzt nicht „sauber i18n’en“.** Ist: Zentren fest DE, Planeten-Rails EN (`HD_PLANET_LABEL`; `HD_PLANET_LABEL_DE` ungenutzt). Bewusste Mischung bis Locale-Produkt (2026-08-17 bleibt). Dann next-intl, nicht Figma, nicht Geometry-TS.
5. **Keine Übersetzungswelle, kein DE-Re-Synth, kein Full-term_mapping-Seed als UI-Vorarbeit.** Overlay-Cache weiter `person_id + locale + ruleset`.

**Nicht:** `sys_kg_nodes` um `label_de`/`label_en`-Spalten erweitern; Essays in term_mapping legen; Overlay aus EN-Cache übersetzen.

---
## 2026-08-17: Sprache — Quelle, Overlay, UI-Chrome getrennt

**Kontext:** KARTE mischt DE-Chrome (`definiert`, `Mechanik`) mit EN-Atom-/S0.5-Texten. Overlay-Prompt ist EN. `pickWording` bevorzugt `language=de`, fällt auf `en`. Locale-Route existiert (`[locale]`), Produkt-Locale für HD-Content ist nicht gewählt. Decision 2026-08-13: Atom-UI folgt später Locale/`wordings.language`.

**Decision:**
1. **DB/KG bleibt Quellsprache.** HD S0/S0.5-Bücher sind EN → Interpretationen und `canonical_wording` bleiben EN, Feld `language` setzen. Nicht im Extract übersetzen. Zweite Sprache = zweite Wording-Zeile (`canonical_id` × `language`), kein Überschreiben.
2. **Inspector** = Lookup, kein LLM. Zeigt den Text der gewählten Locale, sonst Fallback EN. Chrome (Labels, definiert/undefiniert) über next-intl, nicht in die Atomtexte mischen.
3. **Overlay** = read-time, Sprache = Request-Locale, gleicher Fallback. Cache-Schlüssel später: `person_id + locale + overlay_ruleset`. Nicht den EN-Absatz nachträglich übersetzen — neu generieren. Bis Locale-Produkt: Overlay EN (wie die Atome).
4. **Jetzt keine Übersetzungswelle**, kein DE-Re-Synth. Chrome der KARTE darf DE bleiben als Arbeits-UI; Content bleibt EN. Mischung ist bewusst, bis Locale live ist.

**Nicht:** Chunks auf Deutsch neu extrahieren; Overlay in der DB ohne `locale` als einzige Wahrheit speichern.

---
## 2026-08-17: State-Vertrag — 13 Typen, Display-Policy, Träger, Provenienz

**Kontext:** Anzeige „undefined → nur shadow / defined → nur gift“ wäre Ontologie-Lüge. `open` im Code ist Invert von `defined`. Planetenbedeutung fehlte als eigene Schicht. 64keys/Gene-Keys-Umbenennung wäre Kosmetik.

**Decision:**
1. 13 `chart_element_types`, keine 13 Ebenen. `not_self_theme`/`signature` = `descriptor_element`. `concept` = `node_kind`, nicht Chart-Typ. Begriff System-Facette streichen (B≠C).
2. Center-Kern: `defined | undefined`. `open` nicht persistieren. Display-Policy = Priorität, nicht Existenz. SoT: `reference/hd_state_contract.md` + `contracts.md` §1b.
3. Planeten/Punkte = Activation-Source + optional `planetary_accent`. R = `activation.motion`. Juxtaposition aggregiert aus zwei Pol-Fixierungen (Code bereits so).
4. Mind dreifach: Type-Theme ≠ Center-C `mind_when_open` ≠ Systemprinzip. `hd.not_self_mind.*` nicht seeden.
5. Interpretative Inhalte: `content_provenance`. Keine Massen-Umbenennung, kein DB-Wipe vor Audit.
6. Nächster Bau: Shared Packer Inspector/Overlay nach diesem Vertrag. Concept-Node P2. Planeten-Buch queued. Kein Center-Re-Synth.

**Nicht jetzt:** Mandala, `tag_ic_metadata`, Dynamics-Job, PHS-UI, Aura-K2, MinerU aller unused.

---

## 2026-08-17: Wissensarten ≠ mention; Mandala ≠ 15 Keys; HD-KARTE bleibt System-Linse

**Kontext:** S0.5-Overview in contrast/mention zu packen ist keine Königslösung. Drei Vokabulare (Tradition-Slots vs. Chart-State vs. App-Sicht) wurden vermischt. `dimensions.*` (15) sind nicht die 12 Mandala-Segmente und nicht die 3 Ringe (Kern/Nah/Feld). Overlay/Inspector sind KARTE Layer 2 (HD), nicht das Mandala.

**Decision:**
1. Aboutness bleibt primary/contrast/mention. Gattung, Werk-Overview, Beziehungen, Kombinationen haben eigene Fächer (Concept-Node, Source-Essay, Edges, `sys_dynamics`) — siehe `contracts.md` §1a.
2. C-Slots entstehen durch **Recherche oder UI-Bedarf**, nicht automatisch aus MinerU. Kein Corpus-Scan aller Werke auf Verdacht.
3. `sys_dynamics` bleibt kombinatorisch/zeitlich, separat von `payload.process`.
4. Nächste Bau-Schritte: HD-Inspector/Overlay lesen dieselben A/C-Slots, die später Handbuch Tiefe 1–2 nutzt. Mandala und Cross erst nach einem Domänen-Spike + zweitem System. Kein Center-Re-Synth.
5. Landkarte-Draft: Canvas `ic-wissenslandkarte`.

**Nicht jetzt:** Mandala-SVG, `tag_ic_metadata`, Dynamics-Job, Full-Re-Synth.

---

## 2026-08-15: Facetten-Vertrag — Achse A für alle Elemente, C nur wo die Tradition einen Essay hat

**Kontext:** „Nur Center zuerst“ war **Füll-Reihenfolge**, nicht Architektur. Overlay, Handbuch und Werkstatt brauchen Achse A (gift/shadow/trap/…) an **jedem** Element. Achse C (z. B. `mind_when_open`) nur, wo ein eigener Essay existiert. Details: `cursor/contracts.md` §1a.

**Decision:** Vertrag gilt für alle `element_type` / Systeme. Nacharbeit = Lesen vorhandener Payloads + S0.5-Relink in Center-C, kein Wipe, kein Massen-Re-Synth. Klassen-Wissen nicht als mention an Geschwister.

---

## 2026-08-15: Eine ID, viele Facetten — Anzeige ≠ Overlay-Synth

**Kontext:** S0.5 (Never Mind + You and the Shadow) hängt an `hd.center.*`. Ein Re-Synth dieser Nodes mit Top-8 würde Funktions-Text (Winn/Schoeber-Karten) und Mind-wenn-offen in einen Absatz rühren. 64keys zeigt dasselbe Material auf **Sichten** (Typ/Profil vs. Aktivierung: offen|definiert × Potenzial|Schatten), nicht als einen Mischabsatz. Extract-Contract hat die Facetten schon (`dimensions.gift`/`shadow`, `process.trap`/`gift_activation`); Read-Path und `synthesize_node` kippen sie in **ein** `canonical_wording`. Das ist dasselbe Muster wie Rails: eine Line, drei Ebenen — nicht ein Glyph.

**Decision:**
1. **Ein K2-Node bleibt ein Element** (`hd.center.ajna`). Keine `hd.not_self_mind.*` seeden, solange Inspector/Overlay keinen eigenen klickbaren Mind-Knoten brauchen.
2. **Atom-Wording** (`sys_synthesis_wordings`) = mechanisch „was das Element *ist*“. Center-Karten (S0) **nicht** neu synth’en, nicht wipen. Der kurze „wenn offen/definiert“-Satz darin ist Altlast, kein Wipe-Grund.
3. **Facetten** (offen|definiert, gift|shadow, Mind-wenn-offen) werden **read-time** geholt: Chart-State (K1) wählt die Spalte; Quelle ist `link_role=primary` und/oder `dimensions`/`process` — nicht ein zweiter Full-Synth-Topf.
4. **Zwei Lesarten, ein Speicher:** Inspector/Aktivierung-Äquivalent = Key-Lookup, kein LLM, Facetten gestapelt (wie Inspector schon Buchpole vs. Aktivierung trennt). Overlay = wenige Atome **dieser** Person kombinieren; offene Zentren bekommen einen **zweiten** Prompt-Block (Mind/Schatten), nicht denselben Center-Excerpt nochmal länger.
5. **text2kg ohne Rolle ist Recall, keine Wahrheit.** S0.5-Overview-Chunks (`mention`) dürfen am Node bleiben, dürfen aber nicht Inspector/Overlay/Synth füttern. Heart-Chunk (Shadow #20) gehört zu `hd.center.heart`, nicht Solar Plexus.
6. RAG/Embeddings sind nicht der Atom-Abruf. Atom = `canonical_id` + State + Facette.

**Consequences:** Nächster S0.5-Schritt = Relink `primary`/`mention`, dann Overlay-Slot + Inspector-Stapel — kein Center-Re-Synth, keine neuen IDs. `payload.process` bleibt der Werkstatt-Pfad (Decision 2026-08-05), sobald die UI ihn liest.

**Nicht:** Full-Re-Interpret der Center-Bücher; `not_self_mind.*` aus TOC; S0.5 in `IC_SYNTHESIS_MAX_INTERPS` „durchsetzen“.

---

## 2026-08-14: Abgeleitete Fixierung — Overlay differenziert, Rails nicht vermischen

**Kontext:** Jovian Archive (Line Fixing, 2026-06-09) belegt Same-Gate: ein Planet kann andere Linien *desselben* Gates fixieren, wenn er deren Pol-Planet ist (Bsp. Mars 16.1 → 16.3/16.4). IHDS + Jovian belegen Harmonic: Pol-Planet im Partner-Gate des Kanals (Bsp. Venus in 39 → 55.2). Dachau/64keys: Saturn 18.3 ▼ plausibel Jupiter 18.1 Same-Gate; 57.5 Stern plausibel Pluto 57.5 ▲ direkt + Mond 10.1 ▼ harmonic über 10–57. „Juxtaposition“ an der Line ≠ Juxtaposition-Kreuz (4/1).

**Decision:**
1. Glyphe bleibt ▲ / ▼ / ★ (= beide Pole fixiert). Sie zeigt den **Zustand**, nicht den **Weg**.
2. Intern und im Overlay zählt ein Pol mit **Quelle**: `direct` | `same_gate` | `harmonic` (+ später transit/relationship). Felder: Ziel-Line, Pol, Planet, Aktivierung `gate.line`, Seite (Design/Persönlichkeit), Kanal wenn harmonic.
3. Overlay/LLM **nicht** „ist juxtaposition“ als Stempel. Stattdessen: allgemeiner Line-Text + beide Pol-Absätze + Herkunft in einem Satz (Planet, Gate.Line, Mechanismus). Keine Rangfolge `direkt > same-gate > harmonic` erfinden. Bewusst/unbewusst (Persönlichkeit/Design) darf genannt werden — das ist HD-Mechanik, keine Skala.
4. Rails v1 bleiben **direkt**. Abgeleitete Marken nicht so malen, als wäre der sitzende Planet der Buchplanet. Inspector: Buchpole / diese Aktivierung / abgeleitete Quelle getrennt.
5. Edges: abgeleitete Fixierung ist **chart-computed** (Read-time), kein geseedeter Literatur-Edge. Form sinngemäß `Moon 10.1 —fixes_pole:detriment→ 57.5`. Retrieval darf das später als Kontext kanten, nicht als ontologischen Layer.
6. Zwei 64keys-Charts (Dachau + 26.07.2023) stützen Same-Gate und Harmonic am Renderer. Rails bleiben direkt, bis Inspector/Overlay die **Quelle** zeigen. Kein dritter Chart als Blocker für den Rechner.

**Consequences:** Overlay v1b bekommt Fixing-Facts, nicht nur Status-Enum. 18.3: Saturn aktiviert, Jupiter 18.1 liefert ▼. 57.5: Pluto ▲ direkt, Mond 10.1 ▼ harmonic — Line-Juxtaposition, nicht „ausgeglichen“. Weder Planet-Gewichte noch Intensitätsprozente.

**Zweit-Chart 26.07.2023 11:47 Berlin** (Zahlen gleich). Direkt gleich: Mond 39.2 ▲, Mars 53.2 ▼, Jupiter 24.6 ▲, Venus 29.5 neither, Saturn 37.1 neither (Buch: Venus exalted, `detriment_planet: null`; 64keys ohne ▼). Abweichungen = Wege: Saturn 55.6 bei uns ▲ / 64keys Stern → Mond 39.2 Detriment von 55.6 im Partner-Gate 39. Uranus 2.6 leer / 64keys ▲ → Merkur 2.2 Same-Gate. NN 3.3 leer / 64keys ▼ → Pluto in 60 Detriment von 3.3.

**Nicht als Nächstes:** alle unused HD-PDFs durch MinerU. Die Fixing-Mechanik braucht die 384er-Tabelle + Kanalpaare (beides da). *Understanding the Planets* erst, wenn Overlay Träger-Sätze braucht (Chunk-Profil, nicht Chart-Blocker). *Holistic Analysis* Teil 1 fehlt auf Disk. *Line Companion* fehlt; nicht beschaffen nur für diese Regel.

---

## 2026-08-14: Polarität = drei Ebenen, Rails nur direkt

**Kontext:** 64keys zeigt Personality Saturn 18.3 ▼. Rave I’Ching 18.3 ist Neptune exalted / Jupiter detriment. IHDS: eine Linie kann zusätzlich über dasselbe Gate oder das harmonische Gate des Kanals fixiert werden — das ist nicht die Buchzeile.

Dachau: kein Gate 58 (Harmonisches von 18). Dafür Personality Jupiter 18.1 — der Detriment-Planet von 18.3 — im selben Gate. Das kann 64keys’ Saturn-▼ erklären, wäre aber **abgeleitete** Fixierung. 57.5 Pluto ohne ▲ in 64keys erklärt Harmonic nicht (Mond ist 10.1, nicht 10.5).

**Decision:**
1. Rails v1 bleiben **direkt**: Glyph nur wenn dieser Planet der Exalt-/Detriment-Planet **dieser** Gate.Line ist. 384er-Tabelle nicht an 64keys anpassen.
2. Inspector trennt Buchzeile und Chart-Planet: „Linien-Pole (I’Ching)“ vs. „Diese Aktivierung“.
3. Same-Gate / Harmonic / Transit / Beziehung = eigene Ebene (v2), nur wenn IHDS-Regel als Code steht und als „Chart-Fixierung“ beschriftet ist — nicht still auf die Säule.
4. `both` / Juxtaposition ist keine dritte Buch-Zuordnung. v1 = zwei Träger auf derselben Gate.Line.

**Consequences:** Saturn 18.3 bleibt ohne ▲/▼. Jupiter 18.1 bleibt ▼. 29.5 Sonne bleibt ▲. Line-Prosa im Inspector bleibt allgemein; Polarität steht an der Säule / in den zwei Inspector-Zeilen.

---

## 2026-08-14: pdftotext 384er-Tabelle, Lookup an

**Kontext:** `pdftotext -layout` der Complete Rave I’Ching (Storage). Glyph-Map aus benannten Sätzen im selben Extract, nicht geraten. 384/384 Line-Blöcke, 363 mit beiden Polen.

**Decision:** Lookup an. Dachau-64keys 7/8. **18.3:** I’Ching Neptune exalted / Jupiter detriment; 64keys zeigt Saturn ▼. Kein Override — I’Ching ist die Tabelle. User prüft 64keys-18.3.

**Consequences:** Nach Reload: 8.3 ohne Marke, 29.5 ▲, 18.1 ▼ (Jupiter). Saturn 18.3 ohne Marke (Ra, nicht 64keys). **R** aus Swiss-Ephemeris-Speed (`swe.calc_ut` xx[3] < 0); Sun/Earth/Moon nie R. HD-Container neu starten, damit Python-Änderung live ist.

---

**Kontext:** Dachau 18.11.1980 19:20. App zeigte Personality Earth 8.3 als detriment und Design Sun 29.5 als Stern. 64keys: 8.3 ohne Marke; 29.5 = ▲ exalted; both = gestapelte Dreiecke (= Stern); R = Retrograd.

**Decision:**
1. MinerU-named-Katalog nicht anzeigen (`POLARITY_LOOKUP_ENABLED=false`). Falsch ist schlimmer als leer.
2. Zeichen: ▲ exalted, ▼ detriment, ▲▼-Stack = Stern = both. Nicht ★ für exalted.
3. **R** ist K1 (Ephemeris-Speed), nicht I’Ching. Engine-Aktivierungen haben nur `degree` — Retrograd später extra.
4. 100%: `pdftotext -layout` der Complete Rave I’Ching in Storage, Parser, Abgleich gegen 64keys-Fixture `apps/web/lib/hd/hd-dachau-1980-64keys-fixture.ts`, dann Flag an.
5. 8.3 `detriment_planet: earth` war OCR-Spill von Line 8.2 („The earth in detriment“). 8.3-Chunk hat keine Planetennamen, nur `p`/`s`.

**Consequences:** Nach Reload keine Polaritäts-Glyphen. Nächster Content-Schritt pdftotext, nicht Overlay v1.

---

**Kontext:** Contract verlangt 384er `gate+line → exalt_planet, detriment_planet` aus I’Ching-Line-Chunks. MinerU-Zweispalter: rekonstruierte Line-Chunks enthalten fast keine Planetennamen und keine Unicode-Glyphen. Buchstaben+`p`/`s` als Glyph-Map erzeugt Falsch-Mars.

**Decision:**
1. Runtime + Rails-Sterne + Inspector-Status sind gebaut (`unknown` / `exalted` / `detriment` / `neither` / `both`).
2. Katalog nur **named** Treffer (`Mars exalted` / `in detriment` / `no planet in detriment`).
3. Volle 384 = `pdftotext -layout` der Complete Rave I’Ching in Storage, dann denselben Parser. Kein LLM, keine erfundenen Planeten.

**Consequences:** Die meisten Zeilen zeigen noch keine Sterne. Nächster Content-Schritt ist pdftotext, nicht Overlay v1.

---

## 2026-08-14: Offene Zentren immer im Wording-Lookup

**Kontext:** Die HD-Engine schreibt nur *definierte* Center in `chart.nodes`. Der Lookup holte deshalb keine `hd.center.*` für offene Zentren — Inspector ohne Text, Overlay nur Namensliste.

**Decision:** `wordingLookupIds` unioniert **immer** alle neun `hd.center.*`. Overlay v0 bekommt Open-Center-Excerpts (kein Gate-Invent). Engine-`nodes` bleiben definiert-only (K1-Wahrheit).

**Consequences:** Nach Reboot einmal neu berechnen. Nächster Chart-Schritt bleibt 384er Exalt-Lookup, nicht Center-Re-Synth.

---

## 2026-08-14: HD Bodygraph-Rails, Polarität, Overlay-Rezept

**Kontext:** Slice 1 zeigt Zentren + OS-Chips + Overlay v0. Klassische Planetensäulen, Exalt/Detriment und Planeten-Bedeutung fehlten im Konzept.

**Decision:**
1. `/karte/hd` **ist** die zukünftige HD-Karte. Rails links Design / rechts Persönlichkeit gehören in `HdBodygraph`, nicht ins Mandala.
2. Aktivierungen = K1 (Planet × Gate.Line). Polarität = vier Stati (`exalted` / `detriment` / `neither` / `both`) via Lookup auf `hd.line.*`, keine 13×384 Kombi-Nodes.
3. Inspector = Gate-Atom + Line-Atom (+ Planet wenn Nodes da). Overlay bekommt Polarität erst, wenn Gates/Lines im Prompt sind — als Flag + Pol-Absatz, nicht als generischer Status-Stempel.
4. Bau: UI-Säulen → I’Ching-Lookup → Planeten-Buch (`Understanding the Planets…`, queued_unused) → Overlay v1/Edges.
5. SoT: `reference/hd_bodygraph_overlay_contract.md`. Bandbreiten-These und Planet-Hierarchie = Literatur-Check, kein Gewicht.

**Rationale:** Line-Wordings existieren; die 384er-Tabelle nicht. Planeten färben das Tor, sind aber kein 14. Layer.

**Consequences:** Nächster UI-Slice = Säulen klickbar. Keine erfundenen Overlay-Gewichte. PHS-Pfeile bleiben eigene Ansicht.

---

## 2026-08-13: Chart-UI Slice 1 + Overlay v0 (HD KARTE)

**Kontext:** S0-Wordings und HD-Engine waren da; die App hatte keine Chart-Seite. Slice 1 ist der HD-Raum (KARTE layer 2), nicht Vier Spiegel / Mandala.

**Decision:**
1. Route `/home/karte/hd`: Geburt → `POST /api/ic/hd-chart` → Python-HD-Service → `user_persons` / `user_charts` → Bodygraph + Atom-Lookup `sys_synthesis_wordings`.
2. Atomtexte bleiben **Lookup**, kein LLM pro Klick. Overlay (Typ+Strategie+Autorität) ist **read-time**; v0 = Headline-Template. Fließtext nur mit `IC_LLM_URL` oder Langdock (`LANGDOCK_*`, dasselbe Konto wie Worker-Synth). SGLang auf Spark ist dafür nicht Voraussetzung.
3. UI-Sprache der Atoms folgt später Locale/`wordings.language`. Keine fest verdrahteten DE-Atomlabels.
4. `supabase db reset` vermeiden — KG lebt nur in lokaler Postgres. Dump: `supabase db dump --local --data-only`.

**Rationale:** Erst ein Aufrufer (persistierter Chart), dann Overlay. Template ohne LLM ist ehrlich; gestapelte Atomtexte sind keine Kombination.

**Consequences:** Nächster Schritt Overlay-LLM oder S0.5. Schulen nicht ingestieren. Makerkit v4 nicht in diesem Slice.

---

## 2026-08-13: HD-Schulen / Gate-Stimmen — `tradition` auf `hd.*`, kein zweites KG

**Kontext:** S0-Wordings sind jovian (Ra). Weitere Bücher sollen später **Linsen** sein, nicht parallele Human-Design-Graphen. Cosmic Way, Blue I Ching und Schoeber waren in Doku teils als I Ging bzw. „nicht 64keys“ geführt — Produktzuordnung jetzt:

**Decision:**

1. **Gleiche Nodes** `hd.gate.*` / `hd.channel.*` / `hd.center.*`. Unterschied nur **K3/K4** über `tradition` (und `source_work` / optional `teacher`). **Keine** zweite Engine, **kein** zweites `system_id` für diese Stimmen.
2. **Default-Wording (S0, Chart-MVP):** `tradition: jovian` (Ra / Complete Rave I’Ching + übrige S0-Werke). Schulen **nicht** in denselben `canonical_wording`-Topf, solange `tradition` in der Pipeline fehlt.
3. **Gate-Stimmen (64 Tore):**
   | `tradition` | Werk | Rolle |
   |---|---|---|
   | `jovian` | Ra Complete Rave I’Ching | Default |
   | `64keys` | Ebhart *Blue I Ching* (`64keys_Blue-I-Ching.pdf`) | 64keys-Sicht der 64 Gates (Potential/Shadow) |
   | `cosmic_sidereal` | Anthony/Moog *Oracle of the Cosmic Way* | **Beschreibung der 64 Gates aus sideraler Sicht** — K3 auf `hd.gate.*`, **keine** Engine, **kein** `i_ching.*`-Primärziel |
4. **Sidereal rechnen** bleibt `compute_profile.hd` (contracts §13). Cosmic-Way-**Texte** ≠ Ayanamsha. Produkt-Linse „sidereal/cosmic“ darf später **beide** Schalter setzen (Profil + diese Stimme).
5. **Klassisches I Ging** (Wilhelm/Baynes, Legge, Huang, Shaughnessy) = eigenes Struktursystem `i_ching.hex.*` + `text_line` — wie später Kabbala/Chakren: **Ur-System**, nicht HD-Schule. Parkyn *Book of Lines* bleibt HD-Schule (`parkyn`), nicht I-Ging-KG.
6. **Schoeber:** Person/Schule = **64keys-Orbit**. *The Centres* ist **für HD geschrieben** → dieses Werk bleibt in den **jovian/HD-Center-Wordings** (`tradition: jovian`, `teacher: schoeber`). **Kein** Center-Re-Synth, **kein** Mix-Problem 64keys vs. HD auf diesem Buch. 64keys-Gate-Sicht = **nur** Blue I Ching, nicht die Center-Prosa.
7. **Quantum HD** (Curry) unverändert `quantum_hd`. Gene Keys unverändert eigenes `gk.*`.
8. **Jetzt nicht:** Blue I Ching / Cosmic Way ingest+synth; `tradition`-Feld in der Pipeline; Center-Wipe.

**Rationale:** Ein Chart, mehrere Stimmen. Mix entsteht nur, wenn verschiedene `tradition`s ungetaggt in ein Default-Wording fallen. Schoeber-Centers ist Zweitstimme **derselben** HD-Matrix, nicht die Blue-I-Ching-Linse.

**Consequences:** Mapping in `cursor/engines.md` §6.7b; Canon-Policy: Default-Synth nur jovian. Pipeline-`tradition` erst beim **ersten** Schul-Ingest. Nächster Produktschritt bleibt Chart-UI (oder GK/BaZi), nicht Schul-Coverage.

---

## 2026-08-13: Canon-first Synthesis — Mechanik-Wahrheit vor Coverage

**Kontext:** Forensic nach HA2/Four-Views Close-out: `ego_projected` (G/25-51), `self_projected` (splenic-Klang), `definition.none` (Authority/Strategy-Vermischung) trotz Links. Ursache: Relink-Recall + Synth ohne Canon/Verify; Score/Poison allein = Heuristik, keine Gewissheit.

**Decision:**
1. **Canon-first:** Mechanik aus Canon-Cards; Interps nur belegen/ausschmücken.
2. **Status-Enum:** `blocked` | `canon_fallback` | `synth_draft` | `verified` — steuert Write/UI; kein weiches Confidence als Gate.
3. **Placeholder** bei blocked: `[UNSYNTHESIZED:{canonical_id}] Insufficient clean evidence; awaiting review.` — nie erfundene Prosa.
4. **Evidence-Admission binär**; Score höchstens Sortierung unter Admitted.
5. **Vergleichs-/Multi-Topic-Chunks:** nicht default in Synth-Context; Soll `link_role=contrast|mention|primary` — Synth nur `primary`.
6. **contrast/mention** bleiben wertvoll für **Edges/Interactions** (`amplifies` / `depends_on` / `clashes_with`) — anderer Pfad als Node-Wording.
7. **Verify-before-write:** Regeln zuerst; Check-LLM nur bei `verify: semantic` / inconclusive / explizit.
8. **Canon-Rollout:** Auth/Def YAML jetzt; Type/Strategy/Signature als Nächstes; Gates/Channels per Template; andere Systeme beim Antasten.
9. **Bestand:** kein Full-Wipe — Risiko-Queue (BAD/WARN zuerst); stabile Layer nur Stichprobe.

**Rationale:** 100 % Mechanik-Sauberkeit ist erreichbar über Canon+Admission+Verify; Literatur-Reichtum bleibt ehrlich dünn wo Bücher schwach sind.

**Consequences / SoT:**
- Policy + Chat-Playbook: `cursor/reference/synthesis_canon_first.md`
- Canon Auth/Def: `reference/canon/hd_auth_def_canon_v1.yaml`
- Implementierung folgt in Worker (`ic_worker.py` synthesize_node) + Relink `link_role`; bis dahin keine blinden force-Synths auf Auth-Edge-Nodes.

---

## 2026-08-07: Gate-Lines Layer abgeschlossen (384/384 Wordings)

**Status:** ✅ erledigt (folgt auf Decision 2026-08-06 „additive Line-Chunks“).

**Ergebnis:**
1. Line-Chunks **384/384** (Cascade-Fix Gates 26–36, Spot 44.1, PDF-Refill thin/Spill).
2. Interps **384/384** → Relink 1:1 (`ic_hd_iching_line_relink_1to1.py`) → Orphan/Cross-Link-Cleanup.
3. Scoped Synth → **384/384** `sys_synthesis_wordings` für `hd.line.*` (Job `d3a349cb-…`).
4. Kein destruktives Re-Extract der Gate-Chunks.

**Nächster HD-Fokus:** Authority/Definition (General-Bücher) oder Schulen — nicht erneut Lines.

---

## 2026-08-06: Gate-Lines — additive Line-Chunks; Sibling-Share ablösen

**Kontext:** Nach Sibling-Share (Coverage) war Line-Präzision bewusst offen. Entscheidung revidiert: **jetzt sauber**, ohne destruktives `extract_text` (löscht alle Chunks der Source).

**Decision:**
1. Additive Rekonstruktion per `ic_hd_iching_line_chunks.py`: MinerU-Gate-Stream + Spill-Korrektur + `pdftotext`-Fill → neue Chunks mit `chunking.method=rave_iching_gate_lines_reconstructed`, `canonical_id=hd.line.{g}_{n}`.
2. Ziel **384/384** (anfangs 378; Gate 26 + Kaskade später per Audit/pdftotext geschlossen).
3. Danach: `extract_interpretations` → Relink 1:1 (Sibling-Share ablösen) → scoped `synthesize_node` für `hd.line.*`.
4. Kein flächendeckendes Re-Extract der 65 Gate-Chunks.

**Qualitätssicherung im Parser:** Positions-Claims (Titel wiederholen sich gate-übergreifend), keine Free-Text-Anker, Degree-first-OCR-Header, Core-Cluster-Guard gegen MinerU-Spill, Spill-Repair, später `ic_hd_iching_line_pdf_refill.py`.

**Rationale:** Produkt braucht unterscheidbare Line-Wortings; Coverage-Stopgap reicht nicht. Additive Insert vermeidet Orphan-Interps und Wipe-Risiko.

**Consequences:** Abgeschlossen 2026-08-07 — siehe Eintrag oben. Alter Sibling-Share-Eintrag unten bleibt als Historie.

---

## 2026-08-06: Gate-Lines — Sibling-Share jetzt; Line-Präzision bewusst offen

**Status:** **überholt** durch Eintrag „additive Line-Chunks“ oben (gleiche Datumswelle). Sibling-Share war Zwischenstand; Line-Chunks sind deployed.

**Audit-Befund:**
- Extremfälle: Gate 1 und 10 = Stub-Chunks (78/63 Zeichen); Line-Text steckt im Kopf von Gate 2 bzw. 11 → Override `MERGED_LINE_CONTENT={2:1, 11:10}` im Relink-Script.
- Häufiges Muster: ~20 Gate-Chunks starten mit `6 <LineName> …°` (= Line 6 des **vorherigen** Gates). Anker für Gate N+1 feuert oft eine Seite zu früh → Tail von Gate N landet im Head von N+1.
- Weitere kurze Intro-Chunks ohne Line-Header (z. B. 5, 8, 14, 20, …) wurden bei `len≥400` trotzdem auf alle 6 Lines verlinkt (weiche Abdeckung).

**Decision (jetzt):**
1. **Sibling-Share behalten** als Layer-Abdeckung — kein Line-Chunk-Profil und kein Re-Interpret in diesem Sprint.
2. Extremfälle 1/10 per Override abdecken (Inhalt existiert, nur falsch zugeordnet).
3. **Kein** flächendeckendes Nachziehen weiterer `MERGED_LINE_CONTENT`-Paare ohne Messung — würde Nachbar-Interps noch stärker vermischen.

**Decision (später, bewusst offen — wann Line-Präzision produktrelevant wird):**
1. Eigenes Task: Chunk-Grenzen im I'Ching **reparieren** (Profil-Anker so, dass Gate N nicht in N+1 hineinragt) **oder** neues Profil `rave_iching_gate_lines` (Split an `N LineName DD°`).
2. Danach Re-Interpret der betroffenen Chunks + Relink 1:1 `hd.line.{g}_{n}` (Sibling-Share ablösen).
3. Trigger: Handbuch/Chart braucht unterscheidbare Line-Wortings (z. B. „dein Sun in 13.3“ vs. generisches Gate-13-Kapitel) — nicht nur Coverage-Zahlen.

**Rationale:** Dieselbe Kosten-/Risiko-Logik wie Crosses 2026-08-05 (Tagging/Relink vor teurem Re-Chunk). Line-Präzision ist real nötig für die Produkt-Tiefe, aber ein anderer Arbeitspaket-Schnitt als „Layer erstmal füllen“.

**Consequences / Doku:** Eintrag hier + `reference/hd_layer_id_and_chunk_profiles.md` (Offen-Abschnitt Gate-Lines) + Handover-Hinweis. Script-Override und Sibling-Share bleiben bis zum gezielten Fix.

---

## 2026-08-05: Incarnation Cross — Theme-Parent + Varianten-Children; kein `_1`-Default; Chunk-Profil Pflicht

**Kontext:** Seed hat 192 flache `hd.incarnation_cross.*`-Nodes (je RAC/JC/LAC × nummerierte Variante `(1)–(4)`). Literatur und LLMs sprechen oft nur „Vessel of Love“ ohne Nummer. Remap-Versuch mit Default auf `_1` war **verlustbehaftet** (vier echte Crosses = vier Sun-Gates/Quarters). Generic Chunking der Cross-Bücher (1440 Chunks ohne Meta) → 14/192 mit Interps. Analogie zu Gates: dort half `rave_iching_gates`-Chunk-Profil + `gate_number`-Hint; Crosses bekamen kein Äquivalent → gleiches Klassenproblem, andere Buchstruktur.

**Decision:**
1. **Ontologie (Soll):** Pro benanntem Cross-Thema ein **Parent** `hd.cross_theme.{stem}` (z. B. `vessel_of_love`) + **Children** die bestehenden 192 Varianten-Nodes, Edge `variant_of` / `part_of`. Allgemeiner Fließtext → Theme; Chart-Engine liefert immer die **spezifische** Variante → Child. Abfrage Handbuch: Child + Parent (Theme-Kontext), nie still eine andere Variante unterschieben.
2. **Kein Auto-Map** mehrdeutiger Kurzformen auf `_1` (zurückgenommen in `normalize_hd_canonical_id`). Nur 1:1-eindeutige Aliase.
3. **Chunk-Profil** `incarnation_crosses_by_profile` (wie Gates): Split an `THE Nth GATE`, Metadata = exakte RAC/JC/LAC-`canonical_id`s aus `hd_crosses_extracted.json` für dieses Sun-Gate. Danach Re-Chunk/Re-Interpret der Cross-Quellen — nicht Blind-Re-Interpret auf Meta-losen Chunks.
4. **Checkliste vor jedem neuen Struktur-Layer** (Gates, Crosses, PHS, …): Katalog-IDs klar? Theme vs. Instanz? Chunk-Profil nötig? Primary-Hint? → `reference/hd_layer_id_and_chunk_profiles.md`.

**Rationale:** Entspricht bereits dem Muster `line_def` (Theme) vs. `line.{gate}_{n}` (Instanz). Chart-Korrektheit verlangt die richtige `(N)`-Variante; Literatur-Korrektheit braucht einen Ort für unnummerierte Aussagen.

**Consequences:** (1) Theme-Nodes + Edges seeden (nächster Seed-Schritt, noch nicht ausgeführt). (2) Cross-Bücher mit Profil neu chunking/interpret. (3) Vorherige Remap-Links auf `_1` bei Mehrdeutigkeit als verdächtig behandeln / nach Re-Interpret ersetzen. (4) Doku: dieser Eintrag + Layer-Checkliste.

---

## 2026-08-05: Element-Verbindungen — Backfill statt neuer Extraktion, Read-Time-Retrieval statt Precompute

**Kontext:** Ursprünglicher Plan (Decision "4-stufige Extraktion", 2026-02) sah `extract_relationships` (→ `sys_kg_edges` intra_system) + `extract_processes` (→ `sys_dynamics`) als eigene Jobs pro Chunk vor. Beide wurden **nie gebaut** — `ic_worker.py` hat nur 6 Handler (`extract_text, classify_domain, extract_term_mapping, extract_interpretations, text2kg, synthesize_node`). DB-Audit 2026-08-05: `sys_dynamics` = 0 Zeilen, `sys_interactions` = 1 Zeile, `sys_kg_edges` = 3417 Edges, aber 100 % `intra_system`/strukturell (aus Katalog-Seed), 0 `cross_system`.

**Überraschender Fund:** `sys_interpretations.payload` enthält bereits seit der ursprünglichen Prompt-Definition zwei Felder, die genau das leisten, wonach wir suchten — nur nie downstream genutzt:
- `elements[]` — alle im Chunk explizit genannten Entitäten (nicht nur die Haupt-Entität); `text2kg` verlinkt darüber **bereits heute** eine Interpretation an **mehrere** Nodes gleichzeitig (`_resolve_canonical_ids_from_interp`).
- `interactions.{amplifies, depends_on, clashes_with}` — vom LLM bereits typisiert extrahiert. Stichprobe (n=300, aktuelle Langdock-Läufe): **64 % nicht-leer**, 427 `amplifies`-, 269 `depends_on`-, 80 `clashes_with`-Referenzen mit sinnvollem Inhalt (z. B. `hd.gate.1 amplifies [hd.gate.2, hd.center.G]`).

**Decision:**
1. **Kein neuer Extraktions-Pass.** Statt `extract_relationships` neu zu bauen: bestehendes `interactions`-Feld aus bereits vorhandenen Interpretationen per **Backfill-Script** in `sys_kg_edges` (edge_scope=`intra_system`, edge_type=amplifies/depends_on/clashes_with, evidence=chunk/interpretation_id) übertragen. Kosten: 0 neue LLM-Calls für Alt-Bestand; nur für neue Bücher fällt es sowieso als Nebenprodukt der laufenden `extract_interpretations`-Jobs an.
2. **Keine feinere Vorab-Klassifikation der Erwähnungsart nötig** (kein `mentions_other_elements` mit Sub-Typ). Die drei bestehenden Typen (amplifies/depends_on/clashes_with) reichen als Exact-Match-Vorfilter; die eigentliche Nuance liest das LLM zur Lesezeit direkt aus dem zitierten Fließtext (`evidence.quotes`), nicht aus einem vorab kodierten Label.
3. **Kombinationsbedeutung wird NICHT vorab für alle Chart-Kombinationen berechnet** (kombinatorisch unmöglich: 64 Gates × 12 Profile × 9 Center × …). Stattdessen: **Read-Time-Retrieval im geplanten Overlay-Service** (architecture.md §13, "LLM on-demand") — bei Bedarf (Onboarding Top-3, oder Nutzer öffnet eine Domäne/einen Chart-Bereich) werden (a) direkte `sys_kg_edges`-Treffer zwischen den aktiven Nodes eines Charts UND (b) Embedding-Suche über `sys_interpretations` mit den aktiven `canonical_id`s als Filter kombiniert, als Kontext an ein LLM gegeben, das die personalisierte Kombinations-Aussage schreibt — gecacht wie die anderen Echtzeit-Services (Konvergenz-Service: 15-Min-Muster als Vorbild, hier eher "einmalig pro Personen-Kombination" da statisch, kein Transit).
4. Dieser Overlay-Retrieval-Mechanismus existiert noch **nicht** als Code — nur als Konzept hier festgehalten. Bauen erst, wenn Chart-Engine-Service + `user_charts` so weit sind, dass es einen echten Aufrufer gibt (nicht Teil der aktuellen Content-Wave).

**Rationale:** Vermeidet doppelte Kosten (die Daten sind größtenteils schon extrahiert), vermeidet kombinatorische Explosion durch Precompute, bleibt konsistent mit dem bestehenden Architektur-Prinzip "Struktur deterministisch billig, Bedeutungs-Nuance vom LLM zur Laufzeit" (architecture.md §7, §13).

**Consequences:** (1) Backfill-Script `ic_kg_edges_backfill_from_interactions.py` (2) `architecture.md` Datenschicht C/D-Zeile + §13 Overlay-Service um diesen Stand ergänzen. (3) Content-Wave-Extraktion bleibt unverändert (Feld wird bereits mitgeschrieben) — kein Rerun nötig.

**Update 2026-08-05, ausgeführt:** Backfill gelaufen (4463 Interpretationen, 1140 Nodes). Ergebnis: **12.998 neue Edges** (`amplifies`=5481, `depends_on`=4319, `clashes_with`=3198), alle `review_status=candidate` (unterscheidbar von den 3417 `approved` Seed-Edges). `edge_scope`: 16412 `intra_system`, **3 `cross_system`** — die ersten Cross-System-Kanten überhaupt (Datenschicht D war vorher bei 0). Nicht auflösbar waren ~5200 referenzierte canonical_ids je Richtung (Bücher/Systeme ohne vollständigen Node-Katalog, z. B. dünne BaZi/GeneKeys-Abdeckung) — Script ist idempotent re-runnable, holt bei künftigen Content-Wellen automatisch mehr Treffer.

**Klarstellung zu den 3 `cross_system`-Kanten (2026-08-05):** Das sind **beiläufige Ko-Erwähnungen** in Fließtext (z. B. ein BaZi-Buch erwähnt im selben Absatz einen HD-Begriff), keine geprüfte `maps_to`-Entsprechung. Die eigentliche, dafür vorgesehene Phase-3-Mapping-Methodik (Embedding-Similarity zwischen `canonical_description`s) hat weiterhin 0% Fortschritt und ist laut `reference/cross_system_mapping_methodology_review.md` methodisch noch ungeklärt (offener Review, vor Implementierung zu entscheiden). Warum nur 3: erwartbar am aktuellen Korpus (11/68 HD-Bücher, fast nur Ra-Vokabular ohne Systemvergleiche) — wächst automatisch mit weiteren Content-Wellen, besonders explizit vergleichenden Werken.

**Korrektur zu `sys_dynamics` (2026-08-05):** Die ursprüngliche Aussage "kein äquivalentes Feld im aktuellen Payload-Schema" war ungenau. Stichprobe (n=300) zeigt: `payload.process.{trap, gift_activation, experiment_seed}` ist zu **100% befüllt** — das deckt bereits die pro-Element-Ebene ab, die der nie gebaute Job `extract_process_patterns` liefern sollte (Werkstatt-Traps, Experiment-Seeds pro einzelnem Gate/Center/etc.). Kein Backfill nötig — liegt bereit für Read-Time-Retrieval, sobald Overlay/Werkstatt existiert. Was tatsächlich fehlt, ist die `sys_dynamics`-Tabelle selbst: `dynamic_type='trap'` (kombinatorische Falle über 2+ Systeme × Domäne, z. B. "HD-Shadow X + BaZi-Clash Y") und `dynamic_type='phase_cycle'` (Langfrist-Zyklen/Transite). Das ist **kein Backfill-Fall** — beides braucht einen neuen, aktiven LLM-Kombinationsschritt (`extract_pattern_traps`, gruppiert nach `life_domain`, das ebenfalls bereits zu ~99% befüllt ist) bzw. einen Transit-Engine. Bewusst zurückgestellt: höhere Qualität mit breiterer Systemabdeckung pro Domäne, und keine Notwendigkeit, das jetzt parallel zur laufenden Content Wave zu bauen.

**Sequenzierung nächste Schritte (Nutzer-Entscheidung 2026-08-05):** (a) Docs-Korrektur [dieser Eintrag] + Content Wave (HD Profiles/Crosses, danach BaZi-Klassiker, weitere Systeme) läuft unverändert weiter. (b) `extract_pattern_traps` (sys_dynamics befüllen) und (c) Read-Time-Retrieval-Spike im Overlay-Service sind beide zurückgestellt bis Content Wave (alle geplanten Bücher) weiter fortgeschritten ist — dann in der Reihenfolge, in der sie natürlich anfallen (vermutlich b vor c, da c von einer Chart-Persistenz/Onboarding-Aufrufer abhängt, der noch nicht existiert; b braucht nur ausreichende Domain-Abdeckung).

---

## 2026-05-07: Ur-Systeme — `kabbalah`-Split, `chakra` ein Pfad, I-Ging-AA-Auswahl (Wilhelm/Baynes + Legge)

**Decision:**

1. **`kabbalah`:** Zwei **`system_id`s**: **`kabbalah_jewish`** (klassisch / Sefer Yetzirah-Linie, Scholem/Idel, ggf. Zohar-Auszüge) und **`kabbalah_hermetic`** (Golden Dawn, Fortune, Regardie u. ä.). Crosswalk-Kanten nur explizit (`has_analogue`, …).

2. **`chakra`:** **Ein** `system_id` **`chakra`**; Trennung klassisch vs. westlich über **`tradition`** + **`model`** (z. B. `tantra_classical`, `western_synthesis`), kein zweites `system_id` bis sich ein Pilot gegen beweist.

3. **I Ging — welche AA-Treffer für IC `text_line: wilhelm_baynes` (engl. P0):**  
   - **Primär (vollständige Bollingen-Ausgabe, Text + Material + Kommentare / Ten Wings je nach Auflage):** Princeton UP, **Wilhelm → Baynes** (Cary F.), **3rd ed. ca. 1967–1971**, **eine** große PDF-Datei mit bibliographisch klarem Umfang (ca. **700+ Seiten**). In der Trefferliste: z. B. **`The I ching; or, Book of changes_123862961`** oder **`_123768270`** (zlib, Princeton, lxii+740 S.) **oder** **`nexusstc/.../f53e2237935cf72214e6a2bcb0ad5b95.pdf`** (~23 MB) — **vor Download** Dateigröße/Beschreibung mit „3 books“, „commentaries“, „Ten Wings“ abgleichen.  
   - **Alternativ robust:** `ia/ichingorbookofc00wilh.pdf` (Routledge & Kegan Paul **1950**, sehr ausführliches Inhaltsverzeichnis im Snippet) — wenn die Datei vollständig und gut OCR-tauglich ist.  
   - **E-Book statt PDF:** Princeton-**EPUB** 1967/1971 (z. B. `069109750X_The.epub` oder `nexusstc/.../29ee70af8c8770cd40a81c385d1c85df.epub`) — für Lesen ok; **MinerU/Pipeline** bevorzugt oft **PDF**.  
   - **Nicht** als K2-Primäranker: **Pocket**-Ausgaben, **stark gekürzte** Scans, **„Gary F. Baynes“**-Tippfehler-Metadaten (unsauber), Dateien **unter 1 MB** mit vollem Titel (meist Fragment), **chenjin5**/fragliche **MOBI/EPUB** mit ❌-Hinweis, **DJVU** (nur wenn ihr bewusst konvertiert).

4. **I Ging — Zusatzwerk (K3, nicht Ersatz des Orakeltexts):** **`Understanding the I Ching: The Wilhelm Lectures on the Book of Changes`** (Hellmut + Richard, Princeton **1995** o. ä.) — z. B. zlib **`119130701`** oder **`119118554`** oder **`d7ccdfc52e41f03909ad6b37e83ee89a`**; **getrennt** speichern und mit `component: secondary_commentary` taggen.

5. **I Ging — `text_line: legge` (P1):** **Dover**-Reprint *Sacred Books of the East* XVI, z. B. **`The I ching_123761840.pdf`** (1963, ~27 MB) **oder** die Chai-ed. **University Books 1964** (`I ching; Book of changes_121162061`) — **nicht** Treffer, bei denen der Metadatenblock eindeutig **Tao Te Ching** / falsches Werk ist.

6. **Spanisch** (`Yi king : libro de las mutaciones`, Mexico 1999): **optional** zweite Datei für **`language: es`** + `text_line: wilhelm_spanish` — nur wenn ihr spanische K3/K4 im KG wollt; **nicht** statt der englischen Bollingen-Basis.

**Rationale:** K2-Anker muss **eindeutig reproduzierbar** und **vollständig** (Hexagramme + traditionelle Schichten) sein; Dubletten und Schrott-Treffer verwässern Provenance. Split Kabbalah war in `ontology_policy.md` begründet; Chakra bleibt ein Graph bis zur Evidenz des Gegenteils.

**Consequences:** `entity_registry_iching_v01.json` (o. ä.) mit `known_works`-Einträgen inkl. **AA-MD5** nach verifiziertem Download; `literature_canon_by_scope.md` §6.1 um **„gewählte Referenzdatei“** ergänzen sobald MD5 feststeht; Toolkit/VM-Profil `iching_content` später analog HD.

---

**Decision:** Der Rechenmodus `hybrid_design_tropical_personality_sidereal` (`compute_profile.hd`, `cursor/contracts.md` §13) heißt in **UI und Doku** **EarthStar Human Design**. Technische Keys und `system_id: 'hd'` unverändert; Anzeigename in §13-Tabelle.

**Rationale:** Verständlicher, markenfähiger Name innerhalb von IC; klare Abgrenzung zu Jovian-„offiziell“; API bleibt stabil über Enum.

**Consequences:** Copy, Consent-Banner für Erstnutzung, Hilfetexte; Side-by-Side- und Dropdown-Spezifikation in `reference/hd_compute_profiles_kg_and_roadmap.md` §6.1.

---

## 2026-05-06: Human Design — Rechenmodi ohne neues `system_id` (`compute_profile`)

**Decision:** Unterschiedliche astronomische Konventionen für HD (**tropical Ra/Jovian-Standard**, **sidereal**, **Hybrid Design/Persönlichkeit**) werden **nicht** als extra `system_id` modelliert. Stattdessen bleibt **`system_id: 'hd'`**; der Modus steckt in **`compute_profile.hd`** (siehe **`cursor/contracts.md` §13**): `zodiac_mode`, optional `sidereal.ayanamsha`, `backend` (Swiss Ephemeris + Engine-Paket/Version).

**Rationale:** Canonical IDs (`hd.gate.N`, …) sind **eine** Ontologie; mehrere Modi ändern **aktivierte Teilmengen**, nicht die Bedeutungs-Adressierung. So bleiben KG-Seed und Literatur an **denselben** Knoten hängbar; Vergleichbarkeit von Charts ist über **`compute_profile`** explizit und API-neutral.

**Consequences:** Chart-Snapshots und Engine-Requests müssen **`compute_profile`** persistieren; UI und Vergleiche (Composite etc.) nur **innerhalb desselben Profils**. Detailplan und K1–K4-Einordnung: **`reference/hd_compute_profiles_kg_and_roadmap.md`**.

---

## 2026-04-16: Nine Star Ki — K1/K2 v1 (Tabellen, Sonnenmonate, energetischer Stern)

**Decision:** `@ic/engines` **Nine Star Ki** auf **v1** gehoben: **Honmei** weiter aus **Ki-Jahr** (lokaler **4. Feb.**-Grenze) mit **Jahres-Stern-Overrides** wo die einfache Ziffernregel von Standardtabellen abweicht; **Sonderfall** Geburt **Gregorianisch 1986** mit **Ki-Jahr 1985** → Honmei-Basisjahr **1984** (übliche Sonoda/Tabellenkorrektur). **Getsumei** nicht mehr über `wrap9(Honmei − Monatsindex)`, sondern über **12×9-Monatsmuster** (inkl. Anomalie Hauptstern 5 Okt–Dez). **Dritter Stern (energetic / 81er-Tabelle)** aus **(Honmei, Getsumei)**. **Sonnenmonate** als **12 feste Monat/Tag-Schnitte** (Li Chun 4. Feb. … Kleine Kälte 6. Jan.), **ohne** exakte Solar-Term-Uhrzeit.

**Rationale:** Die alte Differenzformel für den Monatsstern ist **fachlich nicht** deckungsgleich mit gängigen japanischen NSK-Tabellen (z. B. Hauptstern 5); K1/K2 sollen **stabil** und **gegen Lehrmittel prüfbar** sein. Tabellen sind klein und deterministisch.

**Klarstellung — HD-Minuten vs. NSK-Sonnenterme:** Human Design nutzt den Geburts**moment** (Ephemeris, Minuten-relevant für Gates/Profil usw.) — dafür ist **präzise lokale Wandzeit + Zone** nötig. Die **Jieqi**-Grenzen (Li Chun, Jing Zhe, …) für Nine Star Ki fallen astronomisch jedes Jahr auf eine **andere Uhrzeit** (nicht automatisch Mitternacht lokaler Zivilzeit). NSK **v1** arbeitet deshalb mit **festen Kalender-Schnitten** (4. Feb., 6. Mrz., …) — eine dokumentierte **K1-Approximation**. Das ist **kein** „einfach dieselbe Swiss-Ephemeris wie HD aufmachen“: man müsste explizit **Solar-Term-Module** (oder Ephemeris-Queries) pro Jahr/Zone fahren → **v2+** / `tradition`. HD-Zeitfelder **kann** die App überall sammeln; sie **ersetzen** ohne diese Zusatzlogik **nicht** die NSK-Term-Uhren.

**Consequences:** Chart-Nodes inkl. `nsk.energetic_star.{1–9}`; Vitest **Step 3** (`nine-star-ki-catalog-validation.test.ts`); Katalog-Meta `schema_version` 1.0.1. Optional später: exakte Li-Chun-Zeit pro Zeitzone → v2 / `tradition`.

---

## 2026-04-16: Maya Tzolkin — v1 (lokales Zivildatum aus aufgelöstem Instant)

**Decision:** Engine **`ic_maya_tzolkin_v1`**: Der **Tzolkin-Tag (Kin)** bezieht sich auf das **lokale Zivilkalenderdatum** in `birth.timezone`, abgeleitet aus dem mit **`utcMillisForWallTimeInZone`** aufgelösten UTC-Instant (gleiche Pipeline wie HD/BaZi). **Ein Kin pro lokalem Ziviltag**; kein Haab/Long Count in v1.

**Rationale:** Konsistente Nutzung von Datum, Uhrzeit und IANA-Zone; vermeidet stillschweigende Abweichungen, falls Eingaben und Zone formal zusammenpassen sollen; für typische Geburtsurkunden-Eingaben identisch zum bisherigen reinen `YYYY-MM-DD`-Parse.

**Consequences:** `raw.gregorian_date` = aufgelöstes `YYYY-MM-DD`; Vitest **Step 3** `maya-tzolkin-catalog-validation.test.ts` (Nodes + Konsistenz zur `kins`-Zeile im Katalog); `mayan_tzolkin_catalog_v0.json` Meta `schema_version` 1.0.1.

---

## 2026-04-20: Phase-1 „triviale“ Systeme — v0-Schulwahl (Maya, NSK, Numerologie, Akan)

**Decision:**

| `system_id` | v0 Berechnungsbasis (K1/K2) | K3/K4 / später |
|-------------|------------------------------|----------------|
| **mayan_tzolkin** | **260-Tage-Tzolkʼin** mit **GMT-Korrelation** (JDN-Anker **584283** = klassischer „0.0.0.0.0“-Tag); Siegel-**Slugs** wie im Deskriptor (**Dreamspell-/Arguelles-Namen**: `red_dragon` … `yellow_sun`), weil `canonical_id` darauf ausgelegt ist — explizit **nicht** identisch mit rein akademischer „Imix/Ik“-Benennung in der UI. Wellen/Castle: **Dreamspell-Raster** (13er-Wavespell, 5×52 Burgen). | „traditional_mayan“ / andere Correlations nur als **zweiter Pfad** / `tradition`. |
| **nine_star_ki** | **Japanisches Nine Star Ki** (Sonoda-Linie). **Ausführung K1/K2:** siehe **2026-04-16** (Engine `ic_nine_star_ki_v1`: Overrides + ggf. 1986→1984, **Monatsmuster**, **energetischer Stern**, feste **Sonnenmonats-Schnitte**). Die Zeile unten beschrieb die **frühere v0-Näherung** (nur noch historisch). | Exakte Li-Chun-Uhrzeit / weitere Schulen → v2+ / `tradition`. |
| **numerology** | **Pythagoreische** Buchstaben-Zuordnung (1–9-Zyklus); **Life Path** aus Geburtsdatum; optional **Destiny / Soul Urge / Personality**, wenn `full_name` mitgegeben wird. **Chaldeisch / Kabbalah** → später / andere `tradition`. | Meisterzahlen 11/22/33 wie üblich; Karmic Debt aus Teilstrings → v0 minimal oder v1. |
| **akan** | **Ghanaische Krada-Namenslogik** nach **Wochentag der Geburt** (Wandzeit in `birth.timezone`); Zuordnung **Sonntag=Kwasi/Akosua** … **Samstag=Kwame/Amma** (weit verbreitete Standardtabelle). **Obosom / Adaduanan** → v1 (Literatur-K2). | Varianten `akan_calendar` / `adaduanan` später. |

**Rationale:** Eine klare v0-Linie pro System für **stabile** `canonical_id`s und Konvergenz; transparenzfreundlich für Nutzer:innen; Literatur- und Schulbreite bleibt an K3/K4 und Linsen.

**Consequences:** `@ic/engines` + minimale `*_catalog_v0.json`; UI-Copy „IC v0 rechnet …“; Tests gegen feste Referenzdaten wo möglich.

---

## 2026-04-19: Konvergenz (Person vs. strukturell); v0 „modern“ vs. „traditionell“; Einzel-Linsen

**Decision:**

1. **Zwei gleichberechtigte Wege zu „Klumpen“ / Meta-Einheit im KG:**  
   - **Personengebunden:** Dieselbe Person liefert für mehrere `system_id` aktivierte Teilgraphen; Konvergenz entsteht aus **Überschneidung und Kanten** zwischen den **personbezogenen** Chart-Knoten (starker App-Anker, intuitive UX).  
   - **Personen-unabhängig (strukturell):** Ur-/Grundsysteme und Element-Raster (I Ging, Kabbalah, Chakren, Wu Xing, Pancha Bhuta, westliche Elemente, …) bilden **ohne Geburtsereignis** eigene **Struktur-KGs**; **Klumpen** entstehen über **Cross-System-Kanten** (`maps_to`, `cross_system`), **Embeddings + LLM-Review** und später Meta-Knoten (Datenschicht E) — also **Ontologie-Konvergenz**, nicht nur „gleicher Geburtstag“.

2. **Beides zusammen:** Strukturelle Klumpen **können und sollen** schon in v0 vorbereitet werden (Deskriptoren, Kataloge, erste Kanten); **personengebundene** Konvergenz nutzt dieselbe Kanten-Infrastruktur, sobald Charts existieren.

3. **v0 bei rechenbaren „kleineren“ Systemen (Maya Tzolkin, Nine Star Ki, Numerologie, Akan, …):** Pro `system_id` **genau eine** K1/K2-Berechnungskonvention (eine Correlation / eine Tabellenlogik), damit **Knoten stabil** und **Vergleiche** zwischen Systemen **interpretierbar** bleiben. **Priorität v0:** **gut dokumentierbar + implementierbar + für die erwartete App-Zielgruppe nachvollziehbar** — das tendiert bei **Tzolkin** oft zur **modernen, explizit benannten Linie** (z. B. **Dreamspell / Arguelles**), bei **NSK/Numerologie** zu **einer** klar benannten Schul- bzw. Tabellenvariante (jeweils in Doku/Copy genannt). **„Traditionell“** in v0 primär über **K3/K4** (Literatur, `tradition`, `werk_kategorie`) und **Linsen**, **nicht** als zweiter paralleler Rechenmotor ohne UI-Klarstellung.

4. **Nutzer:innen, die ein System einzeln sehen wollen:** **System-Linsen** bleiben zentral; die v0-Rechenwahl ist **transparenter technischer Default** („IC rechnet v0 so und so“), **kein** Anspruch auf die einzig gültige spirituelle Linie. Roadmap: zweite Rechenvariante / zweite Correlation nur mit **eigenem Scope** (Lens oder `tradition`-Parameter), nicht als stiller Mix.

**Rationale:** Schnittmengen- und Meta-Analysen brauchen **stabile** strukturelle Identitäten; parallele Schulen ohne Modell würden den Graphen **zersplittern**. Strukturelle Klumpen liefern **Wissen über Muster** unabhängig von Geburtsdaten. Modern-vs-traditionell ist bei **K1/K2** eine **Produkt- und Lieferentscheidung**; bei **K3/K4** bleibt Raum für **traditionelle** Tiefe und Mehrstimmigkeit.

**Consequences:** Engines + Kataloge: ein Pfad, Tests, kurze Nutzer:innen-sichtbare Erklärung; KG- und Pipeline-Arbeit an Ur-/Element-Systemen parallel zu Chart-Engines; spätere Schul-Erweiterungen explizit scoped (Doku + Schema), nicht implizit.

---

## 2026-04-18: Gene Keys — Literatur wie alle anderen Systeme

**Decision:** Gene Keys erhält **keine** gesonderte Copyright-/Paraphrase-Policy in den technischen Projekt-Dokumenten. Literaturbeschaffung, Chunking und Extraktion (K3/K4) laufen über dieselbe Pipeline- und Profil-Logik wie bei allen anderen `system_id` (inkl. Quellenprofil / `entity_registry` nach Bedarf).

**Rationale:** Phase-1-Playbook und Datenmodell sind systemagnostisch; Sonder-Doku würde nur Verwirrung erzeugen und suggerieren, dass GK technisch anders behandelt wird — tut es nicht (`gk.*` bleibt eigenständiges Präfix, shared K1 mit HD).

**Consequences:** `cursor/status.md` und `cursor/engines.md` ohne GK-Sonder-Copyright-Abschnitte; rechtliche Fragen pro Verlag/Lizenz bleiben außerhalb der Engine-Doku, wie bei jedem System.

---

## 2026-02-16: Dokumentations-Architektur (Zweischicht)

**Decision:** Cursor-Docs (6 Dateien, < 300 Zeilen, rein technisch) getrennt von Reference-Docs (PRD, Entscheidungen, Ideen, Inspirationen).

**Rationale:** Cursor braucht technische Wahrheit ohne Vision-Ballast. Der Mensch braucht den größeren Kontext. Zwei verschiedene Leser = zwei verschiedene Doc-Sets.

**Consequences:** cursor/ Ordner wird in Cursor-Rule referenziert. reference/ wird nur bei explizitem Verweis gelesen. Alte Docs → 99_archive/.

---

## 2026-02-16: 10 statt 8 Lebensbereiche

**Decision:** Sexualität & Intimität und Beziehungen & Community als eigenständige Bereiche.

**Rationale:** Bei 8 waren Sexualität in "Partnerschaft" und Community in "Familie" versteckt. Jedes System hat zu beiden Themen eigenständige, substantielle Aussagen (HD Sakral/Intimität, BaZi Peach Blossom, Astro 8.Haus). 10 Segmente im Kreis = 36° pro Segment, visuell sauber.

**Consequences:** life_domain Enum hat 10 Werte statt 8. Mandala hat 10 Segmente. Kein Schema-Impact (Tag, nicht Constraint).

---

## 2026-02-16: Mandala als Signatur statt Radar-Chart mit Tiefe

**Decision:** Die persönliche Landkarte zeigt nicht "Beziehung ist wichtiger als Beruf" (Tiefe-Metapher), sondern den gesamten visuellen Abdruck als einzigartige Signatur.

**Rationale:** Tiefe impliziert Bewertung. Die Form des Kompass IST die Signatur — asymmetrisch, einzigartig, ohne Wertung. Äußere Silhouette = Dichte der Chart-Elemente. Farbe = Systemübereinstimmung. Leuchtende Akzente = zeitliche Aktivität.

**Consequences:** Kein "Score" pro Lebensbereich nötig. Stattdessen: Zählung der Chart-Elemente pro Bereich + Farbkodierung. SM-teilbar als Fingerabdruck.

---

## 2026-02-16: Fluss-Diagramm als separater Visualisierungsmodus

**Decision:** Neben dem Mandala (WAS habe ich) ein Fluss-Diagramm (WIE hängt es zusammen), inspiriert vom Gene Keys Hologenetic Profile.

**Rationale:** Mandala = räumlich, statisch, Exploration. Fluss-Diagramm = prozesshaft, dynamisch, Narrativ. Verschiedene Fragen → verschiedene Visualisierungen.

**Consequences:** Fluss-Diagramm ist Phase 2-3 (braucht Schicht D für Cross-System-Flüsse). Premium-Feature.

---

## 2026-02-16: 15 statt 12 Dimensionen

**Decision:** 3 neue Keys: elemental_quality, temporal_phase, destiny_pattern.

**Rationale:** BaZi (Wuxing), Jyotish (Dashas), Maya (Farben) brauchen diese Dimensionen. Ohne sie sind 30%+ der System-spezifischen Bedeutungen nicht abbildbar.

**Consequences:** Nullable jsonb-Feld, keine Breaking Change. Alte Daten bleiben gültig. Pipeline-Prompts anpassen. 11 Kern-Dimensionen (user-facing), 4 ergänzende (system-spezifisch).

---

## 2026-02-16: Drei Sprachebenen (Wording-Strategie)

**Decision:** System-Ebene (Original-Terminologie), Meta-Ebene (eigenes Wording für übergreifende Konzepte), Handbuch-Ebene (Alltagssprache).

**Rationale:** Copyright-Schutz (Not-Self, Useful God sind geschützt). Verständlichkeit (Fachtermini unverständlich für Laien). Synthese-Mehrwert (wenn 3 Systeme dasselbe beschreiben, braucht es einen eigenen Begriff).

**Consequences:** Wording entsteht als Nebenprodukt von generate_meta_nodes. LLM schlägt vor, Mensch finalisiert.

---

## 2026-02-16: Keine Entwicklungsstufen (anti-AQAL)

**Decision:** Keine hierarchische Bewertung ("du bist auf Stufe X"). Stattdessen: Zeitlinie (Phasen statt Stufen).

**Rationale:** Keines der integrierten Systeme kennt Entwicklungshierarchie. Generator ≠ "höher" als Projektor. Stufen implizieren Bewertung. Inner Compass spiegelt, bewertet nicht.

**Consequences:** Zeitlinie-Layer (Schicht C) ersetzt Stufen. Dynamische Aktualisierung statt statische Einordnung. AQAL-Quadranten als interner Qualitätscheck nutzbar (decken unsere Dimensionen alle 4 Perspektiven ab?).

---

## 2026-02-16: System-Filter als Linsen-Metapher

**Decision:** User kann zwischen "Alle Systeme" (Standard) und Einzelsystem-Linsen umschalten.

**Rationale:** Bedient 3 Zielgruppen: System-Kenner, kulturspezifische Nutzer, Einsteiger. Strategischer Nebeneffekt: Erster Cross-System-Switch wird zum größeren Aha-Moment.

**Consequences:** Trivial (system_id-Filter auf allen Queries). Handbuch-Sprache wechselt von Meta auf System-Ebene.

---

## 2026-02-16: Prozess-Layer mit 4-Schritt-Struktur

**Decision:** Erkennen → In Beziehung treten → Verstehen → Integrieren (inspiriert von IFS, ohne dessen Terminologie).

**Rationale:** IFS ist therapeutisch validiert, gibt Chart-Elementen einen konkreten Arbeitspfad. HD sagt "lebe dein Design" (vage). Wir sagen "hier sind 4 Schritte" (konkret).

**Consequences:** Neues process-Feld im Interpretations-Contract (trap, gift_activation, experiment_seed). Neuer Pipeline-Job: extract_process_patterns. Handbuch-Schicht 3+4 werden damit gefüllt.

---

## 2026-02: Postgres+pgvector statt ArangoDB/Neo4j

**Decision:** Bleiben bei Supabase/Postgres. pgvector für Embeddings.

**Rationale:** Supabase bietet Auth, RLS, Storage, Realtime. Kein separater Graph-DB-Server nötig. Edges sind eine Tabelle, Nodes sind eine Tabelle — das reicht für unsere Größenordnung.

**Consequences:** Kein Graph-Traversal-Performance-Vorteil. Wenn jemals Millionen Nodes: exportieren. Für jetzt: Einfachheit > Performance.

---

## 2026-02: Strukturbäume aus Deskriptoren, NICHT aus PDFs

**Decision:** Systemstruktur (welches Gate in welchem Center) aus JSON-Deskriptoren + Engine-Code. NICHT aus PDF-Extraktion.

**Rationale:** Struktur ist deterministisch und fest. PDFs beschreiben Interpretationen, nicht Struktur. "Gate 34 ist im Sakral-Zentrum" ist eine Tatsache, keine Interpretation.

**Consequences:** Phase 0 = Seed-Script (Deskriptor → Nodes + Edges). PDFs reichern Nodes an, erzeugen sie nicht. Graph existiert BEVOR erste PDF verarbeitet wird.

---

## 2026-02: Embeddings für Cross-System-Mapping statt manuell

**Decision:** Cosine Similarity + LLM-Validierung statt manuelles Kuratieren.

**Rationale:** Skaliert auf beliebig viele Systeme. 50 manuelle Mappings als Startpunkt, dann automatisch. LLM + Embeddings ersetzen manuelles Kuratieren komplett.

**Consequences:** pgvector Pflicht. extract_cross_mappings Job. Review-Status-Feld auf Edges. Human Review bleibt Option (approved/rejected), aber nicht Pflicht.

---

## 2026-02: 4-stufige Extraktion statt ein LLM-Call

**Decision:** extract_entities + extract_meanings + extract_relationships + extract_processes statt alles in einem Prompt.

**Rationale:** Verschiedene Wissensebenen (Fakten vs. Bedeutungen vs. Beziehungen vs. Prozesse) brauchen verschiedene Prompt-Strategien. Ein Call vermischt diese Level.

**Consequences:** 4x so viele LLM-Calls. Aber: Bessere Qualität, sauberere Daten, leichter debuggbar.

---

## 2026-02-16: Zwei-Gate-Filtering für Content-Akquise

**Decision:** Breit scrapen, dann zweistufig filtern statt strenge Keyword-Filter.

**Rationale:** Anna's Archive Scraping produziert ~85% Noise (z.B. "UX Design" bei Suche nach "human design"). Einfache Keyword-Filter sind zu aggressiv — Nischen-Themen wie "Projector Empowerment", "Pfeile", "Liebe im HD" fallen raus. Stattdessen: Gate 1 = leichtgewichtige LLM-Vorklassifikation auf Titel+Metadaten (vor Download), Gate 2 = volle Inhaltsklassifikation nach MinerU-Extraktion (im Worker).

**Consequences:** Kein manuelles Kuratieren nötig. Noise wird automatisch erkannt. Nischen-Themen kommen durch. Admin-Review-Queue für Grenzfälle (Confidence 0.3–0.6). Kein Stub im Produktivbetrieb.

---

## 2026-02-16: Clean Data Restart (keine alten HD-Daten übernehmen)

**Decision:** Bestehende hd_assets/hd_asset_chunks/hd_interpretations in Cloud-DB NICHT migrieren. Sauberer Neustart mit sys_*-Schema.

**Rationale:** Bisherige Daten: 85% Noise in Assets, alle Interpretations sind Stubs ("mvp_stub", system: "other"), Ingestion-Jobs nur noch failed extract_interpretations. 113 PDFs sind schnell neu prozessiert — und diesmal richtig (mit echtem LLM, ohne Noise, mit Pre-Filtering). Schema ändert sich komplett (hd_* → sys_*).

**Consequences:** Lokale DB: supabase:web:reset löscht alles. Cloud: manuell bereinigen. Kein Datenverlust (alles war Stub/Noise). Anna's Archive Pipeline mit verbessertem Filtering neu durchlaufen.

---

## 2026-02-16: Verarbeitung pro System, in Wellen

**Decision:** Systeme nacheinander verarbeiten (HD → Gene Keys → Astro → BaZi → ...), nicht alle gleichzeitig.

**Rationale:** Pro-System ermöglicht Qualitätsvalidierung, Noise-Erkennung und Pipeline-Tuning. Kein Bias-Risiko, da jedes System eigene Wissensbasis aufbaut und Cross-System-Mappings erst in P4 kommen.

**Consequences:** HD als erstes System (größtes Corpus, am besten validierbar). Erkenntnisse aus HD-Verarbeitung fließen in Pipeline-Optimierung für Folgesysteme.

---

## 2026-02-16: Clean Inner Compass statt hd_*-Patch

**Decision:** Frischen Makerkit-Stand pullen, dann sauberen Inner Compass Teil (Schema, Worker, Scripts) neu aufsetzen. Kein String-Replace auf 2400 Zeilen altem Worker.

**Rationale:** 10 Migrations → 1-2 saubere (sys_* + pgvector + neue Felder von Tag 1). Worker referenziert direkt sys_*. Kein Legacy-Code. Wissen/Patterns aus altem Worker werden übernommen, aber Code neu geschrieben.

**Consequences:** Alter Worker (hd_worker_mvp.py) bleibt als Referenz. Makerkit-Framework (Auth, Accounts, RLS, UI-Shell) bleibt wie es ist. Nur der projektspezifische Teil wird neu.

---

## 2026-02-16: Interpretation-zentrierter Ansatz statt NVIDIA-style Triple-Extraktion

**Decision:** Bedeutungs-Extraktion (15 Dimensionen pro Chunk, ~1000 Tokens) statt starre Triple-Extraktion (Subject-Predicate-Object per 512 Zeichen wie NVIDIA text2kg Playbook).

**Rationale:** NVIDIA text2kg ist NER+RE für faktische Domänen (News, Finance) mit festen Entity-Typen (ORG, PERSON) und 15 Relationsverben. Esoterische Texte brauchen Kontext für Bedeutung — 512-Zeichen-Chunks reißen das auseinander. Unsere Dimensions-Struktur (shadow, gift, archetype...) fängt mehr auf als flache Triples. Text2kg kommt danach deterministisch.

**Consequences:** Kein NVIDIA-Pipeline-Klon. Eigene Ontologie (Gate, Center, Stem, Archetype). Eigene Relationsverben (symbolisiert, korrespondiert_mit, aktiviert). Chunk-Größe bleibt ~1000 Tokens. Von NVIDIA übernehmen: Pipeline-Architektur, ggf. cuGraph für spätere Graph-Analytik, LoRA Fine-Tuning als Option.

---

## 2026-08-05: Incarnation Crosses — Chunk-Meta-Tagging statt Re-Chunk/Re-Interpret (Korrektur des Vorschlags vom selben Tag)

**Kontext:** Vorheriger Plan (dokumentiert oben, "Theme-Parent + Varianten-Children") sah als nächsten Schritt vor, entweder (a) `hd.cross_theme.*` Parent-Nodes zu seeden ODER (b) q6 *(„Incarnation Crosses by Profile")* mit dem neuen Chunk-Profil **komplett neu zu chunken und neu zu interpretieren** (löscht alte Chunks via `_delete sys_source_chunks`, danach volle LLM-Re-Interpretation aller ~1440 Chunks über Langdock).

**Warum das ein Fehler gewesen wäre:**
1. **Kosten:** Volles Re-Interpret von 1440 Chunks über Langdock (gpt-5-mini) kostet unnötig Geld/Zeit für etwas, das rein strukturell (Canonical-ID-Zuordnung) ist — keine inhaltliche Extraktionsschwäche.
2. **Risiko:** `_handle_extract_text` löscht `sys_source_chunks` für die Quelle komplett (`_delete ... where source_id=...`). Ob/wie dabei bereits verlinkte `sys_interpretations` (4732 Stück, inkl. der frisch gefixten 546 Cross-Links aus dem Elements-Remap) betroffen sind, war nicht verifiziert (FK-Verhalten unklar). Unnötiges Risiko für bereits vorhandene Arbeit.
3. **Der eigentliche Engpass war nie die Extraktion**, sondern dass `sys_source_chunks.metadata` für q6 keine `canonical_id`/`canonical_ids` trug (Buch nutzte generisches `paragraph_accumulate`-Chunking statt eines Profils) — der Worker-Code (`_resolve_canonical_ids_from_interp`, `_primary_element_hint_from_chunk_meta`) liest genau diese Felder bereits.

**Decision:** Statt Re-Chunk/Re-Interpret → **reines Metadata-Patch + kostenloser Re-Link:**
1. Neues Skript `ic_hd_cross_chunk_tag.py` scannt die **bestehenden** 1440 Chunks von q6 nach `"THE Nth GATE"`-Ankern (Regex, gleiche Logik wie das Chunk-Profil) und trägt den zuletzt gesehenen Gate-Anker pro Chunk fort (Forward-Fill über Chunk-Grenzen, da altes Chunking nicht an Gate-Grenzen ausgerichtet war).
2. Für jeden Chunk werden `personality_sun_gate`, `quarter`, `canonical_ids` (RAC/JC/LAC), `canonical_id`/`primary_canonical_id` **additiv in die Metadata gepatcht** — kein Löschen, kein Re-Chunk. Ergebnis: 1439/1440 Chunks getaggt, alle 64 Gates abgedeckt.
3. Ein einziger `text2kg`-Job wird für die Quelle neu enqueued. `text2kg` liest bei jedem Lauf **alle** Interpretationen der Quelle frisch + aktuelle Chunk-Metadata neu (kein "skip existing") — der Worker-Code hängt jetzt automatisch die `canonical_ids` aus der Chunk-Metadata an jede Interpretation an (Ergänzung vom 2026-08-05 in `_resolve_canonical_ids_from_interp`), **ohne LLM-Call**. Reines DB-Linking.

**Trade-off, den wir bewusst eingehen:** Die Genauigkeit der Gate-Zuordnung pro Chunk ist eine Näherung (letzter Anker im Chunk gewinnt für den ganzen Chunk; TOC-Abschnitte am Buchanfang können vereinzelt falsch/uneindeutig getaggt sein). Für 1440 Chunks ist das kein Problem — echte Content-Kapitel sind lang genug, dass die Näherung trägt.

**Bekannte Ineffizienz (nicht behoben, nur dokumentiert):** `_handle_text2kg` → `_link_interpretation_to_node` macht pro (Interpretation × Canonical-ID) einen **GET+PATCH-Roundtrip** gegen `sys_kg_nodes` (kein Batching). Bei ~4700 Interpretationen × jetzt ~3 zusätzlichen Cross-IDs pro getaggtem Chunk sind das grob 15–20k sequenzielle HTTP-Calls → Laufzeit im Bereich von 30–90+ Minuten für einen einzelnen Re-Link-Lauf. Für kleine Quellen unkritisch, für große/wiederholte Relinks ein Kandidat für Batch-Optimierung (`sys_kg_nodes` Upsert mit mehreren IDs pro Request), aber **kein Blocker jetzt**.

**Nacharbeit (Abend 2026-08-05):** Der erste Full-`text2kg` nach Tagging endete bei nur **51/192**, weil der laufende Spark-Worker den lokalen Chunk-Meta-Fix (`canonical_ids` in `_resolve_canonical_ids_from_interp`) **noch nicht deployed/restarted** hatte — und weil `payload.elements` oft schon (falsche) IDs trägt und den Fallback auf `chunk_meta.canonical_id` überspringt. Lösung: dediziertes Skript `ic_hd_cross_chunk_relink.py` (lädt Chunks+Interps, aggregiert in-memory, **1 PATCH pro Cross-Node**) → **192/192 Nodes, +4190 Links**. Worker danach neu gestartet. Scoped Synth für alle 192 enqueued.

**Offen:** `hd.cross_theme.*` Parent-Nodes bewusst **noch nicht** geseedet — Chart-Engine kennt immer die exakte Variante; erst messen, ob genug Literatur nur den Kurznamen ohne Gate-Kontext nennt.

---

## 2026-02-16: pgvector bestätigt als richtige Lösung

**Decision:** Postgres+pgvector für Embeddings und Cross-System-Mapping. Kein separater Vector-DB-Server.

**Rationale:** Supabase hat pgvector-Extension bereits. Für ~500-5000 Nodes mehr als ausreichend. Einziger Zweck: Cosine Similarity für Cross-System-Mapping-Kandidaten (Schicht D). Kein Pinecone/Weaviate/Qdrant nötig.

**Consequences:** `sys_kg_nodes.embedding vector(1536)` + ivfflat-Index kommt in Schema-Migration. text-embedding-3-large oder lokales Modell auf Spark.

---

## 2026-02: LLM-Wahl: Qwen3-32B als Default

**Decision:** Qwen3-32B als primäres Extraktions-/Synthesis-Modell auf Spark.

**Rationale:** Multilingual (100+ Sprachen), JSON/Structured Output, Apache-2.0 Lizenz, läuft bereits als NVFP4 auf Spark. BaZi-Quellen (Chinesisch) und Jyotish-Quellen (Sanskrit) profitieren von Mehrsprachigkeit.

**Consequences:** DeepSeek R1 8B als Alternative wenn Content zu stark gefiltert wird. A/B-Test mit 5-10 Chunks empfohlen bei Model-Wechsel. Model-Switcher erlaubt Wechsel ohne Code-Änderung.

---

## 2026-02: Deep Structure Seed = Backlog, nicht Sprint

**Decision:** Strukturvertiefung (832 → ~2000 Nodes) erfolgt demand-driven, nicht als Block vor S5.

**Rationale:** 832 Nodes (HD: 526, alle 10 Systeme) reichen vollständig für S5-Validierung. Wenn vor der Pipeline-Validierung 15-20h Daten kuratiert werden, blockiert das den kritischen Pfad. Falls S5 Contract-Anpassungen erfordert, müssten kuratierte Daten ggf. nochmal angefasst werden.

**Consequences:** S5 startet sofort mit bestehendem Graph. Fehlende Nodes werden erst nachgezogen wenn die Pipeline sie tatsächlich vermisst. Vollständiger Backlog in `reference/deep_structure_plan.md`. HD-Vertiefung (Crosses, PHS, Partners) nach S7 in P1.

**Klarstellung (2026-07-01):** Die Entscheidung betrifft **Sprint-Timing**, nicht die Architektur. Atomare K2-Nodes (17 PHS, 192 Crosses, …) **sollen** geseedet werden — Quelle ist `system_structure/*` + Engine, **nicht** PDF. ~69.120 berechnete Positionen werden **nicht** als Nodes modelliert (Chart-K1). Phase 0 „100 %“ = Infrastruktur; vollständiger K2-Seed = offener Phase-1-Punkt.

---

## 2026-01: Schema hd_* → sys_* (Clean Restart)

**Decision:** EINE saubere Migration statt 10 Patches. 10 Tabellen mit sys_* Präfix.

**Rationale:** Kognitiver Overhead: hd_kg_nodes liest sich als "HD" statt "Meta-System". Technische Schuld: 10 Migrations-Dateien. pgvector von Anfang an.

**Consequences:** ~2-3 Tage Aufwand. Infra bleibt (Spark, Worker, MinerU). Nur Tabellennamen + neue Felder.
