# 3 ÜBUNGSAUFGABEN: DER EMPIRISCHE FORSCHUNGSPROZESS
## Steigende Schwierigkeit | Prüfungsnah

---

## **ÜBUNG 1 – ZUORDNUNG (EINSTIEG)**

### Aufgabenstellung
Ordne die folgenden Aussagen den richtigen Kategorien zu. Schreib die **Nummer** neben die Kategorie.

| # | Aussage |
|---|---------|
| 1 | „Wenn Menschen mit Angststörungen ein achtsamkeitsbasiertes Training absolvieren, dann sinkt ihre Angst messbar" |
| 2 | „Patienten mögen die Therapie wahrscheinlich"  |
| 3 | „Steigende Bildung → bessere Gesundheitskompetenz" |
| 4 | „Vielleicht funktioniert die neue Behandlungsmethode" |
| 5 | „Je höher der BMI, desto höher das Diabetes-Risiko" |
| 6 | „Ich habe eine gute Intuition über Therapieerfolg" |

**Zielkategorien:**  
- A) Wissenschaftliche Hypothese (erfüllt die Anforderungen)  
- B) Unbrauchbar als Hypothese (zu vage, nicht empirisch testbar)

---

### **Musterlösung Übung 1**

| Kategorie | Nummern | Begründung |
|-----------|---------|-----------|
| **A) Wiss. Hypothese** | 1, 3, 5 | Alle haben Wenn-dann-Form (bzw. Je-desto), sind falsifizierbar, operationalisierbar |
| **B) Unbrauchbar** | 2, 4, 6 | 2 = zu vage (was ist „mögen"?), 4 = „vielleicht" nicht falsifizierbar, 6 = nicht empirisch (Intuition) |

**Details:**
- **1:** Konditionalsatz ✓, Angststörung messbar ✓, Achtsamkeit operationalisierbar ✓
- **3:** Je-desto-Form = gute Konditionalisierung
- **5:** Direkte Dosis-Wirkungs-Beziehung, klar testbar
- **2:** Was ist „mögen"? Auf Likert-Skala? Mit wem verglichen? Zu unscharf.
- **4:** „Vielleicht" macht nicht falsifizierbar — Hypothese darf nicht selbst unsicher sein
- **6:** Intuition ist nicht intersubjektiv nachprüfbar → unwissenschaftlich

---

### ⚠️ **Häufiger Fehler**
**Fehler:** „Aussage 2 ist eine Hypothese, weil sie eine Aussage über die Zukunft macht"  
**Richtig:** Eine Hypothese muss im *Konditionalsatz* ausgedrückt sein und operationalisiert sein.  
Besser wäre: „*Wenn* Patienten die Therapie verstehen, *dann* mögen sie sie mehr" — aber auch dann: „mögen" braucht Operationalisierung (Zufriedenheitsskala 0–10).

---

---

## **ÜBUNG 2 – MINI-FALL MIT INTERPRETATION (MITTELSTUFE)**

### Aufgabenstellung
**Szenario:**  
Ein Krankenhaus führt eine Studie durch: 150 Patient:innen mit Schlafstörungen werden randomisiert in zwei Gruppen eingeteilt.
- **Gruppe A (n=75):** Schlafhygiene-Workshop + kognitiv-behaviorale Therapie
- **Gruppe B (n=75):** Wartelisten-Kontrollgruppe (Standard-Care)

Nach 8 Wochen:
- **Gruppe A:** 62 von 75 (82,7%) berichten normalen Schlaf (Fragebogen)
- **Gruppe B:** 41 von 75 (54,7%) berichten normalen Schlaf

**p-Wert: 0,003**

---

### **Fragen**

**2a) Formuliere H₀ und H₁ für diese Studie (wissenschaftliche + statistische Form)**

**2b) Interpretiere den p-Wert von 0,003 in einfachen Worten — was bedeutet er?**

**2c) Welche der folgenden Aussagen ist WAHR? (Mehrfachauswahl möglich)**

