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
ISSUE_URL="https://github.com/itu-tid/itu-tid.github.io/issues/new"
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
  python3 - "$note" "$copy" "$SOURCE_URL/$rel" "$rel" "$ISSUE_URL" "$REV" <<'PY'
import sys
from pathlib import Path
from urllib.parse import quote
src, dst, url, rel, issues, rev = sys.argv[1:7]
lines = Path(src).read_text(encoding="utf-8").split("\n")
title = Path(rel).stem.replace("-", " ")
# Prefilled, because the cost of reporting something is what decides whether it
# gets reported at all -- and because the commit tells us which text they read.
new_issue = (f'{issues}?title={quote(title + ": ")}'
             f'&body={quote(f"Which part: \n\nWhat was unclear: \n\n---\n{rel} at {rev}\n")}')
link = (f'<span class="source">Source: [{rel}]({url}) — something unclear? '
        f'[Open an issue]({new_issue}), or send a pull request.</span>')
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

# First the smallest unit: a sentence ending in a colon introduces the listing
# under it, and the two must never be split.
body, pairs = re.subn(
    r'(<p>(?:(?!</p>).)*?:</p>)\s*(<div class="sourceCode".*?</div>)',
    r'<section class="keep-together">\1\2</section>', body, flags=re.S)

def top_level(chunk):
    """Split into top-level elements, tracking nesting so a div inside a
    section does not end it early."""
    out, depth, buf = [], 0, ""
    for tok in re.split(r'(<[^>]+>)', chunk):
        buf += tok
        if tok.startswith("<") and not tok.startswith(("</", "<!")) and not tok.endswith("/>"):
            if not re.match(r'<(br|hr|img|input|meta|link)\b', tok):
                depth += 1
        elif tok.startswith("</"):
            depth -= 1
            if depth == 0:
                out.append(buf); buf = ""
    if buf.strip():
        out.append(buf)
    return out

# Then: a heading travels with the first two blocks under it. Keeping the whole
# subsection together was tried and gives pages a fifth full -- books do not do
# that. They keep a heading from being stranded and let the rest break.
els = top_level(body)
out, kept, i = [], 0, 0
while i < len(els):
    if re.match(r'\s*<h[234]\b', els[i]):
        # Stop at the next heading, whatever its level. Swallowing one would
        # bury it in a break-inside:avoid wrapper, and a heading inside one of
        # those loses its own break-before -- which is how a note stopped
        # starting on a fresh page.
        unit = [els[i]]
        for nxt in els[i + 1:i + 3]:
            if re.match(r'\s*<h[1-6]\b', nxt):
                break
            unit.append(nxt)
        i += len(unit)
        out.append('<section class="keep-together">' + "".join(unit) + "</section>")
        kept += 1
    else:
        out.append(els[i]); i += 1
html = head + "".join(out)
print(f"  lead-ins bound to their listing: {pairs}", file=sys.stderr)
print(f"  headings kept with what follows: {kept}", file=sys.stderr)
p.write_text(html, encoding="utf-8")
PY

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT" --virtual-time-budget=10000 \
  "file://$TMP/chapter.html" 2>/dev/null

echo "$OUT  ($(du -h "$OUT" | cut -f1))"
