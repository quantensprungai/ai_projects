# IC_BRIDGE.md — Übersetzungs-Index KERN → Cursor-Workspace

> **Zweck:** Dieses Dokument ist die einzige Brücke zwischen den KERN-Dokumenten (IC_Fundament + IC_Leitdokument) und dem Cursor-Workspace (architecture.md, contracts.md, pipeline.md, decisions.md etc.). Es ersetzt das PRD als eigenständiges Dokument.
>
> **Regel:** Wenn KERN und Cursor-Doc sich widersprechen, gilt KERN. Dieses Dokument dokumentiert, WO die Übersetzung stattfindet und WO Patches nötig sind.
>
> **Stand:** 26. Februar 2026 | **KERN-Versionen:** IC_Leitdokument v5.1 + IC_Fundament v06

---

## 0. DOKUMENT-ARCHITEKTUR

```
KERN (außerhalb Repo — philosophische + konzeptionelle Wahrheit)
├── IC_Fundament v06          — WARUM? Was glauben wir?
└── IC_Leitdokument v5.1      — WAS? Was haben wir entschieden?
        ↕ diese Datei ↕
CURSOR-WORKSPACE (im Repo — technische + operative Wahrheit)
├── cursor/
│   ├── architecture.md       — Schema, Datenschichten, Tech Stack
│   ├── contracts.md          — Dimensions, Enums, Payloads
│   ├── pipeline.md           — Datenfluss, Extraktion, Prompts
│   ├── engines.md            — Chart-Berechnung
│   ├── status.md             — Wo stehen wir
│   └── handover.md           — Session-Übergabe
├── reference/
│   ├── decisions.md          — Warum so (Entscheidungslog)
│   ├── vision_and_story.md   — Wohin
│   └── schema_and_descriptor_specs.md
└── 99_archive/
    └── prd_v3.md             — ⚠️ ARCHIVIERT, nicht mehr aktiv
```

### Zwischenprodukte → Einarbeitung (nicht als eigene Files behalten)

| Zwischenprodukt | Ziel im Repo | Status |
|---|---|---|
| IC_KG_Node_Edge_Schema v1.1 | `architecture.md` §2 + `contracts.md` §5 | 🔴 Einarbeitung ausstehend |
| IC_System_Ebenen_Mapping v1.0 | `contracts.md` (neuer §10) | 🔴 Einarbeitung ausstehend |
| IC_Extraction_Prompts v1.0 | `pipeline.md` | 🔴 Einarbeitung ausstehend |
| Inner_Compass_PRD_v3 | `99_archive/prd_v3.md` | 🟡 Archivieren |

---

## 1. ENTSCHEIDUNGSREGISTER → CURSOR-DOC MAPPING

Jede KERN-Entscheidung (E-01 bis E-40) wird hier auf das betroffene Cursor-Doc gemappt.

### 1.1 Nicht-änderbare Entscheidungen (Harte Constraints)