- [ ] „Die Studie beweist, dass die KVT wirksam ist"
- [ ] „Es gibt zu 99,7% Gewissheit, dass die KVT in der Grundgesamtheit wirkt"
- [ ] „Wenn die Behandlung in Wirklichkeit nicht hilft, ist die Wahrscheinlichkeit für ein so extremes Ergebnis nur 0,3%"
- [ ] „Wir lehnen H₀ ab und nehmen H₁ an"
- [ ] „Die Unterschiede zwischen A und B könnten Zufall sein"

**2d) Nenne einen Grund, warum diese Studie trotz niedrigem p-Wert noch problematisch sein könnte** (Tipp: Design, Sample, Messung)

---

### **Musterlösung Übung 2**

#### **2a) Hypothesen**

| Form | H₀ | H₁ |
|------|----|----|
| **Wissenschaftlich** | KVT + Schlafhygiene führt zu keiner Verbesserung der Schlafqualität *in der Grundgesamtheit* | KVT + Schlafhygiene führt zu verbesserter Schlafqualität *in der Grundgesamtheit* |
| **Statistisch** | μ_A = μ_B (Mittelwerte sind gleich) | μ_A > μ_B (Mittelwert A größer) |

---

#### **2b) Interpretation p = 0,003**

**Kurz:** Die Wahrscheinlichkeit, dass ein solch großer Unterschied (28%-Punkte) *rein durch Zufall* entsteht, wenn in Wirklichkeit beide Gruppen gleich gut schlafen, liegt bei 0,3%.

**Länger (prüfungsgerecht):**  
Unter der Annahme, dass H₀ wahr ist (KVT hilft nicht), würde man ein so extremes Ergebnis nur in 0,3 von 100 wiederholten Studien erwarten. Das ist unwahrscheinlich genug, um H₀ zu verwerfen.

**NICHT sagen:**
- ❌ „Es gibt 99,7% Chance, dass die Therapie wirkt"
- ❌ „Die Therapie wirkt mit 99,7% Sicherheit"  
  (Das ist eine Wahrscheinlichkeit über Parameterwert, nicht über Alternativhypothese!)

---

#### **2c) WAHR/FALSCH**

| Aussage | Antwort | Begründung |
|---------|--------|-----------|
| „Studie beweist, dass KVT wirksam ist" | ❌ FALSCH | Empirische Studien beweisen nicht, sie zeigen Evidenz. H₀ wird verworfen, aber H₁ könnte trotzdem falsch sein (Fehler 2. Art). Replikation nötig. |
| „99,7% Gewissheit, dass KVT in GG wirkt" | ❌ FALSCH | p-Wert ist NOT die Wahrscheinlichkeit der Hypothese. Der p-Wert beantwortet: „Wie wahrscheinlich das Ergebnis unter H₀?" — nicht „wie wahrscheinlich H₁?" |
| „Wenn KVT nicht hilft, nur 0,3% Wahrscheinlichkeit für so extremes Ergebnis" | ✅ WAHR | Das ist die korrekte Definition des p-Werts. |
| „Wir lehnen H₀ ab und nehmen H₁ an" | ✅ WAHR (mit Vorsicht) | Bei p < 0,05 ist das das Standard-Vorgehen. Aber: Nicht „annehmen" = „als wahr behaupten", eher „vorläufig unterstützt durch Daten". |
| „Unterschiede könnten Zufall sein" | ❌ FALSCH | Mit p = 0,003 ist Zufall sehr unwahrscheinlich gemacht worden. Falsch zu sagen: „Es könnten Zufall sein" (würde p > 0,05 bedeuten). *Aber*: Andere Fehlerquellen (Bias) sind nicht ausgeschlossen! |

---

#### **2d) Kritische Punkte trotz p = 0,003**

**Mögliche Antworten (Auswahl einer):**

