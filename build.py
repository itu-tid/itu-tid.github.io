#!/usr/bin/env python3
"""Build the syllabus pages from the markdown source in the Obsidian vault.

The source is `$TID_VAULT/2026-syllabus.md`, and it lives outside this repo on
purpose: it carries the `%%staff asides%%` and the `New:` / `Status:` rows,
which are notes between the people teaching the course. Stripping those out of
the generated page while leaving them in a committed source file would have
been theatre — the markdown is the original, the HTML only a copy.

So, from the one source:

    ./syllabus.html                          the students' page. Generated,
                                             committed, and what GitHub Pages
                                             serves.
    $TID_VAULT/2026-syllabus-internal.html   ours, everything left in. Written
                                             into the vault, never in here.

Edit the markdown in the vault for content, syllabus.template.html (the design
shell — all the CSS lives there) for design; never edit either generated page
by hand. See staff_only() for how a passage is marked as one or the other.

    export TID_VAULT="…/Megavault/teaching/technical interaction design/"
    python3 build.py

Markdown links to notes in this repo are written repo-relative, so they work
on GitHub and in a local editor; they are rewritten to absolute GitHub URLs in
the HTML, which is served from GitHub Pages where relative paths would 404.
"""

import html
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "syllabus.template.html"
OUT = ROOT / "syllabus.html"   # the students' page, the one we publish

VAULT = os.environ.get("TID_VAULT")
if not VAULT:
    sys.exit("build.py: set TID_VAULT to the course folder in the Obsidian vault — "
             "the syllabus source lives there, not in this repo")
SRC = Path(VAULT) / "2026-syllabus.md"
OUT_INTERNAL = Path(VAULT) / "2026-syllabus-internal.html"

# Fields that exist for whoever is running the course, not for whoever is
# taking it: `Status` is never rendered at all, `New` is a badge on the staff
# page and has no business on the student one.
STAFF_FIELDS = ("New", "Status")

REPO = "https://github.com/itu-tid/itu-tid.github.io"
BADGES = {"GH": "gh", "learnIT": "lit", "New": "new"}
# Tech-TopUps pre-readings, dripped week by week. Not lecture source material,
# so they get their own row under the resource strip rather than a source pill.
NOTES = ("Prereq", "Revisit", "Optional")

# name → colour key, filled from the "Teaching team" list in the markdown
PEOPLE: dict[str, str] = {}
PERSON_KEYS = ("you", "react")


# ---------------------------------------------------------------- inline text

def esc(text):
    return html.escape(text, quote=False)


def emphasis(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)


def link(label, url):
    if url.startswith("http"):
        kind = "lit" if "learnit.itu.dk" in url else "gh"
    else:  # repo-relative → absolute, so the page works off GitHub Pages
        kind = "gh"
        part = "blob" if url.endswith(".md") else "tree"
        url = f"{REPO}/{part}/main/{url}"
    return (f'<a class="rl {kind}" href="{url}" target="_blank" rel="noopener">'
            f"{emphasis(esc(label))}</a>")


def inline(text, badges=False):
    """Markdown inline → HTML. With badges=True, `GH`/`learnIT`/`New` code
    spans become source pills instead of <code>."""
    out = []
    for part in re.split(r"(`[^`]+`)", text):
        if part.startswith("`") and part.endswith("`") and len(part) > 2:
            body = part[1:-1]
            if badges and body in BADGES:
                out.append(f'<span class="src {BADGES[body]}">{esc(body)}</span>')
            else:
                out.append(f"<code>{esc(body)}</code>")
            continue
        pos = 0
        for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", part):
            out.append(emphasis(esc(part[pos:m.start()])))
            out.append(link(m.group(1), m.group(2)))
            pos = m.end()
        out.append(emphasis(esc(part[pos:])))
    return "".join(out)


# ------------------------------------------------------------------- markdown

def sections(lines, level):
    """Split lines into (heading, body-lines) at the given heading level."""
    mark = "#" * level + " "
    found, head, body = [], None, []
    for line in lines:
        if line.startswith(mark):
            if head is not None:
                found.append((head, body))
            head, body = line[len(mark):].strip(), []
        elif head is not None:
            body.append(line)
    if head is not None:
        found.append((head, body))
    return found


def paragraphs(lines):
    out, buf = [], []
    for line in lines:
        if line.strip():
            buf.append(line.strip())
        elif buf:
            out.append(" ".join(buf))
            buf = []
    if buf:
        out.append(" ".join(buf))
    return out


