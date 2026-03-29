# IC Extraktion — 25. Feb 2026 Chat 2 — Chunk 4/5

> **Scope:** Delta-Analyse (39 Items) + User-Korrekturen + Dokumenten-Hierarchie-Klärung

---

## META

| Feld | Wert |
|------|------|
| Quelle | Delta-Analyse-Dokument + anschließende Diskussion, 25. Feb 2026, 12:35–13:26 |
| Typ | EVALUATION + KLÄRUNG |
| Strategie | C — Chunk 4/5 |
| Kürzel | KC25 |

---

## SCHICHT A — SUBSTANZ

---

### A-KC25-35: Delta-Analyse — 39 Konzepte systematisch geprüft
**Inhalt:** Ergebnis: 14 bereits enthalten (✅), 11 NEU (🆕), 3 Abweichungen (⚠️), 11 Vertiefungen (🔬). Die 85% Bestätigungsrate zeigt: Das Leitdokument v2/v3 enthält den Großteil der explorativen Erkenntnisse bereits implizit. Die 15% Neues sind architektur-relevant.
**Tag(s):** [EVALUATION]
**Reifegrad:** ARGUMENTATION
**Beziehung:** EVALUATION Exploration vs. Leitdokument
**Ziel-Bereich:** Konsolidierungs-Methodik
**Herkunft:** ARTEFAKT (Delta-Analyse-Dokument)

---

### A-KC25-36: 3 neue Entscheidungsvorschläge (E-31/32/33)
**Inhalt:** E-31: System-Kernfrage pro System (HD=Wie, BaZi=Was/Wann, etc.) in Kap. VII. E-32: Analyse-Reihenfolge ≠ Vermittlungs-Reihenfolge als explizites Prinzip. E-33: 3-Gruppen-Taxonomie der Systembeziehungen (gleiche Linse / Komplementarität / vertikale Erweiterung).
**Tag(s):** [ENTSCHEIDUNG] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zum Leitdokument
**Ziel-Bereich:** Leitdokument v4
**Herkunft:** ARTEFAKT (Delta-Analyse-Dokument)

---

### A-KC25-37: 3 neue offene Entscheidungen (OE-13/14/15)
**Inhalt:** OE-13: Enneagramm-Rolle — Brücke oder aufwerten? Empfehlung: Hybrid (technisch Klasse C, philosophisch tiefer). OE-14: Kapitel "Was wir NICHT abdecken"? Empfehlung: Ja, mit 8 fehlenden Layern. OE-15: 7-Ebenen-Perspektiv-Modell als eigenständiges Konzept? Empfehlung: Ja, klar abgegrenzt (Ebenen ≠ Phasen).
**Tag(s):** [ENTSCHEIDUNG] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** ERGÄNZUNG zum Leitdokument OE-Register
**Ziel-Bereich:** Leitdokument v4
**Herkunft:** ARTEFAKT (Delta-Analyse-Dokument)

---

### A-KC25-38: Dynamics-Differenzierung — Tabelle reicht, aber PRD braucht mehr
**Inhalt:** 1 Satz im Leitdokument reicht NICHT für das App-Dokument. Pro dynamic_type braucht man: Was wird berechnet (Input), wie wird es angezeigt (UI), welche Staffel (Timeline). Definitionstabelle mit 4 Zeilen (phase_cycle, trap, growth_path, spectrum) ist Minimum. Ohne diese Tabelle bleibt Dynamics eine philosophische Aussage, die ein Entwickler nicht umsetzen kann.
**Tag(s):** [CODE-KONZEPT-GAP] [ARCHITEKTUR]
**Reifegrad:** ARGUMENTATION
**Beziehung:** VERTIEFUNG von E-25 (Dynamics-Taxonomie)
**Ziel-Bereich:** Leitdokument E-25 → PRD → App-Leitdokument
**Herkunft:** CHAT

---

### A-KC25-39: Korrigierte Dokumenten-Hierarchie — Variante D korrekt
**Inhalt:** User korrigiert: Fundament und Leitdokument sind GLEICHRANGIG (bidirektional), nicht hierarchisch. PRD fließt NICHT ins Leitdokument (einmaliger Import war Ausnahme). KERN (Fundament ↔ Steuerung) → leitet Produkt/Vermittlung/Forschung ab. Strang 0 ist NICHT untergeordnet. Dateinamen: IC_Fundament, IC_Steuerung, IC_Produkt_Leitdokument, IC_Produkt_PRD, IC_Produkt_CodeArchitektur etc.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** KORREKTUR der KI-Hierarchie. BESTÄTIGUNG von Variante D aus Chat 1.
**Ziel-Bereich:** Dokumenten-Architektur, kern/README.md
**Herkunft:** CHAT (User-Korrektur)

---

### A-KC25-40: Reihenfolge — erst konsolidieren, dann ableiten
**Inhalt:** User: "ich glaube wir sollten jetzt erstmal weitere konzept/ideen dateien gegen leitdokument v3 abgleichen, bevor wir mit neuen dokumenten weitermachen." Logik: Wenn in Inputs noch Entscheidungen stecken die nicht im Steuerungsdokument sind, baut man auf unvollständiger Basis. Konsolidierung zuerst = Single Source of Truth wird tatsächlich vollständig, bevor abgeleitet wird.
**Tag(s):** [ARCHITEKTUR] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** METHODIK-Entscheidung
**Ziel-Bereich:** Konsolidierungs-Prozess
**Herkunft:** CHAT (User-Entscheidung)

---

