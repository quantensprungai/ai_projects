# 3. Variablen, Operationalisierung und Skalenniveaus

# Kapitel 3: Variablen, Operationalisierung und Skalenniveaus

---

## Kurz erklärt

In der empirischen Forschung wird ein interessierendes Merkmal — zum Beispiel Schmerz oder Bewegungsausmaß — als Variable bezeichnet. Eine Variable hat mindestens zwei mögliche Ausprägungen, zum Beispiel „kein Schmerz" bis „stärkster vorstellbarer Schmerz". Damit eine Variable gemessen werden kann, braucht man eine Operationalisierung: Man legt fest, wie genau das Merkmal erfasst wird, zum Beispiel durch einen Fragebogen, ein Goniometer oder eine Skala. Das Skalenniveau beschreibt, welche mathematischen Eigenschaften die gemessenen Werte haben — also ob man sie nur benennen, rangordnen oder auch rechnerisch vergleichen darf. Das Skalenniveau bestimmt direkt, welche statistischen Verfahren zulässig sind: Ein Mittelwert aus Schulnoten ist rechnerisch möglich, aber inhaltlich nicht sinnvoll, weil die Abstände zwischen den Noten nicht gleich groß sind. Die richtige Zuordnung von Skalenniveau und Verfahren ist daher kein formales Detail, sondern eine inhaltliche Voraussetzung für korrekte Schlussfolgerungen.

---

## PT-Beispiel

Ein Physiotherapeut untersucht, ob manuelle Therapie die Schmerzintensität bei Patienten mit Nackenschmerzen reduziert.

**Merkmal:** Schmerzintensität

**Operationalisierung:** Numerische Rating-Skala (NRS) von 0 bis 10, wobei 0 = kein Schmerz und 10 = stärkster vorstellbarer Schmerz

**Variable:** Schmerzintensität auf der NRS (0–10)

**Ausprägungen:** ganze Zahlen von 0 bis 10

**Skalenniveau:** ordinal — die Rangfolge ist klar (5 ist mehr als 3), aber ob der Unterschied zwischen 2 und 4 genauso groß ist wie zwischen 6 und 8, lässt sich nicht belegen. Abstände sind nicht garantiert gleich.

**Konsequenz:** Der Median ist das geeignete Lagemaß, nicht der Mittelwert. In der Praxis werden NRS-Werte häufig gemittelt — das ist eine vereinfachende Konvention, die methodisch diskutiert wird und in der Prüfung als Fehlerquelle gilt.

Daneben erhebt der Therapeut das aktive Bewegungsausmaß der Halswirbelsäule in Grad (Goniometer). Diese Variable ist verhältnisskaliert: Es gibt einen absoluten Nullpunkt (0 Grad = keine Bewegung), gleiche Abstände sind garantiert, und Aussagen wie „doppelt so viel Bewegungsausmaß" sind zulässig.

---

## Fur die Prufung

### Variablen: Grundbegriffe

| Begriff | Definition | Beispiel |
|---|---|---|
| Merkmal (Variable) | Eigenschaft, die untersucht wird | Schmerzintensität |
| Merkmalsausprägung | Konkreter Wert der Variable | NRS-Wert = 7 |
| Operationalisierung | Festlegung, wie das Merkmal gemessen wird | NRS 0–10 |
| Konstante | Wert, der sich nicht verändert | Alle Probanden sind weiblich |
| UV (unabhängige Variable) | Einflussvariable, Ursache | Therapieform |
| AV (abhängige Variable) | Outcome-Variable, Wirkung | Schmerzintensität nach Therapie |
| Kovariable | Weitere Einflussgröße neben der UV | Alter, Chronizität |
| Störvariable | Kovariable, die nicht kontrolliert wurde | Schlafqualität |

---

### Skalenniveaus: vollstandige Ubersicht

| Skalenniveau | Eigenschaften | Erlaubte Aussagen | PT-Beispiele |
|---|---|---|---|
| Nominalskala | Kategorien ohne Rangfolge | Gleich / verschieden | Diagnose, Geschlecht, Behandlungsform |
| Binare Variable | Sonderfall: nur 2 Kategorien | Gleich / verschieden | Ja/Nein, operiert/nicht operiert |
| Ordinalskala | Kategorien mit Rangfolge, Abstande unbekannt | Groesser / kleiner, aber keine Abstandsaussagen | NRS, Schulnoten, Likert-Skala, Kellgren-Lawrence-Score |
| Intervallskala | Rangfolge + gleiche Abstande, kein absoluter Nullpunkt | Differenzen sinnvoll, Verhaltnisse nicht | Celsius, Fahrenheit |
| Verhaltnissakala | Rangfolge + gleiche Abstande + absoluter Nullpunkt | Alle arithmetischen Operationen, Verhaltnisse | Koerpergroesse (cm), Gewicht (kg), ROM in Grad, Zeit in Sekunden |

