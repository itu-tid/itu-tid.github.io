# Technical Interaction Design — Autumn 2026

> **This file is the source.** Edit it, then run `python3 build.py` to regenerate
> [`syllabus.html`](syllabus.html) — the styled version published on GitHub Pages.
> Never hand-edit the HTML; your changes will be overwritten.

## Overview

**ITU Copenhagen · Autumn 2026 · Thursdays**

Build from minute one; deepen as you go. A **fast technical track** stands up a working, shared, deployed app in the first five weeks, while a **quieter design track** runs alongside — study your users, design for them, revise. Every team builds one **group to-do app**: the same lean core, a population-driven twist of their own. Each week has a lecture, a two-hour exercise slot, and a project milestone. **Dogfood the core, design the twist for someone unlike you, and own every line at the exam.**

In the AI era the scarce skill is **code comprehension**, not code production — owning and being able to explain code you may not have typed. So the deal with students is simple: **use AI all you want; own every line at the exam.** Everything below is built to make that deal fair.

### At a glance

- **14 weeks** — Aug 27 – Dec 3
- **Group to-do** — one project, one twist
- **2h exercise** — 1h solo · 1h project
- **70 / 30** — individual exam · group

### Teaching team

- `you` Mircea — technical
- `react` Konstantina — React
- `design` Designer — interaction design
- `away` covered lecture

## Deliverables — five checkpoints, one predictable rhythm

- **Week 2 · Fri — Population chosen** — Who you’ll build for and how you’ll reach them. Assignment 1 begins.
- **Week 6 · Fri — App live & user study in** — A deployed, shareable app — and the interviews → themes → personas writeup. The tracks meet.
- **Week 7 · Fri — Wireframes, tested** — Special screens wireframed and put through a light usability pass — before you build.
- **Week 10 · Fri — Chosen features working** — Your feature-menu picks — real-time sync, time-tracking — live in the app.
- **Week 14 — Final app + thin report** — Deployed, dogfooded, defensible. Ready for the individual exam.

Checkpoints you hit and **dogfood against** — not weekly submissions marked line-by-line. Human feedback concentrates at the **two check-ins** (weeks 7 & 10).

## Weeks

One section per week. `Solo` / `Project` are the two halves of the exercise slot;
`Status` is planning-only and does not appear in the generated HTML.

### Week 01 · Aug 27 · Mircea

**First React app: components, props & state**  
*Lecture · React I + opening*

Open with Zeeguu — “click a word, get a translation” — and watch it split into a real system. Then straight into React: components, JSX, props, state, rendering lists with keys. The running example is a to-do list.

- **Solo:** Render a list from an array; a component with props.
- **Project:** Form teams, fork the reference to-do repo; `npm install` and run it locally — what package.json, node_modules, and “a package” actually are.
- **Milestone:** Teams formed, skeleton running — *Candidate populations brainstormed.*
- **GH:** [T0-Starter-Kit](Lectures/Technical%20ID/Lecture%201/T0-React-Starter-Kit.md) · [T1-Intro-to-React](Lectures/Technical%20ID/Lecture%201/T1-Intro-to-React.md) (front half) · [T2-Hooks](Lectures/Technical%20ID/Lecture%201/T2-Hooks.md)
- **Status:** written

### Week 02 · Sep 3 · Designer

**Understanding user needs**  
*Lecture · Design I*

Interviews, thematic analysis, personas, user stories — pointed at *your* population. Introduce the onion: the core is lists + items + sharing; every extra feature must earn its ring or it doesn’t ship.