### A-KC25-41: Quellenstrategie — AL = Alexander Laurent, NICHT Abstraction Layer
**Inhalt:** User korrigiert Verwechslung. Laurent-Material Policy (OE-05) ist eine rechtliche Frage, hat nichts mit der Meta-Ebene/eigener Sprache zu tun. Korrektur im v3: Quellenstrategie trennt sauber Original→Cross-Mapping→eigene Sprache. Laurent wird wie alle anderen Quellen extrahiert, mit Provenance-Tags.
**Tag(s):** [KLÄRUNG] [NAMING-EVOLUTION]
**Reifegrad:** ASSERTION
**Beziehung:** KORREKTUR einer KI-Verwechslung
**Ziel-Bereich:** Leitdokument OE-05, Kap. XIII
**Herkunft:** CHAT (User-Korrektur)

---

### A-KC25-42: Wissensquellen-Tabelle — Research Required, nicht KI-Wissen
**Inhalt:** User korrigiert: "müssen wir solche konzepte nochmal separat recherchieren und analysieren. ist ja aktuell nicht vollumfänglich und vielleicht auch nicht sauber aus deinem wissen. in hd gibt es glaube ich auch lebensphasen." KI stimmt zu: Tabelle als VORLÄUFIG markiert, OE-12 als dedizierte Domänen-Recherche aus Originalwerken registriert.
**Tag(s):** [QUALITÄTSURTEIL] [ENTSCHEIDUNG]
**Reifegrad:** ARGUMENTATION
**Beziehung:** KORREKTUR — KI-Trainingswissen ≠ Domänenwissen
**Ziel-Bereich:** Leitdokument OE-12, E-29
**Herkunft:** CHAT (User-Korrektur)

---

### A-KC25-43: Botschafter — KI-Video-Serie, nicht Influencer
**Inhalt:** User korrigiert: "ich erstelle ja auch eine serie/story mit ki video. es ist nicht nur posten von influencern oder botschaftern." Lösung in v3: Keine Cultural-Advisor-Pflicht, stattdessen E-30 Qualitätsprinzipien für KI-generierte kulturelle Darstellung.
**Tag(s):** [KLÄRUNG]
**Reifegrad:** ASSERTION
**Beziehung:** KORREKTUR des Botschafter-Konzepts
**Ziel-Bereich:** Leitdokument E-30, Kap. XI
**Herkunft:** CHAT (User-Korrektur)

---

## SCHICHT C — KI-SELBSTKORREKTUREN

---

### C-KC25-03
**Ursprüngliche Aussage:** "AL" = Abstraction Layer → Meta-Ebene entsteht erst nach Extraktion.
**Korrektur:** User: "AL = Alexander Laurent. ich glaube wir reden aneinander vorbei." KI korrigiert die Quellenstrategie-Formulierung.
**Relevanz:** HOCH — falsche Annahme hätte Quellenstrategie verzerrt

---

### C-KC25-04
**Ursprüngliche Aussage:** Wissensquellen-Tabelle (HD liefert X, BaZi liefert Y) als fertige Zuordnung.
**Korrektur:** User: "müssen wir nicht separat recherchieren?" → KI markiert Tabelle als VORLÄUFIG, registriert OE-12.
**Relevanz:** HOCH — verhindert dass KI-Trainingswissen als Domänenwissen behandelt wird

---

### C-KC25-05
**Ursprüngliche Aussage:** "Botschafter → Cultural Advisor als Requirement"
**Korrektur:** User: "da gehe ich noch nicht mit. ich erstelle eine KI-Video-Serie." → E-30 umformuliert auf Qualitätsprinzipien.
**Relevanz:** MITTEL

---

## SCHICHT D — NUTZER-KLÄRUNGSMOMENTE

---

### D-KC25-07
**Nutzer-Impuls:** "aber das prd v3 müsste nach unserem leitdokument auch nicht mehr aktuell sein" + Graph der korrekten Hierarchie
**Ergebnis:** Fundamentale Klärung: KERN = Fundament ↔ Steuerung (gleichrangig, bidirektional). Alles andere leitet daraus ab. PRD ist Unterdokument von Produkt, kein eigenständiges Steuerungsinstrument.
**Relevanz:** HOCH — korrigiert die gesamte Dokument-Ableitung

---

### D-KC25-08
**Nutzer-Impuls:** "ich glaube wir sollten jetzt erstmal weitere konzept/ideen dateien gegen leitdokument v3 abgleichen"
**Ergebnis:** Methodik-Entscheidung: Konsolidierung vollständig abschließen BEVOR neue Dokumente (PRD v4, App-Leitdokument) erstellt werden. Verhindert Rückwärts-Korrekturen.
**Relevanz:** HOCH

---

## ZUSAMMENFASSUNG CHUNK 4

| Schicht | Einträge |
|---------|----------|
| A | 9 (A-KC25-35 bis A-KC25-43) |
| C | 3 |
| D | 2 |

**Top-3 Erkenntnisse:**
1. **3 User-Korrekturen** (AL-Verwechslung, Wissensquellen unvollständig, Botschafter≠Influencer) — jede einzelne hat ein Artefakt (E-27, OE-12, E-30) im Leitdokument v3 ausgelöst
2. **Dokumenten-Hierarchie endgültig geklärt** (D-07) — Fundament ↔ Steuerung gleichrangig, bidirektional. Alles andere leitet ab. Heute im Repo als `kern/` umgesetzt.
3. **"Erst konsolidieren, dann ableiten"** (D-08) — Methodik-Entscheidung die den Rest des Chats steuert
