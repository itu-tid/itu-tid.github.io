# The useEffect Hook 

## A side effect is anything besides the main calculation

The term comes from functional programming, where the ideal is a **pure function**: give it the same arguments and it gives you the same answer, every time, and changes nothing else in the world.

This one is pure:
```js

function square(i) {
	return i*i;
}
```

This one is not:

```js
function square (i) {
	localStorage.setItem("square", i*i);
	return i*i;
}
```

In the above case `localStorage.setItem` writes the result somewhere. **`localStorage`** is a small key-value store the browser keeps for every site — a handful of megabytes that survives a refresh, and the closest thing to a database you get without a server. It takes strings and gives strings back, and nothing else.

Writing to storage was not what `square` was for. It is a **side effect** — something the function does besides producing its answer.


## Side Effects in React with `useEffect`

A component function has one job: return JSX. Anything else it does — writing to storage, changing the page title, starting a timer, calling a backend — is a side effect, and belongs in an effect rather than in the body of the component.

### The goal: keep your component in step with something outside React

`localStorage`, the document title, a timer, a backend — anything React does not control is *outside*, and an effect is how you keep the two in step.


### Writing one

`useEffect` lets us hook into React and catch the moment a state variable changes, so we can do something about it. Below: a to-do list that writes itself to local storage whenever the list changes.

```jsx
import { useState, useEffect } from "react";

export default function TodoList() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  // …
}
```

Read it as a sentence: **whenever `todos` changes, write it to local storage.** You never call that function yourself. You state the dependency, and React runs it at the right moment — which is the same bargain as `map`: describe the relationship, let React do the work.

`JSON.stringify` is there because local storage only holds **strings**. Hand it an array and you get back `"[object Object]"` on the next load, which is a confusing ten minutes if you have not been warned.

### The two arguments

**First, what to do** — a function, usually written in place as an arrow function, though a named one works just as well.

**Second, when to do it** — an array of the values the effect depends on. React re-runs the effect whenever any of them differs from last time. Props count as well as state; anything the effect reads should be in there.

The array has two special cases, both further down: leave it **empty** and the effect runs once, at mount. Leave it **out altogether** and it runs after every single render, which is almost never what you want.

**And is *reading* from storage a side effect?** In the functional-programming sense, no — nothing changes, so nothing is affected. But it does make the function **impure**: its result depends on something other than its arguments, so two identical calls can return different answers. React's framing sidesteps the argument: reading and writing are both *synchronising with something outside*, and that is what effects are for.

### Other things an effect is for

**The page title**, so the browser tab says something useful:

```jsx
useEffect(() => {
  document.title = `My To-Do (${todos.length})`;
}, [todos]);
```

**What an effect is *not* for** is computing something from state. If a value can be worked out from what you already have, work it out while rendering — `todos.filter(t => !t.done).length` — rather than storing it in state and syncing it with an effect. That is a common enough mistake to have a name: it makes two sources of truth where one would do, and they drift.

`useEffect` might honestly have been called `useReactive`: what you write is a relationship, not an instruction.

### An effect is a relationship, not an instruction

You have already met this with `useState`: change the data, and React works out what the screen should look like — see [Reactive Programming](Intro-to-React.md#reactive-programming).

`useEffect` is the same idea pointed outwards. `useState` keeps the *screen* in step with your data; `useEffect` keeps *everything else* in step with it. Same dependency, same automatic re-run, different destination.


## The empty dependency list: run once, at mount

An effect with an **empty** array runs once, when the component first appears, and never again.

**Mount** is React's word for a component appearing for the first time — its first render, when it goes from not being on screen to being on screen. The opposite is **unmount**, when it is taken off again. A component mounts once and can then re-render any number of times.

An empty dependency list says *nothing to depend on*, so there is never a later change to react to, so it runs at mount and never again.

### What only happens once

**Loading.** The app saves the list on every change; it needs to read it back exactly once, when it starts. That is the whole to-do app made persistent:

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

Note where the load went. `useState(loadTodos)` — the function passed, not called — asks React to run it once, for the initial value, and never again. It could have been an effect with an empty array instead, but then the first render would show an empty list and the saved one would appear a moment later, which flickers.

`JSON.parse` is the other half of `JSON.stringify`: storage gave back the string you put in, and this turns it into an array again. The `saved ? … : []` matters on the very first visit, when there is nothing stored and `getItem` returns `null`.

**In two weeks this same shape points at a backend instead of the browser** — the same hook, the same dependency array, a Parse query instead of `localStorage`. The swap is smaller than it sounds.

### One thing that will confuse you: effects run twice in development

React deliberately mounts every component twice while you are developing, to shake out effects that do not tolerate being run again. In production it happens once.

So if you see two entries in the console where you expected one, that is why, and it is not a bug you introduced. Saving to local storage twice does no harm — it writes the same thing both times.


## Two more shapes, when you need them

`useEffect` has two further forms — a **cleanup function**, and no dependency list at all. Neither does anything useful against local storage, and both matter once an effect talks to a live backend. They are in [useEffect Against a Live Backend](../Backend/useEffect-Against-a-Live-Backend.md), with the problems that make them necessary.


## Exam Questions

### 1. Explain what this useEffect does, and when it runs:
```js
useEffect(() => {
  localStorage.setItem("todos", JSON.stringify(todos));
}, [todos]);
```

### 2. What is the difference between these two useEffect calls?
```js
// Version A
useEffect(() => {
  console.log("Effect A");
}, []);

// Version B
useEffect(() => {
  console.log("Effect B");
});
```
