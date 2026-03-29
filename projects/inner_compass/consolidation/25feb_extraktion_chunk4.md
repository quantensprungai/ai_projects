# IC Extraktion — 25. Feb 2026 Chat — Chunk 4/4

> **Scope:** Leitdokument v2.0 (Chat-Artefakt, 20 Seiten) — Schicht E (Synthese-Überschuss: was steht im Dokument, das nie besprochen wurde?) + Schicht F (Delta gegen Referenz-Docs PRD v3, Master v2, Strang 0 v0.3)

---

## META

| Feld | Wert |
|------|------|
| Quelle | Leitdokument v2.0 (DOCX, produziert 25. Feb 2026) |
| Referenz-Docs | PRD v3, Master v2, Strang 0 v0.3 |
| Typ | ARTEFAKT-EXTRAKTION |
| Strategie | C — Chunk 4/4 |
| Kürzel | KON25 |

---

## SCHICHT E — SYNTHESE-ÜBERSCHUSS (nur im Artefakt, nie im Chat besprochen)

---

### E-KON25-01: inner_strategy JSON-Schema
**Inhalt:** Leitdokument Kap. VI enthält ein vollständiges Schema für Innere Strategie: `{ contributing_nodes: [], factor_scores: { signature: 0.4, conditioning: 0.2, transit: 0.1, affect: 0.2, consciousness: 0.1 }, synthesis_text: "", recommended_experiments: [] }`. Im Chat wurde nur das 4-Faktoren-Konzept besprochen, nie ein konkretes Schema mit Gewichtungen.
**Typ:** SCHEMA
**Qualität:** PLAUSIBEL — Gewichtungen (0.4/0.2 etc.) sind Platzhalter, keine begründeten Werte
**Im Ist-Stand?:** TEILWEISE — E-19 existiert in IC_Leitdokument v5.1, aber Schema-Details unklar

---

### E-KON25-02: Affect-Tracking Schema-Felder
**Inhalt:** `affect_valence (float, -1 bis +1)`, `affect_arousal (float, 0 bis 1)`, `emotion_tags (text[])`, `confidence (float)`, `timestamp`. Im Chat war nur die Entscheidung "opt-in, Default aus" (E-22). Die konkreten Felder sind KI-Synthese basierend auf Russell's Circumplex Model of Affect.
**Typ:** SCHEMA
**Qualität:** WERTVOLL — psychologisch fundiertes Schema (Valence-Arousal-Modell ist Standardmodell)
**Im Ist-Stand?:** UNKLAR — Nicht in cursor/architecture.md oder contracts.md gefunden

---

### E-KON25-03: Feature-Map mit 17 Items, Prioritäten und Staffel-Zuordnung
**Inhalt:** Kap. XIX listet 17 Features mit Quelle, Priorität (MVP/Premium/Phase 2/Phase 3) und Staffel-Zuordnung. Darunter Features die im Chat nie einzeln besprochen wurden: #9 Agent/Begleiter (Phase 2), #11 Exploring/Archetypen-Bibliothek (Premium), #15 Affect Check-in (Phase 3, Staffel 2), #17 Daily Compass (Phase 2, Staffel 1).
**Typ:** PRIORISIERUNG
**Qualität:** WERTVOLL — erste konsolidierte Feature-Priorisierung über alle Quellen
**Im Ist-Stand?:** TEILWEISE — Feature-Liste existiert verteilt, aber nicht als priorisierte Gesamtübersicht

---

### E-KON25-04: Hypothesen H-06 bis H-10
**Inhalt:** Fünf neue Hypothesen, die im Chat nicht explizit besprochen wurden: H-06 (Enneagramm-Brücke erhöht Onboarding-Konversion), H-07 (Emotionale Domäne fördert Engagement), H-08 (Kulturübergreifende Resonanz unterbricht Bestätigungsfehler), H-09 (Empowerment > Sucht für Loyalität), H-10 (Chart + Life-Event Overlap = stärkste Aha-Momente).
**Typ:** HYPOTHESE
**Qualität:** WERTVOLL — H-08 und H-10 sind originäre Beiträge zur Forschungsfrage
**Im Ist-Stand?:** TEILWEISE — H-01–H-07 aus altem Master bekannt, H-08–H-10 sind Synthese-Ergänzungen

