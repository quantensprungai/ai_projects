#!/usr/bin/env python3
"""
ClawdBot Voice/TTS Triple-Fix Script (angepasst für VM102-Setup)
================================================================
  1) PROMPT-PATCH    – Bereinigt Agent-Prompts von [[tts:...]]-Markup
  2) CONFIG-VERIFY   – Prüft TTS-Pipeline-Konfiguration
  3) POST-PROCESSOR  – Fängt [[tts:...]]-Markup ab, extrahiert Text

Nutzung (auf VM102):
  python3 clawdbot_voice_fix.py --check          # Nur prüfen
  python3 clawdbot_voice_fix.py --fix           # Fixes anwenden
  python3 clawdbot_voice_fix.py --fix --dry-run # Zeigen was geändert würde

Pfade (VM102):
  - Config: ~/.clawdbot-personal/clawdbot.json
  - Workspaces: ~/clawd/workspace-{heiko,noah,flora,familie}
"""
import os
import re
import sys
import json
import shutil
import subprocess
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, List, Dict

# VM102-Setup
CONFIG = {
    "clawdbot_base": os.path.expanduser("~/.clawdbot-personal"),
    "clawd_base": os.path.expanduser("~/clawd"),
    "config_file": os.path.expanduser("~/.clawdbot-personal/clawdbot.json"),
    "tts_output_dir": "/tmp/clawdbot_tts",
    "tts_voice": "de-DE-KatjaNeural",
    "tts_format": "mp3",
    "workspace_agents": ["heiko", "noah", "flora", "familie"],
}

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("voice-fix")


# ═══════════════════════════════════════════════
#  TEIL 1: PROMPT-PATCH
# ═══════════════════════════════════════════════

def strip_tts_markup(text: str) -> str:
    """Entfernt [[tts:...]] und [[tts:text]]...[[/tts:text]] aus Text."""
    # [[tts:...]] oder [[tts:... | channel=signal]] → Inhalt behalten
    text = re.sub(r"\[\[tts:(.*?)(?:\|[^\]]*?)?\]\]", r"\1", text, flags=re.DOTALL)
    # [[tts:text]]...[[/tts:text]] → Inhalt behalten
    text = re.sub(r"\[\[tts:text\]\](.*?)\[\[/tts:text\]\]", r"\1", text, flags=re.DOTALL)
    return text.strip()


class PromptPatcher:
    """Scannt Workspace-Dateien nach problematischen Patterns."""

    PATTERNS = [
        (r"\[\[tts:.*?\]\]", "[[tts:...]] Markup", True),
        (r"\[\[tts:text\]\].*?\[\[/tts:text\]\]", "[[tts:text]] Block", True),
        (r'<tool_call>.*?"name"\s*:\s*"tts".*?</tool_call>', "tool_call tts", True),
        (r'"asVoice"\s*:\s*true', "asVoice:true in tool_call", False),
    ]

    def __init__(self, clawd_base: str, dry_run: bool = False):
        self.clawd_base = Path(clawd_base)
        self.dry_run = dry_run
        self.findings: List[Dict] = []

    def scan(self) -> List[Dict]:
        self.findings = []
        for agent in CONFIG["workspace_agents"]:
            ws = self.clawd_base / f"workspace-{agent}"
            if not ws.exists():
                continue
            for fpath in ws.rglob("*.md"):
                if fpath.is_file():
                    self._scan_file(fpath)
        return self.findings

    # Kontext = Verbots-Regel (z.B. "NIEMALS [[tts:...]]") → kein Finding
    PROHIBITION_CONTEXT = re.compile(
        r"(NIEMALS|Kein|kein|darf nicht|verwenden|ausgeben|nicht ausgeben|technische Einschränkung)",
        re.I
    )

    def _scan_file(self, fpath: Path):
        try:
            content = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            log.warning(f"Kann {fpath} nicht lesen: {e}")
            return
        for regex, desc, fixable in self.PATTERNS:
            for m in re.finditer(regex, content, re.DOTALL):
                # Kontext prüfen: Zeile vor/nach dem Match
                start = max(0, m.start() - 80)
                end = min(len(content), m.end() + 80)
                context = content[start:end]
                if self.PROHIBITION_CONTEXT.search(context):
                    continue  # Verbots-Regel, kein echtes Problem
                self.findings.append({
                    "file": str(fpath),
                    "desc": desc,
                    "match": m.group()[:100],
                    "line": content[:m.start()].count("\n") + 1,
                    "fixable": fixable,
                })

    def fix(self) -> int:
        """Patched nur Dateien, die falsche ANWEISUNGEN enthalten (z.B. 'Füge [[tts]] ein').
        Regel-Dateien mit 'NIEMALS [[tts:...]]' werden nicht geändert."""
        fixed = 0
        seen = set()
        for f in self.findings:
            if not f["fixable"]:
                continue
            fpath = Path(f["file"])
            if str(fpath) in seen:
                continue
            try:
                content = fpath.read_text(encoding="utf-8")
            except Exception:
                continue
            # Nicht patchen wenn es eine Verbots-Regel ist
            if re.search(r"(NIEMALS|Kein|kein|darf nicht|verwenden|ausgeben).*\[\[tts", content, re.I):
                continue
            # Nur wenn es eine Anweisung zum Nutzen von [[tts]] ist (z.B. "Füge [[tts]] ein")
            if re.search(r"(füge|füg|add|use|nutze|output).*\[\[tts", content, re.I):
                new = strip_tts_markup(content)
                if new != content:
                    if not self.dry_run:
                        shutil.copy2(fpath, fpath.with_suffix(fpath.suffix + ".bak"))
                        fpath.write_text(new, encoding="utf-8")
                        fixed += 1
                        log.info(f"Gefixt: {fpath.name}")
                    seen.add(str(fpath))
        return fixed


