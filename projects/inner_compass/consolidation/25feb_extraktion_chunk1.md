# IC Extraktion — 25. Feb 2026 Chat — Chunk 1/4

> **Scope:** Architektur-Grundsatz, Ist-Analyse, 5 Deltas (erste Chat-Hälfte bis Delta-Entscheidungen)

---

## META

| Feld | Wert |
|------|------|
| Quelle | Konsolidierungs-Chat, 25. Feb 2026, 10:22–10:53 |
| Typ | MIXED (Schwerpunkt KONSTRUKTION + KLÄRUNG) |
| Strategie | C — Chunk 1/4 |
| Kürzel | KON25 |

---

## SCHICHT A — SUBSTANZ

---

### A-KON25-01: Vorgehen Top-Down statt Bottom-Up
**Inhalt:** Die Empfehlung ist, von Strang 0 und Master ausgehend zu konsolidieren — nicht vom Code-Stand. Begründung: Wenn man vom Code ausgeht, invertiert man die Hierarchie und macht Implementierungsartefakte (Workarounds, schnelle Entscheidungen) zu Konzeptentscheidungen.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zu Gesamt-Konsolidierungsstrategie
**Ziel-Bereich:** Konsolidierungs-Methodik
**Herkunft:** CHAT

---

### A-KON25-02: 5-Phasen-Konsolidierungsplan
**Inhalt:** Phase 1: Strang 0 + Master schärfen → Phase 2: Verteilte Ideen konsolidieren → Phase 3: App-Strang-Leitdokument erstellen → Phase 4: Abgleich mit Code-Stand → Phase 5: Delta-Liste (Code-Anpassungen). Angepasst durch User-Realität (Code→Konzepte→Strang 0→Master war die tatsächliche Reihenfolge).
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zu Konsolidierungs-Methodik
**Ziel-Bereich:** Konsolidierungs-Methodik
**Herkunft:** CHAT

---

### A-KON25-03: Variante D — Zwei-Ebenen-Architektur
**Inhalt:** Statt 4 hierarchischen Ebenen (Master→Strang 0→1→2→3) eine 2-Ebenen-Architektur: KERN (Fundament + Leitdokument als bidirektionales Paar) und AUSSPIELUNG (App, Vermittlung, Forschung — jeweils mit Unterdokumenten). Entscheidender Unterschied: Fundament und Leitdokument sind keine Hierarchie, sondern informieren sich gegenseitig. Unter jeder Ausspielung gibt es Unter-Dokumente (PRD, Code-Architektur, UX-Specs etc.).
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** SUPERSEDES Variante A (Master über allem), Variante B (Strang 0→Master→Stränge), Variante C (Wildwuchs)
**Ziel-Bereich:** Dokumenten-Architektur (kern/README.md)
**Herkunft:** CHAT

---

### A-KON25-04: Option B Naming — Weg von "Strang"-Nummerierung
**Inhalt:** Naming-Vorschlag: Fundament (statt Strang 0), Steuerung (statt Master), Produkt (statt Strang 1), Vermittlung (statt Strang 2), Forschung (statt Strang 3). Dateinamen: IC_Fundament_v0.3, IC_Steuerung_v2.0, IC_Produkt_Leitdokument_v1.0 etc. Begründung: "Master" klingt nach Git-Branch; "Strang 0" klingt nach Programmierung, nicht nach Philosophie.
**Tag(s):** [NAMING-EVOLUTION] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** SUPERSEDES "Master Document", "Strang 0/1/2/3"
**Ziel-Bereich:** Dokumenten-Architektur, Dateibenennungen
**Herkunft:** CHAT

---

### A-KON25-05: Strang 0 ist Wurzel des Masters, nicht paralleler Strang
**Inhalt:** Strang 0 (Philosophie, Genese, Werte) ist nicht ein Output neben App und Buch — er ist das, woraus das Master-Document seine Kohärenz bezieht. Wenn er auf derselben Ebene hängt, wird er zum optionalen Anhängsel. Geändertes Graph-Modell: S0→M→S1/S2/S3 statt M→S0/S1/S2/S3.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG zu Variante D (A-KON25-03)
**Ziel-Bereich:** Strang 0 / IC_Fundament
**Herkunft:** CHAT

