# The useEffect Hook

## A pure function does not reach outside itself, in either direction

The term comes from functional programming, where the ideal is a **pure function** — one that computes its result and does nothing else. It makes two promises:

1. **It changes nothing outside itself.** Nothing in the world is different afterwards.
2. **It depends on nothing outside itself.** So the same arguments always give the same answer.

One promise points outward, the other inward, and breaking each has its own name.

This one keeps both:

```js
function square(i) {
	return i * i;
}
```

This one breaks the first. It also writes the answer into **`localStorage`** — a small key-value store the browser keeps for every site, a handful of megabytes that survives a refresh, and the closest thing to a database you get without a server. It takes strings and gives strings back, and nothing else.

```js
function square(i) {
	localStorage.setItem("square", i * i);
	return i * i;
}
```

Writing to storage was not what `square` was for. That is reaching **outward**, and reaching outward has a name: a **side effect** — something the function does besides producing its answer.

### Reading from outside breaks the second promise

Writing reached outward. This one leaves the world alone and reaches **inward** instead:

```js
function lastSquare() {
	return localStorage.getItem("square");
}
```

Nothing is written, so nothing is *affected* — in the strict sense this is not a side effect at all. But call it twice with the same arguments (there are none) and you can get two different answers, because the answer was never in the arguments. It came from outside.

Which leaves us needing one word that covers both cases, and there is one:

> **A function is impure when it reaches outside itself in either direction — when it changes something out there, or when its answer depends on something out there.**

`square` reaches out, which makes it impure *and* a side effect. `lastSquare` reaches in, which makes it impure and not a side effect at all. Every side effect is impure; not every impure function is a side effect.

React has no use for that distinction. Saving your to-dos and loading them back are the same job done in two directions, and neither belongs in the body of a component. **So from here on this note says *impure*, and means either direction.**


## The impure parts belong in an effect, not in the component body

A component function has one job: return JSX. Anything else it does — writing to storage, reading it back, changing the page title, calling a backend — makes it impure, and belongs in an effect rather than in the body of the component.

Those four have something in common worth naming: none of them is under React's control. **Anything React does not control is *outside*, and an effect is how you keep your component and the outside in step.**

Leave the `setItem` in the body instead and it runs on *every* render, including the ones that had nothing to do with your to-dos. The effect is where you get to say **when**.

### You state the dependency, and React runs the function at the right moment

`useEffect` lets us hook into React and catch the moment a state variable changes, so we can do something about it. Below: a to-do list that writes itself to local storage whenever the list changes.

```jsx
import { useState, useEffect } from "react";

export default function TodoList() {
  const [todos, setTodos] = useState([]);   // each one is { id, text, done }

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  // … the input, the list, the delete button: last week's component, unchanged
}
```

Read it as a sentence: **whenever `todos` changes, write it to local storage.** You never call that function yourself explicitly. You state the dependency, and React runs it at the right moment. You describe the relationship, let React do the work. 

`JSON.stringify` is there because local storage only holds **strings**. Hand it an array and you get back `"[object Object]"` on the next load, which is a confusing ten minutes if you have not been warned.

### The first argument says what to do, the second says when

**First, what to do** — a function, usually written in place as an arrow function, though a named one works just as well.

**Second, when to do it** — an array of the values the effect depends on. **Every effect runs once after the first render, whatever is in the array.** After that, React re-runs it whenever one of the dependencies differs from last time. Props count as well as state; anything the effect reads should be in there.

That first run is easy to forget and it is half of most answers: `[todos]` means *once at the start, and again on every change* — not *only on change*.

The array has two special cases. Leave it **empty** and the effect runs once, at mount — that is the next section. Leave it **out altogether** and it runs after every single render, which is almost never what you want and which is why it waits for [useEffect Against a Live Backend](../Backend/useEffect-Against-a-Live-Backend.md), where it does real damage.

### The page title is the same shape as saving to storage

So that the browser tab says something useful:

```jsx
useEffect(() => {
  document.title = `My To-Do (${todos.length})`;
}, [todos]);
```

### An effect is not for computing something you already have

If a value can be worked out from what you already have, work it out while rendering — `todos.filter(t => !t.done).length` — rather than storing it in state and syncing it with an effect. That is a common enough mistake to have a name — **derived state**, kept in state when it should have been derived. It makes two sources of truth where one would do, and they drift.

