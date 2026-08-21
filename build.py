#!/usr/bin/env python3
"""Build syllabus.html from syllabus.md.

syllabus.md is the single source of truth. This script reads it, and fills
syllabus.template.html (the design shell — all the CSS lives there) with the
markdown's content. Edit the markdown for content, the template for design;
never edit syllabus.html by hand.

    python3 build.py

Markdown links to notes in this repo are written repo-relative, so they work
on GitHub and in a local editor; they are rewritten to absolute GitHub URLs in
the HTML, which is served from GitHub Pages where relative paths would 404.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "syllabus.md"
TEMPLATE = ROOT / "syllabus.template.html"
OUT = ROOT / "syllabus.html"

REPO = "https://github.com/itu-tid/itu-tid.github.io"
BADGES = {"GH": "gh", "learnIT": "lit", "New": "new"}

# Which colour track a week's row gets, keyed by teacher. Filled from the
# "Teaching team" list in the markdown; a teacher not listed there (a guest)
# falls back to the lecture's eyebrow — "React II" → react, "Design II" → design.
TRACKS: dict[str, str] = {}


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
    doc["lede"] = lead[1:]
    doc["glance"] = [re.match(r"-\s+\*\*(.+?)\*\*\s+—\s+(.*)", ln.strip()).groups()
                     for ln in over.get("At a glance", []) if ln.strip().startswith("- ")]
    doc["legend"] = [re.match(r"-\s+`(\w+)`\s+(.*)", ln.strip()).groups()
                     for ln in over.get("Teaching team", []) if ln.strip().startswith("- ")]
    for key, label in doc["legend"]:
        name = re.sub(r"\*\*|\s+—.*", "", label).strip()
        if key != "away":
            TRACKS[name] = key

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

def track_of(who, eyebrow):
    for name, key in TRACKS.items():
        if who.startswith(name):
            return key
    if "Design" in eyebrow:
        return "design"
    return "react" if "React" in eyebrow else "you"


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


def week_row(heading, body, last):
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

    # title and eyebrow sit on consecutive lines; the description follows
    text = [ln.strip() for ln in body
            if ln.strip() and not ln.strip().startswith("- ")]
    if len(text) < 3:
        sys.exit(f'build.py: week "{heading}" needs a title, an eyebrow and a description')
    title, eyebrow, desc = text[0].strip("* "), text[1].strip("* "), " ".join(text[2:])
    f = dict(fields(body))

    mile, _, sub = f.get("Milestone", "").partition(" — ")
    checkin = (f'\n            <span class="checkin">◆ {inline(f["Check-in"])}</span>'
               if "Check-in" in f else "")
    cls = f'row t-{track_of(who, eyebrow)}' + (" away" if away else "") + (" last" if last else "")

    return f"""    <div class="{cls}">
      <div class="when"><div class="wk">{esc(wk)}</div><div class="date">{esc(date)}</div><div class="node"></div></div>
      <div class="card">
        <div class="lec">
          <div class="lec-top"><span class="who {track_of(who, eyebrow)}">{inline(who)}</span><span class="lec-eyebrow">{inline(eyebrow)}</span>{f'<span class="away-tag">{inline(away)}</span>' if away else ''}</div>
          <div class="ttl">{inline(title)}</div>
          <div class="desc">{inline(desc)}</div>
        </div>
        <div class="lanes">
          <div class="lane exercise">
            <div class="lane-h"><span class="mk"></span>Exercise</div>
            <div class="split"><span class="h solo">1h solo</span>{inline(f.get('Solo', ''))}</div>
            <div class="split"><span class="h grp">1h project</span>{inline(f.get('Project', ''))}</div>
          </div>
          <div class="lane project">
            <div class="lane-h"><span class="mk"></span>Project milestone</div>
            <div class="mile">{inline(mile)}<span class="sub">{inline(sub.strip('*'))}</span></div>{checkin}
          </div>
        </div>
        {resources(fields(body))}
      </div>
    </div>"""


def render(doc):
    ind = "      "
    weeks = doc["weeks"]
    rows = [week_row(h, b, last=(i == len(weeks) - 1)) for i, (h, b) in enumerate(weeks)]

    slots = {
        "KICKER": inline(doc["kicker"]),
        "H1": esc(doc["h1"]),
        "LEDE": "\n    ".join(f'<p class="lede">{inline(p)}</p>' for p in doc["lede"]),
        "GLANCE": "\n".join(
            f'{ind}<div class="stat"><div class="n">{inline(n)}</div>'
            f'<div class="l">{inline(l)}</div></div>' for n, l in doc["glance"]),
        "LEGEND": "\n".join(
            f'{ind}<span><i class="{"away" if k == "away" else f"dot {k}"}">'
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


if __name__ == "__main__":
    document = parse(SRC.read_text(encoding="utf-8"))
    OUT.write_text(render(document), encoding="utf-8")
    print(f"{OUT.name}: {len(document['weeks'])} week rows, "
          f"{len(document['notes'])} notes, {len(document['spine'])} checkpoints")
