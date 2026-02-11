# Erkenntnisse & Ideen für später (HD-SaaS)

<!--
last_update: 2026-02-10
status: living doc
scope:
  summary: "Sammelstelle für Brainstorming, Abgleich mit Ursprungskonzepten und Ideen, die jetzt nicht umgesetzt werden, aber dokumentiert bleiben sollen."
  in_scope:
    - Relation Types, Dimensions, Interpretation-Struktur
    - Priority Rules, Emergent Logic, Conflict Resolution
    - Körper/Erwartungen/Beziehung/Umgebung vs. Dimensions
  out_of_scope:
    - Änderungen an laufender Implementierung (nur Referenz)
notes:
  - "Verknüpfung: next_steps_was_fehlt_noch.md (Option B), interpretations_contract.md, text2kg_spec.md, dimensions_contract.md."
-->

Dokumentiert Erkenntnisse aus Abgleich mit Ursprungskonzepten, HILOG-System-Design und Brainstorming. **Nicht alles wird jetzt umgesetzt** – diese Ideen bleiben für spätere Phasen erhalten.

---

## 1) Relation Types – bewusst beschränkt

**Entscheidung:** Nur **4 Relation Types** im KG: `part_of`, `depends_on`, `amplifies`, `maps_to`.

- **Prozesslogik** („was folgt“, „triggers“, „leads_to“) gehört in **Dynamics** (hd_dynamics), nicht in KG-Edges.
- **Soziallogik** (mit_centers, with_profile) bleibt in **node.metadata.interactions** bzw. hd_interactions, niemals als Edges.
- **Narrative/Story** („was folgt“) = inhaltliche Erzählung, nicht dasselbe wie KG-Relationstypen.

**Für später:** Falls weitere Typen nötig (z. B. `weakens`, `emerges_to`), nur nach Prüfung: Bleibt es strukturell? Oder ist es Prozesslogik? Letztere → Dynamics.

---

## 2) Body / Hidden Expectations / Relationship / Environment

**Abgleich:** Ursprungskonzepte kannten oft separate Bereiche für:
- Body (Körper, Physis)
- Hidden Expectations / Projection Field
- Relationship (Beziehungsdynamik)
- Environment (Umgebung, PHS, Ortsabhängigkeit)

**Umgesetzt:** Bereits über **Dimensions** abgedeckt (keine neuen Tabellen):

| Ursprungskonzept | Dimensions-Slot |
|------------------|-----------------|
| Body / Körper | `body_mechanics` |
| Hidden Expectations / Erwartungsfeld | `projection_field` |
| Relationship / Beziehungsdynamik | `relationship_pattern` |
| Environment / Umgebung | `environment` |

Vollständiges Schema: **dimensions_contract.md**.

---

## 3) Interpretations-Struktur – Beispiele

Die Payload-Struktur (essence, mechanics, expression, challenges, growth, dimensions, interactions) deckt verschiedene Element-Typen ab:

- **Generator:** essence (Lebensenergie), mechanics (Sakral-Reaktion), expression (Flow/Frustration), challenges/growth.
- **Projektor:** mechanics (erkennen, nicht initiieren), expression (warten auf Einladung), challenges (nicht anerkennen).
- **Strategie:** mechanics (wie Entscheidungen fallen), expression (warten auf Reaktion / Einladung je Typ).
- **Autorität:** mechanics (wie Körper/Geist Ja sagt), expression (Klarheit durch warten).

Alle folgen dem gleichen Contract; Beispiele (Generator, Projektor, Strategie, Autorität) in **interpretations_contract.md** §6.

---

## 4) Priority Rules / Emergent Logic / Conflict Resolution

**Für später dokumentiert** – nicht im MVP:

- **Priority Rules:** Wenn mehrere Dimensionen oder Interpretationen kollidieren (z. B. Type vs. Authority), welche hat Vorrang? In HD oft: Authority > Type > Profile > … – als Regelwerk später modellierbar.
- **Emergent Logic:** Wenn mehrere Elemente zusammenwirken (z. B. offenes Solarplexus + Generator), entstehen neue Muster. Für Agent/Pattern-Reasoning relevant; erfordert Reasoning-Layer.
- **Conflict Resolution:** Wie wird bei widersprüchlichen Quellen (verschiedene Bücher) entschieden? Aktuell: Interpretationen bleiben getrennt; Synthesis kann Quellen konsolidieren oder quellenspezifisch darstellen. Später: explizite Regeln.

---

## 5) 12–14 Layer-Schemas ( externe Referenz)

Verschiedene Ontologien (z. B. HILOG, andere HD-Schulen) nutzen 12–14 Layer-Schemas. **Nicht verbindlich übernehmen.** Unser Dimensions-Set (12 Keys + optional) deckt die wichtigsten Bereiche ab; externe Schemas als Referenz behalten, nicht als Pflicht.

---

## 6) Concept Nodes / expresses_as Edges

**Optional, später:** `node_type=concept` für Shadow, Gift, Archetype; Kanten `expresses_as` von Element-Node zu Concept-Node. Aktuell: Dimensions-Inhalte nur in **node.metadata.dimensions**.

---

## 7) Gewichtung (HD z. B. Sonnentor ~70 %, Erdentor ~30 %)

**Umgesetzt:** Edge-Spalte **strength** (low | medium | strong | dominant | overriding). Prozentwerte optional in **edge.metadata** (z. B. `metadata.influence_score`, `metadata.source_planet`).

---

## Referenzen

- **Nächste Schritte / Option B:** next_steps_was_fehlt_noch.md  
- **Interpretations:** interpretations_contract.md  
- **KG / Edges:** text2kg_spec.md  
- **Dimensions:** dimensions_contract.md  
- **Layer-Abgleich:** layer_implementation_abgleich.md