| E-ID | Entscheidung | Cursor-Doc | Sektion | Patch nötig? |
|---|---|---|---|---|
| E-01 | Drei Stränge: App, Buch, Forschung | `decisions.md` | Grundstruktur | ✅ Bereits da |
| E-02 | IC_Fundament als gleichrangiger KERN | `decisions.md` | Grundstruktur | ✅ Bereits da |
| E-03 | Dimensions-Contract (15 Dim.) — erweiterbar, nie löschbar | `contracts.md` | §1 | ✅ Bereits da |
| E-04 | HD, BaZi, Astro, Maya = Klasse A | `contracts.md` | §4 | ✅ Bereits da |
| E-07 | 5 KG-Schichten A→E | `architecture.md` | §1 | 🔴 PATCH: Regeln pro Schicht fehlen |
| E-08 | KG als Kern-Architektur | `architecture.md` | §2 | ✅ Bereits da |
| E-09 | Human-Review für Schicht D/E | `architecture.md` | §1 | 🔴 PATCH: Constraint-Regel fehlt |
| E-10 | Confidence-Level pro Knoten | `contracts.md` | §3 Payload | ✅ Bereits da (confidence) |
| E-11 | Provenance-Tag pro Knoten | `contracts.md` | §3 Payload | ✅ Bereits da (source) |
| E-12 | 5 Navigationsachsen | `decisions.md` | — | ✅ Implizit |
| E-15 | Hypothesen-Sprache für alle Ableitungen | `contracts.md` | — | 🔴 PATCH: hypothesis-Flag fehlt |
| E-18 | 11 Lebensbereiche (einheitlich) | `contracts.md` | §2 | 🔴 PATCH: Nur 10 drin, 11. fehlt |
| E-19 | Domänen × Phasen-Matrix (nicht-linear) | `contracts.md` | — | 🔴 PATCH: Fehlt komplett |
| E-20 | 7 Phasen / Heldenreise | `contracts.md` | — | 🔴 PATCH: Fehlt komplett |
| E-22 | Konvergenzmarker = stärkstes Signal | `decisions.md` | — | 🟡 Erwähnen |
| E-23 | Wording: Hypothesen-Sprache Pflicht | `contracts.md` | §7 | 🔴 PATCH: Constraint fehlt |
| E-25 | Dimensions-Contract erweiterbar, nie löschbar | `contracts.md` | §1 | ✅ Implizit |
| E-26 | Rohmechaniken aus Originalwerken | `pipeline.md` | — | 🟡 Klarstellen |
| E-27 | KI-Eigeninterpretation verboten für A/B + factor_scores | `pipeline.md` | — | 🔴 PATCH: Constraint fehlt |

### 1.2 Festgelegte/Aktualisierte Entscheidungen

| E-ID | Entscheidung | Cursor-Doc | Sektion | Patch nötig? |
|---|---|---|---|---|
| E-05 | Gene Keys Staffel 2, Klasse B | `contracts.md` | §4 | ✅ Bereits da |
| E-06 | Enneagramm Klasse C → Pflicht-Brücke via HD | `decisions.md` | — | 🟡 Ergänzen |
| E-13 | Keine Psychologie-Systeme als Primärsystem | `decisions.md` | — | ✅ Implizit |
| E-14 | Synthesis-Meta-View als Default + Lens-Switcher | `contracts.md` | §7 | 🟡 Ergänzen |
| E-16 | Enneagramm-Einstieg via HD-Chart, kein sep. Assessment | `decisions.md` | — | 🔴 PATCH: Fehlt |
| E-17 | Graduation-Konzept verpflichtend | `decisions.md` | — | 🟡 Ergänzen |
| E-21 | 4 Zeitdynamik-Dimensionen | `contracts.md` | §6 | 🟡 Ergänzen (Hierarchie → E-40) |
| E-24 | Widersprüche sichtbar machen → Protokoll E-39 | `decisions.md` | — | 🟡 Ergänzen |
| E-28 | Quellenstrategie: Original → Mapping → Synthese | `pipeline.md` | — | 🔴 PATCH: 3-Schritt fehlt |
| E-30 | KI-Kulturdarstellung mit Qualitätsprinzipien | `decisions.md` | — | 🟡 Ergänzen |

### 1.3 Neue Entscheidungen (v4/v5)

| E-ID | Entscheidung | Cursor-Doc | Sektion | Patch nötig? |
|---|---|---|---|---|
| E-31 | Enneagramm-Triade via HD-Chart ableitbar | `decisions.md` | — | 🔴 NEU |
| E-32 | Analyse: außen→innen / UX: innen→außen | `contracts.md` | §7 | 🔴 PATCH: Richtungs-Constraint |
| E-33 | 3-Gruppen-Taxonomie der Systembeziehungen | `contracts.md` | §5 | 🔴 NEU |
| E-34 | Karte ≠ Territorium (im Fundament, 3-teilig) | `decisions.md` | — | 🟡 Referenz |
| E-35 | 7-Ebenen-Modell als eigenständiges Konzept | `decisions.md` | — | 🟡 Referenz |
| E-36 | System × Ebenen-Mapping: level_tag = KG-Pflicht | `contracts.md` | §3 Payload | 🔴 PATCH: level_tag fehlt |
| E-37 | System-Kernfragen (WIE/WAS/WO/WELCHE WELLE/WOHIN/WOZU/WARUM) | `decisions.md` | — | 🟡 Ergänzen |
| E-38 | 3-Gruppen-Taxonomie der Systeme | `contracts.md` | §4 | 🔴 PATCH: Taxonomie fehlt |
| E-39 | Widerspruchs-Protokoll: zeigen → einordnen → einladen → markieren | `contracts.md` | §5 (edge) | 🔴 PATCH: contradicts-Edge fehlt |
| E-40 | Zeitmodell-Prioritäts-Hierarchie | `contracts.md` | §6 | 🔴 PATCH: Hierarchie fehlt |

