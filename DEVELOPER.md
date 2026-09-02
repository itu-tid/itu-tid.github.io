# Working on this repo

For whoever maintains the course. Students need none of it.

## The syllabus is built, and its source is not here

`syllabus.html` is generated. The markdown it comes from lives at `$TID_VAULT/2026-syllabus.md`, in the Obsidian vault, **not in this repository** — because it carries `%%staff asides%%` and `New:` / `Status:` rows that are notes between the people teaching the course. Keeping the source here and stripping it on the way out would have been theatre: the markdown is the original, the page only a copy of it.

```bash
export TID_VAULT="…/Megavault/teaching/technical interaction design/"
python3 build.py
```

That writes two pages from the one source:

| | |
|---|---|
| `./syllabus.html` | the students' page. Committed, and what GitHub Pages serves. |
| `$TID_VAULT/2026-syllabus-internal.html` | ours, with everything left in. Stays in the vault. |

Edit the markdown in the vault for content and `syllabus.template.html` for design. Never edit either generated page by hand — the next build overwrites it.

### Marking a passage as ours

Three mechanisms, all resolved by `staff_only()` in `build.py`:

- **`%%…%%`** — an inline aside, dropped from the student page. Use it for spans *inside* a paragraph or list item, not for whole paragraphs: an emptied paragraph still renders as an empty one.
- **`- **New:** …`** — a badge on the staff page, absent from the student one. What still has to be written for a given week.
- **`- **Status:** …`** — never rendered on either page. Planning state.

**In the notes, `%%…%%` does nothing.** That syntax is Obsidian's, and only `build.py` understands it — so a `%%TODO%%` left in a lecture note is invisible while you write it and then published to students verbatim, on GitHub and in the PDF chapter. Use an HTML comment instead:

```markdown
<!-- TODO: this example is still the Counter, not the to-do -->
```

Hidden in Obsidian, hidden on GitHub, hidden in the chapter. Better still, put the note in that week's plan in the vault, where you will actually see it when preparing.

### The pre-commit hook is what replaced the Action

There was a GitHub Action. It went when the source left the repo, because it cannot build from a file it cannot see. Its replacement is local:

```bash
git config core.hooksPath git-hooks   # once per clone
```

`git-hooks/pre-commit` rebuilds `syllabus.html` from the vault before **every** commit and stages it if it changed — so it catches a stale page even when you are committing something else entirely, which is the case you would otherwise miss. Without `TID_VAULT` set — a co-teacher's clone — it does nothing and lets the commit through, because there is nothing it could build.

That leaves exactly one gap: edit the syllabus in the vault and never commit anything, and the published page stays behind until your next commit. Run `python3 build.py` and commit if you want it out sooner.

## PDF chapters

One PDF per week, for linking from learnIT, built from the same notes the syllabus names:

```bash
python3 tools/build-pdfs.py        # every week
python3 tools/build-pdfs.py 1 2    # just these
```

