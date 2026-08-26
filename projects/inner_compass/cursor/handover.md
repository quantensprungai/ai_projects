<!--
Reality Block
last_update: 2026-08-26
scope: Chat-Handover Inner Compass (Copy-Paste-Block + Themen-Anhänge)
in_scope: aktueller Chart-Stand, Reboot, Code-Anker, Don'ts, Verweise
out_of_scope: Implementierung; S5-Runbook-Details außer als Archiv unten
-->

# Inner Compass — Handover

> **Neuer Chat:** den Block zwischen den Triple-Backticks kopieren und als **erste Nachricht** einfügen.
> Zusätzlich reicht: „Handover + `reference/hd_bodygraph_overlay_contract.md` lesen, hier weitermachen.“
> Darin stehen Rails, Overlay, Env, Reboot-Reihenfolge, Code-Anker und was nicht tun.

---

## Kontext-Block (kopieren)

```
Projekt: Inner Compass — geburtsbasiertes Meta-System (11 Quellsysteme + Basisstrukturen → 3-Schichten-KG → personalisiertes Handbuch)
Tech: Next.js (Makerkit 3.1.3) + Supabase + Spark (GPU, Worker, MinerU, LLM)
Code: code/inner_compass_app/   Docs: projects/inner_compass/
SoT Chart: projects/inner_compass/reference/hd_bodygraph_overlay_contract.md
SoT State: projects/inner_compass/reference/hd_state_contract.md
Decision: reference/decisions.md 2026-08-17 State-Vertrag + 2026-08-14 Rails
Layer: reference/hd_layer_master_checklist_2026-08-11.md (Delta 2026-08-17)
Synth: cursor/reference/synthesis_canon_first.md
Pipeline-Wörter: cursor/pipeline.md §1a

Gesamtprozess:
  Phase 0 Fundament 100% · Phase 1 Engines ~95% · Phase 2 Content ~75% · Phase 3 Cross-System 0%
  Phase 4 App ~35% — vier Spaces als leere Shell; HD KARTE Graph visuell zu; Overlay-LLM v1o

ROTER FADEN (Stand 2026-08-25; 1–17 bis 08-19, 18 = Chart-Visual):
  1. ✅ S5 E2E + HD Bodygraph-Wellen + HD S0 Close-out
  2. ✅ Chart-UI /home/karte/hd — Geburt → services/hd (Docker :8002) → Bodygraph + Rails + Atom-Wordings
  3. ✅ Overlay v0 LLM — Langdock gpt-5-mini (Typ×Strategie×Autorität + offene Zentren).
       Key nur in apps/web/.env.development.local (nicht committen). URL/Modell in .env.development
  4. ✅ Rails — Design links (rot) / Persönlichkeit rechts. Inspector Gate+Line.
       Line-IDs Engine hd.line.34.1 → KG hd.line.34_1
  5. ✅ Offene Zentren-Lookup (2026-08-14) — Engine schreibt nur *definierte* Center in nodes.
       wordingLookupIds unioniert immer alle 9 hd.center.*. Overlay bekommt Open-Center-Excerpts.
       Inspector zeigt offen/definiert. Nach Reboot einmal neu berechnen, dann Klick auf offenes Zentrum.
  6. ✅ 384er Exalt-Lookup AN (pdftotext). Rails = direkt Planet × Buchzeile.
       18.3 Saturn = neither (Ra). 64keys ▼ = vermutlich Chart-Fixierung
       (Jupiter 18.1 im selben Gate), nicht in die 384er-Tabelle übernehmen.
       Inspector: Linien-Pole vs. diese Aktivierung. Glyphs ▲ / ▼ / Stern. R live.
  7. ✅ Planeten-Nodes — 13 `hd.planet.*` geseedet. Split `planet_split_v1` + Relink `planet_relink_v1b`: **je 1 Träger-primary**. Mix-Reste (Mars+Jupiter, Uranus+Neptune) und Doppel-Absätze → mention. Inspector Accent-C liest essence. Overlay liest Planeten nicht (v1h).
  8. ✅ Overlay v1a/v1b Kanäle+Kreuz; Kanal-Chips; v1c Fixing+R an Schlüssel-Lines
  9. ✅ S0.5 Relink (primary 13 / contrast 30 / mention 14; Heart auf hd.center.heart).
 10. ✅ State-Vertrag 2026-08-17 + Packer P1: Inspector-Stapel nach Display-Policy; Overlay Block 2 = undefined-Center-Priorslots.
       Overlay-Cache v1f (`user_charts.overlay`, undefined-first + Center-C quality). Profil in Satz 1. Concept-Node P2 Skript.
 11. ✅ S0 Defined-C Relink v2 (Qualität): Quellen **Winn + Schoeber**; PHS/andere demoted. Will Center → Heart (1 Defined-C). Identity+Will Mix nicht mehr am G. S0.5-Solarplexus: Welle/Authority = `gift` (nur defined SP); open emotional bleibt Shadow.
       Overlay-Cache `hd_overlay_v1n`. Mechanical-Atom: Read-time-Split nach defined/undefined (kein Wipe). Sakral-Zyklus am Defined-Satz; SP Cue-Split. Heart-Tor-Inventar nicht im Center-Atom. S0.5 Hint = nur dieser Slot.
 12. ✅ Stream F Channel-C Relink v1c (`ic_s0_channel_facet_relink.py`): `primary` + gift/shadow an **36/36**. Logic (63/4), Brainwave (20–57), Concentration (9–52) aus Circuitry. Type-unnamed skip. Type 4 = Transit, ungelesen. Inspector: Atom + Achse A. Overlay-Cache jetzt `hd_overlay_v1n`.
 13. ✅ Ego-Authority + Quadruple Relink (Four Views; HA2 ohne Authority-Essays). `ic_hd_authority_definition_relink.py --only` **ohne Synth**. ego_manifested/projected/self_projected haben wieder Primaries; quadruple Four-Views-Essays.
 14. ✅ KARTE Register-IA (2026-08-18): Inspector = 5 Register **Zentren · Kanäle · Tore · Betriebssystem · Zusammenschau**. Default nach Berechnung = Zentren (alle 9, definierte zuerst, Akkordeon), Overlay-Absatz ist das **letzte** Register — Lookup vor LLM. Kanäle-Register listet alle definierten Kanäle + hängende Tore (aktiviert, Gegentor fehlt; deterministisch aus `chart.channels`). Chips bleiben Navigation, Register tragen den Inhalt. Trap unter dem Namen des Slots (secondary), nicht als eigene Sicht. Frequenz-Hinweis einmal pro Pane, nicht pro Zentrum. OS-Zeile mit Feldnamen (Typ/Strategie/Autorität/Profil/Definition/Kreuz) statt kontextloser Chips; Definition kommt aus `chart.nodes`, **nicht** in `headlines` (sonst Overlay-Hash-Miss). Geburtsformular klappt nach der ersten Berechnung weg (bis Onboarding steht).
 15. ✅ **Mapping Instanz → Def + Register „Körper"** (2026-08-18): neu `apps/web/lib/hd/hd-phs.ts` (`hd_variable_mapping_v1`): Pfeilposition = Primärschlüssel, `colorDefId/toneDefId/baseDefId`, 21 Def-IDs (`HD_PHS_DEF_CANONICAL_IDS`) immer im `wordingLookupIds`. `normalize-hd-chart.ts` reicht jetzt `color/tone/base` je Aktivierung **und** `variable` (vier Pfeile mit direction/aspect/defId) durch — beide Engine-Formen (`variable.<key>` des Adapters und `variable.arrows[]` der README) werden auf die Position gemappt.
       DB-Stand geprüft: **6 color_def · 6 tone_def · 5 base_def · 4 variable_def, alle mit Wording**; Engine-Kombi-IDs (`hd.color.48.3.2`) haben **0 Nodes** — genau die Lücke, kein Literatur-Thema.
       Engine-Ground-Truth (Dachau, `:8002`): `raw.variable = {digestion|environment|motivation|perspective: {value,name,aspect,def_type}, arrow_string "<<<>", short_code "PLR DLL"}`. Kurzcode/Pfeil-String = Engine-Label, **kein UI** (vier Ecken + Color.Tone reichen). Register Körper zeigt vier Pfeile (gleiche Chevron-Glyphe wie am Graph) + PHS-Tiefe **beider Sonnen**; Tore-Register zeigt Color/Tone/Base der gewählten Aktivierung.
       Fußnote: `services/hd/src/hd_compute.py` (Fallback ohne dturkuler) benennt Perspective/Motivation anders als der Adapter. Live-Pfad ist der Adapter; deshalb mappt die UI über die **Position**, nicht über Engine-Schlüsselnamen.
       ⚠️ **Befund PHS-Achsen:** die 6/6/5 Def-Nodes sind nicht achsengebunden — aufgelöst in 16.

 16. ✅ **PHS-Achsen + Viertel geseedet, Register Fakten (2026-08-19).** Befund aus 15 aufgelöst: `hd.color_def.*` ist laut `hd_catalog_v0.json` die **Motivations**-Skala (Fear…Innocence) — die UI hat sie fälschlich für alle vier Pfeile gelesen. Achsen jetzt eigenständig, Skalennamen **aus der Literatur belegt** (`ic_hd_axis_discover.py --headings --axis-names`):
       Determination 1-6 Appetite·Taste·Thirst·Touch·Sound·Light (q2/q3, TOC „3rd Color: Thirst", „Light: 6th Color Design") · Cognition 1-6 Smell·Taste·Outer/Inner Vision·Feeling·Touch (q2/q3, „The 1st Tone: Smell"…) · Perspective 1-6 Survival·Possibility·Power·Wanting·Probability·Personal (q6-q8, „1st Color Node: Survival", „Nodal View 4: Wanting") · Motivation 1-6 Fear·Hope·Desire·Need·Guilt·Innocence (Katalog; Zahl+Name belegt für 1/2/4/6).
       **Positionen ebenfalls aus der Literatur:** Motivation = Personality **Sun** („both 2nd Color hope for their Personality Sun/Earth", q8), Perspective = Personality **Nodes** („The Core of Seeing is in the Personality Nodes", q6), Determination/Cognition = Design **Sun**, Environment = Design **Node** (bottom_left). Pfeilrichtung kommt vom **Tone** (Katalog `variables[].source`, Adapter-Kommentar), der Achsenwert von der **Color**.
       Seed `ic_seed_hd_axes_quarters.py` (`hd_phs_axis_quarter_v1`): 30 Achsen-Nodes + 4 `hd.quarter.*` (Themen aus q9: Purpose Fulfilled through Mind/Form/Bonding/Transformation, je 16 Gates in `metadata.gates`). Relink `ic_hd_axis_quarter_relink.py` (`axis_quarter_link_mode=axis_quarter_relink_v1`, TOC→mention, 3+ Zahlen→contrast, Primary-Cap 6): 28 Nodes, 4-6 Primaries je Node.
       ⚠️ **`hd.environment.1-6` bewusst ohne Relink:** die sechs Ortsnamen (Caves/Markets/…) stehen **nicht** im Korpus, und q4/q5 („Lunar & Planetary Color") tragen mehrere Achsen — dort steht „6th Color: Innocence", also Motivation. Treffer „3rd Color" nahe „environment" belegt die Achse nicht. Nodes sind Struktur, Text fehlt bis eine Environment-Quelle da ist.
       ⚠️ **`hd.color_def.*` = Legacy** (`superseded_by hd.motivation.N`): die Wordings sind selbst achsen-vermischt — `color_def.2` erklärt *Taste* (Determination), nicht *Hope*. Deshalb hat Motivation eigene Nodes statt zu erben. `hd.base_def.*`: Katalog trug fälschlich Linien-Keynotes; **nur Base 2 = Evolution** belegt (PHS q3 „The 2nd Base: Evolution"). 1/3/4/5 ohne Namen, Wordings der alten Atome nicht gewischt.
       **`hd.line_def.1-6` existierten schon** (59-95 Interps, alle 6 mit Wording) — kein Seed nötig, nur Lookup. Register **Fakten** ist live: Persönlichkeits-Sonne-Viertel + Design-Sonne-Viertel, Verteilung mit ausgeschriebenem „Design / Persönlichkeit". Linien-Zählung 1-6 (Dachau: Mutation über Tor 14, Design-Sonne Dualität Tor 29).
       **Wordings (Langdock gpt-5-mini, 2026-08-19):** 28/28 Nodes mit Literatur synthetisiert (4 Quarter + 6 Determination + 6 Cognition + 6 Motivation + 6 Perspective). Environment 1-6 ohne Literatur, daher kein Synth. Aufruf: `python ic_run_with_langdock.py ic_k2_synth_batch.py --system hd --only-id … --force`.
       **Figma:** https://www.figma.com/design/6KCXRVzu39tqEjpr66hGwc — Starter **3 Seiten**. 00 Contract · 01 Tokens & Geometry · 06 Captures. Geometry v0 als Frame rechts auf 01 (`Bodygraph Geometry v0`, x=1600): 9 Zentren + 64 Tore + 36 Kanäle, `visible`/`label`/`hit_area`, Katalog-IDs. Kein Page-03 (Plan-Limit). Captures: `6:2` aktuell, `2:2` älter. Dump nicht putzen. Vertrag `cursor/reference/figma_karte_contract.md`.
  17. ✅ Overlay-Policy (2026-08-19): Zusammenschau ist **eng aus Produktregel** (eine Lesung, kein zweiter Inspector), nicht weil gpt-5-mini Quota/Tokens nicht reicht. v1l hat bereits 16k Completion-Cap. Constraint = Admission. Live = **v1o** (optionaler Fakten-Satz aus `hd-facts.ts`; Pol-Absatz je fixiertem Schlüssel-Pol aus I’Ching-Chunks; LLM klebt Zahlen, schreibt Viertel-/Linien-Atome nicht um). SoT: Overlay-Vertrag §5.0. PHS-Labels höchstens später Facts, keine Overlay-Essays (§5.1).
       ⚠️ **Environment-Hub** (Höhle / Markt / Küche / Berg / Täler / Ufer): Labels sind thick enough, Atome too thin — **nicht** in KG kopieren. `hd.environment.1-6` bleibt Struktur ohne Relink/Synth.
 18. ✅ **Chart-Visual (2026-08-24/25).** Geometrie live in `hd-bodygraph-geometry.ts` (Backup `cursor/reference/geometry-backup-2026-08-24/`). Wahrnehmungsregeln: `cursor/reference/figma_karte_contract.md` §4b.
       Zentren: Jovian-Füllung wenn definiert, **hell genug für einheitliche dunkle Schrift** (Kopf/G Gold `#E0B84E`, Ajna `#6FB8A6`, Kehle/Milz/Solar/Wurzel Sand `#C4A07C`, Sakral `#E85C4A`, Herz `#E07A72`) — kein Bordeaux, keine weiße Schrift auf dunklem Fill. Undefined = opakes Background + `fill-foreground` (Dark-Theme). Design/Persönlichkeit **nicht** auf die Form — Rails + Kanalhälften. Hanging = Mitte *dieses* Pfads. Integration 10–20–34–57 = sechs Pfade (einen Tick dünner, weil Überlappung). Übrige Kanäle dicker; beide Seiten aktiv = extra dick. Selection = dickere Füllfarbe, kein Gold-Halo. Tore = Zahl ohne Chip (hue-Chips und Papier-Chips verworfen). Rails: Header fett bei Selection, Polarität|Zahl|R.
       64keys malt Zentren XOR blau/orange, nie gestreift. Tie-Break unbelegt → nicht malen.
       ✅ **Vier Pfeile am Graph** (2026-08-25): runder Chevron + Color mit Tone-Tiefzahl neben dem Kopf. Design links, Persönlichkeit rechts. Mapping `collectVariableMarkers`. Klick → Register Körper (Color-Achse). Die fünf PHS-Achsen in Körper sind die *Zahlen* derselben vier Ecken; Cognition teilt den oberen linken Pfeil (Tone der Design-Sonne), kein fünfter Chevron. Color/Tone neben den Planeten = Toggle (Default aus). Overlay v1o. Chart-State: SessionStorage + GET. Inspector Tore: zwei Extreme der Linie (keine Quelltitel/IDs in der UI). KARTE spricht **Handbuch**, nicht Pipeline.

