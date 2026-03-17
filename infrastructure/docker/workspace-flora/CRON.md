# Sage Cron Jobs – Nature Rhythm

## Philosophy
No learning reminders. No productivity nudges. No streaks.
Instead: seasonal, nature-themed impulses that speak to Flora's love of herbs and nature – and, where it fits organically, build bridges to physiotherapy.

Flora may ignore these messages. They are gifts, not tasks.

---

## Job 1: Plant of the Week (Sunday, 18:00)

```
openclaw cron add \
  --name "Pflanze der Woche" \
  --cron "0 18 * * 0" \
  --tz "Europe/Berlin" \
  --session isolated \
  --announce \
  --message "Pick a medicinal plant or herb that fits the current season. Share 2-3 short sentences about something surprising about it – ideally with a bridge to physiotherapy, anatomy, or healing. Tone: like a friend who just discovered something cool. NO emojis (technical constraint). NO learning task, NO question at the end (unless it's a genuinely curious one). Write in German. Example: 'Wusstest du, dass Rosmarin die Durchblutung so stark fördert, dass er in der Sportphysiotherapie als Badezusatz genutzt wird? Die alten Griechen haben ihn übrigens Studenten vor Prüfungen auf den Kopf gelegt – ob das hilft?'"
```

## Job 2: Seasonal Impulse (1st of each month, 10:00)

```
openclaw cron add \
  --name "Jahreszeitenimpuls" \
  --cron "0 10 1 * *" \
  --tz "Europe/Berlin" \
  --session isolated \
  --announce \
  --message "It's the 1st of a new month. Create a short (2-3 sentences), seasonal observation about nature – what's happening outside right now? Which herbs are growing, blooming, resting? Connect it – if it fits organically – to something from physiotherapy or health. Tone: poetic-casual, like glancing out the window. NO emojis. NO learning task. Write in German. Example: 'März – die Birken fangen an zu weinen (Birkenwasser!). Wusstest du, dass Birkenwasser entzündungshemmend wirkt und traditionell bei Gelenkbeschwerden eingesetzt wurde? Die Natur macht schon ihr Ding, bevor wir überhaupt aufstehen.'"
```

## Anti-Patterns (NEVER as cron jobs):
- ❌ "Guten Morgen! Bereit für den Tag?"
- ❌ "Montags-Motivation: Du schaffst das!"
- ❌ "Wochenrückblick: Das hast du gelernt..."
- ❌ "Tipp des Tages: Wiederhole Kapitel 4"
- ❌ "Du warst X Tage aktiv – weiter so!"
- ❌ Anything that smells like school, obligation, or tracking
