---
last_update: 2026-08-26
status: contract v0 — KARTE Graph visuell zu; Overlay v1o; Variable-Pfeile live; Rails Color/Tone
scope:
  summary: "HD-Karte: Bodygraph + Planetensäulen, Inspector, Exalt/Detriment-Stati, Overlay-Rezept, Planeten-KG, Bau-Reihenfolge."
  in_scope:
    - Interaktionsmodell HdBodygraph (SVG + Säulen + Inspector)
    - Vier Polaritäts-Stati (exalted / detriment / neither / both)
    - Abgeleitete Fixierung (direct / same_gate / harmonic) als Overlay-Facts, nicht als Buchplanet
    - Was Inspector vs Overlay liest
    - Planeten als Träger-Nodes, nicht als 14. Layer
    - Quellen und offene Literatur-Checks
    - Overlay-Policy: warum eng, was darf später rein, was nie
    - Sequenz UI → Tabelle → Planetenbuch → Overlay-Gewichte
  out_of_scope:
    - Mandala / 4 Spaces
    - PHS-Detail-UI (Color/Tone/Base-Karten)
    - Cross-System-Mapping
    - Pixel-/Visual-Design
    - Implementierung in diesem File
basis:
  - cursor/architecture.md §13 Overlay, §14 HdBodygraph
  - reference/deep_structure_plan.md (Line-Metadata Exalt/Detri = Backlog)
  - reference/hd_structure_13_layers_and_engines.md
  - reference/hd_layer_id_and_chunk_profiles.md (384 Line-Wordings)
  - reference/literature_hd_toc_coverage_2026-08-11.md (Planeten-Buch unused)
  - Chat 2026-08-13/14 (Chart-UI Slice 1 + Overlay-LLM live)
---

# HD Bodygraph + Overlay — Contract v0

Diese Seite ist die **zukünftige HD-Karte** (`/home/karte/hd` → später `/karte/hd`), kein Wegwerf-Test. Mandala bleibt ein anderes Objekt.

## 1. Drei Lesarten (nicht ein Button-Haufen)

| Lesart | Inhalt | Ort |
|--------|--------|-----|
| **Betriebssystem** | Typ, Strategie, Autorität, Definition, Profil | Chips neben dem Graph; **Zusammenschau** |
| **Körpergraph** | Zentren, Kanäle, Tore + **Planetensäulen** | SVG + linke/rechte Rails |
| **Thema / Körper** | Inkarnationskreuz; PHS / Variables | eigene Zeile, nicht im Graph, nicht in der Typ-Zusammenschau |

Ein Klick = eine Selection (`canonical_id` plus optional Aktivierungs-Kontext). Overlay bleibt die OS-Lesung, bis ein späteres „Fokus-Overlay“ extra spezifiziert wird.

## 2. Visuell / Klick

**Säulen (Jovian-Standard):** links **Design** (rot, Körper/Unbewusstes), rechts **Persönlichkeit** (schwarz, bewusst).

Jede Zeile = eine **Aktivierung** (K1, kein Bedeutungs-Node):

`Planetenglyphe · Tor.Linie · Polaritäts-Markierung`

13 Objekte je Seite: Sun, Earth, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, N.Node, S.Node. Die Engine liefert das bereits in `personality_activations` / `design_activations`.

| Wo | Klick | Inspector |
|----|-------|-----------|
| Säulen-Zeile | aktiviert Gate + Line dieser Aktivierung | siehe §4 |
| Tor-Punkt im SVG | dasselbe Gate (ggf. mehrere Aktivierungen) | Gate, dann Lines dieses Charts |
| Kanal | Chip (kein klickbares SVG) | Atom + Achse A (gift/shadow) |
| Zentrum | Center | Center-Wording |
| Chips Typ/Strategie/Autorität/Profil/Kreuz | Atom | Atom-Text; Overlay unverändert |

Zeichen nicht verwechseln:

| Zeichen | Bedeutung |
|---------|-----------|
| **▲** an der Säulen-Zeile | exalted (Planet = Exalt-Planet dieser Line) |
| **▼** an der Säulen-Zeile | detriment |
| **▲▼ übereinander (= Stern)** | Line-Juxtaposition: beide Pole dieser Line fixiert (Weg siehe §3.1). Nicht Juxtaposition-Kreuz (4/1). |
| **R** | Retrograd — K1 aus Ephemeris-Speed (`swe.calc_ut`, Speed < 0) |
| 4 große Pfeile um den Graph | Variables (PHS) — **live** als ←/→ + Color.Tone; Klick → Register Körper |
| Mini-Pfeile an der Zeile | Color/Tone — erst PHS-Ansicht |

## 3. Polarität: vier Stati

Drei Ebenen, nicht vermischen:

| Ebene | Was | Wo |
|-------|-----|----|
| Buchzeile | 18.3 heißt Zealot; Exalt = Neptune, Detriment = Jupiter | 384er-Lookup, Inspector „Linien-Pole“ |
| Direkte Aktivierung | Welcher Planet sitzt auf der Line? Inspector „Diese Aktivierung“ | Occupying vs. Buch |
| Chart-Fixierung | direct + same_gate + harmonic | Rails-Glyphe + Inspector-Quellen |

Pro **Aktivierung** auf den Rails (nur direkt):

| Status | Wann | Anzeige |
|--------|------|---------|
| `exalted` | Planet der Aktivierung = Exalt-Planet **dieser** Line | ▲ |
| `detriment` | Planet = Detriment-Planet dieser Line | ▼ |
| `neither` | anderer Planet auf dieser Line | keine Extrem-Marke (**Default / häufigster Fall**) |
| `both` | **zwei** Aktivierungen auf **derselben** Gate.Linie, eine exalted und eine detriment | ▲▼ gestapelt (= Stern) |

`both` auf Rails v1 entsteht nicht, weil ein Planet beides gleichzeitig ist. Zwei Träger auf derselben Gate.Line, oder (v2) zwei Pole über verschiedene Wege.

Dachau: 64keys Saturn 18.3 ▼ ist nicht die Buchzeile. Persönlichkeit Jupiter 18.1 kann 18.3 ▼ per Same-Gate erklären. 57.5 Stern: Pluto 57.5 ▲ direkt + Mond 10.1 ▼ harmonic über 10–57 (Liniennummer im Partner-Gate muss nicht 5 sein). 384er-Tabelle nicht an 64keys anpassen.

**Hypothese, Literatur-Check offen:** exalted/detriment = Extreme der Line; `neither` = mehr Bandbreite. Nicht als Produkttext, bis I’Ching + Planeten-Kurs das so tragen. Line-Juxtaposition = beide Pole fest angelegt, **nicht** „ausgeglichen“.

### 3.1 Zustand vs. Weg (Overlay-Pflicht)

Die Glyphe ist das **Ergebnis**. Overlay und Inspector nennen den **Weg**.

| Weg `sourceType` | Bedingung | Beleg |
|------------------|-----------|--------|
| `direct` | Planet sitzt auf der Line und ist deren Exalt- oder Detriment-Planet | Rave I’Ching; IHDS |
| `same_gate` | Derselbe Pol-Planet sitzt auf einer **anderen** Line **desselben** Gates | Jovian Archive, Line Fixing (Mars 16.1 → 16.3/16.4) |
| `harmonic` | Derselbe Pol-Planet sitzt im **Partner-Gate** des Kanals (beliebige Line dort) | IHDS 11–56; Jovian Venus 39 → 55.2 |
| später | Transit, Beziehungschart | IHDS / Jovian; nicht Natal-Default |

Ein Fact pro fixiertem Pol:

```
targetLine     hd.line.57_5
pole           exaltation | detriment
sourceType     direct | same_gate | harmonic
sourcePlanet   pluto
sourceGateLine 57.5
sourceSide     design | personality
channel        10-57          # nur harmonic
occupying      pluto @ 57.5   # wer auf der Ziel-Line sitzt; darf ≠ sourcePlanet sein
```

Gleiche Regel, wenn die Line **vorher neither** war und erst abgeleitet ▲ oder ▼ bekommt (nicht nur bei Stern).

**Nicht erfinden:** `direct` sei stärker als `same_gate` oder `harmonic`. Unterschied = Herkunft und Färbung (welcher Planet, bewusst/unbewusst, über welches Tor/welchen Kanal) — keine Intensitätsskala.

**Zwei Juxtaposition-Wörter:** Line-Juxtaposition (beide Pole einer Line) ≠ Juxtaposition-Kreuz / 4/1-Geometrie.

### 3.2 Wie Overlay das liest (kein Stempel)

Nicht: „57.5 ist juxtaposition.“  
Sondern strukturierte Facts + Atomtexte, LLM verbindet:

1. Allgemeine Line (ohne Pol-Wertung).
2. Jeder **fixierte** Pol-Absatz aus der Line (I’Ching), zugeordnet zum **Quell-Planeten**.
3. Ein Herkunftssatz: direkt auf der Line / anderes Line desselben Gates / Partner-Gate + Kanal.
4. Occupying-Planet, falls er nicht der Pol-Planet ist (Saturn trägt 18.3; Jupiter 18.1 färbt den Detriment-Pol).
5. Design vs. Persönlichkeit, wenn die Quellen auf verschiedenen Seiten liegen.

Dachau-Beispiele für den Prompt (v1b, nur Schlüssel-Lines):

```
18.3 occupying: personality Saturn (not a pole planet)
  detriment: same_gate · personality Jupiter 18.1
  → do not say "Saturn is the detriment planet of 18.3"

57.5 occupying: design Pluto
  exaltation: direct · design Pluto 57.5
  detriment: harmonic · design Moon 10.1 via channel 10-57
  → line juxtaposition; do not say "balanced" or "half and half"
```

Edges: solche Facts sind **chart-computed** zur Lesezeit. Form für späteres Retrieval: `hd.line.10_1` —fixes_pole:detriment→ `hd.line.57_5`. Nicht in `sys_kg_edges` als Literatur seeden. Overlay v1 darf definierte Kanäle + diese Facts mitgeben, sobald die Line überhaupt im Prompt ist.

### 3.3 64keys-Abgleich

Zwei Charts mit identischen Gate.Line-Zahlen stützen Same-Gate und Harmonic (Dachau; 26.07.2023; plus 24.05.2019). 37.1 neither in beiden — Buch hat keinen Detriment-Planeten. Rechner live; Rails = Chart-Fixierung; Inspector listet Quellen.

Negativ-Kontrolle: Partner-Gate hat den Pol-Planeten, Ziel-Line unbesetzt → keine Säulen-Zeile; Fixierung höchstens im Inspector.

### Was strukturiert fehlt vs. was als Prosa da ist

| Objekt | Stand |
|--------|--------|
| 384 Line-**Wordings** `hd.line.{g}_{n}` | ✅ Synth 2026-08-07 |
| 384er **Lookup** `gate+line → exalt_planet, detriment_planet` | ✅ pdftotext Complete Rave I’Ching 2011 |
| Generische 4 Status-Essays als Stempel auf jedes Gate | **nicht** das Modell (Barnum) |
| 13×384 Planet×Line-Kombinationstexte | **nicht** vorberechnen |

Die Line-Prosa im Rave I’Ching enthält bereits die **line-spezifischen** Sätze „Mars exalted…“ / „Uranus in detriment…“. Das ist die genaue Kombi **dieser Line × dieser zwei Planeten**, nicht ein dritter Textkorpus.

Katalog-Tabelle ist live (`hd-line-polarity.json`, pdftotext). Nicht aus MinerU-Chunks neu parsen.