**Quadranten / Linien-Statistik:** Gate→Viertel aus `hd_crosses_extracted.json` (16/16/16/16). `hd.quarter.*` geseedet + gewordet (16). Generische Rollen lagen schon als `hd.line_def.1–6` vor (nicht `hd.line.1`). Register Fakten zählt, Atome bleiben generisch.

Wörterbuch Chunk/Interp/Anhang/Synth/primary: cursor/pipeline.md §1a.

Aktueller Punkt: **App-Shell** (2026-08-26). HD-KARTE Graph freeze bleibt. Vier Spaces als leere Rahmen: JETZT `/home` · KARTE `/home/karte` · WERKSTATT `/home/werkstatt` · ZEIT `/home/zeit`. HD = `/home/karte/hd`. Onboarding `/home/onboarding` (Formular live; Begleiter-Feld `data-ic-entry=companion` leer). Locale-Modell fest. **Sprache/i18n jetzt nicht bauen.**

Nächstes Paket (Reihenfolge, nicht parallel):
  Shell) Spaces + Onboarding füllen, sobald eine Fläche Inhalt braucht. Kein hartes Gate.
  KARTE) Freeze halten. Graph-Labels nicht nach next-intl ziehen.
  Locale) Nicht jetzt.
  Dynamik) Atom-Prozess liegt; System-Dynamik (`sys_dynamics` intra) und Cross-Dynamik **nicht** jetzt. Relink-Q still, nach UI-Mix.
  Agent) Nicht bauen. Nur das Companion-Feld freihalten.
  Git) Commit+push nur auf expliziten User-Wunsch.
  Makerkit) v4 = eigenes späteres Paket.
  KARTE-nicht) 64keys Blau/Orange am Zentrum — erst wenn ein Chart den Mischfall belegt.

