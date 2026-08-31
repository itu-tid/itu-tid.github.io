#!/usr/bin/env python3
"""Render one PDF chapter per week, from the notes the syllabus names.

    export TID_VAULT="…/Megavault/teaching/technical interaction design/"
    python3 tools/build-pdfs.py                     # every week
    python3 tools/build-pdfs.py 1 2                 # just these
    python3 tools/build-pdfs.py --changed a.md b.md # whichever weeks use those notes
    python3 tools/build-pdfs.py --book              # all of it as one, into ./pdf

The week -> notes mapping is not written down here. It is read out of the
syllabus's `GH:` rows, the same source that decides what the published page
says, so a note that moves between weeks moves its chapter with it and there is
no second list to forget to update.

Output goes to $TID_PDF_OUT if set -- the shared iCloud folder students are
given -- and to ./pdf otherwise. Either way it is one file per week, named for
the week and its title, and never committed: a rebuilt PDF is a megabyte of new
binary, and fourteen of them every time a note changes would bury the history.

Weeks whose notes all live on learnIT produce nothing, and say so.
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).parent.parent))
import build  # noqa: E402  -- reuse the syllabus parser rather than a second one

ROOT = Path(__file__).parent.parent
OUT = Path(os.environ.get("TID_PDF_OUT") or ROOT / "pdf")
SUBTITLE = "Technical Interaction Design · ITU · Autumn 2026"


def slug(text):
    text = re.sub(r"[*`_]", "", text)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def weeks():
    """(number, title, [note paths]) for every week that has notes in the repo."""
    doc = build.parse(build.staff_only(build.expand(build.SRC.read_text("utf-8")), keep=True))
    for heading, body in doc["weeks"]:
        m = re.match(r"Week 0*(\d+) · ", heading)
        if not m:
            continue
        prose = [ln.strip() for ln in body if ln.strip() and not ln.strip().startswith("- ")]
        title = prose[0].strip("* ")
        gh = dict(build.fields(body)).get("GH", "")
        notes, seen = [], set()
        for target in re.findall(r"\]\(([^)]+)\)", gh):
            path = ROOT / unquote(target.split("#")[0])
            # a link to a folder means every note in it, in name order -- that is
            # how the syllabus points at the ten heuristic counterexamples
            found = sorted(path.glob("*.md")) if path.is_dir() else [path]
            for f in found:
                if f.suffix == ".md" and f.exists() and f not in seen:
                    seen.add(f)
                    notes.append(f)
        yield int(m.group(1)), title, notes


def weeks_using(paths):
    """Week numbers whose chapter includes any of these notes."""
    targets = {Path(p).resolve() for p in paths}
    return {num for num, _, notes in weeks()
            if targets & {n.resolve() for n in notes}}


def book():
    """Every chapter, in course order, as one document.

    Written to ./pdf rather than $TID_PDF_OUT, deliberately: this is a review
    tool, not something students are given. Read end to end it shows up
    inconsistencies that are invisible one note at a time -- uneven voice,
    chapters in an order that made sense per week and not in sequence. The
    per-week chapters remain the thing that gets published.
    """
    notes, seen = [], set()
    for num, _, ns in sorted(weeks()):
        for n in ns:
            if n not in seen:
                seen.add(n)
                notes.append(n)
    if not notes:
        sys.exit("build-pdfs: no notes found")
    target = ROOT / "pdf" / "Technical-Interaction-Design.pdf"
    target.parent.mkdir(exist_ok=True)
    subprocess.run(
        [str(ROOT / "tools/md-to-pdf.sh"), str(target),
         "Technical Interaction Design", SUBTITLE, *map(str, notes)],
        check=True, cwd=ROOT)
    print(f"\n{len(notes)} notes into one book at {target}")


def main(wanted):
    if not os.environ.get("TID_VAULT"):
        sys.exit("build-pdfs: set TID_VAULT — the syllabus source lives in the vault")
    OUT.mkdir(exist_ok=True)
    built = skipped = 0
    for num, title, notes in weeks():
        if wanted and num not in wanted:
            continue
        if not notes:
            print(f"  week {num:2}  — no notes in the repo (learnIT only), skipped")
            skipped += 1
            continue
        target = OUT / f"Week-{num:02d}-{slug(title)}.pdf"
        subprocess.run(
            [str(ROOT / "tools/md-to-pdf.sh"), str(target),
             f"Week {num} · {re.sub(r'[*]', '', title)}", SUBTITLE, *map(str, notes)],
            check=True, cwd=ROOT)
        built += 1
    # A week that gets retitled is written under a new name, and the old file
    # would otherwise sit there forever -- publish-chapters builds its index
    # from whatever is in the directory, so the chapter would be listed twice.
    # Expected covers every week, not only the ones just built, so this cleans
    # up after a --changed run as well.
    expected = {f"Week-{n:02d}-{slug(t)}.pdf" for n, t, notes in weeks() if notes}
    for stale in sorted(set(OUT.glob("Week-*.pdf")) - {OUT / e for e in expected}):
        stale.unlink()
        print(f"  removed {stale.name} — no week produces it any more")

    print(f"\n{built} chapter(s) written to {OUT}, {skipped} week(s) skipped")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--book":
        if not os.environ.get("TID_VAULT"):
            sys.exit("build-pdfs: set TID_VAULT — the syllabus source lives in the vault")
        book()
    elif args and args[0] == "--changed":
        if not os.environ.get("TID_VAULT"):
            sys.exit("build-pdfs: set TID_VAULT — the syllabus source lives in the vault")
        affected = weeks_using(args[1:])
        if not affected:
            print("build-pdfs: nothing changed that any chapter uses")
            sys.exit(0)
        main(affected)
    else:
        main({int(a) for a in args})
