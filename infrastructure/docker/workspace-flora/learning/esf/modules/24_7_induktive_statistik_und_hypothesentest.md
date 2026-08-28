# 7. Induktive Statistik und Hypothesentestung

# Kapitel 7: Induktive Statistik und Hypothesentestung

---

## Kurz erklärt

Die deskriptive Statistik beschreibt nur die vorliegende Stichprobe. Die induktive Statistik geht einen Schritt weiter: Sie fragt, ob ein in der Stichprobe beobachteter Effekt auch in der Grundgesamtheit gilt. Da man nie die gesamte Population messen kann, bleibt immer eine Unsicherheit. Diese Unsicherheit wird durch zwei Kenngrößen ausgedrückt: den p-Wert und das Konfidenzintervall. Das Vorgehen folgt einer festen Logik: Man formuliert ein Hypothesenpaar, legt vor der Auswertung ein Signifikanzniveau fest, berechnet eine Prüfgröße und trifft dann eine Entscheidung. Diese Entscheidung kann falsch sein, auch wenn alles korrekt durchgeführt wurde.

---

## PT-Beispiel

Eine Physiotherapeutin untersucht, ob manuelle Therapie bei Patienten mit Nackenschmerzen das Bewegungsausmaß der Halswirbelsäule stärker verbessert als ein Heimübungsprogramm.

**Forschungsfrage:** Gibt es einen Unterschied im Bewegungsausmaß (in Grad) nach 6 Wochen zwischen der Gruppe mit manueller Therapie und der Gruppe mit Heimübungen?

**Hypothesenpaar:**
- H0: Manuelle Therapie und Heimübungen führen nach 6 Wochen zu keinem Unterschied im Bewegungsausmaß der HWS.
- H1: Manuelle Therapie führt nach 6 Wochen zu einem größeren Bewegungsausmaß als Heimübungen.

**Signifikanzniveau:** alpha = 0,05 (wird vor der Auswertung festgelegt).

**Ergebnis:** p = 0,03. Da p < 0,05, wird H0 abgelehnt. Die Studie zeigt einen statistisch signifikanten Unterschied.

**Klinische Relevanz:** Der mittlere Unterschied zwischen den Gruppen beträgt 3 Grad. Ob 3 Grad klinisch bedeutsam sind, hängt vom minimalen klinisch relevanten Unterschied (MCID) für dieses Messinstrument ab. Statistisch signifikant bedeutet nicht automatisch klinisch relevant.

---

## Fur die Prüfung

### Das Hypothesenpaar

| Begriff | Inhalt |
|---|---|
| H0 (Nullhypothese) | Kein Unterschied, kein Zusammenhang, kein Effekt in der Population |
| H1 (Alternativhypothese) | Effekt, Unterschied oder Zusammenhang in der Population vorhanden |
| Komplementarität | H0 und H1 schliessen alle Möglichkeiten lückenlos ab |
| Gerichtet | H1 gibt eine Richtung an (z. B. Gruppe A > Gruppe B) |
| Ungerichtet | H1 gibt nur an, dass ein Unterschied besteht, ohne Richtung |

### Der p-Wert: Bedeutung und häufige Fehler

**Korrekte Definition:** Der p-Wert gibt an, wie wahrscheinlich es ist, die beobachteten Daten (oder noch extremere) zu erhalten, wenn H0 in der Grundgesamtheit wahr wäre. Formal: P(Daten | H0 wahr).

**Entscheidungsregel:**
- p < Signifikanzniveau (alpha, meist 0,05): H0 wird abgelehnt, H1 wird angenommen.
- p >= Signifikanzniveau: H0 wird beibehalten (nicht bewiesen, nur nicht abgelehnt).

**Drei Fehler, die in der Prüfung abgefragt werden:**

1. p-Wert ist NICHT die Wahrscheinlichkeit, dass H0 wahr ist. p = 0,03 bedeutet nicht, dass H0 nur mit 3 % Wahrscheinlichkeit stimmt.
2. p < 0,05 bedeutet NICHT, dass der Effekt klinisch relevant ist.
3. p >= 0,05 bedeutet NICHT, dass kein Effekt existiert. Es bedeutet nur, dass die vorliegenden Daten keinen ausreichenden Beleg für H1 liefern.

### Signifikanzniveau und Fehlerarten