def blocks(lines):
    """Overview prose → a sequence of ("p", text) and ("ul", [items])."""
    out, para, items = [], [], []
    def flush_para():
        if para:
            out.append(("p", " ".join(para)))
            para.clear()
    def flush_list():
        if items:
            out.append(("ul", list(items)))
            items.clear()
    for line in lines:
        text = line.strip()
        if text.startswith("- "):
            flush_para()
            items.append(text[2:].strip())
        elif text:
            flush_list()
            para.append(text)
        else:
            flush_para()
    flush_para()
    flush_list()
    return out


def fields(lines):
    """`- **Key:** value` bullets → list of (key, value), order preserved."""
    return [(m.group(1), m.group(2).strip())
            for m in (re.match(r"-\s+\*\*(.+?):\*\*\s*(.*)", ln.strip()) for ln in lines)
            if m]


def parse(text):
    top = dict(sections(text.split("\n"), 2))
    missing = {"Overview", "Weeks", "How the pieces fit"} - set(top)
    if missing:
        sys.exit(f"build.py: syllabus.md is missing section(s): {', '.join(sorted(missing))}")
    doc = {"h1": text.split("\n", 1)[0].lstrip("# ").split(" — ")[0].strip(), "top": top}

    over = dict(sections(top["Overview"], 3))
    lead = paragraphs(sections(top["Overview"], 3)[0][1] if False else
                      top["Overview"][:index_of_heading(top["Overview"])])
    doc["kicker"] = lead[0].strip("*")
    doc["lede"] = blocks(top["Overview"][:index_of_heading(top["Overview"])])[1:]
    doc["glance"] = [re.match(r"-\s+\*\*(.+?)\*\*\s+—\s+(.*)", ln.strip()).groups()
                     for ln in over.get("At a glance", []) if ln.strip().startswith("- ")]
    doc["legend"] = [re.match(r"-\s+`(\w+)`\s+(.*)", ln.strip()).groups()
                     for ln in over.get("Teaching team", []) if ln.strip().startswith("- ")]
    for key, label in doc["legend"]:
        if key in PERSON_KEYS:
            PEOPLE[re.sub(r"\*\*|\s+—.*", "", label).strip()] = key

    spine_key = next(k for k in top if k.startswith("Deliverables"))
    doc["spine_h"] = spine_key
    doc["spine"] = [re.match(r"-\s+\*\*(.+?)\s+—\s+(.+?)\*\*\s+—\s+(.*)", ln.strip()).groups()
                    for ln in top[spine_key] if ln.strip().startswith("- ")]
    doc["spine_foot"] = paragraphs([ln for ln in top[spine_key]
                                    if not ln.strip().startswith("- ")])[0]

    doc["weeks"] = sections(top["Weeks"], 3)
    doc["notes"] = [(h, paragraphs(b)[0]) for h, b in sections(top["How the pieces fit"], 3)]
    tail = paragraphs([ln for ln in top["How the pieces fit"] if not ln.startswith("### ")])
    doc["foot"] = tail[-1].strip("*") if tail else ""
    return doc


def index_of_heading(lines):
    for i, ln in enumerate(lines):
        if ln.startswith("### "):
            return i
    return len(lines)


# --------------------------------------------------------------------- render

MONTHS = {m: i for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}


def parse_date(text, year):
    """"Oct 8" → a date."""
    m = re.match(r"([A-Z][a-z]{2})\s+(\d{1,2})", text.strip())
    return date(year, MONTHS[m.group(1)], int(m.group(2))) if m else None


def next_tuesday(after, skip_week_of=None):
    """The next Tuesday strictly after a Thursday lecture — skipping the one
    that falls inside the autumn break, which is why week 7 gets two weeks."""
    day = after + timedelta(days=(1 - after.weekday()) % 7 or 7)
    if skip_week_of and day.isocalendar()[:2] == skip_week_of.isocalendar()[:2]:
        day += timedelta(days=7)
    return day


# Two independent axes. The track says what kind of week it is; the person says
# who is standing at the front. They do not line up — Konstantina teaches both
# design and technical weeks — so they get separate colours: the card's left
# border carries the track, the timeline node and the name badge carry the person.
def track_of(eyebrow):
    return "design" if "Design" in eyebrow else "tech"


