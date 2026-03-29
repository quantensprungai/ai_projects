# IC Extraktion — Chat 7, Chunk 3/6: Architektur-Kern (3-Ring, 4-Fragen, Modell-Taxonomie)

> **Chunk-Scope:** 3-Ring-Mandala Architektur, 4-Fragen-Grammatik, Modell A als Interface, Pipeline vs. Inhalt, Content-Matrix (~55 statt 77), KG-Schema (ring_tag, depth_model), Decision Records DR-26 + DR-27
> **Kürzel:** AR7

---

## SCHICHT A — SUBSTANZ

---

### A-AR7-25: 3-Ring-Mandala als konzentrische Architektur
**Inhalt:** 11 flache Domänen → 3 konzentrische Ringe, gegliedert nach "Nähe zum Selbst": Kern (core) = Sinn & Richtung (1 Feld). Mitte (self_layer) = Identität, Emotionen, Körper, Geist (4 Felder). Außen (life_domain) = Beziehungen, Familie, Beruf, Gemeinschaft (4–5 Felder). Jeder Ring hat eigene Vertiefungslogik: Kern + Mitte = Modell C dominant (4 Schichten). Außen = volle 7 Phasen. Ergibt ~55 qualifizierte Inhaltszellen statt 77 Phantom-Zellen.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** IMPLEMENTIERT (in DR-2026-02-26, E-1)
**Ziel-Bereich:** IC_Gesamtwerk Kap. 8, IC_Leitdokument E-18 v2
**Herkunft:** CHAT + ARTEFAKT (DR-26)

---

### A-AR7-26: Modell A ist Interface-Schicht, nicht inhaltliches Modell
**Inhalt:** Die 5 Navigationsachsen (Landkarte/Mandala, Handbuch, Zeitlinie, Flussdiagramm, Heldenreise) sind VIEWS, nicht MODELS. Jede Achse zeigt Inhalte aus anderen Modellen: Landkarte→Domänen (INTERACTING), Handbuch→Modell C (BEING), Zeitlinie→Modell B (DOING), Flussdiagramm→KG-Bridges (D), Heldenreise→Modell B narrativ. Konsequenz: MVC-Trennung in der App. Modell A ist im Buch irrelevant (kein App-Interface). 3-Schichten-Taxonomie: Interface (A) / Pipeline (D) / Inhalt (B, C, E, F + Domänen).
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** IMPLEMENTIERT (in DR-2026-02-26, E-2)
**Ziel-Bereich:** IC_Gesamtwerk, App-Architektur
**Herkunft:** CHAT + ARTEFAKT (DR-26)

---

### A-AR7-27: 4-Fragen-Grammatik (BEING/HAVING/DOING/INTERACTING)
**Inhalt:** Max-Neefs 4 existentielle Kategorien als universelles Design-Prinzip. BEING (Wer bin ich?)→Modell E+C. HAVING (Was brauche/habe ich?)→Modell F. DOING (Was tue ich?)→Modell B+Experimente. INTERACTING (Wo lebe ich?)→Domänen/Mandala. Die 4 Fragen durchziehen ALLES: jedes Modell, jede Domäne, jede Tiefenschicht. Anwendungsregel: Jeder Content-Block muss mindestens eine der 4 Fragen adressieren. Das ist das Bindegewebe des IC.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** IMPLEMENTIERT (in DR-2026-02-26, E-3)
**Ziel-Bereich:** IC_Gesamtwerk Kap. 11 (Grammatik), alle Modelle
**Herkunft:** CHAT + ARTEFAKT (DR-26)

---

### A-AR7-28: HAVING als blinder Fleck — IC's größte konzeptuelle Lücke
**Inhalt:** Status-Analyse der 4 Perspektiven: BEING ████░ stark (Modelle C, E + Quellsysteme). DOING ████░ stark (Modell B + Phasen). INTERACTING ███░░ mittel (Domänen definiert, Mandala-Redesign ausstehend). HAVING █░░░░ schwach — nur Finanzen/Ressourcen als Domäne. HAVING umfasst viel mehr: Fähigkeiten/Skills (BaZi, HD-Kanäle), Beziehungsnetzwerke, Rituale/Praktiken, Werte/Normen, materielle Ressourcen. → Modell F wird zur HAVING-Achse.
**Tag(s):** [EVALUATION] [LÜCKE]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** IC_Gesamtwerk, Modell F
**Herkunft:** CHAT

---