# ═══════════════════════════════════════════════
#  TEIL 2: CONFIG-VERIFY
# ═══════════════════════════════════════════════

class ConfigVerifier:
    def __init__(self, config: dict):
        self.config = config
        self.results: List[Dict] = []

    def verify_all(self) -> Tuple[int, int, int]:
        self.results = []
        cfg = self.config

        # Binaries
        self._check("ffmpeg", shutil.which("ffmpeg"), "apt install ffmpeg")
        self._check("whisper", shutil.which("whisper") or os.path.isfile(os.path.expanduser("~/.local/bin/whisper")), "pip install openai-whisper")
        self._check("node", shutil.which("node"), "Node.js 22+ für Edge TTS")
        try:
            r = subprocess.run(["edge-tts", "--help"], capture_output=True, timeout=5)
            self._check("edge-tts", r.returncode == 0, "pip install edge-tts")
        except FileNotFoundError:
            self._check("edge-tts", False, "pip install edge-tts")

        # Config
        config_path = Path(cfg["config_file"])
        if config_path.exists():
            with open(config_path) as f:
                data = json.load(f)
            tts = data.get("messages", {}).get("tts", {})
            self._check("messages.tts.auto", tts.get("auto") == "always", "update_clawdbot_voice_config.py ausführen")
            self._check("tools.deny tts", "tts" in data.get("tools", {}).get("deny", []), "tools.deny: [\"tts\"] in Config")
            # Channel-spezifisch: Signal braucht evtl. tts: true (laut Diagnose)
            sig = data.get("channels", {}).get("signal", {})
            # channels.signal.tts ist KEIN gültiger Key (OpenClaw 2026.1) – nicht hinzufügen!
        else:
            self.results.append({"name": "config", "status": "FAIL", "detail": f"{config_path} nicht gefunden", "fix_hint": ""})

        # Workspaces
        clawd = Path(cfg.get("clawd_base", "~/clawd")).expanduser()
        for agent in cfg.get("workspace_agents", []):
            ws = clawd / f"workspace-{agent}"
            self._check(f"workspace-{agent}", ws.exists(), f"Verzeichnis {ws} anlegen")

        passed = sum(1 for r in self.results if r.get("status") == "PASS")
        warned = sum(1 for r in self.results if r.get("status") == "WARN")
        failed = sum(1 for r in self.results if r.get("status") == "FAIL")
        return passed, warned, failed

    def _check(self, name: str, ok: bool, fix_hint: str = ""):
        status = "PASS" if ok else "FAIL"
        self.results.append({"name": name, "status": status, "detail": "OK" if ok else fix_hint, "fix_hint": fix_hint})


