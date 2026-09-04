# Forms and Controlled Components

Until now the app could only add random tasks from a list. Supporting the user to type the task means we have to link React state with HTML input element state. We'll see how to do it below.

## Controlled components

### An `<input>` normally keeps its own text. 

You type, the browser remembers, and React knows nothing about it.

### Bridging React with HTML by intercepting keypresses

(more precise is DOM, but we don't care)

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

The button's enabled-ness is *derived* from the text, not stored separately in a second state variable:

```jsx
const [text, setText] = useState("");
const [isDisabled, setIsDisabled] = useState(true);   // don't

function handleChange(e) {
  setText(e.target.value);
  setIsDisabled(e.target.value.length === 0);          // ...and never forget this
}
```

Now two things have to be kept in step by hand, and one day they will not be. Reach for the derived version whenever you catch yourself about to add a second piece of state that is really about the first.

### The pattern has a name: controlled

An input whose value comes from state is called **controlled**. An input left to keep its own text is **uncontrolled**.

You will not write an uncontrolled one in this course. You need the word anyway, because every answer online uses it, and because React puts it in the warning it prints when a `value` arrives late: 

> *"A component is changing an uncontrolled input to be controlled."* 

That means `value` was `undefined` on the first render, usually because the state started as `undefined` rather than `""`.

## Enter does nothing until the input is inside a form

Give that button an `onClick` and it adds a to-do. Now press **Enter** in the input instead.

Nothing happens — and everybody expects Enter to work. 

That is what a `<form>` is for, and it is the reason forms are still worth using in React rather than a naked input and a click handler.

One new thing in the code below: `onAdd`. The form does not own the list of to-dos so it cannot add anything itself. `TodoList` owns it, so it hands the form a function to call when the user submits.

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

`setText("")` empties the field, and it is the controlled loop that makes that possible: the text lives in `text`, so clearing `text` clears the box. If the input were holding its own text, you would have to reach into the browser DOM to get at it.

Later, when that `<input>` turns up in more than one place, it is worth pulling into a component of your own — see [Finding the Components](../Structure/Finding-the-Components.md).


## The list is what owns the to-dos

`onAdd` has been arriving from somewhere all this time. Here is the somewhere.

The form calls `onAdd(text)` with a **string**, because typing a name is all a form knows how to do. Turning that string into a to-do is the list's job:

```jsx
function TodoList() {
  const [todos, setTodos] = useState([]);   // each one is { id, text, done }

  function handleAdd(text) {
    setTodos([...todos, { id: crypto.randomUUID(), text, done: false }]);
  }

  function handleRemove(id) {
    setTodos(todos.filter((t) => t.id !== id));
  }

  function handleToggle(id) {
    setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
  }

  return (
    <>
      <NewTodoForm onAdd={handleAdd} />
      <ul>
        {todos.map((todo) => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onRemove={handleRemove}
            onToggle={handleToggle}
          />
        ))}
      </ul>
    </>
  );
}
```

And the row it renders, which draws one to-do and reports what was done to it:

```jsx
function TodoItem({ todo, onToggle, onRemove }) {
  return (
    <li>
      <input
        type="checkbox"
        checked={todo.done}
        onChange={() => onToggle(todo.id)}
      />
      <span className={todo.done ? "done" : ""}>{todo.text}</span>
      <button onClick={() => onRemove(todo.id)}>×</button>
    </li>
  );
}
```

### Three names for one connection

This is the part that trips everyone, and it is worth slowing down on. Look at what `handleAdd` is called in each of the three places it appears:

| where | written as | what it is |
|---|---|---|
| in `TodoList` | `function handleAdd(text)` | the function that actually does the work |
| at the call site | `onAdd={handleAdd}` | handing that function to the form |
| inside `NewTodoForm` | `onAdd` | the name the form knows it by |

They look like three things. They are one function, named twice — once by the component that owns it, once by the component that will call it.

It is easier if you read it in the form's own voice:

> I am a form with an Add button. I know how to collect text and I know when the button was pressed. What I do **not** know is what adding means, because the list is not mine. So: you who want to use me have to hand me a function, and I will call it when Add is pressed. In my own code I will refer to it as `onAdd`, because that is all I know about it.

`TodoList` answers: *here is that function, it is called `handleAdd`, and what it does is put a new to-do on my list.*

That is why the two names differ, and the difference is a convention worth following: **`on…` is what the prop is called, `handle…` is what the function is called.** `onAdd` describes the *event* from the child's side; `handleAdd` describes the *work* from the parent's side. React's own props follow it — `onChange`, `onSubmit`, `onClick` — and yours should too, so that a reader can tell at a glance which side of the connection they are looking at.

### Why the arrow: `onClick={() => onRemove(todo.id)}`

Look at that line in `TodoItem` and it seems to have an arrow function for no reason. Try removing it and you will see why.

You already know that `onClick={handleRemove}` hands over the function while `onClick={handleRemove()}` calls it immediately, during render, and hands over whatever it returned. So far so good.

But here you need to call it **with a particular to-do's id**, and the moment you write the brackets to pass an argument, you have called it:

```jsx
<button onClick={onRemove(todo.id)}>      // calls it while rendering. Every row. Immediately.
```

The arrow is how you get out of that. It is a function you are defining on the spot, which does nothing until it is called:

```jsx
<button onClick={() => onRemove(todo.id)}>   // hands over a function that, when run, calls onRemove
```

Read it as *"when clicked, call `onRemove` with this row's id"*. Any time you need a handler that takes an argument, this is the shape.

### A checkbox is controlled by `checked`, not by `value`

Everything above about controlled inputs still holds, with one substitution. A text input carries text, so its state prop is `value`. A checkbox carries a yes or a no, so its state prop is **`checked`**, and the thing to read off the event is **`e.target.checked`** rather than `e.target.value`.

`TodoItem` above does not need to read the event at all — the row already knows which to-do it is, and `done` is just being flipped — so `onChange={() => onToggle(todo.id)}` ignores its argument entirely.

Use `value` on a checkbox and you get the warning from earlier in this note, *"changing an uncontrolled input to be controlled"*, because `checked` was never given. It is the same warning with a different cause, and the cause is the one you are most likely to hit.

### Changing one item in a list means a new object as well as a new array

`handleAdd` builds a new array with `[...todos, x]`. `handleRemove` builds a new array with `filter`. Toggling is the third of these, and the only one that changes an item that is already in the list.

`map` is what does it:

```jsx
todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t))
```

Walk the list. Hand back every to-do unchanged, except the one whose `id` matched — and for that one, hand back **a copy**. Read `{ ...t, done: !t.done }` as *everything this to-do already had*, and then `done` set to the opposite of what it was.

So `map` produces a new array, and the spread produces a new object for the one that changed. Both halves matter, and this line is the shape you will use every time a list item changes.

### A to-do is an object now, and that is what makes delete possible

Last week a to-do was a string: `["Buy milk", "Call the landlord"]`. That works right up until a row can be removed, because to delete one you have to say *which* one — and the obvious way to say it is by its text:

```jsx
setTodos(todos.filter((t) => t !== text));   // deletes every "Buy milk"
```

Two people can both put "Buy milk" on the list, and that line removes both of them. The row's own text cannot identify the row.

The position in the array can, and `filter((t, i) => i !== index)` really does work today. It stops working the moment anything about the list is not a straight click on a rendered row — a reorder, or an update that arrives from a backend while the user is halfway through something. And the position is also what [makes a poor `key`](Intro-to-React.md#every-item-needs-a-key).

So each to-do carries its own name from the moment it is made, an ID made with `crypto.randomUUID()` — built into the browser, no library needed. A counter that goes up by one works just as well.

**The id is made once, when the to-do is made**, not worked out while rendering. A key has to name the *same* item on every render, and anything computed at render time is a new answer each time. This is the one place in the course where deriving a value instead of storing it is the wrong move.

### `TodoItem` has a delete button and cannot delete anything

Look at what `TodoItem` was given: the `todo` to draw, and `onRemove` to call. It does not know what `onRemove` does. It is not deleting anything — it is *reporting a click*, and the list decides what that means.

That is not an accident of this example, it is how the whole tree is wired: data down as props, events back up as functions to call.

## What came up in the lecture

Things that happened while this was coded live, rather than things that were planned.

### The smallest thing that counts as a form

Asked in class what a `<form>` actually is, and the answer that stuck was by analogy. A slice of bread is not a sandwich. Bread and cheese is a sandwich. In the same way: a button on its own is not a form, an input on its own is not a form, and an input with a button is.

That is not a joke about the definition, it is the definition doing work. A form is the *grouping* — the thing that says these inputs and this button belong together, are submitted together, and are what Enter applies to. Which is exactly why the input had to go inside one before Enter did anything.

### "Too many re-renders"

Wiring the checkbox up produced this, immediately:

```
Too many re-renders. React limits the number of renders to prevent an infinite loop.
```

The cause was a missing arrow:

```jsx
<input type="checkbox" onChange={onToggle(todo.id)} />     // wrong
<input type="checkbox" onChange={() => onToggle(todo.id)} />  // right
```

The first one calls `onToggle` *while rendering*. `onToggle` sets state. Setting state causes a render. That render calls `onToggle` again. React counts the loop and stops you.

It is the same mistake as [the arrow above](#why-the-arrow-onclick-onremove-todo-id), and worth knowing in this louder form too: if you ever see *too many re-renders*, look for a handler you called instead of passed.

### `JSX syntax is disabled` means the file is called `.js`

Extracting the row into a new file produced an error that says nothing about the filename:

```
JSX syntax is disabled and should be enabled via parser options
```

The file was `TodoItem.js`. Renaming it to `TodoItem.jsx` fixed it.

This is **Vite's rule, not React's** — Vite decides whether to run the JSX transform by looking at the extension, so a `.js` file is treated as ordinary JavaScript and the first `<` is a syntax error. Other React setups are less fussy; the older Create React App compiled JSX in `.js` files quite happily. Worth knowing only because the message points nowhere near the cause.

### The point of extracting `TodoItem`

Pulling the row out into its own component is not tidying for its own sake. Left alone, a file like this grows to five hundred lines of JSX, and at that size nobody can read it, nobody can find a bug in it, and every change is a risk.

That is also worth knowing about the AI tools you will be using: they will cheerfully write you five hundred lines of JSX in one component, because you asked for a feature and that is a way to deliver it. The judgement about what should be its own component is still yours, and saying *no, pull that out, I want to be able to read this* is part of using the tool well rather than a nicety on top.

## Exam Questions

### 1. What does it mean for an input to be *controlled*, and what is the alternative?

### 2. Why does a form need `e.preventDefault()` in a single-page application?

### 3. The input shows nothing when you type. Give two different reasons this can happen.

### 4. Why can a controlled input be cleared after submitting, when an uncontrolled one cannot?

### 5. You add a **Clear** button next to **Add** and now clearing also adds a to-do. Why, and what is the fix?

### 6. Last week a to-do was a string. Why can the list not stay that way once rows can be deleted?

### 7. Why is a to-do's `id` created in `handleAdd` rather than worked out while rendering? Everywhere else the course says to derive rather than store.

### 8. `TodoItem` renders the delete button but cannot delete anything. What does it do instead?


## References

- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)
- *Adding Interactivity* > [Responding to Events](https://react.dev/learn/responding-to-events)
