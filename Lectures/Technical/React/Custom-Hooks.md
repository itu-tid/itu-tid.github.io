# Custom Hooks

[The Three States of Remote Data](The-Three-States-of-Remote-Data.md) ended with a promise: every screen that fetches needs the same `useState` pair and the same `useEffect`, and "later in the course we come back and do something about this one." This is that note.

## Every page that loads something repeats the same twelve lines

Here is `ListPage` from todo-26, once its query has moved into `loadList(listId)` in a service, as in the week 8 exercise:

```jsx
export default function ListPage() {
  const { listId } = useParams();

  const [list, setList] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function load() {
      try {
        setList(await loadList(listId));
      } catch (err) {
        setError(err.message);
      }
    }
    load();
  }, [listId]);

  if (error) return <p>{error}</p>;
  if (!list) return <p>Loading…</p>;
  return <ToDoList list={list} />;
}
```

The home page that loads your lists has the same two `useState` calls, the same `useEffect`, and the same `try`/`catch`. So does every page in your group project that shows something from Parse. Only two things change from one copy to the next: *which* service function is called, and *what* the page renders.

The service layer could not remove this duplication, because it is not about talking to Parse. It is about **React state**: something is loading, then it is there or it failed. Moving state out of a component needs a hook.

## A custom hook is a function whose name starts with `use` and that calls other hooks

That is all it is. There is no API to register it and nothing to import from React to make one:

```jsx
// src/hooks/useList.js
import { useEffect, useState } from "react";
import { loadList } from "../services/listService.js";

export function useList(listId) {
  const [list, setList] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function load() {
      try {
        setList(await loadList(listId));
      } catch (err) {
        setError(err.message);
      }
    }
    load();
  }, [listId]);

  return { list, error };
}
```

And the page shrinks to what it is actually about:

```jsx
export default function ListPage() {
  const { listId } = useParams();
  const { list, error } = useList(listId);

  if (error) return <p>{error}</p>;
  if (!list) return <p>Loading…</p>;
  return <ToDoList list={list} />;
}
```

The `use` prefix is not decoration. It tells the [rules of hooks](Hooks.md) linter that this function calls hooks, so it checks the callers too: no `useList` inside an `if`, a loop, or an event handler. Name it `getList` and the linter goes quiet, but the rules still apply, and breaking them still breaks your component.

## A hook is worth writing even when only one component uses it

Reuse is the reason that is easiest to see, and not the most important one. Two others hold even for a hook with a single caller:

- **Decomposition.** A component that loads a list, polls it, tracks whether the app is online and handles the install prompt does four things, and reads like it. Each hook pulled out of it takes one of those things away and gives it a name. What is left reads like a description of the screen: `useList(listId)`, `useInterval(reload, 10_000)`. The same instinct that splits a big component into smaller components ([Extracting Components](../Structure/Refactoring-by-Extracting-Components.md)) applies to the logic inside one.
- **Encapsulation.** `ListPage` no longer knows that the list comes from Parse, that a stale answer has to be ignored, or that loading can fail in two ways. If you later replace polling with push, or Parse with something else, you change `useList` and no screen notices. A hook is a wall around a decision you might want to change.

So the question is not only "will I need this twice?" but "would this component be easier to read if this part had a name?"

## The hook returns data, and the component decides what it looks like

A custom hook returns values (state, and functions that change it), never JSX. `useList` does not know whether the list ends up in a `<ul>`, a MUI `Card`, or a count in the navigation bar. That is the same split as the service layer, one level up:

| layer | knows about | does not know about |
|---|---|---|
| service (`loadList`) | Parse, class names, field names | React, the screen |
| hook (`useList`) | React state, loading and failing | Parse, the screen |
| component (`ListPage`) | what the user sees | Parse, how loading works |

When a hook starts returning `<p>Loading…</p>`, it has turned into a component with an odd name. Turn it into a component.

## Each call gets its own state; a hook shares code, not data

If the home page and the navigation bar both call `useCurrentUser()`, each gets its **own** `useState`, inside its own component, and each runs its own `useEffect`. Two components, two requests, two copies of the user that can drift apart.

This is the most common misunderstanding about custom hooks. A hook is a way of reusing *logic*. When two components need the *same value*, that value lives in one place, in their common parent or in a context, and travels down as props. That is the topic of [Patterns of Component Communication](Patterns-of-Component-Communication.md).

## A fix made in the hook is made on every screen