1. **Placebo-/Erwartungseffekt:**  
   Gruppe A weiß, dass sie Therapie erhält → könnte sich besser fühlen ohne echte Schlafverbesserung (Fragebogen misst Selbstbericht, nicht objektiv). → Verbesserung könnte Bias sein.

2. **Fehlende Verblindung:**  
   Wenn Therapeut:in und Patient:in nicht verblindet sind (fast unmöglich bei psychologischer Intervention), entsteht Verzerrung.

3. **Drop-out/Attrition:**  
   Aussage nicht klar: Sind alle 150 bis Ende dabei? Wer bricht ab? Selektive Drop-outs in Kontrollgruppe würden Effekt überschätzen.

4. **Operationalisierung:**  
   „Normaler Schlaf" definiert nur über Fragebogen (PSQI, subjektive Einschätzung?) — nicht über objektive Maße (Polysomnographie). Menschen unterschätzen/überschätzen Schlaf.

5. **Zeitliche Stabilität:**  
   8 Wochen Beobachtung — ist der Effekt noch da nach 6 Monaten?

**Prüfungs-Antwort (kurz):**  
*„Die Schlafqualität wurde nur per Fragebogen gemessen (Selbstbericht), nicht objektiv. Das ermöglicht Erwartungseffekte. Zusätzlich: Fehlende oder unklare Verblindung."*

---

### ⚠️ **Häufige Fehler**

| Fehler | Richtig |
|--------|---------|
| „p = 0,003 bedeutet 99,7% Wahrscheinlichkeit, dass die Therapie wirkt" | p-Wert ist Wahrscheinlichkeit des *Ergebnisses unter H₀*, nicht Wahrscheinlichkeit von H₁ |
| „Die Studie beweist die Wirksamkeit" | Empirische Studien beweisen nicht, sie liefern Evidenz |
| „Ein niedriger p-Wert schließt Bias aus" | Nein! p-Wert ist nur ein statistisches Maß. Bias (z.B. Placebo, falsche Messung) kann trotzdem vorhanden sein |
| „Mit p = 0,003 können wir Unterschied nicht erklären" | Falsch: *Weil* p so niedrig ist, können wir Zufall ausschließen — aber nicht andere Erklärungen (Bias, Placebo) |

---

---

## **ÜBUNG 3 – FALLINTEGRATION + METHODISCHE LOGIK (SCHWER)**

### Aufgabenstellung

**Szenario:**  
Ein Forschungsteam in einer Rehabilitationsklinik fragt:  
*„Wie erleben Patient:innen mit chronischen Rückenschmerzen die Kombination aus Physiotherapie und psychologischer Begleitung?"*

Sie entschließen sich zu einer **qualitativen Studie**:
- 12 Patient:innen mit chronischen Rückenschmerzen (6–36 Monate Dauer)
- Leitfaden-Interviews à 45–60 Minuten, audio-aufgezeichnet
- Offene Fragen wie: „Beschreiben Sie einen typischen Tag mit Ihren Schmerzen. Wie hat sich das durch die Therapie verändert?"
- Thematische Kodierung der Transkripte (induktiv)
- Ziel: Aussagekräftige Themenbereiche (z.B. „Akzeptanz vs. Kampf", „Hoffnung")

---

### **Fragen**

**3a) Warum hat das Team sich für einen *qualitativen* Ansatz entschieden und nicht für ein RCT mit Fragebögen? Nenne zwei Gründe.**

**3b) Was bedeutet „induktive Analyse" hier konkret? Wie unterscheidet sich die Forschungslogik von der quantitativen Studie in Übung 2?**

**3c) Die Kodierung ergibt folgende Themen:**
- **Thema 1 (n=11/12):** „Therapie als Handlung statt Passivität" (Patient:innen berichten, dass Aktivität zurückzugewinnen psychologisch wichtiger war als Schmerzreduktion selbst)
- **Thema 2 (n=4/12):** „Angst vor Verschlimmerung trotz Therapie" (4 Patient:innen bleiben skeptisch, obwohl objektiv Besserung sichtbar)
- **Thema 3 (n=8/12):** „Stigma und Akzeptanz in Familie/Beruf" (Patient:innen kämpfen damit, in ihren sozialen Rollen anerkannt zu werden)

