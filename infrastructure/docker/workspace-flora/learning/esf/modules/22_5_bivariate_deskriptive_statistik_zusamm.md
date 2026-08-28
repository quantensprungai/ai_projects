# 5. Bivariate Deskriptive Statistik: Zusammenhänge beschreiben

# 5. Bivariate Deskriptive Statistik: Zusammenhänge beschreiben

---

## Kurz erklärt

Die bivariate deskriptive Statistik beschreibt die Beziehung zwischen zwei Variablen. Im Unterschied zur univariaten Statistik, die eine Variable isoliert betrachtet, fragt man hier: Hängen zwei Merkmale zusammen, und wenn ja, wie stark und in welche Richtung? Dafür gibt es verschiedene Koeffizienten, deren Wahl vom Skalenniveau der Variablen abhängt. Ein zentrales Ergebnis einer Korrelationsanalyse ist immer nur eine Beschreibung des Zusammenhangs, keine Aussage über Ursache und Wirkung. Für den Zusammenhang zwischen zwei dichotomen Variablen in epidemiologischen Designs werden statt Korrelationskoeffizienten Risikomaße wie RR und OR verwendet.

---

## PT-Beispiel

Ein Physiotherapeut möchte wissen, ob ein Zusammenhang zwischen Schmerzintensität (numerische Ratingskala 0-10, ordinal) und Bewegungsausmaß der Halswirbelsäule in Grad (metrisch, verhältnisskaliert) besteht. Da die Schmerzskala ordinal ist und keine Normalverteilung angenommen werden kann, wird Spearmans Rangkorrelation (rs) berechnet. Das Streudiagramm zeigt: Je höher die Schmerzintensität, desto geringer das Bewegungsausmaß. Das Ergebnis rs = -0,71 beschreibt einen starken negativen (gegensinnigen) Zusammenhang. Kausalität lässt sich daraus nicht ableiten: Es ist unklar, ob der Schmerz die Bewegung einschränkt, ob eingeschränkte Bewegung Schmerz verursacht, oder ob ein dritter Faktor wie Muskelverspannung beide Variablen beeinflusst.

---

## Fur die Prufung

### Korrelationskoeffizienten: Zuordnung nach Voraussetzungen

| Koeffizient | Skalenniveau | Verteilung | Zusammenhangstyp |
|---|---|---|---|
| Pearson-r | mindestens intervallskaliert (metrisch) | Normalverteilung beider Variablen | linear |
| Spearman-rs | mindestens ordinal | keine Normalverteilung nötig | monoton (nicht zwingend linear) |

Monoton bedeutet: Die eine Variable steigt tendenziell, wenn die andere steigt (oder fällt), aber nicht unbedingt proportional.

### Voraussetzungen Pearson-r (alle vier müssen erfüllt sein)

- Mindestens intervallskalierte Variablen
- Linearer Zusammenhang (prüfen: Streudiagramm)
- Normalverteilung beider Variablen
- Keine Ausreißer

### Interpretation des Korrelationskoeffizienten (Pearson und Spearman)

| Betrag des Koeffizienten | Interpretation |
|---|---|
| 0,00 - 0,10 | kein Zusammenhang |
| 0,10 - 0,30 | schwacher Zusammenhang |
| 0,30 - 0,50 | mittlerer Zusammenhang |
| 0,50 - 1,00 | starker Zusammenhang |
| +1,00 | perfekter positiver Zusammenhang |
| -1,00 | perfekter negativer Zusammenhang |

Vorzeichen = Richtung. Betrag = Stärke.

### Streudiagramm: Funktion und Ablesen

- x-Achse: Variable A, y-Achse: Variable B
- Jeder Punkt = eine Person/Beobachtung
- Punktwolke von links unten nach rechts oben: positiver Zusammenhang
- Punktwolke von links oben nach rechts unten: negativer Zusammenhang
- Kreisförmige Punktwolke ohne erkennbare Richtung: kein Zusammenhang
- Dient auch zur Prüfung der Voraussetzung "linearer Zusammenhang" vor der Pearson-Korrelation

### Korrelation und Kausalitat: mogliche Alternativerklarungen

Wenn r = 0,8 zwischen Werbespots und Süßigkeitenkauf gefunden wird, sind folgende Erklärungen möglich:

