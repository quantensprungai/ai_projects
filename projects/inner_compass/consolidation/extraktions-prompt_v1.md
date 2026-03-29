# IC Konsolidierung — Extraktions-Prompt v1

> **Zweck:** Einheitlicher Prompt zur Extraktion von Erkenntnissen aus Chat-Transkripten
> und deren produzierten Artefakten. Zum Copy-Paste in neue Chat-Fenster.
>
> **Stand:** 28. März 2026
> **Kontext:** Entwickelt aus der Konsolidierungssession vom 25. Feb 2026

---

## Methodenbeschreibung (nicht mit in den Chat kopieren)

### Quellen-Typen
Ein Chat kann mehrere Quellen-Objekte enthalten:
- **Dialog** — die Diskussion selbst (User-Turns + KI-Turns)
- **Eingebettete Dokumente** — Volltexte, die inline gepostet wurden
- **Chat-Artefakte** — Dokumente, die die KI WÄHREND des Chats produziert hat (DOCX, MD etc.)
- **Referenz-Dokumente** — externe Docs, gegen die abgeglichen wird

### Die 6 Extraktions-Schichten
| Schicht | Was | Quelle | Wert |
|---------|-----|--------|------|
| A — Substanz | Konzepte, Modelle, Entscheidungen, Definitionen | Chat + Artefakt | Kern |
| B — End-of-Answer | Richtungen, nächste Schritte, offene Fragen am Ende jeder KI-Antwort | Nur Chat | Steuerungssignale |
| C — KI-Korrekturen | Momente wo die KI eine frühere Aussage revidiert | Nur Chat | Qualitätssicherung |
| D — Nutzer-Klärungen | Nutzer-Fragen die zu Erkenntnissprüngen führten | Nur Chat | Verborgene Konzepte |
| E — Synthese-Überschuss | Was im Artefakt steht, aber nie besprochen wurde | Nur Artefakt | Verlorenes Wissen |
| F — Delta Artefakt↔Referenz | Wo das Artefakt von Input-Docs abweicht | Artefakt vs. Referenz | Drift-Erkennung |

### Verarbeitungs-Strategien
- **A**: Quelle ist kurz/fokussiert → ein Durchlauf, alle Schichten
- **B**: Quelle hat 2-3 klare Themenstränge → pro Thema ein Durchlauf
- **C**: Quelle ist lang/dicht → in N Chunks aufteilen, je Chunk ein Durchlauf

### Workflow
1. Prompt unten kopieren
2. Unter `QUELLE:` den Chat-Text einfügen
3. Falls Chat-Artefakte existieren: unter `ARTEFAKT:` einfügen
4. Falls Referenz-Docs für Delta-Analyse: unter `REFERENZ-DOCS:` einfügen
5. In neues Chat-Fenster pasten → Ergebnis als MD speichern nach `consolidation/`

---

## Prompt (ab hier kopieren)

````markdown
Du bist ein Wissensarchitekt für das Inner Compass (IC) Projekt.
Deine Aufgabe: Klassifiziere und extrahiere alle destillationswürdigen
Erkenntnisse aus der folgenden Quelle. Sei präzise, vollständig und strukturiert.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHRITT 1 — KLASSIFIKATION (kurz, vor der Extraktion)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Beantworte zuerst diese 5 Punkte:
1. Typ: KONSTRUKTION / EVALUATION / VERTIEFUNG / KLÄRUNG / MIXED
2. Länge: kurz / mittel / lang
3. Hauptthemen: 2–4 Stichworte
4. Strategie: A (ein Durchlauf) / B (welche Themen?) / C (wie viele Chunks?)
5. Besonderheiten:
   - CHAT-ONLY Material vorhanden? (Konzepte die NUR hier existieren)
   - Naming-Evolution erkennbar? (Begriffe die sich im Verlauf ändern)
   - End-of-Answer-Direktiven erkennbar?
   - Chat-Artefakte produziert? (DOCX, MD, Code etc. die während des Chats generiert wurden)

Falls Strategie = C: Führe die Extraktion chunk-weise durch.
Falls ein ARTEFAKT mitgeliefert wird: Schichten E+F zusätzlich extrahieren.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHRITT 2 — EXTRAKTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