Nicht: Full-Re-Synth, Center-Wipe, `open` als dritte Enum, SGLang über 7973 Interps / 20877 Anhänge.
Sources: S0.5 `37170478-…` / `cf923ac4-…`. S0 Defined: `ic_s0_center_defined_relink.py`. Channel: `ic_s0_channel_facet_relink.py` (`channel_relink_v1c`; Life Force `2a9272bc-…`). Planeten-Source `7e52cc9a-…`. Auth/Def: Four Views `c3135579-…` (HA2 `5517ac0c-…` Diagnostics, 0 Ego/Quad-Hits).

NACH REBOOT (Reihenfolge):
  1. Docker Desktop
  2. Makerkit/Supabase (kit_dev). Login test@makerkit.dev / testingpassword
  3. HD-Service ist NICHT in der Makerkit-Compose (GPL-Isolation) — eigener Stack:
       cd code/inner_compass_app/services/hd
       docker compose up -d
     Health: http://127.0.0.1:8002/health
     Nach einmaligem `up -d` startet Docker Desktop ihn neu (`restart: unless-stopped`).
  4. Next aus code/inner_compass_app:
       pnpm --filter web exec next dev --port 3000
     Env: apps/web/.env.development + .env.development.local
     HD_SERVICE_URL=http://127.0.0.1:8002
     5. http://localhost:3000/home/karte/hd — letzter Chart lädt von allein (GET). Overlay-Cache v1o miss beim ersten Mal. Mechanik am Center nur noch dieser State.

