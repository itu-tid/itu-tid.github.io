# Technical Interaction Design — Autumn 2026

**ITU Copenhagen · 7.5 ECTS · Thursdays · 14 weeks · Aug 27 – Dec 3** (autumn break Oct 15, no lecture)
**Lead:** Mircea Lungu · **React lectures:** Konstantina · **Interaction design:** a designer (TBC) · **Week 3:** Bjørn / a TA (TBC)

> This is the front-page map of the course: what each week is, who teaches it, what material backs it, and what is still to write. The fuller week-by-week detail — exercise slots and project milestones per week — lives in [`syllabus.html`](syllabus.html); `README.md` still describes the repo itself.

---

## The thesis

In the AI era the scarce skill is **code comprehension**, not code production — owning and being able to explain code you may not have typed. So the deal with students is simple: **use AI all you want; own every line at the exam.** The course builds toward that: a fast technical track stands up a working, shared, deployed app in the first six weeks while a quieter design track runs alongside; the two meet at week 6 on a live, researched app; everything after is depth, each advanced topic motivated by an app the students already care about.

Every team builds **one group to-do app** — the same lean core (`owner → lists → items`, sharing at the list level), plus a population-driven twist of their own. Teams **dogfood the core** all term but **design the twist for an outside population they go and study**. Accessibility is the through-line.

---

## Deliverables spine — five checkpoints, Friday cadence

| # | When | Checkpoint | What it means |
|---|------|-----------|---------------|
| 1 | **Week 2 · Fri** | Population chosen | Who you'll build for and how you'll reach them. Assignment 1 begins. |
| 2 | **Week 6 · Fri** | App live & user study in | A deployed, shareable app — plus interviews → themes → personas. The tracks meet. Assignment 1 due. |
| 3 | **Week 7 · Fri** | Wireframes, tested | Special screens wireframed and put through a light usability pass — before you build. |
| 4 | **Week 10 · Fri** | Chosen features working | Feature-menu picks (real-time sync, time-tracking) live in the app. |
| 5 | **Week 14** | Final app + thin report | Deployed, dogfooded, defensible. Ready for the individual exam. |

These are checkpoints students **hit and dogfood against** — not weekly submissions marked line-by-line.

---

## Week by week

Status: **written** = note exists in this repo · **adapt** = exists but needs rework for 2026 · **NEW** = to write (see the TODO below).
⚠ learnIT links are **2025 course URLs** — they work as prep references now but must be repointed when the 2026 shell is created.