---

### E-KON25-05: Zwiebel-These → KG-Mapping-Tabelle
**Inhalt:** Kap. X.1 enthält explizites Mapping: Anlage/Signatur → Schicht A+B, Prägung/Konditionierung → B+D+psych.Layer, Bewusstsein → C (Prozess-Layer), Zyklus → C (temporal_phase), Innere Strategie → E (Meta-Node). Im Chat wurde die Zwiebel-These besprochen und die 4-Faktoren-Formel entwickelt, aber diese konkrete Schicht-Zuordnung zum KG ist Synthese.
**Typ:** MAPPING
**Qualität:** WERTVOLL — macht die Verbindung Philosophie↔Technik explizit
**Im Ist-Stand?:** UNKLAR — nicht in cursor/architecture.md gefunden

---

### E-KON25-06: Cross-Strand-Koordinationsmatrix
**Inhalt:** Kap. XVIII: Vollständige Matrix Leitdokument↔Strang 1↔Strang 2↔Strang 3 für 10 Bereiche (Philosophie, Systeme, Dimensionen, Lebensbereiche, Wording, Innere Strategie, 7 Phasen, Dynamik, Biografie-Layer, Story/Release). Zeigt pro Bereich, was im Leitdokument gilt und wie jeder Strang es umsetzt.
**Typ:** TABELLE
**Qualität:** WERTVOLL — einzige Stelle die Cross-Strand-Verantwortlichkeiten explizit macht
**Im Ist-Stand?:** TEILWEISE — Master v2 hat einfachere Version (Kap. V)

---

### E-KON25-07: AQAL-Lückenanalyse als Tabelle mit Lösungsstrategie
**Inhalt:** Kap. XIV: 4-Quadranten-Tabelle mit Abdeckungsgrad und konkreter Lösung pro Quadrant. ICH=stark, ES=schwach→Biografie+Experimente, WIR=ansatzweise→Relationship Mode, ES-PL=schwach→Lebensskizze. Im Chat wurde die Lücke besprochen, aber die tabellarische Lösung pro Quadrant ist Synthese.
**Typ:** TABELLE
**Qualität:** WERTVOLL — operationalisiert E-07 (AQAL als Qualitätsraster)
**Im Ist-Stand?:** UNKLAR

---

### E-KON25-08: Entscheidungsregister E-01–E-24 mit Änderbarkeits-Klassifizierung
**Inhalt:** Kap. XV enthält alle 24 Entscheidungen mit Version und Änderbarkeit ("Nicht änderbar" / "Erweiterbar" / "Timing änderbar" / "Technisch änderbar"). Besonders: E-01–E-14 aus Master v2 haben neue Nummerierung und Formulierung. Im Chat wurde über die Entscheidungen diskutiert, aber die Änderbarkeits-Klassifizierung ist Synthese.
**Typ:** PRIORISIERUNG
**Qualität:** WERTVOLL — macht Governance-Regeln für jede Entscheidung explizit
**Im Ist-Stand?:** JA — in IC_Leitdokument v5.1 weiterentwickelt (E-01 bis E-40)

---

### E-KON25-09: OE-Nummern-Neuordnung (OE-01 bis OE-11)
**Inhalt:** Die offenen Entscheidungen wurden von der Master-v2-Nummerierung (F-01 bis F-07) auf OE-01 bis OE-11 umgestellt. Neue OEs: OE-08 (Staffel-Zuordnung), OE-09 (Innere Strategie Konzeptpapier), OE-10 (fehlende Kulturkreise), OE-11 (Heldenreise-Einstiegslogik).
**Typ:** DEFINITION
**Qualität:** WERTVOLL — saubere Tracking-Nummern
**Im Ist-Stand?:** JA — in v5.1 weitergeführt

---

