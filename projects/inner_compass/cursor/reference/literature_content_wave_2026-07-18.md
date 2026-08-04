# Literatur Content-Wellen — Stand 2026-07-18

last_update: 2026-08-04 (Gates+Channels+Circuits Layer-Synth Re-Fix; text2kg Auto-Synth Root-Cause behoben)
scope: Alle kuratierten Werke bleiben im Scope; Reihenfolge = K2-Struktur + Subsysteme, nicht Alphabet
in_scope: Inventar-Refresh, Queue, Orientierungsprinzip, Synth-Wellen-Policy, Open Hygiene
out_of_scope: PDF-Upload/Pipeline-Ausführung (läuft separat)

## Orientierung — woran sich die Reihenfolge hält


| Orientierung                                             | Nutzen für Literatur-Pipeline?                                                 |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **K1** (Chart zur Laufzeit)                              | **Nein** — Pillars/Gates einer Person sind kein Werk-Curriculum                |
| **K2 Katalog-Layer**                                     | **Ja** — Types → Centers → Gates → Channels → Profiles → PHS → …               |
| **Subsystem-Priorität** (`hd_catalog` `phase1_priority`) | **Ja** — `required` bodygraph/PHS vor `optional` DreamRave/BG5/Cosmology       |
| **Registry `download_priority_order`**                   | **Ja, sekundär** — war für AA-Downloads; deckt sich grob mit Kanon vor Schulen |
| **Alphabet / Dateiname**                                 | **Nein** — nur Zufallsreihenfolge                                              |


**Kurz:** Werke füttern **K3/K4 auf K2-Nodes**. Deshalb folgen wir der **K2-Abhängigkeit**, nicht K1 und nicht dem Dateinamen.

## Alle Werke bleiben

208 `status=ok` — nichts aussortieren. Wellen = Queue-Reihenfolge.


| Wave | Bedeutung                 | ~Anzahl |
| ---- | ------------------------- | ------- |
| 0    | Bereits S5/S6             | 5       |
| 1    | Core-Struktur (Layer ≤25) | ~45     |
| 2    | Mid/PHS (Layer ≤45)       | ~32     |
| 3    | Schulen / modern / Rest   | ~126    |


Queue: `reference/literature_content_wave_queue_2026-07-18.csv`  
Builder: `scripts/build_content_wave_queue.py` (Feld `structure_layer` + `structure_layer_name`)

## Synth-Policy (Content-Welle) — verbindlich ab 2026-07-22

`synthesize_node` ist **pro System** (`system_id=hd|bazi|…`), aber innerhalb des Systems **alle Nodes mit `interpretation_ids`** — nicht nur das aktuelle Buch.


| Regel                                                          | Warum                                                                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Pro PDF: Extract → classify → interpret → **text2kg (strict)** | Interps + Links skalieren linear                                                                       |
| **Kein** Full-`synthesize_node` nach jedem PDF                 | Laufzeit wächst mit allen gelinkten Nodes des Systems (~200 HD-Werke wären sonst unpraktikabel)        |
| Synth in **Wellen**                                            | Nach Layer (Types / Channels / Centers / …) oder gezielt `only_canonical_ids` / `ic_k2_synth_batch.py` |
| Roh-Interps bleiben in DB                                      | Synth kann jederzeit nachziehen; Qualität ≠ „sofort nach jedem Buch“                                   |


**GPU:** Phase 1 (`extract_text` / MinerU) und Phase 2 (LLM) nicht parallel. Werke mit nur `extract` queued warten, bis LLM-Synth-Welle fertig ist — das ist ok (z. B. Channels by Type 1).

**Zombies:** Jobs auf `running` ohne Worker-Fortschritt (oft Spark↔Supabase-Timeout) → failed resetten + einen Synth-Job neu enqueuen. Status-Ping/Automation später sinnvoll; kein Blocker für die Policy.

**GPU-Mutex:** MinerU-Extract und SGLang-LLM **nicht parallel** — LLM stoppen (`~/ai/scripts/serve/sglang_stop_all.sh`), Extract, danach LLM wieder starten + Phase2. Sonst MinerU → „produced no .md“ (VRAM voll).

## HD — Layer-Reihenfolge (Bodygraph zuerst)

