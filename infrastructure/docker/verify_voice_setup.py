#!/usr/bin/env python3
"""Voice-Setup (STT + TTS) auf VM102 prüfen – auf VM102 ausführen."""
import json
import os
import shutil
import subprocess

def run(cmd, capture=True):
    try:
        r = subprocess.run(cmd, shell=True, capture_output=capture, text=True, timeout=10)
        return r.stdout.strip() if capture else r.returncode == 0
    except Exception as e:
        return str(e)

def main():
    print("=== 1. System-Abhängigkeiten ===")
    print("ffmpeg:", "OK" if shutil.which("ffmpeg") else "FEHLT")
    whisper_ok = shutil.which("whisper") or os.path.isfile(os.path.expanduser("~/.local/bin/whisper"))
    print("whisper:", "OK" if whisper_ok else "FEHLT")
    node_v = run("node -v")
    print("node:", node_v if node_v else "FEHLT")
    edge_ok = run("edge-tts --help 2>/dev/null | head -1")
    print("edge-tts:", "OK" if edge_ok else "FEHLT (pip install edge-tts)")

    print("\n=== 2. Config (clawdbot.json) ===")
    config_path = os.path.expanduser("~/.clawdbot-personal/clawdbot.json")
    if os.path.isfile(config_path):
        with open(config_path) as f:
            cfg = json.load(f)
        tts = cfg.get("messages", {}).get("tts", {})
        print("messages.tts.auto:", tts.get("auto", "nicht gesetzt"))
        print("messages.tts.provider:", tts.get("provider", "nicht gesetzt"))
        edge = tts.get("edge", {})
        edge_enabled = edge.get("enabled")
        print("messages.tts.edge.enabled:", edge_enabled if edge_enabled is not None else "nicht gesetzt")
        if edge_enabled is False:
            print("⚠ WARNUNG: edge.enabled=false – tts.js überspringt Edge TTS mit 'edge: disabled'!")
        print("tools.deny:", cfg.get("tools", {}).get("deny", []))
        print("tools.media.audio.enabled:", cfg.get("tools", {}).get("media", {}).get("audio", {}).get("enabled", "nicht gesetzt"))
    else:
        print("Config nicht gefunden:", config_path)

    print("\n=== 3. TTS-Prefs (tts.json) ===")
    prefs_path = os.path.expanduser("~/.clawdbot-personal/settings/tts.json")
    if os.path.isfile(prefs_path):
        with open(prefs_path) as f:
            prefs = json.load(f)
        print(json.dumps(prefs, indent=2))
        auto = prefs.get("auto")
        if auto == "off":
            print("⚠ WARNUNG: tts.json hat auto='off' – überschreibt clawdbot.json! TTS wird nicht ausgeführt.")
        print("maxLength:", prefs.get("maxLength", "nicht gesetzt"), "| summarize:", prefs.get("summarize", "nicht gesetzt"))
    else:
        print("tts.json nicht gefunden")

    print("\n=== 3b. node-edge-tts in Clawdbot's node_modules (KRITISCH!) ===")
    clawdbot_node = os.path.expanduser("~/.clawdbot/lib/node_modules/clawdbot")
    edge_in_clawdbot = os.path.isdir(os.path.join(clawdbot_node, "node_modules", "node-edge-tts"))
    if edge_in_clawdbot:
        print("node-edge-tts: OK (in clawdbot/node_modules)")
    else:
        print("node-edge-tts: FEHLT in clawdbot/node_modules!")
        print("  Fix: cd ~/.clawdbot/lib/node_modules/clawdbot && npm install node-edge-tts")
        print("  (npx-Cache zählt nicht – Clawdbot sucht in eigenen node_modules)")

    print("\n=== 4. Edge TTS direkt testen ===")
    test_file = "/tmp/tts_test.mp3"
    # OpenClaw nutzt node-edge-tts (Node.js) – zuerst prüfen; edge-tts (Python) als Fallback
    for cmd, name in [
        (["npx", "-y", "node-edge-tts", "-t", "Hallo Test", "-v", "de-DE-KatjaNeural", "-f", test_file], "node-edge-tts (OpenClaw)"),
        (["edge-tts", "--voice", "de-DE-KatjaNeural", "--text", "Hallo Test", "--write-media", test_file], "edge-tts (Python)"),
    ]:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if r.returncode == 0 and os.path.isfile(test_file):
            print(f"OK ({name}):", test_file, "erstellt, Größe:", os.path.getsize(test_file), "bytes")
            break
    else:
        print("FEHLER: Weder edge-tts noch node-edge-tts funktioniert. Prüfe: pip install edge-tts oder npm install -g node-edge-tts")

    print("\n=== 5. Gateway-Status ===")
    r = subprocess.run(["systemctl", "--user", "is-active", "clawdbot-gateway-personal.service"], capture_output=True, text=True)
    print(r.stdout.strip() if r.returncode == 0 else "nicht aktiv")

    print("\n=== 6. Letzte Gateway-Logs (TTS/voice/signal) ===")
    r = subprocess.run(
        "journalctl --user -u clawdbot-gateway-personal.service -n 50 --no-pager 2>/dev/null",
        shell=True, capture_output=True, text=True
    )
    for line in (r.stdout or "").split("\n"):
        if any(k in line.lower() for k in ["tts", "voice", "signal", "delivered", "failed", "error"]):
            print(line[:120])

if __name__ == "__main__":
    main()
