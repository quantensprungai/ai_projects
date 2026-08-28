# Übungen — Bivariate Deskriptive Statistik: Zusammenhänge beschreiben

---

## Aufgabe 1 (Grundniveau)

Ein Forschungsteam erhebt bei 60 Patienten zwei Variablen: Gehgeschwindigkeit in m/s (metrisch, normalverteilt) und Sturzangst auf einer 4-stufigen Ordinalskala (1 = keine Angst, 4 = sehr hohe Angst).

**a)** Welcher Korrelationskoeffizient ist für diesen Datensatz geeignet — Pearson-r oder Spearman-rs? Nennen Sie zwei Gründe.

**b)** Das Ergebnis lautet rs = -0,44. Beschreiben Sie den Zusammenhang: Richtung, Stärke und inhaltliche Bedeutung in einem Satz.

**c)** Eine Kollegin sagt: „Das beweist, dass Sturzangst langsamer macht." Was ist daran statistisch problematisch?

---

## Aufgabe 2 (Mittelniveau)

In einer Kohortenstudie wird untersucht, ob regelmäßiges Rauchen mit dem Auftreten von Rückenschmerzen zusammenhängt. Von 200 Rauchern entwickeln 80 Rückenschmerzen. Von 200 Nichtrauchern entwickeln 40 Rückenschmerzen.

**a)** Berechnen Sie das Relative Risiko (RR) ohne Taschenrechner. Zeigen Sie den Rechenweg.

**b)** Interpretieren Sie den RR-Wert inhaltlich: Was bedeutet er für Raucher im Vergleich zu Nichtrauchern?

**c)** Warum wird in dieser Studie RR und nicht OR berechnet?

---

## Aufgabe 3 (Prüfungsniveau)

Lesen Sie die folgende Studienbeschreibung und beantworten Sie die Fragen.

*Eine Studie untersucht den Zusammenhang zwischen täglicher Bildschirmzeit in Stunden (metrisch) und Schlafqualität auf dem Pittsburgh Sleep Quality Index (PSQI, 0–21 Punkte, ordinal). Das Streudiagramm zeigt eine deutlich gebogene, U-förmige Punktwolke. Berechnet wird Pearson-r = -0,09, der als „kein Zusammenhang" interpretiert wird.*

**a)** Nennen Sie zwei methodische Fehler, die in der Beschreibung stecken.

**b)** Welcher Koeffizient wäre stattdessen zu wählen? Begründen Sie mit Blick auf Skalenniveau und Streudiagrammbefund.

**c)** Was bedeutet es, dass Pearson-r nahe 0 ist, obwohl das Streudiagramm eine U-Form zeigt? Erläutern Sie das Prinzip in zwei Sätzen.

**d)** Formulieren Sie eine plausible Drittvariable, die sowohl Bildschirmzeit als auch Schlafqualität beeinflussen könnte, und erklären Sie kurz, warum das die Interpretation des Zusammenhangs erschwert.

---

---

## Musterlösung

---

### Aufgabe 1

**a)** Spearman-rs ist geeignet.
Grund 1: Die Sturzangst ist ordinalskaliert — Pearson-r setzt mindestens Intervallskalierung voraus.
Grund 2: Da eine Variable ordinal ist, kann keine Normalverteilung beider Variablen vorausgesetzt werden — eine Voraussetzung für Pearson-r ist damit verletzt.

**b)** rs = -0,44 beschreibt einen mittleren negativen Zusammenhang: Patienten mit höherer Sturzangst tendieren dazu, langsamer zu gehen.

**c)** Aus einer Korrelation lässt sich keine Kausalität ableiten. Es ist ebenso möglich, dass langsames Gehen die Sturzangst erhöht, oder dass eine Drittvariable (z. B. allgemeine körperliche Einschränkung) beide Variablen gleichzeitig beeinflusst.

---

### Aufgabe 2

