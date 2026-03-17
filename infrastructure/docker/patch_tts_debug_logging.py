#!/usr/bin/env python3
"""
Fügt TTS-Debug-Logging in tts.js ein – zeigt ob textToSpeech aufgerufen wird und was zurückkommt.

WICHTIG: Der Gateway lädt gateway/server-methods/tts.js, NICHT dist/tts/tts.js!
Auf VM102 ausführen. Nach dem Debuggen: Backup wiederherstellen (tts.js.bak → tts.js).
"""
import re
import shutil
from pathlib import Path

# Gateway lädt diese Datei – dist/tts/tts.js wird NICHT verwendet!
TTS_JS = Path.home() / ".clawdbot/lib/node_modules/clawdbot/dist/gateway/server-methods/tts.js"

# Pattern: const result = await textToSpeech({...}); oder result = await textToSpeech({...});
OLD = re.compile(
    r"(const |let |var )?result = await textToSpeech\(\s*\{\s*"
    r"text:\s*textForAudio,\s*"
    r"cfg:\s*params\.cfg,\s*"
    r"prefsPath,\s*"
    r"channel:\s*params\.channel,\s*"
    r"overrides:\s*directives\.overrides,\s*"
    r"\}\s*\);",
    re.DOTALL,
)

NEW = '''console.log("[TTS-DEBUG] calling textToSpeech...");
let result;
try {
    result = await textToSpeech({
        text: textForAudio,
        cfg: params.cfg,
        prefsPath,
        channel: params.channel,
        overrides: directives.overrides,
    });
    console.log("[TTS-DEBUG] textToSpeech returned: success=" + result.success + " audioPath=" + result.audioPath + " error=" + result.error + " voiceCompatible=" + result.voiceCompatible);
} catch (ttsErr) {
    console.log("[TTS-DEBUG] textToSpeech THREW: " + (typeof ttsErr === "string" ? ttsErr : JSON.stringify(ttsErr)) + " stack=" + (ttsErr && ttsErr.stack));
    return nextPayload;
}'''


def main():
    if not TTS_JS.exists():
        print(f"Fehler: {TTS_JS} nicht gefunden.")
        return 1
    content = TTS_JS.read_text(encoding="utf-8", errors="replace")
    if "[TTS-DEBUG]" in content:
        print("Debug-Logging bereits eingefügt.")
        return 0
    match = OLD.search(content)
    if not match:
        print("Pattern nicht gefunden – tts.js-Struktur evtl. geändert.")
        print("Prüfen: grep -n 'textToSpeech\\|PAST ALL CHECKS' " + str(TTS_JS))
        print("Manuell mit nano bearbeiten:")
        print(f"  nano {TTS_JS}")
        return 1
    backup = TTS_JS.with_suffix(".js.bak")
    shutil.copy2(TTS_JS, backup)
    content = OLD.sub(NEW, content, count=1)
    TTS_JS.write_text(content, encoding="utf-8")
    print("TTS-Debug-Logging eingefügt (gateway/server-methods/tts.js).")
    print(f"Backup: {backup}")
    print("Gateway neu starten, dann Nachricht senden:")
    print("  systemctl --user restart clawdbot-gateway-personal.service")
    print("  journalctl --user -u clawdbot-gateway-personal.service -f | grep TTS-DEBUG")
    return 0


if __name__ == "__main__":
    exit(main())
