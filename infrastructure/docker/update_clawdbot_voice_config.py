#!/usr/bin/env python3
"""
STT (Sprachnachrichten verstehen) + TTS (Sprachantwort bei Voice-Inbound) aktivieren.

Auf VM102 ausführen:
  python3 update_clawdbot_voice_config.py

STT: Whisper-CLI (lokal, kein API-Key) – pip install openai-whisper
TTS: Edge TTS (kein API-Key nötig)
ffmpeg: Pflicht für Signal-Voice – Opus→WAV konvertieren. apt install ffmpeg
"""
import json
import os
import shutil
import sys

CONFIG_PATH = "/home/user/.clawdbot-personal/clawdbot.json"

# STT: nur Whisper-CLI (lokal, kein API-Key)
def get_stt_models():
    models = []
    candidates = [
        shutil.which("whisper"),
        os.path.expanduser("~/.local/bin/whisper"),
        "/home/user/.local/bin/whisper",
    ]
    whisper_path = next((p for p in candidates if p and os.path.isfile(p)), None)
    if whisper_path:
        models.append({
            "type": "cli",
            "command": whisper_path,
            "args": ["--model", "base", "{{MediaPath}}"],
            "timeoutSeconds": 45,
        })
    return models


def main():
    try:
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print(f"Fehler: {CONFIG_PATH} nicht gefunden.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Fehler: ungültiges JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # tools.media.audio (STT)
    if "tools" not in cfg:
        cfg["tools"] = {}
    # TTS-Tool deaktivieren – Plattform übernimmt TTS automatisch (messages.tts.auto)
    # Verhindert, dass Agent tool_call mit name "tts" ausgibt
    deny = cfg["tools"].get("deny", [])
    if "tts" not in deny:
        deny.append("tts")
    cfg["tools"]["deny"] = deny
    if "media" not in cfg["tools"]:
        cfg["tools"]["media"] = {}
    cfg["tools"]["media"]["audio"] = {
        "enabled": True,
        "maxBytes": 20971520,
        "models": get_stt_models(),
    }
    has_whisper = any(p and os.path.isfile(p) for p in [
        shutil.which("whisper"),
        os.path.expanduser("~/.local/bin/whisper"),
        "/home/user/.local/bin/whisper",
    ])
    print("STT (Audio):", "Whisper-CLI" if has_whisper else "KEIN (Whisper nicht gefunden)")

    # messages.tts (TTS – Antwort als Voice bei Sprachnachricht)
    if "messages" not in cfg:
        cfg["messages"] = {}
    cfg["messages"]["tts"] = {
        "auto": "always",
        "provider": "edge",
        "maxTextLength": 8000,
        "prefsPath": "/home/user/.clawdbot-personal/settings/tts.json",
        "edge": {"enabled": True, "lang": "de-DE", "voice": "de-DE-KatjaNeural"},
        "modelOverrides": {"enabled": False},  # Verhindert [[tts:...]]-Direktiven im Prompt
        # audioAsVoice: Führt bei manchen Clawdbot-Versionen zu Config invalid / keine Antwort – auskommentiert
        # Stattdessen: Agent fügt [[audio_as_voice]] in Antwort ein (AGENTS.md)
    }
    # channels.signal.tts ist KEIN gültiger Key (OpenClaw 2026.1) – führt zu Config invalid!
    # TTS-Prefs: Summary deaktivieren (ohne API-Key schlägt Summary fehl → Audio wird übersprungen).
    # WICHTIG: Bei summary=False und Antwort > maxLength wird Audio komplett übersprungen (nur Text).
    # Flora neigt zu langen Antworten → ggf. maxLength auf 15000 erhöhen oder Flora-Prompt kürzen.
    prefs_dir = "/home/user/.clawdbot-personal/settings"
    prefs_path = os.path.join(prefs_dir, "tts.json")
    os.makedirs(prefs_dir, exist_ok=True)
    prefs = {"summarize": False, "maxLength": 8000}
    if os.path.exists(prefs_path):
        try:
            with open(prefs_path) as f:
                prefs = {**prefs, **json.load(f)}
        except Exception:
            pass
    prefs["summarize"] = False
    prefs["maxLength"] = 8000
    # auto in tts.json überschreibt clawdbot.json – bei "off"/"inbound" kommt bei Text-Nachrichten kein TTS.
    # Mit clawdbot.json synchron halten:
    if cfg["messages"]["tts"].get("auto") == "always":
        prefs["auto"] = "always"
    with open(prefs_path, "w") as f:
        json.dump(prefs, f, indent=2)
    tts_auto = cfg["messages"]["tts"].get("auto", "off")
    print(f"TTS: Edge ({tts_auto}) – {'jede Antwort als Sprachnachricht' if tts_auto == 'always' else 'aus (nur Text)'}; weibliche Stimme (Katja)")
    print("     maxLength 8000, Summary aus (ohne OpenAI)")
    print("     tools.deny: tts (Agent kann kein tool_call tts mehr nutzen)")

    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)

    print("\nConfig aktualisiert. Gateway neu starten:")
    print("  systemctl --user restart clawdbot-gateway-personal.service")
    if not has_whisper:
        print("\nHinweis: Whisper-CLI nicht gefunden. Für lokales STT ohne API-Key:")
        print("  pip install openai-whisper")
    if not shutil.which("ffmpeg"):
        print("\nWICHTIG: ffmpeg fehlt! Signal-Voice (Opus) braucht ffmpeg zum Decodieren.")
        print("  sudo apt install ffmpeg")


if __name__ == "__main__":
    main()