Output goes to **`$TID_PDF_OUT`** — a clone of [itu-tid/lecture-notes-pdf](https://github.com/itu-tid/lecture-notes-pdf), published at <https://itu-tid.github.io/lecture-notes-pdf/> — and to `./pdf` if that is unset. **The chapters are never committed to this repository.** Each rebuild is about a megabyte of new binary per week, and fourteen of them every time a note changes would bury the history in a term.

`tools/publish-chapters.sh` pushes them, and it **rewrites that repository rather than appending to it**: every publish replaces its single commit and force-pushes, so the binaries never accumulate there either. Nothing in it deserves a history — the history lives here, with the source.

**The files are `Week-NN.pdf` and nothing else**, so that retitling a week does not break its URL. That matters more than it looks: learnIT links and student bookmarks would go, but so would the *latest version* link printed inside every earlier copy of that same chapter — in the one document whose job is to survive going stale. The titles therefore live in `chapters.json`, written beside the PDFs by `build-pdfs.py`; `publish-chapters.sh` inlines it into `index.html` rather than having the page fetch it, so the index still works opened straight off disk.

A week that leaves the syllabus has its chapter deleted on the next build, since the index lists what the manifest says and a stray file would otherwise linger.

iCloud was tried first and failed the only test that mattered: a shared-folder link shows non-Apple visitors a sign-in wall and no file listing at all. Asking a cohort to create an Apple ID to read the lecture notes was not a trade worth making.

The week → notes mapping is not written down anywhere in the tool: it is read out of the syllabus's `GH:` rows, so a note that moves between weeks moves its chapter with it. A link to a folder means every note inside it, in name order — that is how week 7 picks up the ten heuristic counterexamples.

### You do not have to remember to run it

`git-hooks/post-commit` does it for you: it looks at which notes the commit touched, works out which chapters use them, rebuilds only those, and publishes — all in the background.

Post-commit rather than pre-commit precisely *because* the PDFs are not in the repository — they do not have to exist before the commit is made, so the commit returns instantly and the chapters catch up a minute later. Progress goes to `$TMPDIR/tid-pdf-rebuild.log`.

**How it works, and why not LaTeX.** `tools/md-to-pdf.sh` runs pandoc to turn the notes into one HTML document, applies `tools/print.css`, and prints it with headless Chrome. The obvious route — pandoc straight to PDF — was tried first and lost: `pdflatex` dies on the box-drawing characters in the Vite project tree, `tectonic` survives those but drops the `→` in the VS Code menu paths, and both clip long code lines off the right margin. Chrome wraps code, renders every glyph, and lets the chapters use the same typefaces and palette as the published syllabus.

Each chapter carries the commit it was built from, the date, and a link to the version the site is serving now; each note inside it links to its own file on GitHub, so a student who finds a mistake can open an issue or a pull request. The notes are copied to a temp directory to have that link spliced in, which is why every original directory joins `--resource-path` — without it the images stop resolving. The splice looks for the first `# ` *outside a code fence*, because `Parse-Server-Deployment-Guide.md` and `React-Starter-Kit.md` are full of shell comments that look exactly like headings.

### Known gaps

**Chapters only rebuild on Mircea's machine, and fail silently everywhere else.** `git-hooks/post-commit` exits immediately without `TID_VAULT`, and `tools/build-pdfs.py` needs it too, because the week → notes mapping is read out of the syllabus in the vault. So a note edited and pushed by anyone else leaves the published PDF quietly disagreeing with the markdown, with nothing to say so. **This matters from week 3 (10 Sep)**, the first lecture Konstantina teaches while Mircea is away.

The fix is small and follows a pattern already here: have `build.py` write a `chapters.json` *into this repo* carrying week → title → note paths, staged by the pre-commit hook exactly as `syllabus.html` already is. A GitHub Action can then rebuild on any push with no access to the vault — install pandoc and Chrome, read the manifest, force-push to the chapters repo with a deploy key. Keep the local hook as well: it is faster and it updates Mircea's own copy of the PDFs, which an Action cannot.

**A mermaid diagram prints as its own source.** `Authorization-and-ACL-in-Parse.md` has a ```mermaid block, and this pipeline has no mermaid: pandoc passes it through and Chrome prints it as a code listing, so week 5's chapter shows students `erDiagram / _User ||--o{ TodoItem : owns`. It is the only mermaid in the repo. Either convert it to an ASCII diagram like the others, or render mermaid at build time.

**No page numbers.** Chrome's headless PDF exposes no way to add them without also stamping a `file://` URL in the footer.

**The Google Fonts import** means the first build on a cold cache is slower.

## What else lives in the vault

The split is by kind, not by course: this repo holds material other people write into and that gets built; the vault holds the thinking. Nothing syncs between them, because the two sets do not overlap — `build.py` is the only bridge, and it only ever writes outward.

    2026-syllabus.md              the source above
    2026-syllabus-internal.html   the staff page it generates
    2026-planning.md              what is undecided, and why
    2026-redesign-handoff.md      the brief the 2026 redesign started from
    2026-lecture-1-opening.md     delivery notes for the first lecture
    2026-lecture-14-closing.md    and for the last one
    2026-MUST-DO.md               dated, with consequences -- read it before each week
    2026-inbox.md · 2026-backlog.md
    2026-repo-history-before-purge.bundle

That last one is a full clone of this repository as it stood before staff notes, student names and an external censor's email address were stripped out of its history. `git clone` it if you ever need to see how the syllabus evolved.

## Notes

Two folders by track — `Lectures/Technical/` and `Lectures/Interaction-Design/` — and inside the technical one, five by subject: React, Structure, Backend, Routing, Tooling. Neither filenames nor folders encode the week, on purpose: the ordering changes every year, and a folder called `Lecture 3` has no way of telling you it has gone stale — which is exactly what happened to the 2025 layout. The syllabus decides what belongs where, and it is generated and checked. Track and subject are what the folders encode, because neither changes: routing will still be routing next year.

Each note ends with an `## Exam Questions` section covering its own material. Add questions there rather than in a separate file, for the same reason: a question in its own file drifts away from the material it tests.

Images live in one `images/` per track, not one per subject folder — splitting forty files five ways buys nothing.

## The app we build

[itu-tid/todo-26](https://github.com/itu-tid/todo-26), tagged once per lecture. Live-code into it, tidy afterwards, then tag — so the commits inside a week are the lecture as it happened and the tag is the version worth reading. Teams do not start from it — they build their own repo from empty in week 6, against the ER diagram their user study produced. This one is for reading: the canonical version of everything the lectures do, to compare against.