**Interpretationsaufgabe:**  
Warum kann die Häufigkeit (11/12, 4/12, 8/12) **nicht** wie in einer quantitativen Studie als „Evidenzstärke" verwendet werden? (Tipp: Sample-Logik)

**3d) Was müsste das Team berichten, damit Sie als Leser:in die **Übertragbarkeit** der Ergebnisse beurteilen können?** (3 Elemente)

**3e) Bonus-Verständnisfrage (optional):**  
Das Team hat die Interview-Leitfragen mit offenen Fragen gestellt. Warum ist das konsistent mit dem qualitativen Paradigma, würde aber in einer quantitativen Studie problematisch sein?

---

### **Musterlösung Übung 3**

#### **3a) Warum qualitativ statt quantitativ-RCT?**

**Zwei akzeptable Gründe (min. einer):**

1. **Explorative Forschungsfrage:**  
   Die Frage lautet „Wie erleben Patient:innen..." — das ist eine *Sinnverstehens*-Frage, nicht eine Test-Hypothese wie „Therapie A vs. B".  
   Qualitativ macht Sinn, wenn Du nicht weißt, welche Faktoren *relevant* sind.

2. **Komplexität sozialer/psychologischer Prozesse:**  
   Chronische Schmerzen sind biopsychosozial. Eine Likert-Skala (z.B. „Wie zufrieden sind Sie? 1–10") erfasst nicht, *warum* ein:e Patient:in trotz Schmerzen wieder arbeitet, oder *warum* Angst bleibt, obwohl es besser wird.  
   Die Tiefenbeschreibung ist das Ziel.

3. **Kleine, heterogene Stichprobe:**  
   n=12 ist zu klein für statistische Aussagen über eine Population. Aber ausreichend für intensive Analyse und Themengenerierung.

**Prüfungsantwort (kurz):**  
*„Die Forschungsfrage zielt auf Sinnverstehen und subjektive Erfahrung, nicht auf Hypothesentestung. Eine qualitative Studie ist explorativer und kann komplexe Kontexte erfassen, die ein Fragebogen nicht abbildet."*

---

#### **3b) Induktive Analyse — Unterschied zu Übung 2**

| Aspekt | Übung 2 (Quantitativ) | Übung 3 (Qualitativ) |
|--------|----------------------|----------------------|
| **Hypothese** | Vorab formuliert (H₀, H₁) | Entsteht *aus* den Daten |
| **Logik** | Deduktiv (Allgemein → Test an Stichprobe) | Induktiv (Daten → Muster → Allgemeine Aussage) |
| **Analyserichtung** | Top-down (Theorie → Messung → Auswertung) | Bottom-up (Transkript → Kodierung → Themen → Theorie) |
| **Prozess** | Standardisiert, vorher festgelegt | Zirkulär, reflektiv (Lesen → Kodieren → Re-Lesen → Verfeinern) |
| **Ergebnis** | p-Wert, Signifikanz | Themenkatalog, Sinnstrukturen |

**Konkret in Übung 3:**  
Das Team las die Interviews, las sie nochmal, und fragte sich: *„Welche Muster sehe ich? Was ist den Patient:innen wichtig?"*  
→ **Dann erst** entstanden die drei Themen.  
Das Gegenteil von Übung 2, wo die Forschungsfrage („KVT wirkt bei Schlafstörungen?") von Anfang an klar war.

---

#### **3c) Warum Häufigkeiten NICHT wie quantitativ interpretiert?**

**Kernproblem: Sample-Logik**

**Falsche Interpretation:**
- „11 von 12 (91,7%) erleben Therapie als Handlung" = „Das trifft auf ~91,7% aller Patient:innen mit chronischen Schmerzen zu"  
- Das ist nicht haltbar!

**Warum nicht?**

1. **Bewusste, nicht-zufällige Stichprobe:**  
   Die 12 Patient:innen wurden nicht zufällig aus einer Population gezogen (wie in Übung 2 per Randomisierung). Stattdessen:
   - Selbstauskunft („Ich stelle mich zum Interview zur Verfügung")
   - Möglicherweise rekrutiert an einer Klinik, die Psycho-Angebote macht
   - → Wahrscheinlich mehr zur psychologischen Verarbeitung offen als zufälliger Schnitt

2. **Kleine Stichprobe für Populationsaussagen unwirtschaftlich:**  
   n=12 ist *genug*, um tiefe Analysen zu machen und Themen zu generieren. Aber *nicht*, um die Häufigkeit in einer Population zu schätzen.

3. **Thematische Kodierung ist nicht-nomologisch:**  
   „Thema 1 tritt 11-mal auf" sagt nicht, wie häufig es bei anderen Patient:innen mit anderen Therapeut:innen in anderen Ländern auftritt.

**Richtige Interpretation:**
- „In dieser Stichprobe zeigt sich ein starkes Thema: Die Fähigkeit zur Handlung ist psychologisch zentraler als die Schmerzreduktion selbst"
- → Das ist ein **Sinnmuster**, keine Häufigkeitsangabe
- → Interessant für Theoriebildung, aber **generalisierbar nur auf Basis weiterer Forschung** (z.B. andere qualitative Studien, dann ggf. quantitativ prüfen)

**Prüfungsantwort (kurz):**  
*„Qualitative Stichproben sind typischerweise nicht-zufällig und klein. Die Häufigkeiten (11/12, 4/12) beschreiben diese Stichprobe, nicht die Grundgesamtheit. Quantitativ würde man sagen: Populationsparameter unbekannt."*

---

#### **3d) Elemente für Beurteilung der Übertragbarkeit (Transferability)**

Damit Du als Leser:in nachvollziehen kannst, auf wen/wo die Ergebnisse übertragbar sind:

1. **Kontextbeschreibung der Stichprobe:**
   - Demografika: Alter, Geschlecht, Dauer Rückenschmerz, Beruf?
   - Klinik-Kontext: Stationär/Ambulant? Art der Therapie? Therapiedauer?
   - Auswahlkriterien: Wen habtet ihr *eingeschlossen/ausgeschlossen*?
   - **Beispiel:** *„12 Patient:innen (durchschnittlich 54 Jahre, 7 Frauen, 8–24 Monate Symptome) aus ambulanter Rehabilitationsklinik für chronische Schmerzen in Deutschsprachiger Schweiz"*

2. **Therapiekontext präzisieren:**
   - Welche Phys/Psycho-Elemente genau? Von wem geleitet?
   - Therapiedauer, -intensität?
   - Theoretischer Hintergrund (z.B. KVT, Biofeedback, Achtsamkeit)?

3. **Reflexion der Forscher:innen:**
   - Wurden Annahmen/Voreinnahmen offengelegt? (z.B. „Wir erwarteten, dass Psyche wichtig ist" → muss reflektiert werden!)
   - Könnte die Stichprobe selektiv sein? (z.B. nur die motivierten Patient:innen stellen sich zum Interview)
   - Limits der Übertragbarkeit explicit benennen

**Prüfungsantwort (kurz):**  
*„(1) Detaillierte Stichprobenbeschreibung (Alter, Schmerztyp, Dauer, Setting), (2) Therapiebeschreibung (Art, Dauer, Anbieter), (3) Reflexion möglicher Selektionsbias (z.B. nur motivierte Patient:innen) und explizite Grenzen der Übertragbarkeit."*

---

#### **3e) Bonus: Offene Fragen — qualitativ sinnvoll, quantitativ problematisch**

**Warum offene Fragen im qualitativen Design funktionieren:**
- **Induktive Logik:** Du brauchst *ungefilterte* Antworten, um Muster zu entdecken
- Patient:in antwortet in eigenen Worten → reichhaltige Daten
- Therapeut:in kann nachfragen, wenn etwas unklar ist → Flexibilität
- Beispiel: „Beschreiben Sie einen Tag..." könnte zeigen, dass Hoffnung-Verlust wichtiger als Schmerz ist (vorher nicht bekannt)

**Warum offene Fragen in quantitativen Designs problematisch:**
- **Standardisierung unmöglich:** Wenn jede:r anders antwortet, kannst Du nicht vergleichen (Gruppe A vs. B)
- **Kodierung zusätzliche Fehlerquelle:** Du musst offene Antworten in numerische Codes umwandeln (z.B. „motiviert" = 1, „unmotiviert" = 0) → Interpretationsspielraum für Fehler
- **Vergleichbarkeit:** Um zwei Gruppen zu vergleichen, brauchst Du *standardisierte* Fragen, auf die alle gleich antworten (z.B. Likert-Skala)
- Beispiel aus Übung 2: Statt „Wie schlafen Sie?" (offen) → „Wie viele Stunden schlafen Sie durch? ☐ 0–2h ☐ 2–4h ☐ 4–6h ☐ >6h" (standardisiert, vergleichbar)

**Prüfungsantwort (kurz):**  
*„Qualitative Studien brauchen offene Fragen, um induktiv Muster zu entdecken. Quantitative Studien brauchen standardisierte Fragen, um Gruppen vergleichbar zu machen und Bias durch Kodierung zu minimieren."*

---

### ⚠️ **Häufige Fehler bei Übung 3**

| Fehler | Richtig |
|--------|---------|
| „Die 11 von 12 Patient:innen zeigen, dass 91,7% aller Schmerz-Patient:innen das so erleben" | Qualitative Stichproben sind nicht-repräsentativ. 11/12 ist ein Muster in *dieser* Stichprobe, nicht eine Populationsschätzung |
| „Qualitativ = weniger wissenschaftlich, weil kein p-Wert" | Falsch. Qualitativ und quantitativ sind *gleichwertige*, aber andere Paradigmen. Rigor liegt in Transparenz, Reflexion, Nachvollziehbarkeit |
| „Mit n=12 können wir keine Aussagen machen" | Falsch. n=12 ist *klein für statistische Inferenz*, aber *ausreichend für tiefe thematische Analyse* |
| „Thema 2 (n=4) ist nicht relevant, weil nur 4 es zeigen" | Falsch. In qualitativen Studien können *Minderheits*-Perspektiven wichtig sein. 4 Patient:innen, die Angst bleiben, könnte wichtiger Befund sein als nur die Erfolgsgeschichten |
| „Die Ergebnisse sind subjektiv und deshalb nicht wissenschaftlich" | Halbrichtig. Sie sind interpretativ (nicht nomologisch), aber nicht weniger wissenschaftlich, wenn die Methode transparent ist |

---

---

## **ÜBERSICHTS-CHECKLISTE FÜR ALLE AUFGABEN**

Bevor Du antwortest, prüfe:

- [ ] **Hypothese?** → Muss konditionalisiert + falsifizierbar sein
- [ ] **H₀ vs. H₁?** → H₀ ist „kein Effekt", H₁ ist „es gibt Effekt"
- [ ] **p-Wert?** → Wahrscheinlichkeit des Ergebnisses unter H₀, NICHT Wahrscheinlichkeit der Hypothese selbst
- [ ] **Quanti vs. Quali?** → Quanti testet Hypothesen, Quali generiert Hypothesen
- [ ] **Repräsentativität?** → Zufall? Randomisiert? Oder bewusst-kleine Sample?
- [ ] **Bias?** → p < 0,05 macht Zufall unwahrscheinlich, nicht Bias
- [ ] **Operationalisierung?** → Ist klar, wie die Variable gemessen wird?

---

**Viel Erfolg bei der Prüfung! 🎯**