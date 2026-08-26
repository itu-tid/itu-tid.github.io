Lecture notes for the ***Technical*** part of the Technical Interaction Design course at the ITU by Mircea. 

## Autumn 2026
- **[Syllabus](syllabus.md)** — week by week: who teaches what, the five deliverable checkpoints, and which notes back each lecture. Styled version: [syllabus.html](syllabus.html).

`syllabus.md` is the source; run `python3 build.py` to regenerate the styled pages from it.
It writes two, from the one source: `syllabus.html` — the students' page, and what GitHub
Pages serves — and `syllabus-internal.html`, the same thing with the teaching team's asides
and the `New:` to-write rows left in. Anything wrapped in `%%…%%` in the markdown, and any
`New:` or `Status:` row, is ours and stays off the student page.
Pushing a change to `syllabus.md` on `main` rebuilds both automatically ([workflow](.github/workflows/build-syllabus.yml)), so neither drifts from the markdown.

## Coding Pre-requisites
- [1-Basics-of-CSS](Tech-TopUps/1-Basics-of-CSS.md)
- [2-DOM-Manipulation-with-Javascript](Tech-TopUps/2-DOM-Manipulation-with-Javascript.md)
- [3-Javascript-the-Language](Tech-TopUps/3-Javascript-the-Language.md)
- [4-Layouts-and-Responsiveness](Tech-TopUps/4-Layouts-and-Responsiveness.md)


## Technical ID

The notes live flat in [`Lectures/Technical ID/`](Lectures/Technical%20ID). Which note
belongs to which week is decided by the [syllabus](syllabus.md) and nothing else — the
filenames deliberately do not encode it, because the ordering changes every year and a
folder name has no way of telling you it has gone stale. Each note ends with its own
**Exam Questions**, so a question can never drift away from the material it tests.

Course order, as the 2026 syllabus runs it:

| week | notes |
|---|---|
| 1 · React I | [React Starter Kit](Lectures/Technical%20ID/React-Starter-Kit.md) · [Intro to React](Lectures/Technical%20ID/Intro-to-React.md) · [Hooks](Lectures/Technical%20ID/Hooks.md) |
| 2 · React II | [Forms & Conditional Rendering](Lectures/Technical%20ID/Forms-and-Conditional-Rendering.md) · [Updater Functions for State](Lectures/Technical%20ID/Updater-Functions-for-State.md) · [Updating Objects and Lists in State](Lectures/Technical%20ID/Updating-Objects-and-Lists-in-State.md) · [Patterns of Component Communication](Lectures/Technical%20ID/Patterns-of-Component-Communication.md) · [The useEffect Hook](Lectures/Technical%20ID/The-useEffect-Hook.md) |
| 3 · Design I | [Styling React Components](Lectures/Technical%20ID/Styling-React-Components.md) |
| 4 · Backend I | [Backends and the Parse Platform](Lectures/Technical%20ID/Backends-and-the-Parse-Platform.md) · [Parse Configuration for Vite](Lectures/Technical%20ID/Parse-Configuration-for-Vite.md) |
| 5 · Backend II | [Authorization and ACL in Parse](Lectures/Technical%20ID/Authorization-and-ACL-in-Parse.md) |
| 6 · Routing & deploy | [Web App Architectures](Lectures/Technical%20ID/Web-App-Architectures.md) · [Routing in React](Lectures/Technical%20ID/Routing-in-React.md) |
| 8 · Collaboration | [Collaboration with Git-Flow](Lectures/Technical%20ID/Collaboration-with-Git-Flow.md) · [Code Organization](Lectures/Technical%20ID/Code-Organization.md) · [Code-Quality set](Lectures/Technical%20ID/Code-Quality) |
| 9 · Design III | [Libraries](Lectures/Technical%20ID/Libraries.md) |
| 10 · Organisation | [Refactoring by Extracting Components](Lectures/Technical%20ID/Refactoring-by-Extracting-Components.md) · [The useRef Hook](Lectures/Technical%20ID/The-useRef-Hook.md) |
| 11 · Backend III | [Efficient Communication with the Backend](Lectures/Technical%20ID/Efficient-Communication-with-the-Backend.md) · [Running Code Server-Side](Lectures/Technical%20ID/Running-Code-Server-Side.md) · [useEffect Against a Live Backend](Lectures/Technical%20ID/useEffect-Against-a-Live-Backend.md) |
| 13 · Code quality | [Code-Quality set](Lectures/Technical%20ID/Code-Quality) · [Debugging](Lectures/Technical%20ID/Debugging.md) |

## The app we build

[itu-tid/todo-26](https://github.com/itu-tid/todo-26) — the reference to-do, tagged once
per lecture (`git checkout week-01`). Teams fork it in week 3.