def person_of(who, eyebrow):
    for name, key in PEOPLE.items():
        if who.startswith(name):
            return key
    # a guest we do not know: fall back to the kind of lecture it is
    return "react" if ("React" in eyebrow or "Design" in eyebrow) else "you"


def resources(items):
    groups = []
    for label, value in items:
        if label not in BADGES:
            continue
        lead = ""
        m = re.match(r"^([^\[`*]*?:)\s*", value)
        if m:
            lead = f'<div class="ri-lead">{inline(m.group(1))}</div>'
            value = value[m.end():]
        lis = "".join(f"<li>{inline(i.strip())}</li>" for i in value.split(" · ") if i.strip())
        groups.append(f'<div class="res-grp"><span class="src {BADGES[label]}">{label}</span>'
                      f'<div class="ri-body">{lead}<ul class="ri">{lis}</ul></div></div>')
    return f'<div class="res">{"".join(groups)}</div>' if groups else ""


def prereads(items):
    rows = "".join(
        f'<div class="prereq"><span class="pq">{label}</span>'
        f'<span>{inline(value)}</span></div>'
        for label, value in items if label in NOTES)
    return f"\n        {rows}" if rows else ""


def week_row(heading, body, last, boundary=None):
    if heading.startswith("Break"):
        date = heading.split("·")[1].strip()
        note = paragraphs(body)[0]
        return ('    <div class="brk">\n'
                f'      <div class="when"><div class="wk">&nbsp;</div><div class="date">{esc(date)}</div><div class="node"></div></div>\n'
                f'      <div class="brk-card">◆ {inline(note)}</div>\n'
                "    </div>")

    head = re.match(r"(Week \d+)\s+·\s+([^·]+?)\s+·\s+(.+)", heading)
    if not head:
        sys.exit(f'build.py: cannot parse week heading: "{heading}"')
    wk, date, who = (g.strip() for g in head.groups())
    away = ""
    if who.endswith("*"):
        who, away = re.match(r"(.+?)\s+\*\((.+?)\)\*$", who).groups()

    # title and eyebrow sit on consecutive lines; the description follows and may
    # run to several paragraphs, which are kept apart rather than run together
    prose = [ln for ln in body if not ln.strip().startswith("- ")]
    text = [ln.strip() for ln in prose if ln.strip()]
    if len(text) < 3:
        sys.exit(f'build.py: week "{heading}" needs a title, an eyebrow and a description')
    title, eyebrow = text[0].strip("* "), text[1].strip("* ")
    seen, rest = 0, []
    for ln in prose:
        if seen >= 2:
            rest.append(ln)
        elif ln.strip():
            seen += 1
    paras = paragraphs(rest)
    desc = ("".join(f"<p>{inline(x)}</p>" for x in paras)
            if len(paras) > 1 else inline(paras[0]))
    f = dict(fields(body))

    # weeks with no team yet run two hours of solo work instead of 1h + 1h
    if "Studio" in f:
        # a check-in week: the whole slot is one room, teams called one at a time
        lane_head = "Exercise · 2h studio"
        lines = [("grp", "2h studio", f["Studio"])]
        if "Solo" in f:
            lines.insert(0, ("solo", "at home", f["Solo"]))
        lines = tuple(lines)
    elif "Second hour" in f:
        lane_head, lines = "Exercise · 2h solo", (
            ("solo", "first hour", f.get("Solo", "")),
            ("solo", "second hour", f["Second hour"]))
    elif "Project" in f:
        lane_head, lines = "Exercise", (
            ("solo", "1h solo", f["Solo"]),
            ("grp", "1h project", f["Project"]))
    else:
        sys.exit(f'build.py: week "{heading}" needs a Project or a Second hour field')
    exercise = "\n            ".join(
        f'<div class="split"><span class="h {cls}">{label}</span>{inline(body)}</div>'
        for cls, label, body in lines)

    # two horizons, kept apart. Both are work handed out today; they differ in
    # how far away they land — next Tuesday, or somewhere further out.
    rows = []
    if "Done by" in f:
        label = f"todo by {boundary}" if boundary else "todo"
        rows.append(f'<div class="split"><span class="h grp">{label}</span>'
                    f'<span class="key">{inline(f["Done by"])}</span></div>')
    if "Starting" in f:
        rows.append('<div class="split"><span class="h solo">starting</span>'
                    f'{inline(f["Starting"])}</div>')
    project = "\n            ".join(rows)
    # a learnIT assignment is a hand-in, so it belongs beside the milestone
    # rather than in the reading list
    extra = ""
    # a deliverable appears twice: outlined on the week it is set, filled on the
    # lecture you turn up to having handed it in. Both always name the date.
    if "Due" in f:
        extra = f'\n            <span class="due">Due {inline(f["Due"])}</span>' + extra
    if "Set" in f:
        extra = f'\n            <span class="set">Set · {inline(f["Set"])}</span>' + extra
    if "Check-in" in f:
        extra += f'\n            <span class="checkin">◆ {inline(f["Check-in"])}</span>'
    track, person = track_of(eyebrow), person_of(who, eyebrow)
    # weeks before the teams exist have no project lane at all
    has_project = bool(rows or extra)
    project_lane = ("" if not has_project else
                    '\n          <div class="lane project">\n'
                    '            <div class="lane-h"><span class="mk"></span>Project</div>\n'
                    f'            {project}{extra}\n'
                    '          </div>')

    cls = f"row t-{track} p-{person}" + (" away" if away else "") + (" last" if last else "")

    return f"""    <div class="{cls}">
      <div class="when"><div class="wk">{esc(wk)}</div><div class="date">{esc(date)}</div><div class="node"></div></div>
      <div class="card">
        <div class="lec">
          <div class="lec-top"><span class="who {person}">{inline(who)}</span><span class="lec-eyebrow">{inline(eyebrow)}</span>{f'<span class="away-tag">{inline(away)}</span>' if away else ''}</div>
          <div class="ttl">{inline(title)}</div>
          <div class="desc">{desc}</div>
        </div>
        <div class="lanes{"" if has_project else " alone"}">
          <div class="lane exercise">
            <div class="lane-h"><span class="mk"></span>{lane_head}</div>
            {exercise}
          </div>{project_lane}
        </div>
        {resources(fields(body))}{prereads(fields(body))}
      </div>
    </div>"""