Zur Laufzeit: zuerst direkt `activation.planet` × Lookup; zusätzlich abgeleitete Pole als Facts (§3.1). Overlay bekommt **Facts + Pol-Absatz**, nicht nur ein Status-Enum.

## 4. Inspector (Klick, kein LLM)

Bei Säulen-Zeile / Tor, **gestapelt, nicht vermischt**:

1. **Extreme der Linie** — zwei Planeten, die diese Linie polarisieren (▲ / ▼), plus die zwei Absätze. Aktives Extrem hervorheben; `neither` = Occupying ist nicht einer der beiden Planeten.
2. **Dieser Planet** — Chart-Planet × Lookup. **R** = rückläufig, Eigenschaft des Planeten hier, nicht der Extreme.

UI-Stimme (Handbuch): keine Quelltitel, keine canonical IDs, kein Engine-Jargon, kein „Buch“. Mechanik-IDs bleiben intern (`data-canonical-id`). Fachbegriff-Toggle ist Profil-Sache, nicht Default auf der KARTE.
3. **Abgeleitete Fixierung** (v2) — Same-Gate / Harmonic mit Quelle; nicht als Buchplanet des Occupying
4. **Gate** — `hd.gate.N` (Thema)
5. **Line** — `hd.line.{g}_{n}` (Oktave; allgemeiner Atomtext, keine Chart-Lesung)
6. **Planet** — Träger `hd.planet.*`: Glyphe + Name + Primary-Essay (*Understanding the Planets*). Kein Synth. Overlay v1i: **ein** Satz Design-Sonne + Personality-Sonne als Identität (occupying gate.line), nicht die 13 Essays. Packer: `hd-planet-facets.ts`.

„Inspector zeigt den Line-Wording“ hieß: den **Line-Atomtext** als Spezifikum, **plus** Gate als Eltern-Thema. Nicht Line statt Gate.

**Zentrum (gleicher Stapel, andere Facetten):** Atom = `hd.center.*` mechanisch, **read-time** nach `defined|undefined` geschnitten (`splitMechanicalForState`); `canonical_wording` in der DB bleibt Mix. UI darf „offen“ sagen. Display-Policy: immer Mechanik; dann C-Slot; Gift und Shadow gleichrangig; Trap/Feld sekundär. S0.5 nicht auf definierte Center. Defined-C = Winn + Schoeber (`defined_relink_v2`). SoT: `hd_state_contract.md`.

**Kanal:** Chip → Mechanik-Atom + Achse A (`gift`/`shadow`/`trap`) aus `primary`-Interps (`channel_relink_v1`). Kein Center-C (`mind_when_open`). Overlay bleibt Atom-Excerpt (v1g), kein Kanal-Gift im Prompt.

## 5. Overlay / LLM (Zusammenschau)

### 5.0 Warum der Absatz eng ist (nicht GPT-Mini-Quota)

Die Zusammenschau ist **eine Lesung**, kein zweiter Inspector. Regel: wenn der Overlay-Screen wie ein Stapel aller Register wirkt, ist er zu lang.

Das ist **Architektur**, kein Token-Notstand. Constraint = **Admission** (was der Absatz darf), nicht Modellgröße. `gpt-5-mini` hat genug Fenster (v1l: 16k Completion-Cap, `reasoning_effort` medium). Mehr Atome in den Prompt zu kippen macht den Absatz nicht wahrer — es macht ihn inventiv: Gates, die nicht da sind; Gift als Existenzbedingung; Juxtaposition als Balance.

**Was schon drin ist (v1o):** Typ × Strategie × Autorität, Profil in Satz 1–2, definierte Kanäle, Kreuz, undefined-Center (Namen + Wisdom/Conditioning), Fixing+R nur an Schlüssel-Lines (Sonne/Erde + Kanal-Tore), **ein optionaler Fakten-Satz** (Viertel beider Sonnen + Linien-Gewicht), **Pol-Absatz je fixiertem Schlüssel-Pol** aus I’Ching-Chunks (paraphrasiert im Overlay, voll im Inspector). Overlay ist ohne den Fakten-Satz vollständig.

