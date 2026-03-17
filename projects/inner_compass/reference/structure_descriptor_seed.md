# Struktur, Deskriptor und Seed — Klarstellung

> Deskriptor vs. Seed verstehen; alle Ebenen pro System erfassen; Struktur sauber und separat speichern. Pro System einzeln betrachten/bauen.

---

## 0. Woher kommt die Struktur? Kit-first vs. Außen-Referenz

**Empfehlung: Kits zuerst analysieren.**

- **Option A (Außen zuerst):** Struktur aus externen Specs (Schema, Leitdokument, IC_KG) definieren und dann in den Kits parsen, um sie zu befüllen. Nachteil: Doppelpflege; die Kits können mehr oder anders strukturiert sein als die Spec.
- **Option B (Kit-first):** Die Kits **vollständig analysieren** — Logik, Elemente, Ebenen, Konstanten und Lookup-Tabellen, die im Code/Data des Kits bereits vorhanden sind. Daraus die Struktur (Ebenen, Nodes, Edges) ableiten und **als unsere Single Source** speichern. Außen-Referenz (Schema, hd_ontological_layer, Leitdokument) dient dann **zur Validierung und Abgleich**, nicht als primäre Quelle für die Struktur-Liste.

**Vorteil Kit-first:** Wir haben alles, was die Engine ohnehin nutzt; die Struktur ist oft schon sauber aufbereitet (Enums, Konstanten, Tabellen). Kein Abgleich zwischen „was das Schema sagt“ und „was der Kit kann“. Nach der Kit-Analyse prüfen wir gegen unsere Ebenen-Checkliste (z. B. hd_ontological_layer 1–13), ob etwas fehlt, und ergänzen nur dann manuell oder aus zweiter Quelle.

**Konkret:** Pro System zuerst im jeweiligen Kit (packages/engines/<system>/) nach allen relevanten Strukturdaten suchen: Centers/Gates/Channels, Stems/Branches, Planeten/Zeichen, Seals/Tones, etc. Daraus die Structure-Datei (oder den structure-Block) erzeugen. Danach: Abgleich mit reference (Schema, Deskriptor element_types), Seed liest die so gewonnene Structure.

### Erste Schritte: Mit HD starten, im Kit nach Struktur suchen

1. **Ort:** `code/hd_saas_app/packages/engines/hd/` (hdkit, geklonte Kopie).
2. **Suchen nach:** Dateien, die Centers, Gates, Channels, Lines, ggf. Tone/Color/Basis definieren. Im geklonten hdkit unter `packages/engines/hd/` liegen u.a.:
   - **bodygraph-data.js** — Gate- und Center-Daten, Lookup-Tabellen
   - **constants.js** — IDs, Namen, Zuordnungen (Center → Gates, Channel = Gate-Paare)
   - **hdkit.js** — Hauptlogik (berechnet Bodygraph aus Geburtsdaten)
   Zusätzlich: alle Stellen, die „center“, „gate“, „channel“, „line“, „tone“, „color“, „profile“, „authority“, „type“ exportieren oder definieren.
3. **Ziel:** Liste aller Ebenen und aller IDs/Beziehungen, die das Kit für Berechnung und Darstellung nutzt. Daraus die Structure (z.B. system_structure/hd.json) ableiten.
4. **Danach:** Mit hd_ontological_layer 1–13 (IC_KG_Node_Edge_Schema) abgleichen, fehlende Ebenen ergänzen; Seed auf diese Structure umstellen oder aus ihr generieren.

So starten wir mit HD und suchen im Code-Kit nach den abgelegten Infos — keine externe Struktur zuerst, Kit als Quelle. **Auswertung der drei Dateien:** [reference/hd_kit_structure_extraction.md](hd_kit_structure_extraction.md) (welche Ebenen wo stehen, was abgeleitet werden kann, was fehlt).

---

## 1. Was ist was? Deskriptor vs. Seed