### A-AR7-29: Content-Matrix — ~55 qualifizierte Zellen statt 77 Phantom-Zellen
**Inhalt:** Differenzierte Matrix: Außen-Ring (4–5 Domänen × 7 Phasen = 28–35 vollwertige Zellen). Mitte-Ring (4 Felder × 4 Schichten = 16 Vertiefungseinheiten). Kern (1 Feld × 4 Schichten = 4 Vertiefungseinheiten). GESAMT ≈ 55 statt 77. Die Phantom-Zellen (z.B. "Identität Phase 7: Weitergabe") werden eliminiert — sie waren nie sinnvoll befüllbar.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** IC_Gesamtwerk, Content-Planung
**Herkunft:** CHAT + ARTEFAKT (AU v1.0)

---

### A-AR7-30: KG-Schema Erweiterung — ring_tag + depth_model
**Inhalt:** Zwei neue Pflichtfelder: ring_tag (core | self_layer | life_domain) verortet Node im 3-Ring-Mandala. depth_model (phases | layers | both) bestimmt zulässige Vertiefungslogik. Kein Breaking Change — additiv. Bestehende Nodes erhalten ring_tag per Migrationsscript.
**Tag(s):** [SCHEMA] [ENTSCHEIDUNG]
**Reifegrad:** IMPLEMENTIERT (in AU v1.0)
**Ziel-Bereich:** KG-Schema, cursor/architecture.md
**Herkunft:** ARTEFAKT (AU v1.0)

---

### A-AR7-31: Kern im Mandala ≠ Quelle (These 1) — bewusste Unterscheidung
**Inhalt:** Der core-Ring im Mandala enthält die identitätsnächsten Lebensbereiche (Identität, Körper, Emotionen). Die Quelle (These 1 = das Prä-Existente) liegt UNTER dem gesamten Mandala — sie ist der Boden, auf dem es steht. Der Kern des Mandalas ist nicht die Quelle. Das muss im Gesamtwerk explizit gesagt werden, damit kein Missverständnis entsteht.
**Tag(s):** [KLÄRUNG] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** IC_Gesamtwerk Kap. 8 (Mandala), Kap. 2 (Thesen)
**Herkunft:** CHAT

---

### A-AR7-32: Max-Neef 4 Kategorien sind Perspektiven, NICHT Buckets
**Inhalt:** Wichtige Korrektur: Being/Having/Doing/Interacting sind bei Max-Neef keine Inhaltskategorien, in die man Dinge einsortiert. Sie sind Satisfier-TYPEN — die Art, WIE Bedürfnisse befriedigt werden. Jedes Bedürfnis existiert in allen 4 Dimensionen gleichzeitig. "Autonomie" hat eine BEING-Dimension (ich bin selbstbestimmt), eine HAVING-Dimension (ich habe Wahlfreiheit), eine DOING-Dimension (ich treffe eigene Entscheidungen), eine INTERACTING-Dimension (mein Umfeld erlaubt Selbstbestimmung). Das ist der elegante Kern von Max-Neef.
**Tag(s):** [KLÄRUNG]
**Reifegrad:** ARGUMENTATION
**Ziel-Bereich:** IC_Gesamtwerk Kap. 11 (Grammatik)
**Herkunft:** CHAT

---

### A-AR7-33: 15 Dimensionen (E-03) — primär intern, nicht user-facing
**Inhalt:** Die 15 dimension_keys (mechanical, shadow, gift, etc.) sind primär Extraktions-Kategorien und KG-Tags. Sie werden NICHT als "15 Dimensionen" user-facing präsentiert. User-seitig wirken sie als implizite Filter hinter den Kulissen (KG-Query). Ausgewählte können als "Perspektiven" im Lens-Switcher auftauchen — aber nicht alle 15, und nicht unter dem Label "Dimension". Die 4-Fragen-Grammatik ist das primäre User-facing Navigationsprinzip.
**Tag(s):** [ENTSCHEIDUNG] [KLÄRUNG]
**Reifegrad:** IMPLEMENTIERT (in DR-2026-02-27, E-8)
**Ziel-Bereich:** IC_Leitdokument, cursor/contracts.md
**Herkunft:** CHAT

---

### A-AR7-34: Wund-Hierarchie über die Ebenen
**Inhalt:** Wunden ENTSTEHEN auf Ebene 4–6 (Disposition, Psychodynamik, Bewusstsein). Ebenen 1–3 (Verhalten, Energie, Körper) sind SYMPTOM-Ebenen — Ausdrucksformen von Wunden, die tiefer entstehen. Ebene 7 (Transzendent) ist der Integrationsraum — keine Wunde, sondern WOZU. Metapher: Wurzeln (4–6) = Ursprung, Blätter (1–3) = Symptome. Spezifische Zuordnung: Eb. 4→Mars-Wunde (prä-natal). Eb. 5→EG-Leidenschaft + Fixierung. Eb. 6→Chiron-Wunde (generational). Eb. 7→Inkarnationskreuz (Integration).
**Tag(s):** [ARCHITEKTUR] [SCHEMA]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zu DR-27/E6 (Kernverletzung)
**Ziel-Bereich:** IC_Gesamtwerk Kap. 5 (Prisma)
**Herkunft:** CHAT

