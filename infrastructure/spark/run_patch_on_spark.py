#!/usr/bin/env python3
"""Führt den MinerU-Patch einmal auf Spark aus (per SSH). Kein .sh, kein CRLF-Problem."""
import base64
import subprocess
import sys

REMOTE_PY = """
path = "/home/sparkuser/srv/hd-worker/.venv/lib/python3.12/site-packages/mineru/cli/common.py"
with open(path) as f:
    t = f.read()
old = "    if f_draw_layout_bbox:"
new = "    f_draw_layout_bbox = False  # Workaround: pypdf negative seek bei einigen PDFs\\n    if f_draw_layout_bbox:"
if new not in t and old in t:
    with open(path, "w") as f:
        f.write(t.replace(old, new, 1))
    print("Patched OK")
else:
    print("Nichts geändert (bereits patched oder Muster nicht gefunden)")
"""

b64 = base64.b64encode(REMOTE_PY.strip().encode()).decode()
host = sys.argv[1] if len(sys.argv) > 1 else "sparkuser@100.96.115.1"
port = "2222"
# Base64 durchreichen, auf Spark dekodieren und an python3 pipen – keine Quote-Probleme
remote_cmd = f"echo {b64} | base64 -d | python3"
cmd = ["ssh", "-p", port, host, remote_cmd]
print("Running: ssh -p", port, host, "...")
r = subprocess.run(cmd)
sys.exit(r.returncode)
