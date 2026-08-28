#!/usr/bin/env bash
# Einmaliger Batch: ESF-Folien-PDFs → strukturiertes Markdown (MinerU auf Spark).
# Kein HD-Worker / keine Supabase-Pipeline — nur lokale Extraktion für Flora-Lernmaterial.
#
# Voraussetzungen (Spark):
#   - venv mit MinerU, z. B. ~/srv/hd-worker/.venv (requirements-hd-worker-spark.txt)
#   - genug VRAM: ggf. SGLang stoppen vor dem Lauf (siehe infrastructure/spark/hd_worker_ops.md)
#
# Nutzung:
#   ./mineru_batch_esf.sh /pfad/zu/pdfs /pfad/zu/output
#
# Beispiel (PDFs vorher per scp nach Spark):
#   scp ~/Downloads/*ESF* user@spark:~/batch/esf/input/
#   ssh user@spark 'bash ~/ai_projects/infrastructure/spark/scripts/esf/mineru_batch_esf.sh ~/batch/esf/input ~/batch/esf/output'

set -euo pipefail

INPUT_DIR="${1:?Usage: $0 <input_dir> <output_dir>}"
OUTPUT_DIR="${2:?Usage: $0 <input_dir> <output_dir>}"
VENV="${MINERU_VENV:-$HOME/srv/hd-worker/.venv}"
BACKEND="${MINERU_BACKEND:-hybrid-auto-engine}"
DEVICE="${MINERU_DEVICE:-cuda}"
LANG="${MINERU_LANG:-latin}"

MINERU="${VENV}/bin/mineru"
if [[ ! -x "$MINERU" ]]; then
  echo "MinerU nicht gefunden: $MINERU" >&2
  echo "MINERU_VENV setzen oder venv installieren." >&2
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

# Hybrid: PyMuPDF für textlastige Decks, MinerU für bild-/formellastige
PYMUPDF_ONLY=(
  "ESF_EINFUHRUNG"
  "ESF_EINFÜHRUNG"
)

use_pymupdf() {
  local base
  base="$(basename "$1" .pdf)"
  for prefix in "${PYMUPDF_ONLY[@]}"; do
    [[ "$base" == *"$prefix"* ]] && return 0
  done
  return 1
}

pymupdf_extract() {
  local pdf="$1"
  local out_md="$2"
  "$VENV/bin/python" - <<'PY' "$pdf" "$out_md"
import sys
from pathlib import Path
import fitz
pdf, out = sys.argv[1], Path(sys.argv[2])
doc = fitz.open(pdf)
parts = [f"# {Path(pdf).stem}\n"]
for i, page in enumerate(doc, 1):
    text = (page.get_text() or "").strip()
    parts.append(f"\n## Folie {i}\n\n{text if text else '_(kein extrahierbarer Text — MinerU prüfen)_'}\n")
out.write_text("\n".join(parts), encoding="utf-8")
print(f"PyMuPDF → {out} ({len(doc)} Seiten)")
PY
}

run_mineru() {
  local pdf="$1"
  local stem="$2"
  local work="${OUTPUT_DIR}/.work_${stem}"
  rm -rf "$work"
  mkdir -p "$work"

  echo "==> MinerU: $(basename "$pdf")"
  "$MINERU" -p "$pdf" -o "$work" -b "$BACKEND" --device "$DEVICE" --lang "$LANG"

  local md
  md="$(find "$work" -name '*.md' -type f | head -1)"
  if [[ -z "$md" ]]; then
    echo "WARN: Keine .md von MinerU — Fallback PyMuPDF" >&2
    pymupdf_extract "$pdf" "${OUTPUT_DIR}/${stem}.md"
    return
  fi

  cp "$md" "${OUTPUT_DIR}/${stem}.md"
  echo "MinerU → ${OUTPUT_DIR}/${stem}.md"
}

shopt -s nullglob
pdfs=("$INPUT_DIR"/*.pdf)
if [[ ${#pdfs[@]} -eq 0 ]]; then
  echo "Keine PDFs in $INPUT_DIR" >&2
  exit 1
fi

for pdf in "${pdfs[@]}"; do
  stem="$(basename "$pdf" .pdf)"
  if use_pymupdf "$pdf"; then
    echo "==> PyMuPDF (textlastig): $(basename "$pdf")"
    pymupdf_extract "$pdf" "${OUTPUT_DIR}/${stem}.md"
  else
    run_mineru "$pdf" "$stem"
  fi
done

echo ""
echo "Fertig. Output:"
ls -la "$OUTPUT_DIR"/*.md 2>/dev/null || true
echo ""
echo "Qualitätsprobe: 5 Folien pro Deck manuell gegen PDF prüfen (Formeln, Tabellen)."