**Fakten-Satz (v1n, live):** Chart-Fakten als Klebstoff, nicht als Rewrite der Atome. Beispiel Dachau:
„Personality Sun sits in the Quarter of Mutation (gate 14); 13 of 26 activations fall there. Design Sun sits in Duality (gate 29). Line 5 carries the most weight.“
Zahlen kommen aus `hd-facts.ts`, nicht aus dem LLM. Das Modell klebt genau einen Satz mit diesen Zahlen; es darf die Viertel-/Linien-Atome nicht umschreiben. Fehlt der Block oder das Modell lässt ihn weg — der Absatz bleibt gültig.

**Was später, nur als Facts, nicht als Literaturstapel:**
PHS-Achsen-Labels der Instanz (`Determination 3 · Thirst` …) — ein halber Satz, sobald das Mapping sitzt. Nicht die vier Pfeil-Essays (`hd.variable_def.*`) und nicht Environment ohne Quelle.

**Was nie ins Overlay:**
- alle 26 Aktivierungen
- volle Gate-/Line-Essays
- Concept-Node `hd.concept.open_center`
- alle definierten Center als Checkliste
- Wiederholung desselben Atomtexts, der schon im Register steht
- PHS-Ortsnamen ohne belegte Quelle
- LLM-Zuschnitt der generischen `hd.line_def.*` / `hd.quarter.*` auf „dein Chart“

Register **Fakten / Körper / Zentren** = Lookup. Overlay = Kombination. So bleibt Chart-Wahrheit deterministisch.

v0 (live): Typ × Strategie × Autorität + Profil-Label + **undefined Center mit Atomtext** (Lookup aller 9 `hd.center.*`, nicht nur Engine-`nodes`). Prompt: Chart-State **undefined** zuerst; HD-Wort „open“ nur als Klammer. Keine Gates erfinden. S0.5 ist **zweiter** Block für undefined Center (Priorslots), nicht Ersatz/Re-Synth des Atoms und nicht „defined haben keinen Schatten“. **Profil in Satz 1–2** (Typ × Profil, z. B. 3/5 Splenic Projector). `hd.concept.open_center` wird **nicht** ins Overlay gelesen.

**Cache (v1o):** `user_charts.overlay` jsonb, Schlüssel `person_id + locale + ruleset (hd_overlay_v1o) + chartHash` (Hash enthält den Fakten-Summary + `polesMode`). v1n→v1o = Pol-Absatz der fixierten Schlüssel-Lines aus I’Ching-Chunks; v1m→v1n = optionaler Fakten-Satz; v1l→v1m = undefined Center im Prompt als Namen + Wisdom/Conditioning, keine Center-Checkliste. Hinted S0.5-Karten füllen nur den Hint-Slot (Shadow nicht mehr Expression/Trap/Projektion). Chart-Anzeige: SessionStorage (HMR/Refresh) + GET `/api/ic/hd-chart` (letzter `user_charts`-Snapshot, ohne Engine).

**v1a/v1b (live):** definierte Kanäle + Inkarnationskreuz im Prompt. Channel-IDs Katalog-Reihenfolge (`8_1` nicht `1_8`). Cross-Slug: Engine `the_right_angle_…` → KG ohne `the_`.

**v1c (live):** Fixing+R nur für Schlüssel-Lines, die der Absatz schon nennt: Sonne/Erde beider Seiten (Kreuz) und alle Aktivierungen auf den Toren definierter Kanäle. Nicht die 26 Säulen. Facts mit Herkunft (`direct` / `same_gate` / `harmonic`) + Occupying + R; kein Status-Stempel „balanced“. Saturn 18.3 bleibt Rails/Inspector, solange 18 kein Kreuz- oder Kanal-Tor ist.

