# Forms and Conditional Rendering

Last week the app could only add whatever it felt like — the button reached into a list of sample tasks and picked one at random. This week you type the task yourself, which means React has to own the input, and the screen has to change shape depending on what is in it.

Two topics in one note, because they arrive together: the moment you can add items you can also remove them, and the moment the list can be empty the screen needs to say something other than nothing.

## Connecting Inputs To State Via Event Handlers

An `<input>` normally keeps its own text. You type, the browser remembers, and React knows nothing about it — which is fine until the app needs to *use* what was typed.

So we take that job away from the input and give it to state. Two attributes, and nothing else:

```jsx
import { useState } from "react";

function AddTodo() {
  const [text, setText] = useState("");

  return (
    <input
      value={text}
      onChange={(e) => setText(e.target.value)}
    />
  );
}
```

Read the loop, because it is genuinely circular and that is what makes it feel strange at first:

1. The input shows whatever `text` says.
2. You press a key. The input does **not** change itself — it calls `onChange`.
3. `setText` updates the state, React re-renders, and the input shows the new `text`.

Every keystroke goes out to state and comes back. Delete the `onChange` and try typing: nothing happens, because you have told the input to display `text` and given it no way to change it.

### This is called a `controlled component`

The form element is controlled by React state rather than by itself. (Should probably be *controlling component*, since the state is doing the controlling, but the name is what it is.)

What you get for it is **one source of truth**. The input cannot disagree with the app, because there is only one copy of the answer. And because state is just a variable, you can now do things the browser could never do for you:

```jsx
<button disabled={text.length === 0}>Add</button>
```

The button's enabled-ness is *derived* from the text, not stored separately. Nothing has to remember to switch it on and off — it is recomputed on every render. Reach for that whenever you catch yourself about to add a second piece of state that is really about the first.

## Wrapping it in a form

The button works. Now press **Enter** in the input.

Nothing happens — and everybody expects Enter to work. That is what a `<form>` is for, and it is the reason forms are still worth using in React rather than a naked input and a click handler:

```jsx
function AddTodo({ onAdd }) {
  const [text, setText] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    onAdd(text);
    setText("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <button disabled={text.length === 0}>Add</button>
    </form>
  );
}
```

Three things there are worth naming.

**`onSubmit` fires for both** the button click and the Enter key, so you write the handler once. You also get the semantics for free: a screen reader announces a form, and a phone keyboard offers a **Go** key instead of a newline.

**`e.preventDefault()` is not boilerplate.** A form's default behaviour is to send its contents to the server and load whatever comes back — the way the web worked before JavaScript. That would throw away your entire app and reload the page. We are a single-page application: nothing should ever be sent anywhere or reloaded unless we say so. Take the line out and watch it happen once; the flash of the page reloading is worth seeing.

**`setText("")` clears the field**, which is only possible *because* the input is controlled. An uncontrolled input holds its own text and you would have to reach into the DOM to empty it.

## Conditional Rendering 

Often components need to display differently based on some state or prop.

The moment a list can be added to and deleted from, it can also be **empty** — and an empty `<ul>` on screen looks like a bug rather than an achievement. That is the first place you need this:

```jsx
{todos.length === 0 && <p>Nothing to do. Enjoy the afternoon.</p>}
```

Three possible ways to render conditionally:

**1. An `if`, before the `return`** — best when whole branches differ:

```jsx
function TodoItem({ text, done }) {
  if (done) {
    return <li className="done"><s>{text}</s></li>;
  }
  return <li>{text}</li>;
}
```

**2. The `? :` operator**, inside the JSX — best when only a small part changes:

```jsx
<li>{done ? <s>{text}</s> : text}</li>
```

**3. `&&`**, when there is nothing to show in the other case:

```jsx
{todos.length === 0 && <p>Nothing to do. Enjoy the afternoon.</p>}
```

A warning about that last one. `&&` returns its **left** side when the left side is falsy — so `{todos.length && <p>…</p>}` renders a literal **0** on the page when the list is empty, because `0` is falsy but is still something React will happily display. Compare explicitly (`=== 0`, `> 0`) and the problem disappears.

Note:
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation.

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*


# References

- *Describing the UI* > [Conditional Rendering](https://react.dev/learn/conditional-rendering)
- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)


## Exam Questions

### 1. What is a controlled component in React?

### 2. Why does a form need `e.preventDefault()` in a single-page application?

### 3. The input shows nothing when you type. Give two different reasons this can happen.
