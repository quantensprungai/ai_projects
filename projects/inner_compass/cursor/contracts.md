# Inner Compass — Contracts & Enums

> Autoritative Referenz für Dimensionen, Lebensbereiche, Payloads, Enums.
> Wenn Schema und dieses Dokument sich widersprechen, gilt dieses Dokument.

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
  "life_domain": "string | null — Enum aus Abschnitt 2",
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
               'clashes_with' | 'maps_to' | 'produces' | 'controls'
edge_scope:    'intra_system' | 'cross_system'
review_status: 'approved' | 'candidate' | 'rejected'
strength:      'low' | 'medium' | 'strong' | 'dominant'
```

`maps_to` + `cross_system` = Cross-System-Mapping (Schicht D).

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