def legend_mark(key):
    if key == "away":
        return "away"
    return f"dot {key}" if key in PERSON_KEYS else f"bar {key}"


def render(doc):
    ind = "      "
    weeks = doc["weeks"]
    year = int(re.search(r"(20\d\d)", doc["kicker"]).group(1))
    brk = next((parse_date(h.split("·")[1], year)
                for h, _ in weeks if h.startswith("Break")), None)

    def boundary_for(heading):
        parts = heading.split("·")
        lecture = parse_date(parts[1], year) if len(parts) > 1 else None
        if not lecture or heading.startswith("Break"):
            return None
        tue = next_tuesday(lecture, brk)
        return f"Tue {tue.day} {tue:%b}"

    rows = [week_row(h, b, last=(i == len(weeks) - 1), boundary=boundary_for(h))
            for i, (h, b) in enumerate(weeks)]

    slots = {
        "KICKER": inline(doc["kicker"]),
        "H1": esc(doc["h1"]),
        "LEDE": "\n    ".join(
            f'<p class="lede">{inline(body)}</p>' if kind == "p" else
            '<ul class="lede">' + "".join(f"<li>{inline(i)}</li>" for i in body) + "</ul>"
            for kind, body in doc["lede"]),
        "GLANCE": "\n".join(
            f'{ind}<div class="stat"><div class="n">{inline(n)}</div>'
            f'<div class="l">{inline(l)}</div></div>' for n, l in doc["glance"]),
        "LEGEND": "\n".join(
            f"{ind}<span><i class=\"{legend_mark(k)}\">"
            f'{"away" if k == "away" else ""}</i> {inline(t)}</span>'
            for k, t in doc["legend"]),
        "SPINE_H": inline(doc["spine_h"]),
        "SPINE": "\n".join(
            f'{ind}<div class="milestone">\n{ind}  <div class="m-wk">{inline(w)}</div>\n'
            f'{ind}  <div class="m-name">{inline(n)}</div>\n'
            f'{ind}  <div class="m-sub">{inline(s)}</div>\n{ind}</div>'
            for w, n, s in doc["spine"]),
        "SPINE_FOOT": inline(doc["spine_foot"]),
        "TIMELINE": "\n\n".join(rows),
        "NOTES_H": inline("How the pieces fit"),
        "NOTES": "\n".join(
            f'{ind}<div class="note">\n{ind}  <div class="nt">{inline(t)}</div>\n'
            f'{ind}  <p>{inline(p, badges=True)}</p>\n{ind}</div>'
            for t, p in doc["notes"]),
        "FOOT": inline(doc["foot"]),
    }

    out = TEMPLATE.read_text(encoding="utf-8")
    for key, value in slots.items():
        out = out.replace("{{" + key + "}}", value)
    left = re.findall(r"\{\{[A-Z_]+\}\}", out)
    if left:
        sys.exit(f"build.py: template slot(s) never filled: {', '.join(left)}")
    return out