CODE:
  apps/web/app/[locale]/home/_components/hd-karte/
  apps/web/lib/hd/hd-wording-lookup.ts   (immer 9 hd.center.*)
  apps/web/lib/hd/hd-line-polarity.ts + hd-line-polarity.json
  apps/web/lib/hd/hd-line-facets.ts
  apps/web/lib/hd/hd-line-fixing.ts
  apps/web/scripts/ic_hd_line_polarity_from_pdftotext.py
  apps/web/lib/hd/normalize-hd-chart.ts
  apps/web/lib/hd/hd-planets.ts
  apps/web/lib/hd/hd-center-facets.ts
  apps/web/lib/hd/hd-channel-facets.ts
  apps/web/lib/hd/hd-overlay.ts
  apps/web/lib/hd/hd-overlay-cache.ts
  apps/web/lib/hd/hd-phs.ts
  apps/web/lib/hd/hd-facts.ts
  apps/web/lib/hd/hd-chart-assemble.ts
  apps/web/lib/hd/hd-karte-session.ts
  apps/web/lib/hd/hd-bodygraph-geometry.ts
  apps/web/lib/hd/hd-bodygraph-path.ts
  apps/web/lib/hd/hd-karte-palette.ts
  cursor/reference/figma_karte_contract.md
  apps/web/lib/ic/ic-spaces.ts
  apps/web/app/[locale]/home/_components/ic-spaces/
  apps/web/scripts/ic_s05_center_facet_relink.py
  apps/web/scripts/ic_s0_center_defined_relink.py
  apps/web/scripts/ic_s0_channel_facet_relink.py
  apps/web/scripts/ic_hd_authority_definition_relink.py
  apps/web/scripts/ic_seed_hd_planets.py
  apps/web/scripts/ic_s0_planet_relink.py  (--tighten-carriers v1b; --demote-examples)
  apps/web/scripts/ic_s0_planet_reinterpret.py  (planet_split_v1, nosynth)
  apps/web/scripts/ic_start_langdock_worker.py
  apps/web/scripts/ic_s05_open_center_concept.py
  apps/web/app/api/ic/hd-chart/route.ts
  services/hd/src/hd_compute.py

