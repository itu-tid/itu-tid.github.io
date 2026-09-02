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

# Every note ends with the same two or three sections, so in a chapter of six
# notes they are a third of the contents page and carry none of the argument.
# They are also the sections nobody needs an index for: always last, always in
# the same place. Dropped from the contents only -- the sections stay.
# Matched on the anchor slug rather than the link text: pandoc hard-wraps the
# generated markup, so "Exam Questions" can arrive as "Exam\nQuestions". The
# -\d+ suffix is pandoc deduplicating ids across the concatenated notes.
BOILERPLATE = ("references", "exam-questions", "meta", "project-work")
html, dropped = re.subn(
    r'<li>\s*<a\s[^>]*href="#(?:' + "|".join(BOILERPLATE) + r')(?:-\d+)?"[^>]*>.*?</a>\s*</li>\s*',
    "", html, flags=re.S)
print(f"  contents: {dropped} boilerplate entries dropped", file=sys.stderr)

# A subsection that will not fit in what is left of the page starts a new one,
# rather than breaking two lines in and stranding its heading or its lead-in
# sentence overleaf. Chrome ignores break-after:avoid entirely, so this is done
# by wrapping each h3 with its content and keeping the wrapper whole --
# break-inside is the one break property Chrome implements. A subsection taller
# than a page cannot be kept whole, and Chrome falls back to breaking it as
# before, which is what the orphans/widows on `pre` are there for.
body_at = html.index("</nav>") + len("</nav>") if "</nav>" in html else 0
head, body = html[:body_at], html[body_at:]
kept = 0

def wrap(chunk, tag, stop_at):
    """Wrap `tag` and everything under it, up to the next heading in stop_at."""
    global kept
    out = []
    for part in re.split(rf'(?=<{tag}\b)', chunk):
        if not part.startswith(f"<{tag}"):
            out.append(part); continue
        end = re.search(rf'<h[{stop_at}]\b', part)
        inner, rest = (part[:end.start()], part[end.start():]) if end else (part, "")
        out.append(f'<section class="keep-together">{inner}</section>{rest}')
        kept += 1
    return "".join(out)

# A heading that will not fit with its opening material starts a new page rather
# than breaking two lines in and stranding its lead-in sentence overleaf. Both
# levels need it: h3 for a subsection, and h2 for whatever a section says before
# its first subsection. Chrome ignores break-after:avoid entirely, so this works
# by wrapping and keeping the wrapper whole -- break-inside is the one break
# property Chrome implements. Anything taller than a page cannot be kept whole
# and falls back to breaking as before, which the orphans/widows on `pre` cover.
# First the smallest unit: a sentence ending in a colon is introducing the
# listing under it, and the two must never be split. This is the fallback for a
# section too tall to keep whole, where the break has to land somewhere.
body, pairs = re.subn(
    r'(<p>(?:(?!</p>).)*?:</p>)\s*(<div class="sourceCode".*?</div>)',
    r'<section class="keep-together">\1\2</section>', body, flags=re.S)
print(f"  lead-ins bound to their listing: {pairs}", file=sys.stderr)

body = wrap(body, "h3", "12")          # a subsection, up to the next h1 or h2
body = wrap(body, "h2", "123")         # a section's preamble, up to its first h3
html = head + body
print(f"  headings kept with their content: {kept}", file=sys.stderr)
p.write_text(html, encoding="utf-8")
PY

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT" --virtual-time-budget=10000 \
  "file://$TMP/chapter.html" 2>/dev/null

echo "$OUT  ($(du -h "$OUT" | cut -f1))"
