# Inner Compass — Contracts & Enums

> Autoritative Referenz für Dimensionen, Lebensbereiche, Payloads, Enums, Facetten.
> Wenn Schema und dieses Dokument sich widersprechen, gilt dieses Dokument.
> Facetten-Vertrag (§1a) + State/Display (§1b) + Decision `reference/decisions.md` 2026-08-17.
> Domänen-Routing / Katalog-Drift: `reference/decisions.md` 2026-08-27.
> HD-State-Matrix: `reference/hd_state_contract.md`.

## 1. Dimensions-Contract (15 Keys)

Jede Interpretation wird entlang dieser 15 Dimensionen beschrieben. Alle nullable.
Im Backend-Schema als `jsonb`-Feld `dimensions` im Interpretations-Payload.

### Kern-Dimensionen (systembreit tragfähig, 3+ Systeme)

| Key | Was | Systeme |
|-----|-----|---------|
| `shadow` | Schattenmuster, Fallen | HD, BaZi, Astro, Jyotish, Maya, Gene Keys |
| `gift` | Geschenke, Stärken, Signatur | HD, BaZi, Astro, Jyotish, Maya, Gene Keys, Numerologie |
| `role` | Rolle in der Welt | HD, BaZi, Astro, Jyotish, Maya, Numerologie |
| `archetype` | Archetypische Muster | HD, BaZi, Astro, Jyotish, Maya, Numerologie |
| `psychological` | Innere psychologische Muster | HD, BaZi, Astro, Jyotish, Numerologie |
| `social` | Soziale Interaktionsmuster | HD, BaZi, Astro, Jyotish, Maya |
| `relationship_pattern` | Beziehungsdynamiken | HD, BaZi, Astro, Jyotish |
| `elemental_quality` | Elementare Qualität (Wuxing/Elemente/Farben) | BaZi, Astro, Jyotish, Maya, Nine Star Ki |
| `temporal_phase` | Zeitliche Phase/Zyklus | BaZi, Astro, Jyotish, Maya, HD |
| `destiny_pattern` | Bestimmungsmuster (Ming/Yogas/Kreuz) | BaZi, Jyotish, HD, Numerologie, Maya |
| `mechanical` | Funktionale Mechanik im System | HD, BaZi, Astro, Jyotish |

### Ergänzende Dimensionen (system-spezifisch wertvoll)

| Key | Was | Primär |
|-----|-----|--------|
| `somatic` | Körperliche Auswirkungen | HD (Zentren), teilw. BaZi/Astro |
| `body_mechanics` | Ernährung, körperliche Bedürfnisse | HD (PHS), BaZi |
| `environment` | Optimale Umgebung | HD (PHS), BaZi (Feng Shui) |
| `projection_field` | Was andere in dir sehen | HD (Offene Zentren), Astro (ASC) |

User-facing (Landkarte/Mandala): Primär die 11 Kern-Dimensionen. Ergänzende erscheinen bei System-Filter-Wechsel.

**Verhältnis zu Facetten (§1a):** Diese 15 Keys sind die **Extraktionsbrille** (LLM füllt, was der Chunk hergibt). Sie sind **nicht** der Abruf-Index. Abruf = Element × Achse A/B/C unten. `mechanical` / `gift` / `shadow` kommen in beiden vor — Extract schreibt sie, die Sicht *liest* sie als Life-Facette.

## 1a. Facetten-Vertrag (Abruf, alle Element-Typen)

Eine **ID** bleibt ein K2-Element. Facetten sind **Slots am Typ**, keine Kind-Nodes (Ausnahme: wo das *andere System* sie als Katalog hat, z. B. Gene Keys Shadow/Gift/Siddhi = eigene K2).

Drei Achsen, nicht vermischen:

| Achse | Was | Quelle | Beispiel |
|---|---|---|---|
| **A — Leben / Prozess** | systemweit, Handbuch + Overlay + Werkstatt | `dimensions.*`, `process.*` (schon im Payload) | gift, shadow, trap, gift_activation, experiment |
| **B — Chart-State** | was *bei dieser Person* wahr ist | Engine K1 | Center `defined\|undefined`; Gate hanging vs. im Kanal; Line-Pol fixiert |
| **C — Struktur-Slot** | Essay, den die Tradition *nur für diesen Typ* hat | Deskriptor `facet_schema.by_element_type` | Center `mind_when_open`; Line Exalt-/Detriment-*Absatz* (Buchzeile) |

