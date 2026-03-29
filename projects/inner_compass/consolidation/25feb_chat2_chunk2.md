# IC Extraktion — 25. Feb 2026 Chat 2 — Chunk 2/5

> **Scope:** Deep Review des Leitdokuments v2 (nur intern) — Struktur-Kritik + 5 konzeptionelle Probleme

---

## META

| Feld | Wert |
|------|------|
| Quelle | Konsistenz-Chat 2, 25. Feb 2026, 12:18 |
| Typ | EVALUATION (intern) |
| Strategie | C — Chunk 2/5 |
| Kürzel | KC25 |

---

## SCHICHT A — SUBSTANZ

---

### A-KC25-09: Struktur-Kritik — Kap. XI (Story/Release) ist Fremdkörper
**Inhalt:** Kapitel XI mischt Produktarchitektur (formal-nüchtern) mit fiktiven Figuren (Aria, Jian, etc.). Im Leitdokument als Ontologie-Instanz hat das nichts verloren. Empfehlung: Ins Leitdokument gehört nur "E-23: 3-Schicht-Release. Details in Strang 1/2."
**Tag(s):** [QUALITÄTSURTEIL] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** EVALUATION der Dokumentstruktur
**Ziel-Bereich:** Leitdokument Kap. XI
**Herkunft:** CHAT

---

### A-KC25-10: Struktur-Kritik — Kap. XIV (AQAL) ist isolierter Appendix
**Inhalt:** AQAL-Kapitel steht isoliert und verweist auf Lücken, die in anderen Kapiteln bereits gelöst werden. Empfehlung: In die Architektur integrieren oder ganz raus.
**Tag(s):** [QUALITÄTSURTEIL]
**Reifegrad:** ASSERTION
**Beziehung:** EVALUATION der Dokumentstruktur
**Ziel-Bereich:** Leitdokument Kap. XIV
**Herkunft:** CHAT

---

### A-KC25-11: Struktur-Kritik — Feature-Map (Kap. XIX) gehört nicht ins Leitdokument
**Inhalt:** Feature-Map mit Sprint-Details ist Strang-1-Inhalt, nicht Ontologie. Leitdokument sollte nur Prinzipien definieren, nicht Sprint-Planung.
**Tag(s):** [QUALITÄTSURTEIL]
**Reifegrad:** ARGUMENTATION
**Beziehung:** EVALUATION der Dokumentstruktur
**Ziel-Bereich:** Leitdokument Kap. XIX → Strang 1
**Herkunft:** CHAT

---

### A-KC25-12: Konzeptproblem 1 — Innere Strategie ist pseudo-quantitativ
**Inhalt:** factor_scores wie signature: 0.4, conditioning: 0.2 etc. erwecken Eindruck quantitativer Präzision, wo keine existiert. Niemand erklärt woher die Gewichte kommen. Widerspricht dem eigenen Prinzip "Hypothesen, nie Festlegungen". Ist das einzige Element das wie ein diagnostisches Instrument klingt — genau das was das Dokument ablehnt. Empfehlung: Numerische Scores rausnehmen oder als rein illustrativ kennzeichnen, Default = narrative Synthese.
**Tag(s):** [RISIKO] [QUALITÄTSURTEIL]
**Reifegrad:** ARGUMENTATION
**Beziehung:** WIDERSPRUCH zu eigener Ethik (E-11 "Hypothesen, nie Festlegungen")
**Ziel-Bereich:** Leitdokument E-19/E-27, Innere Strategie
**Herkunft:** CHAT

---

### A-KC25-13: Konzeptproblem 2 — Scope-Explosion (5×11×7×15×4×4+)
**Inhalt:** 5 Achsen × 11 Lebensbereiche × 7 Phasen × 15 Dimensionen × 4 Dynamiken × 4+ Systeme = gigantischer theoretischer Raum. Kein Prioritäts-Mechanismus dafür, was der User zuerst sieht. Heldenreise ist der Versuch, aber optional (Phase 2). Ohne verpflichtende Führung wird User von Landkarte erschlagen. Empfehlung: Für MVP eine Achse als Default (Heldenreise ODER Landkarte), Rest als Progressive Disclosure.
**Tag(s):** [RISIKO] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG — fehlendes "Was wir NICHT bauen"-Kapitel
**Ziel-Bereich:** Leitdokument, MVP-Scope
**Herkunft:** CHAT

---

### A-KC25-14: Konzeptproblem 3 — Resonanz-These auf Drahtseil
**Inhalt:** "Die Frage ist nicht: Stimmt das? Sondern: Klingt das wahr genug?" ist intellektuell redlich, aber untergräbt potenziell die eigene Konvergenz-These. Wenn Systeme nur durch Resonanz wirken (nicht Wahrheit), dann ist Konvergenz kein Muster in der Realität, sondern nur menschliche Bestätigungstendenz. Das Dokument tanzt auf diesem Drahtseil ohne sich zu entscheiden. Empfehlung: Kein Bug sondern Feature — aber im Wording vorsichtig handhaben. Schmaler UX-Korridor: User muss gleichzeitig staunen UND skeptisch bleiben.
**Tag(s):** [RISIKO] [QUALITÄTSURTEIL]
**Reifegrad:** ARGUMENTATION
**Beziehung:** SPANNUNG zwischen Resonanz-These und Konvergenz-These
**Ziel-Bereich:** Leitdokument II.1, Ethik, Wording
**Herkunft:** CHAT

