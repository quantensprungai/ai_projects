# Dimensions Contract (HD-SaaS)

<!--
last_update: 2026-02-10
status: final
scope:
  summary: "Vollständiger Satz von Dimensions-Keys für hd_interpretations.payload und node.metadata; Keys mandatory, Werte nullable."
  in_scope:
    - Core + erweiterte Layer-Dimensions
    - Verwendung in Interpretations, text2kg, Synthesis
  out_of_scope:
    - Pro-System-spezifische Ausfüllung
notes:
  - "Interpretations: interpretations_contract.md. KG: text2kg schreibt dimensions 1:1 in node.metadata.dimensions."
-->

**Zweck:** Garantiert semantische Tiefe, verhindert Mischlogik (z. B. Mechanics vs. Social Role), ermöglicht präzise Synthesis und State Detection, schafft Multi-Layer-Kompatibilität (Body Mechanics, Environment, Relationship, Projection).

**Regel:** Dimensions müssen **immer** als vollständiger Key-Satz vorhanden sein (payload.dimensions und node.metadata.dimensions). **Werte dürfen null sein.**

---

## Vollständiges Schema

### Core (immer vorhanden)

| Key | Typ | Bedeutung |
|-----|-----|-----------|
| mechanical | string \| null | Mechanik, Ablauf |
| psychological | string \| null | Psychologische Ebene |
| somatic | string \| null | Körperlich/somatisch |
| social | string \| null | Soziale Rolle, Gemeinschaft |
| shadow | string \| null | Schatten, Not-Self |
| gift | string \| null | Gabe, korrekter Ausdruck |
| role | string \| null | Rolle, Archetypen-Rolle |
| archetype | string \| null | Archetyp |

### Erweiterte Layer (Keys mandatory, Werte nullable)

| Key | Typ | Bedeutung |
|-----|-----|-----------|
| body_mechanics | string \| null | Physische Traits, unbewusste Körpereinflüsse (Layer Body-Mechanics) |
| environment | string \| null | Ortsabhängigkeit, PHS, Umgebung (Layer Environment/Fate) |
| relationship_pattern | string \| null | Beziehungsdynamik, Nähe/Distanz (Layer Relationship Dynamics) |
| projection_field | string \| null | Erwartungsfeld, soziale Projektion (Layer Hidden Expectations) |

Diese vier Slots decken die Bereiche Body, Hidden Expectations, Relationship, Environment ab – ohne separate Tabellen. Abgleich: erkenntnisse_und_fuer_spaeter.md §2.

### Optional (später erweiterbar)

| Key | Typ |
|-----|-----|
| practice | string \| null |
| context | string \| null |
| language | string \| null |
| examples | string[] \| null |

---

## JSON-Beispiel (payload.dimensions)

```json
{
  "dimensions": {
    "mechanical": null,
    "psychological": null,
    "somatic": null,
    "social": null,
    "shadow": null,
    "gift": null,
    "role": null,
    "archetype": null,
    "body_mechanics": null,
    "environment": null,
    "relationship_pattern": null,
    "projection_field": null
  }
}
```

Optional können zusätzlich `practice`, `context`, `language`, `examples` geführt werden (interpretations_contract).

---

## Downstream

- **text2kg:** Schreibt das komplette Objekt `payload.dimensions` in **node.metadata.dimensions** (MUST). Dimensions werden **nie** als KG-Edges abgebildet.
- **Synthesis / State Detection:** Können gezielt Slots abfragen (z. B. alle Nodes mit `shadow` = X, oder `environment` für Ortsbezug).

**Referenzen:** `interpretations_contract.md`, `text2kg_spec.md`, `layer_model_and_schemas.md`.