NICHT TUN:
  supabase db reset (KG nur lokal; Dump Desktop 2026-08-13)
  Mandala-SVG / volle Space-Inhalte (Shell ist da)
  Schul-Ingest / tradition-Pipeline / Center-Wipe
  Planet-Gewichte erfinden
  hd.not_self_mind.* seeden
  64keys/Gene Keys Massen-Rename
  64keys-Blau/Orange auf Zentren raten; Streifenfüllung auf Zentren
  Gate-Chips am Bodygraph (hue-gematcht oder Papier) — ausprobiert, verworfen
  Figma-MCP-Reads (Quota); Geometrie nicht aus Figma flachziehen
  open als dritten Center-State persistieren
  Makerkit v4 in diesem Slice (eigenes späteres Paket; bleibt 3.1.3)
  SGLang über alle Interps/Anhänge (Stream Q ist Regeln + Stichprobe, nicht 8k)

KG nur lokal. HD-Schulen nicht ingest vor tradition-Feld.
```

---

## Phase-1-Hintergrund (nicht in den Copy-Paste-Block)

Engine-Staffel, Kits, K1–K4, Sidereal/Hybrid — nur lesen, wenn der Chat über Engines geht (Abschnitt unten). Kurz:

- Hybrid TS-first: `@ic/engines` + Python-Microservices HD (`:8002`) und Jyotish
- HD-Ephemeris: Swiss Ephemeris, tropical Standard. Sidereal/Hybrid = Spec, nicht gebaut
- Schema: `sys_*` + `user_*`; Canonical IDs `{system}.{type}.{id}` z. B. `hd.gate.34`
- MCP: Makerkit Kit MCP (lokal), Supabase MCP (Cloud), Config `.cursor/mcp.json`

---

## Human Design — Schulen / Gate-Stimmen (`tradition`)

```
Kurz (decisions.md 2026-08-13 + engines.md §6.7b):
- Ein hd.*-Baum. Linsen = tradition auf K3, keine parallelen KGs.
- jovian = S0-Default (Ra). 64keys-Gates = Blue I Ching (Ebhart). cosmic_sidereal = Cosmic Way = 64-Gate-Prosa sideral (keine Engine).
- Schoeber-Person = 64keys-Orbit; *The Centres* = HD-geschrieben → bleibt in Center-Wordings (jovian + teacher schoeber). Kein Re-Synth.
- Klassisches I Ging (Wilhelm/…) = i_ching.* (Ur-System), nicht HD-Schule.
- Jetzt nicht: Schul-Ingest, tradition-Pipeline, Center-Wipe.
```

## Human Design — Rechenmodi (tropical / sidereal / hybrid)

```
Kurz:
- system_id bleibt immer `hd` — Unterschiede stecken in compute_profile.hd (cursor/contracts.md §13).
- Swiss Ephemeris ist im HD-Service SCHON angebunden (pyswisseph im vendored dturkuler); Standardmodus = tropical (Jovian-kompatibel).
- Sidereal-Flag + Ayanamsha sowie Hybrid (Design tropisch / Persönlichkeit sidereal) sind SPEC + Roadmap, NICHT implementiert.
  → reference/hd_compute_profiles_kg_and_roadmap.md · decisions.md 2026-05-06

Wenn ihr das BAUEN wollt — Startreihenfolge:
1) Governance: Default-Ayanamsha (wenn sidereal), Verhalten des Design-Datums (−88°) bei full sidereal festlegen.
2) API: BirthData + compute_profile.hd in services/hd (FastAPI) und @ic/engines hd-client-Typen spiegeln.
3) Engine: vendored humandesign_api …/core.py — calc_ut mit Sidereal-Mode parametrisieren ODER zwei Läufe + Merge (Hybrid).
4) Tests: feste Geburtszeit → erwartete Gates (Regression gegen Jovian tropical bleibt Pflicht-Fixture).
5) App: Chart-Snapshot persistiert compute_profile; UI-Label; keine stillen Cross-Modus-Vergleiche.
```

## Wenn der Chat über ENGINES geht

```
Zusätzlich lesen:
- cursor/engines.md (K1-K4 Framework, Kit-Kandidaten mit Lizenzen, Prüf-Checkliste, Architektur)
- code/inner_compass_app/packages/engines/README.md (TS-Engines, npm-basiert)
- code/inner_compass_app/services/jyotish/README.md (Python-Microservice, AGPL-isoliert)
- code/inner_compass_app/services/hd/README.md (Python-HD, GPL-isoliert, Docker :8002)
- kern/IC_System_Pruef_Framework.docx (Originalquelle K1-K4 + Evidenzklassen)
- reference/hd_kit_structure_extraction.md (HD-Kit-Analyse, was fehlt)
- **EarthStar Human Design** = IC-Produktname für Hybrid (`hybrid_design_tropical_personality_sidereal`); UI-Spez Stufe 1/2 → `reference/hd_compute_profiles_kg_and_roadmap.md` §6.1
- reference/structure_descriptor_seed.md (Deskriptor vs. Seed vs. Structure Klarstellung)
- cursor/contracts.md §13 (compute_profile für hd)