---

### A-KC25-15: Konzeptproblem 4 — Graduation vs. Geschäftsmodell strukturell ungelöst
**Inhalt:** OE-02 (Monetarisierung) steht als "Priorität: Mittel". Das ist zu niedrig. Wenn Kernprinzip "Erfolg = User braucht uns weniger", dann ist Monetarisierung existenziell. Ohne tragfähiges Modell wird Graduation unter wirtschaftlichem Druck gekippt. Empfehlung: OE-02 auf Hoch. Mögliche Modelle: Einmaliges Lebens-Handbuch (Kauf statt Abo), Community-Beiträge, Staffel-Unlock als Kaufmodell.
**Tag(s):** [RISIKO] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** SPANNUNG im Spannungsfeld "Graduation vs. Geschäftsmodell"
**Ziel-Bereich:** Leitdokument OE-02/OE-07, Monetarisierung
**Herkunft:** CHAT

---

### A-KC25-16: Konzeptproblem 5 — Botschafter-Figuren Cultural Appropriation Risiko
**Inhalt:** KI-generierte Figuren aus 5 Kulturen die "live posten" — bei eigenem Ethik-Prinzip "kultureller Respekt, nie aneignend". Eine KI-generierte ghanaische Figur namens "Amara" die Akan-Weisheit repräsentiert (von westlichem Produkt) ist exakt was Cultural Appropriation-Kritiker angreifen. Empfehlung: Echte Community-Vertreter einbinden ODER Figuren als explizit fiktiv/archetypisch framen ohne reale Kulturkreis-Verknüpfung.
**Tag(s):** [RISIKO]
**Reifegrad:** ARGUMENTATION
**Beziehung:** WIDERSPRUCH zu E-30 (kultureller Respekt)
**Ziel-Bereich:** Leitdokument Kap. XI, Story-Architektur
**Herkunft:** CHAT

---

### A-KC25-17: Gesamturteil — "intellektuell überzeugend, operativ überladen"
**Inhalt:** Bewertungsmatrix: Philosophisches Fundament ✅, Ethischer Rahmen ✅, Architektur-Tiefe ✅, Konvergenz-USP ✅, MVP-Realisierbarkeit 🔴, Monetarisierung 🔴, Cultural Sensitivity ⚠️, Innere Strategie ⚠️, Scope-Kontrolle 🔴. Gefährlichstes Muster: "Alles ist optional, alles ist erweiterbar, alles koexistiert" — klingt elegant, aber niemand weiß was der MVP wirklich ist.
**Tag(s):** [QUALITÄTSURTEIL]
**Reifegrad:** ARGUMENTATION
**Beziehung:** EVALUATION des Gesamtkonzepts
**Ziel-Bereich:** Leitdokument, Gesamtbewertung
**Herkunft:** CHAT

---

### A-KC25-18: Fehlende Kapitel — "Was wir NICHT bauen"
**Inhalt:** Im Leitdokument fehlt ein explizites Kapitel das beschreibt, was NICHT gebaut wird und warum. Das wäre das wichtigste Kapitel gegen Scope Creep.
**Tag(s):** [LÜCKE] [ARCHITEKTUR]
**Reifegrad:** ASSERTION
**Beziehung:** ERGÄNZUNG zum Leitdokument
**Ziel-Bereich:** Leitdokument (neues Kapitel)
**Herkunft:** CHAT

---

## SCHICHT C — KI-SELBSTKORREKTUREN

---

### C-KC25-01
**Ursprüngliche Aussage:** KI kritisiert Scope als MVP-Problem ("Für einen MVP ist das potenziell zu viel").
**Korrektur:** User stellt klar: "das ist auch kein mvp sondern die gesamtvision". KI akzeptiert: Das Leitdokument IST die Gesamtvision, die stückweise gebaut wird.
**Grund / Trigger:** User-Korrektur
**Relevanz:** HOCH — verhindert falsche MVP-Scope-Schnitte

---

## SCHICHT D — NUTZER-KLÄRUNGSMOMENTE

---

### D-KC25-03
**Nutzer-Impuls:** "bevor wir die von dir erkannten punkte angehen, habe ich noch einen langen diskussionsstrang, den ich mit dir beleuchten möchte"
**Ergebnis:** Statt sofort das Leitdokument zu fixen, wird erst ein umfangreicher explorativer Input (HD-Mechanik, Systemvergleiche) gegen das Leitdokument abgeglichen. Das verhindert, dass Fixes gemacht werden, die der explorative Input obsolet machen würde.
**Relevanz:** HOCH — korrekte Reihenfolge (Input vollständig → dann fixen)

---

## ZUSAMMENFASSUNG CHUNK 2

| Schicht | Einträge |
|---------|----------|
| A | 10 (A-KC25-09 bis A-KC25-18) |
| C | 1 |
| D | 1 |

**Top-3 Erkenntnisse:**
1. **Innere Strategie pseudo-quantitativ** (A-12) — der schärfste konzeptionelle Einwand. factor_scores widersprechen dem eigenen Ethik-Prinzip. Führt direkt zu E-27 in v3.
2. **"Was wir NICHT bauen" fehlt** (A-18) — wichtigstes fehlendes Kapitel für Scope-Kontrolle
3. **Resonanz-These vs. Konvergenz-These** (A-14) — das philosophische Drahtseil des Projekts. Nicht lösbar, aber muss bewusst navigiert werden.