**Aboutness** (`link_role` primary | contrast | mention) ist **keine** Wissensart. Sie entscheidet nur: darf dieser Chunk *diesen* Node füttern? Wörterbuch der Pipeline-Objekte (Chunk vs Interp vs Anhang vs Synth): `pipeline.md` §1a.

Wissensarten (nicht alles in mention stopfen):

| Art | Wohin |
|---|---|
| Essay *dieses* Elements | `primary` → Slot A oder C |
| Namensnennung | `mention` — tot für Wording |
| Geschwister-Vergleich | `contrast` → Kante, nicht Node-Prosa |
| Gattung (Klasse „undefined centers“) | Concept-Node, `node_kind=concept`, z. B. `hd.concept.open_center` (P2 live; Overlay liest ihn nicht) |
| Beziehung A→B | `interactions` / `sys_kg_edges` |
| Werk-Einleitung | Source-Essay oder Klassen-Node, nicht 9 Center |
| Kombination 2+ Elemente (ein System) | `sys_dynamics` intra (`system_id`) — Zyklen, Spektren, Type×Center |
| Kombination 2+ Systeme | `sys_dynamics` cross — später `extract_pattern_traps` |

`sys_dynamics` (`trap` / `phase_cycle` / `growth_path` / `spectrum`) ist **eine Ebene höher** als `payload.process`: process = Falle *dieses* Centers; dynamics = Prozess zwischen Elementen. Zuerst systemintern (HD-Zyklen), darüber Cross-System. Siehe Decision 2026-08-26 Dynamiken.

### Achse A — fest, alle Systeme, alle Elemente

Entspricht PRD Handbuch + Spaces. Nicht raten, nicht pro Layer neu erfinden:

| Slot | Payload | Handbuch | Space | Overlay |
|---|---|---|---|---|
| `mechanical` | `dimensions.mechanical` / essence | Tiefe 1 Spiegel | KARTE / Inspector-Atom | ja (OS, Kanäle, Center-„was es ist“) |
| `gift` | `dimensions.gift` | Tiefe 2 Muster | KARTE / 64keys-Potenzial | ja, wenn die Sicht es braucht |
| `shadow` | `dimensions.shadow` | Tiefe 2 Muster | KARTE / Schatten-Sicht | ja, gleichrangig mit gift; Overlay nennt beides kurz bei undefined |
| `trap` | `process.trap` | Tiefe 3 Prozess | WERKSTATT Brunnen | selten im Overlay (zu tief) |
| `gift_activation` | `process.gift_activation` | Tiefe 3 | WERKSTATT Leiter | selten |
| `experiment_seed` | `process.experiment_seed` | Tiefe 4 Experiment | WERKSTATT | nein |
| `temporal_phase` | `dimensions.temporal_phase` | — | ZEIT | nur wenn Transit das Element trifft |
| `life_domain` | Tag, kein Slot | Mandala-Ring | KARTE | Navigation, keine Prosa. Abruf später `belongs_to_domain` (Decision 2026-08-27), nicht dieser Singular |

Gewohnheiten / Lösungen: **kein** neuer Key. `expression` + `experiment_seed` + `gift_activation`. Kombinatorische Fallen (HD-Shadow × BaZi-Clash) bleiben `sys_dynamics`, nicht Facette am Einzel-Node (`decisions.md` 2026-08-05).

`ic_tags` (Tiefe, Brunnen, Leiter, Grammatik) **ordnen** vorhandene Interps den Spaces zu — sie verdoppeln Achse A nicht. Job `tag_ic_metadata` (pipeline.md) ist genau dieses Mapping, noch nicht gelaufen.

### Achse B — Selector, kein Text-Slot

`definition_status` (`defined | undefined`) wählt den **C-Slot** (defined_expression vs. open_expression / mind_when_open), nicht ob Gift oder Shadow „wahr“ ist. Gift und Shadow bleiben zwei Frequenzen. UI: definiert/undefiniert; HD-Lehrsprache „offen“ = derselbe State. `open` ist kein dritter Kern-Enum (`hd_state_contract.md`).

64keys-ähnliche Spalten = A × B (Potenzial/Schatten × defined/undefined) — das ist eine **Anbietersicht**, kein universeller HD-State. Provenienz: `vendor_64keys`.

### Achse C — nur wo die Tradition einen eigenen Essay hat