You have met this already: `disabled={text.length === 0}` in [Forms and Controlled Components](Forms-and-Controlled-Components.md) is the same rule, one note earlier.

### An effect is a relationship, not an instruction

`useEffect` might honestly have been called `useReactive`.

You have already met this with `useState`: change the data, and React works out what the screen should look like — see [Reactive Programming](Intro-to-React.md#reactive-programming).

`useEffect` is the same idea pointed outwards. `useState` keeps the *screen* in step with your data; `useEffect` keeps *everything else* in step with it. Same dependency, same automatic re-run, different destination.


## An empty dependency list means run once, at mount

An effect with an **empty** array runs once, when the component first appears, and never again.

**Mount** is React's word for a component appearing for the first time — its first render, when it goes from not being on screen to being on screen. The opposite is **unmount**, when it is taken off again. A component mounts once and can then re-render any number of times.

An empty dependency list says *nothing to depend on*, so there is never a later change to react to, so it runs at mount and never again.

### The list is saved on every change, and read back exactly once

The app saves the list on every change; it needs to read it back exactly once, when it starts. That is the persistence half of the app, complete:

```jsx
function loadTodos() {
  const saved = localStorage.getItem("todos");
  return saved ? JSON.parse(saved) : [];
}

export default function TodoList() {
  const [todos, setTodos] = useState(loadTodos);

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  // …
}
```

Note where the load went. `useState(loadTodos)` — the function passed, not called — asks React to run it once, for the initial value, and never again.

It could have been an effect with an empty array instead, but then the first render would show an empty list and the saved one would appear a moment later, which flickers.

The missing `()` is deliberate, and this is the one place all week where it is. Write `useState(loadTodos())` instead and the app still works, which is what makes it worth pointing at: you would be reading from storage on **every** render, and never notice. React ignores the *argument* after the first render; it cannot stop you computing it.

`JSON.parse` is the other half of `JSON.stringify`: storage gave back the string you put in, and this turns it into an array again. The `saved ? … : []` matters on the very first visit, when there is nothing stored and `getItem` returns `null`.

**In two weeks this same shape points at a backend instead of the browser** — the same hook, the same dependency array, a Parse query instead of `localStorage`. The swap is smaller than it sounds.

### Effects run twice in development, on purpose

React — specifically the `<StrictMode>` wrapper around your app in `main.jsx` — deliberately mounts every component twice while you are developing, to shake out effects that do not tolerate being run again. In production it happens once.

So if you see two entries in the console where you expected one, that is why, and it is not a bug you introduced. Saving to local storage twice does no harm — it writes the same thing both times.

It is worth knowing what this is *for*, though. An effect that **sends** something — a message, an order, a payment — would have sent it twice, and that is exactly the bug the double mount is designed to make visible while you are still at your desk.


## Cleanup and the missing dependency list wait until there is a backend

`useEffect` has two further forms — a **cleanup function**, and no dependency list at all. Neither does anything useful against local storage, and both matter once an effect talks to a live backend. They are in [useEffect Against a Live Backend](../Backend/useEffect-Against-a-Live-Backend.md), with the problems that make them necessary.


## Exam Questions

### 1. Explain what this useEffect does, and when it runs:
```js
useEffect(() => {
  localStorage.setItem("todos", JSON.stringify(todos));
}, [todos]);
```

### 2. What is the difference between these two, and which one saves your work?
```js
// Version A
useEffect(() => {
  localStorage.setItem("todos", JSON.stringify(todos));
}, []);

// Version B
useEffect(() => {
  localStorage.setItem("todos", JSON.stringify(todos));
}, [todos]);
```

### 3. One of these is a side effect and one of them is not. Say which, and why React puts both in an effect anyway.
```js
function square(i) {
  localStorage.setItem("square", i * i);
  return i * i;
}

function lastSquare() {
  return localStorage.getItem("square");
}
```

### 4. The to-do list is read back with `useState(loadTodos)` rather than an effect with an empty dependency array. Both work. What does the user see if you use the effect, and why?

### 5. You expected one line in the console and you got two. What is React doing, why is it harmless for local storage, and what kind of effect would it *not* be harmless for?