---

### Zulassige statistische Verfahren nach Skalenniveau

| Skalenniveau | Lageparameter | Streuungsmass | Nicht zulassig |
|---|---|---|---|
| Nominal | Modus | — | Mittelwert, Median |
| Ordinal | Median | Interquartilsbereich (IQR) | Mittelwert, Standardabweichung |
| Intervall / Verhaltnis | Mittelwert | Standardabweichung (SD) | — |

**Regel:** Jedes hoehere Skalenniveau schliefst die Verfahren der niedrigeren Niveaus ein. Man kann eine Variable von einem hoeheren auf ein niedrigeres Niveau transformieren (z. B. Alter metrisch zu Alterskategorien ordinal) — dabei entsteht Informationsverlust. Der umgekehrte Weg ist nicht moeglich.

---

### Pruefungsfallen: konkret

**Ordinalskala und Mittelwert:**
Schmerzskalen (NRS, VAS), Likert-Skalen und Schulnoten sind ordinal. Der Abstand zwischen Wert 3 und 4 muss nicht gleich sein wie zwischen 7 und 8. Ein berechneter Mittelwert (z. B. „mittlerer NRS-Wert = 4,3") ist statistisch nicht korrekt begründet — der Median ware das richtige Lagermass.

**Intervallskala ohne echten Nullpunkt:**
0 Grad Celsius bedeutet nicht „keine Temperatur". Der Nullpunkt ist willkuerlich gewaehlt. Deshalb ist die Aussage „20 Grad sind doppelt so warm wie 10 Grad" falsch. Verhaeltnisaussagen sind nur bei Verhaltniskalen zulaessig.

**Binare Variablen:**
Zwei-Kategorien-Variablen (operiert/nicht operiert, gestuerzt/nicht gestuerzt) sind ein Sonderfall des Nominals. Sie werden oft als dichotom bezeichnet. Rechnerisch koennen sie als 0/1 kodiert werden, bleiben aber nominal.

**Transformation:**
Hoeher skalierte Variablen koennen in niedriger skalierte umgewandelt werden (Alter → Altersgruppe). Das ist moeglich, aber mit Informationsverlust verbunden. Niedriger skalierte Variablen koennen nicht nachtraeglich „aufgewertet" werden.

---

## Vertiefung

**Qualitative vs. quantitative Variablen**

- Qualitative Variablen: Zugehoerigkeit zu einer Kategorie, keine Rangordnung moeglich (Nominal). Beispiel: Nationalitaet, Haarfarbe.
- Quantitative Variablen: Zugehoerigkeit nach Groesse, Rangordnung moeglich (Ordinal, Intervall, Verhaltnis). Beispiel: Alter, NRS-Wert.

**Stetig vs. diskret**

- Stetig: Theoretisch beliebig genaue Messung moeglich, unendlich viele Zwischenwerte. Beispiel: Koerpergroesse in cm, Zeit in Sekunden.
- Diskret: Nur bestimmte (meist ganze) Werte moeglich, abzaehlbar. Beispiel: Anzahl der Therapiesitzungen, Sturzereignisse.
- Dichotom: Sonderfall mit genau 2 Auspraegungen.

**Operationalisierung in der PT-Praxis: zwei Typen von Messgroessen**

- Konkrete Groessen: direkt messbar. Beispiele: Koerpergewicht, Finger-Boden-Abstand in cm, Gelenkwinkel in Grad.
- Abstrakte Konstrukte: nicht direkt beobachtbar, benoetigen validierte Messinstrumente. Beispiele: Lebensqualitaet, motorische Kontrolle, Schmerzkatastrophisierung. Diese werden haeufig ueber Fragebogen mit Likert-Skalen erfasst — die resultierenden Werte sind ordinal, auch wenn Summenscores gebildet werden.

**Merksatz zur Verhaltnisskala:**
Absoluter Nullpunkt = vollstaendige Abwesenheit der Eigenschaft. 0 kg bedeutet kein Gewicht. 0 Grad Bewegungsausmaß bedeutet keine Bewegung. 0 Grad Celsius bedeutet nicht „keine Temperatur" — deshalb ist Celsius Intervall, nicht Verhaltnis.