# ═══════════════════════════════════════════════
#  TEIL 3: POST-PROCESSOR (für Output-Bereinigung)
# ═══════════════════════════════════════════════

class TTSPostProcessor:
    """Bereinigt Agent-Output: [[tts:...]] → reiner Text."""

    def __init__(self, config: dict):
        self.config = config

    def process(self, text: str) -> dict:
        """Gibt bereinigten Text zurück. Bei [[tts:...]] wird Inhalt extrahiert."""
        result = {"text": text, "had_markup": False, "changes": []}
        # [[tts:...]]
        tts_matches = re.findall(r"\[\[tts:(.*?)(?:\|[^\]]*?)?\]\]", text, re.DOTALL)
        if tts_matches:
            result["had_markup"] = True
            clean = re.sub(r"\[\[tts:(.*?)(?:\|[^\]]*?)?\]\]", r"\1", text, flags=re.DOTALL)
            result["text"] = clean.strip()
            result["changes"].append("[[tts:...]] entfernt")
        # [[tts:text]]...[[/tts:text]]
        if "[[tts:text]]" in text:
            result["had_markup"] = True
            clean = re.sub(r"\[\[tts:text\]\](.*?)\[\[/tts:text\]\]", r"\1", text, flags=re.DOTALL)
            result["text"] = clean.strip()
            result["changes"].append("[[tts:text]] Block entfernt")
        return result


# ═══════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="ClawdBot Voice/TTS Triple-Fix (VM102)")
    parser.add_argument("--check", action="store_true", help="Nur prüfen")
    parser.add_argument("--fix", action="store_true", help="Fixes anwenden")
    parser.add_argument("--dry-run", action="store_true", help="Zeigen was geändert würde")
    parser.add_argument("--base-dir", type=str, help="Clawd-Base (default: ~/clawd)")
    args = parser.parse_args()

    config = CONFIG.copy()
    if args.base_dir:
        config["clawd_base"] = args.base_dir

    print("""
╔══════════════════════════════════════════════╗
║  ClawdBot Voice/TTS Triple-Fix (VM102)       ║
║  1) Prompt-Patch  2) Config-Verify  3) Proc ║
╚══════════════════════════════════════════════╝
""")

    # TEIL 2: Config-Verify
    print("=" * 50)
    print("  TEIL 2: CONFIG-VERIFY")
    print("=" * 50)
    verifier = ConfigVerifier(config)
    passed, warned, failed = verifier.verify_all()
    for r in verifier.results:
        icon = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌"}.get(r.get("status", ""), "?")
        print(f"  {icon} {r.get('name', '?')}: {r.get('detail', '')}")
    print(f"\n  Ergebnis: {passed} OK, {failed} Fehler\n")

    # TEIL 1: Prompt-Patch
    print("=" * 50)
    print("  TEIL 1: PROMPT-PATCH (Scan)")
    print("=" * 50)
    patcher = PromptPatcher(config["clawd_base"], dry_run=args.dry_run or not args.fix)
    findings = patcher.scan()
    if not findings:
        print("  ✅ Keine problematischen Patterns in Workspace-Dateien gefunden")
    else:
        for f in findings:
            print(f"  ⚠️ {Path(f['file']).name}:{f['line']} → {f['desc']}")
            print(f"       Match: {f['match'][:70]}...")
        if args.fix:
            fixed = patcher.fix()
            print(f"\n  Gefixt: {fixed} Dateien")

    # TEIL 3: Post-Processor Test
    print("\n" + "=" * 50)
    print("  TEIL 3: POST-PROCESSOR (Selbsttest)")
    print("=" * 50)
    proc = TTSPostProcessor(config)
    test = 'Hallo! [[tts:Dies ist ein Test.]] Wie geht es dir?'
    result = proc.process(test)
    print(f"  Input:  {test[:60]}...")
    print(f"  Output: {result['text'][:60]}...")
    if result["changes"]:
        print(f"  → {result['changes']}")

    print("\n" + "=" * 50)
    print("  ZUSAMMENFASSUNG")
    print("=" * 50)
    print(f"  Config: {passed}✅ {failed}❌  |  Prompts: {len(findings)} Findings")
    if not args.fix and findings:
        print(f"\n  Nächster Schritt: python3 clawdbot_voice_fix.py --fix")
    print()


if __name__ == "__main__":
    main()