Entspricht `hd_catalog_v0.json` Subsysteme + `deep_structure_plan.md`:

1. **Types / Design Concepts / Living Your Design** ✅
2. **Channels** (Life Force ✅ → Channels by Type 1–4 ✅ + Layer-Synth ✅ 2026-07-23, **Re-Synth mit Selection-Fix ✅ 2026-08-04**)
3. **Circuits** (Ra: *Rave BodyGraph Circuitry* ✅ extract → text2kg → Alias-Relink → Layer-Synth 2026-07-24, **Re-Synth mit Selection-Fix ✅ 2026-08-04**)
4. **Centers** (kein Ra-Original im Inventar → Winn → Schoeber als K3/K4; **strict text2kg** ✅ 0 Stubs; Layer-Synth ✅ 9/9 2026-08-04)
5. **Gates/Lines Companion** (Rave I'Ching ✅ Re-Interpret 2026-08-04; Layer-Synth ✅ 64/64 2026-08-04; Line-Companion-Bücher nachziehen)
6. **Profiles / Incarnation Crosses**
7. **PHS** (Variables, Color/Tone/Base)
8. **Rave Psychology**
9. **Schulen** (Quantum, Parkyn, …) — `tradition`-Tags
10. **Optional:** DreamRave, BG5, Design of Forms, Cosmology

**Reihenfolge ist Leitplanke, kein Dogma:** Ra-`K2_ref` vor Schulen. Deshalb Circuits (Ra) vor Winn-Centers, auch wenn die Queue-CSV Centers numerisch früher listet.

## Open Hygiene (Nacharbeit) — Stand 2026-08-04

Channels-Layer ist **sauber** (36/36 + Synth). Darüber hinaus offen:


| Item                                                  | Status                                                                        | Wann                  |
| ----------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------- |
| Reverse-Channel-Dupes (10)                            | ✅ gemerged + gelöscht                                                         | done                  |
| Invalid Channels (`1_2`, `5_1`→Profil, `6_3`→Line, …) | ✅ remapped/unlinked                                                           | done                  |
| Catalog-Guard Gates/Channels/Lines                    | ✅ `ic_hd_k2_catalog.py` + Worker kein Fake-Channel                            | done                  |
| Gate-Wildwuchs `66/67/69` + Fake-Lines (`28_38`…)     | ✅ remapped/gelöscht (`ic_hd_gate_line_hygiene.py`)                            | done                  |
| Circuitry text2kg unmatched (35)                      | Aliase + Relink; Residual dokumentiert (unten)                                | done                  |
| Circuitry Alias-Relink + Circuits-Synth               | Relink ✅; Layer-Synth ✅ 9/9 (ohne `integration`)                              | done                  |
| Circuitry Residual-Wildwuchs (nicht aliasbar)         | Fake-Channels / `asset_chunk.*` / malformed Gate-Lines — strict leave         | later optional        |
| Qwen3 Thinking-Hang bei Synth                         | `chat_template_kwargs.enable_thinking=false` in `ic_worker._call_llm`         | done                  |
| Stub-Interps von Nodes unlinken                       | ✅ `ic_stub_interp_hygiene.py --unlink-from-nodes --apply` (100 Nodes, −136) | done                  |
| Rave I'Ching Re-Interpret                             | ✅ Langdock + Hint: 65/65 Interps, Gate-Tag 64/64, text2kg, 64/64 Nodes      | done 2026-08-04       |
| Gene Keys Opening Doors 18 Stubs                      | ✅ Langdock: 18 Stub-Chunks → real; **39/39** Interps, 0 Stubs, text2kg ✅; Full-Synth cancelled | done 2026-08-04 |
| Synth lädt nur `interpretation_ids[:15]`              | ✅ Load Default **alle** IDs; Prompt max **12** + Diversität (`ic_worker`)   | done 2026-08-04       |
| **text2kg auto-enqueued unscoped Full-Synth**         | ✅ Root-Cause gefunden (Audit) + gefixt: Default jetzt **aus** (`IC_TEXT2KG_AUTO_SYNTH=false`); Synth nur noch explizit via Layer-Skripte | done 2026-08-04 |
| Gates-Layer-Synth (Re-Synth mit Selection-Fix)        | ✅ 64/64 via Langdock, ~14,5 Min, Job `cf980fb6…`                             | done 2026-08-04       |
| Channels-Layer-Synth (Re-Synth mit Selection-Fix)     | ✅ 36/36 via Langdock, Job `cbd6820f…` — `20_34` jetzt korrekt (Charisma, 34↔20) | done 2026-08-04 |
| Circuits-Layer-Synth (Re-Synth mit Selection-Fix)     | ✅ 9/9 via Langdock, Job `d5d87e09…`                                          | done 2026-08-04       |
| Centers-Layer-Synth (Winn+Schoeber, Selection-Fix)    | ✅ 9/9 via Langdock, Job `1a361e2c…`, ~2,5 Min                                | done 2026-08-04       |
| HD-Rest-Layer (Types/Authorities/Profiles/Lines/Definitions/PHS) | ✅ 31/31 via Langdock, Job `12312a82…`, ~6 Min                     | done 2026-08-04       |
| **BaZi Re-Synth** (Destiny Code, war am stärksten vom alten Fenster betroffen) | ✅ 34/34 via Langdock, Job `d1a70862…`, bis zu 105 Interps/Node vorher gekappt auf 8 | done 2026-08-04 |
| GeneKeys Re-Synth (Vollständigkeit, geringes Risiko)  | ✅ 64/64 via Langdock, Job `76e5b1d7…`, ~12 Min                               | done 2026-08-04       |
| **Voll-Audit:** Stubs noch verlinkt? Jobs hängend?    | ✅ 0 Stub-Interps verlinkt (alle Systeme), 0 queued/running Jobs              | verifiziert 2026-08-04 |
| Profile/Lines Inhaltslücken                           | erwartet (dünne Interp-Dichte je Line, nicht behebbar ohne mehr Bücher)       | beobachten            |

### LLM-Betrieb / Kosten (empirisch 2026-08-04)

**Langdock-Konto:** ~**€0,41** für A/B-Piloten + Retries + Rave-Full (65 Chunks `gpt-5-mini`, Base `https://api.langdock.com/openai/eu/v1`).

Grobe Ableitung (konservativ, inkl. Pilot-Overhead):

| Größe | Schätzung |
| ----- | --------- |
| pro Interpret-Chunk (`gpt-5-mini`) | ~**€0,004–0,006** |
| Rave 65 Chunks allein | ~€0,25–0,35 |
| 10 000 Chunks Mass-Interpret | ~**€40–60** |
| 20 000 Chunks | ~**€80–120** |
| Synth (Layer, stärkeres Modell) | extra — nicht in den €0,41 |

→ Frühere Mid-Schätzung (~€55–60 Full-Wave Interpret-lastig) bleibt plausibel; Synth/QA separat.

**Hybrid (Soll):** Mass-Interpret → Langdock `gpt-5-mini`; Extract/MinerU → Spark GPU; Synth-Wellen → Spark/Qwen *oder* später stärkeres Langdock-Modell. Unscoped Full-`synthesize_node` nach jedem Buch weiter **vermeiden**.

### Rave A/B + Full Re-Interpret

Skripte: `ic_rave_ab_interpret.py`, `ic_stub_interp_hygiene.py`, `start_rave_langdock_worker.py` / `restart_rave_langdock_reinterp.py`  
Source: `3c7c0a7b-9dd1-41b1-ac47-c0cd26dedbe5`

1. Offline A/B Spark vs Langdock (JSONL, kein DB-Write)  
2. Primary-Element-Hint → Retest 5/5 beide  
3. Worker `force_reextract` via Langdock → text2kg strict  
4. Unscoped Synth nach text2kg **cancelled**

**Ergebnis:** 65/65 Interps, 0 Stubs, Gate-Tag 64/64, alle 64 `hd.gate.*` mit Rave-Interp gelinkt.

### Primary-Element-Hint — Status

**Bereits im Worker** (`ic_worker._primary_element_hint_from_chunk_meta`): nutzt vorhandene Chunk-Metadata.

| Metadata | Hint |
| -------- | ---- |
| `canonical_id` | Primär-Entity soft-anchorn |
| `element_type` + `element_id` | dito |
| `gate_number` | HD `hd.gate.N` / Gene Keys `gk.gene_key.N` |
| nichts (Narrativ) | kein Hint — LLM liest Text |

**Kein zweites Hint-System nötig.** Offen bleibt nur Extract-seitig: Chunk-Profile sollen Primär-Entity in Metadata schreiben, wo sie sie kennen (wie `rave_iching_gates`). text2kg löst dieselben Felder schon als Fallback.


**Guard-Scope:** Nicht nur Channels — Gates nur 1–64, Channels nur Katalog-36 (inkl. Reverse-Normalize), Lines nur `gate∈1..64` ∧ `line∈1..6`. Centers/Types/Profiles/Circuits ohnehin Katalog+Alias.

### Circuitry unmatched detail (source `88ed9448`, text2kg 2026-07-24)

**Pass 1** (`b562dfbc`): 35 Interps nicht gelinkt (Strict; kein Node-Create).


| Reason                   | n   | Beispiele                                        |
| ------------------------ | --- | ------------------------------------------------ |
| `not_in_hd_k2_whitelist` | 27  | siehe Taxonomy unten                             |
| `unresolved`             | 8   | meist. `asset_chunk` Element-Refs ohne Canonical |


**Aliase** (in `ic_hd_k2_catalog.py`, deployed Spark):


| Roh / LLM-ID                                    | → Canonical                               |
| ----------------------------------------------- | ----------------------------------------- |
| `hd.circuit.understanding`                      | `hd.circuit.collective_logic`             |
| `hd.circuit.sensing`                            | `hd.circuit.collective_abstract`          |
| `hd.circuit_group.individual/collective/tribal` | `hd.circuit.individual/collective/tribal` |
| `hd.circuit.centering` / `hd.center.centering`  | `hd.circuit.individual_centering`         |


**Pass 2 Relink** (`bbae61d0`): completed; Coverage danach u. a. `collective_logic` 3 Interps, `collective_abstract` 2 (vorher 0). Worker-Log Pass-2: ~344 linked, ~23 unmatched residual.

**Residual-Taxonomy (nicht aliasbar — bewusst unmatched / später Hygiene):**


| Klasse                  | IDs                                                                          | Aktion                                          |
| ----------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------- |
| Fake-Channels           | `hd.channel.3_6_0`, `4_2_5_3`, `50_20`, `9_20`, `understanding_circuit`      | leave (Catalog-Guard)                           |
| LLM-Chunk-IDs           | `hd.asset_chunk.88ed9448_*` + unresolved `asset_chunk`                       | leave                                           |
| Malformed Gate/Line     | `hd.gate.31_7`, `hd.gate.54.4`, `hd.gate.59_line.1..3`, bare `hd.line.4/5/6` | optional später remap (31-7→Channel; 54.4→Line) |
| Alias-Klasse (erledigt) | `understanding` / `sensing` / `circuit_group.*` / `centering`                | via Alias                                       |


**Interp-Dichte nach Relink (dünn):** viele Circuit-Nodes nur 1–3 Interps — Buch streut Labels stark; Layer-Synth trotzdem für alle Nodes **mit** Interps. `hd.circuit.integration` = 0 Interps → nicht im Synth-Scope.

**Layer-Synth Ergebnis (2026-07-24):**


| Canonical                         | Interps | synth_chars (ca.)       |
| --------------------------------- | ------- | ----------------------- |
| `hd.circuit.collective`           | 1       | ~289                    |
| `hd.circuit.collective_abstract`  | 2       | ~609                    |
| `hd.circuit.collective_logic`     | 3       | ~541                    |
| `hd.circuit.individual`           | 1       | ~361                    |
| `hd.circuit.individual_centering` | 2       | ~325                    |
| `hd.circuit.individual_knowing`   | 1       | ~393                    |
| `hd.circuit.tribal`               | 1       | ~396                    |
| `hd.circuit.tribal_defense`       | 2       | ~469                    |
| `hd.circuit.tribal_ego`           | 1       | ~432                    |
| `hd.circuit.integration`          | 0       | stub (~11) — kein Synth |


Jobs: Batch `4206ecb6` (9 IDs) + Follow-up `1f39a3a1` (nur `individual_centering` nach Hang).

**Wichtig — Buchinhalt ≠ nur Circuits:** TOC ist überwiegend Channel-Kapitel (Integration + Knowing/Centering/Understanding/Sensing/Ego/Defense). Audit 2026-07-24 (`source 88ed9448`, 100 Interps):


| Namespace      | Nodes mit Circuitry-Interps | Bemerkung                                              |
| -------------- | --------------------------- | ------------------------------------------------------ |
| `hd.channel.*` | **36/36**                   | voll integriert via text2kg (z. B. `20_34` 13 Interps) |
| `hd.gate.*`    | 61                          | Nebenlinks aus Channel-Text                            |
| `hd.circuit.*` | 9                           | dünn (1–3) — Circuit-Kapitel kurz                      |
| `hd.center.*`  | 8                           | Nebenlinks                                             |
| orphan Interps | 5                           | Residual/strict                                        |


→ Channels wurden **nicht außen vor gelassen**. Circuit-Layer-Synth hat nur `hd.circuit.`* neu geschrieben; Channel-**Wortings** stammen noch aus Life-Force/Channels-by-Type (Interps aus Circuitry hängen schon an den Nodes, Re-Synth optional).

**Ops-Notes 2026-07-24:**

1. Mehrfach-`spark_s5d_synth_only.sh` → kurze Multi-PID-Fenster → Job als Zombie `running`. Fix: Job resetten, **einen** Worker.
2. Qwen3 Thinking kann einzelne Synth-Calls >10 Min streamen und `requests` Timeout umgehen. Fix: `enable_thinking=False` in `_call_llm` (deployed Spark).

### Centers (Winn + Schoeber) — Stand 2026-08-04 ✅ Layer-Synth done


| Buch                             | source_id  | Extract      | Interpret     | text2kg | Layer-Synth                          |
| -------------------------------- | ---------- | ------------ | ------------- | ------- | ------------------------------------ |
| Winn *Understanding the Centers* | `c90803be` | ✅ 276 chunks | ✅ 276/276, 0 stubs | ✅      | ✅ scoped, Job `1a361e2c…` |
| Schoeber *The Centres*           | `3a5fe2ff` | ✅ 160 chunks | ✅ 160/160, 0 stubs | ✅      | ✅ scoped, Job `1a361e2c…` |


Center-Nodes haben bereits viele Links (z. B. Throat 138, Sacral 133). **Es fehlt nicht Phase2**, sondern nur der **scoped Centers-Layer-Synth** nach Selection-Fix. Die queued `synthesize_node`-Jobs sind Full-System (unscoped) — Selection-Fix hat hier den größten Hebel. 9/9 Nodes fertig via Langdock in ~2,5 Min, Job `1a361e2c…`, `completed`.

### Synth-Prozess — Review + Audit-Ergebnis (2026-08-04)

Pro PDF: Extract → classify → interpret → **text2kg strict** → **kein** Full-Synth.  
Pro Layer (Types / Channels / Circuits / Gates / Centers / …):

1. Alle relevanten Bücher bis text2kg  
2. Optional Alias/Relink / Hygiene  
3. **Selection:** alle gelinkten Interps **laden**, dann ranken/diversifizieren → begrenzte Prompt-Menge  
4. `synthesize_node` mit `only_canonical_ids` (Skript: `ic_synth_layer_ops.py`)  
5. QA Stichprobe

**Unscoped vs scoped (wichtig):** Nach text2kg enqueued der Worker früher **immer** `synthesize_node` **ohne** `only_canonical_ids`. Das schreibt **alle** Nodes eines Systems neu (Gates+Channels+Centers+…), nicht nur die vom aktuellen Buch betroffenen.

**Ist das real passiert — Audit über alle 81 je gelaufenen `synthesize_node`-Jobs (`ic_synth_audit_all_systems.py`):**

31 completed Jobs waren unscoped (Vollsystem), u. a. **3× `hd`** während der Content-Welle selbst (q1 Design Concepts 07-19, q2 How to Read a Graph 07-20, q5 Channels by Type 4 07-22) sowie mehrfach Rave, Gene Keys und 1× BaZi. D. h. **pro System reicht nicht** — jeder dieser Läufe hat mit der alten, engen Auswahl-Logik (nur `interpretation_ids[:15]`, max. 8, keine Quellen-Diversität) das *gesamte* System überschrieben. Konkret betroffen: Channels-Layer (36/36, Stand 2026-07-23) und Circuits-Layer (9/9, Stand 2026-07-24) — beide vor dem Selection-Fix entstanden.

**Fix (Root-Cause, nicht nur Symptom):** `_handle_text2kg` in `ic_worker.py` enqueued den Synth-Job jetzt nur noch, wenn `IC_TEXT2KG_AUTO_SYNTH=true` explizit gesetzt ist (Default **false**). Text2KG verlinkt weiter Interpretationen an Nodes, löst aber keine automatische Synthese mehr aus. Synthese läuft ausschließlich noch explizit **pro System UND pro Layer/Element-Cluster** über `ic_synth_layer_ops.py --enqueue-layer <prefix>` bzw. `ic_k2_synth_batch.py`.

**Re-Synth durchgeführt (2026-08-04, alle via Langdock/gpt-5-mini):**

| Layer | Scope | Ergebnis |
| ----- | ----- | -------- |
| Gates | 64 `hd.gate.*` | ✅ 64/64, Job `cf980fb6…`, ~14,5 Min |
| Channels | 36 `hd.channel.*` | ✅ 36/36, Job `cbd6820f…` — Stichprobe `20_34` jetzt korrekt (Charisma-Channel, Gate 34↔20) |
| Circuits | 9 `hd.circuit.*` (10. = `integration`, 0 Interps, kein Synth) | ✅ 9/9, Job `d5d87e09…` |

**Load vs Prompt:** DB-Load Default = **alle** gelinkten IDs (`IC_SYNTHESIS_LOAD_INTERPS=0`). Prompt bekommt davon max. **12** (`IC_SYNTHESIS_MAX_INTERPS`) — nicht weil wir Quellen ignorieren, sondern weil ein LLM-Call nicht 100+ Volltexte sinnvoll fusioniert (Qualität + Context + Kosten). Diversität sorgt, dass mehrere Bücher im Prompt landen. Später optional Map-Reduce (Cluster→Zwischenfazit→Final).

**Update 2026-08-04, zweite Runde — alles geschlossen:** Vollständiger Coverage-Check zeigte, dass BaZi (Destiny Code) am stärksten betroffen war — 25 von 34 Nodes hatten >15 Interps, bis zu **105** (Stems/Branches/Ten-Gods), unter altem Fenster auf 8 gekappt. Zusätzlich 31 kleinere HD-Nodes (Types bis zu 29 Interps, Authorities, Profiles, Lines, Definitions, PHS) waren noch nicht mit dem Fix neu synthetisiert. Beide Wellen + GeneKeys (Vollständigkeit, geringes Risiko da max. 11 Interps/Node) sind jetzt durch. **Damit ist die komplette bisherige Content-Welle (HD-Kernstruktur + BaZi + GeneKeys) auf dem neuen Selection-Fix, und ein Voll-Audit bestätigt: 0 verlinkte Stub-Interps, 0 hängende Jobs, keine unscoped Full-System-Synths mehr möglich (strukturell durch `IC_TEXT2KG_AUTO_SYNTH=false` verhindert).**

## BaZi — Layer-Reihenfolge

Registry `phase_1a` Klassiker zuerst (nicht Destiny Code zuerst):

1. **Klassiker** 子平真诠 / 滴天髓 / 三命通会 / 渊海子平
2. **Ten Gods** (Power of X …)
3. **Stems/Branches/Jiazi/Nayin**
4. **Structures / Yong Shen**
5. **Da Yun / Timing**
6. **Moderne Überblicke** (Destiny Code ✅ schon gelaufen)

## Andere Systeme (gleiche Logik)


| System     | Struktur-Leitplanke                                              |
| ---------- | ---------------------------------------------------------------- |
| Gene Keys  | Keys/Spectrum → Golden Path → Codon Rings → HD-Brücke            |
| Astro      | Klassik (Ptolemy/Dorotheus) → Tradition (Lilly/Demetra) → Modern |
| Ziwei      | Sterne/Paläste → Klassiker → Modern                              |
| Jyotish    | Graha/Rashi → Nakshatra → Dasha/Yoga                             |
| Ur-Systeme | `literature_canon_by_scope.md` P0 K2_ref vor K3                  |


## Inventar

Quelle: `C:\Users\Admin105\Downloads\Literatur` (219 Dateien)  
CSVs: `literature_*_2026-07-18.csv`