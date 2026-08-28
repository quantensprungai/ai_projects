# 4. Deskriptive Statistik: Daten zusammenfassen und darstellen

# 4. Deskriptive Statistik: Daten zusammenfassen und darstellen

---

## Kurz erklärt

Deskriptive Statistik beschreibt Daten, ohne Schlussfolgerungen auf eine größere Population zu ziehen. Man fasst eine Datenmenge so zusammen, dass sie übersichtlich und lesbar wird. Dafür verwendet man Lagemaße (wo liegt das Zentrum der Daten?) und Streuungsmaße (wie weit streuen die Werte um dieses Zentrum?). Welches Maß man wählt, hängt vom Skalenniveau der Variable und davon ab, ob die Daten symmetrisch oder schief verteilt sind. Lagemaß und passendes Streuungsmaß werden immer gemeinsam angegeben — ein Wert allein ist wenig aussagekräftig.

---

## PT-Beispiel

Eine Physiotherapiepraxis erfasst bei 9 Patienten mit akutem Rückenschmerz die Schmerzintensität auf einer Skala von 0 bis 10:

Werte: 3, 4, 4, 5, 5, 5, 6, 7, 9

Mittelwert (MW): Summe = 48, geteilt durch 9 = ca. 5,3

Median (Md): Werte der Grosse nach sortiert (hier bereits sortiert), mittlerer Wert (Position 5) = 5

Nun kommt ein chronischer Patient dazu mit Wert 10. Neuer Datensatz (n=10): 3, 4, 4, 5, 5, 5, 6, 7, 9, 10.

MW: Summe = 58, geteilt durch 10 = 5,8 — der MW steigt spürbar.

Md: Mittelwert aus Position 5 und 6 = (5+5)/2 = 5 — der Median bleibt stabil.

Fazit: Bei einer kleinen Stichprobe mit einem Ausreißer (chronischer Patient, Wert 10) beschreibt der Median das typische Schmerzniveau der Gruppe besser als der Mittelwert.

Für die Streuung: Range = 10 - 3 = 7. Der IQR (Q3 minus Q1) würde den Bereich der mittleren 50 Prozent der Werte abbilden und ist weniger empfindlich gegenüber diesem Ausreißer.

---

## Für die Prüfung

### Lagemaße: Übersicht und Anwendung

| Maß | Berechnung | Skalenniveau | Wann verwenden |
|---|---|---|---|
| Mittelwert (MW) | Summe aller Werte / Anzahl der Werte | Metrisch | Symmetrische Verteilung, keine Ausreißer |
| Median (Md) | Mittlerer Wert nach Sortierung | Mindestens ordinal | Schiefe Verteilung, Ausreißer vorhanden |
| Modus | Häufigster Wert | Nominal und höher | Kategoriale Daten, grobe Orientierung |

Wichtig: Bei gerader Anzahl von Werten wird der Median als Mittelwert der beiden mittleren Werte berechnet.

---

### Streuungsmaße: Übersicht und Anwendung

| Maß | Berechnung | Wann verwenden | Empfindlich gegen Ausreißer? |
|---|---|---|---|
| Standardabweichung (SD) | Wurzel der Varianz | Metrisch, symmetrische Verteilung, zusammen mit MW | Ja |
| Interquartilsbereich (IQR) | Q3 minus Q1 | Schiefe Verteilung, zusammen mit Median | Nein |
| Range (Spannweite) | Maximum minus Minimum | Nur ergänzend, nie allein | Ja, stark |
| Varianz | Durchschnittliche quadrierte Abweichung vom MW | Grundlage für SD, selten allein berichtet | Ja |

---

### Zuordnung: Geschwisterpaare

Diese Kombinationen gehören zusammen und werden gemeinsam angegeben:

- Symmetrische Verteilung (Normalverteilung): MW und SD
- Schiefe Verteilung oder Ausreißer: Median und IQR
- Range niemals allein als einziges Streuungsmaß

---

### Häufigkeitsverteilungen

- Absolute Häufigkeit: Anzahl, wie oft ein Wert vorkommt
- Relative Häufigkeit: Absolute Häufigkeit geteilt durch n (Stichprobengrösse)
- Prozentuale Häufigkeit: Relative Häufigkeit mal 100
- Kumulierte Häufigkeit: Sukzessive Addition der relativen oder prozentualen Häufigkeiten — Aussage: wie viele Werte liegen bis zu einer bestimmten Kategorie vor

