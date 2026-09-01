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

An input whose value comes from state is called **controlled**. The opposite is **uncontrolled**: do not set `value`, and the input keeps its own text.

That is the whole of the terminology, and it is worth knowing mainly because it turns up in every answer you will find online — and in the warning React prints when a `value` arrives late: 

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

`setText("")` empties the field, which is only possible *because* the input is controlled. An uncontrolled input holds its own text and you would have to reach into the browser DOM to empty it.

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

### A checkbox is controlled by `checked`, not by `value`

Everything above about controlled inputs still holds, with one substitution. A text input carries text, so its state prop is `value`. A checkbox carries a yes or a no, so its state prop is **`checked`**, and the thing to read off the event is **`e.target.checked`** rather than `e.target.value`.

`TodoItem` above does not need to read the event at all — the row already knows which to-do it is, and `done` is just being flipped — so `onChange={() => onToggle(todo.id)}` ignores its argument entirely.

Use `value` on a checkbox and you get the warning from earlier in this note, *"changing an uncontrolled input to be controlled"*, because `checked` was never given. It is the same warning with a different cause, and the cause is the one you are most likely to hit.

### Changing one item in a list means a new object as well as a new array

`handleAdd` builds a new array with `[...todos, x]`. `handleRemove` builds a new array with `filter`. Toggling is the third of these, and the only one that changes an item that is already there.

`map` is what does it: walk the list, hand back every to-do unchanged except the one that matched, and for that one hand back **a copy with `done` flipped**.

That copy is the part worth slowing down on, because the obvious alternative looks right and is not:

```jsx
const copy = [...todos];                       // a new array...
copy.find((t) => t.id === id).done = true;     // ...holding the SAME objects
setTodos(copy);
```

Week 1 told you React compares what you hand the setter against what it had, and that handing back the same array means no change. That is true and this code obeys it: the array really is new, and the screen really does update. But the *to-do* inside it was never copied — it was edited in place, and it is the same object your `useEffect` is about to write to storage, the same object anything else holding a reference is looking at.

**The rule is not "give the setter a new array". It is "do not change anything that is already in state."** A new array is only half of it when what you are changing lives inside one.

### A to-do is an object now, and that is what makes delete possible

Last week a to-do was a string: `["Buy milk", "Call the landlord"]`. That works right up until a row can be removed, because to delete one you have to say *which* one, and a string cannot say. Two people can both put "Buy milk" on the list. [The index is not an answer either](Intro-to-React.md#every-item-needs-a-key): delete the first row and the index of every row after it changes.

So each to-do carries its own name, made with `crypto.randomUUID()` — built into the browser, no library needed. A counter that goes up by one works just as well.

**The id is made once, when the to-do is made**, not worked out while rendering. A key has to name the *same* item on every render, and anything computed at render time is a new answer each time. This is the one place in the course where deriving a value instead of storing it is the wrong move.

### `TodoItem` has a delete button and cannot delete anything

Look at what `TodoItem` was given: the `todo` to draw, and `onRemove` to call. It does not know what `onRemove` does. It is not deleting anything — it is *reporting a click*, and the list decides what that means.

That is not an accident of this example, it is how the whole tree is wired: data down as props, events back up as functions to call.

## References

- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)
- *Adding Interactivity* > [Responding to Events](https://react.dev/learn/responding-to-events)


## Exam Questions

### 1. What does it mean for an input to be *controlled*, and what is the alternative?

### 2. Why does a form need `e.preventDefault()` in a single-page application?

### 3. The input shows nothing when you type. Give two different reasons this can happen.

### 4. Why can a controlled input be cleared after submitting, when an uncontrolled one cannot?

### 5. You add a **Clear** button next to **Add** and now clearing also adds a to-do. Why, and what is the fix?

### 6. Last week a to-do was a string. Why can the list not stay that way once rows can be deleted?

### 7. Why is a to-do's `id` created in `handleAdd` rather than worked out while rendering? Everywhere else the course says to derive rather than store.

### 8. `TodoItem` renders the delete button but cannot delete anything. What does it do instead?