**Polarität muss ins Overlay**, sobald Gates/Lines überhaupt im Prompt sind — sie färbt, *wie* Line/Tor gelebt wird. Nicht 26 Aktivierungen in einen Absatz.

Rezept:

| Stufe | Overlay bekommt |
|-------|-----------------|
| v0 | OS (Typ/Strategie/Autorität), Profil als Färbung |
| v1 | + definierte **Kanäle** + wenige Schlüssel-Gates (Sonne/Erde = Kreuz) + `sys_kg_edges` intra-system |
| v1b | pro mitgegebenem Gate/Line: **Fixing-Facts** (§3.1) + passender Pol-Absatz je *fixiertem* Pol + Occupying. Nicht nur Enum `both`. |
| v1i | ein Satz Design-Sonne + Personality-Sonne (occupying), nicht 13 Planeten-Essays |
| v1j | Template-Fallback = OS-Labels (kein Prompt-Dump); kürzere Center-Excerpts |
| v1k | Langdock gpt-5-mini `reasoning_effort: low`; Template+Fehler kein Cache-Hit |
| v1l | wieder medium + 16k Token-Cap (nicht Geld); low nur Retry; Prosa statt Checkliste |
| v1m | Overlay: Center-Namen + Wisdom/Conditioning; Packer: Hint = nur dieser Slot |
| v1n | ein optionaler Fakten-Satz: Viertel der beiden Sonnen + Linien-Gewicht; Zahlen aus `hd-facts.ts` |
| v1o | Pol-Absatz je *fixiertem* Schlüssel-Pol aus reconstructed I’Ching-Chunks; Inspector beide Buch-Absätze |
| später | weitere Träger-Sätze nur wenn das Buch eine klare Rolle hergibt; keine Gewichte |

Prompt-Regeln sobald Polarität im Overlay ist: keine erfundenen Gates; Exalt ≠ gut, Detriment ≠ schlecht; Line-Juxtaposition nicht als Balance; Occupying nicht mit Pol-Planet verwechseln; Herkunft nennen.

Keine erfundenen Prozent-Gewichte. HD-nähere „Stärke“, die **jetzt** berechenbar ist: Gate in definiertem Kanal vs. hanging. Sonne/Erde = Kreuz-Achse (schon als Cross-Objekt). „Obere Planeten persönlich / untere sozial“ = **nicht** als Kante einbauen, bis das Planeten-Buch das hergibt (klingt nach westlicher Astrologie + Anzeige-Reihenfolge). Keine Rangfolge der Fixing-Wege.

### 5.1 Engine-ID vs. KG-ID (warum Variables nicht einfach ins Overlay)

Die Engine schreibt **Chart-Instanzen**. Das KG speichert **Bedeutungs-Nodes**. Ohne Remap trifft der Lookup ins Leere.

| Engine (`chart.nodes` / raw) | KG-Seed | Stand |
|------------------------------|---------|--------|
| `hd.line.34.1` | `hd.line.34_1` | ✅ Remap in `wordingLookupIds` |
| `hd.channel.10_57` (min_max) | `hd.channel.10_57` bzw. Katalog-Reihenfolge (z. B. Charisma `20_34`) | Wordings **36/36**; Lookup + Overlay + **Kanal-Chips** live |
| `hd.incarnation_cross.{slugify(Name)}` | 192 `hd.incarnation_cross.*` | Nodes + Wordings **genug** (Checkliste 2026-08-11). Lookup + Chip live (`the_`-Slug). |
| `hd.variable.<<>>` (vier Pfeile als String) | `hd.variable.digestion` … `perspective` und/oder `hd.variable_def.*`; Color/Tone/Base = `hd.color_def.N` nicht `hd.color.34.1.3` | Engine-Kombi-ID ≠ Def-Node. Deshalb „IDs passen oft nicht“. PHS-Ansicht braucht Mapping Instanz → Def (`hd-phs.ts`). **Keine Overlay-Essays** (keine Pfeil-Texte, keine `hd.variable_def.*` im Absatz). PHS-Labels der Instanz dürfen später als Facts (ein halber Satz), nicht als Literaturstapel. |
| `hd.color.34.1.3` | `hd.color_def.3` | dasselbe Muster; Color/Tone-Ziffern an den Rails; Mini-L/R nur an den vier Kopf-Pfeilen |