Nicht für alle Typen erfinden. Im Deskriptor deklarieren, sonst existiert der Slot nicht.

**HD (Stand 2026-08-15, ehrlich unvollständig):**

| element_type | C-Slots | Bemerkung |
|---|---|---|
| `center` | `defined_expression`, `open_expression`, `mind_when_open` | S0.5 füllt mind/open; Karten = mechanical. `mind_when_open` = C-Slot (Center-Frage), nicht Not-Self Theme, nicht Mind-Prinzip |
| `line` | `exalt`, `detriment` | Buchzeile 384er; Chart-Pol ist Achse B |
| `gate` | — | Line ist Child-K2; Gate-Atom = A |
| `channel` | — | Circuit ist Parent-K2 |
| `type` | — | `not_self_theme` + `signature` sind schon eigene K2 |
| `strategy` / `authority` / `profile` / `circuit` / `definition` / `cross` | — | vorerst nur A; C nachziehen wenn Literatur+UI einen eigenen Essay erzwingen |
| `phs` / `variable` | `body_mechanics`, `environment` | schon in dimensions-Ergänzung |

Andere Systeme: dieselben **A**-Slots. **C** im jeweiligen Deskriptor (BaZi: z. B. Day-Master useful/unuseful; GK: Shadow/Gift/Siddhi = K2, nicht C).

### Nacharbeit (kein Corpus-Wipe)

1. **Vertrag jetzt** — dieses §1a + `facet_schema` in `hd.json`. Kein Re-Interpret, kein Center-Re-Synth.
2. **Lesen jetzt** — UI/Overlay dürfen `dimensions.gift|shadow` und `process.*` der *bereits* verlinkten Interps nutzen (process ist laut Audit ~100 % befüllt, nur ungelesen).
3. **S0.5 als erstes C-Füllen** — Relink primary → `mind_when_open` / `shadow` für **undefined**; Overview → `hd.concept.open_center`, nicht 9 Center. Open-Center-Gift nicht auf definierte Center kopieren. Unhinted S0-Primaries nur wenn Essay eindeutig defined oder open.
3a. **S0 Defined-C Relink** — `ic_s0_center_defined_relink.py` v2: nur Winn + Schoeber; Will Center → Heart; Mix/Kanal/PHS skip. S0.5-Solarplexus: Welle/Authority nicht auf undefined.
3b. **Channel Achse-A Relink** — `ic_s0_channel_facet_relink.py` v1c: `primary` + `gift|shadow`. Quellen: Life Force (Hash-Titel), **Rave BodyGraph Circuitry**, Channels by Type 1–3, Winn. Type 4 = Transit-Programm, skip. Max. 3 Primaries/Kanal. Logic (63/4, Node `hd.channel.4_63`) aus Circuitry. Hygiene 20–57 / 9–52: Type-unnamed skip; named/focus darf 1 Geschwister; Circuitry-Scan-Add.
4. **C-Recherche pro Typ** — kurze Tabelle + Literatur, wenn Overlay/Inspector diesen Typ *differenziert* braucht. Historische `canonical_wording` = weiter `mechanical`.
5. **`tag_ic_metadata`** — wenn WERKSTATT/Handbuch-Tiefen gebaut werden, nicht vor S0.5-Relink.

## 1b. HD State, Display, Träger, Provenienz

SoT-Details: `reference/hd_state_contract.md`. Kurz:

**13 `chart_element_types`**, keine 13 Ebenen. Zusätzlich `descriptor_element` (`not_self_theme`, `signature`), `node_kind` (`chart_element|concept|source|system_class`), Activation-Sources (Planeten/Punkte). `hd.concept.*` ist kein 14. Chart-Typ.

**Display-Policy Center:** immer `mechanical`. Danach C-Slot zum State. **Gift und Shadow gleichrangig** (zwei Frequenzen). Trap/Feld sekundär. Overlay darf enger sein — warum und was als Nächstes: Overlay-Vertrag §5.0 (`reference/hd_bodygraph_overlay_contract.md`). S0.5-Essays nicht auf definierte Center.

**Planeten** = Träger (`node_kind=source`), nicht Chart-Typ. `motion` an der Aktivierung. Accent-Text später aus *Understanding the Planets*. Fixation = Event mit `source_activation`.

**Mind dreifach:** Not-Self Theme (Type-K2) ≠ `mind_when_open` (Center-C) ≠ Mind-Prinzip (Systemlehre).

