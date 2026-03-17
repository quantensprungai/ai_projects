#!/usr/bin/env python3
"""
Sage Cron Jobs für Flora – auf VM102 ausführen.
Voraussetzung: clawdbot --profile personal, Flora gepaart (Signal)
"""
import os
import subprocess
import shutil

# clawdbot kann in verschiedenen Pfaden liegen (Installer vs. npm)
cmd = (
    shutil.which("clawdbot")
    or shutil.which("openclaw")
    or shutil.which("moltbot")
    or (os.path.expanduser("~/.clawdbot/bin/clawdbot") if os.path.isfile(os.path.expanduser("~/.clawdbot/bin/clawdbot")) else None)
)
if not cmd:
    print("Fehler: clawdbot oder openclaw nicht gefunden.")
    exit(1)
cmd = [cmd, "--profile", "personal"] if isinstance(cmd, str) else ["clawdbot", "--profile", "personal"]

def run_cron_add(name, cron, message):
    # --announce: manche ältere clawdbot-Versionen kennen es nicht; Default bei isolated = deliver
    args = cmd + ["cron", "add", "--name", name, "--cron", cron, "--tz", "Europe/Berlin",
                  "--session", "isolated", "--agent", "flora", "--message", message]
    print(f"Füge hinzu: {name}...")
    r = subprocess.run(args)
    if r.returncode != 0:
        print(f"  Warnung: Exit-Code {r.returncode}")

print("Verwende:", " ".join(cmd))
print()

run_cron_add(
    "Pflanze der Woche",
    "0 18 * * 0",
    "Pick a medicinal plant or herb that fits the current season. Share 2-3 short sentences about something surprising about it – ideally with a bridge to physiotherapy, anatomy, or healing. Tone: like a friend who just discovered something cool. NO emojis (technical constraint). NO learning task, NO question at the end (unless it's a genuinely curious one). Write in German. Example: 'Wusstest du, dass Rosmarin die Durchblutung so stark fördert, dass er in der Sportphysiotherapie als Badezusatz genutzt wird? Die alten Griechen haben ihn übrigens Studenten vor Prüfungen auf den Kopf gelegt – ob das hilft?'"
)

run_cron_add(
    "Jahreszeitenimpuls",
    "0 10 1 * *",
    "It's the 1st of a new month. Create a short (2-3 sentences), seasonal observation about nature – what's happening outside right now? Which herbs are growing, blooming, resting? Connect it – if it fits organically – to something from physiotherapy or health. Tone: poetic-casual, like glancing out the window. NO emojis. NO learning task. Write in German. Example: 'März – die Birken fangen an zu weinen (Birkenwasser!). Wusstest du, dass Birkenwasser entzündungshemmend wirkt und traditionell bei Gelenkbeschwerden eingesetzt wurde? Die Natur macht schon ihr Ding, bevor wir überhaupt aufstehen.'"
)

print()
print("Cron-Jobs hinzugefügt. Prüfen:", " ".join(cmd), "cron list")