# --------------------------------------------------------------- placeholders

def numbers(seq):
    """[3, 7, 9] → "3, 7 and 9"."""
    n = [str(x) for x in seq]
    if not n:
        return "none"
    return n[0] if len(n) == 1 else ", ".join(n[:-1]) + " and " + n[-1]


def week_facts(text):
    """Facts the prose keeps getting wrong, computed from the week cards.

    Hand-written notes drift every time the term is restructured — the design
    weeks move, a check-in appears, a lecture changes hands. Anything here can
    be written as {{name}} in the markdown and will always be right.
    """
    doc = parse(text)
    weeks, design, checkin, feedback, people = [], [], [], [], {}
    for head, body in doc["weeks"]:
        m = re.match(r"Week 0*(\d+) · [^·]+· (.+)", head)
        if not m:
            continue
        num, who = int(m.group(1)), re.sub(r"\s*\*\(.*?\)\*", "", m.group(2)).strip()
        f = dict(fields(body))
        prose = [ln.strip() for ln in body if ln.strip() and not ln.strip().startswith("- ")]
        weeks.append(num)
        if len(prose) > 1 and "Design" in prose[1]:
            design.append(num)
        if "Check-in" in f:
            checkin.append(num)
        if "Feedback" in f:
            feedback.append(num)
        people.setdefault(who, []).append(num)

    facts = {
        "design-weeks": numbers(design),
        "checkin-weeks": numbers(checkin),
        "feedback-weeks": numbers(feedback),
        "week-count": str(len(weeks)),
    }
    for who, ws in people.items():
        facts[f"weeks:{who}"] = numbers(ws)
        facts[f"count:{who}"] = str(len(ws))
    return facts


def expand(text):
    for key, value in week_facts(text).items():
        text = text.replace("{{" + key + "}}", value)
    left = set(re.findall(r"\{\{([a-z][a-z:\- ]*)\}\}", text))
    if left:
        sys.exit(f"build.py: unknown placeholder(s): {', '.join(sorted(left))}")
    return text


def staff_only(text, keep):
    """Resolve the `%%...%%` staff-aside markers.

    One markdown source, two audiences. Anything wrapped in `%%` is written for
    the teaching team — delivery notes, the reasoning behind a sequencing
    choice, who is covering what — and is dropped from the student build. Use
    it for spans *inside* a paragraph or list item, not for whole paragraphs:
    an emptied paragraph would still render as one.

    `- **New:**` and `- **Status:**` rows go the same way, by field name.
    """
    if keep:
        return re.sub(r"%%(.*?)%%", r"\1", text, flags=re.S)
    text = re.sub(r"[ \t]*%%.*?%%", "", text, flags=re.S)
    text = "\n".join(ln for ln in text.split("\n")
                     if not re.match(rf"\s*- \*\*({'|'.join(STAFF_FIELDS)}):\*\*", ln))
    return re.sub(r"\n{3,}", "\n\n", text)


def check_new_list(text, doc):
    """The provenance note lists the to-write items by week. It cannot be
    generated — the labels are editorial — but it can be stopped from drifting."""
    note = re.search(r"`New` the short list left to write:(.*)", text)
    if not note:
        return
    claimed = sorted({int(x) for x in re.findall(r"wk (\d+)", note.group(1))})
    actual = sorted(int(re.match(r"Week 0*(\d+)", h).group(1))
                    for h, b in doc["weeks"]
                    if re.match(r"Week", h) and "New" in dict(fields(b)))
    if claimed != actual:
        sys.exit("build.py: the 'short list left to write' names weeks "
                 f"{claimed} but weeks {actual} have a New: item")


if __name__ == "__main__":
    raw = expand(SRC.read_text(encoding="utf-8"))
    for out, keep in ((OUT_INTERNAL, True), (OUT, False)):
        source = staff_only(raw, keep=keep)
        document = parse(source)
        if keep:
            check_new_list(source, document)
        out.write_text(render(document), encoding="utf-8")
        print(f"{out}: {len(document['weeks'])} week rows, "
              f"{len(document['notes'])} notes, {len(document['spine'])} checkpoints")
