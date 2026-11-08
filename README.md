Notes for **Technical Interaction Design** at the IT University of Copenhagen.

## Autumn 2026

- **[Syllabus](syllabus.html)** — week by week: who teaches what, which notes back each lecture, and what is due when.
- **[Working as a Team](Project-Collaboration.md)** — how a group divides the project
- **[Report Structure](Report-Structure.md)** — what goes in the final report
- **[Exam Structure](Exam-Structure.md)** — how the oral runs, and what you get asked
- **[Coding Guidelines](Coding-Guidelines.md)**

## How the course runs

**Mircea** teaches the technical track; **Konstantina** teaches the design track — weeks 3, 7, 8, 9 and 12. **Lea** runs the Figma clinic in week 7, **Anna** the Back4App walkthrough in week 4; both are in the exercise hours every week.

Each Thursday: a lecture, then two hours of exercise — **one hour on your own**, one hour **with your group**. Weeks 1 and 2 are entirely individual, because the teams do not exist yet. From week 10 on, both hours go to the group project.

**Every group hand-in below is a mandatory activity**, in the [formal ITU sense](https://itustudent.itu.dk/Study-Administration/Rights-and-Requirements): the course description requires them before you may sit the exam, and they are what it calls your portfolio contributions. They are not graded, only approved or not approved, and each one comes back with feedback. One that is not approved can be resubmitted before the exam hand-in. Every hand-in lists the group members who contributed to it, because the requirement is that each of you takes part. If you have missed a hand-in so far, email us with the reason and we will make it work.

**The solo hour is not mandatory.** It ran until week 9. It is not graded and not checked: it is where you learn this, and it is your preparation for the individual exam.

**Use your personal GitHub account, not the ITU one.** Two reasons: what you build here is worth having in public under your own name after the course ends, and the ITU enterprise account is more restricted than a personal one.

**Your group's repository goes in a free organisation your team creates**, with all four of you as owners — not on one member's account. A repository owned by a person can only be pinned to *that* person's profile, so three of you would end the course with nothing to show. In an organisation, everyone who has committed to it can pin it.

While we are on it: **commit with the email address your GitHub account knows about.** Git takes whatever `git config user.email` says, and if that is an address GitHub does not recognise, your commits are not linked to you at all — no contribution graph, no credit, on the one repository you most want credit for. Check with `git config user.email`, and compare it against the addresses in your GitHub account settings.

**70% individual exam, 30% group project**, with a hard floor: bomb the individual and you fail, however strong the group. The project is your exam curriculum — if you used it, you understand it.

The last two minutes of every lecture are yours: **[one anonymous question](https://forms.gle/pse8zJNMQthy4UcFA)**, the same link every week. It gets read before the next lecture and answered at the start of it — which is the only reason it is worth your two minutes.

## Deadlines

Every one is a **Tuesday at 23:59**, except the user study, which was due at 09:00. Each is a mandatory hand-in, approved or not approved, with feedback.

**The project starts with people, not with code.** The first thing you produce is not a repository — it is a handful of interviews, the themes that keep coming up across them, and the tasks those themes turn into. Week 3 teaches how, and the first deliverable below is where you hand it in. What you build afterwards is shaped by what you find there, which is the whole argument of the course.

| due            | what                                                                                                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tue 8 Sep**  | Teams registered on learnIT. **Four is the size we want**; if that does not work for you, email us before this date. Weeks 1 and 2 are individual.                                                      |
| **Tue 29 Sep** | Interviews → what to build — your population, how you analysed the interviews, what the app has to do (any format, traceable and prioritised), and the feature you will build. The brief is on learnIT. |
| **Tue 27 Oct** | Wireframes, tested — the screens your population needs, what testing changed, and the ER diagram of your app. Extended from Fri 23 Oct.                                                                 |
| **Tue 10 Nov** | Visual & accessibility pass — the a11y audit, and what the visual pass changed                                                                                                                          |
| **Tue 24 Nov** | Chosen features working — your feature-menu picks, live in the app                                                                                                                                      |
| **December**   | Final app + thin report — deployed, dogfooded, defensible. Date set by the exam schedule.                                                                                                               |

Each design deliverable lands about two weeks after the lecture that teaches it, and the feedback opens a later lecture — so there is time to act on it before the next one depends on it.

## Lecture notes

Two folders, split by who owns the material: [`Lectures/Technical/`](Lectures/Technical) and [`Lectures/Interaction-Design/`](Lectures/Interaction-Design). Inside each, the notes are flat. Which note belongs to which week is decided by the syllabus and nothing else — filenames deliberately do not encode it, because the ordering changes every year and a folder name has no way of telling you it has gone stale. Track does not change, which is why it is the one thing the folders *do* encode. Each note ends with its own **Exam Questions**, so a question can never drift from the material it tests.

Course order, as the 2026 syllabus runs it — generated from it, so the two cannot disagree:

<!-- weeks:start -->

| week | notes | the solo hour |
|---|---|---|
| **1** · Aug 27 | [Intro to React](Lectures/Technical/React/Intro-to-React.md) · [Hooks](Lectures/Technical/React/Hooks.md) | Scaffold your own app with Vite, following the [starter kit](Lectures/Technical/React/React-Starter-Kit.md) — `npm create`, `npm install`, `npm run dev` — remove Vite's example code, and rebuild the class to-do from your notes: an array of items, a component with props, keys. |
| **2** · Sep 3 | [Component State](Lectures/Technical/React/Component-State.md) · [Forms & Controlled Components](Lectures/Technical/React/Forms-and-Controlled-Components.md) · [Conditional Rendering](Lectures/Technical/React/Conditional-Rendering.md) · [The useEffect Hook](Lectures/Technical/React/The-useEffect-Hook.md) | Copy the class code into `week-02/`. |
| **3** · Sep 10 | [The Interaction Design Process](Lectures/Interaction-Design/The-Interaction-Design-Process.md) | CSS, on the app you already have: how props and callbacks carry information up and down the tree, how styles flow downwards, the browser's inspector, a custom font, a mobile-first layout that stops growing at 600px, and buttons — with specificity and inheritance. |
| **4** · Sep 17 | [Backends and Low-Code Backends](Lectures/Technical/Backend/Backends-and-Low-Code-Backends.md) · [Replacing localStorage with a Real Database](Lectures/Technical/Backend/Backends-Low-Code-Backends-and-the-Parse-Platform.md) | Set up your *own* Back4App app and connect your to-do list to it, with a TA in the room: install Parse, put the Parse calls in a `services/todoService.js`, and switch the list's add, toggle and delete over to it. |
| **5** · Sep 24 | [Authentication & Authorization in Parse](Lectures/Technical/Backend/Authorization-and-ACL-in-Parse.md) · [Relationships Between Object Classes](Lectures/Technical/Backend/Relationships-Between-Object-Classes.md) | Add an auth page and conditional rendering to your own app; |
| **6** · Oct 1 | [Sharing a List Is a Many-to-Many Relationship](Lectures/Technical/Backend/Many-to-Many-Sharing-a-List.md) · [Publishing Your App on GitHub Pages](Lectures/Technical/Tooling/Publishing-on-GitHub-Pages.md) · [Routing in React](Lectures/Technical/Routing/Routing-in-React.md) · [The Three States of Remote Data](Lectures/Technical/React/The-Three-States-of-Remote-Data.md) | In your own app, load the user's lists, give each its own form and its own to-dos through a pointer, then give each list its own page with React Router and `Link`. |
| **7** · Oct 8 | [Usability and Its Evaluation](Lectures/Interaction-Design/Usability-and-Its-Evaluation.md) · [10 worked heuristic counterexamples](Lectures/Interaction-Design/usability-examples) | Figma, with Lea: a team with Education status, frames, auto layout, components, dev mode, and the community files. |
| **8** · Oct 22 | [Collaboration with Git-Flow](Lectures/Technical/Tooling/Collaboration-with-Git-Flow.md) · [Pulling Out the Service Layer](Lectures/Technical/Structure/Pulling-Out-the-Service-Layer.md) · [Code Organization](Lectures/Technical/Structure/Code-Organization.md) + [Component-extraction cheatsheet](Lectures/Technical/Structure/Component-Extraction-Cheatsheet.md) (the review checklist) · [Finding the Components](Lectures/Technical/Structure/Finding-the-Components.md) | Make a feature branch from `development`, move the list query out of `ListPage.jsx` into `loadList(listId)` in a service, push it, and open a pull request. |
| **9** · Oct 29 | [Libraries](Lectures/Technical/Tooling/Libraries.md) | npm, hands-on: scripts in `package.json`, installing and removing a package, `npm outdated`, `package.json` against `package-lock.json`, judging a package before you install it (emoji-picker-react as the example), and MUI. |
| **10** · Nov 5 | No new notes: the session was questions and feedback for each group. | — |
| **11** · Nov 12 | [Efficient Communication](Lectures/Technical/Backend/Efficient-Communication-with-the-Backend.md) (live queries included) · [Running Code Server-Side](Lectures/Technical/Backend/Running-Code-Server-Side.md) · [Field-Level Permissions](Lectures/Technical/Backend/Field-Level-Permissions.md) (the exercise: totalTime / currentSessionStart / TodoTimeTracking) | — |
| **12** · Nov 19 | [Patterns of Component Communication](Lectures/Technical/React/Patterns-of-Component-Communication.md) · [Extracting Components, and Where the State Goes](Lectures/Technical/Structure/Refactoring-by-Extracting-Components.md) · [Updater Functions for State](Lectures/Technical/React/Updater-Functions-for-State.md) · [The useRef Hook](Lectures/Technical/React/The-useRef-Hook.md) | — |
| **13** · Nov 26 | [Component-Extraction Guide](Lectures/Technical/Structure/Component-Extraction-Guide.md) | — |
| **14** · Dec 3 | [Report Structure](Report-Structure.md) · [Exam Structure](Exam-Structure.md) · every note ends with its own Exam Questions | — |

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
