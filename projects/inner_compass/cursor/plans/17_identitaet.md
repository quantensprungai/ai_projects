<!--
Reality Block
last_update: 2026-09-30
scope: Textschicht Identität, danach Liebe gegen 14b
in_scope: Chunk-Zeile Identität, HD-Rang nur G, Identitäts-Keil am G-Zentrum
out_of_scope: Ziwei/BaZi neu formulieren, Beruf umschreiben, 418, db reset, alle zwölf Bereiche
-->

# Textschicht Identität

Gelesen 2026-09-28 aus `sys_source_chunks`, dieselbe Art wie [Plan 16](16_beruf.md). Paraphrase, Titel und Chunk. Keine Buchabsätze.

## Zeile

| System | Erstlage | Zusatz | Färbung nach dem ersten Satz | Anderer Kontext |
|---|---|---|---|---|
| HD | G-Zentrum. Definiert: festes Selbst, Richtung, Liebe zu sich. Offen: kein festes Selbst, Weisheit über Identität | Kanäle und hängende Tore, die das G definieren | Typ und Strategie, übrige offene Zentren | PHS, Kreuz, BG5 |
| Astro | Aszendent / 1. Haus: Leben, Charakter, Erscheinung, Heraustreten | Der Herrscher des Aszendenten färbt, wenn er im Chart steht. Nicht jeder Planet im Haus | — | Transit |
| Ziwei | 命宫 ist die Person | Sterne im 命宫 färben | Gruppen mit 夫妻, 迁移, 子女 | 流年, 合盘 |
| BaZi | 日主 ist, woran der Chart gewogen wird | 月令 ist der Rahmen, nicht der Identitätssatz | — | 取运 |

### HD

*Definitive Book*, Chunk 61: das G-Zentrum setzt die Identität als Richtung durch Zeit und Raum. Chunk 144: ein definiertes G hat ein festes, verlässliches Selbst, Richtung und die Fähigkeit, andere zu lieben, ohne von ihnen abzuhängen. Chunk 145 und 149: ein offenes G hat keine feste Identität; das ist keine Lücke, die ein anderer Kanal füllt, sondern die Weisheit darüber, wie Identität sich zeigt. Chunk 253: die Kanäle zwischen Sakral und G verbinden Kraft mit Identität, Richtung und Liebe.

Typ und Strategie bleiben, wie man eintritt. Sie sind nicht dieser Satz. Ein Kanal, der das G nicht berührt, ist nicht die Identitäts-Erstlage.

### Astro

*The Houses* (Houlding), Chunk 56: das 1. Haus ist Leben, Leib, Erscheinung und der Punkt der Person. Charisma, Wille und emotionale Kraft kommen aus dem Zustand des Hauses und aus seinem Herrscher. Chunk 58: Merkur hat dort seine Freude, wenn er würdig steht; Saturn ist Mitsignifikator nur, wenn er mäßig gestärkt und von einem Wohltäter aspektiert ist. Das ist keine Liste aller Planeten im Haus. Chunk 57 nutzt einen Planeten im Haus für die Farbe in der Stundenastrologie, nicht als Natal-Satz.

Gelesen 2026-09-30: der Aszendent bleibt der erste Satz. Der Herrscher färbt danach, einmal, und nicht noch einmal, wenn er schon führte. Ein Planet, der nur im Haus steht, führt nicht. Merkurs Freude und Saturns Mitsignifikator bleiben draußen, bis Würde und Aspekt gelesen sind.

### Ziwei

*王亭之谈斗数*, Chunk 7: 紫微 im 命宫 beschreibt die Person (Haltung, Führung, Einsamkeit), und die Gruppen 三方四正 plus 福德 färben. Chunk 3: 命宫 steht gegenüber 妻妾 und trifft 迁移 und 子女. Der 命宫 bleibt die Identitäts-Färbung. Kein neuer Satz in diesem Schnitt.

### BaZi

*子平真诠*, Chunks 8–14: der 日主 ist, dessen Stärke gewogen wird; 月令 bleibt der Rahmen, an dem der 用神 hängt. Das bestätigt die Beruf-Zeile: der Tagstamm ist Identität, nicht Beruf. Kein neuer Satz.

## Liebe gegen 14b

14b bleibt.

- HD: *Definitive Book*, Chunk 416 (Beruf-Lesung): Strategie und Autorität sind der Eintritt in Beruf oder Beziehung. Typ + Strategie bleibt die Liebes-Erstlage. Die Bindungskanäle bleiben Zusatz. Kein Kanal bleibt Schweigen.
- Astro: *The Houses*, Chunk 65: das 7. Haus ist Ehe und enge Beziehungen, Partner, auch Geschäftspartnerschaft. Haus 7 / Deszendent bleibt. Venus bleibt Zusatz, dieser Chunk widerspricht ihr nicht.
- Ziwei: 夫妻宫 bleibt der Liebespalast (Gruppe in Chunk 3). BaZi: der 日主 bleibt die Person; ein Ehepalast ist nicht diese Zeile.

Offene Zentren färben Identität und Liebe nach dem ersten Satz. Die Berufs-Regel, sie aus dem Prompt zu nehmen, gilt hier nicht.

## Code

Nur die HD-Identitäts-Zelle. `rankIdentity` nimmt nur noch einen G-Kanal oder ein hängendes G-Tor. Ein anderer Kanal wird nicht zur Identität. Der Keil ist das G, definiert oder offen. Typ und Strategie färben danach. Formulierer v8, damit der alte Typ-Keil nicht aus dem Cache kommt. Astro, Ziwei, BaZi und die Liebes-Zeile ohne Code.
