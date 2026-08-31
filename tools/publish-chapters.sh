#!/bin/bash
# Publish the built chapters to the itu-tid/chapters repository.
#
# That repository is *rewritten* rather than appended to: each publish replaces
# its single commit and force-pushes. A rebuilt PDF is a megabyte of new binary,
# so an ordinary history would grow by ~19 MB every time a note changed. There
# is nothing in it worth a history anyway -- the history lives with the source.

set -e
[ -f ~/.local_envvars.sh ] && source ~/.local_envvars.sh
DIR="${TID_PDF_OUT:?set TID_PDF_OUT to the chapters clone}"
cd "$DIR"

# The PDFs are named Week-NN.pdf so that a retitled week keeps its URL, which
# means the titles have to come from somewhere: build-pdfs writes chapters.json
# beside them, and it is inlined here rather than fetched, so the page still
# works opened straight off disk.
python3 <<'PY'
import json, re
from pathlib import Path
chapters = json.loads(Path("chapters.json").read_text(encoding="utf-8"))
p = Path("index.html")
# rewrite the whole assignment, not a one-shot placeholder, so publishing twice
# updates the list the second time as well
p.write_text(re.sub(r"const chapters = .*?\n\];",
                    lambda _: "const chapters = " + json.dumps(chapters, indent=2, ensure_ascii=False) + ";",
                    p.read_text(encoding="utf-8"), count=1, flags=re.S), encoding="utf-8")
PY

git checkout -q --orphan publish 2>/dev/null || git checkout -q --orphan publish-$$
git add -A
git -c user.name="$(git -C "$TID_REPO" config user.name)" \
    -c user.email="$(git -C "$TID_REPO" config user.email)" \
    commit -q -m "Chapters, built $(date +%Y-%m-%d) from itu-tid.github.io"
git branch -q -M main
git push -q --force origin main
echo "publish-chapters: $(ls Week-*.pdf | wc -l | tr -d ' ') chapters pushed"
