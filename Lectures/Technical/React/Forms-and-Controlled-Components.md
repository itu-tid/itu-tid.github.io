# Forms and Controlled Components

Until now the app could only add random tasks from a list. Supporting the user to type the task means we have to link React state with HTML input element state. We'll see how to do it below.

## Controlled components

### An `<input>` normally keeps its own text. 

You type, the browser remembers, and React knows nothing about it.

### Reading the value of the `input` from state, and intercepting keypresses

We take the job of tracking the state of the input from the browser and give it to React. Two attributes do it -- `value` and `onChange`:

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

- React calls your `onChange` with an [event object](Intro-to-React.md#handlers-receive-an-event-object), named `e` by convention.
- `e.target` is the element that fired it: this input.
- `e.target.value` is the text now in it, *including* the key just pressed.

Read the loop, because it is genuinely circular and that is what makes it feel strange at first:

1. The input shows whatever `text` says.
2. You press a key. The input calls `onChange`, handing it the event.
3. `setText` updates the state, React re-renders, and the input shows the new `text`.
4. Re-rendering does **not** fire `onChange` again. The loop turns once per keystroke, then stops.

What you get for it is **one source of truth**. The input cannot disagree with the app, because there is only one copy of the answer. 

### Essential Rule: A value you can work out from state should not be state itself

Because `text` is an ordinary value you can read anywhere in the JSX, you can now do things the browser could never do for you:

```jsx
<button disabled={text.length === 0}>Add</button>
```

The button's enabled-ness is *derived* from the text, not stored separately in an `isEnabled` state variable, for example: 

```jsx
const [text, setText] = useState("");
const [isDisabled, setIsDisabled] = useState(true);

// later
setIsEnabled(...)
// ... 
```

Now two things have to be kept in step by hand, and one day they will not be. Reach for the derived version whenever you catch yourself about to add a second piece of state that is really about the first.

### The pattern has a name: controlled

An input whose value comes from state is called **controlled**. The opposite is **uncontrolled**: do not set `value`, and the input keeps its own text.

That is the whole of the terminology, and it is worth knowing mainly because it turns up in every answer you will find online — and in the warning React prints when a `value` arrives late: 

> *"A component is changing an uncontrolled input to be controlled."* 

That means `value` was `undefined` on the first render, usually because the state started as `undefined` rather than `""`.

## Enter does nothing until the input is inside a form

Give that button an `onClick` and it adds a to-do. Now press **Enter** in the input instead.

Nothing happens — and everybody expects Enter to work. 

That is what a `<form>` is for, and it is the reason forms are still worth using in React rather than a naked input and a click handler.

One new thing in the code below: `onAdd`. The form does not own the list of to-dos so it cannot add anything itself. `TodoList` does own the list, and what it does is that it hands down a function to be used by the child component to update the parent that a new element has to be added. That arrangement has a name and a note of its own: [Patterns of Component Communication](Patterns-of-Component-Communication.md).

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

### Convention is that when a function is to be called when a given event happens, the name starts with `on...`

`onChange` and `onSubmit` are React's, spelled exactly so

`onAdd` is a name the parent invents, and it could as well have been `whenSomebodyAdds`. The `on…` spelling is a convention that says *this prop is a function you call when something happens* — nothing more.

### One handler catches both the click and the Enter key

`onSubmit` fires for the button click *and* for Enter, so you write the handler once. 
You also get the semantics for free: a screen reader announces a form, and a phone keyboard offers a **Go** key instead of a plain Return.

### `preventDefault` is what stops the whole page reloading

A form's default behaviour is to send its contents to the server and load whatever comes back — the way the web worked before JavaScript. That would throw away your entire app and reload the page. 

We are a single-page application: nothing should ever be sent anywhere or reloaded unless we say so. Take the line out and watch it happen once; the flash of the page reloading is worth seeing.

### Every button in a form submits it unless you say otherwise

The Add button above needs no `type`, because every `<button>` already has the type `submit` by default. There are three button types in total: 

| `type`   | what it does                                           |
| -------- | ------------------------------------------------------ |
| `submit` | submits the form — **this is the default**             |
| `button` | nothing on its own; it only runs your `onClick`        |
| `reset`  | empties every field in the form (you rarely want this) |

So the Add button is a submit button without saying so, and that is what makes the click and the Enter key arrive at the same handler.

### If a button is not meant to submit the form then explicitly make it type `button` - otherwise bugs

The default bites the first time you put a *second* button in a form. A **Clear** or **Cancel** beside Add will submit the form too, and you will spend a while wondering why cancelling adds a to-do. The confusing part is that Clear still *appears* to work: submitting empties the box as well, so the field clears exactly as you intended. Only the list gives it away. Written out, the pair reads clearly:

```jsx
<button type="submit">Add</button>
<button type="button" onClick={() => setText("")}>Clear</button>
```

`type="button"` looks like it says nothing until you know the alternative it is refusing. It means *this is only a button* — do not submit anything.

### A controlled input is one you can clear

`setText("")` empties the field, which is only possible *because* the input is controlled. An uncontrolled input holds its own text and you would have to reach into the browser DOM to empty it.

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