**Provenienz** auf interpretativen Inhalten (`framework`, `rights_status`, `text_origin`). Keine Massen-Umbenennung, kein Wipe vor Audit.

**C-Persistenz:** `payload.facets` (Vertrag). MVP liest `metadata.facet_hints` + `link_role=primary`. Intern: `not_applicable|no_evidence|not_extracted|pending_review|populated`.

`knowledge_kind` ist nicht `link_role`. Concept-Relink: `class_overview`, nicht „≥4 Zentren“.

## 2. Lebensbereiche (12 Enums)

User-facing Navigation. Tag `life_domain` im Interpretations-Payload.

| # | Enum-Wert | Label | Kernfrage | Ring | System-Mapping |
|---|-----------|-------|-----------|------|----------------|
| 1 | `self_identity` | Selbst & Identität | Wer bin ich im Kern? | Nah | 1. Haus/Bhava, 命宫 |
| 2 | `love_partnership` | Liebe & Partnerschaft | Wie liebe ich? | Nah | 7. Haus/Bhava, 夫妻宫 |
| 3 | `sexuality_intimacy` | Sexualität & Intimität | Wie verbinde ich mich körperlich? | Nah | 8. Haus (Intimität), 桃花 |
| 4 | `relationships_community` | Beziehungen & Community | Wie gestalte ich Zugehörigkeit? | Feld | 11. Haus/Bhava, 交友宫 |
| 5 | `career_calling` | Beruf & Berufung | Was ist meine Arbeit? | Feld | 10. Haus/Bhava, 官禄宫 |
| 6 | `family_home` | Familie & Zuhause | Wie gestalte ich Heimat? | Feld | 4. Haus/Bhava, 父母宫+田宅宫 |
| 7 | `health_body` | Gesundheit & Körper | Was braucht mein Körper? | Nah | 6. Haus/Bhava, 疾厄宫 |
| 8 | `money_resources` | Geld & Ressourcen | Wie verdiene und verwalte ich? | Feld | 2. Haus/Bhava, 财帛宫 |
| 9 | `creativity_expression` | Kreativität & Ausdruck | Was will durch mich? | Feld | 5. Haus/Bhava, 子女宫 |
| 10 | `meaning_spirituality` | Sinn & Spiritualität | Was ist das größere Bild? | Kern | 9. Haus/Bhava, 福德宫 |
| 11 | `exchange_learning` | Austausch & Lernen | Wie teile und verstehe ich? | Feld | 3. Haus/Bhava, 兄弟宫, 迁移宫 |
| 12 | `transformation_renewal` | Wandlung & Erneuerung | Was muss loslassen, damit Neues kommt? | Nah | 8. Haus (Tiefe), 12. Haus/Bhava |

Lebensbereiche sind ein Tag, kein Schema-Constraint. Hinzufügen/Entfernen/Mergen jederzeit möglich.

**Abruf:** nicht der Singular `payload.life_domain`. Soll = Kanten `belongs_to_domain` (multi, `candidate`/`approved`, evidence). Plural `life_domains[]` nur dokumentiert, bis die Kanten existieren. Katalog-v0 (Haus/Palast/Bhava/OS) ist deterministisch; Literatur-Pass erst, wenn etwas die Kanten liest. SoT: `reference/decisions.md` 2026-08-27.

**Katalog vs. dieses Enum (Drift — erst prüfen, wenn das System gelesen wird):**

| Datei | Stand |
|---|---|
| `system_structure/ziwei_structure_v0.json` `life_domain_map` | nutzt die Enums dieser Tabelle |
| `system_structure/astro_catalog_v0.json` `houses[].life_domain` | **andere** Strings (`resources_values`, `home_roots`, `partnerships`, …) — angleichen oder eigenes `life_domain_map`, wenn Astro-UI kommt |
| `system_structure/jyotish_catalog_v0.json` `bhavas` | `karakatva[]`, kein `life_domain` — Multi-Map schreiben, wenn Jyotish geroutet wird |
| BaZi / I Ging | kein 12-Rad (4 Pfeiler / 64 Hexagramme) |

Erweiterung von 10→12 (2026-03): §20d-Revision in ergebnis_modelle.md — "Kommunikation" und "Transformation" wurden bei 10 Systemen zu Recht abgelehnt; mit 14 Systemen (inkl. Jyotish 12 Bhavas, Ziwei 12 Paläste, Westl. Astro 12 Häuser) ist die Lücke nicht mehr vertretbar.