---

## 2. PATCH-LISTE — Konkrete Änderungen an Cursor-Docs

### 2.1 contracts.md — 10 Patches

| # | Was | Wo | Inhalt | Quelle |
|---|---|---|---|---|
| P-01 | +1 Lebensbereich | §2 Lebensbereiche | `learning_growth` = "Wachstum & Entwicklung" — "Wohin entwickle ich mich?" | E-18, Leitdok. Kap. XVI |
| P-02 | Lebensbereiche-Labels aktualisieren | §2 | KERN definiert 11 Domänen mit z.T. anderen Labels als contracts.md (z.B. "Identität & Selbstbild" statt "Selbst & Identität", "Emotionen & Innenwelt" statt "Liebe & Partnerschaft" etc.) — vollständige Tabelle aus Leitdok. Kap. XVI übernehmen | E-18 |
| P-03 | 7-Phasen-Modell | Neuer §11 | Entdecken→Verstehen→Verkörpern→Schatten→Navigation→Integration→Horizont, je mit Ton + App-Trigger + primäre Systeme | E-20, Leitdok. Kap. XI |
| P-04 | level_tag Pflichtfeld | §3 Payload | `level_tag: int (1-7)` — PFLICHT pro KG-Node, nicht pro System | E-36, Leitdok. Kap. V |
| P-05 | hypothesis-Flag | §3 Payload + §5 Edges | `hypothesis: boolean` + `human_review_required: boolean` — Pflicht für Schicht D/E Outputs | E-15, E-09 |
| P-06 | Richtungs-Constraint | §7 Wording | Analyse-Richtung = außen→innen (A→E), UX-Richtung = innen→außen (Bestätigung→Muster→Tiefe) — explizit dokumentieren | E-32, Leitdok. Kap. XVII.3 |
| P-07 | 3-Gruppen-Taxonomie | §4 System-Enums oder neuer §12 | Gleiche Linse (Astro↔Jyotish), Echte Komplementarität (HD↔BaZi), Vertikale Erweiterung (HD→GeneKeys) | E-38, Leitdok. Kap. VI.3 |
| P-08 | Edge: contradicts + Stärke | §5 Edge-Enums | `relation_type` += `contradicts`, `extends`, `correlates`, `triggers`, `deepens`, `influences`, `active_during`, `belongs_to_domain`, `part_of_phase` | Leitdok. Kap. IX.4 |
| P-09 | Zeitmodell-Hierarchie | §6 Dynamic-Types | 4 Dimensionen (Astronomisch, Psychologisch, Biographisch, Konvergenz) + Prioritäts-Hierarchie: biographisch > Konvergenz > astronomisch > psychologisch | E-40, Leitdok. Kap. XIII |
| P-10 | Domäne × Phase Matrix | Neuer §13 oder Anhang | 11 × 7 Matrix mit MVP-Prioritäten (● / ○) — aus Leitdok. Kap. XI.2 | E-19, Leitdok. Kap. XI.2 |

### 2.2 architecture.md — 4 Patches