### E-KON25-10: Change-Log (Kap. XX)
**Inhalt:** Vollständiges Change-Log mit 14 Einträgen, datiert 25.02.2026. Dokumentiert v1.0→v2.0 Transition mit allen Quellen pro Änderung (Konsolidierung, Delta 1-5, Diskussion, Vision-Doc). Im Chat nicht besprochen — reine Synthese-Ergänzung für Governance.
**Typ:** TABELLE
**Qualität:** WERTVOLL — ermöglicht Rückverfolgbarkeit
**Im Ist-Stand?:** UNKLAR — ob Change-Log-Praxis in v5.1 beibehalten wurde

---

## SCHICHT F — DELTA: ARTEFAKT vs. REFERENZ-DOCS

---

### F-KON25-01: PRD v3 "10 Lebensbereiche" → Leitdokument "11 Lebensbereiche"
**Referenz-Doc:** PRD v3, §4
**Stelle:** Lebensbereiche
**Art:** BEWUSSTE-ÄNDERUNG
**Inhalt:** PRD hat 10 Bereiche. Leitdokument v2 hat 11 (Emotionen & Innenwelt als #2 hinzugefügt). Im Chat besprochen und entschieden (D-KON25-06).
**Relevanz:** HOCH — Schema-Impact (life_domain Enum braucht 11. Wert)

---

### F-KON25-02: PRD v3 "5 User Journey Ebenen" → Leitdokument "5 Navigationsachsen"
**Referenz-Doc:** PRD v3, §10
**Stelle:** User Journey
**Art:** NEUINTERPRETATION
**Inhalt:** PRD beschreibt 5 User-Journey-Ebenen (Spiegel→Handbuch→Zeitlinie→Prozess→Verbindung) als lineare Vertiefung. Leitdokument v2 reinterpretiert als 5 gleichberechtigte Navigationsachsen (Landkarte/Handbuch/Fluss/Zeitlinie/Heldenreise) — nicht linear sondern parallel. Besonders: "Heldenreise" und "Fluss-Diagramm" sind als eigene Achsen benannt, "Verbindung (Cross-System)" ist in alle Achsen integriert statt eigene Ebene.
**Relevanz:** HOCH — fundamentale UX-Architektur-Änderung

---

### F-KON25-03: Master v2 "E-01 bis E-14" → Leitdokument "E-01 bis E-24" (Umnummerierung)
**Referenz-Doc:** Master v2, §II
**Stelle:** Entscheidungsregister
**Art:** NEUINTERPRETATION
**Inhalt:** Master v2 hatte E-01 bis E-14 mit anderer Nummerierung (z.B. Master E-01="Spiegel nicht Autorität" → Leitdokument E-01="Drei Stränge"). Einige Master-Entscheidungen wurden zusammengelegt, andere umformuliert. Die Nummern sind NICHT kompatibel — eine Mapping-Tabelle fehlt.
**Relevanz:** HOCH — Verwirrungspotenzial bei Cross-Referenzierung

---

### F-KON25-04: Master v2 "F-01 bis F-07" → Leitdokument "OE-01 bis OE-11"
**Referenz-Doc:** Master v2, §IX
**Stelle:** Offene Fragen
**Art:** NEUINTERPRETATION
**Inhalt:** Ähnlich wie F-KON25-03: Offene Fragen wurden umnummeriert und erweitert. F-01 (Naming) → OE-01. F-02 (Graduation) → kein OE (als E-10 entschieden). F-03 bis F-07 → teilweise in OEs, teilweise als entschieden markiert.
**Relevanz:** MITTEL — Umnummerierung ist dokumentiert im Change-Log

---

### F-KON25-05: Strang 0 v0.3 "Drei Schichten" → Leitdokument "Vier Faktoren"
**Referenz-Doc:** Strang 0 v0.3, §III These 2
**Stelle:** Zwiebel-These
**Art:** BEWUSSTE-ÄNDERUNG
**Inhalt:** Strang 0 beschreibt 4 Schichten (Konditionierung, Anlage, Bewusstsein, Kern). Leitdokument v2 übersetzt das in 4 Faktoren für die Innere Strategie (Signatur, Konditionierung, Bewusstsein, Zyklus) + offener Kern. "Zyklus" ist ein NEUER Faktor der in Strang 0 nicht vorkommt — er kommt aus der Dynamik-Diskussion (E-21).
**Relevanz:** HOCH — Innere Strategie hat einen Faktor mehr als die Zwiebel-These Schichten hat

---

### F-KON25-06: PRD v3 "Schicht C: Dynamiken" → Leitdokument "4 Dynamik-Dimensionen"
**Referenz-Doc:** PRD v3, §5
**Stelle:** Datenschicht C
**Art:** BEWUSSTE-ÄNDERUNG
**Inhalt:** PRD definiert Schicht C als "Zeitliche Zyklen UND inhaltliche Prozesse (Fallen, Auswege, Experimente)". Leitdokument v2 differenziert das in 4 explizite Dynamik-Dimensionen (astronomisch, psychologisch, biographisch, prozessual). Die PRD-Definition war korrekt aber unscharf — Leitdokument schärft.
**Relevanz:** MITTEL — keine Widerspruch, aber deutlich mehr Struktur

---

### F-KON25-07: Master v2 hat keine Heldenreise / 7 Phasen
**Referenz-Doc:** Master v2
**Stelle:** Gesamtes Dokument
**Art:** AUSLASSUNG (im Master v2) / ERGÄNZUNG (im Leitdokument)
**Inhalt:** Master v2 enthält kein 7-Phasen-Modell, keine Hero's Journey, kein Phasen-Konzept. E-11 sagt explizit "Keine Entwicklungshierarchie — Zeitlinie ersetzt Stufen durch Zyklen und Phasen" — ohne zu spezifizieren WELCHE Phasen. Leitdokument v2 fügt das vollständige 7-Phasen-Modell hinzu (E-20), das aus dem alten Master v0.1 stammt.
**Relevanz:** HOCH — das 7-Phasen-Modell ist eine der wichtigsten Architektur-Entscheidungen

---

### F-KON25-08: PRD v3 "Staffel 1 = HD+BaZi+Astro+Maya" vs. Master v2 "Maya = Staffel 3"
**Referenz-Doc:** PRD v3 §11 vs. Master v2 §IV
**Stelle:** Staffel-Zuordnung
**Art:** WIDERSPRUCH (zwischen Referenz-Docs untereinander)
**Inhalt:** PRD sagt Maya = Staffel 1, Master v2 sagt Maya = Staffel 3. Leitdokument v2 übernimmt PRD-Version (Staffel 1), markiert aber OE-08 als offene Entscheidung. Der Widerspruch wird also nicht aufgelöst, sondern bewusst geparkt.
**Relevanz:** MITTEL — geparkt ist akzeptabel, aber muss vor Launch entschieden werden

---

## ZUSAMMENFASSUNG CHUNK 4

| Schicht | Einträge |
|---------|----------|
| E — Synthese-Überschuss | 10 |
| F — Delta Artefakt↔Referenz | 8 |

**Top-3 Erkenntnisse (Schicht E — Synthese):**
1. **inner_strategy Schema** (E-01) + **Affect-Tracking Felder** (E-02) — konkrete technische Schemata, die nie besprochen wurden aber implementierungsrelevant sind
2. **Feature-Map mit Priorisierung** (E-03) — einzige konsolidierte Übersicht aller 17 Features mit MVP/Premium/Phase-Zuordnung
3. **Zwiebel→KG Mapping** (E-05) — macht die Verbindung Philosophie↔Technik explizit, fehlt sonst überall

**Top-3 Erkenntnisse (Schicht F — Deltas):**
1. **Umnummerierung E-01–E-14 → E-01–E-24** (F-03) — Nummern sind NICHT kompatibel, Mapping-Tabelle fehlt, hohes Verwirrungspotenzial
2. **7-Phasen-Modell fehlt komplett in Master v2** (F-07) — wichtigste Architektur-Ergänzung des Leitdokuments v2
3. **"Zyklus" als neuer Faktor** (F-05) — kommt nicht aus der Zwiebel-These (Strang 0), sondern aus der Dynamik-Diskussion (E-21). Clever, aber die Herkunft ist nicht dokumentiert.