## 3. Interpretations-Payload (jsonb)

```json
{
  "essence": "string — Einzeiliger Kern",
  "mechanics": "string — Wie funktioniert es?",
  "expression": "string — Wie zeigt es sich?",
  "challenges": ["string"],
  "growth": ["string"],
  "dimensions": {
    "mechanical": "string | null",
    "psychological": "string | null",
    "somatic": "string | null",
    "social": "string | null",
    "shadow": "string | null",
    "gift": "string | null",
    "role": "string | null",
    "archetype": "string | null",
    "body_mechanics": "string | null",
    "environment": "string | null",
    "relationship_pattern": "string | null",
    "projection_field": "string | null",
    "elemental_quality": "string | null",
    "temporal_phase": "string | null",
    "destiny_pattern": "string | null"
  },
  "process": {
    "trap": "string | null — Typische Falle",
    "gift_activation": "string | null — Wie wird das Geschenk aktiviert",
    "experiment_seed": "string | null — Konkreter Experiment-Ansatz"
  },
  "facets": {
    "mind_when_open": "string | null",
    "open_expression": "string | null",
    "defined_expression": "string | null",
    "exalt": "string | null",
    "detriment": "string | null"
  },
  "content_provenance": {
    "framework": "hd_core | traditional_hd | vendor_64keys | gene_keys | source_other | app_custom | unknown",
    "rights_status": "unknown | pending_review | owned | licensed | do_not_publish",
    "text_origin": "imported | original | unknown",
    "display_allowed": "boolean"
  },
  "life_domain": "string | null — Enum aus Abschnitt 2; kein Abruf-Index (Decision 2026-08-27). später life_domains[] oder belongs_to_domain-Kanten",
  "interactions": {
    "amplifies": ["canonical_id"],
    "depends_on": ["canonical_id"],
    "clashes_with": ["canonical_id"]
  },
  "source": "llm_extraction | manual | stub",
  "evidence": {
    "chunk_id": "uuid | null",
    "quotes": ["string"]
  }
}
```

## 4. System-Enums

```
-- Berechnungssysteme (system_role = 'calculation'):
system_id: 'hd' | 'bazi' | 'astro' | 'jyotish' | 'mayan_tzolkin' |
           'genekeys' | 'numerology' | 'nine_star_ki' | 'akan' | 'ziwei'

-- Struktursysteme (system_role = 'structural'):
system_id: 'i_ching' | 'kabbalah' | 'chakra' | 'enneagram'

-- Meta-Ebene:
system_id: 'meta'
```

`meta` = system-übergreifende Meta-Knoten (Schicht E).

`i_ching` — **nicht** `iching` (einheitliche Schreibweise mit Unterstrich). Faktische 1:1-Verbindung zu `hd.gate.N` und `gk.gate.N`.

**Enneagramm-Schulen:** Analog zu HD-Schulen — `tradition`-Tag auf K3/K4-Nodes. Schulen-spezifische K2-Erweiterungen (Tritypes: Chestnut, Levels of Development: Riso-Hudson) als separates Array mit `school`-Feld im Catalog.

## 5. Edge-Enums

```
relation_type: 'part_of' | 'amplifies' | 'depends_on' | 'modifies' | 
               'clashes_with' | 'maps_to' | 'produces' | 'controls' |
               'belongs_to_domain'
edge_scope:    'intra_system' | 'cross_system'
review_status: 'approved' | 'candidate' | 'rejected'
strength:      'low' | 'medium' | 'strong' | 'dominant'
```

`maps_to` + `cross_system` = Cross-System-Mapping (Schicht D).

`belongs_to_domain` = Element → Lebensbereich (§2). Ziwei-Paläste: `candidate` in Node-Metadata aus `life_domain_map` (Seed 2026-08-27). Ziel-Node später `ic.life_domain.{enum}` (12 Stück). Multi erlaubt. Leitdokument IX.4; Decision 2026-08-27. Nicht verwechseln mit Job `classify_domain` (der taggt `system_id`).

## 6. Dynamic-Types

```
dynamic_type: 'phase_cycle' | 'trap' | 'growth_path' | 'spectrum'
```

- `phase_cycle`: Zeitliche Zyklen (Saturn Return, Luck Pillars, Wavespells)
- `trap`: Verhaltensmuster/Fallen (Not-Self, Unfavorable God)
- `growth_path`: Entwicklungspfade (Dekonditionierung, Element-Balance)
- `spectrum`: Polaritäten (Shadow↔Gift↔Siddhi, Channel-Dualitäten)

