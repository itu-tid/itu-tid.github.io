# Forms and Controlled Components

Until now the app could only add whatever it felt like — the button reached into a list of sample tasks and picked one at random. Typing the task yourself means React has to own the input, and the screen has to change shape depending on what is in it.

## Give the value to state, and every keystroke goes back through the setter

An `<input>` normally keeps its own text. You type, the browser remembers, and React knows nothing about it — which is fine until the app needs to *use* what was typed.

So we take that job away from the input and give it to state. Two attributes do it — `value` and `onChange`:

```jsx
import { useState } from "react";

function NewTodoForm() {
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

### A value you can work out from state should not be state itself

Because state is just a variable, you can now do things the browser could never do for you:

```jsx
<button disabled={text.length === 0}>Add</button>
```

The button's enabled-ness is *derived* from the text, not stored separately. Nothing has to remember to switch it on and off — it is recomputed on every render. Reach for that whenever you catch yourself about to add a second piece of state that is really about the first.

### The pattern has a name: **controlled**

An input whose value comes from state is called **controlled**. The opposite is **uncontrolled**: leave off `value`, and the input keeps its own text — you have to go and ask it what it holds when you want to know.

That is the whole of the terminology, and it is worth knowing mainly because it turns up in error messages and in every answer you will find online.

## Enter does nothing until the input is inside a form

The button works. Now press **Enter** in the input.

Nothing happens — and everybody expects Enter to work. 

That is what a `<form>` is for, and it is the reason forms are still worth using in React rather than a naked input and a click handler.

One new thing in the code below: `onAdd`. The form does not own the list of to-dos — `TodoList` does — so it cannot add anything itself. What it gets instead is a function to call, handed down by whoever does own the list. That arrangement has a name and a note of its own: [Patterns of Component Communication](Patterns-of-Component-Communication.md).

```jsx
function NewTodoForm({ onAdd }) {
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

### One handler catches both the click and the Enter key

`onSubmit` fires for the button click *and* for Enter, so you write the handler once. You also get the semantics for free: a screen reader announces a form, and a phone keyboard offers a **Go** key instead of a newline.

### `preventDefault` is what stops the whole page reloading

It is not boilerplate. A form's default behaviour is to send its contents to the server and load whatever comes back — the way the web worked before JavaScript. That would throw away your entire app and reload the page. We are a single-page application: nothing should ever be sent anywhere or reloaded unless we say so. Take the line out and watch it happen once; the flash of the page reloading is worth seeing.

### Every button in a form submits it unless you say otherwise

The Add button above needs no `type`, because every `<button>` already has one, and there are three:

| `type` | what it does |
|---|---|
| `submit` | submits the form — **this is the default** |
| `button` | nothing on its own; it only runs your `onClick` |
| `reset` | empties every field in the form (you rarely want this) |

So the Add button is a submit button without saying so, and that is what makes the click and the Enter key arrive at the same handler.

The default bites the first time you put a *second* button in a form. A **Clear** or **Cancel** beside Add will submit the form too, and you will spend a while wondering why cancelling adds a to-do. Written out, the pair reads clearly:

```jsx
<button type="submit">Add</button>
<button type="button" onClick={() => setText("")}>Clear</button>
```

`type="button"` looks like it says nothing until you know the alternative it is refusing. It means *this is only a button* — do not submit anything.

### A controlled input is one you can clear

`setText("")` empties the field, which is only possible *because* the input is controlled. An uncontrolled input holds its own text and you would have to reach into the DOM to empty it.

Later, when that `<input>` turns up in more than one place, it is worth pulling into a component of your own — see [Finding the Components](../Structure/Finding-the-Components.md).


## References

- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)
- *Adding Interactivity* > [Responding to Events](https://react.dev/learn/responding-to-events)


## Exam Questions

### 1. What does it mean for an input to be *controlled*, and what is the alternative?

### 2. Why does a form need `e.preventDefault()` in a single-page application?

### 3. The input shows nothing when you type. Give two different reasons this can happen.

### 4. Why can a controlled input be cleared after submitting, when an uncontrolled one cannot?

### 5. You add a **Clear** button next to **Add** and now clearing also adds a to-do. Why, and what is the fix?
