---
last_update: 2026-08-25
status: active — P0 freeze; Packer + Relink live; KARTE Graph visuell zu; Variable-Pfeile live
scope:
  summary: "HD State-Vertrag: 13 chart_element_types, Chart-State, Display-Policy, Planeten als Träger, Type-derived facts, Provenienz. Keine 13 hierarchischen Ebenen."
  in_scope:
    - Vokabular (element_type vs node_kind vs descriptor_element)
    - State-Achsen und Display-Policy Center
    - Planetary activation + accent
    - Type-derived facts, Variable-Pfeile, Mind-Dreiteilung
    - Content-Provenienz (keine Massen-Umbenennung)
  out_of_scope:
    - PHS-UI, Transit-Engine, Aura-K2-Seed, MinerU-Wellen
    - Implementierung in diesem File
basis:
  - cursor/contracts.md §1a / §1b
  - reference/decisions.md 2026-08-17
  - Downloads-Matrix hd_state_contract_matrix.md (2026-08-17)
  - overlay-contract Planeten als Träger
---

# HD State Contract

SoT für chartabhängige Zustände. Facetten-Abruf bleibt `contracts.md` §1a. Dieses File ist **State + Display + Träger**, nicht die 15 Extract-Keys.

## 0. Vokabular (einfrieren)

Nicht von „13 Ebenen“ sprechen. Historic `hd_structure_13_layers_and_engines.md` = Engine-Schichtung (Base→Cross). Produkt:

```text
13 canonical chart_element_types
  + derived descriptor facts
  + activation sources (chart points)
  + activation metadata
  + tradition slots
  + relations/dynamics
  + content_provenance
```

**13 `chart_element_types`:** `center`, `gate`, `line`, `channel`, `circuit`, `type`, `strategy`, `authority`, `profile`, `definition`, `incarnation_cross`, `phs`, `variable`.

`phs` / `variable` sind im Deskriptor noch nicht geseedet — Vertrag vorbereiten, diese Scheibe nicht seeden.

Deskriptor behält zusätzlich `not_self_theme` und `signature` als **`descriptor_element`** (K2 existiert). Das sind keine 14./15. Chart-Typen und keine `hd.concept.*`.

`node_kind`: `chart_element | concept | source | system_class`. `hd.concept.open_center` = concept, nicht Chart-Typ.

Vier Dinge getrennt:

| | Was | Beispiel |
|---|---|---|
| A Elementtyp | der Knoten | `hd.line.57_5` |
| B Chart-State | diese Person | `definition_status: undefined`; juxtaposition |
| C Tradition-Slot | Essay dieses Typs | `mind_when_open`; `exalt` |
| D Relation/Dynamik | zwischen Elementen | harmonic fix; `sys_dynamics` |

`link_role` = Aboutness (`primary|contrast|mention`). `knowledge_kind` = Wissensart (`element_essay|class_overview|relationship|sibling_contrast|source_overview|system_introduction|combination`).

Begriff **System-Facette** nicht verwenden (vermischt B und C).

## 1. Center-Kernstate

Persistiert:

```text
definition_status: defined | undefined
```

`open` ist **kein** dritter Kernwert. Im Code ist `undefinedCenters` das Invert von `definedCenters` (`normalize-hd-chart.ts` `collectCenters`). UI darf umgangssprachlich „offen“ sagen; Packer und Vertrag sprechen `undefined`.

Optional später, nicht erzeugen bis ein Produkt es braucht:

- Roh: `has_active_gate`, `active_gate_count`, `has_complete_channel`
- Derived label: `completely_open` nur wenn `has_active_gate == false`

`open_context` darf `definition_status` nicht überschreiben.

## 2. Display-Policy Center (nicht Ontologie)

State bestimmt **Reihenfolge und Gewichtung**, nicht Existenz. Gift bleibt bei undefined verfügbar; Shadow bei defined.

Immer zuerst: `mechanical` (`canonical_wording`, **read-time** nach State geschnitten; DB nicht wipen).

Dann der **C-Slot zum State** (defined_expression vs. open_expression + mind_when_open).

Danach **Gift und Shadow gleichrangig** — zwei Frequenzen. Chart-State sagt nicht, welche du lebst; das folgt Strategie/Autorität. Nicht: undefined → Shadow zuerst als Wahrheit.

Trap / Projektionsfeld sekundär (Prozess/Feld).

S0.5-Essays (Never Mind / Shadow) sind **undefiniert-Essays**. Ihr Gift darf nicht als Gift eines **definierten** Centers erscheinen.

