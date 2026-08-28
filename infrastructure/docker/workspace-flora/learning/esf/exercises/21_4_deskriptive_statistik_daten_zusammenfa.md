# Übungen — Deskriptive Statistik: Daten zusammenfassen und darstellen

---

## Übung 1 (Grundniveau)

**Zuordnung: Lagemaß und Streuungsmaß**

In der folgenden Liste sind Situationen beschrieben. Geben Sie jeweils an, welcher Lageparameter und welches Streuungsmaß geeignet ist.

a) Eine Physiotherapeutin erfasst die Gehstrecke (in Metern) bei 30 Patienten nach Knie-TEP. Das Histogramm zeigt eine symmetrische, glockenförmige Verteilung. Keine Ausreißer.

b) Eine Praxis erfasst die Therapiedauer (in Wochen) bei Patienten mit chronischem Rückenschmerz. Wenige Patienten haben extrem lange Verläufe von über 60 Wochen. Die Verteilung ist stark rechtsschief.

c) In einer Befragung wird erfasst, welche Sportart Patienten in der Freizeit bevorzugen (Fußball, Schwimmen, Radfahren, keiner). Die Antwort ist eine nominale Variable.

d) Eine Therapeutin berichtet nur die Spannweite (Range) der erfassten Schmerzwerte, ohne einen weiteren Kennwert anzugeben.

Begründen Sie jede Antwort in einem Satz.

---

## Übung 2 (Mittleres Niveau)

**Mini-Fall: Gruppenvergleich und grafische Darstellung**

Eine Studie vergleicht die Schmerz-Reduktion (Skala 0–10, metrisch) nach 8 Wochen Physiotherapie in zwei Gruppen:

- Gruppe A (Einzeltherapie, n = 20): Werte gleichmäßig verteilt, MW = 3,4, SD = 0,9
- Gruppe B (Gruppentherapie, n = 20): Mehrere Patienten mit sehr geringer Schmerzreduktion (Werte nahe 0), einige mit sehr hoher Reduktion. Median = 2,5, IQR = 3,1

Beantworten Sie folgende Teilfragen:

a) Warum wird für Gruppe A der Mittelwert und die Standardabweichung berichtet, für Gruppe B dagegen Median und IQR? Begründen Sie mit Bezug auf die Verteilungsform.

b) Welche grafische Darstellung ist für den Vergleich beider Gruppen besonders geeignet, wenn man davon ausgeht, dass Gruppe B eine schiefe Verteilung aufweist? Begründen Sie kurz.

c) In der Ergebnistabelle steht für Gruppe B: MW = 2,8, SD = 2,6. Eine Kommilitonin sagt: "Dann nehmen wir einfach den Mittelwert, ist doch einfacher." Erklären Sie, warum das problematisch ist.

---

## Übung 3 (Prüfungsniveau)

**Interpretation und Kopfrechnen**

Ein Forschungsteam erfasst bei 5 Patienten mit Schulterschmerz die Anzahl der Behandlungsstunden bis zur deutlichen Besserung:

Werte: 4, 6, 6, 8, 26

a) Berechnen Sie den Mittelwert und den Median. Zeigen Sie den Rechenweg. (Taschenrechner nicht erlaubt.)

b) Welcher Wert beschreibt das typische Behandlungsvolumen dieser Gruppe besser — Mittelwert oder Median? Begründen Sie anhand Ihrer Ergebnisse.

c) Welches Streuungsmaß passt zu Ihrer Wahl in b)? Begründen Sie.

d) Das Forschungsteam möchte prüfen, ob die Daten normalverteilt sind. Die Stichprobengröße beträgt n = 5. Welcher Test ist geeignet, und warum ist das visuelle Betrachten eines Histogramms bei dieser Stichprobengröße allein nicht ausreichend?

e) Der Wert 26 wird nachträglich korrigiert: Tatsächlich handelt es sich um einen Dateneingabefehler, der korrekte Wert ist 8. Neuer Datensatz: 4, 6, 6, 8, 8. Was verändert sich bei Mittelwert und Median? Berechnen Sie den neuen Mittelwert. Was zeigt dieser Vergleich über die Robustheit des Medians?

---

## Musterlösungen

---

### Musterlösung Übung 1

**a)** Skalenniveau: metrisch, Verteilung: symmetrisch, keine Ausreißer.
Geeignet: **Mittelwert und Standardabweichung.**
Begründung: Bei symmetrischer, metrischer Verteilung ohne Ausreißer repräsentiert der MW das Zentrum der Daten zuverlässig; die SD beschreibt die Streuung um diesen MW.

**b)** Skalenniveau: metrisch, Verteilung: rechtsschief, Ausreißer vorhanden.
Geeignet: **Median und IQR.**
Begründung: Der MW wird durch die extremen Werte nach oben verzerrt; der Median berücksichtigt nur die Position der Werte und bleibt stabil, der IQR ist ebenfalls unempfindlich gegenüber Ausreißern.

**c)** Skalenniveau: nominal.
Geeignet: **Modus** (häufigste Kategorie).
Begründung: Nominale Daten lassen keine Rangreihe oder Abstände zu — einzig der Modus ist als Lageparameter sinnvoll; ein Streuungsmaß ist auf Nominalniveau nicht sinnvoll angebbar.

**d)** Die Range allein ist kein ausreichendes Streuungsmaß.
Begründung: Die Range ist extrem empfindlich gegenüber Ausreißern und gibt nur das Maximum minus Minimum an — sie enthält keine Information über die Verteilung der Werte dazwischen. Sie wird nur ergänzend, nie allein berichtet.

---

### Musterlösung Übung 2

