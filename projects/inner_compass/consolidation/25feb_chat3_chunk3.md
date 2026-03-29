# IC Extraktion — 25. Feb 2026 Chat 3 — Chunk 3/3

> **Scope:** Artefakt-Analyse: Leitdokument v4 (Schicht E Synthese-Überschuss), v3→v4 Delta (Schicht F), v5-Empfehlung

---

## META

| Feld | Wert |
|------|------|
| Quelle | Leitdokument v4 (29 Seiten) + v3→v4 Delta-Analyse |
| Referenz | Leitdokument v3 |
| Typ | ARTEFAKT-EXTRAKTION |
| Strategie | C — Chunk 3/3 |
| Kürzel | KV25 |

---

## SCHICHT E — SYNTHESE-ÜBERSCHUSS (im v4-Artefakt, nicht im Chat besprochen)

---

### E-KV25-01: Graduation-Konzept (Kap. XIV, komplett neu)
**Inhalt:** Phase 7 in mind. 3–4 Lebensbereichen abgeschlossen → eigene Sprache entwickelt. Experimentierzyklen im Körper verankert. Widersprüche integriert. Graduation ≠ Account löschen, IC wird von Guide zu Referenz. Post-Graduation: optionale Rückkehr bei Life-Events. Graduation-Ritual: "Was hast du herausgefunden, das vorher nicht in Sprache war?"
**Typ:** KAPITEL
**Qualität:** WERTVOLL — operationalisiert E-17 (Graduation)
**Im Ist-Stand?:** UNKLAR — ob in v5.1 angekommen

---

### E-KV25-02: Lebensbereiche-Liste nochmals geändert (v4 vs. v3 vs. v2)
**Inhalt:** v4 hat wieder andere Bezeichnungen: "Körper & Gesundheit" statt "Gesundheit & Körper", "Geist & Denken" als neuer Bereich (#4), "Wachstum & Entwicklung" (#11). "Sexualität & Intimität" fehlt (war in v2 als bewusste Entscheidung). "Beziehungen & Liebe" zusammengelegt (waren in v2 getrennt). Das ist die dritte verschiedene Liste in drei Versionen — nie explizit besprochen.
**Typ:** DEFINITION
**Qualität:** PRÜFUNGSBEDARF — drei verschiedene Listen in drei Versionen, keine davon explizit entschieden
**Im Ist-Stand?:** UNKLAR — v5.1 hat möglicherweise eine vierte Variante

---

### E-KV25-03: Widerspruchs-Protokoll (Kap. XII) — 4-Schritte komplett
**Inhalt:** Zeigen → Einordnen ("verschiedene Ebenen, kein Fehler") → Einladen ("welches fühlt sich wahrer an?") → Markieren (KG-Edge: contradicts + confidence). Mit Muster-Sprache. Im Chat wurde nur das Prinzip besprochen, die 4-Schritte-Ausarbeitung mit Sprachbeispielen ist Synthese.
**Typ:** FEATURE-DETAIL
**Qualität:** WERTVOLL — direkt als UX-Spec verwendbar
**Im Ist-Stand?:** UNKLAR

---

### E-KV25-04: 5-Modelle-Tabelle (IV.1 — Abgrenzung)
**Inhalt:** Tabelle: A=5 Achsen (Raum/App-UI), B=7 Phasen (Zeit/Journey), C=4 Handbuch-Schichten (Tiefe/Inhalt), D=KG-Pipeline (außen→innen/Technisch), E=7 Ebenen (keine Richtung/Fundament). Im Chat wurden die 5 Modelle besprochen, aber die kompakte Tabelle mit Kernfrage×Richtung×Verortung ist Synthese.
**Typ:** TABELLE
**Qualität:** WERTVOLL — beste Orientierungshilfe im gesamten Projekt
**Im Ist-Stand?:** UNKLAR

---

## SCHICHT F — DELTA: v4 vs. v3

---

### F-KV25-01: 5 kritische Verluste v3→v4 (systematisch)
**Referenz-Doc:** Leitdokument v3 vs. v4
**Art:** BEWUSSTE ANALYSE (Delta-Dokument produziert)
**Inhalt:** (1) Phasen-Ton + App-Trigger (v3 Kap. IV → fehlt in v4). (2) Domäne×Phase Matrix 11×7 (v3 IV.1 → fehlt komplett). (3) inner_strategy factor_scores Schema (v3 E-27 → fehlt). (4) Story/Release-Architektur + E-30 Qualitätsprinzipien (v3 Kap. XI → fehlt komplett). (5) Drei-Sprachebenen-Tabelle mit Beispielen (v3 Kap. XII → umstrukturiert, Beispiele verloren).
**Relevanz:** HOCH — alle 5 sind operativ relevante Verluste

---

### F-KV25-02: v5-Empfehlung mit konkretem Changelog
**Referenz-Doc:** Delta-Analyse
**Art:** EMPFEHLUNG
**Inhalt:** v5 = v4 (Basis, E-01–E-40) + 5 wiederhergestellte v3-Blöcke + Mapping-Tabelle + neue Erkenntnisse. Vorgeschlagene neue Entscheidungen: E-41 Phasen-Ton+Trigger, E-42 Domäne×Phase Matrix, E-43 inner_strategy Schema, E-44 Story/Release + E-30, E-45 Wording konsolidiert. Anhang A: System×Ebenen Mapping v1.0.
**Relevanz:** HOCH — definiert den Pfad zu v5

---

### F-KV25-03: Lebensbereiche-Drift (dritte Version ohne Diskussion)
**Referenz-Doc:** v2→v3→v4 Lebensbereiche-Listen
**Art:** UNBEWUSSTE-DRIFT
**Inhalt:** Jede Version hat andere Bezeichnungen und teilweise andere Bereiche. "Sexualität & Intimität" (v2 bewusst entschieden) → in v3 zu "Transformation & Wachstum" → in v4 "Wachstum & Entwicklung". "Geist & Denken" erscheint in v4 neu. Drei Versionen, drei Listen, keine explizit besprochen.
**Relevanz:** HOCH — grundlegendes Navigations-Element der App instabil

---

### F-KV25-04: Kanal-Dualität 4-Felder NICHT in v4/v5 integriert
**Referenz-Doc:** Chat-Diskussion vs. Leitdokument v4
**Art:** AUSLASSUNG
**Inhalt:** Die Kanal-Dualität (1a/1b/2a/2b) wurde im Chat ausführlich analysiert und als "eigenständige konzeptuelle Leistung" und "perfektes Phase-3-Feature" bewertet. Sie ist weder im Leitdokument v4 noch in der v5-Empfehlung aufgenommen. Verortung laut Chat: IC_Fundament Annex + Phase-3-Vertiefung.
**Relevanz:** MITTEL — wertvolles Konzept, aber nicht architektur-kritisch

---

## ZUSAMMENFASSUNG CHUNK 3

| Schicht | Einträge |
|---------|----------|
| E — Synthese-Überschuss | 4 |
| F — Delta v4↔v3 | 4 |

**Top-3 Erkenntnisse:**
1. **5 kritische v3→v4 Verluste** (F-01) — systematisch dokumentiert, v5-Pfad definiert mit E-41–E-45
2. **Lebensbereiche-Drift** (F-03) — drei verschiedene Listen in drei Versionen, keine davon explizit entschieden. Das grundlegendste Navigations-Element der App ist instabil.
3. **Kanal-Dualität nicht aufgenommen** (F-04) — wertvolles Konzept das durch die Dokument-Iterationen durchgerutscht ist
