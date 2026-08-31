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
#
# A printed chapter is a copy, and a copy goes stale. So each one carries the
# commit it was built from and a link back to the live version, and every note
# inside it links to its own source file -- a student who finds a mistake can go
# and fix it rather than only mention it.

set -e
cd "$(git rev-parse --show-toplevel)"

OUT="$1"; TITLE="$2"; SUBTITLE="$3"; shift 3
case "$OUT" in /*) ;; *) OUT="$PWD/$OUT";; esac
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "md-to-pdf: Google Chrome not found" >&2; exit 1; }

SOURCE_URL="https://github.com/itu-tid/itu-tid.github.io/blob/main"
CHAPTER_URL="https://itu-tid.github.io/lecture-notes-pdf"
REV="$(git rev-parse --short HEAD)"
BUILT="$(date '+%-d %B %Y')"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Each note is copied with a link to its source spliced in under its title. The
# copies live in $TMP, so every original directory has to join --resource-path
# or the images stop resolving.
RESOURCE_PATH="$PWD"
COPIES=()
for note in "$@"; do
  rel="${note#$PWD/}"; rel="${rel#./}"   # build-pdfs hands us absolute paths
  copy="$TMP/$(echo "$rel" | tr '/' '_')"
  python3 - "$note" "$copy" "$SOURCE_URL/$rel" "$rel" <<'PY'
import sys
from pathlib import Path
src, dst, url, rel = sys.argv[1:5]
lines = Path(src).read_text(encoding="utf-8").split("\n")
link = f'<span class="source">Source: [{rel}]({url}) — issues and pull requests welcome.</span>'
fence = False
for i, line in enumerate(lines):
    if line.lstrip().startswith("```"):
        fence = not fence          # a `# ` inside a fence is a shell comment
    elif line.startswith("# ") and not fence:
        lines.insert(i + 1, "\n" + link)
        break
else:
    lines.insert(0, link + "\n")
Path(dst).write_text("\n".join(lines), encoding="utf-8")
PY
  COPIES+=("$copy")
  RESOURCE_PATH="$RESOURCE_PATH:$(dirname "$note"):$(dirname "$note")/images"
done

pandoc "${COPIES[@]}" \
  --standalone --embed-resources \
  --css "$PWD/tools/print.css" \
  --resource-path "$RESOURCE_PATH" \
  --metadata title="$TITLE" \
  --metadata subtitle="$SUBTITLE" \
  --toc --toc-depth=2 --metadata toc-title="Contents" \
  --shift-heading-level-by=0 \
  -f gfm+footnotes+smart -t html5 \
  -o "$TMP/chapter.html"

# The colophon goes inside the title block so it sits with the title at the foot
# of page one. pandoc has no metadata field that would carry a link, so it is
# spliced into the rendered header instead of templated in.
python3 - "$TMP/chapter.html" "$CHAPTER_URL/$(basename "$OUT")" "$REV" "$BUILT" <<'PY'
import re, sys
from pathlib import Path
from urllib.parse import quote
page, url, rev, built = sys.argv[1:5]
p = Path(page); html = p.read_text(encoding="utf-8")
# The URL is the link text, because a printed chapter is the case this line
# exists for and a printed link is unclickable. Typeable beats clickable here,
# scheme included, on its own line so it is unmistakably a URL.
colophon = (f'<p class="colophon">Built {built} · commit <code>{rev}</code><br>'
            f'Latest version: <a href="{quote(url, safe=":/")}">{url}</a></p>')
html, n = re.subn(r'(<p class="subtitle">.*?</p>)', r'\1' + colophon, html, count=1, flags=re.S)
if not n:
    sys.exit("md-to-pdf: no subtitle in the rendered header to hang the colophon on")
p.write_text(html, encoding="utf-8")
PY

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT" --virtual-time-budget=10000 \
  "file://$TMP/chapter.html" 2>/dev/null

echo "$OUT  ($(du -h "$OUT" | cut -f1))"
