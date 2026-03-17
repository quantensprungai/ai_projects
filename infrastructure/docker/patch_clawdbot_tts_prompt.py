#!/usr/bin/env python3
"""
Patcht clawdbot tts.js – entfernt die [[tts:...]]-Prompt-Injection.
Die Plattform injiziert sonst "Use [[tts:...]]" in den Prompt, wodurch das Modell
dieses Markup ausgibt. Bei auto: "always" soll das Modell nur normalen Text schreiben.

Auf VM102 ausführen. Nach Clawdbot-Updates ggf. erneut ausführen.
"""
import shutil
from pathlib import Path

TTS_JS = Path.home() / ".clawdbot/lib/node_modules/clawdbot/dist/tts/tts.js"

# Strings die [[tts:...]] empfehlen → ersetzen durch "nur normalen Text"
REPLACEMENTS = [
    ("Only use TTS when you include [[tts]] or [[tts:text]] tags.", "TTS is automatic - write plain text only. Never use [[tts]] or [[tts:text]]."),
    ("Use [[tts:...]] and optional [[tts:text]]...[[/tts:text]] to control voice/expressiveness.", "Write plain text only. Platform converts to audio automatically. Never use [[tts:...]] or [[tts:text]]."),
]

def main():
    if not TTS_JS.exists():
        print(f"Fehler: {TTS_JS} nicht gefunden.")
        return 1
    content = TTS_JS.read_text(encoding="utf-8", errors="replace")
    original = content
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)
    if content == original:
        print("Keine Änderung nötig (bereits gepatcht oder Strings nicht gefunden).")
        return 0
    shutil.copy2(TTS_JS, TTS_JS.with_suffix(".js.bak"))
    TTS_JS.write_text(content, encoding="utf-8")
    print("tts.js gepatcht. Backup: tts.js.bak")
    print("Gateway neu starten: systemctl --user restart clawdbot-gateway-personal.service")
    return 0

if __name__ == "__main__":
    exit(main())
