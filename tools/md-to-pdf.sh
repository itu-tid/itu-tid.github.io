#!/bin/bash
# Render one or more markdown notes into a single PDF chapter.
#
#   tools/md-to-pdf.sh OUT.pdf "Title" "Subtitle" note.md [note.md ...]
#
# pandoc turns the markdown into one HTML document, tools/print.css gives it the
# same typefaces and palette as the published syllabus, and Chrome prints it.
# Chrome rather than LaTeX because these notes are full of box-drawing
# characters, arrows and long lines: pdflatex dies on the first, tectonic drops
# the second, and both clip the third off the right margin.

set -e
cd "$(git rev-parse --show-toplevel)"

OUT="$1"; TITLE="$2"; SUBTITLE="$3"; shift 3
case "$OUT" in /*) ;; *) OUT="$PWD/$OUT";; esac
FIRST="$1"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "md-to-pdf: Google Chrome not found" >&2; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# --resource-path lets pandoc find images that sit next to their notes
pandoc "$@" \
  --standalone --embed-resources \
  --css "$PWD/tools/print.css" \
  --resource-path "$(dirname "$FIRST"):$(dirname "$FIRST")/images:$PWD" \
  --metadata title="$TITLE" \
  --metadata subtitle="$SUBTITLE" \
  --toc --toc-depth=2 --metadata toc-title="Contents" \
  --shift-heading-level-by=0 \
  -f gfm+footnotes+smart -t html5 \
  -o "$TMP/chapter.html"

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT" --virtual-time-budget=10000 \
  "file://$TMP/chapter.html" 2>/dev/null

echo "$OUT  ($(du -h "$OUT" | cut -f1))"