| # | Was | Wo | Inhalt | Quelle |
|---|---|---|---|---|
| P-11 | KG-Schichten-Regeln | §1 | Pro Schicht: Was rein darf, wer reviewed, was user-facing wird. Explizite Regel: "Schicht D+E = NIEMALS ohne human_review user-facing" | E-09, Leitdok. Kap. IX + XXI.4 |
| P-12 | Node-Schema erweitern | §3 | `level_tag`, `phase_tag`, `domain_tag`, `dynamic_type`, `human_review_required` als Pflichtfelder | E-36, Leitdok. Kap. IX.2-3 |
| P-13 | 11 statt 10 Lebensbereiche | §1 oder konsistent mit contracts.md | Konsistenz sicherstellen | E-18 |
| P-14 | Quellenstrategie 3-Schritt | Neuer §11 oder in Pipeline | Schritt 1: Originalquellen → A/B. Schritt 2: System-Mapping → level_tag. Schritt 3: Synthese → D/E mit human_review | E-28, Leitdok. Kap. XXI |

### 2.3 pipeline.md — 3 Patches

| # | Was | Wo | Inhalt | Quelle |
|---|---|---|---|---|
| P-15 | KI-Eigeninterpretation verboten | Globaler Constraint | Schicht A/B: NUR aus Originalquellen extrahiert. Keine KI-Eigeninterpretation. factor_scores: EXPERIMENTAL, nicht user-facing bis validiert | E-27, Leitdok. Kap. XV.2 |
| P-16 | Extraction-Prompts | 4 LLM-Job-Spezifikationen | extract_entities, extract_meanings, extract_relationships, extract_processes — aus IC_Extraction_Prompts v1.0 einarbeiten | Zwischenprodukt |
| P-17 | Chunking-Standards | Neuer Abschnitt | 500–1500 Tokens, 100 Overlap, Metadaten pro Chunk, strukturelle Marker als eigene Chunks | Leitdok. Kap. XXI.3 |

### 2.4 decisions.md — 8 Ergänzungen

| # | Was | Inhalt | Quelle |
|---|---|---|---|
| P-18 | HD→EG Brücke (E-31) | 3-Schritte: Triade automatisch → Subtyp via Resonanz → Subtyp-Hypothese via hängende Tore. Sprach-Regel: NIE "Du bist Typ 6." | E-31, Leitdok. Kap. VII + Fundament Kap. IV-B |
| P-19 | Karte ≠ Territorium (E-34) | Was IC sieht vs. nicht sieht vs. warum das kein Fehler ist. 3-teilig. | E-34, Leitdok. Kap. III.4 + Fundament Kap. III.6 |
| P-20 | 7-Ebenen-Modell (E-35) | Perspektiven (1-7), KEINE Entwicklungsstufen. Nummerierung = Entdeckungsreihenfolge. | E-35, Leitdok. Kap. IV + Fundament Kap. III.7 |
| P-21 | Widerspruchs-Protokoll (E-39) | 4 Schritte: zeigen → einordnen → einladen → markieren | E-39, Leitdok. Kap. XII |
| P-22 | Graduation-Konzept (E-17) | Phase 7 in 3-4 Domänen abgeschlossen. Graduation ≠ Account löschen. Post-Graduation bei Life-Events. | E-17, Leitdok. Kap. XIV |
| P-23 | Enneagramm-Einstieg (E-16) | Via HD-Chart. Kein separates Assessment. Klasse C. | E-16, E-31, Leitdok. Kap. VII |
| P-24 | System-Kernfragen (E-37) | HD=WIE, BaZi=WAS/WANN, Astro=WO, Maya=WELCHE WELLE, GeneKeys=WOHIN, Jyotish=WOZU, EG=WARUM | E-37, Leitdok. Kap. VI.2 |
| P-25 | Biografie-Layer (E-24) | Opt-in, granular, löschbar, lokal, kein Scoring | E-24, Leitdok. Kap. XX |

---

## 3. HARTE CONSTRAINTS — Was Cursor NIE brechen darf

Diese Constraints gelten für JEDEN Code, JEDE Prompt, JEDE UI-Entscheidung im Cursor-Workspace:

| # | Constraint | Quelle | Konsequenz bei Bruch |
|---|---|---|---|
| HC-01 | **Hypothesen-Sprache:** NIE "Du bist X." IMMER "Dein Chart deutet auf X — erkennst du das?" | E-15, E-23 | UX-Review → Rewrite |
| HC-02 | **Schicht D+E human_review:** Kein Output aus Schicht D/E darf ohne human_review user-facing werden | E-09 | Feature-Gate → Block |
| HC-03 | **KI-Eigeninterpretation verboten:** Schicht A/B NUR aus Originalquellen. Keine LLM-Eigeninterpretation | E-27 | Pipeline-Constraint |
| HC-04 | **Dimensions nie löschbar:** Dimensions-Contract ist erweiterbar, NIE löschbar | E-25 | Schema-Migration-Rule |
| HC-05 | **Kein Sucht-Design:** Ziel = Empowerment + Graduation. Keine Dark Patterns | Leitdok. Kap. II | Design-Review |
| HC-06 | **Datensparsamkeit:** Geburtsdaten lokal, Affect opt-in, Biografie löschbar, kein Scoring | E-24, Leitdok. Kap. XX | Privacy-Review |
| HC-07 | **Kulturelle Gleichwertigkeit:** Kein System ist das "Hauptsystem" | Fundament Kap. III.2 | Content-Review |
| HC-08 | **Widersprüche zeigen, nicht verbergen:** Multi-System-Widersprüche sind Feature, nicht Bug | E-39 | UX-Constraint |
| HC-09 | **level_tag ist Pflicht:** Jeder KG-Node braucht level_tag 1-7 | E-36 | Schema-Constraint |
| HC-10 | **factor_scores = EXPERIMENTAL:** Nicht user-facing bis N>30 Validierung + A/B-Test | E-27 | Feature-Flag |

---

## 4. OE-WATCH-LISTE — Offene Entscheidungen die den Code betreffen

Diese OEs sind NICHT im Code zu committen — aber sie beeinflussen Architektur-Entscheidungen:

| OE | Prio | Thema | Impact auf Cursor-Docs | Wann klären |
|---|---|---|---|---|
| OE-04 | 🔴 HOCH | Gene Keys Lizenzklärung | Bestimmt ob `system_id: 'genekeys'` in Staffel 2 oder nie kommt. Ersatzstrategie (OE-18) muss VOR Extraktion stehen | VOR Extraktion |
| OE-05 | 🔴 HOCH | Laurent-Material Policy | Betrifft Quantum HD Quellen in `pipeline.md` | VOR Extraktion |
| OE-11 | 🔴 HOCH | Heldenreise-Einstiegslogik | Hybrid empfohlen: Standard Phase 1 + Option "Krise" → Phase-4-Einstieg | VOR MVP UX |
| OE-12 | 🟡 HOCH | Forschungsdesign Strang 3 | N, Datensätze, Consent — betrifft Opt-in Flows + Hypothesis-Testing | Parallel |
| OE-13a | 🟡 MITTEL | HD→EG Subtyp-Validierung | 3-Schritt-Methodik gesetzt, aber Schritt 3 = Hypothese. hypothesis_badge auf allen Schritt-3-Outputs | Post-MVP |
| OE-16 | 🟡 MITTEL | Graduation UX-Details | Kap. XIV Konzept gesetzt, UX offen | Strang 1 |
| OE-17 | 🟡 MITTEL | Zielgruppen-Operationalisierung | Einsteiger/Fortgeschrittene/Experten in Onboarding & UI | Pre-Launch |
| OE-18 | 🟡 MITTEL | Gene Keys Ersatzstrategie | Falls OE-04 negativ: Ebene-2-3-Gap wie schließen? | Abhängig von OE-04 |
| OE-19 | 🟡 MITTEL | Domäne × Phase UX-Design | Wie zeigt App nicht-linearen Phasenstatus? | Strang 1 |

---

## 5. MVP-SCOPE (aus KERN abgeleitet)

### 5.1 Was ist MVP (Staffel 1)?

```
INHALT:    Phase 1 × alle 11 Domänen + Domäne 1 (Identität) × alle 7 Phasen
SYSTEME:   Klasse A (HD, BaZi, Westl. Astro, Maya) — vollständig
KG:        Schicht A + B vollständig, Schicht C teilweise
FEATURES:  Onboarding, Landkarte/Mandala, Handbuch (4 Schichten), Zeitlinie,
           Flussdiagramm, System-Filter + Lens-Switcher, Cross-System-Insights,
           3 Sprachebenen, Heldenreise (Phase 1-3)
```