---

## SCHICHT D — NUTZER-KLÄRUNGSMOMENTE

---

### D-AR7-07
**Nutzer-Impuls:** "aber das prd3 ist doch auch teil des cursor codes/projekts als reference. dh. wir sollten das nicht updaten"
**Ergebnis:** Korrekt — PRD v3 wird archiviert. Kein neues PRD. Die BRIDGE + aktualisierte Cursor-Docs ersetzen es. (Bereits in Chat 5 entschieden, hier bestätigt als Kontext für die Architektur-Session.)
**Relevanz:** MITTEL — Kontextbestätigung

### D-AR7-08
**Nutzer-Impuls:** "lass uns das wirklich im detail betrachten" (zu Domänen × Ebenen × Phasen × Schichten)
**Ergebnis:** Führt zur vollständigen ontologischen Analyse: "Was IST eine Domäne — und was ist etwas anderes?" Die 3 Testkriterien entstehen. Die Erkenntnis: es fehlt eine Strukturkategorie zwischen Domänen und Dimensionen. → wird zunächst "Grundqualitäten" genannt, löst sich später in Max-Neef auf.
**Relevanz:** HOCH

---

## SCHICHT E — SYNTHESE-ÜBERSCHUSS (Artefakte)

---

### E-AR7-01: IC_Architektur-Update v1.0 (15 Seiten)
**Inhalt:** Vollständiges Konsolidierungsdokument: 3-Ring-Architektur (Abschnitt 1, 7 Unter-Punkte), Modell-Taxonomie Interface/Pipeline/Inhalt (Abschnitt 2), 4-Fragen-Grammatik mit Mapping + Status-Analyse (Abschnitt 3), Content-Matrix ~55 Zellen (Abschnitt 4), KG-Schema Impact (Abschnitt 5), 10-Item Parking Lot (Abschnitt 6), Skeleton v02 Impact-Tabelle (Abschnitt 7), 15-Zeilen Impact-Übersicht (Abschnitt 8), 7 priorisierte Schritte (Abschnitt 9), 10-Einträge Glossar (Anhang A). Nie als Ganzes im Chat durchgesprochen.
**Typ:** DOKUMENT
**Qualität:** WERTVOLL — erstes vollständig konsolidiertes Architektur-Ergebnis
**Im Ist-Stand?:** JA — als DOCX vorhanden

### E-AR7-02: IC_Decision_Record DR-2026-02-26 (5 Seiten)
**Inhalt:** 3 Entscheidungen (E-1: 3-Ring, E-2: Modell A Interface, E-3: 4-Fragen) + 4 Sonderfälle + Content-Matrix + KG-Erweiterung + 8-Item Parking Lot + Impact-Übersicht + priorisierte nächste Schritte.
**Typ:** DOKUMENT
**Qualität:** WERTVOLL
**Im Ist-Stand?:** JA — als DOCX vorhanden

### E-AR7-03: IC_Decision_Record DR-2026-02-27 (9 Seiten)
**Inhalt:** 7 Entscheidungen (E-4 bis E-10): Max-Neef bestätigt, EG↔Bedürfnis-Mapping als Hypothese, Kernverletzung in Wund-Hierarchie, Handbuch-Schichten orthogonal zu 4-Fragen, 15 Dimensionen intern, 7 Ebenen prüfen, IC-Bedürfnisliste zurückgezogen. + Aktualisierter Parking Lot + vollständige Modell-Taxonomie + Quer-Konzepte + Glossar.
**Typ:** DOKUMENT
**Qualität:** WERTVOLL
**Im Ist-Stand?:** JA — als DOCX vorhanden

---

## ZUSAMMENFASSUNG CHUNK 3

| Schicht | Einträge |
|---------|----------|
| A — Substanz | 10 |
| D — Nutzer-Klärungen | 2 |
| E — Synthese-Überschuss | 3 |
| **Gesamt** | **15** |

**Top-3 Erkenntnisse:**
1. **3-Ring-Mandala + 4-Fragen-Grammatik + Modell-Taxonomie** (A-25/26/27) — die drei Kern-Architektur-Entscheidungen dieser Session, alle in DR-26 formalisiert.
2. **HAVING als blinder Fleck** (A-28) — die wichtigste Lückendiagnose. IC konnte alles außer "Was brauchst du?" → Modell F als Antwort.
3. **Max-Neef 4 Kategorien = Perspektiven, nicht Buckets** (A-32) — kritische Klarstellung: Being/Having/Doing/Interacting sortieren nicht Dinge ein, sondern sind verschiedene Blickwinkel auf dieselben Dinge.
