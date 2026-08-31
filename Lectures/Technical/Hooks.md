# React Hooks

You have just used one. `useState` is a hook, and it is worth stopping for a moment on what that word means, because every other one you meet this term follows the same rules.

## A hook is how a component reaches things React is holding for it

Your component is a plain function. React calls it to get JSX, and then throws away every local variable inside it — that is why a normal `let count = 0` cannot survive a click.

But React itself remembers. It keeps a little store beside each component on screen, and a **hook** is how your function reaches into that store. `useState` asks for a slot that persists between calls; the setter tells React the slot changed, so the component should be called again.

That is the whole idea. Everything else is bookkeeping.

## They all start with `use`

Not decoration — it is how React's linter recognises them and checks the rules below. The three you will meet in this course:

| hook | what it gets you | you reach for it |
|---|---|---|
| `useState` | a value that survives re-renders, and re-renders when it changes | today |
| [`useEffect`](The-useEffect-Hook.md) | a way to reach *outside* React — storage, a backend, a timer | when the app has to stay in step with something React does not control |
| [`useRef`](The-useRef-Hook.md) | a value that survives re-renders but does **not** cause one | when you start extracting components |

The contrast in that last row is the useful one. State and refs both survive; only state redraws. You want a ref for something the screen does not depend on — the DOM node you need to focus, a timer's id, a counter nobody displays.

## The rules: top level, always, unconditionally

- Call hooks at the **top level of a component**, not inside `if`, not inside a loop, not inside a nested function.
- They can also be called from another hook, which is how custom hooks work.

React will refuse to compile code that breaks this, and the reason is worth knowing, because it turns an arbitrary-looking rule into an obvious one.

**React matches hooks to their stored values by call order, not by name.** It does not know your variable is called `count`; it knows this component called a state hook first, and a second one after that. So:

```jsx
function Broken({ showTitle }) {
  if (showTitle) {
    const [title, setTitle] = useState("My list");   // ← sometimes first, sometimes absent
  }
  const [items, setItems] = useState([]);            // ← so this is sometimes #1, sometimes #2
}
```

The first time `showTitle` is true, `items` is the second slot. When it turns false, the same line asks for the *first* slot — and gets handed the title. Everything after it shifts too. Keeping every hook at the top level, called every time, is what guarantees the order never changes.

## Exam Questions

### 1. What are the rules for using React hooks?

### 2. Why does that rule exist — what would go wrong if you called a hook inside an `if`?

### 3. Both state and refs survive a re-render. What is the difference between them, and when would you reach for a ref?