Overlay darf **enger** sein (Länge): undefined Center nennen, je ein Satz Sampling/Weisheit und Konditionierung. Das ist keine Aussage „definierte Zentren haben keinen Schatten“.

**Nicht in diese Policy:** Not-Self Theme, Signature, Aura, Variable/PHS, Retrograde, planetary_accent, chart_context, Concept-Gattung.

## 3. Type-derived descriptor facts

```text
Type → Strategy, Authority-Kontext, Aura, Not-Self Theme, Signature
```

K2-IDs bleiben wertbasiert: `hd.not_self_theme.bitterness`, `hd.signature.success` (nicht `hd.not_self_theme.projector`). `derived_from: hd.type.*`.

`aura`: Vertrag `candidate` / `engine_derived`. Kein neues K2.

`hd.not_self_mind.*` nicht seeden, nicht als Haupt-ID.

## 4. Activation metadata

Kein Elementtyp. Einmal an der Aktivierungsquelle:

- `side`: `personality | design`
- `consciousness`: `conscious | unconscious | both`
- `motion`: `direct | retrograde | stationary | unknown` — **nicht** Gate-/Line-State
- `chart_context.kind`: `natal | transit | relationship | composite | progression | unknown`

Heute nur Natal. Kontext trotzdem deklarieren.

Inspector darf zeigen: `57.5 — Pluto, Personality, retrograde`. Speichern: `activation.motion`. Retrograde ändert nicht Fixing-Mechanismus, Exalt/Detriment oder Facetten.

Code: `HdActivation.retrograde` boolean — später Enum. Overlay v1c packt R nur für benannte Lines; das ist Anzeige, nicht `line_state: retrograde`.

## 5. Planetary Activation (Träger)

Kette:

```text
Chart-Point (body)
  → planetary activation
  → Gate + Line
  → Channel / Center / Definition
  → Line Fixing / Interpretationsbezug
```

Planeten / Punkte sind **`node_kind=source`**, kein 14. Chart-Typ. `body_kind`: `planet | luminary | lunar_node | earth_point | other_chart_point`. Code-Typ `HdPlanetId` bleibt Träger-ID (Sun/Earth/Nodes inklusive).

Vier Ebenen, nicht in den Line-Node kopieren:

1. **Rohdaten** — body, side, consciousness, motion, longitude, gate, line, color/tone/base
2. **Mechanischer Effekt** — `activates_gate`, `activates_line`, `source_for_fixation`
3. **Planetary accent** — quellengebundener Content-Slot. Buch ingest+relink liegt; Inspector liest `primary` (*Understanding the Planets*). Overlay noch ohne Träger-Satz.
4. **Fixation event** — Relation `source_activation` → Line-Pol

Dachau 57.5:

- exaltation ← Pluto 57.5, `direct`
- detriment ← Mond 10.1, `harmonic` via `hd.channel.10_57`
- `aggregate_status: juxtaposition`

Juxtaposition = beide Pole fixiert, kein Mechanismus, keine Balance, ≠ Kreuz-Geometrie 4/1. Keine Stärke-Rangfolge der Wege.

Line-Fixing-Code ist bereits so getrennt (`hd-line-fixing.ts`). Ruleset-Name: `hd_extended_line_fixing_v1`.

## 6. Variable / PHS

Pfeilposition = Primärschlüssel: `top_left`, `bottom_left`, `top_right`, `bottom_right`. Je `direction` left/right + `raw` Color/Tone/Base.

Semantik über `hd_variable_mapping_v1` (Determination/Digestion, Awareness/Motivation, …) — nicht als Core-Enums.

`configuration.code` (`LRLR`) / `quadruple_left` = abgeleitetes Label, nicht Primär-State.

**PHS ≠ Variable.** PHS = Determination/Nourishment; Variable = vier Pfeile. Mapping, Graph-Marker und Register Körper/Fakten sind live. Mini-Pfeile an den Rails (Color/Tone je Planet) erst PHS-Ansicht, nicht Overlay.

## 7. Mind — drei Dinge

| | Ebene | Wo |
|---|---|---|
| Not-Self Theme | Type | `hd.not_self_theme.*` |
| Center-Frage / Conditioning | Center C-Slot | `mind_when_open` (Legacy-Alias; später `center_question`) |
| Mind-Prinzip | Systemlehre | *Never Mind*: Mind beobachtet, entscheidet nicht — kein Chart-State |

S0.5 (*Never Mind*, *You and the Shadow*) hängt an `hd.center.*`. Checkliste-Wellenname `not_self_mind` war TOC, kein K2.

