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

# the index lists whatever is actually there, so a renamed week cannot 404
FILES=$(ls Week-*.pdf 2>/dev/null | python3 -c "import json,sys; print(json.dumps([l.strip() for l in sys.stdin]))")
python3 - "$FILES" <<'PY'
import re, sys
from pathlib import Path
p = Path("index.html")
# rewrite the whole assignment, not a one-shot placeholder, so publishing twice
# updates the list the second time as well
p.write_text(re.sub(r"const files = .*?;",
                    lambda _: f"const files = {sys.argv[1]};",
                    p.read_text(), count=1, flags=re.S))
PY

git checkout -q --orphan publish 2>/dev/null || git checkout -q --orphan publish-$$
git add -A
git -c user.name="$(git -C "$TID_REPO" config user.name)" \
    -c user.email="$(git -C "$TID_REPO" config user.email)" \
    commit -q -m "Chapters, built $(date +%Y-%m-%d) from itu-tid.github.io"
git branch -q -M main
git push -q --force origin main
echo "publish-chapters: $(ls Week-*.pdf | wc -l | tr -d ' ') chapters pushed"