| Begriff | Was es ist | Wo es lebt | Rolle |
|--------|------------|------------|--------|
| **Deskriptor** | Die **Spezifikation** eines Systems: Welche Element-Typen gibt es, welche IDs, welche Regeln, welches Format. Optional: ein Block **structure** = die vollständige Liste der Knoten/Kanten (Hierarchie, Ebenen). | `projects/inner_compass/system_descriptors/<system>.json` (z.B. hd.json, bazi.json) | Antwort auf: „Wie heißt das System, welche element_types, wie bauen wir canonical_id?“ — und optional: „Welche Nodes/Edges existieren?“ |
| **Structure** (Struktur) | Die **vollständige Baumstruktur** eines Systems: alle Ebenen, alle Knoten (z.B. 9 Center, 64 Gates, 36 Channels, 12 Profile, …), alle Kanten (part_of, etc.). Das ist das, was aus den Kits geparst oder manuell gepflegt wird. | Bisher: hardcoded in `ic_seed_structure.py`. **Ziel:** sauber getrennt, z.B. `system_descriptors/structure/<system>.json` oder ein `structure`-Block im Deskriptor. | Eine **einzige Quelle**: „Alle Ebenen, alle IDs, alle Beziehungen“ — damit wir keine Ebene vergessen. |
| **Seed** | Das **Script**, das die leeren Knoten und Kanten in die **Datenbank** schreibt (sys_kg_nodes, sys_kg_edges). Es **liest** die Struktur (aus Deskriptor oder aus separater Structure-Datei) und **führt aus**: „Erzeuge für jeden Eintrag einen Node, für jede Beziehung eine Edge.“ | `code/hd_saas_app/apps/web/scripts/ic_seed_structure.py` | **Ausführung:** Struktur → DB. Keine eigene „Wahrheit“, nur Consumer der Structure. |

**Kurz:**

- **Deskriptor** = Konfiguration + Regeln (+ optional Structure).
- **Structure** = die komplette Knoten-/Kanten-Liste pro System (alle Ebenen), **sauber und separat** speicherbar.
- **Seed** = Script, das Structure (wo auch immer sie steht) liest und in die DB schreibt.

**Datenfluss:**

```
[System-Deskriptor .json]     ← Regeln, element_types, canonical_prefix
         +
[Structure .json oder Block]  ← Alle Ebenen, alle Nodes/Edges (aus Kit geparst oder gepflegt)
         ↓
    ic_seed_structure.py      ← liest beides, schreibt sys_kg_nodes + sys_kg_edges
         ↓
    Postgres (sys_kg_*)      ← leerer Strukturgraph, bereit für PDF-Interpretationen
```

Deskriptor sagt **wie** wir benennen und validieren; Structure sagt **was** alles existiert; Seed macht daraus die DB.

---

## 2. Alle Ebenen pro System — damit wir nichts vergessen

Jedes System hat eine **interne Hierarchie** (Ebenen). Diese müssen wir explizit führen, damit beim Parsen aus den Kits und beim Seeden **alle** Ebenen vorkommen. Unten die verbindliche Checkliste pro System (einzeln betrachten/bauen).

### Human Design (HD)

**hd_ontological_layer 1–13** (IC_KG_Node_Edge_Schema v1.1). Von fein (Körper) bis grob (Typ/Definition):

| Layer | Ebene | Anzahl | Kurz |
|-------|--------|--------|------|
| 1 | Basis (Hexagramm-Basis) | 5 | Basis-Typen |
| 2 | **Ton** | 6 | Ton (1–6) |
| 3 | **Farbe** | 6 | Farbe |
| 4 | **Linie** | 6 | Line (1–6 pro Gate) |
| 5 | **Tor (Gate)** | 64 | Gate |
| 6 | **Kanal (Channel)** | 36 | Channel (verbindet 2 Gates) |
| 7 | **Zentrum (Center)** | 9 | Center |
| 8 | **Profil** | 12 | Profile (1/1 … 6/2) |
| 9 | Variable/Pfeile | 4 | Pfeile (Digestion, Awareness, …) |
| 10 | **Autorität** | 7 | Authority |
| 11 | **Typ** | 5 | Type (Generator, MG, …) |
| 12 | **Definition** | 4 | Single, Split, … |
| 13 | **Inkarnationskreuz** | 192 | Incarnation Cross |

Zusätzlich in Deskriptor: strategy, not_self_theme, signature, circuit (als Attribut), incarnation_cross als Node-Typ. Beim Parsen aus hdkit und beim Structure-Format: **alle 13 Layer** abbilden; „bis Tone runter“ = Layer 2 (Ton) ist die feinste körperorientierte Ebene.

**Klarstellung 13 Ebenen, Strukturbaum vs. KG, Engines & Lizenz:** [hd_structure_13_layers_and_engines.md](hd_structure_13_layers_and_engines.md). **Ebenen-Recherche, Vollständigkeit, Gene Keys pro Schule:** [hd_ebenen_recherche_und_strukturbaum_vollstaendigkeit.md](hd_ebenen_recherche_und_strukturbaum_vollstaendigkeit.md).