- Werbespots verursachen Kauf (Kausalität A auf B)
- Kaufverhalten erhöht Werbeausgaben (Kausalität B auf A, Umkehrung)
- Drittvariable (z. B. verfügbares Einkommen) beeinflusst beide
- Zufälliger Zusammenhang in der Stichprobe

Eine Korrelation allein kann keine dieser Erklärungen ausschließen.

### RR und OR: Unterschied und Zuordnung

| Merkmal | RR (Relatives Risiko) | OR (Odds Ratio) |
|---|---|---|
| Deutsch | Risikioverhältnis | Chancenverhältnis |
| Studiendesign | prospektiv, Kohortenstudie | retrospektiv, Fall-Kontroll-Studie |
| Was wird verglichen | Wahrscheinlichkeit des Ereignisses in Gruppe A vs. B | Chance des Ereignisses in Gruppe A vs. B |
| Wert = 1 | kein Effekt | keine Assoziation |
| Wert > 1 | Exposition erhöht Risiko (Risikofaktor) | Exposition erhöht Chance des Ereignisses |
| Wert < 1 | Exposition senkt Risiko (protektiv) | Exposition senkt Chance des Ereignisses |

Risiko = Anzahl Ereignisse / Gesamtzahl der Gruppe.
Chance (Odds) = Anzahl Ereignisse / Anzahl Nicht-Ereignisse.

### RR berechnen: Schritte

1. Risiko in exponierter Gruppe: Ereignisse exponiert / Gesamtzahl exponiert
2. Risiko in nicht-exponierter Gruppe: Ereignisse nicht-exponiert / Gesamtzahl nicht-exponiert
3. RR = Risiko exponiert / Risiko nicht-exponiert

### OR berechnen: Schritte

1. Odds in exponierter Gruppe: Ereignisse exponiert / Nicht-Ereignisse exponiert
2. Odds in nicht-exponierter Gruppe: Ereignisse nicht-exponiert / Nicht-Ereignisse nicht-exponiert
3. OR = Odds exponiert / Odds nicht-exponiert

Kurzformel aus 2x2-Tabelle (Felder a, b, c, d im Schema Ereignis+/- x Exposition+/-): OR = (a x d) / (b x c)

---

## Vertiefung

### Kovarianz als Grundlage der Pearson-Korrelation

- Kovarianz: misst, ob Abweichungen zweier Variablen vom jeweiligen Mittelwert gleichsinnig oder gegensinnig auftreten
- Problem: nicht standardisiert, daher abhängig von der Maßeinheit, keine einheitliche Interpretation
- Pearson-r: Kovarianz geteilt durch das Produkt beider Standardabweichungen, dadurch standardisiert auf den Bereich -1 bis +1

### Spearman-rs: Prinzip

- Rohdaten werden in Ränge umgewandelt (kleinster Wert = Rang 1)
- Anschließend wird auf den Rängen eine Korrelation berechnet
- Bei Rangbindungen (gleiche Werte) werden mittlere Ränge vergeben
- Robuster gegenüber Ausreißern und Nicht-Normalverteilung als Pearson-r

### Wann welches Verfahren

- Beide Variablen metrisch, normalverteilt, kein Ausreißer, linearer Zusammenhang erkennbar: Pearson-r
- Eine oder beide Variablen ordinal, oder Normalverteilung verletzt, oder Ausreißer vorhanden: Spearman-rs
- Beide Variablen nominal/dichotom, Studiendesign epidemiologisch: RR oder OR

### Prufungsfallen kompakt

- Pearson-r auf ordinale Daten: nicht zulässig. Schmerzskalas (NRS, VAS) gelten in der Prüfung als ordinal, sofern nicht anders angegeben.
- r = 0 bedeutet: kein linearer Zusammenhang. Es kann trotzdem ein nicht-linearer Zusammenhang bestehen.
- RR und OR liefern bei seltenen Ereignissen ähnliche Werte, bei häufigen Ereignissen weichen sie deutlich ab. OR überschätzt dann das relative Risiko.
- OR wird bei Fall-Kontroll-Studien verwendet, weil die Gruppengrößen (Fälle vs. Kontrollen) vom Forscher festgelegt werden und kein echtes Ausgangsrisiko berechnet werden kann.