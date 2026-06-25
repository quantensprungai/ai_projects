---
last_update: 2026-05-07
status: draft
scope:
  summary: "Entscheidungs-Matrix: wann ein system_id + Tags reicht vs. Split bei Ontologie-Kollision; Defaults pro Ur-System; Chart-Engines vs. Ontologie; IC-Präferenzen Kabbalah/Chakra."
  in_scope:
    - Kriterien A/B (kein Split vs. Split)
    - Policy-Tabelle Ur-Systeme + western_elements
    - calculation_model / engine_profile für Jyotish/BaZi/Astro/Tzolkin
    - Verknüpfung literature_canon_by_scope.md
  out_of_scope:
    - Konkrete DB-Migrationen
    - Implementierung MinerU/Extraktion
notes:
  - "Inhalt schließt an externe Architektur-Analyse an; für IC kuratiert und mit Präferenzentscheidungen versehen."
---

# Ontologie-Policy: ein Graph vs. Split (`system_id`)

## Standard (Default)

**Ein Meta-Knowledge-Graph** mit first-class **Metadaten** auf jeder extrahierten Aussage / jedem Knoten:

- `tradition`, `text_line`, `lens` (z. B. `tcm`, `samkhya`, `cosmology`)
- `source_work`, `evidence_class`, Provenance
- für Chart-Systeme zusätzlich: **`calculation_model`** / **`engine_profile`** (Ayanamsha, Haus-System, Jahr-Grenze BaZi, tropical/sidereal, …) — **nicht** durch Ontologie-Split ersetzen

**Split (zweites `system_id` oder getrennte „Teilwelt“)** nur als **Ausnahme**, wenn beim Datenmodell klar wird:

- **gleiches Label ≠ gleiche Entität** (strukturell verschiedene Ontologie), und
- ihr sonst dauerhaft `sameAs`/`closeMatch`/`hasAnalogue`-Hölle produziert oder Validierungsregeln sich widersprechen.

---

## 1. Entscheidungskriterien (repo-tauglich)

### A) Kein Split — ein `system_id`, mehrere Schichten

Wenn:

- ein **stabiler K2-Kern** existiert, auf den sich alle Textlinien beziehen (z. B. 64 Hexagramme),
- Unterschiede vor allem **K3/K4** sind (Übersetzung, Kommentar, moderne Deutung),
- die **Entitäten dieselben bleiben**, nur Definitionstexte variieren.

**Technisch:** gleiche canonical IDs (z. B. `i_ching.hex.N`), mehrere **Interpretations-/Definitions-Records** mit `text_line` / `component` (z. B. `judgement`, `image`, `line_1`…`line_6`, `wings`).

### B) Split — zwei `system_id`s oder strikt getrennte Teilgraphen

Wenn:

- **gleich benannte** Knoten („Tree of Life“, „Sefirot“, „Pfad“) **strukturell verschiedene** Ontologien meinen,
- zwei **Curricula/Traditionen** eigenständig behandelt werden sollen (andere Kanten-Typen, andere Validierung),
- ein gemeinsamer Knotenpool **Kontamination** von Queries/UI erzeugt.

**Technisch:** getrennte `entity_registry_*`, optional **Crosswalk-Kanten** nur dort, wo ihr bewusst mappt: `has_analogue`, `inspired_by`, `shares_term_with` (semantisch schwach halten).

---

## 2. Policy-Tabelle (Ur-Systeme + West-Elemente)

| `system_id` | Default | Split-Trigger | Pflicht-Tags / Dimensionen |
| ------------- | ------- | --------------- | --------------------------- |
| **i_ching** | **1** KG | praktisch nie | `text_line`, `component` |
| **`kabbalah_jewish`** / **`kabbalah_hermetic`** | **Split (2 IDs)** | jüdisch-klassisch vs. hermetisch/Golden Dawn | pro Track: `tradition`; Crosswalk nur explizit |
| **chakra** | **1** KG | nur wenn Modelle nicht mehr sauber als „dieselbe Entität“ beschreibbar | `tradition`, `model` (z. B. `6_chakra`, `7_chakra`), ggf. `entity_status` |
| **pancha_bhuta** | **1** KG | nur wenn Ayurveda als **eigene Medizin-Ontologie** strikt getrennt werden soll | `lens`: `samkhya`, `yoga`, `ayurveda` |
| **wu_xing** | **1** KG | nur wenn TCM inkl. Pathologie/Diagnostik als **eigenes** Medizin-KG ohne Mischung | `lens`: `tcm`, `cosmology`, `fengshui` (später); `relation_set`: `sheng`, `ke`, ggf. `zang_fu` |
| **western_elements** | **1** KG | selten | `epoch` / `text_line`: `classical_philosophy`, `hellenistic_astro`, `occult_correspondences` |

Detaillierte **Literatur-Kanon-Tabellen** → `literature_canon_by_scope.md` §6.

---

## 3. Chart-/Engine-Systeme (anderer „Split“-Grund)

Hier ist Trennung meist **keine Ontologie-Spaltung**, sondern **Berechnungsvariante**:

- **`jyotish`**, **`bazi`**, **`ziwei`**, **`astro`**, **`mayan_tzolkin`**, …: je **ein** `system_id`
- Varianten über **`calculation_model`** / **`engine_profile`** (Ayanamsha, Haus-System, Grenzen, tropical/sidereal, …)

So **kontaminieren** Ephemeris-/Parameter-Entscheidungen **nicht** die K3/K4-Interpretationsknoten.

---

## 4. IC-Präferenzentscheidungen (auf die „zwei kurzen Fragen“)

### Kabbalah: zwei `system_id`s oder ein `kabbalah` mit `track`?

**Festgelegt (siehe `decisions.md` 2026-05-07):** **`kabbalah_jewish`** und **`kabbalah_hermetic`**.

**Begründung:** Ontologie-Kollision ist hier hoch; getrennte Registries und ggf. getrennte AA-/MinerU-Pfade reduzieren Fehlzuordnung. Ein einziges `kabbalah` mit `track` wäre zweitbeste Lösung, wenn ihr Deskriptor-/Engine-Zahl unbedingt minimal halten wollt.

### Chakra: ein Entity-Set mit `model`-Tags oder zwei Tracks (`chakra_classical` / `chakra_western`)?

**Festgelegt (siehe `decisions.md` 2026-05-07):** **ein** `chakra` mit starken Tags; kein zweites `system_id` ohne Pilot-Beweis.

---

## 5. Nächste Schritte (ohne sofort alles zu implementieren)

1. Eintrag in **`reference/decisions.md`**: Kabbalah-Split-Namen + Chakra-Default bestätigen.
2. Wenn `entity_registry_*` angelegt werden: **Tag-Felder** im Schema von Anfang an vorsehen (auch wenn zunächst leer).
3. `literature_canon_by_scope.md` §6 bei Bedarf auf **P0/P1 Core** kürzen (nach Literaturbeschaffung).

---

## 6. Verknüpfungen

| Datei | Rolle |
| ----- | ----- |
| `reference/literature_canon_by_scope.md` | Kanon-Werke, K2_ref/K3_deutung, Tabellen |
| `cursor/status.md` | Ur-Systeme vs. Engines |
| `reference/decisions.md` | Festlegung `kabbalah_*` Namen |