### Gene Keys (GK)

Baut auf HD-Gates auf; eigene Ebenen:

- Gene Key (1–64, entspricht Gate)
- Sequence Step (activation, venus, pearl)
- Shadow / Gift / Siddhi (pro Gene Key drei Frequenzen)
- Programming Partner

### BaZi

- Stems (10), Branches (12), Jiazi (60)
- Elements (5), Ten Gods (10)
- Zyklen: Producing, Controlling
- Day Master, Luck Pillars (Dynamik)

### Westliche Astrologie (Astro)

- Planeten (10+), Zeichen (12), Häuser (12)
- Aspekttypen, Rulerships
- Optional: Dignities, Decans

### Maya Tzolkin

- Solar Seal (20), Tone (13), Kin (260)
- Wavespell (20), Castle (5)
- Earth Family, Richtung (Challenges, Guides)

### Jyotish (Staffel 2)

- Rashi (12), Nakshatra (27), Graha, Bhava
- Dasha-Systeme, Yogas

### Nine Star Ki, Akan, Numerologie, Enneagram

Jeweils eigene, wenige Ebenen (in den system_descriptors bereits als element_types gelistet). Pro System einmal explizit durchgehen und in die Structure-Liste aufnehmen.

---

## 3. Speicherformat: Structure sauber und separat

**Empfehlung:** Structure **nicht** nur als Anhängsel im Deskriptor, sondern **eigene Datei pro System** — damit klar ist: „Hier steht nur die Struktur (alle Ebenen, alle Nodes/Edges), nichts anderes.“

**Vorschlag Ordnerstruktur:**

```
projects/inner_compass/
  system_descriptors/
    hd.json              ← Deskriptor (Regeln, element_types, kg_rules, …)
    bazi.json
    ...
  system_structure/      ← NEU: nur Struktur, eine Datei pro System
    hd.json              ← Hierarchie + alle Nodes/Edges für HD (13 Ebenen)
    bazi.json
    astro.json
    mayan_tzolkin.json
    genekeys.json
    ...
```

**Inhalt einer Structure-Datei (z.B. hd.json):**

- **levels** oder **hierarchy**: geordnete Liste aller Ebenen (z.B. für HD: basis, tone, color, line, gate, channel, center, profile, variable, authority, type, definition, incarnation_cross).
- Pro Ebene: **nodes** (Liste der IDs bzw. Definitionen) und **edges** (von/zu, relation_type). Optional: Verweis auf den Kit-Pfad, aus dem geparst wurde (z.B. hdkit bodygraph-data.js).

So bleibt der **Deskriptor** schlank (Regeln, Formate) und die **Structure** ist die einzige Quelle für „alle Ebenen, alle Knoten/Kanten“. Das Seed-Script lädt dann: Deskriptor (für system_id, canonical_prefix, Regeln) + Structure (für die konkreten Nodes/Edges). Pro System bauen wir **einen** Structure-Baum und **einen** Parser (oder manuelle Pflege), und prüfen gegen die Ebenen-Checkliste oben.

---

## 4. Pro System einzeln betrachten/bauen

- Kits und Systeme sind unterschiedlich; **kein** generisches „ein Parser für alle“.
- Vorgehen pro System:
  1. **Ebenen-Liste** aus diesem Dokument (oder aus Schema/Deskriptor) übernehmen und abhaken.
  2. **Structure-Datei** anlegen (z.B. `system_structure/hd.json`) mit levels + nodes + edges.
  3. **Parser** aus dem jeweiligen Kit (oder manuelle Pflege) füllt diese Datei; Abgleich mit Ebenen-Liste.
  4. **Seed-Script** erweitern: liest für dieses System die Structure-Datei (oder den structure-Block) und erzeugt sys_kg_nodes/sys_kg_edges.
- So stellst du sicher, dass innerhalb jedes Systems **alle Ebenen** vorkommen und **sauber und separat** abgelegt sind; Deskriptor und Seed bleiben klar getrennt (Deskriptor = Regeln, Seed = Ausführung der Structure).

---

*Referenz: cursor/architecture.md (Phase 0), cursor/engines.md (§7 Parsing), cursor/pipeline.md (§6 Strukturbaum-Seeding), IC_KG_Node_Edge_Schema v1.1 (hd_ontological_layer 1–13).*
