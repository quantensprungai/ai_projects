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

## 2. Lebensbereiche (10 Enums)

User-facing Navigation. Tag `life_domain` im Interpretations-Payload.

| # | Enum-Wert | Label | Kernfrage |
|---|-----------|-------|-----------|
| 1 | `self_identity` | Selbst & Identität | Wer bin ich im Kern? |
| 2 | `love_partnership` | Liebe & Partnerschaft | Wie liebe ich? |
| 3 | `sexuality_intimacy` | Sexualität & Intimität | Wie verbinde ich mich körperlich? |
| 4 | `relationships_community` | Beziehungen & Community | Freundschaften, Zugehörigkeit |
| 5 | `career_calling` | Beruf & Berufung | Was ist meine Arbeit? |
| 6 | `family_home` | Familie & Zuhause | Wie gestalte ich Heimat? |
| 7 | `health_body` | Gesundheit & Körper | Was braucht mein Körper? |
| 8 | `money_resources` | Geld & Ressourcen | Wie verdiene und verwalte ich? |
| 9 | `creativity_expression` | Kreativität & Ausdruck | Was will durch mich? |
| 10 | `meaning_spirituality` | Sinn & Spiritualität | Was ist das größere Bild? |

Lebensbereiche sind ein Tag, kein Schema-Constraint. Hinzufügen/Entfernen/Mergen jederzeit möglich.

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
system_id: 'hd' | 'bazi' | 'astro' | 'jyotish' | 'mayan_tzolkin' | 
           'genekeys' | 'numerology' | 'nine_star_ki' | 'akan' | 'meta'
```

`meta` = system-übergreifende Meta-Knoten (Schicht E).

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

Beispiele: `hd.gate.34`, `bazi.stem.jia`, `astro.planet.mars`, `maya.seal.dragon`, `meta.archetype.initiator`