| Begriff | Definition | Beispiel |
|---|---|---|
| Signifikanzniveau (alpha) | Vorab festgelegte Schwelle, ab der H0 abgelehnt wird. Üblicherweise 0,05. | Vor der Studie festlegen, nicht danach anpassen. |
| Alpha-Fehler (Typ-I-Fehler) | H0 wird abgelehnt, obwohl sie in der Population wahr ist. | Man schliesst auf einen Effekt, der nicht existiert. |
| Beta-Fehler (Typ-II-Fehler) | H0 wird beibehalten, obwohl H1 in der Population gilt. | Man übersieht einen real existierenden Effekt. |
| Teststärke (Power) | Wahrscheinlichkeit, einen tatsächlich vorhandenen Effekt auch zu entdecken. 1 minus Beta. | Grosse Stichproben erhöhen die Power. |

**Merkhilfe für die Prüfung:**

- Alpha-Fehler: falscher Alarm (man handelt, obwohl nichts da ist).
- Beta-Fehler: verpasster Treffer (man handelt nicht, obwohl etwas da wäre).

### Zusammenhang zwischen alpha und beta

- Senkt man alpha (z. B. auf 0,01), wird der Alpha-Fehler seltener, aber der Beta-Fehler häufiger.
- Beide Fehler gleichzeitig zu minimieren ist nur durch Vergrösserung der Stichprobe möglich.

### Konfidenzintervall (KI)

**Korrekte Interpretation des 95%-KI:** Wenn man das gleiche Verfahren sehr oft an verschiedenen Stichproben aus derselben Population anwenden würde, würden 95 % der so berechneten Intervalle den wahren Populationsparameter enthalten.

**Falsche Interpretation:** Das KI bedeutet NICHT, dass der wahre Wert mit 95 % Wahrscheinlichkeit in diesem konkreten Intervall liegt. Das ist eine bayesianische Aussage, nicht die frequentistische Interpretation.

**Praktische Nutzung:**
- KI, das den Nullwert einschliesst (z. B. Differenz 0 bei einem Gruppenvergleich): kein signifikanter Befund.
- KI, das den Nullwert nicht einschliesst: entspricht einem signifikanten Befund bei gleichem alpha.
- Breites KI: grosse Unsicherheit, meist kleine Stichprobe.
- Enges KI: kleine Unsicherheit, meist grosse Stichprobe.

### Statistisch signifikant vs. klinisch relevant

| Merkmal | Statistisch signifikant | Klinisch relevant |
|---|---|---|
| Frage | Ist der Effekt grösser als Zufall? | Ist der Effekt gross genug, um für Patienten bedeutsam zu sein? |
| Abhängig von | Stichprobengrösse, Variabilität | MCID (minimaler klinisch relevanter Unterschied), Patientenkontext |
| Beispiel | n = 1000, Unterschied 2 mm ROM, p = 0,02 | 2 mm ROM ist klinisch nicht bedeutsam |
| Schlussfolgerung | Kein automatischer Rückschluss möglich | Erfordert inhaltliches Urteil |

---

## Vertiefung

### Ablauf eines Hypothesentests (Schritte in Reihenfolge)

1. Forschungsfrage formulieren.
2. Hypothesenpaar bilden: H0 und H1 (komplementär, vor der Datenerhebung).
3. Signifikanzniveau alpha festlegen (vor der Auswertung, üblicherweise 0,05).
4. Daten erheben.
5. Geeignetes Testverfahren wählen (abhängig von Skalenniveau, Verteilung, Anzahl der Gruppen).
6. Prüfgrösse berechnen, p-Wert ablesen.
7. Entscheidung: p < alpha → H0 ablehnen / p >= alpha → H0 beibehalten.
8. Inhaltliche Interpretation: Effektgrösse, klinische Relevanz.

### Einflussfaktoren auf den p-Wert

- Effektgrösse: je grösser der Effekt, desto kleiner der p-Wert.
- Stichprobengrösse: je mehr Personen, desto kleiner der p-Wert, auch bei kleinen Effekten.
- Streuung der Daten: je grösser die Streuung, desto grösser der p-Wert.

### Prüfungsfallen auf einen Blick

- p = 0,04 beweist nicht, dass H0 falsch ist. Es ist eine Entscheidungsregel unter Unsicherheit.
- Ein nicht-signifikantes Ergebnis ist kein Beweis für die H0. Abwesenheit von Evidenz ist nicht Evidenz für Abwesenheit.
- Das Signifikanzniveau wird VOR der Datenerhebung festgelegt, nicht danach.
- KI und p-Wert liefern konsistente Aussagen: Wenn das 95%-KI den Nullwert nicht einschliesst, ist p < 0,05.