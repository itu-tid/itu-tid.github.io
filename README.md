Notes for **Technical Interaction Design** at the IT University of Copenhagen.

## Autumn 2026

- **[Syllabus](syllabus.html)** — week by week: who teaches what, which notes back each lecture, and what is due when.
- **[Working as a Team](Project-Collaboration.md)** — how the four of you divide the project
- **[Report Structure](Report-Structure.md)** — what goes in the final report
- **[Exam Structure](Exam-Structure.md)** — how the oral runs, and what you get asked
- **[Coding Guidelines](Coding-Guidelines.md)**

## How the course runs

**Mircea** teaches the technical track; **Konstantina** teaches the design track — weeks 3, 7, 8, 9 and 12. **Lea** runs the Figma clinic in week 7, **Anna** the Back4App walkthrough in week 4; both are in the exercise hours every week.

Each Thursday: a lecture, then two hours of exercise — **one hour on your own**, one hour **with your group**. The solo hour is required but ungraded, and it piles up into a personal portfolio that is your exam preparation. Weeks 1 and 2 are entirely individual, because the teams do not exist yet.

**70% individual exam, 30% group project**, with a hard floor: bomb the individual and you fail, however strong the group. The project is your exam curriculum — if you used it, you understand it.

The last two minutes of every lecture are yours: **[one anonymous question](https://forms.gle/pse8zJNMQthy4UcFA)**, the same link every week. It gets read before the next lecture and answered at the start of it — which is the only reason it is worth your two minutes.

## Deadlines

Every one is a **Tuesday at 23:59**. Checkpoints you hit and dogfood against, not submissions marked line by line.

| due | what |
|---|---|
| **Tue 8 Sep** | Teams registered — a group of four, on learnIT. Weeks 1 and 2 are individual. |
| **Tue 22 Sep** | Themes → tasks — your population, three to five themes with quotes, each mapped to a [task](Lectures/Interaction-Design/Tasks.md), prioritised |
| **Tue 20 Oct** | Wireframes, tested — the screens your population needs, what testing changed, and the extended ER diagram |
| **Tue 10 Nov** | Visual & accessibility pass — the a11y audit, and what the visual pass changed |
| **Tue 24 Nov** | Chosen features working — your feature-menu picks, live in the app |
| **December** | Final app + thin report — deployed, dogfooded, defensible. Date set by the exam schedule. |

Each design deliverable lands about two weeks after the lecture that teaches it, and the feedback opens a later lecture — so there is time to act on it before the next one depends on it.

## Lecture notes

Two folders, split by who owns the material: [`Lectures/Technical/`](Lectures/Technical) and [`Lectures/Interaction-Design/`](Lectures/Interaction-Design). Inside each, the notes are flat. Which note belongs to which week is decided by the syllabus and nothing else — filenames deliberately do not encode it, because the ordering changes every year and a folder name has no way of telling you it has gone stale. Track does not change, which is why it is the one thing the folders *do* encode. Each note ends with its own **Exam Questions**, so a question can never drift from the material it tests.

Course order, as the 2026 syllabus runs it:

| week                 | notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 · React I          | [React Starter Kit](Lectures/Technical/React/React-Starter-Kit.md) · [Intro to React](Lectures/Technical/React/Intro-to-React.md) · [Hooks](Lectures/Technical/React/Hooks.md)                                                                                                                                                                                                                                                                                                                   |
| 2 · React II         | [Forms & Controlled Components](Lectures/Technical/React/Forms-and-Controlled-Components.md) · [Conditional Rendering](Lectures/Technical/React/Conditional-Rendering.md) · [The useEffect Hook](Lectures/Technical/React/The-useEffect-Hook.md) · [Debugging](Lectures/Technical/React/Debugging.md) · then, stepping back: [Finding the Components](Lectures/Technical/Structure/Finding-the-Components.md) · [Patterns of Component Communication](Lectures/Technical/React/Patterns-of-Component-Communication.md) |
| 3 · Design I         | [The Interaction Design Process](Lectures/Interaction-Design/The-Interaction-Design-Process.md) · [Tasks](Lectures/Interaction-Design/Tasks.md) · [Styling React Components](Lectures/Technical/React/Styling-React-Components.md)                                                                                                                                                                                                                                                   |
| 4 · Backend I        | [Backends and the Parse Platform](Lectures/Technical/Backend/Backends-and-the-Parse-Platform.md) · [Parse Configuration for Vite](Lectures/Technical/Backend/Parse-Configuration-for-Vite.md)                                                                                                                                                                                                                                                                                                  |
| 5 · Backend II       | [Authorization and ACL in Parse](Lectures/Technical/Backend/Authorization-and-ACL-in-Parse.md)                                                                                                                                                                                                                                                                                                                                                                                         |
| 6 · Routing & deploy | [Web App Architectures](Lectures/Technical/Routing/Web-App-Architectures.md) · [Routing in React](Lectures/Technical/Routing/Routing-in-React.md) · [Protecting Routes](Lectures/Technical/Routing/Protecting-Routes.md)                                                                                                                                                                                                                                                                               |
| 7 · Design II        | [Usability and Its Evaluation](Lectures/Interaction-Design/Usability-and-Its-Evaluation.md) · [usability examples](Lectures/Interaction-Design/usability-examples)                                                                                                                                                                                                                                                                                                             |
| 8 · Collaboration    | [Collaboration with Git-Flow](Lectures/Technical/Tooling/Collaboration-with-Git-Flow.md) · [Code Organization](Lectures/Technical/Structure/Code-Organization.md) · [Component-Extraction Cheatsheet](Lectures/Technical/Structure/Component-Extraction-Cheatsheet.md)                                                                                                                                                                                                                                     |
| 9 · Design III       | [Libraries](Lectures/Technical/Tooling/Libraries.md)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 10 · Organisation    | [Refactoring by Extracting Components](Lectures/Technical/Structure/Refactoring-by-Extracting-Components.md) · [The useRef Hook](Lectures/Technical/React/The-useRef-Hook.md)                                                                                                                                                                                                                                                                                                                  |
| 11 · Backend III     | [Updater Functions for State](Lectures/Technical/React/Updater-Functions-for-State.md) · [Efficient Communication with the Backend](Lectures/Technical/Backend/Efficient-Communication-with-the-Backend.md) · [Running Code Server-Side](Lectures/Technical/Backend/Running-Code-Server-Side.md) · [useEffect Against a Live Backend](Lectures/Technical/Backend/useEffect-Against-a-Live-Backend.md)                                                                                                        |
| 13 · Code quality    | [Component-Extraction Guide](Lectures/Technical/Structure/Component-Extraction-Guide.md) · [Debugging](Lectures/Technical/React/Debugging.md)                                                                                                                                                                                                                                                                                                                                                  |

## TopUps

Short self-study modules in [`TopUps/`](TopUps), covering the background a lecture assumes but does not teach. Only the first is due before the course starts; the rest arrive on the card of the week that needs them, so read each one *before* the week beside it.

| read before | module |
|---|---|
| week 1 | [3 · JavaScript, the Language](TopUps/3-Javascript-the-Language.md) |
| week 2 | [1 · Basics of CSS](TopUps/1-Basics-of-CSS.md) |
| week 4 | [6 · Async Programming & Promises](TopUps/6-Async-Programming-and-Promises.md) |
| week 8 | [5 · Coding Practices](TopUps/5-Coding-Practices.md) |
| week 9 | [4 · Layouts and Responsiveness](TopUps/4-Layouts-and-Responsiveness.md) |
| week 13, optional | [2 · DOM Manipulation with JavaScript](TopUps/2-DOM-Manipulation-with-Javascript.md) |

## Chapters as PDF

Each week's notes bundled into one PDF, for reading offline or printing: **<https://itu-tid.github.io/lecture-notes-pdf/>**

They are generated from the notes in this repository, so if the two ever disagree, the markdown here is the newer one.

## The app we build

[itu-tid/todo-26](https://github.com/itu-tid/todo-26) — the reference to-do, tagged once per lecture (`git checkout week-01`). Teams fork it in week 3.

---

Maintaining the course? [DEVELOPER.md](DEVELOPER.md) — how the syllabus is built, and what lives in the vault instead of here.
