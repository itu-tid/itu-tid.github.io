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