There is a bug in the `useEffect` above, and in every copy of it in your project. Open list A, then quickly click to list B. Two requests are now on their way. If A's answer arrives *after* B's, the page shows list A under list B's URL.

The fix is to ignore an answer that arrives after the effect has been cleaned up:

```jsx
useEffect(() => {
  let ignore = false;

  async function load() {
    try {
      const result = await loadList(listId);
      if (!ignore) setList(result);
    } catch (err) {
      if (!ignore) setError(err.message);
    }
  }
  load();

  return () => {
    ignore = true;   // listId changed, or the page closed: this answer is stale
  };
}, [listId]);
```

Written into twelve components, that fix gets forgotten in at least one of them. Written into `useList`, it is made once and every screen has it. This, more than the lines saved, is why you extract a hook: the tricky part of the pattern gets one home.

## A polling timer belongs in a hook, because its cleanup is easy to forget

[Efficient Communication](../Backend/Efficient-Communication-with-the-Backend.md#polling-asks-again-every-few-seconds-and-is-usually-enough) shows how to reload data every few seconds with `setInterval`, and why the interval must be cleared when the component goes away. Forgetting that cleanup is exactly the kind of mistake a hook prevents. The first version is short:

```jsx
// src/hooks/useInterval.js
import { useEffect } from "react";

export function useInterval(callback, milliseconds) {
  useEffect(() => {
    const id = setInterval(callback, milliseconds);
    return () => clearInterval(id);
  }, [callback, milliseconds]);
}
```

```jsx
// the shopping list reloads every ten seconds while it is open
useInterval(reload, 10_000);
```

### A ref keeps the latest callback without restarting the timer

That version has a problem you only see in use. `reload` is defined inside the component, so it is a **new function on every render**. It is in the dependency array, so every render clears the timer and starts a new one. Type into a form on that page, and each keystroke restarts the ten seconds: the list never reloads while you type.

Take `callback` out of the dependencies, and the opposite happens: the timer keeps the `reload` from the first render forever, with the state of the first render in it (a *stale closure*).

What the hook needs is a place to keep **the latest callback, without restarting the timer when it changes**: a value that survives renders, and whose change does not cause one. That is exactly what a ref is ([The useRef Hook](The-useRef-Hook.md)):

```jsx
import { useEffect, useRef } from "react";

export function useInterval(callback, milliseconds) {
  const latestCallback = useRef(callback);

  // after every render, remember the newest callback; the timer is not touched
  useEffect(() => {
    latestCallback.current = callback;
  });

  // the timer starts once, and always calls whatever callback is newest
  useEffect(() => {
    const id = setInterval(() => latestCallback.current(), milliseconds);
    return () => clearInterval(id);
  }, [milliseconds]);
}
```

The component still writes `useInterval(reload, 10_000)`. All of this is inside the hook, which is the point: the tricky part has one home.

## A hook can wrap a browser event just as well as a fetch

Hooks are not only for remote data. Anything a component has to *subscribe to and clean up after* is a candidate: a timer, the window's width, whether the browser is online. todo-26 has one more since week 11: `src/hooks/useInstallPrompt.js` listens for the browser's "this app can be installed" event and returns `{ canInstall, install }`, so that the home page can show an Install button without knowing how installing works (see [Installing Your App on a Phone](../Tooling/Installing-Your-App-on-a-Phone.md#notes)).

Once a project has a `src/hooks/` folder, the hook names read like a list of what the app does: `useList`, `useInterval`, `useInstallPrompt`. Each one names a single behavior, which is the same test you apply to a component name.

## Exam Questions

### 1. What makes a function a custom hook? What changes if you rename `useList` to `getList`?

### 2. Two components both call `useCurrentUser()`. How many requests go to the backend, and how many copies of the user exist? What would you do if they must always show the same user?

### 3. Why should a custom hook return data rather than JSX?

### 4. Explain the bug that the `ignore` flag fixes. Why is a custom hook a better place for that fix than each component?

### 5. Write `useInterval(callback, milliseconds)`. What happens if you leave out the function that `useEffect` returns?

### 6. Give two reasons to extract a custom hook that only one component uses.

### 7. Why does `useInterval` keep the callback in a ref instead of putting it in the effect's dependency array?

## References

- [Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks), react.dev
- [Fetching data](https://react.dev/reference/react/useEffect#fetching-data-with-effects), react.dev: the `ignore` flag
