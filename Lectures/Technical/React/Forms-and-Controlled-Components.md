# Forms and Conditional Rendering

Until now the app could only add whatever it felt like — the button reached into a list of sample tasks and picked one at random. Typing the task yourself means React has to own the input, and the screen has to change shape depending on what is in it.

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
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <button disabled={text.length === 0}>Add</button>
    </form>
  );
}
```

Three things are happening there.

**`onSubmit` fires for both** the button click and the Enter key, so you write the handler once. You also get the semantics for free: a screen reader announces a form, and a phone keyboard offers a **Go** key instead of a newline.

**`e.preventDefault()` is not boilerplate.** A form's default behaviour is to send its contents to the server and load whatever comes back — the way the web worked before JavaScript. That would throw away your entire app and reload the page. We are a single-page application: nothing should ever be sent anywhere or reloaded unless we say so. Take the line out and watch it happen once; the flash of the page reloading is worth seeing.

Later, when the same `<input>` turns up in more than one place, it is worth pulling into a component of your own — see [Finding the Components](../Structure/Finding-the-Components.md).

**`setText("")` clears the field**, which is only possible *because* the input is controlled. An uncontrolled input holds its own text and you would have to reach into the DOM to empty it.


# References

- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)
- *Adding Interactivity* > [Responding to Events](https://react.dev/learn/responding-to-events)


## Exam Questions

### 1. What does it mean for an input to be *controlled*, and what is the alternative?

### 2. Why does a form need `e.preventDefault()` in a single-page application?

### 3. The input shows nothing when you type. Give two different reasons this can happen.

### 4. Why can a controlled input be cleared after submitting, when an uncontrolled one cannot?