---

### A-KON25-06: Fehlender expliziter App-Strang (Strang 1) als Inkonsistenz
**Inhalt:** Es existiert ein PRD v3.0, aber kein Strang-1-Dokument in der gleichen Systematik wie Strang 0. Die PRD ist eine Feature-Spec, kein konzeptionelles Strang-Dokument. Empfehlung: Eigenes IC_Produkt_Leitdokument als Brücke zwischen PRD und Leitdokument erstellen.
**Tag(s):** [LÜCKE]
**Reifegrad:** ASSERTION
**Beziehung:** ERGÄNZUNG zu Dokumenten-Architektur
**Ziel-Bereich:** Strang 1 / IC_Produkt
**Herkunft:** CHAT

---

### A-KON25-07: Spannungsfelder gehören als eigenes Kapitel ins Master
**Inhalt:** Vier Kernspannungen durchziehen das Projekt: (1) Freiheit vs. Determination, (2) Synthese vs. Vereinnahmung, (3) Spiegel vs. Autorität, (4) Sich-überflüssig-machen vs. Geschäftsmodell. Diese sind keine Fehler — sie SIND das Projekt. Jeder Strang löst sie anders auf. Gehören als explizites Kapitel ins Master/Leitdokument.
**Tag(s):** [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zu IC_Leitdokument (Kap. VI Spannungsfelder in Master v2)
**Ziel-Bereich:** Leitdokument, Spannungsfelder-Kapitel
**Herkunft:** CHAT

---

### A-KON25-08: Vierter wissenschaftlicher Weg — Komparative Ontologie
**Inhalt:** Neben den drei genannten Ansätzen (Design Science, Phänomenologie, UX-Studie) fehlt ein vierter: Komparative Ontologie — formale Strukturanalyse ob Konzepte in HD, BaZi, Astrologie strukturelle Parallelen aufweisen. Das wäre Wissenschaftsgeschichte + vergleichende Anthropologie + formale Ontologie. "Das ist dein originärer Beitrag, nicht die App."
**Tag(s):** [ARCHITEKTUR] [QUALITÄTSURTEIL]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zu Strang 3 / Forschung
**Ziel-Bereich:** IC_Forschung, wissenschaftliche Rahmung
**Herkunft:** CHAT

---

### A-KON25-09: Delta 1 — 7 Phasen vs. "Kein Stufenmodell" (aufgelöst)
**Inhalt:** Alter Master v0.1 definiert 7 explizite Phasen (Hero's Journey) als DE-01. Master v2 sagt E-11: "Keine Entwicklungshierarchie". PRD: "Phasen statt Hierarchie". Auflösung: Kein Widerspruch, wenn sauber getrennt. Phasen = zeitliche Abschnitte / Arbeitsprozesse, KEINE Bewertungsstufen. Man kann jederzeit zurückspringen. Formulierungsregel: "Phasen beschreiben zeitliche Abschnitte — nie Bewertungsstufen."
**Tag(s):** [ENTSCHEIDUNG] [KLÄRUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** KLÄRUNG von Widerspruch zwischen Master v0.1 DE-01 und Master v2 E-11
**Ziel-Bereich:** Leitdokument E-15 / E-20, 7-Phasen-Modell
**Herkunft:** CHAT

---

### A-KON25-10: Delta 2 — Staffel-Zuordnung (geparkt)
**Inhalt:** Maya Tzolkin: Staffel 1 (PRD) vs. Staffel 3 (Master v2). Numerologie: Staffel 2 (PRD) vs. Staffel 3 (Master v2). Entscheidung: Geparkt als OE-08 mit drei Bewertungskriterien: Viraler Hebel × Cross-System-Wow × Story-Dramaturgie. Aktuelle Staffel-1-Auswahl (HD, BaZi, Astro, Maya) ist strategisch solide wegen 4 verschiedener Kulturkreise.
**Tag(s):** [ENTSCHEIDUNG] [RISIKO]
**Reifegrad:** ASSERTION
**Beziehung:** WIDERSPRUCH zwischen PRD v3 und Master v2
**Ziel-Bereich:** Leitdokument OE-08, Staffel-Planung
**Herkunft:** CHAT

---

### A-KON25-11: Delta 3 — Enneagramm als Brücken-System (entschieden)
**Inhalt:** Alter Master v0.1 DE-02: Enneagramm explizit ausgeschlossen (lizenziert). Master v2 E-07: Klasse C "semantische Brücke, Onboarding-Schlüssel". Entscheidung: Rein als Klasse C. Konzept ist gemeinfrei (Sufi-Wurzeln). Spezifische Tests (Riso-Hudson) sind geschützt → eigene Beschreibungen. Enneagramm wird zum Onboarding-Schlüssel weil es bei Zielgruppe (Millennials/Gen-Z) bekannter ist als HD. Flag: input_type: "self_assessment". Staffel 2 oder 3 (nicht Launch).
**Tag(s):** [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** SUPERSEDES Master v0.1 DE-02, BESTÄTIGT Master v2 E-07
**Ziel-Bereich:** Leitdokument E-16, System-Inventar
**Herkunft:** CHAT

---

### A-KON25-12: Delta 4 — Psychologischer Layer zurückholen (entschieden)
**Inhalt:** Gesamtes Kapitel VIII des alten Masters v0.1 (Psychologischer Layer: Innere Strategie, biografischer Kontext, 3 Säulen) fehlt in Gen-2-Dokumentation. Größter Verlust bei der Migration. Entscheidung: Zurückholen. Innere Strategie wird keine neue Dimension, sondern ein Ableitungs-Layer in Schicht E (Meta-Nodes). Manifestiert sich im Handbuch als Schicht 3 (Prozess).
**Tag(s):** [ENTSCHEIDUNG] [LÜCKE]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zu Leitdokument, RÜCKHOLUNG aus Master v0.1 Kap. VIII
**Ziel-Bereich:** Leitdokument E-17, Innere Strategie
**Herkunft:** CHAT

---

### A-KON25-13: Delta 5 — 10 Lebensbereiche (Differenzen identifiziert)
**Inhalt:** Alter Master v0.1 und PRD v3 haben unterschiedliche 10er-Listen. Wesentliche Differenzen: PRD hat Sexualität als eigenständig (fehlt im alten Master), dafür fehlen Emotionen/Innenwelt. Kreativität ist neu in PRD. Entscheidung: PRD-Liste als Basis, 10 bleibt die Zahl. Begründung: 10 × 36° = visuell sauber, system-agnostisch. Lebensbereiche sind Tags (life_domain), kein Schema-Constraint → flexibel erweiterbar.
**Tag(s):** [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** WIDERSPRUCH zwischen Master v0.1 und PRD v3
**Ziel-Bereich:** Leitdokument, Lebensbereiche
**Herkunft:** CHAT

---

### A-KON25-14: Bestandsaufnahme — 4 Dokumente, 2 Generationen
**Inhalt:** Systematische Einordnung: Gen 1 = Alter Master v0.1 (Juni 2025, Alles-in-einem). Gen 2 = PRD v3 + Master v2 + Strang 0 v0.3 (alle Feb 2026). Das Problem: Der alte Master war ein Alles-in-einem-Dokument, bei der Aufteilung in Gen 2 sind Ideen verloren gegangen oder unvollständig migriert.
**Tag(s):** [ARCHITEKTUR] [QUALITÄTSURTEIL]
**Reifegrad:** ARGUMENTATION
**Beziehung:** EVALUATION des Dokumentenstands
**Ziel-Bereich:** Konsolidierungs-Methodik
**Herkunft:** CHAT

---

### A-KON25-15: Kongruenz-Matrix — 6 kongruente, 5 divergente Bereiche
**Inhalt:** Kongruent ohne Handlungsbedarf: Kernfrage, Spiegel-nicht-Autorität, Graduation, KG-Architektur (5 Schichten), 15 Dimensions-Contract, Mandala=horizontal/Handbuch=vertikal, HD als Referenz-Impl. Divergent (5 Deltas): 7 Phasen vs. Stufenmodell, Staffel-Zuordnung, Enneagramm, Psychologischer Layer, 10 Lebensbereiche.
**Tag(s):** [EVALUATION]
**Reifegrad:** ARGUMENTATION
**Beziehung:** EVALUATION — Grundlage für Delta-Entscheidungen
**Ziel-Bereich:** Konsolidierungs-Methodik
**Herkunft:** CHAT

---

## SCHICHT B — END-OF-ANSWER DIREKTIVEN

---

### B-KON25-01
**Inhalt:** "Lade mir die verteilten Konzeptdateien hoch. Ich erstelle eine Konsolidierungsmatrix. Daraus bauen wir das Strang-1-App-Leitdokument."
**Typ:** DOKUMENT-ANFORDERUNG + NÄCHSTER-SCHRITT
**Reifegrad:** ASSERTION
**Befolgt?:** JA — User hat Dokumente nachgeliefert

---

### B-KON25-02
**Inhalt:** "Hast du zum Naming-Vorschlag ('Leitdokument' statt 'Master') eine Meinung?"
**Typ:** OFFENE-FRAGE
**Reifegrad:** STUB
**Befolgt?:** TEILWEISE — User stimmt zu, aber finale Naming-Entscheidung steht aus (OE-01/04)

---

### B-KON25-03
**Inhalt:** "Gib mir die PRD als erstes. Die ist der ehrlichste Anker, weil sie beschreibt, was wirklich existiert."
**Typ:** DOKUMENT-ANFORDERUNG + RICHTUNG
**Reifegrad:** ARGUMENTATION
**Befolgt?:** JA

---

### B-KON25-04
**Inhalt:** "Welche der 5 Entscheidungen können wir jetzt treffen? Und: Du hast eine Diskussion erwähnt — willst du die noch einbringen bevor wir entscheiden?"
**Typ:** ENTSCHEIDUNG + BINÄRE-WEICHE
**Reifegrad:** ASSERTION
**Befolgt?:** JA — User trifft alle 5 Deltas und liefert weitere Diskussion

---

### B-KON25-05
**Inhalt:** "Soll ich direkt das konsolidierte Leitdokument als DOCX erstellen, mit allen bisherigen Entscheidungen (E-01 bis E-14 + die fünf neuen Delta-Entscheidungen), offenen Fragen (OE-01 bis OE-08), und der neuen Struktur (Variante D / Benennung B)?"
**Typ:** NÄCHSTER-SCHRITT
**Reifegrad:** ASSERTION
**Befolgt?:** JA — Leitdokument v1 wurde generiert

---

## SCHICHT C — KI-SELBSTKORREKTUREN

---

### C-KON25-01
**Ursprüngliche Aussage:** KI skizziert 5 Kapitel für App-Journey (Ankommen, Erkennen, Konfrontation, Prozess, Sinn).
**Korrektur:** KI erkennt selbst: "Die 5 Kapitel bilden die 7 Phasen nicht vollständig ab. Phase 3 (Körper) und Phase 6 (Bewusstseinsebene) fehlen. Phase 4 (Prozess) war ein UX-Schritt, keine Tiefenschicht — ich hab zwei verschiedene Logiken vermischt."
**Grund / Trigger:** User hatte bereits 7-Phasen-Modell im Hinterkopf; KI vergleicht eigene 5er-Skizze mit dem älteren 7er-Modell.
**Relevanz:** HOCH — führt direkt zu E-20 (7 Phasen als verbindliche Architektur)

---

### C-KON25-02
**Ursprüngliche Aussage:** Strang 0 als paralleler Strang neben Strang 1/2/3.
**Korrektur:** "Strang 0 ist kein Strang — er ist das Fundament des Masters selbst. Wenn er auf derselben Ebene hängt wie App und Paper, wird er zum optionalen Anhängsel."
**Grund / Trigger:** Vergleich verschiedener Architektur-Varianten (A/B/C/D).
**Relevanz:** HOCH — führt zu Variante D (Zwei-Ebenen-Architektur)

---

## SCHICHT D — NUTZER-KLÄRUNGSMOMENTE

---

### D-KON25-01
**Nutzer-Impuls:** "das problem ist, dass ich mit der grundidee angefangen habe, dann code angefangen habe, dann die verschiedenen konzeptweiterentwicklungen und erst dann strang 0 und master aufgesetzt habe"
**Ergebnis:** Erkenntnis, dass Strang 0 und Master nachträgliche Rationalisierungen eines organisch gewachsenen Prozesses sind. Das erklärt die Widersprüche und ändert die Konsolidierungsstrategie: PRD (realer Stand) als Anker statt top-down von Strang 0.
**Relevanz:** HOCH

---

### D-KON25-02
**Nutzer-Impuls:** "lass uns auf die grüne wiese gehen" + "muss dann im jedem strang eigentlich noch tiefer gehen. also unter leitdokument strang 1 app dann prd, code docs, usw.?"
**Ergebnis:** Bestätigung der Unter-Dokument-Struktur innerhalb Variante D. Ja, unter jeder Ausspielung gibt es Unter-Dokumente. Führt zur vollständigen Architektur-Skizze.
**Relevanz:** HOCH

---

### D-KON25-03
**Nutzer-Impuls:** "ist strang eigentlich ein gutes wording hier?"
**Ergebnis:** Systematische Naming-Analyse. "Strang" suggeriert Linearität und Parallelität, "Strang 0" klingt nach Programmierung. Führt zu Option A (Strang beibehalten, Nummerierung aufgeben) und Option B (neues Wording: Fundament, Steuerung, Produkt, Vermittlung, Forschung). User wählt Option B.
**Relevanz:** HOCH

---

### D-KON25-04
**Nutzer-Impuls:** "was ist bzw sollte [master] eigentlich sein?"
**Ergebnis:** Fundamentale Klärung: Master = interne Ontologie, kein Text zum Veröffentlichen. Strukturiertes Register aller Kernkonzepte, Designentscheidungen, Hypothesen, Definitionen. Jeder Strang zieht daraus, was er braucht, in seiner Sprache.
**Relevanz:** MITTEL — war konzeptionell bereits klar, aber die explizite Formulierung ist wichtig

---

## ZUSAMMENFASSUNG CHUNK 1

| Schicht | Einträge |
|---------|----------|
| A — Substanz | 15 |
| B — End-of-Answer | 5 |
| C — KI-Korrekturen | 2 |
| D — Nutzer-Klärungen | 4 |

**Top-3 Erkenntnisse:**
1. Variante D (Zwei-Ebenen: Kern + Ausspielung) als Dokumenten-Architektur — löst das Hierarchie-Problem und ermöglicht bidirektionale Beziehung Fundament↔Leitdokument
2. 5 Deltas zwischen Dokumenten-Generationen identifiziert und entschieden — besonders die 7-Phasen-Klärung (Phasen≠Stufen) ist architektur-tragend
3. Option B Naming (Fundament/Steuerung/Produkt statt Strang 0/Master/Strang 1) — heute in kern/ tatsächlich so umgesetzt

**Weiter mit Chunk 2:** Delta-Vertiefungen (Innere Strategie 3→4 Faktoren, 11 Lebensbereiche, Emotionen-Lücke)