Wichtige Entscheidungen:
- PyJHora (AGPL): BEHALTEN als isolierter Microservice (Code open-sourced, App privat)
- Ziwei Doushu: iztro (MIT, TS) — größter Kit-Fund
- BaZi: @yhjs/bazi (MIT, TS) ersetzt alvamind
- Westl. Astro: **celestine** (MIT, in `@ic/engines`)
- node-jhora: PROPRIETÄR, NICHT nutzbar (trotz GitHub)
- IC-Sprache: emergiert aus Konvergenz-Klumpen im KG, NICHT vorausgesetzte Hierarchie (architecture.md §15)
```

## Wenn der Chat über ARCHITEKTUR geht

```
Zusätzlich lesen:
- cursor/architecture.md (Schema, Datenschichten, Tech Stack, §12-14 NEU, §15 KG-Übereinanderlegen & IC-Sprache NEU)
- cursor/contracts.md (Dimensions-Contract, Payloads, Enums, §10-13 NEU)
- reference/structure_descriptor_seed.md (Deskriptor vs. Seed vs. Structure)
```

## Wenn der Chat über PIPELINE geht

```
Zusätzlich lesen:
- cursor/pipeline.md (Jobs, Flows, Prompts, §10-12 NEU)
- Worker-Specs in cursor/pipeline.md §7
- Infra: infrastructure/spark/ (MinerU, LLM-Serving)
```

## Wenn der Chat über PRODUKT/DESIGN geht

```
Zusätzlich lesen:
- consolidation/ic_gesamtinventur.md (Gesamtinventur + Scope v1/v2/v3)
- consolidation/z2_user_journey.md (User-Journey, ACHTUNG: v0.1, App-Spaces fehlen noch)
- reference/prd_v3.md (vollständiges PRD)
- reference/decisions.md (alle Design-Entscheidungen)
- reference/gesamtbetrachtung_review_2026-07.md (Konzept-Review: Genealogie-Gap, Phasen-Detection,
  Resonanz-Feedback-Loop, Content-Ökonomie, UX-Empfehlungen — offener Review)
- reference/ux_konzept_2026-07.md (UX-Deep-Dive v1: IA, Onboarding, Mandala, WERKSTATT-Ritual,
  Konvergenz-UX, Freemium, MVP-Schnitt)
```

## Wenn der Chat über DB/SCHEMA geht

```
MCP-Tools nutzen (automatisch verfügbar in Cursor):
- Makerkit Kit MCP: get_schema_files, get_database_summary, get_table_info, create_migration, diff_migrations
- Supabase MCP: Direkte SQL-Queries gegen Cloud-DB
- Voraussetzung für lokale DB-Tools: supabase start (Port 54322)

Zusätzlich lesen:
- cursor/architecture.md (Schema, sys_*-Tabellen, Datenschichten)
- cursor/contracts.md (Enums, Dimensions, Payloads)
- code/inner_compass_app/apps/web/supabase/schemas/ (deklarative Schema-Dateien)
```

---

## S5 E2E — VM105 (Stand 2026-07-02)

> **Ziel:** 1 HD-PDF → Supabase Upload → Spark Worker → Chunks → Interpretationen → text2kg → synthesize_node.  
> **Nicht:** alle 216 Literatur-Dateien — nur **1 Test-PDF**.

### Session-Stand 2026-07-03 (S5b ✅)

| Item | Wert |
|------|------|
| Account | `5deaa894-2094-4da3-b4fd-1fada0809d1c` |
| Source (S5-PDF) | `3c7c0a7b-9dd1-41b1-ac47-c0cd26dedbe5` — *Complete Rave I'Ching* |
| **S5a Pipeline E2E** | ✅ **done** (2026-07-02) |
| **S5b Extract** | ✅ 65 Chunks, 64 unique `gate_number` (MinerU pipeline, `IC_CHUNK_PROFILE=rave_iching_gates`) |
| **S5b Phase 2** | ✅ classify, term_mapping, interpretations, text2kg, synthesize |
| **S5b Synthesis** | ✅ **64/64** echte Gate-Wortings (Gate 63 via `only_canonical_ids` + JSON-Fix) |
| Chunk-Profil | `ic_chunk_profiles.py` → `rave_iching_gates` (Code-Repo + Spark) |
| Spark Worker-Start | `spark_s5b_synth.sh` (pkill + `set -a` `.env.vm105`) — **immer** VM105-URL exportieren |
| Spark LLM | `qwen3-32b-nvfp4` :30001 · `IC_LLM_SYNTHESIS_TIMEOUT=300` |
| Supabase VM105 | `http://100.70.238.41:54321` (Tailscale) · Key via `pnpm exec supabase status` |

**Skripte:** `ic_s5b_rerun.py` · `ic_s5b_gate63_synthesis.py` · `ic_s5_spark_synthesis_prep.py` · `spark_s5b_extract.sh` · `spark_s5b_synth.sh`

**Verify:**

```sql
select count(*) filter (where not canonical_description like '[DRY-RUN]%') as real,
       count(*) filter (where canonical_description like '[DRY-RUN]%') as stub
from sys_synthesis_wordings
where account_id = '5deaa894-2094-4da3-b4fd-1fada0809d1c'
  and canonical_id like 'hd.gate.%';
-- Ziel: real=64, stub=0
```

### Session-Stand 2026-07-02 (S5a, historisch)

| Item | Wert |
|------|------|
| **S5a Pipeline E2E** | ✅ **done** (2026-07-02): text2kg, synthesize 47/47 echt, Job completed |
| **S5b Chunk 64/64** | ~~offen~~ → ✅ erledigt 2026-07-03 |

**Spark synthesize (Copy-Paste):**

```bash
ssh -p 2222 sparkuser@100.96.115.1
cd ~/srv/hd-worker
export SUPABASE_URL=http://100.70.238.41:54321
export SUPABASE_SERVICE_ROLE_KEY=<von VM105 supabase status>
export IC_LLM_URL=http://127.0.0.1:30001
export IC_LLM_MODEL=qwen3-32b-nvfp4
export IC_LLM_SYNTHESIS_TIMEOUT=300
export IC_WORKER_JOB_TYPES=synthesize_node
.venv/bin/python -u ic_worker.py --once   # oder --loop --sleep 5
tail -f logs/s5_synthesize.log
```