`mind_when_open` ist kein State, kein dritter Center-Wert, kein Not-Self Theme. Nur bei Evidenz füllen.

Concept-Node `hd.concept.open_center` (`knowledge_kind=class_overview`) P2: Relink-Skript `ic_s05_open_center_concept.py`. Overview nicht als primary auf den 9 Centern. Overlay liest den Concept-Node nicht.

## 8. Content-Provenienz

Keine Massen-Umbenennung (64keys/Gene Keys/Shadow). Umbenennen schützt nicht und verwirrt Abruf.

Mechanische Keys bleiben: `center`, `gate`, `line`, `defined`, `undefined`, `exaltation`, `detriment`, `harmonic`, `retrograde`.

Interpretative Inhalte:

```json
"content_provenance": {
  "framework": "hd_core | traditional_hd | vendor_64keys | gene_keys | source_other | app_custom | unknown",
  "rights_status": "unknown | pending_review | owned | licensed | do_not_publish",
  "text_origin": "imported | original | unknown",
  "display_allowed": false
}
```

HD-Schulen = `tradition` auf gleichem `hd.gate.N`. Gene Keys = eigenes System `gk.*`. Kein Wipe vor Audit. Shadow/Gift zuerst quellenspezifische Slots, keine universellen HD-States.

C-Persistenz (Vertrag, keine Massenmigration): `payload.facets` für `mind_when_open`, `open_expression`, `defined_expression`, `exalt`, `detriment`. MVP liest `facet_hints` + primary-Interps. Intern Null: `not_applicable | no_evidence | not_extracted | pending_review | populated`. `life_domains` Plural nur dokumentieren.

## 9. State-Matrix (13 Typen, Kern)

Statuswerte: `confirmed | engine_derived | vendor_specific | candidate | not_applicable | open_question`.

Wrapper je Dimension: `value`, `status`, `confidence`, `derived_from`, `ruleset`, `explanation_key`.

| Typ | Kern-States (MVP) | Vorsichtig / später |
|---|---|---|
| center | `defined \| undefined` | `open_context`, completely_open |
| gate | present/absent; hanging/channel_complete/inactive | dormant |
| channel | complete/partial/absent | — |
| line | activation; fixation je Pol; aggregate juxtaposition | — |
| definition | single/split/triple/quadruple/none | bridges |
| type | computed type | — |
| strategy / authority / profile / cross | computed facts | — |
| circuit | mapping | dominance |
| phs / variable | raw + availability | labels ohne Mapping |

Line-Fixation: Mechanismen `direct | same_gate | harmonic` (+ später relationship/transit) **je Pol**. `juxtaposition` nur aggregiert.

Detaillierte Enum-Tabellen und JSON-Beispiele: Recherche-Matrix 2026-08-17 (Downloads); bei Widerspruch gilt **dieses File** + `contracts.md` §1a/1b.

## 10. MVP-Abgrenzung

Verbindlich in der KARTE-Scheibe: Center `defined|undefined`; Personality/Design; Type/Strategy/Authority/Profile/Definition; Line-Fixing + R; Display-Policy; Overlay-Cache. Gate hanging / Channel partial sind im Vertrag, in der UI noch nicht als Badge. Provenienz-Felder im Vertrag, nicht massenhaft in der DB.

Nicht als Nutzer-Claim: `open` als Core-Enum; universelle Anbieter-Matrix; PHS-Labels ohne Mapping; Stärke von harmonic vs direct; Planeten-Accent ohne Buch.

## 11. Delta — was liegt (2026-08-17)

Siehe auch Checkliste „Bestandsaufnahme 2026-08-17“. Kurz:

- Liegt, mechanisch richtig: Rails, Line-Fixing, 384er C, Type/Not-Self/Signature-K2, Center-Karten mechanical, S0.5 an `hd.center.*`
- Packer liest: S0.5 primary + `facet_hints` + Gift/Shadow (undefined). S0 Defined-C `defined_relink_v2` (Winn+Schoeber; Will=Heart). Overlay-Cache v1f. Concept-Node `hd.concept.open_center`
- Name: `undefinedCenters` (Invert von defined; UI-Wort „offen“ ok)
- KARTE-zu: Inspector/Overlay lügen nicht über Center-State. Mechanical-Mix im Atom bleibt.
- Richtig nicht geseedet: `hd.not_self_mind.*`
- Planeten-Accent: Inspector liest Primary; Overlay noch ohne Träger-Satz
- Nicht: Corpus-Relink aller Layer, MinerU-Wipe, Aura-K2, Massen-Rename
