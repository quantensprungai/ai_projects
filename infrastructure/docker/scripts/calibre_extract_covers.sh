#!/usr/bin/env bash
# Run on pve: extract covers for Calibre library (PDF/EPUB/MOBI).
set -euo pipefail
LIB="${1:-/mnt/bigdata/archive/nomad-storage/books}"
cd "$LIB"
updated=0
skipped=0
while IFS= read -r id; do
  [[ -z "$id" ]] && continue
  dir=$(find "$LIB" -maxdepth 3 -type d -name "* (${id})" 2>/dev/null | head -1)
  if [[ -z "$dir" ]]; then
    skipped=$((skipped + 1))
    continue
  fi
  if [[ -f "$dir/cover.jpg" ]] && [[ -s "$dir/cover.jpg" ]]; then
    skipped=$((skipped + 1))
    continue
  fi
  bookfile=$(find "$dir" -maxdepth 1 -type f \( -iname '*.pdf' -o -iname '*.epub' -o -iname '*.mobi' \) | head -1)
  if [[ -z "$bookfile" ]]; then
    skipped=$((skipped + 1))
    continue
  fi
  tmp="$dir/_cover_tmp.jpg"
  if ebook-meta "$bookfile" --get-cover "$tmp" 2>/dev/null && [[ -s "$tmp" ]]; then
    mv -f "$tmp" "$dir/cover.jpg"
    calibredb set_cover --cover "$dir/cover.jpg" "$id" --with-library="$LIB" >/dev/null 2>&1 || true
    updated=$((updated + 1))
    echo "cover ok id=$id"
  else
    rm -f "$tmp"
    skipped=$((skipped + 1))
  fi
done < <(calibredb list --for-machine --fields=id --with-library="$LIB" | cut -f1)
echo "Done covers: updated=$updated skipped=$skipped"