- **Solo:** React refresher (standalone): props & state reps — keep it warm before React II.
- **Project:** Pick your population; plan the user study.
- **Milestone:** Population chosen — *Assignment 1 (user study) begins.*
- **learnIT:** The ID Process ([slides](https://learnit.itu.dk/mod/resource/view.php?id=228493) + [notes](https://learnit.itu.dk/mod/resource/view.php?id=230914)) · [User Interviews & Thematic Analysis](https://learnit.itu.dk/mod/assign/view.php?id=228499) · [Braun & Clarke 2019](https://learnit.itu.dk/mod/resource/view.php?id=230965) · [personas / user stories](https://learnit.itu.dk/mod/resource/view.php?id=231338) · [Tricia Wang talk](https://learnit.itu.dk/mod/kalvidres/view.php?id=230963)
- **Status:** adapt — needs the **one-page wrapper**

### Week 03 · Sep 10 · Bjørn / TAs? *(Mircea away)*

**Controlled components, forms & useEffect**  
*Lecture · React II · guest — to confirm*

Events, controlled inputs, form handling, conditional rendering, lists in state — squarely a frontend developer’s home turf, the right lecture for an away week. Then `useEffect`, met first against someone else’s API: fetch JSONPlaceholder `/todos` into your list. Next week the same hook points at a backend you own.

- **Solo:** Build one controlled form component from scratch; fetch a list with `useEffect`.
- **Project:** Add / edit items as a controlled form.
- **Milestone:** Add & edit items work in the UI — *Interviews being conducted in parallel.*
- **GH:** [T1-Intro-to-React](Lectures/Technical%20ID/Lecture%201/T1-Intro-to-React.md) (back half): event handling → controlled components → conditional rendering · [T3-the-useEffect-Hook](Lectures/Technical%20ID/Lecture%201/T3-the-useEffect-Hook.md) — pulled forward from week 4
- **Status:** written — **useEffect pulled forward from week 4**

### Week 04 · Sep 17 · Mircea

**Database & login, together**  
*Lecture · Backend I*

Parse, a real database, and authentication in one move — the login form is where last week’s controlled components pay off, and last week’s `useEffect` now runs against a backend you own rather than a public API. The core data model lands: owner → lists → items. The load-bearing bridge, taught in person.

- **Solo:** Connect to Parse; save and read one object.
- **Project:** Stand up the backend; wire the to-do to a shared DB.
- **Milestone:** Backend live · items persist · login works — *Dogfooding possible: localhost against a shared DB.*
- **GH:** [L4 Backends & the Parse Platform](Lectures/Technical%20ID/Lecture%204/1.%20Backends-and-the-Parse-Platform.md) (login included) · [Parse-Config-for-Vite](Lectures/Technical%20ID/Lecture%204/Parse-Configuration-for-Vite.md) · [T3-useEffect](Lectures/Technical%20ID/Lecture%201/T3-the-useEffect-Hook.md) (revisit — now against your own backend)
- **Status:** written — reframed, lightened by week 3

### Week 05 · Sep 24 · Mircea

**Sharing: ACLs, roles, private vs shared**  
*Lecture · Backend II*

Authorization and ACL in Parse — the group mechanism. A private list is owner-only; a shared list is a team role. This is the collection layer: items point to a List, sharing lives at the list level. The ACL lesson wearing a friendly face.

- **Solo:** Set an ACL on an object; create and assign a role.
- **Project:** Implement private vs shared lists with roles.
- **Milestone:** A list can be private or shared with a team — *Thematic analysis → personas + user stories.*
- **GH:** [L5 Authorization & ACL in Parse](Lectures/Technical%20ID/Lecture%205/Authorization-and-ACL%20in%20Parse.md) (ToDo25)
- **New:** List collection layer — items point to a List (ToDo25 is single-user)
- **Status:** written + **NEW: List collection layer**

### Week 06 · Oct 1 · Mircea

**Routing, git-flow, and going live**  
*Lecture · Routing + deploy*

Start with the arc that explains everything you’ve built: three generations of web apps — server-rendered pages → server scripts generating pages → single-page apps. *That’s* what you’ve been making, an SPA — which is exactly why it needs client-side routing. Then routing in a single-page app, collaboration with git-flow, and deployment. The app goes public on GitHub Pages; the SPA-routing quirk is reframed as a feature that forces real understanding. It’s now shareable and installable. And with a live app to judge against, a first taste of the course’s core skill: we **review an AI-generated PR to it together**, against a short checklist of what good React looks like — small components, state where it belongs, clear names, no needless dependencies. That checklist is your rubric for every review from here on.

- **Solo:** Add a route with a URL parameter; deploy one page.
- **Project:** Add routing; deploy the app publicly.
- **Milestone:** App is live, public, shareable — *Assignment 1 due · optional PWA manifest → on their phones.*
- **GH:** [L3 Web-App-Architectures](Lectures/Technical%20ID/Lecture%203/1.%20Web-App-Architectures.md) · [Routing in React](Lectures/Technical%20ID/Lecture%203/2.%20Routing%20in%20React.md) · [Collaboration with Git-Flow](Lectures/Technical%20ID/Lecture%203/3.%20Collaboration-with-Git-Flow.md) · [General/Code-Organization](Lectures/Technical%20ID/General/Code%20Organization.md) + [L7 cheatsheet](Lectures/Technical%20ID/Lecture%207/COMPONENT_EXTRACTION_CHEATSHEET.md) (the review checklist)
- **New:** Frontend deploy → GitHub Pages (not in the notes yet)
- **Status:** **NEW: frontend deploy** + **NEW: review checklist**

### Week 07 · Oct 8 · Designer *(Mircea away)*

**Screen design & usability for your population**  
*Lecture · Design II*

Model your own extension and sketch your special screens as **wireframes** — then put them through a light usability pass (a heuristic walkthrough or three quick think-alouds with classmates) *before* anyone builds. Cheap to test a wireframe, expensive to test a polished screen: this is why we wireframe over Figma. Accessibility is the through-line (now legally live in Denmark). Imitate then originate: you were handed the core data model — now you design your own for the people you studied.

- **Solo:** React refresher (standalone): a small component drill — revive the frontend muscle after five backend weeks.
- **Project:** Wireframe the special screens; run a quick usability pass on them; extend the ER diagram.
- **Milestone:** Wireframes tested · extended data model designed — *The loop turns: build → design → test → revise.*
- **Check-in:** Check-in — is your scope & data model sound?
- **learnIT:** [Requirements, User Flows & Wireframing](https://learnit.itu.dk/mod/assign/view.php?id=228506) · [Prototyping slides](https://learnit.itu.dk/mod/resource/view.php?id=231641) · [Lauesen ch.13](https://learnit.itu.dk/mod/resource/view.php?id=228522) · [NN/g Heuristic Evaluation Workbook](https://learnit.itu.dk/mod/url/view.php?id=234019) · [Usability Report template](https://learnit.itu.dk/mod/url/view.php?id=228523)
- **Status:** adapt — needs the **one-page wrapper**

### Break · Oct 15

Autumn break — no lecture

### Week 08 · Oct 22 · Konstantina *(Mircea away)*

**Intermediate React patterns**  
*Lecture · React III*

Extracting components, updater functions, updating objects and lists in state, useRef, and the patterns of component communication — the toolkit for a project that’s now growing real features. This is also *what good React looks like*: it sharpens the checklist students review AI PRs against. Another strong away-week fit.

- **Solo:** Lift state up; extract a reusable component.
- **Project:** Refactor the project; build special-feature components.
- **Milestone:** Special features taking shape — *Cleaner component structure across the app.*
- **GH:** L2 T4–T8: [Extracting Components](Lectures/Technical%20ID/Lecture%202/T4-Refactoring%20by%20Extracting%20Components.md) · [Updater Functions](Lectures/Technical%20ID/Lecture%202/T5-Updater-Functions-for-State.md) · [Updating Objects & Lists](Lectures/Technical%20ID/Lecture%202/T6-Updating%20Objects%20and%20Lists%20in%20State.md) · [useRef](Lectures/Technical%20ID/Lecture%202/T7-React-the-useRef-Hook.md) · [Component Communication](Lectures/Technical%20ID/Lecture%202/T8-Patterns%20of%20Component%20Communication.md)
- **Status:** written

### Week 09 · Oct 29 · Mircea

**Time-tracking, and the idea of context**  
*Lecture · Depth I*

A simple feature that blooms: you can’t run two timers at once, so starting one must stop another — which means the app must know what’s *active*. That’s a **context** spanning all lists. And since Parse ACLs are object-level not field-level, private timing splits into its own table. Complexity where AI stops helping.

- **Solo:** Build a start/stop timer with a single active context.
- **Project:** Teams who chose it: add time-tracking with context.
- **Milestone:** First menu feature integrated — *Context reified where two timers would collide.*
- **GH:** [L5 time-tracking example](Lectures/Technical%20ID/Lecture%205/Authorization-and-ACL%20in%20Parse.md) (totalTime / currentSessionStart / TodoTimeTracking table)
- **New:** Reify “context” as the spanning idea
- **Status:** **NEW: reify "context"**

### Week 10 · Nov 5 · Mircea

**Real-time collaboration**  
*Lecture · Depth II*

Two people on one task; Parse live queries; live sync across a shared list. And the collision worth naming: if two people track time on one task, whose time is it? Multi-user reality lands on the app they already live in.

- **Solo:** Subscribe to a live query; react to a remote change.
- **Project:** Real-time updates on shared lists.
- **Milestone:** Live sync working — *Teams dogfood in earnest — changes appear for everyone.*
- **Check-in:** Mid-project check-in — one focused conversation per group
- **GH:** [L6 Efficient Communication With the Backend](Lectures/Technical%20ID/Lecture%206/1.%20Efficient%20Communication%20With%20the%20Backend.md) — live queries / real-time
- **Status:** written

### Week 11 · Nov 12 · Mircea

**Efficient communication & server-side code**  
*Lecture · Depth III*

Do less over the wire; move work into Parse cloud functions. The one place types earn their keep — a deliberate JS-vs-TS side-by-side at the service layer. (TypeScript stays an optional bonus, not a second track.)

- **Solo:** Write one cloud function; measure the round-trips saved.
- **Project:** Move one operation server-side.
- **Milestone:** Server-side logic where it earns its place — *Chosen feature-menu subset complete.*
- **GH:** [L6 Efficient Communication](Lectures/Technical%20ID/Lecture%206/1.%20Efficient%20Communication%20With%20the%20Backend.md) · [Running Code Server-Side](Lectures/Technical%20ID/Lecture%206/2.%20Running%20Code%20Server-Side.md)
- **New:** JS-vs-TS side-by-side at the service layer
- **Status:** written + **NEW: JS-vs-TS**

### Week 12 · Nov 19 · Konstantina *(Mircea away)*

**Making it feel real: MUI & mobile-first**  
*Lecture · React IV*

A component library (MUI — fast, accessible, functional) and a mobile-first pass. Use a design system, don’t build one. This is also where packages become a *judgment*: what you take on when you add a dependency, and why blindly `npm install`-ing whatever the AI suggests is the not-owning-your-code trap. Polish that turns a working prototype into something you’d actually keep on your phone.

- **Solo:** Rebuild one screen with MUI components.
- **Project:** Apply MUI; do a mobile-first pass.
- **Milestone:** Polished, mobile-first UI — *The app feels real.*
- **GH:** [General / Libraries](Lectures/Technical%20ID/General/Libraries.md) (dependency judgment)
- **New:** MUI + mobile-first pass — Konstantina to build
- **Status:** **NEW: MUI + mobile-first** (Konstantina builds)

### Week 13 · Nov 26 · Mircea

**Refactoring & owning the code**  
*Lecture · Code quality — culmination*

The skill you’ve practiced since week 6, at full strength. By now you’ve reviewed several AI PRs in your solo drills — today one of you **drives a live review** in front of the class while everyone interrogates it. Read the AI’s code: what’s wrong, what’s subtly wrong, what works but over-reaches (a needless dependency, a component that should’ve been three), and what you can’t yet explain — because what you can’t defend, you don’t own. The thesis at full volume, and exam prep in the open.

- **Solo:** Review an AI-generated PR on your own repo; write three review comments you’d stand behind.
- **Project:** Your turn to drive: one member reviews an AI PR live while the group interrogates it — rehearsal for exam questioning.
- **Milestone:** Codebase cleaned — *Every member can explain every part.*
- **GH:** L7 code-quality set: [Case-Study ToDo](Lectures/Technical%20ID/Lecture%207/CASE_STUDY_TODO_APP.md) · [Component-Extraction Guide](Lectures/Technical%20ID/Lecture%207/COMPONENT_EXTRACTION_GUIDE.md) + [Cheatsheet](Lectures/Technical%20ID/Lecture%207/COMPONENT_EXTRACTION_CHEATSHEET.md) · [Code-Quality Sprint Plan](Lectures/Technical%20ID/Lecture%207/CODE_QUALITY_SPRINT_PLAN.md) · [Class-Discussion Guide](Lectures/Technical%20ID/Lecture%207/CLASS_DISCUSSION_GUIDE.md) · [General/Code-Organization](Lectures/Technical%20ID/General/Code%20Organization.md) · [Debugging](Lectures/Technical%20ID/General/Debugging.md)
- **New:** Live AI-PR-review framing
- **Status:** written + **NEW: live AI-PR framing**

### Week 14 · Dec 3 · Mircea

**Own it at the exam**  
*Lecture · Wrap & exam prep*

Walk through the exam shape — common-core interrogation of your live app, then defend your own feature menu. Revisit the deal: use AI all you want; own every line when we meet. Final integration and the thin report.

- **Solo:** Mock exam questions on your own app.
- **Project:** Final integration; deploy the final version; finish the report.
- **Milestone:** Final deployed app + thin report — *Ready for the individual exam.*
- **GH:** [Exam-Questions.md](Lectures/Technical%20ID) across every lecture (question bank)
- **New:** Exam structure + day-one AI-permission framing
- **Status:** **NEW: exam structure + AI framing**

## How the pieces fit

### The exercise slot

**1h solo, then 1h project.** Everyone personally drills the week’s concept in a sandbox, then carries it into the group project the same afternoon. Solo drills are **required but ungraded** — an existence check, not a grading anvil — and pile up into a personal portfolio that *is* your exam prep. Most drills mirror the week; on the **two design weeks (2 & 7) the solo drill is a standalone React refresher** so the technical thread never has a dead week. And a couple of times in the back half, the drill swaps “build X” for **“review this AI-generated PR on your repo and write three comments you’d defend”** — code review as spaced repetition, not a one-off.

### Code review, a running thread

The course’s core skill isn’t taught once at the end — it’s a habit built from the moment there’s an app to judge. **Introduced week 6** on the freshly-live app, with a short **“good React” checklist** as the rubric (sharpened by Konstantina’s week-8 patterns). **Practised** as recurring back-half solo drills. **Culminates week 13**, student-driven and exam-shaped. Reading and judging code you didn’t write, rising in independence — the same imitate → originate arc as everything else here.

### Two repos, two jobs

A **shared reference to-do**, git-tagged per lecture, is the canonical good code and the seed each team forks. A **personal exercise repo** — one folder per week — holds the solo drills, checked at a glance, not by pull request.

### The project constraint

Lean required core: owner → lists → items, sharing at the list level. Everything else is an **optional feature menu** — project grouping, time-tracking + context, two-on-one-task — that teams pick from and defend. One population, one twist, fully built.

### Dogfood vs design

Teams run their own coordination on the app all term (dogfood the core), but design the distinctive features **for an outside population** they go and study — carer + elderly parent, flatmates, event crews. Accessibility is the shared lens.

### Assessment

**70% individual exam, 30% group project**, with a hard floor: bomb the individual and you fail, however strong the group. The project is your exam curriculum — if you used it, you understand it.

### Feedback, rehomed

No weekly pull-request reviews — they never scaled at this size. Instead: **dogfooding** tells you continuously whether it works, **AI** is your always-on first-pass code reviewer, and human feedback **concentrates at two check-ins** (wk 7 scope & data model, wk 10 mid-project) plus a **live AI-PR review** in wk 13 — whole-class, zero per-group grading.

### Away weeks

All four travel weeks are covered by real lectures, not filler: Konstantina takes React (wk 8, 12), a guest covers React II (wk 3 — Bjørn / a TA, to confirm), the designer takes screen design (wk 7). Every load-bearing backend lecture stays on an in-person week.

### Where each week’s material comes from

`GH` your [**itu-tid/lecture-notes**](https://github.com/itu-tid/lecture-notes) — the technical spine, mostly already written. `learnIT` last year’s **design materials** — interviews, thematic analysis, wireframing, usability. `New` the short list left to write: **frontend deploy to GitHub Pages** (wk 6), List collection layer (wk 5), context (wk 9), TS side-by-side (wk 11), MUI + mobile-first (wk 12, Konstantina), live AI-PR framing (wk 13), exam + AI framing (wk 14).

### Pre-course

The six **Tech-TopUps** modules (CSS, DOM, JS, layouts, coding practices, async), with **Scrimba’s free tier** as the interactive companion — Learn HTML & CSS (5.7h) and Learn JavaScript (9.4h), both MDN-built; Learn React (15.1h) as a bonus. A **Node/npm setup step** runs pre-course. npm arrives in three doses: setup (pre-course) → mechanics (wk 1) → judgment (wk 12).

*Draft · sequencing subject to change · built Aug 2026*

## Still to write

- [ ] **Frontend deploy to GitHub Pages** (wk 6) — the biggest single gap; nothing on hosting in the notes.
- [ ] **List collection layer** (wk 5) — items point to a List; ToDo25 is single-user with no List table.
- [ ] **Reify "context"** as the spanning idea (wk 9).
- [ ] **JS-vs-TS side-by-side** at the Parse service layer (wk 11).
- [ ] **MUI + mobile-first** (wk 12) — Konstantina to build.
- [ ] **Live AI-PR-review framing** — wk 6 intro + wk 13 culmination.
- [ ] **Exam structure + day-one AI-permission framing** (wk 14).
- [ ] **The wk 6 "good React" checklist** — 4–5 items, a yardstick not a treatise: small components, state where it belongs, clear names, no needless dependencies.
- [ ] **One-page wrapper for the design lectures** (wk 2, wk 7) — point the inherited user-needs material at *your own population, your own to-do*. Critical: an unfamiliar designer will otherwise drift into generic theory.
- [ ] **The project brief** — lean core, population twist, feature menu, one-story rule, AI-allowed/you-own-it, MVP framing, deploy, dogfood-vs-design.
- [ ] **Repoint learnIT links** once the 2026 course shell exists — every learnIT link above is a 2025 resource ID.

## Open decisions

- **Week-3 guest** — confirm Bjørn or a TA. Whoever it is teaches from **prepared slides** (not improvised live coding — that is exactly what students revolted against) and gets a short brief on the **wk 3 → wk 4 seam**: controlled components set up the login form.
- **MUI** — confirm formally, or have Konstantina write a short MUI-vs-Tailwind-vs-shadcn note.
- **Personal final feature** — parked as an optional verbal invitation, not a graded deliverable. Not in the syllabus unless revived.