## 7. Wording-Ebenen

| Ebene | Enum | Wo sichtbar | Beispiel |
|-------|------|-------------|---------|
| System | `system_level` | Bei System-Filter-Linse | "Offenes Emotionalzentrum" |
| Meta | `meta_level` | Cross-System-Ansicht | Eigener Begriff (z.B. "Blindspot") |
| Handbuch | `handbook_level` | Persönliches Handbuch | "Wenn du in Stress gerätst..." |

## 8. Synthesis Wording Styles

```
style: 'natural' | 'coaching' | 'poetic' | 'technical'
language: 'de' | 'en' | 'zh' | ...
```

## 9. Canonical ID Format

```
{system}.{element_type}.{element_id}
```

Beispiele: `hd.gate.34`, `bazi.stem.jia`, `astro.planet.mars`, `maya.seal.dragon`, `ziwei.palace.soulPalace`, `ziwei.star.ziweiMaj`, `meta.archetype.initiator`

## 10. IC-Prozess-Tags (NEU — aus Gesamtinventur v0.5)

Zusätzliche Tags im Interpretations-Payload für IC-spezifische Zuordnung.
Im `jsonb`-Feld als eigenständiges Objekt `ic_tags` (neben `dimensions`, `process`).

```json
{
  "ic_tags": {
    "ic_step": "integer | null — 1–9 (9-Schritte-Prozess)",
    "ic_depth": "integer | null — 1–4 (Handbuch: Spiegel/Muster/Prozess/Experiment)",
    "ic_brunnen_layer": "integer | null — 1–4 (Verhalten/Muster/Überzeugung/Kernverletzung)",
    "ic_leiter_stufe": "integer | null — 1–5 (Sehen/Fühlen/Verstehen/Handeln/Ernten)",
    "ic_grammatik": "string | null — BEING | HAVING | DOING | INTERACTING",
    "ic_register": "string | null — mechanik | transformation | praxis",
    "ic_safety_gate": {
      "min_depth": "integer | null — Ab welcher Tiefe zugänglich (null = immer)",
      "requires_nervensystem_check": "boolean — Nervensystem-Check nötig vor Zugang"
    },
    "ic_reflexion_frage": "string | null — Reflexionsfrage für dieses Element",
    "ic_experiment_seed": "string | null — Erweiterung von process.experiment_seed"
  }
}
```

### IC-Step-Enums

```
ic_step:
  1 = Eintritt (Chart-Erstellung)
  2 = Wiedererkennung (Resonanz-Erlebnis)
  3 = Verortung (Domänen + Bedürfnisse)
  4 = Verkörperung (Gabel-Punkt, Anker)
  5 = Diagnose (Pattern Traps, EG-Brücke)
  6 = Vertiefung (Brunnen, Wunde-Kette)
  7 = Transformation (Leiter, Experiment)
  8 = Zeitkontext (Pfad + Gezeiten)
  9 = Graduation (Feier, Loslassen)
```

### IC-Depth-Enums (Handbuch-Schichten)

```
ic_depth:
  1 = Spiegel (Was sagen die Systeme? Weg A: Konzeptuell)
  2 = Muster (Cross-System-Bridges, Alltagsmuster. Weg A→B)
  3 = Prozess (Körperlich/emotional arbeiten. Weg B. Safety-Gate!)
  4 = Experiment (Konkreter Versuch im Feld. Weg B+C. Safety-Gate!)
```

### IC-Grammatik-Enums (Max-Neef)

```
ic_grammatik:
  BEING       = Was BIN ich hier?
  HAVING      = Was HABE ich / fehlt mir?
  DOING       = Was TUE ich?
  INTERACTING = Wie INTERAGIERE ich?
```

### IC-Register-Enums (Stimme)

```
ic_register:
  mechanik        = Sachlich, neutral (Schritte 1–3)
  transformation  = Warm, einladend (Schritte 4–7)
  praxis          = Direkt, handlungsorientiert (Schritte 7–9)
```

### Safety-Gate-Regeln

| Tiefe | Zugang | Bedingung |
|-------|--------|-----------|
| 1 (Spiegel) | Frei | — |
| 2 (Muster) | Frei | — |
| 3 (Prozess) | Gated | Nervensystem-Check bestanden (Sicherheit oder regulierte Aktivierung) |
| 4 (Experiment) | Gated | Tiefe 3 durchlaufen + Nervensystem-Check |

