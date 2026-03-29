# IC Extraktion — 25. Feb 2026 Chat 2 — Gesamtzusammenfassung

> **Quelle:** Konsistenz-Check + Deep Review + System-Exploration + Delta-Analyse + Leitdokument v3 Artefakt
> **Extrahiert:** 28. März 2026 | 5 Chunks | 6 Schichten (A–F)

---

## Zählung

| Schicht | Einträge | Beschreibung |
|---------|----------|-------------|
| A — Substanz | 43 | Konzepte, Entscheidungen, Evaluationen, Korrekturen |
| B — End-of-Answer | 1 | Steuerungssignal |
| C — KI-Korrekturen | 5 | Revisionen (3 User-getrieben, 2 KI-intern) |
| D — Nutzer-Klärungen | 8 | User-Impulse mit Richtungswechseln |
| E — Synthese-Überschuss | 7 | Artefakt-Inhalte ohne Chat-Diskussion |
| F — Delta Artefakt↔Referenz | 5 | Abweichungen v3↔v2 |
| **Gesamt** | **69** | |

---

## Top-10 Erkenntnisse (priorisiert nach Auswirkung)

### 1. 7-Ebenen-Perspektiv-Modell ≠ 7 Phasen (A-25)
Zwei verschiedene 7er-Strukturen! Perspektiv-Ebenen = WAS existiert (Ontologie des Menschen), Phasen = WIE der User es durchläuft (Journey). Diese Unterscheidung fehlt in allen aktuellen Docs.

### 2. 3-Gruppen-Taxonomie der Systembeziehungen (A-27)
Systeme sind nicht alle "gleich verschieden": (1) gleiche Linse/anderer Code (Astro↔Jyotish ~80%), (2) andere Linse/echte Komplementarität (HD↔BaZi ~20%), (3) vertikale Erweiterung (Gene Keys→HD). Fehlt komplett im Leitdokument.

### 3. System-Kernfragen (A-28)
HD=Wie, BaZi=Was/Wann, Jyotish=Wozu, Maya=Welche Welle, Gene Keys=Wohin. In einem Satz pro System wird die Staffel-Dramaturgie greifbar.

### 4. Analyse≠Vermittlung (A-29)
Pipeline arbeitet außen→innen (A→E), UX arbeitet innen→außen (Bestätigung→Tiefe). Dieses Prinzip fehlt im Leitdokument und ist architektur-tragend.

### 5. Innere Strategie pseudo-quantitativ (A-12)
factor_scores widersprechen dem eigenen Ethik-Prinzip "Hypothesen, nie Festlegungen". Führt direkt zu E-27 (experimental markiert) in v3.

### 6. 8 fehlende Layer geburtsbasierter Systeme (A-24)
Epigenetik, Bindung, Trauma, Kultur, Transgenerational, Bewusstseinsstufen, Freier Wille, Relationale Emergenz. Kein System deckt das ab. Gehört als ehrliches Grenzen-Kapitel ins IC_Fundament.

### 7. Resonanz vs. Konvergenz Drahtseil (A-14)
Wenn Systeme "nur durch Resonanz" wirken, ist Konvergenz kein reales Muster sondern Bestätigungstendenz. Das Projekt tanzt auf diesem Drahtseil. Kein Bug — aber muss bewusst navigiert werden.

### 8. Phasen-Umbenennung als unbewusste Drift (F-02)
Phase 4 "Disposition" (Staunen, KERNMOMENT) → "Schatten" (Konfrontation) in v3 ohne Diskussion. Signifikante Bedeutungsverschiebung. Prüfung gegen v5.1 nötig.

### 9. Schema-Erweiterungen im Artefakt (E-02, E-03)
Node-Schema mit provenance + dynamic_type und system_annotation als Node-Typ — direkt implementierbar, nie besprochen.

### 10. "Erst konsolidieren, dann ableiten" (D-08)
User-Methodik-Entscheidung: Alle Inputs abgleichen BEVOR neue Dokumente erstellt werden. Verhindert Rückwärts-Korrekturen.

---

## Kritischste Verluste / Unbewusste Drifts