META
────
Quelle:        [Name / Datei / Chat-Datum]
Typ:           [aus Schritt 1]
Strategie:     [aus Schritt 1]
Chunk:         [z.B. 1/3, oder "komplett"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHICHT A — SUBSTANZ (Chat + Artefakt)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extrahiere: Konzepte, Modelle, Entscheidungen, Argumente,
            Definitionen, Strukturen, Ableitungen, Schemata.

Für jeden Eintrag:
---
ID:            A-[Quelle-Kürzel]-[lfd. Nr.]
Inhalt:        [1–3 Sätze, Kernaussage]
Tag(s):        [ARCHITEKTUR] / [ENTSCHEIDUNG] / [VERWORFEN] / [RISIKO] /
               [CODE-KONZEPT-GAP] / [LÜCKE] / [NAMING-EVOLUTION] /
               [QUALITÄTSURTEIL] / [SCHEMA]
Reifegrad:     STUB / ASSERTION / ARGUMENTATION / IMPLEMENTIERT
Beziehung:     VERTIEFUNG / ERGÄNZUNG / WIDERSPRUCH /
               NAMING-EVOLUTION / SUPERSEDES zu [Konzept/Kapitel]
Ziel-Bereich:  [Kapitel / Thema im IC_Gesamtwerk]
Herkunft:      CHAT / ARTEFAKT / BEIDES
---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHICHT B — END-OF-ANSWER DIREKTIVEN (nur Chat)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extrahiere: Was steht am Ende jeder KI-Antwort als Richtung,
            nächster Schritt, offene Frage, Entscheidungsaufforderung?
            (Diese Signale werden oft übersehen — hohe Priorität)

Für jeden Eintrag:
---
ID:            B-[Quelle-Kürzel]-[lfd. Nr.]
Inhalt:        [Exaktes Zitat oder enge Paraphrase]
Typ:           RICHTUNG / NÄCHSTER-SCHRITT / OFFENE-FRAGE /
               ENTSCHEIDUNG / DOKUMENT-ANFORDERUNG / BINÄRE-WEICHE
Reifegrad:     STUB / ASSERTION / ARGUMENTATION
Befolgt?:      JA / NEIN / TEILWEISE / UNKLAR
---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHICHT C — KI-SELBSTKORREKTUREN (nur Chat)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extrahiere: Momente wo die KI eine frühere Aussage revidiert,
            zurücknimmt oder präzisiert. Hochwertig!

Für jeden Eintrag:
---
ID:            C-[Quelle-Kürzel]-[lfd. Nr.]
Ursprüngliche Aussage: [kurz]
Korrektur:             [kurz]
Grund / Trigger:       [was hat die Korrektur ausgelöst?]
Relevanz:              HOCH / MITTEL / NIEDRIG
---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHICHT D — NUTZER-KLÄRUNGSMOMENTE (nur Chat)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extrahiere: Momente wo eine Nutzer-Frage oder -Präzisierung
            zu einem Erkenntnissprung geführt hat.
            (Oft verbirgt sich hier das eigentliche Konzept)

Für jeden Eintrag:
---
ID:            D-[Quelle-Kürzel]-[lfd. Nr.]
Nutzer-Impuls: [Frage / Einwurf / Präzisierung]
Ergebnis:      [was hat sich dadurch geklärt?]
Relevanz:      HOCH / MITTEL / NIEDRIG
---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHICHT E — SYNTHESE-ÜBERSCHUSS (nur wenn Artefakt vorhanden)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extrahiere: Was steht im produzierten Artefakt, das NICHT in der
            Chat-Diskussion vorkommt? Die KI hat beim Generieren
            des Dokuments Inhalte synthetisiert, die nie besprochen wurden.

Für jeden Eintrag:
---
ID:            E-[Quelle-Kürzel]-[lfd. Nr.]
Inhalt:        [Was wurde hinzugefügt?]
Typ:           SCHEMA / TABELLE / HYPOTHESE / DEFINITION / MAPPING /
               FEATURE-DETAIL / PRIORISIERUNG
Qualität:      WERTVOLL / PLAUSIBEL / FRAGWÜRDIG / PRÜFUNGSBEDARF
Im Ist-Stand?: JA (in aktuellem KERN) / NEIN (verloren) / TEILWEISE / UNKLAR
---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCHICHT F — DELTA: ARTEFAKT vs. REFERENZ-DOCS (nur wenn beides vorhanden)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Extrahiere: Wo weicht das produzierte Artefakt von den
            Input-Dokumenten ab — bewusst oder unbewusst?

Für jeden Eintrag:
---
ID:            F-[Quelle-Kürzel]-[lfd. Nr.]
Referenz-Doc:  [welches Dokument]
Stelle:        [Abschnitt / Entscheidung / Konzept]
Art:           BEWUSSTE-ÄNDERUNG / UNBEWUSSTE-DRIFT / WIDERSPRUCH /
               AUSLASSUNG / NEUINTERPRETATION
Inhalt:        [was genau weicht ab?]
Relevanz:      HOCH / MITTEL / NIEDRIG
---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ZUSAMMENFASSUNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Einträge gesamt:   A: _  B: _  C: _  D: _  E: _  F: _
Top-3 Erkenntnisse (eine Zeile je):
  1.
  2.
  3.
Kritischste Verluste (was existiert nur hier und nirgendwo sonst?):
  1.
  2.
  3.
Offene Punkte / Empfehlung für nächsten Chunk:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

QUELLE:
[Chat-Text hier einfügen]

ARTEFAKT (falls vorhanden):
[Produziertes Dokument hier einfügen — DOCX-Text, generiertes MD etc.]

REFERENZ-DOCS (falls Delta-Analyse gewünscht):
[Input-Dokumente hier einfügen — PRD, Master, Strang 0 etc.]
````

---

## Versions-Log

| Version | Datum | Änderung |
|---------|-------|----------|
| v1 | 28.03.2026 | Initiale Version. Prompt 1 (Klassifikation) + Prompt 2 (Extraktion) zusammengeführt. Schichten E+F (Synthese-Überschuss, Delta) hinzugefügt. Basierend auf Erkenntnissen aus Konsolidierungs-Chat 25. Feb. |