| # | Date | Who | Title | Topic in one line | Material | Status |
|---|------|-----|-------|-------------------|----------|--------|
| 1 | Aug 27 | Mircea | First React app: components, props & state | Zeeguu opener, then components, JSX, props, state, lists with keys | <ul><li>[T0-React-Starter-Kit](Lectures/Technical%20ID/Lecture%201/T0-React-Starter-Kit.md)</li><li>[T1-Intro-to-React](Lectures/Technical%20ID/Lecture%201/T1-Intro-to-React.md) (front half)</li><li>[T2-Hooks](Lectures/Technical%20ID/Lecture%201/T2-Hooks.md)</li></ul> | written |
| 2 | Sep 3 | **Designer** | Understanding user needs | Interviews, thematic analysis, personas, user stories, the onion constraint | learnIT ⚠ <ul><li>[slides](https://learnit.itu.dk/mod/resource/view.php?id=228493)</li><li>[notes](https://learnit.itu.dk/mod/resource/view.php?id=230914)</li><li>[User Interviews & Thematic Analysis](https://learnit.itu.dk/mod/assign/view.php?id=228499)</li><li>[Braun & Clarke 2019](https://learnit.itu.dk/mod/resource/view.php?id=230965)</li><li>[personas / user stories](https://learnit.itu.dk/mod/resource/view.php?id=231338)</li><li>[Tricia Wang talk](https://learnit.itu.dk/mod/kalvidres/view.php?id=230963)</li></ul> | adapt — needs the **one-page wrapper** |
| 3 | Sep 10 | **Bjørn / TA — TBC** *(Mircea away)* | Controlled components, forms & useEffect | Events, controlled inputs, conditional rendering — then useEffect against a *public* API (JSONPlaceholder `/todos`) | <ul><li>[T1-Intro-to-React](Lectures/Technical%20ID/Lecture%201/T1-Intro-to-React.md) (back half)</li><li>[T3-the-useEffect-Hook](Lectures/Technical%20ID/Lecture%201/T3-the-useEffect-Hook.md)</li></ul> | written — **useEffect pulled forward from wk4** |
| 4 | Sep 17 | Mircea | Database & login, together | Parse + auth in one move; core model `owner → lists → items`; useEffect now against *your own* backend | <ul><li>[L4 Backends & the Parse Platform](Lectures/Technical%20ID/Lecture%204/1.%20Backends-and-the-Parse-Platform.md) (login included)</li><li>[Parse-Configuration-for-Vite](Lectures/Technical%20ID/Lecture%204/Parse-Configuration-for-Vite.md)</li></ul> | written — reframed, lightened by wk3 |
| 5 | Sep 24 | Mircea | Sharing: ACLs, roles, private vs shared | Authorization in Parse; the collection layer — items point to a List, sharing lives at list level | <ul><li>[L5 Authorization-and-ACL in Parse](Lectures/Technical%20ID/Lecture%205/Authorization-and-ACL%20in%20Parse.md)</li></ul> | written + **NEW: List collection layer** |
| 6 | Oct 1 | Mircea | Routing, git-flow, and going live | Three generations of web apps → SPA → routing; git-flow; **deploy to GitHub Pages**; **code-review intro** on the live app | <ul><li>[L3 Web-App-Architectures](Lectures/Technical%20ID/Lecture%203/1.%20Web-App-Architectures.md)</li><li>[Routing in React](Lectures/Technical%20ID/Lecture%203/2.%20Routing%20in%20React.md)</li><li>[Collaboration-with-Git-Flow](Lectures/Technical%20ID/Lecture%203/3.%20Collaboration-with-Git-Flow.md)</li><li>[Code Organization](Lectures/Technical%20ID/General/Code%20Organization.md)</li><li>[L7 cheatsheet](Lectures/Technical%20ID/Lecture%207/COMPONENT_EXTRACTION_CHEATSHEET.md)</li></ul> | **NEW: frontend deploy** + **NEW: review checklist** |
| — | *Oct 15* | — | *Autumn break — no lecture* | | | |
| 7 | Oct 8 | **Designer** *(Mircea away)* | Screen design & usability for your population | Own extension, own ER diagram, **wireframes + usability pass**, a11y. **First check-in.** | learnIT ⚠ <ul><li>[Requirements, User Flows & Wireframing](https://learnit.itu.dk/mod/assign/view.php?id=228506)</li><li>[Prototyping slides](https://learnit.itu.dk/mod/resource/view.php?id=231641)</li><li>[Lauesen ch.13](https://learnit.itu.dk/mod/resource/view.php?id=228522)</li><li>[NN/g Heuristic Evaluation Workbook](https://learnit.itu.dk/mod/url/view.php?id=234019)</li><li>[Usability Report template](https://learnit.itu.dk/mod/url/view.php?id=228523)</li><li>repo: [usability examples](Lectures/usability_examples)</li></ul> | adapt — needs the **one-page wrapper** |
| 8 | Oct 22 | **Konstantina** *(Mircea away)* | Intermediate React patterns | Extracting components, updater functions, objects & lists in state, useRef, component communication — and what *good React* looks like | <ul><li>[T4-Refactoring by Extracting Components](Lectures/Technical%20ID/Lecture%202/T4-Refactoring%20by%20Extracting%20Components.md)</li><li>[T5-Updater-Functions](Lectures/Technical%20ID/Lecture%202/T5-Updater-Functions-for-State.md)</li><li>[T6-Updating Objects and Lists](Lectures/Technical%20ID/Lecture%202/T6-Updating%20Objects%20and%20Lists%20in%20State.md)</li><li>[T7-useRef](Lectures/Technical%20ID/Lecture%202/T7-React-the-useRef-Hook.md)</li><li>[T8-Component Communication](Lectures/Technical%20ID/Lecture%202/T8-Patterns%20of%20Component%20Communication.md)</li></ul> | written |
| 9 | Oct 29 | Mircea | Time-tracking, and the idea of context | One timer stops another → the app must know what's *active*; a context spanning all lists; private timing splits into its own table | <ul><li>[L5 Authorization-and-ACL in Parse](Lectures/Technical%20ID/Lecture%205/Authorization-and-ACL%20in%20Parse.md) (time-tracking example)</li></ul> | **NEW: reify "context"** |
| 10 | Nov 5 | Mircea | Real-time collaboration | Parse live queries; live sync on shared lists; two people on one task. **Mid-project check-in.** | <ul><li>[L6 Efficient Communication With the Backend](Lectures/Technical%20ID/Lecture%206/1.%20Efficient%20Communication%20With%20the%20Backend.md)</li></ul> | written |
| 11 | Nov 12 | Mircea | Efficient communication & server-side code | Do less over the wire; Parse cloud functions; one deliberate JS-vs-TS side-by-side | <ul><li>[L6 Efficient Communication](Lectures/Technical%20ID/Lecture%206/1.%20Efficient%20Communication%20With%20the%20Backend.md)</li><li>[Running Code Server-Side](Lectures/Technical%20ID/Lecture%206/2.%20Running%20Code%20Server-Side.md)</li></ul> | written + **NEW: JS-vs-TS** |
| 12 | Nov 19 | **Konstantina** *(Mircea away)* | Making it feel real: MUI & mobile-first | Use a design system, don't build one; dependencies as judgment (the `npm install` trap) | <ul><li>[General/Libraries](Lectures/Technical%20ID/General/Libraries.md)</li></ul> | **NEW: MUI + mobile-first** (K builds) |
| 13 | Nov 26 | Mircea | Refactoring & owning the code | Culmination: a student drives a **live AI-PR review** while the class interrogates it | [L7 set](Lectures/Technical%20ID/Lecture%207) — <ul><li>[Case Study](Lectures/Technical%20ID/Lecture%207/CASE_STUDY_TODO_APP.md)</li><li>[Extraction Guide](Lectures/Technical%20ID/Lecture%207/COMPONENT_EXTRACTION_GUIDE.md)</li><li>[Sprint Plan](Lectures/Technical%20ID/Lecture%207/CODE_QUALITY_SPRINT_PLAN.md)</li><li>[Class Discussion Guide](Lectures/Technical%20ID/Lecture%207/CLASS_DISCUSSION_GUIDE.md)</li><li>[Code Organization](Lectures/Technical%20ID/General/Code%20Organization.md)</li><li>[Debugging](Lectures/Technical%20ID/General/Debugging.md)</li></ul> | written + **NEW: live AI-PR framing** |
| 14 | Dec 3 | Mircea | Own it at the exam | Exam shape, the AI-permission deal restated, final integration + thin report | `Exam-Questions.md` in <ul><li>[L1](Lectures/Technical%20ID/Lecture%201/Exam-Questions.md)</li><li>[L2](Lectures/Technical%20ID/Lecture%202/Exam-Questions.md)</li><li>[L3](Lectures/Technical%20ID/Lecture%203/Exam-Questions.md)</li><li>[L4](Lectures/Technical%20ID/Lecture%204/Exam-Questions.md)</li><li>[L5](Lectures/Technical%20ID/Lecture%205/Exam-Questions.md)</li><li>[L6](Lectures/Technical%20ID/Lecture%206/Exam-Questions.md)</li></ul> | **NEW: exam structure + AI framing** |

---

## Where the material comes from

- **GH — this repo.** The technical spine, ~80% already written, under [`Lectures/Technical ID/`](Lectures/Technical%20ID). Login is already inside the L4 Parse note; live queries are already inside L6; L7 is the code-quality set anchoring week 13. Every lecture ships an `Exam-Questions.md` — a head start on the question bank.
- **learnIT — 2025 design materials.** Interviews, thematic analysis, wireframing, usability. ⚠ All links above are 2025 resource IDs and need repointing once the 2026 course shell exists.
- **NEW — the short list left to write.** See the TODO below.
- **Pre-course.** The six [Tech-TopUps](Tech-TopUps) modules (CSS, DOM, JS, layouts, coding practices, async), with **Scrimba's free tier** as the interactive companion — Learn HTML & CSS (5.7h) and Learn JavaScript (9.4h), both MDN-built; Learn React (15.1h) as a bonus. A **Node/npm setup step** runs pre-course. npm arrives in three doses: setup (pre-course) → mechanics (wk1) → judgment (wk12).

---

## How the pieces fit

**The exercise slot — 2h = 1h solo + 1h project.** Each student drills the week's concept in a sandbox, then carries it into the group project the same afternoon. Solo drills are **required but ungraded** — an existence check, not a grading anvil — and accumulate into a personal portfolio that *is* exam prep. Most drills mirror the week; on the **two design weeks (2 & 7) the solo drill is a standalone React refresher**, so the technical thread never has a dead week. In the back half, a couple of drills swap "build X" for **"review this AI-generated PR on your repo and write three comments you'd defend."**

**Two repos, two jobs.** (1) A **shared reference to-do**, git-tagged per lecture — Mircea demos on it, teams fork it as their seed. (2) A **personal exercise repo** per student, one folder per week, **checked at a glance, not by pull request** (doesn't scale at ~25 students).

**Code review as a running thread.** Introduced **wk6** on the freshly-live app with a short "good React" checklist as the rubric → sharpened by Konstantina's **wk8** patterns → practised in back-half solo drills → culminates **wk13**, student-driven and exam-shaped.

**Feedback, rehomed.** Bi-weekly PR reviews are **dropped** — they never scaled with few TAs. Replaced by four things that do: **dogfooding** (continuous "does it work"), **AI** as an always-on first-pass reviewer, **two concentrated human check-ins** (wk7 scope & data model, wk10 mid-project), and the **live AI-PR review** in wk13 — whole-class, zero per-group grading.

**Assessment — 70% individual exam / 30% group project, with a hard floor:** bomb the individual and you fail regardless of group quality. The exam is a common-core interrogation of the team's live deployed app, plus a defence of the student's own feature-menu choice. The **report is thin**: two short sections about *their* population (user study distilled; extended ER diagram + screen mapping), with raw thematic analysis in an appendix.

**Away-week coverage.** All four of Mircea's travel weeks are real lectures, not filler: Konstantina takes React (**wk8, wk12**), the designer takes interaction design (**wk2, wk7**), a guest covers React II (**wk3 — Bjørn / a TA, TBC**). Every load-bearing backend lecture (wk4, wk5) stays on an in-person week.

**TypeScript** is not a second track — optional bonus only, with one deliberate JS-vs-TS side-by-side at the Parse service layer (wk11).

---

## New — to write

- [ ] **Frontend deploy to GitHub Pages** (wk6) — the biggest single gap; nothing on hosting in the notes.
- [ ] **List collection layer** (wk5) — items point to a List; ToDo25 is single-user with no List table.
- [ ] **Reify "context"** as the spanning idea (wk9).
- [ ] **JS-vs-TS side-by-side** at the Parse service layer (wk11).
- [ ] **MUI + mobile-first** (wk12) — Konstantina to build.
- [ ] **Live AI-PR-review framing** — wk6 intro + wk13 culmination.
- [ ] **Exam structure + day-one AI-permission framing** (wk14).
- [ ] **The wk6 "good React" checklist** — 4–5 items, a yardstick not a treatise: small components, state where it belongs, clear names, no needless dependencies.
- [ ] **One-page wrapper for the design lectures** (wk2, wk7) — point the inherited user-needs material at *your own population, your own to-do*. Critical: an unfamiliar designer will otherwise drift into generic theory.
- [ ] **The project brief** — lean core, population twist, feature menu, one-story rule, AI-allowed/you-own-it, MVP framing, deploy, dogfood-vs-design.
- [ ] **Repoint learnIT links** once the 2026 course shell exists (all IDs above are 2025).

## Still open

- **Week-3 guest** — confirm Bjørn or a TA. Whoever it is teaches from **prepared slides** (not improvised live coding — that is exactly what students revolted against) and gets a short brief on the **wk3 → wk4 seam**: controlled components set up the login form.
- **MUI** — confirm formally, or have Konstantina write a short MUI-vs-Tailwind-vs-shadcn note.
- **Personal final feature** — parked as an optional verbal invitation, not a graded deliverable. Not in the syllabus unless revived.
