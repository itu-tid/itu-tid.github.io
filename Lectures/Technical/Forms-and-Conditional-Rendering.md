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
2. You press a key. It calls `onChange`.
3. `setText` updates the state, React re-renders, and the input shows the new `text`.

Every keystroke goes out to state and comes back. Delete the `onChange` and try typing: nothing happens, because you have told the input to display `text` and given it no way to change it.

What you get for it is **one source of truth**. The input cannot disagree with the app, because there is only one copy of the answer. 

And because state is just a variable, you can now do things the browser could never do for you:

```jsx
<button disabled={text.length === 0}>Add</button>
```

The button's enabled-ness is *derived* from the text, not stored separately. Nothing has to remember to switch it on and off — it is recomputed on every render. Reach for that whenever you catch yourself about to add a second piece of state that is really about the first.

### The pattern has a name: **controlled**

An input whose value comes from state is called **controlled**. The opposite is **uncontrolled**: leave off `value`, and the input keeps its own text — you have to go and ask it what it holds when you want to know.

That is the whole of the terminology, and it is worth knowing mainly because it turns up in error messages and in every answer you will find online.

### Making it your own component

`value` and `onChange` are ordinary props, so nothing stops you putting that input inside a component of your own:

```jsx
function TextInput({ value, onChange, placeholder }) {
  return (
    <input
      className="text-input"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
    />
  );
}
```

The state stays where it was — `TextInput` has none of its own:

```jsx
function AddTodo() {
  const [text, setText] = useState("");

  return (
    <TextInput
      value={text}
      onChange={setText}
      placeholder="What needs doing?"
    />
  );
}
```

That is the part worth pausing on. `useState` did not move into `TextInput`. If it had, `AddTodo` would have no idea what was typed, and could never clear the field or add the task. `TextInput` displays what it is given and reports what happened; it remembers nothing between renders.

Two things improved, and neither is about saving typing.

**The caller stopped touching `e.target.value`.** `TextInput` unwraps the event and hands up a plain string, so `AddTodo` can pass `setText` directly. The parent now works in the language of the app — a piece of text — instead of the language of the DOM.

**There is one place to change how inputs look.** The `className`, and anything you add later, lives here rather than in every screen that happens to need typing.

And look at the shape of it: `TextInput` takes the value it should show, and a way to report that something changed. Exactly what the raw `<input>` takes. The pattern travelled up a level without changing — which is why React reuses the word, and calls *any* component whose important state is held by its parent a controlled one.

## Wrapping it in a form

The button works. Now press **Enter** in the input.

Nothing happens — and everybody expects Enter to work. 

That is what a `<form>` is for, and it is the reason forms are still worth using in React rather than a naked input and a click handler:

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
      <TextInput value={text} onChange={setText} placeholder="What needs doing?" />
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

There are three ways to write one, and to see what actually differs between them it is worth writing the *same* thing three times. Here is a to-do row that should look different once it is done.

**1. An `if`, before the `return`** — when the two versions are different enough to be worth reading separately:

```jsx
function TodoItem({ text, done }) {
  if (done) {
    return <li className="done"><s>{text}</s></li>;
  }
  return <li>{text}</li>;
}
```

**2. The `? :` operator**, inside the JSX — when only a small part changes, and repeating the whole `<li>` would hide how little that is:

```jsx
function TodoItem({ text, done }) {
  return <li className={done ? "done" : ""}>{done ? <s>{text}</s> : text}</li>;
}
```

**3. `&&`** — when there is genuinely nothing to show in the other case, so a `? :` would end in an awkward `: null`:

```jsx
function TodoItem({ text, done }) {
  return (
    <li>
      {text} {done && <span aria-label="done">✓</span>}
    </li>
  );
}
```

They are not three styles of the same thing. `if` and `? :` both answer *which of these two*, and `&&` answers *is there anything here at all* — which is why the empty-list message above is written with `&&` and could not sensibly be written any other way.

A warning about that last one. `&&` returns its **left** side when the left side is falsy — so `{todos.length && <p>…</p>}` renders a literal **0** on the page when the list is empty, because `0` is falsy but is still something React will happily display. Compare explicitly (`=== 0`, `> 0`) and the problem disappears.

Note:
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation.

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*


# References

- *Describing the UI* > [Conditional Rendering](https://react.dev/learn/conditional-rendering)
- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)


## Exam Questions

### 1. What does it mean for an input to be *controlled*, and what is the alternative?

### 2. Why does a form need `e.preventDefault()` in a single-page application?

### 3. The input shows nothing when you type. Give two different reasons this can happen.