Cross-Wordings sind nicht mehr „14/192 dünn“ — das war der Stand vor dem Tagging 2026-08-05/11. `literature_content_wave` dazu ist veraltet; SoT Dichte: `hd_layer_master_checklist_2026-08-11.md`.

### 5.2 Nächste Schnitte (kein neuer Großplan)

Nicht Fixing+R+Pfeile+Kreuz in einen v0-Absatz. Reihenfolge:

1. ✅ **Overlay v1a/v1b — Kanäle + Kreuz** (Lookup + Prompt). Slug: `the_` abstreifen.
2. ✅ **Inspector-Kanal:** definierte Kanäle als Chips → Atom + Achse A (`channel_relink_v1`). Kein SVG-Umbau.
3. ✅ **Overlay v1c — Fixing+R** nur für Sonne/Erde (Kreuz) und Tore genannter Kanäle.
4. ✅ **Variables/Pfeile:** Mapping `hd-phs.ts` + Marker am Graph (←/→ Color.Tone) + Register Körper/Fakten. Color/Tone-Ziffern an den Rails (keine 26 Mini-L/R). Overlay v1n-Facts live.
5. **Nicht blockierend:** Planeten-Buch, Holistic Analysis 1, Line Companion, `cross_theme.*`, Edges-Retrieval.

v1a braucht keinen Content-Lauf. v1b einen Slug-Check am Dachau-Chart. Pfeile brauchen Mapping, keinen MinerU-All-Ingest.

## 6. Planeten im KG

Planeten sind **kein** 14. `chart_element_type`. Sie sind **Träger** (`node_kind=source`). Historic „13 Ebenen“ = Engine-Schichtung, nicht Ontologie — `hd_state_contract.md`.

- Nodes später: `hd.planet.sun` … `hd.planet.pluto` / Nodes (13). Bedeutung: wofür der Träger steht.
- Nicht: `astro.planet.*` wiederverwenden als HD-Default (anderes System).
- Engine-IDs für PHS-Kombis (`hd.color.34.1.3…`) **nicht** als KG-Nodes; atomar mappen (`hd.color_def.3`, `hd.line.34_1`). Siehe PHS-Alias in `hd_layer_id_and_chunk_profiles.md`.

## 7. Quellen

| Brauch | Wo |
|--------|-----|
| Line-Texte inkl. Exalt/Detri-Prosa | Complete Rave I’Ching; Chunks `rave_iching_gate_lines_reconstructed`; Wordings 384/384 |
| Lookup-Tabelle | dieselben Chunks parsen; Plan `deep_structure_plan.md` 1a |
| Was Planeten *tun* | **`Understanding the Planets in our Design`** (Ra / Rudd 2003) — `queued_unused` |
| PHS-Pfeile / Color | Lunar & Planetary Color* — unused, **nicht** Säulen-Grundbedeutung |
| Chart-Chrome | Rave Cartography (Layout); Engine `raw.*_activations` |

## 8. Bau-Reihenfolge

Nicht Planeten-KG, Edges und UI parallel.

1. ✅ **UI Rails** — Säulen Design/Persönlichkeit, ▲/▼/Stern + R, Klick → Inspector Gate+Line.
2. ✅ **384er-Lookup + Chart-Fixierung** — Rails ▲/▼/Stern aus direct / same_gate / harmonic. Inspector: Buchpole, Occupying-direkt, Quellen. **R** live.
3. **Planeten-Nodes** + unused Planeten-Buch durch die Pipeline (Chunk-Profil zuerst, Checkliste Layer-IDs).
4. ✅ **Overlay v1a/v1b** — Kanäle + Kreuz im Prompt. ✅ v1c Fixing+R an Schlüssel-Lines; Edges später.