---

### Normalverteilung: Merkmale und Beurteilung

Merkmale einer Normalverteilung:

- Symmetrisch, glockenförmig
- MW, Median und Modus fallen zusammen
- Die meisten Werte liegen in der Mitte, wenige an den Rändern

Visuelle Beurteilung:

- Histogramm: Zeigt die Form der Verteilung. Symmetrische Glockenform spricht für Normalverteilung.
- Q-Q-Plot: Punkte liegen auf einer Geraden bei Normalverteilung.
- Boxplot: Geeignet bei schiefen Verteilungen, macht Ausreißer sichtbar.

Abweichungen von der Normalverteilung:

- Schiefe (Skewness): Verteilung ist nach links oder rechts verzerrt. Typisch bei klinischen Daten, z.B. Schmerzdauer mit wenigen sehr langen Verläufen.
- Kurtosis: Verteilung ist entweder zu spitz (leptokurtisch) oder zu flach (platykurtisch) im Vergleich zur Normalverteilung.

Statistische Prüfung bei kleinen Stichproben (n unter 50): Shapiro-Wilk-Test. Bei größeren Stichproben: Kolmogorov-Smirnov-Test. Beide prüfen, ob die Daten signifikant von der Normalverteilung abweichen.

---

### Skalenniveau und Wahl des Verfahrens

| Skalenniveau | Geeigneter Lageparameter | Geeignetes Streuungsmaß |
|---|---|---|
| Nominal | Modus | Keine sinnvolle Angabe |
| Ordinal | Median | IQR, Range |
| Metrisch (symmetrisch) | MW | SD |
| Metrisch (schief / Ausreißer) | Median | IQR |

---

### Grafische Darstellungen

- Histogramm: Metrische Daten, zeigt Häufigkeitsverteilung und Form (Normalverteilung erkennbar)
- Balkendiagramm: Nominale oder ordinale Daten
- Boxplot: Zeigt Median, IQR, Range und Ausreißer — geeignet bei schiefen Verteilungen und Gruppenvergleichen

---

## Vertiefung

### Prüfungsfallen konkret

**MW versus Median bei Ausreißern**

Bei einer Stichprobe mit wenigen extremen Werten (z.B. Schmerzdauer: die meisten Patienten haben akuten Schmerz, wenige chronische Fälle mit sehr langen Dauern) wird der MW nach oben verzerrt. Der Median bleibt stabil, weil er nur die Position, nicht den Abstand der Werte berücksichtigt. Prüfungsrelevant: Wenn eine Verteilung als schief beschrieben wird oder Ausreißer erwähnt werden, ist Median und IQR die richtige Antwort.

**SD ohne MW sinnlos**

Die SD beschreibt die durchschnittliche Abweichung der Messwerte vom MW. Ohne MW fehlt der Bezugspunkt. Beide Maße werden bei symmetrischen, metrischen Daten zusammen angegeben.

**Normalverteilung vorausgesetzt, aber nicht geprüft**

Das visuelle Betrachten eines Histogramms allein reicht nicht aus, um Normalverteilung zu bestätigen. Bei kleinen Stichproben (n unter 50) ist die visuelle Beurteilung unsicher. Zusätzlich sollte der Shapiro-Wilk-Test eingesetzt werden. Viele statistische Tests (z.B. Pearson-Korrelation, t-Test) setzen Normalverteilung voraus — wird diese nicht geprüft, sind die Ergebnisse möglicherweise nicht interpretierbar.

---

### Kurzregel für die Prüfung

Frage: Welcher Lageparameter und welches Streuungsmaß sind geeignet?

Schritt 1: Skalenniveau bestimmen.
Schritt 2: Verteilungsform prüfen (symmetrisch oder schief, Ausreißer?).
Schritt 3: Paar wählen — MW plus SD bei Normalverteilung, Median plus IQR bei Abweichung.
Schritt 4: Darstellungsform wählen — Histogramm bei symmetrischen Daten, Boxplot bei schiefen Verteilungen.