### 5.2 Was ist Post-MVP?

```
INHALT:    Alle verbleibenden Zellen der 11×7 Matrix
SYSTEME:   Klasse B (Gene Keys, Jyotish) in Staffel 2
FEATURES:  Kanal-Dualität (4-Felder), HD→EG Subtyp-Hypothese (Schritt 3),
           Innere Strategie (Meta-Node), Affect Check-in, Konvergenz-Marker,
           Daily Compass, Relationship Mode, Biografie-Layer
KG:        Schicht D (Cross-System) + E (Meta-Knoten)
```

### 5.3 Was ist NICHT im Scope (bewusst draußen)?

```
- Psychologie-Systeme als Primärsystem (E-13)
- Numerologie als Einzelsystem (Klasse D)
- KI-generierte Story-Serie (Strang 2 → IC_Vermittlung)
- Forschungs-Pipeline (Strang 3 → IC_Forschung)
- factor_scores user-facing (bis Validierung)
```

---

## 6. HYPOTHESENREGISTER → Code-Implikationen

Aus dem KERN-Hypothesenregister — nur die, die den Code direkt betreffen:

| H-ID | Hypothese | Code-Implikation | Feature-Flag |
|---|---|---|---|
| H-01 | Konvergenz-These | Schicht D quantifizieren → `edge_scope: cross_system` + confidence | Schicht D implementieren |
| H-02 | Multi-Spiegel > Einzelsystem | A/B-Test: Multi-System vs. Single-System Ansicht | UX-Test |
| H-05 | Innere Strategie ableitbar | `inner_strategy.factor_scores` = EXPERIMENTAL. `human_review_required: true` | `feature_flag: factor_scores_visible = false` |
| H-06 | EG-Brücke erhöht Konversion | Conversion-Test: mit/ohne EG-Triade im Onboarding | `feature_flag: eg_triad_onboarding` |
| H-10 | Biografie-Konvergenz | Chart + Life-Event Overlap → `belongs_to_domain` + `active_during` Edges | Post-MVP |

---

## 7. 5-MODELLE VERWECHSLUNGSSCHUTZ

Aus dem Fundament Kap. IV-A — kritisch für korrekte Implementierung:

| Modell | Kernfrage | Richtung | Im Code wo? |
|---|---|---|---|
| A — 5 Navigationsachsen | Wie navigiert der User? | Raum | App-UI / Routes |
| B — 7 Phasen / Heldenreise | Wann ist der User wo? | Zeit (vorwärts) | `phase_tag` im KG + UX-Journey |
| C — 4 Handbuch-Schichten | Wie tief geht ein Element? | Vertikal (Tiefe) | Content-Layer im Handbuch |
| D — KG-Pipeline A→E | Wie denkt IC intern? | Außen → Innen | Pipeline / Worker |
| E — 7-Ebenen-Perspektiv-Modell | Welches System zeigt was? | Keine (Perspektive) | `level_tag` im KG |

**MERKSATZ:** 7 Phasen (B) ≠ 7 Ebenen (E). Phasen = WANN etwas aufgerufen wird. Ebenen = WAS es gibt.

---

## 8. SYSTEM × EBENEN × PHASE MAPPING (Import-Referenz)

Vollständige Tabelle aus Leitdok. Kap. V.5 — dient als KG-Seed-Referenz:

```
System          Element                level_tag  phase_tag  dynamic_type  domain_tag
HD              Typ (MG/G/M/P/R)      4          1          static        1 Identität
HD              Offene Zentren         3+5        4          trap          2 Emotionen
HD              Inkarnationskreuz      7          7          static        9 Spiritualität
HD              PHS / Variables        3          3          static        3 Körper
HD              Autorität              4          5          static        1 Identität
HD              Profil                 4+7        1-2        static        1 Identität
HD              Not-Self-Thema         5          4          trap          2 Emotionen
BaZi            Day Master             4          1          static        1 Identität
BaZi            Luck Pillars           4          5          phase_cycle   7 Arbeit
BaZi            Clashing Pillars       5          4          trap          4 Familie
BaZi            Nützliche Götter       7          7          growth_path   9 Spiritualität
BaZi            Element-Konstitution   3          3          spectrum      3 Körper
Astro           Sonnenzeichen          4          1          static        1 Identität
Astro           Mondzeichen            5          2-4        spectrum      2 Emotionen
Astro           Nordknoten             7          7          growth_path   9 Spiritualität
Astro           Saturn                 5          4-5        phase_cycle   7 Arbeit
Astro           Chiron                 5+3        4          trap          3 Körper
Astro           Aszendent              1          1          static        1 Identität
Maya            Geburts-Kin            4          1          static        1 Identität
Maya            Galaktischer Ton       7          7          static        9 Spiritualität
Gene Keys       Shadow                 5          4-6        growth_path   11 Wachstum
Gene Keys       Gift                   2-4        6          growth_path   11 Wachstum
Gene Keys       Siddhi                 6-7        6-7        growth_path   9 Spiritualität
Enneagramm      Triade                 3+5        4          static        2 Emotionen
Enneagramm      Typ (1-9)             5          4          trap          1 Identität
Jyotish         Nakshatras             4+7        7          static        9 Spiritualität
Jyotish         Dashas                 4          5-7        phase_cycle   7 Arbeit
```

---

## 9. SPRACH-REGELN FÜR CURSOR-KONTEXT

Diese Regeln gelten für jeden LLM-Prompt, jede UI-Textstelle, jeden Agent-Output:

| Regel | Beispiel FALSCH | Beispiel RICHTIG |
|---|---|---|
| Nie deterministische Aussagen | "Du bist ein Manifestor" | "Dein Chart deutet auf den Manifestor-Typ — erkennst du das?" |
| Cross-System-Konvergenz | "HD und BaZi sagen dasselbe" | "HD und BaZi zeigen hier dasselbe Thema — das ist ein starkes Signal" |
| Widersprüche | (verbergen) | "Diese zwei Systeme sehen dich hier unterschiedlich. Welches fühlt sich wahrer an?" |
| Hypothesen-Badge | "Dein Enneagramm-Typ ist 6" | "Dein offenes Ajna deutet auf die Mentaltriade (5/6/7) — welcher davon klingt wahr?" |
| Schicht D/E Output | (direkt anzeigen) | "[Hypothese] Basierend auf Cross-System-Analyse..." |

---

## 10. AUSFÜHRUNGSPLAN — Patches in Reihenfolge

| Schritt | Aktion | Aufwand | Abhängigkeit |
|---|---|---|---|
| 1 | P-01 bis P-10: contracts.md patchen | ~2h | — |
| 2 | P-11 bis P-14: architecture.md patchen | ~1h | — |
| 3 | P-15 bis P-17: pipeline.md patchen | ~1h | Zwischenprodukt IC_Extraction_Prompts |
| 4 | P-18 bis P-25: decisions.md ergänzen | ~1.5h | — |
| 5 | PRD v3 → 99_archive/ verschieben | 5 min | — |
| 6 | Zwischenprodukte einarbeiten + archivieren | ~2h | Schritt 1-3 abgeschlossen |
| 7 | status.md + handover.md aktualisieren | ~30 min | Schritt 1-6 abgeschlossen |

**Gesamtaufwand: ~8-9h Arbeitszeit** (kann über mehrere Sessions verteilt werden)

---

## CHANGE-LOG

```
Datum       Version  Änderung
26.02.2026  v1.0     Erstversion: 40 E-IDs gemappt, 25 Patches definiert,
                     10 Harte Constraints, 9 OE-Watch-Items, MVP-Scope,
                     Hypothesenregister, 5-Modelle-Verwechslungsschutz,
                     System×Ebenen×Phase Mapping, Sprach-Regeln, Ausführungsplan
```

---

> **IC_BRIDGE.md v1.0 | 26. Februar 2026 | Übersetzungs-Index KERN → Cursor-Workspace**
> 
> Dieses Dokument ist die Brücke. Wenn du im Cursor arbeitest und eine konzeptionelle Frage hast: schau hier nach. Wenn die Antwort hier nicht steht: schau ins KERN (Leitdokument v5.1 oder Fundament v06).
