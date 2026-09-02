Notes for **Technical Interaction Design** at the IT University of Copenhagen.

## Autumn 2026

- **[Syllabus](syllabus.html)** — week by week: who teaches what, which notes back each lecture, and what is due when.
- **[Working as a Team](Project-Collaboration.md)** — how a group divides the project
- **[Report Structure](Report-Structure.md)** — what goes in the final report
- **[Exam Structure](Exam-Structure.md)** — how the oral runs, and what you get asked
- **[Coding Guidelines](Coding-Guidelines.md)**

## How the course runs

**Mircea** teaches the technical track; **Konstantina** teaches the design track — weeks 3, 7, 8, 9 and 12. **Lea** runs the Figma clinic in week 7, **Anna** the Back4App walkthrough in week 4; both are in the exercise hours every week.

Each Thursday: a lecture, then two hours of exercise — **one hour on your own**, one hour **with your group**. Weeks 1 and 2 are entirely individual, because the teams do not exist yet.

**This course has no mandatory activities**, in the [formal ITU sense](https://itustudent.itu.dk/Study-Administration/Rights-and-Requirements) of something you must pass to be allowed to sit the exam. Nothing here can cost you an exam attempt. The solo hour is not graded and not checked — it is simply where you learn this, and what it piles up into is a personal portfolio that is your exam preparation. The deadlines below are checkpoints you hit and get feedback on, not submissions marked line by line.

**Use your personal GitHub account, not the ITU one.** Two reasons: what you build here is worth having in public under your own name after the course ends, and the ITU enterprise account is more restricted than a personal one.

**Your group's repository goes in a free organisation your team creates**, with all four of you as owners — not on one member's account. A repository owned by a person can only be pinned to *that* person's profile, so three of you would end the course with nothing to show. In an organisation, everyone who has committed to it can pin it.

While we are on it: **commit with the email address your GitHub account knows about.** Git takes whatever `git config user.email` says, and if that is an address GitHub does not recognise, your commits are not linked to you at all — no contribution graph, no credit, on the one repository you most want credit for. Check with `git config user.email`, and compare it against the addresses in your GitHub account settings.

**70% individual exam, 30% group project**, with a hard floor: bomb the individual and you fail, however strong the group. The project is your exam curriculum — if you used it, you understand it.

The last two minutes of every lecture are yours: **[one anonymous question](https://forms.gle/pse8zJNMQthy4UcFA)**, the same link every week. It gets read before the next lecture and answered at the start of it — which is the only reason it is worth your two minutes.

## Deadlines

Every one is a **Tuesday at 23:59**. Checkpoints you hit and dogfood against, not submissions marked line by line.

**The project starts with people, not with code.** The first thing you produce is not a repository — it is a handful of interviews, the themes that keep coming up across them, and the tasks those themes turn into. Week 3 teaches how, and the first deliverable below is where you hand it in. What you build afterwards is shaped by what you find there, which is the whole argument of the course.

| due | what |
|---|---|
| **Tue 8 Sep** | Teams registered on learnIT. **Four is the size we want**; if that does not work for you, email us before this date. Weeks 1 and 2 are individual. |
| **Tue 22 Sep** | Themes → tasks — your population, three to five themes with quotes, each mapped to a [task](Lectures/Interaction-Design/Tasks.md), prioritised |
| **Tue 20 Oct** | Wireframes, tested — the screens your population needs, what testing changed, and the extended ER diagram |
| **Tue 10 Nov** | Visual & accessibility pass — the a11y audit, and what the visual pass changed |
| **Tue 24 Nov** | Chosen features working — your feature-menu picks, live in the app |
| **December** | Final app + thin report — deployed, dogfooded, defensible. Date set by the exam schedule. |

Each design deliverable lands about two weeks after the lecture that teaches it, and the feedback opens a later lecture — so there is time to act on it before the next one depends on it.

## Lecture notes

Two folders, split by who owns the material: [`Lectures/Technical/`](Lectures/Technical) and [`Lectures/Interaction-Design/`](Lectures/Interaction-Design). Inside each, the notes are flat. Which note belongs to which week is decided by the syllabus and nothing else — filenames deliberately do not encode it, because the ordering changes every year and a folder name has no way of telling you it has gone stale. Track does not change, which is why it is the one thing the folders *do* encode. Each note ends with its own **Exam Questions**, so a question can never drift from the material it tests.

Course order, as the 2026 syllabus runs it — generated from it, so the two cannot disagree:

<!-- weeks:start -->

| week | notes | the solo hour |
|---|---|---|
| **1** · Aug 27 | [Intro to React](Lectures/Technical/React/Intro-to-React.md) · [Component State](Lectures/Technical/React/Component-State.md) · [Hooks](Lectures/Technical/React/Hooks.md) | Scaffold your own app with Vite, following the [starter kit](Lectures/Technical/React/React-Starter-Kit.md) — `npm create`, `npm install`, `npm run dev` — and look at what appeared: package.json, node_modules, and what “a package” actually is. |
| **2** · Sep 3 | [Forms & Controlled Components](Lectures/Technical/React/Forms-and-Controlled-Components.md) · [Conditional Rendering](Lectures/Technical/React/Conditional-Rendering.md) · [The useEffect Hook](Lectures/Technical/React/The-useEffect-Hook.md) | Build one controlled form from scratch; |
| **3** · Sep 10 | [The Interaction Design Process](Lectures/Interaction-Design/The-Interaction-Design-Process.md) · [Tasks](Lectures/Interaction-Design/Tasks.md) | CSS, on the app you already have — layout, type, spacing, colour. |
| **4** · Sep 17 | [Backends & the Parse Platform](Lectures/Technical/Backend/Backends-and-the-Parse-Platform.md) (login included) · [§ Modeling Relationships in Parse](Lectures/Technical/Backend/Backends-and-the-Parse-Platform.md#modeling-relationships-in-parse) · [§ Entity-Relationship Diagrams](Lectures/Technical/Backend/Backends-and-the-Parse-Platform.md#entity-relationship-diagrams) · [Parse Configuration for Vite](Lectures/Technical/Backend/Parse-Configuration-for-Vite.md) · [Debugging](Lectures/Technical/React/Debugging.md) | Replication — set up your *own* Parse app in your personal repo, following the lecture steps, with a TA in the room. |
| **5** · Sep 24 | [Authorization & ACL in Parse](Lectures/Technical/Backend/Authorization-and-ACL-in-Parse.md) (ToDo25) | Set an ACL on an object; |
| **6** · Oct 1 | [Web App Architectures](Lectures/Technical/Routing/Web-App-Architectures.md) · [Routing in React](Lectures/Technical/Routing/Routing-in-React.md) · [Protecting Routes If Not Logged In](Lectures/Technical/Routing/Protecting-Routes.md) | Add a route with a URL parameter; |
| **7** · Oct 8 | [Usability and Its Evaluation](Lectures/Interaction-Design/Usability-and-Its-Evaluation.md) · [10 worked heuristic counterexamples](Lectures/Interaction-Design/usability-examples) | Run a heuristic walkthrough over a classmate's wireframes; |
| **8** · Oct 22 | [Collaboration with Git-Flow](Lectures/Technical/Tooling/Collaboration-with-Git-Flow.md) · [Finding the Components](Lectures/Technical/Structure/Finding-the-Components.md) · [Patterns of Component Communication](Lectures/Technical/React/Patterns-of-Component-Communication.md) · [Code Organization](Lectures/Technical/Structure/Code-Organization.md) + [Component-extraction cheatsheet](Lectures/Technical/Structure/Component-Extraction-Cheatsheet.md) (the review checklist) | Open and merge one branch through git-flow; |
| **9** · Oct 29 | [Libraries](Lectures/Technical/Tooling/Libraries.md) (dependency judgment) | Rebuild one screen with MUI in your own repo — the type scale, the palette and the spacing you get for free, and what you gave up to get them. |
| **10** · Nov 5 | [Extracting Components, and Where the State Goes](Lectures/Technical/Structure/Refactoring-by-Extracting-Components.md) · [The useRef Hook](Lectures/Technical/React/The-useRef-Hook.md) · [Component-Extraction Guide](Lectures/Technical/Structure/Component-Extraction-Guide.md) | Extract one overgrown component in your own repo, and lift whatever state the extraction stranded. |
| **11** · Nov 12 | [Efficient Communication](Lectures/Technical/Backend/Efficient-Communication-with-the-Backend.md) (live queries included) · [Updater Functions for State](Lectures/Technical/React/Updater-Functions-for-State.md) · [Running Code Server-Side](Lectures/Technical/Backend/Running-Code-Server-Side.md) | Write one cloud function and measure the round-trips saved; |
| **12** · Nov 19 | [Time-tracking example](Lectures/Technical/Backend/Authorization-and-ACL-in-Parse.md) (totalTime / currentSessionStart / TodoTimeTracking) | Build a start/stop timer with a single active context. |
| **13** · Nov 26 | [Component-Extraction Guide](Lectures/Technical/Structure/Component-Extraction-Guide.md) | Review an AI-generated PR on your own repo; |
| **14** · Dec 3 | [Report Structure](Report-Structure.md) · [Exam Structure](Exam-Structure.md) · every note ends with its own Exam Questions | Mock exam questions on your own app. |

<!-- weeks:end -->

## TopUps

Short self-study modules in [`TopUps/`](TopUps), covering the background a lecture assumes but does not teach. Only the first is due before the course starts; the rest arrive on the card of the week that needs them, so read each one *before* the week beside it.

| read before | module |
|---|---|
| now, if you want it | [0 · HTML, the little you need](TopUps/0-HTML-the-little-you-need.md) — assumed by week 1, and never taught. Nine tags and where JSX differs. |
| week 1 | [3 · JavaScript, the Language](TopUps/3-Javascript-the-Language.md) |
| the exercise hour | [React Starter Kit](Lectures/Technical/React/React-Starter-Kit.md) — scaffolding your own app with Vite |
| week 2 | [1 · Basics of CSS](TopUps/1-Basics-of-CSS.md) |
| week 4 | [6 · Async Programming & Promises](TopUps/6-Async-Programming-and-Promises.md) |
| week 8 | [5 · Coding Practices](TopUps/5-Coding-Practices.md) |
| week 9 | [4 · Layouts and Responsiveness](TopUps/4-Layouts-and-Responsiveness.md) |
| week 13, optional | [2 · DOM Manipulation with JavaScript](TopUps/2-DOM-Manipulation-with-Javascript.md) |

## Chapters as PDF

Each week's notes bundled into one PDF, for reading offline or printing: **<https://itu-tid.github.io/lecture-notes-pdf/>**

They are generated from the notes in this repository, so if the two ever disagree, the markdown here is the newer one.

## The app we build

[itu-tid/todo-26](https://github.com/itu-tid/todo-26) — the reference to-do, tagged once per lecture (`git checkout week-01`). It is there to read and compare against, not to start from: your group builds its own repo from empty, on the model your own user study produced.

---

Maintaining the course? [DEVELOPER.md](DEVELOPER.md) — how the syllabus is built, and what lives in the vault instead of here.
