# Component State

**The app now.** Add pushes a task onto the array — and nothing appears on screen. The variable really did change; the screen simply does not care. That failure is the whole argument for state, so it is worth running before you read on.

## Every component can store local state 

The difference from props is **ownership**. Props arrive from the parent and the component may only read them; state belongs to the component itself, which is the only thing that can change it. Props are what you were given; state is what you keep.

First, the version that does **not** work — worth typing out, because the reason it fails is the reason state exists:

```jsx
const SAMPLE_TASKS = [
	"Buy milk", 
	"Call the landlord", 
	"Book the dentist",
    "Water the plants", 
    "Reply to Mette"];

function randomTask() {
  return SAMPLE_TASKS[Math.floor(Math.random() * SAMPLE_TASKS.length)];
}

let todos = ["Buy milk"]; // an ordinary variable

function TodoList() {
  function handleAdd() {
    todos.push(randomTask());
    console.log(todos);            // the array really does grow — look at the console
  }
  // …and the screen never changes
}
```

The array grows. The console proves it. The screen ignores you completely, because nothing told React that anything happened — it only re-runs your component when you ask it to, and pushing onto a variable is not asking.

## State comes from `useState`

The `useState` hook:
- takes an **initial** value
- returns **current value** and a **setter function** (returns from where? you get it from React! React gave you this setter! It baked an observer inside of it! So now if you change the state with its help, it will know that the state has changed! Let's see what does this imply)

```jsx

// We are importing the useState function from React
import { useState } from "react";

function TodoList() {
  const [todos, setTodos] = useState(["Buy milk"]);

  function handleAdd() {
    setTodos([...todos, randomTask()]);   
    // a *new* array, not a push
  }

  return (
    <>
      <ul>
        {todos.map((text, index) => <TodoItem key={index} text={text} />)}
      </ul>
      <button onClick={handleAdd}>Add</button>
    </>
  );
}
```

Two things changed, and both matter:

1. `todos` now comes from `useState`, so React is the one holding it. The broken version above did survive — a variable outside the component persists perfectly well — but nothing connected it to the screen. Had we moved that `let` *inside* the component it would have been worse still, created fresh on every call.
- `setTodos` is given a **new array** — `[...todos, randomTask()]` — rather than the old one mutated. **React decides whether to redraw by comparing what it was given with what it** **had**; hand it the same array object back and it sees no change, even if the contents differ. `push` would have done exactly that.

*Optional*: See the [button with counter example](https://react.dev/learn#updating-the-screen) for a combination of state and events

## Reactive Programming

**The app now.** It works: **Add** appends a random sample task and the list grows. The question left over is *why the screen redrew at all* — nobody told it to.

When a state variable defined with `useState` changes with the help of the setter (and thus, not changing the variable directly!!) a redrawing of the whole component is triggered.

This is *reactive programming*. And reactive programming is why React is called so.

A bit like in Excel -- one of the classical reactive programming environments -- where when you change one cell, all the others who depend on it and only those are changed automatically.

In React, the dependents are not formulas, but UIs. When a state variable or a prop changes, the library automatically redraws all the relevant UI elements, and only those.

So the loop the app now runs is:

> you click **Add** → `handleAdd` calls `setTodos` with a new array → React notices the state it is holding is not the array it had → it calls `TodoList()` again → `map` builds one more `<TodoItem />` than last time → the new row appears.

Nobody wrote "add a row to the screen" anywhere. You changed the data and described what the screen should look like for any data; React did the rest. That is the trade React asks you to make, and everything else this term is a consequence of it.

Here is the whole thing:

```jsx
import { useState } from "react";

const SAMPLE_TASKS = ["Buy milk", "Call the landlord", "Book the dentist",
                      "Water the plants", "Reply to Mette"];

function randomTask() {
  return SAMPLE_TASKS[Math.floor(Math.random() * SAMPLE_TASKS.length)];
}

function TodoItem({ text }) {
  return <li className="todo-item">{text}</li>;
}

export default function TodoList() {
  const [todos, setTodos] = useState(["Buy milk"]);

  function handleAdd() {
    setTodos([...todos, randomTask()]);
  }

  return (
    <>
      <h1>My To-Do ({todos.length})</h1>
      <ul>
        {todos.map((text, index) => (
          <TodoItem key={index} text={text} />
        ))}
      </ul>
      <button onClick={handleAdd}>Add</button>
    </>
  );
}
```

Forty lines, and every idea above is in there somewhere.

And deliberately silly: **Add** picks a task at random, because there is nothing to type into yet. Giving it something to type into is [Forms and Controlled Components](Forms-and-Controlled-Components.md) — along with the first real bug, when deleting from the middle of the list shows you why keying by position was never going to hold.

## Exam Questions

### 1. Explain the difference between props and state in React.

### 2. What is *reactive* about programming in React?

### 3. You push a new item onto an array and the screen does not change. Why not, and what do you do instead?

### 4. Why should you avoid mutating state objects and arrays directly in React?

## References

- *Adding Interactivity* > [State: A Component's Memory](https://react.dev/learn/state-a-components-memory)