16er-Matrix Diagonal-Regel: Brunnen S4 × INTERACTING (unten-rechts) = höchste Intimität → strengstes Gate.

## 11. App-Space-Enums (NEU — Arbeitstitel)

```
app_space:
  space_now       = JETZT (Home, personalisierter Radar)
  space_map       = KARTE (Erkunden, Mandala, Charts)
  space_workshop  = WERKSTATT (Vertiefen, Brunnen→Leiter)
  space_time      = ZEIT (Timing, Transite, Zyklen)
```

Interne IDs (`space_*`) sind stabil. User-facing Labels (JETZT/KARTE/WERKSTATT/ZEIT) sind Arbeitstitel und können sich ändern.

## 12. Person-/Relationship-Enums (NEU — ab v2)

```
person_role:
  self      = Eigene Person (Primary)
  partner   = Lebenspartner/in
  child     = Kind
  parent    = Elternteil
  sibling   = Geschwister
  friend    = Freund/in
  other     = Sonstige

relationship_chart_type:
  composite  = HD Composite Chart
  synastry   = Astro Synastry
  branch_compare = BaZi Day-Branch-Vergleich
  kin_compare    = Maya Kin-Vergleich
```

## 13. Chart-Compute-Metadaten (`compute_profile`)

**Prinzip:** Für **Human Design** bleibt `system_id` **immer** `hd`. Tropical-, Sidereal- oder Hybrid-Berechnungen sind **kein** separates Rechensystem im Enum §4 — sie unterscheiden sich in der **astronomischen Konvention** und im **Engine-Lauf**, nicht in der Bedeutungs-Ontologie (`hd.gate.*` bleibt dieselbe ID-Familie).

**Empfohlenes Feld** am **Chart-Snapshot**, Request-Payload oder serialisiertem Engine-Ergebnis (nebengeordnet zu Geburtsdaten):

```json
{
  "compute_profile": {
    "hd": {
      "zodiac_mode": "tropical_ra_standard | sidereal | hybrid_design_tropical_personality_sidereal",
      "sidereal": {
        "ayanamsha": "lahiri | raman | krishnamurti | yukteshwar | fagan_bradley | custom | null",
        "custom_degrees": "number | null"
      },
      "backend": {
        "ephemeris": "swiss_ephemeris",
        "engine_impl": "dturkuler_humandesign_api",
        "engine_impl_version": "string | null"
      }
    }
  }
}
```

**Semantik:**

| `zodiac_mode` | Anzeigename (UI, IC) | Bedeutung (IC) |
|---------------|------------------------|----------------|
| `tropical_ra_standard` | **Klassisches HD (tropical)** o. ä. | Default / Jovian-kompatibel: tropischer Tierkreis, gleiche Gate-Ableitung wie gängige Ra-/IHDS-Software (Referenz für Produktvergleiche). |
| `sidereal` | **Sidereal HD** (+ gewähltes Ayanamsha im Untertitel) | Sämtliche für HD genutzten Planetenlangen sidereal (inkl. gewählter Ayanamsha); gleiche Longitude→Gate-Pipeline wie tropical, andere Eingabelangen. |
| `hybrid_design_tropical_personality_sidereal` | **EarthStar Human Design** | IC-Hybrid: Design-Zeitpunkt / rote Seite tropical; Persönlichkeit / schwarze Seite sidereal — **nur** mit dokumentierter Engine-Version; Evidenz oft Klasse C/D (siehe `engines.md` §3). Produkt-/Doku-Name festgelegt in `reference/hd_compute_profiles_kg_and_roadmap.md`. |

Anzeigenamen sind **keine** neuen `system_id`-Werte; sie dienen **Labels, Hilfetexten und Consent** — technisch maßgeblich bleibt `zodiac_mode`.

**Vergleichbarkeit:** Composite, Synastry und „gleicher Mensch“ nur innerhalb **desselben** `compute_profile.hd`-Blocks — gemischte Modi nicht stillschweigend vergleichen.

**Canonical IDs:** Unverändert `hd.gate.N`, `hd.type.*`, … — mehrere Modi erzeugen **unterschiedliche aktivierte Teilmengen** auf derselben Ontologie, keine neuen `system_id`-Werte.