| # | Was | Wo | Status |
|---|-----|-----|--------|
| 1 | Phase 4 "Disposition" → "Schatten" | Leitdokument v3 Kap. IV | UNBEWUSSTE DRIFT — prüfen gegen v5.1 |
| 2 | "Sexualität & Intimität" verschwunden | Leitdokument v3 Kap. IX | UNBEWUSSTE DRIFT — war bewusste Chat-1-Entscheidung |
| 3 | Edge-Typ "expresses_as" entfernt | Leitdokument v3 Kap. X.3 | UNBEWUSSTE DRIFT — war in v2 |
| 4 | "Was wir NICHT bauen/abdecken" | Nirgends | LÜCKE — fehlt in allen Versionen |
| 5 | OE-13/14/15 (aus Delta-Analyse) | Nur im Delta-Dokument | UNKLAR ob in v3 eingegangen |

---

## Naming-Evolutionen

| Schritt | Vorher | Nachher | Auslöser | Qualität |
|---------|--------|---------|----------|----------|
| 1 | Phase 1 "Ankommen" | "Erkennen" | KI-Synthese v3 | ⚠️ Nie besprochen |
| 2 | Phase 4 "Disposition" | "Schatten" | KI-Synthese v3 | 🔴 Bedeutungsverschiebung |
| 3 | Phase 5 "Konfrontation" | "Navigation" | KI-Synthese v3 | ⚠️ Nie besprochen |
| 4 | "Sexualität & Intimität" | "Transformation & Wachstum" | KI-Synthese v3 | 🔴 Verlust eines Bereichs |
| 5 | Botschafter "Luka/Amara" | "Kwame/Sofia" | KI-Synthese v3 | MITTEL |
| 6 | OE-02 "Monetarisierung" Mittel | → Hoch empfohlen | Deep Review | WERTVOLL |

---

## Offene Prüfpunkte (gegen IC_Leitdokument v5.1 abgleichen)

- [ ] Phase-4-Name: "Disposition", "Schatten" oder etwas anderes in v5.1?
- [ ] Lebensbereiche: Ist "Sexualität & Intimität" in v5.1 vorhanden?
- [ ] Sind E-31/32/33 (System-Kernfragen, Analyse≠Vermittlung, 3-Gruppen-Taxonomie) in v5.1?
- [ ] Sind OE-13/14/15 in v5.1 aufgenommen?
- [ ] Gibt es ein "Grenzen"-Kapitel im IC_Fundament v06?
- [ ] Sind die Node-Schema-Erweiterungen (dynamic_type, provenance) im Code?
- [ ] Gibt es system_annotation als Node-Typ?
- [ ] Status Edge-Typ "expresses_as" — noch vorhanden oder entfernt?
- [ ] Ist das 7-Ebenen-Perspektiv-Modell irgendwo dokumentiert?

---

## Dateien dieser Extraktion (Chat 2)

| Datei | Inhalt |
|-------|--------|
| `25feb_chat2_klassifikation.md` | Klassifikation (5 Punkte) |
| `25feb_chat2_chunk1.md` | Konsistenz-Check + 6 Inkonsistenzen |
| `25feb_chat2_chunk2.md` | Deep Review (5 konzeptionelle Probleme) |
| `25feb_chat2_chunk3.md` | Explorative Diskussion (HD/Systeme/7-Ebenen) |
| `25feb_chat2_chunk4.md` | Delta-Analyse (39 Items) + Korrekturen |
| `25feb_chat2_chunk5.md` | Leitdokument v3 Artefakt (Schicht E+F) |
| `25feb_chat2_zusammenfassung.md` | Diese Datei |

---

## Vergleich Chat 1 vs. Chat 2

| Metrik | Chat 1 | Chat 2 |
|--------|--------|--------|
| Einträge gesamt | 84 | 69 |
| Chunks | 4 | 5 |
| Artefakte | 1 (Leitdokument v2) | 2 (Leitdokument v3 + Delta-Analyse) |
| Unbewusste Drifts (Schicht F) | 1 (E-Nummern-Umnummerierung) | 3 (Phasen, Lebensbereiche, Edge-Typen) |
| User-Korrekturen (Schicht D) | 9 | 8 |
| KI-Korrekturen (Schicht C) | 4 | 5 |
| Substanz-Einträge (Schicht A) | 46 | 43 |

**Beobachtung:** Chat 2 hat MEHR unbewusste Drifts (Schicht F) als Chat 1. Das deutet darauf hin, dass die KI beim Generieren von v3 mehr "eigenmächtige" Änderungen vorgenommen hat als bei v2. Die Phasen-Umbenennung und die Lebensbereiche-Änderung sind die kritischsten — sie betreffen Kern-Architektur-Elemente.