Kreuz: Nodes 192 + Wordings laut Checkliste genug. Overlay holt sie jetzt (Slug-Remap `the_`). Variable-Kombi-ID `hd.variable.<<>>` ≠ Def-Nodes; Mapping vor PHS-UI.

## 9. Offen (to check)

- [ ] Trägt die Literatur die Bandbreiten-These (`neither` = weniger Extrem)?
- [x] `both` auf Rails v1 = zwei Träger auf derselben Gate.Line. Line-Juxtaposition über Same-Gate/Harmonic = v2 Facts.
- [x] Chart-Fixierung: zwei 64keys-Charts stützen same-gate + harmonic. Rechner + Inspector-Quelle als Nächstes; Rails direkt bis Quelle sichtbar.
- [x] Overlay-Prompt v1c: Fixing-Facts statt Status-Stempel (kein „balanced juxtaposition“).
- [x] I’Ching-Zeilen ohne Detriment-Planet — Lookup `detriment_planet: null` (37.1: 64keys und wir neither).
- [ ] Anzeige-Reihenfolge der 13 Zeilen (Sonne oben … Pluto unten) vs. irgendeine Wirkungs-Rangfolge
- [x] Line-Wordings (Synth): Exalt/Detri-Absätze **nicht** trennbar — paraphrasiert. Pol-Absatz aus reconstructed pdftotext-Chunks (`hd-line-facets.ts`), nicht aus `canonical_wording`.

## 10. Code-Anker (Ist)

- UI: `apps/web/app/[locale]/home/_components/hd-karte/`
- Overlay: `apps/web/lib/hd/hd-overlay.ts` (OS + Kanäle + Kreuz + v1c Schlüssel-Fixing + Profil-Lead + undefined-first)
- Overlay-Cache: `apps/web/lib/hd/hd-overlay-cache.ts` + `user_charts.overlay` (`hd_overlay_v1o`)
- Chart-Hydrate: GET `/api/ic/hd-chart` + `hd-karte-session.ts` (SessionStorage)
- Overlay-Facts: `apps/web/lib/hd/hd-facts.ts` (`packOverlayFacts`)
- Center-Packer: `apps/web/lib/hd/hd-center-facets.ts` (unhinted S0 nur wenn eindeutig defined/open; Atom `splitMechanicalForState`)
- S0 Defined-Relink: `apps/web/scripts/ic_s0_center_defined_relink.py`
- Overlay-Fixing: `apps/web/lib/hd/hd-overlay-fixing.ts` — nur Sonne/Erde + Kanal-Tore
- Wording-Lookup: `apps/web/lib/hd/hd-wording-lookup.ts` — Center + Channel-Remap + Cross-`the_`-Slug
- Polarität: `apps/web/lib/hd/hd-line-polarity.ts` + `hd-line-polarity.json` + `hd-line-fixing.ts` + `hd-line-facets.ts`
- Extract: `apps/web/scripts/ic_hd_line_polarity_from_pdftotext.py`
- Wording-Lookup: `apps/web/lib/hd/hd-wording-lookup.ts` — **immer** alle 9 `hd.center.*` (Engine-`nodes` = nur definierte Center)
- Normalize: `apps/web/lib/hd/normalize-hd-chart.ts` (Polarität via Lookup; Variable/Color/Tone/Base durchgereicht)
- PHS-Map: `apps/web/lib/hd/hd-phs.ts` (Position = Primärschlüssel; Graph-Marker + Register Körper)
- Engine: `services/hd/src/hd_compute.py` → `personality_activations` / `design_activations`
- API: `apps/web/app/api/ic/hd-chart/route.ts`
