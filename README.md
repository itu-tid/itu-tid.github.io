Lecture notes for the ***Technical*** part of the Technical Interaction Design course at the ITU by Mircea. 

## Autumn 2026
- **[Syllabus](syllabus.html)** — week by week: who teaches what, the five deliverable checkpoints, and which notes back each lecture.

`syllabus.html` is generated. Its markdown source is **not in this repo** — it lives at
`$TID_VAULT/2026-syllabus.md` in the Obsidian vault, because it carries `%%staff asides%%`
and `New:` / `Status:` rows that are notes between the people teaching the course. Keeping
the source here and stripping it on the way out would have been theatre: the markdown is
the original, the page only a copy.

    export TID_VAULT="…/Megavault/teaching/technical interaction design/"
    python3 build.py

writes `syllabus.html` here and a staff copy of the same page, with everything left in,
back into the vault. Edit the markdown in the vault, `syllabus.template.html` for design,
and never either generated page by hand.

## Coding Pre-requisites
- [1-Basics-of-CSS](Tech-TopUps/1-Basics-of-CSS.md)
- [2-DOM-Manipulation-with-Javascript](Tech-TopUps/2-DOM-Manipulation-with-Javascript.md)
- [3-Javascript-the-Language](Tech-TopUps/3-Javascript-the-Language.md)
- [4-Layouts-and-Responsiveness](Tech-TopUps/4-Layouts-and-Responsiveness.md)


## Technical ID

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
| 2 · React II | [Forms & Conditional Rendering](Lectures/Technical/Forms-and-Conditional-Rendering.md) · [Updater Functions for State](Lectures/Technical/Updater-Functions-for-State.md) · [Updating Objects and Lists in State](Lectures/Technical/Updating-Objects-and-Lists-in-State.md) · [Patterns of Component Communication](Lectures/Technical/Patterns-of-Component-Communication.md) · [The useEffect Hook](Lectures/Technical/The-useEffect-Hook.md) |
| 3 · Design I | [The Interaction Design Process](Lectures/Interaction-Design/The-Interaction-Design-Process.md) · [Styling React Components](Lectures/Technical/Styling-React-Components.md) |
| 4 · Backend I | [Backends and the Parse Platform](Lectures/Technical/Backends-and-the-Parse-Platform.md) · [Parse Configuration for Vite](Lectures/Technical/Parse-Configuration-for-Vite.md) |
| 5 · Backend II | [Authorization and ACL in Parse](Lectures/Technical/Authorization-and-ACL-in-Parse.md) |
| 7 · Design II | [Usability and Its Evaluation](Lectures/Interaction-Design/Usability-and-Its-Evaluation.md) · [usability examples](Lectures/Interaction-Design/usability-examples) |
| 6 · Routing & deploy | [Web App Architectures](Lectures/Technical/Web-App-Architectures.md) · [Routing in React](Lectures/Technical/Routing-in-React.md) |
| 8 · Collaboration | [Collaboration with Git-Flow](Lectures/Technical/Collaboration-with-Git-Flow.md) · [Code Organization](Lectures/Technical/Code-Organization.md) · [Code-Quality set](Lectures/Technical/Code-Quality) |
| 9 · Design III | [Libraries](Lectures/Technical/Libraries.md) |
| 10 · Organisation | [Refactoring by Extracting Components](Lectures/Technical/Refactoring-by-Extracting-Components.md) · [The useRef Hook](Lectures/Technical/The-useRef-Hook.md) |
| 11 · Backend III | [Efficient Communication with the Backend](Lectures/Technical/Efficient-Communication-with-the-Backend.md) · [Running Code Server-Side](Lectures/Technical/Running-Code-Server-Side.md) · [useEffect Against a Live Backend](Lectures/Technical/useEffect-Against-a-Live-Backend.md) |
| 13 · Code quality | [Code-Quality set](Lectures/Technical/Code-Quality) · [Debugging](Lectures/Technical/Debugging.md) |

## Course documents

- [Working as a Team](Project-Collaboration.md) — how the four of you divide the project
- [Report Structure](Report-Structure.md) — what goes in the final report, section by section
- [Exam Structure](Exam-Structure.md) — how the oral runs, and the kinds of question asked
- [Coding Guidelines](Coding-Guidelines.md)

## The app we build

[itu-tid/todo-26](https://github.com/itu-tid/todo-26) — the reference to-do, tagged once
per lecture (`git checkout week-01`). Teams fork it in week 3.