**a)** Gruppe A zeigt eine gleichmäßige (symmetrische) Verteilung ohne ausgeprägte Ausreißer. Unter dieser Bedingung ist der MW ein unverzerrtes Maß für die Mitte der Verteilung, und die SD beschreibt die Streuung sinnvoll um diesen MW. Gruppe B weist eine schiefe Verteilung auf (viele niedrige Werte, einige sehr hohe). Hier würde der MW durch die extremen Werte nach oben verzerrt und das typische Behandlungsergebnis überzeichnen. Der Median bleibt stabil, weil er nur auf Rangpositionen basiert. Der IQR gibt den Bereich der mittleren 50 Prozent der Werte an und ist ebenfalls ausreißerresistent.

**b)** Geeignet ist der **Boxplot.** Er zeigt für jede Gruppe gleichzeitig Median, IQR, Range und Ausreißer. Gerade bei schiefer Verteilung (Gruppe B) macht der Boxplot die Asymmetrie und eventuelle Extremwerte sichtbar. Ein Histogramm wäre alternativ für eine Gruppe möglich, eignet sich aber weniger gut für den direkten Gruppenvergleich.

**c)** Die Kommilitonin liegt falsch. Eine SD von 2,6 bei einem MW von 2,8 zeigt, dass die Streuung fast so groß ist wie der MW selbst. Das ist ein deutliches Zeichen für eine schiefe Verteilung oder extreme Ausreißer. Der MW wird durch diese Extremwerte verzerrt und repräsentiert dann nicht mehr das typische Ergebnis der Mehrheit der Patienten. In diesem Fall ist der Median das ehrlichere und aussagekräftigere Lagemaß — der MW wirkt nach außen präziser, als er inhaltlich ist.

---

### Musterlösung Übung 3

**a)**

Mittelwert:
Summe = 4 + 6 + 6 + 8 + 26 = 50
MW = 50 / 5 = **10**

Median:
Werte bereits sortiert: 4, 6, **6**, 8, 26
Mittlerer Wert (Position 3) = **6**

**b)** Der **Median (6)** beschreibt das typische Behandlungsvolumen besser. Der MW von 10 liegt deutlich über den Werten von vier der fünf Patienten und wird durch den Ausreißer (26 Stunden) stark nach oben gezogen. Der Median ist unempfindlich gegenüber diesem Extremwert und spiegelt das Zentrum der Mehrheit der Beobachtungen wider.

**c)** Passendes Streuungsmaß: **IQR (Interquartilsbereich).** Da der Median als Lagemaß gewählt wurde und die Verteilung durch einen Ausreißer verzerrt ist, wird der IQR als robustes Streuungsmaß verwendet. Die SD wäre in dieser Situation ebenfalls durch den Ausreißer verzerrt und damit irreführend.

**d)** Geeignet ist der **Shapiro-Wilk-Test**, der bei kleinen Stichproben (n unter 50) eingesetzt wird, um zu prüfen, ob die Daten signifikant von der Normalverteilung abweichen. Das visuelle Betrachten eines Histogramms ist bei n = 5 allein nicht ausreichend, weil mit so wenigen Werten keine stabile Verteilungsform im Histogramm erkennbar ist — zufällige Schwankungen sehen leicht wie systematische Abweichungen aus oder umgekehrt. Eine visuelle Beurteilung ist bei kleinen Stichproben zu unzuverlässig.

**e)**

Neuer Datensatz: 4, 6, 6, 8, 8
Summe = 4 + 6 + 6 + 8 + 8 = 32
Neuer MW = 32 / 5 = **6,4**

Median: Werte sortiert: 4, 6, **6**, 8, 8 — Median bleibt **6**, unverändert.

Der Mittelwert hat sich durch die Korrektur eines einzelnen Wertes deutlich verändert (von 10 auf 6,4). Der Median blieb bei 6 stabil. Das zeigt die **Robustheit des Medians gegenüber Ausreißern**: Er reagiert nicht auf den konkreten Abstand eines Extremwertes vom Zentrum, sondern nur auf die Rangposition der Werte. Der MW hingegen berücksichtigt jeden Wert mit seinem tatsächlichen Abstand vom Mittel und ist daher empfindlich gegenüber Fehlern und Extremwerten.

---

## Häufige Fehler

**Übung 1:** Schülerinnen und Schüler wählen bei ordinalen Daten den Mittelwert. Das ist nicht korrekt — auf Ordinalniveau sind Abstände zwischen Kategorien nicht definiert, daher ist der Median das geeignete Maß. Ein weiterer häufiger Fehler: Die Range wird als vollständiges Streuungsmaß akzeptiert, ohne zu erkennen, dass sie nur zwei Extrempunkte beschreibt.

**Übung 2:** Der häufigste Fehler in Teilaufgabe c) ist, die hohe SD als "normales Merkmal großer Streuung" abzutun, ohne zu schlussfolgern, dass sie die Verwendung des Mittelwerts infrage stellt. Eine SD, die fast so groß ist wie der MW, ist ein Warnsignal für Schiefe oder Ausreißer — nicht nur ein Hinweis auf "viel Varianz".

**Übung 3:** Bei der Berechnung des Mittelwerts wird die 26 vergessen oder die Summe falsch addiert. Zudem wird in b) häufig der Mittelwert gewählt, weil er "genauer wirkt" — ohne zu berücksichtigen, dass rechnerische Genauigkeit und inhaltliche Repräsentativität zwei verschiedene Dinge sind. In d) wird der Kolmogorov-Smirnov-Test genannt — dieser ist jedoch für größere Stichproben vorgesehen. Bei n = 5 ist der Shapiro-Wilk-Test korrekt.