**Erfolg:** 47/47 Gate-Wortings **ohne** `[DRY-RUN]`-Prefix; Job `completed`.

---
### Repo & Branch

| | |
|---|---|
| Docs | `C:\Users\Admin105\ai_projects` *(Unterstrich, nicht `ai-projects`)* |
| Code | `C:\Users\Admin105\ai_projects\code\inner_compass_app` |
| Branch | `cursor/inner-compass-alignment-reconcile-spark-handover` |
| Stand | `d59faee` — Literatur-CSVs 2026-06-30, Ra-Katalog, Cross-System-Methodik |

```powershell
cd C:\Users\Admin105\ai_projects
git fetch; git checkout cursor/inner-compass-alignment-reconcile-spark-handover; git pull
```

### Kontext

- Phase 1 Engines ~95 % · Phase 2 Pipeline **0 %** — **S5 = nächster Meilenstein**
- Literatur-SoT: he5013/Nextcloud (216 Dateien); VM105 Teilbestand unter `Downloads\Literatur`
- MinerU-Spike abgeschlossen (MinerU > Unlimited-OCR); Worker-Env: **`IC_USE_MINERU=true`**
- Test-PDF: `Downloads\Literatur\hd\` — *Complete Rave I'Ching* (MD5 `9daaa92…` in `hd/`, nicht `archiv/`)
- MinerU-Referenz: `reference/mineru_complete_rave_iching_20p_result.md`
- Spark hat bereits `~/sample_complete_rave_iching.pdf` (OCR-Spike)

### Doku

- `reference/s5_runbook.md` — Haupt-Runbook
- `cursor/pipeline.md` — Job-Kette
- `infrastructure/spark/HD_WORKER_HANDOVER.md` — Spark/MinerU (`sys_*`, nicht `hd_*`)
- `reference/aa_ic_toolkit_alignment.md` — Uploader `--sys-mode`

### Topologie

| Komponente | Host | Tailscale |
|---|---|---|
| Supabase lokal | VM105 | `100.70.238.41` |
| Worker + MinerU | Spark `spark-56d0` | `100.96.115.1` |
| AA-Downloads | VM102 | — |

**Worker auf Spark:** `SUPABASE_URL=http://100.70.238.41:54321` (nicht `localhost`).

### Schritte A–C (Phase 1 nur MinerU)

**A) VM105 — Supabase**

```powershell
cd C:\Users\Admin105\ai_projects\code\inner_compass_app
pnpm run supabase:web:start
# ggf. pnpm exec supabase start --ignore-health-check
# Optional Seed: cd apps\web; python scripts\ic_seed_structure.py
```

**B) VM105 — PDF + Job**

Uploader (Toolkit + `.env` mit `SERVICE_ROLE_KEY`, `ACCOUNT_ID=5deaa894-…`):

```powershell
python src/hd_saas_uploader.py --upload-pdfs "C:\Users\Admin105\Downloads\Literatur\hd\<Complete_Rave>.pdf" --max-pdfs 1 --sys-mode
```

Oder Studio + SQL laut `s5_runbook.md` Option B.

**C) Spark — nur `extract_text`**

```bash
# SGLang stoppen; dann:
export SUPABASE_URL="http://100.70.238.41:54321"
export SUPABASE_SERVICE_ROLE_KEY="<supabase status auf VM105>"
export IC_USE_MINERU=true
export IC_MINERU_LANG=latin
export IC_WORKER_JOB_TYPES=extract_text
~/srv/hd-worker/.venv/bin/python3 ~/ai_projects/code/inner_compass_app/apps/web/scripts/ic_worker.py --loop --sleep 5
```

(Pfad Worker/venv auf Spark ggf. anpassen — siehe `HD_WORKER_HANDOVER.md`.)

### Validierung

```sql
select count(*) from sys_source_chunks where source_id = '<SOURCE_ID>';
select status, job_type, debug from sys_ingestion_jobs order by created_at desc limit 5;
```

**Erfolg Phase 1:** `sys_source_chunks > 0`, sinnvolle Gate-Texte, kein leerer OCR-Fallback.

### Phase 2 — LLM + text2kg (Stand 2026-07-01)

**Voraussetzung:** Seed gelaufen (`python scripts/ic_seed_structure.py`) — sonst legt text2kg asset_chunk-Nodes an.

| Schritt | Env / Aktion |
|---------|----------------|
| Chunk-Profil | `IC_CHUNK_PROFILE=rave_iching_gates` (Gate-Chunks mit `gate_number` in Metadata) |
| LLM-Phase | `IC_WORKER_JOB_TYPES` ohne Filter; `IC_LLM_URL` auf Spark |
| text2kg | Linkt Interpretationen → `hd.gate.{N}` via Chunk-Metadata (nicht asset_chunk) |
| synthesize | Priorisiert Nodes **mit** `interpretation_ids`; Timeout: **`IC_LLM_SYNTHESIS_TIMEOUT`** (Default 240s) |

**Verifikation nach Phase 2:**

```sql
-- Keine asset_chunk-Nodes für Gates (sollte 0 sein wenn Seed + Fix aktiv)
select node_key from sys_kg_nodes
where system = 'hd' and node_key like 'hd.asset_chunk.%' limit 5;

-- Gate-Nodes mit Interpretationen
select node_key, metadata->'interpretation_ids' as interps
from sys_kg_nodes
where node_key like 'hd.gate.%' and metadata ? 'interpretation_ids'
limit 5;
```

