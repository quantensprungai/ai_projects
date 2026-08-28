# 8. Kritische Appraisal und Interpretation von Forschungsergebnissen

# Kapitel 8: Kritisches Appraisal und Interpretation von Forschungsergebnissen

---

## Kurz erklärt

Eine Studie zu lesen bedeutet nicht, ihr zu vertrauen. Kritisches Appraisal ist das strukturierte Prüfen einer Studie auf methodische Qualität, bevor man ihre Ergebnisse in der Praxis anwendet. Dafür gibt es Checklisten wie PEDro (für RCTs in der Physiotherapie) oder CONSORT (für die Berichterstattung von RCTs), die systematisch abfragen, ob zentrale Qualitätsmerkmale erfüllt sind. Die Evidenzhierarchie zeigt, welche Studiendesigns grundsätzlich stärkere Aussagekraft haben — aber ein hohes Design-Level allein garantiert keine Qualität. Ein schlecht durchgeführter RCT kann weniger aussagekräftig sein als eine sorgfältige Kohortenstudie. Am Ende zählt nicht nur, ob ein Ergebnis statistisch signifikant ist, sondern ob es klinisch relevant und auf die eigene Patientengruppe übertragbar ist.

---

## PT-Beispiel

Eine RCT untersucht manuelle Therapie bei chronischem Kreuzschmerz: p = 0.03 zugunsten der Interventionsgruppe. Auf den ersten Blick sieht das überzeugend aus. Beim kritischen Lesen zeigt sich: n = 18 pro Gruppe, Dropout 35 %, keine verblindete Outcome-Erhebung, und der Unterschied im Schmerzwert beträgt 0,4 Punkte auf einer 10er-Skala. Der minimale klinisch relevante Unterschied (MCID) liegt bei dieser Skala bei 2 Punkten. Das Ergebnis ist statistisch signifikant, aber klinisch nicht relevant. Zusätzlich schränkt der hohe Dropout die interne Validität ein. Diese Studie rechtfertigt keine Änderung der Behandlungspraxis.

---

## Für die Prüfung

### Evidenzhierarchie (von hoch nach niedrig)

| Ebene | Studiendesign |
|---|---|
| 1 | Systematische Reviews und Meta-Analysen von RCTs |
| 2 | Einzelne RCTs |
| 3 | Nicht-randomisierte kontrollierte Studien |
| 4 | Kohortenstudien |
| 5 | Fall-Kontroll-Studien |
| 6 | Fallserien, Fallberichte |
| 7 | Expertenmeinung, Konsensus |

**Prüfungsfalle:** Level 1 oder 2 bedeutet nicht automatisch hohe Qualität. Entscheidend sind immer: Stichprobengrösse, Bias-Risiko, Dropout, Heterogenität.

---

### Checklisten: PEDro vs. CONSORT

| Merkmal | PEDro | CONSORT |
|---|---|---|
| Verwendungszweck | Bewertung der methodischen Qualität von RCTs | Leitlinie zur Berichterstattung von RCTs |
| Anwendung durch | Leser, Reviewer | Autoren beim Verfassen |
| Typische Items | Randomisierung, Verblindung, ITT-Analyse, Dropout-Bericht | Flowchart, Stichprobenkalkulation, Randomisierungsverfahren |
| Kontext PT | Direkt relevant, da auf klinische Studien zugeschnitten | Allgemein medizinisch |

---

### Kritische Lesefragen: Bias, Konfounding, Generalisierbarkeit

**Bias (systematischer Fehler):**
- Selektionsbias: Gruppen sind vor Interventionsbeginn nicht vergleichbar
- Performance-Bias: Unterschiedliche Behandlung der Gruppen ausser der Intervention selbst
- Detection-Bias: Outcome-Erhebung nicht verblindet
- Attrition-Bias: Unterschiedliche oder hohe Dropout-Raten (Faustregel: über 20 % kritisch, über 30 % meist nicht mehr akzeptabel)
- Reporting-Bias: Nur signifikante Ergebnisse werden berichtet

**Konfounding:**
- Eine dritte Variable beeinflusst sowohl die unabhängige als auch die abhängige Variable
- Beispiel: Studie zu Trainingseffekten, aber die Interventionsgruppe ist im Schnitt 10 Jahre jünger
- Kontrolle durch: Randomisierung, Matching, statistische Adjustierung

**Generalisierbarkeit (externe Validität):**
- Frage: Ist die Stichprobe repräsentativ für meine Patientengruppe?
- Prüfpunkte: Ein- und Ausschlusskriterien, Setting (Klinik vs. Praxis), Alter, Schweregrad, Komorbiditäten
- Hohe interne Validität (sauberes Design) geht oft auf Kosten der externen Validität (strenge Einschlusskriterien, die die Realität nicht abbilden)

---

### Klinische Relevanz beurteilen

| Kriterium | Frage |
|---|---|
| Statistisch signifikant | Ist p < 0.05 (oder Konfidenzintervall ohne 0/1)? |
| Klinisch relevant | Überschreitet der Effekt den MCID? |
| Stichprobengrösse | Ausreichend gepowert, oder nur zufälliger Befund? |
| Baseline-Unterschiede | Waren Gruppen vor der Intervention vergleichbar? |
| Dropout | Wie viele Teilnehmende fehlen im Endresultat? |
| Intention-to-treat | Wurden alle Randomisierten in der Auswertung behalten? |

---

## Vertiefung

### Heterogenität in Meta-Analysen

- **I²-Statistik** misst den Anteil der Varianz zwischen Studien, der nicht durch Zufall erklärt wird
- I² unter 25 %: geringe Heterogenität — Pooling sinnvoll
- I² 25–50 %: moderate Heterogenität — mit Vorsicht interpretieren
- I² über 50 %: hohe Heterogenität — gepoolter Effekt ist inhaltlich fraglich
- Ursachen hoher Heterogenität: unterschiedliche Populationen, verschiedene Interventionsformen, unterschiedliche Outcomemessung, verschiedene Follow-up-Zeiträume
- **Prüfungsfalle:** Ein niedriger p-Wert im gepoolten Effekt einer Meta-Analyse mit I² > 50 % ist kein zuverlässiges Ergebnis

---

### Intention-to-treat (ITT) vs. Per-Protocol-Analyse

| Ansatz | Beschreibung | Problem bei Weglassen |
|---|---|---|
| ITT | Alle randomisierten Personen werden ausgewertet, unabhängig von Compliance und Dropout | Ohne ITT wird Attrition-Bias unterschätzt |
| Per Protocol | Nur Personen, die die Intervention vollständig abgeschlossen haben | Systematische Verzerrung: Non-Completer oft kränker oder weniger motiviert |

---

### Interne vs. externe Validität

- **Interne Validität:** Ist der gemessene Effekt tatsächlich auf die Intervention zurückzuführen, und nicht auf Störvariablen?
- **Externe Validität:** Lässt sich das Ergebnis auf andere Populationen, Settings oder Zeitpunkte übertragen?
- Beide stehen häufig in einem Spannungsverhältnis: Je strenger kontrolliert eine Studie ist, desto weiter entfernt sie sich von der klinischen Realität

---

### Zusammenfassung: Was macht ein Ergebnis klinisch verwertbar?

- Studiendesign passend zur Forschungsfrage
- Ausreichende Stichprobengrösse mit Power-Berechnung
- Verblindung, Randomisierung, ITT-Analyse dokumentiert
- Dropout unter 20 %, begründet und symmetrisch
- Effektgrösse oberhalb des MCID
- Patientengruppe vergleichbar mit der eigenen klinischen Population
- Ergebnis repliziert oder durch weitere Studien gestützt