**a)**
Risiko Raucher: 80 / 200 = 0,40
Risiko Nichtraucher: 40 / 200 = 0,20
RR = 0,40 / 0,20 = **2,0**

**b)** Raucher haben ein doppelt so hohes Risiko, Rückenschmerzen zu entwickeln, wie Nichtraucher. Rauchen ist in dieser Studie mit einem erhöhten Risiko assoziiert (RR > 1).

**c)** Es handelt sich um eine Kohortenstudie mit prospektivem Design. Die Ausgangsgruppengrößen sind bekannt und zufällig zugeteilt (bzw. beobachtet), daher lässt sich ein echtes Ausgangsrisiko berechnen. RR setzt genau das voraus. OR würde hier das Risiko überschätzen, da das Ereignis (Rückenschmerzen) mit 40 % bzw. 20 % nicht selten ist.

---

### Aufgabe 3

**a)**
Fehler 1: Pearson-r ist bei ordinalskalierten Daten (PSQI) nicht zulässig — das Verfahren setzt mindestens Intervallskalierung voraus.
Fehler 2: Das Streudiagramm zeigt eine U-förmige Kurve — damit ist der Zusammenhang nicht linear. Pearson-r misst aber ausschließlich lineare Zusammenhänge und ist daher auch aus diesem Grund unangemessen.

**b)** Spearman-rs wäre zu wählen: Der PSQI ist ordinal, und Spearman-rs setzt keine Normalverteilung und keinen linearen Zusammenhang voraus — es wird lediglich ein monotoner Zusammenhang geprüft. Auch Spearman-rs kann eine U-Form nicht vollständig abbilden, ist aber zumindest hinsichtlich des Skalenniveaus korrekt.

**c)** Pearson-r misst nur den linearen Anteil eines Zusammenhangs. Bei einer U-Form heben sich positive und negative Abweichungen gegenseitig auf, sodass der Koeffizient nahe null liegt — obwohl ein systematischer, nicht-linearer Zusammenhang besteht. r = 0 schließt also einen Zusammenhang nicht aus, sondern bedeutet nur: kein linearer Zusammenhang erkennbar.

**d)** Beispiel: Stress oder psychische Belastung. Wer stark gestresst ist, verbringt möglicherweise mehr Zeit am Bildschirm (als Ablenkung oder berufsbedingt) und schläft gleichzeitig schlechter (durch physiologische Aktivierung). Wenn eine Drittvariable beide Messgrößen beeinflusst, kann der beobachtete Zusammenhang zwischen Bildschirmzeit und Schlafqualität zumindest teilweise auf diese Drittvariable zurückzuführen sein — und nicht auf eine direkte Beziehung der beiden Variablen untereinander.

---

---

## Häufige Fehler

**Aufgabe 1:**
Der häufigste Fehler ist die Wahl von Pearson-r mit der Begründung, die Gehgeschwindigkeit sei metrisch. Entscheidend ist aber das niedrigste Skalenniveau der beiden Variablen — und das ist hier ordinal. Sobald eine Variable ordinal ist, entfällt Pearson-r.

**Aufgabe 2:**
Viele Studierende verwechseln RR und OR oder begründen die Wahl nicht mit dem Studiendesign. RR ist an das prospektive Design geknüpft, weil nur dann die Ausgangsrisiken in beiden Gruppen bekannt sind. Ein zweiter häufiger Fehler: Das Ergebnis RR = 2 wird als „Rauchen verursacht Rückenschmerzen" interpretiert — auch hier gilt: Kohortenstudien zeigen Assoziation, nicht Kausalität.

**Aufgabe 3:**
Der klassische Fehler ist die Schlussfolgerung, r = 0 bedeute „kein Zusammenhang" — ohne die Einschränkung auf lineare Zusammenhänge zu nennen. Wer das Streudiagramm ignoriert und sich allein auf den Koeffizientenwert verlässt, übersieht systematisch nicht-lineare Muster. Das Streudiagramm ist deshalb kein optionaler Schritt, sondern Voraussetzungsprüfung.