**S5-Ablauf (empfohlen):**

1. **Testlauf** — 1 PDF, Pipeline E2E (Phase 1 Chunking + Phase 2 LLM/text2kg)
2. **Verifikation** — SQL oben; Stichprobe Gate 1/7
3. **DB-Cleanup** — Test-Artefakte löschen (`hd.asset_chunk.*`, Duplikat-Jobs, alte Interpretationen des Test-Source); **Seed-Nodes behalten** oder Seed neu
4. **Sauberer Lauf** — optional `supabase db reset` + Seed + Pipeline nochmal (nach Seed-Erweiterung sinnvoll)

Nicht „alles wegwerfen“: Schema + Katalog-JSONs + Code bleiben; nur **account-spezifische Ingest-Daten** aus dem Test.

### DB-Naming (sys_* vs. hd.*)

| Ebene | Alt (HD-App) | Jetzt (Inner Compass) |
|-------|--------------|------------------------|
| Tabellen | `hd_kg_*`, `hd_*` | **`sys_*`** (`sys_kg_nodes`, `sys_interpretations`, …) |
| Helper-Schema | `hd` | **`ic`** |
| System-Spalte | — | `system = 'hd'` \| `'bazi'` \| … (Quellsystem, nicht Tabellenname) |
| Canonical ID | — | **`hd.gate.34`** — `hd.` = Namespace des Quellsystems, **nicht** Tabellenpräfix |

Legacy-Pfad `code/hd_saas_app/` existiert parallel; **aktive Pipeline:** `code/inner_compass_app/`.

### 69.120 Kombinationen — vollständig ohne 69k Nodes?

**Nein.** 64 Gates × 6 Lines × 6 Colors × 6 Tones × 5 Bases ≈ **69.120** berechenbare Positionen pro Aktivierung — das sind **Chart-Ergebnisse** (K1), keine Struktur-Nodes.

**Strukturbaum (K2)** enthält **atomare** Bedeutungs-Nodes (~700–780 für HD):
- 64 Gates, 384 Lines (gate-spezifisch im Seed), 36 Channels, 9 Centers, …
- **17 PHS-Nodes** (6 Color + 6 Tone + 5 Base — global, nicht pro Gate)
- 192 Incarnation Crosses, 4 Variables, …

Kombinationen entstehen zur **Laufzeit**: Engine liefert Position → App/LLM kombiniert Bedeutungen der atomaren Nodes. Details: `reference/hd_structure_13_layers_and_engines.md`, `reference/deep_structure_plan.md` §PHS.

**Vollständig für K2** = alle 13 Layer als atomare Nodes geseedet — **nicht** 69k Einzel-Nodes. **Stand 2026-07-02:** PHS (17), Variables (4), Crosses (192), Strategy/NotSelf/Signature + Catalog-Circuits aus JSON geseedet; Layer 1–4 + 9 + 13 abgedeckt.

### K1/K2 vs. K4 (Kurz)

- **K1/K2:** Struktur/Seed aus Engines + `ic_seed_structure.py` — Graph **vor** PDFs.
- **K4:** PDF-Text → `sys_interpretations` → text2kg **PATCH** auf Seed-Nodes.
- **Wellen-Modell:** Struktur **pro System** seeden (HD zuerst), nicht alle 14 gleichzeitig.
- **gate_number → hd.gate.N:** HD-first in `_resolve_canonical_id_from_interp`, erweiterbar für andere Systeme via Chunk-Metadata.
- **Cross-System:** Synthese für UI; Roh-Interpretationen für Phase 3 — Review `reference/cross_system_mapping*.md`.

### Seed-Verifikation HD (2026-07-02)

| Check | Ergebnis |
|-------|----------|
| 64 Gates `hd.gate.1`–`64` vs. `hd_catalog_v0.json` | ✅ PASS |
| Center-Zuordnung Seed vs. Katalog | ✅ PASS (0 Mismatches) |
| 36 Channels | ✅ PASS |
| 17 PHS (`hd.color.1`–`6`, `hd.tone.1`–`6`, `hd.base.1`–`5`) | ✅ PASS — aus `hd_catalog_v0.json` |
| 4 Variables (`hd.variable.digestion` … `perspective`) | ✅ PASS |
| 192 Incarnation Crosses (`hd.incarnation_cross.*`) | ✅ PASS — aus `hd_crosses_extracted.json` |
| Type→Strategy/NotSelf/Signature + Channel→Circuit | ✅ PASS — 115 Edges aus `hd_structure_v0.json` |
| Offene Gaps vs. Katalog/Structure | ⚠️ Awareness Streams (8), Cross→Gate-Edges, PHS-Hierarchie (Line→Color→Tone→Base), Legacy-Circuit-Keys (`individual`/`tribal`/`collective` vs. Katalog-Subcircuits) |

### Rückmeldung an he5013

Upload-Methode · Chunk-Count · 1–2 Textbeispiele · Job-`debug` bei Fehler · ob Phase 2 (LLM) starten.

---

Wenn du einen **frischen Chat** für die HD-Karte willst: oben den **Kontext-Block** einfügen und darunter:

```
Handover + reference/hd_bodygraph_overlay_contract.md lesen, hier weitermachen.
```

Nicht bei Slice 1 von vorn. Nächster Schritt: pdftotext -layout der Complete Rave I'Ching → volle 384er-Tabelle, oder S0.5.
