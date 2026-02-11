#!/bin/bash
# Einmalig auf Spark ausführen: deaktiviert draw_layout_bbox in MinerU (Workaround pypdf "negative seek").
# Aufruf auf Spark: bash patch_mineru_draw_bbox.sh
# Von Windows (PowerShell, LF-Pipe): siehe HD_WORKER_HANDOVER.md

set -e
FILE="$HOME/srv/hd-worker/.venv/lib/python3.12/site-packages/mineru/cli/common.py"
if [[ ! -f "$FILE" ]]; then
  echo "Datei nicht gefunden: $FILE"
  exit 1
fi

if grep -q "f_draw_layout_bbox = False  # Workaround" "$FILE"; then
  echo "Bereits gepatcht."
  exit 0
fi

python3 << 'PY'
path = "/home/sparkuser/srv/hd-worker/.venv/lib/python3.12/site-packages/mineru/cli/common.py"
with open(path) as f:
    t = f.read()
old = "    if f_draw_layout_bbox:"
new = "    f_draw_layout_bbox = False  # Workaround: pypdf negative seek bei einigen PDFs\n    if f_draw_layout_bbox:"
if new not in t and old in t:
    with open(path, "w") as f:
        f.write(t.replace(old, new, 1))
    print("Patched OK")
else:
    print("Nichts geändert (bereits patched oder Muster nicht gefunden)")
PY
