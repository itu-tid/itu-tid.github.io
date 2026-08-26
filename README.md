Notes for **Technical Interaction Design** at the IT University of Copenhagen.

## Autumn 2026

- **[Syllabus](syllabus.html)** — week by week: who teaches what, the six deliverable checkpoints, and which notes back each lecture.

## Lecture notes

Two folders, split by who owns the material: [`Lectures/Technical/`](Lectures/Technical)
and [`Lectures/Interaction-Design/`](Lectures/Interaction-Design). Inside each, the notes
are flat. Which note belongs to which week is decided by the syllabus and nothing else —
filenames deliberately do not encode it, because the ordering changes every year and a
folder name has no way of telling you it has gone stale. Track does not change, which is
why it is the one thing the folders *do* encode. Each note ends with its own **Exam
Questions**, so a question can never drift from the material it tests.

Course order, as the 2026 syllabus runs it:

| week | notes |
|---|---|
| 1 · React I | [React Starter Kit](Lectures/Technical/React-Starter-Kit.md) · [Intro to React](Lectures/Technical/Intro-to-React.md) · [Hooks](Lectures/Technical/Hooks.md) |
| 2 · React II | [Forms & Conditional Rendering](Lectures/Technical/Forms-and-Conditional-Rendering.md) · [Updater Functions for State](Lectures/Technical/Updater-Functions-for-State.md) · [Updating Objects and Lists in State](Lectures/Technical/Updating-Objects-and-Lists-in-State.md) · [Patterns of Component Communication](Lectures/Technical/Patterns-of-Component-Communication.md) · [The useEffect Hook](Lectures/Technical/The-useEffect-Hook.md) · [Debugging](Lectures/Technical/Debugging.md) |
| 3 · Design I | [The Interaction Design Process](Lectures/Interaction-Design/The-Interaction-Design-Process.md) · [Tasks](Lectures/Interaction-Design/Tasks.md) · [Styling React Components](Lectures/Technical/Styling-React-Components.md) |
| 4 · Backend I | [Backends and the Parse Platform](Lectures/Technical/Backends-and-the-Parse-Platform.md) · [Parse Configuration for Vite](Lectures/Technical/Parse-Configuration-for-Vite.md) |
| 5 · Backend II | [Authorization and ACL in Parse](Lectures/Technical/Authorization-and-ACL-in-Parse.md) |
| 6 · Routing & deploy | [Web App Architectures](Lectures/Technical/Web-App-Architectures.md) · [Routing in React](Lectures/Technical/Routing-in-React.md) · [Protecting Routes](Lectures/Technical/Protecting-Routes.md) |
| 7 · Design II | [Usability and Its Evaluation](Lectures/Interaction-Design/Usability-and-Its-Evaluation.md) · [usability examples](Lectures/Interaction-Design/usability-examples) |
| 8 · Collaboration | [Collaboration with Git-Flow](Lectures/Technical/Collaboration-with-Git-Flow.md) · [Code Organization](Lectures/Technical/Code-Organization.md) · [Component-Extraction Cheatsheet](Lectures/Technical/Component-Extraction-Cheatsheet.md) |
| 9 · Design III | [Libraries](Lectures/Technical/Libraries.md) |
| 10 · Organisation | [Refactoring by Extracting Components](Lectures/Technical/Refactoring-by-Extracting-Components.md) · [The useRef Hook](Lectures/Technical/The-useRef-Hook.md) |
| 11 · Backend III | [Efficient Communication with the Backend](Lectures/Technical/Efficient-Communication-with-the-Backend.md) · [Running Code Server-Side](Lectures/Technical/Running-Code-Server-Side.md) · [useEffect Against a Live Backend](Lectures/Technical/useEffect-Against-a-Live-Backend.md) |
| 13 · Code quality | [Component-Extraction Guide](Lectures/Technical/Component-Extraction-Guide.md) · [Debugging](Lectures/Technical/Debugging.md) |

## TopUps

Short self-study modules in [`TopUps/`](TopUps), covering the background a lecture assumes
but does not teach. Only the first is due before the course starts; the rest arrive on the
card of the week that needs them, so read each one *before* the week beside it.

| read before | module |
|---|---|
| week 1 | [3 · JavaScript, the Language](TopUps/3-Javascript-the-Language.md) |
| week 2 | [1 · Basics of CSS](TopUps/1-Basics-of-CSS.md) |
| week 4 | [6 · Async Programming & Promises](TopUps/6-Async-Programming-and-Promises.md) |
| week 8 | [5 · Coding Practices](TopUps/5-Coding-Practices.md) |
| week 9 | [4 · Layouts and Responsiveness](TopUps/4-Layouts-and-Responsiveness.md) |
| week 13, optional | [2 · DOM Manipulation with JavaScript](TopUps/2-DOM-Manipulation-with-Javascript.md) |

## Chapters as PDF

Each week's notes, bundled into one PDF for reading offline or printing, in the shared
folder linked from learnIT. They are generated from the notes in this repository, so if
the two ever disagree, the markdown here is the newer one.

## Course documents

- [Working as a Team](Project-Collaboration.md) — how the four of you divide the project
- [Report Structure](Report-Structure.md) — what goes in the final report, section by section
- [Exam Structure](Exam-Structure.md) — how the oral runs, and the kinds of question asked
- [Coding Guidelines](Coding-Guidelines.md)

## The app we build

[itu-tid/todo-26](https://github.com/itu-tid/todo-26) — the reference to-do, tagged once
per lecture (`git checkout week-01`). Teams fork it in week 3.

---

Maintaining the course? [DEVELOPER.md](DEVELOPER.md) — how the syllabus is built, and what
lives in the vault instead of here.
