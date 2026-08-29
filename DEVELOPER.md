# Working on this repo

For whoever maintains the course. Students need none of it.

## The syllabus is built, and its source is not here

`syllabus.html` is generated. The markdown it comes from lives at
`$TID_VAULT/2026-syllabus.md`, in the Obsidian vault, **not in this repository** — because
it carries `%%staff asides%%` and `New:` / `Status:` rows that are notes between the people
teaching the course. Keeping the source here and stripping it on the way out would have
been theatre: the markdown is the original, the page only a copy of it.

```bash
export TID_VAULT="…/Megavault/teaching/technical interaction design/"
python3 build.py
```

That writes two pages from the one source:

| | |
|---|---|
| `./syllabus.html` | the students' page. Committed, and what GitHub Pages serves. |
| `$TID_VAULT/2026-syllabus-internal.html` | ours, with everything left in. Stays in the vault. |

Edit the markdown in the vault for content and `syllabus.template.html` for design. Never
edit either generated page by hand — the next build overwrites it.

### Marking a passage as ours

Three mechanisms, all resolved by `staff_only()` in `build.py`:

- **`%%…%%`** — an inline aside, dropped from the student page. Use it for spans *inside*
  a paragraph or list item, not for whole paragraphs: an emptied paragraph still renders
  as an empty one.
- **`- **New:** …`** — a badge on the staff page, absent from the student one. What still
  has to be written for a given week.
- **`- **Status:** …`** — never rendered on either page. Planning state.

**In the notes, `%%…%%` does nothing.** That syntax is Obsidian's, and only `build.py`
understands it — so a `%%TODO%%` left in a lecture note is invisible while you write it
and then published to students verbatim, on GitHub and in the PDF chapter. Use an HTML
comment instead:

```markdown
<!-- TODO: this example is still the Counter, not the to-do -->
```

Hidden in Obsidian, hidden on GitHub, hidden in the chapter. Better still, put the note in
that week's plan in the vault, where you will actually see it when preparing.

### The pre-commit hook is what replaced the Action

There was a GitHub Action. It went when the source left the repo, because it cannot build
from a file it cannot see. Its replacement is local:

```bash
git config core.hooksPath git-hooks   # once per clone
```

`git-hooks/pre-commit` rebuilds `syllabus.html` from the vault before **every** commit and
stages it if it changed — so it catches a stale page even when you are committing something
else entirely, which is the case you would otherwise miss. Without `TID_VAULT` set — a
co-teacher's clone — it does nothing and lets the commit through, because there is nothing
it could build.

That leaves exactly one gap: edit the syllabus in the vault and never commit anything, and
the published page stays behind until your next commit. Run `python3 build.py` and commit
if you want it out sooner.

## PDF chapters

One PDF per week, for linking from learnIT, built from the same notes the syllabus names:

```bash
python3 tools/build-pdfs.py        # every week
python3 tools/build-pdfs.py 1 2    # just these
```

Output goes to **`$TID_PDF_OUT`** — a clone of
[itu-tid/lecture-notes-pdf](https://github.com/itu-tid/lecture-notes-pdf), published at
<https://itu-tid.github.io/lecture-notes-pdf/> — and to `./pdf` if that is unset. **The
chapters are never committed to this repository.** Each rebuild is about a megabyte of new
binary per week, and fourteen of them every time a note changes would bury the history in
a term.

`tools/publish-chapters.sh` pushes them, and it **rewrites that repository rather than
appending to it**: every publish replaces its single commit and force-pushes, so the
binaries never accumulate there either. Nothing in it deserves a history — the history
lives here, with the source. It also regenerates `index.html` from whatever files are
actually present, so a renamed week cannot leave a dead link behind.

iCloud was tried first and failed the only test that mattered: a shared-folder link shows
non-Apple visitors a sign-in wall and no file listing at all. Asking a cohort to create an
Apple ID to read the lecture notes was not a trade worth making.

The week → notes mapping is not written down anywhere in the tool: it is read out of the
syllabus's `GH:` rows, so a note that moves between weeks moves its chapter with it. A
link to a folder means every note inside it, in name order — that is how week 7 picks up
the ten heuristic counterexamples.

### You do not have to remember to run it

`git-hooks/post-commit` does it for you: it looks at which notes the commit touched, works
out which chapters use them, rebuilds only those, and publishes — all in the background.

Post-commit rather than pre-commit precisely *because* the PDFs are not in the repository —
they do not have to exist before the commit is made, so the commit returns instantly and
the chapters catch up a minute later. Progress goes to `$TMPDIR/tid-pdf-rebuild.log`.

**How it works, and why not LaTeX.** `tools/md-to-pdf.sh` runs pandoc to turn the notes
into one HTML document, applies `tools/print.css`, and prints it with headless Chrome.
The obvious route — pandoc straight to PDF — was tried first and lost: `pdflatex` dies on
the box-drawing characters in the Vite project tree, `tectonic` survives those but drops
the `→` in the VS Code menu paths, and both clip long code lines off the right margin.
Chrome wraps code, renders every glyph, and lets the chapters use the same typefaces and
palette as the published syllabus.

Known gaps: no page numbers (Chrome's headless PDF exposes no way to add them without
also stamping a `file://` URL in the footer), and the Google Fonts import means the first
build on a cold cache is slower.

## What else lives in the vault

The split is by kind, not by course: this repo holds material other people write into and
that gets built; the vault holds the thinking. Nothing syncs between them, because the two
sets do not overlap — `build.py` is the only bridge, and it only ever writes outward.

    2026-syllabus.md              the source above
    2026-syllabus-internal.html   the staff page it generates
    2026-planning.md              what is undecided, and why
    2026-redesign-handoff.md      the brief the 2026 redesign started from
    2026-lecture-1-opening.md     delivery notes for the first lecture
    2026-lecture-14-closing.md    and for the last one
    2026-inbox.md · 2026-backlog.md
    2026-repo-history-before-purge.bundle

That last one is a full clone of this repository as it stood before staff notes, student
names and an external censor's email address were stripped out of its history. `git clone`
it if you ever need to see how the syllabus evolved.

## Notes

Flat inside `Lectures/Technical/` and `Lectures/Interaction-Design/`. Filenames do not
encode the week, on purpose: the ordering changes every year, and a folder called
`Lecture 3` has no way of telling you it has gone stale — which is exactly what happened
to the 2025 layout. The syllabus decides what belongs where, and it is generated and
checked. Track is the one thing the folders encode, because track does not change.

Each note ends with an `## Exam Questions` section covering its own material. Add
questions there rather than in a separate file, for the same reason: a question in its own
file drifts away from the material it tests.

Images live beside the notes that use them, in each folder's own `images/`.

## The app we build

[itu-tid/todo-26](https://github.com/itu-tid/todo-26), tagged once per lecture. Live-code
into it, tidy afterwards, then tag — so the commits inside a week are the lecture as it
happened and the tag is the version worth reading. Teams fork it in week 3, so it has to
be genuinely good through `week-02` by then.
