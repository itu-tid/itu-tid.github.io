# Custom Hooks

![Three cells, each behind its own membrane, with signal molecules travelling between them](../images/cells-and-messages.svg)

Alan Kay studied molecular biology before he turned to computers, and he coined the term *object-oriented*. He imagined software built like a body: out of cells. Each cell keeps its insides behind a membrane, and cells work together only by sending each other messages. Nobody reaches into another cell.

A component, a service and a custom hook are such cells. A row that calls `onRemove` sends a message; a row holding `setTodos` is a hole in the membrane.

[The Three States of Remote Data](The-Three-States-of-Remote-Data.md) ended with a promise: every screen that fetches needs the same `useState` pair and the same `useEffect`, and "later in the course we come back and do something about this one." This is that note.

## A custom hook is the third way to pull out a part and give it a name

You have done this twice already. Each time, you found a part of a component that did its own job, moved it out, gave it a name, and hid a decision behind that name:

| what you pull out | where it goes | what it hides |
|---|---|---|
| repeated JSX | a component ([week 8](../Structure/Finding-the-Components.md)) | how a row is drawn |
| talking to the backend | a service ([week 8](../Structure/Pulling-Out-the-Service-Layer.md)) | that the data comes from Parse |
| state and effects | a custom hook (this note) | how loading, errors and stale answers work |

The principle is the same in all three, and older than React.

### Decomposition: cut the whole into parts you can name

Each part does one job and has a name in a word or two: `MyListRow`, `listService`, `useList`. The whole then reads as its names: `Home` is two headings, two kinds of row and a form.

### Encapsulation: each part hides a decision

`listService` hides that the data comes from Parse. `useList` hides how the page keeps track of loading, the result and the error. Nothing outside depends on what is hidden.

### Cut where a decision is likely to change

Parnas, 1972: put each decision that may change inside one part. When it changes (Parse for another backend, polling for push), only that part changes.

### The cut buys reading first, changing second, reuse last

- **Reading:** a part makes sense without the rest.
- **Changing:** one decision, one place.
- **Reuse:** a bonus. Most parts are worth it even when used once.

### Every part costs a name and a jump

Too few parts, and one component does everything. Too many, and following one click means opening five files.

### Three questions decide every cut

1. **Can you name it?** If not, it is not one thing yet.
2. **What does it hide?** If nothing, it is only indirection.
3. **Would a change of that decision stay inside it?** If not, the cut is in the wrong place.

Custom hooks are how React applies this to state. Another framework names the third row differently; the questions stay the same.

## Every page that loads something repeats the same lines

Here is `ListPage` from todo-26, once its query has moved into `loadList(listId)` in a service, as in the week 8 exercise:

```jsx
export default function ListPage() {
  const { listId } = useParams();

  const [list, setList] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function load() {
      setLoading(true);
      setError(null);
      try {
        setList(await loadList(listId));
      } catch (err) {
        setError(err.message);
      }
      setLoading(false);
    }
    load();
  }, [listId]);

  if (loading) return <p>Loading…</p>;
  if (error) return <p>{error}</p>;
  return <ToDoList list={list} />;
}
```

The home page that loads your lists has the same three `useState` calls, the same `useEffect`, and the same `try`/`catch`. So does every page in your group project that shows something from Parse. Only two things change from one copy to the next: *which* service function is called, and *what* the page renders.

The service layer could not remove this duplication, because it is not about talking to Parse. It is about **React state**: something is loading, then it is there or it failed. Moving state out of a component needs a hook.

## A custom hook is a function whose name starts with `use`, that calls other hooks, and that follows the rules of hooks

There is no API to register it and nothing to import from React to make one. But because it calls hooks, the [rules of hooks](Hooks.md#the-rules-top-level-always-unconditionally) from week 1 apply to it, on both sides:

- **Inside it**, every hook is called at the top level, in the same order on every render: never inside an `if`, a loop or a nested function. An `if` around *other* code is fine; `useList` below has a `try`/`catch` inside its effect.
- **Its callers** call it only from a component or from another hook, again at the top level: never from an event handler or a plain function.

```jsx
// src/hooks/useList.js
import { useEffect, useState } from "react";
import { loadList } from "../services/listService.js";

export function useList(listId) {
  const [list, setList] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function load() {
      setLoading(true);
      setError(null);
      try {
        setList(await loadList(listId));
      } catch (err) {
        setError(err.message);
      }
      setLoading(false);
    }
    load();
  }, [listId]);

  return { list, loading, error };
}
```

And the page shrinks to what it is actually about:

```jsx
export default function ListPage() {

  const { listId } = useParams();
  const { list, loading, error } = useList(listId);

  if (loading) return <p>Loading…</p>;
  if (error) return <p>{error}</p>;
  return <ToDoList list={list} />;
}
```

The `use` prefix is not decoration. It is how the rules-of-hooks linter knows that this function calls hooks, so it checks both sides. Name it `getList` and the linter goes quiet, but the rules still apply, and breaking them still breaks your component.


## Passing the loader as a function turns `useList` into one hook for every page

`useList` still has one thing hard-coded: it calls `loadList`. The home page that loads your lists would need a `useMyLists`, a profile page a `useProfile`, and each would be the same twenty lines with a different service call in the middle.

Write the specific hook first. Once you have written it three or four times and see that only that one call differs, pass the call in as a parameter:

```jsx
// src/hooks/useLoadingFromDB.js
import { useEffect, useState } from "react";

export function useLoadingFromDB(dbLoaderFunction, dbObjectId) {
  const [dbObject, setDbObject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  async function load() {
    try {
      setDbObject(await dbLoaderFunction());
      setError(null);
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  }

  useEffect(() => {
    setLoading(true);
    load();
  }, [dbObjectId]);

  return { dbObject, loading, error, reload: load };
}
```

The hook does not know what it loads; it only knows that loading takes time and can fail. Three things changed from `useList`:

- **`dbLoaderFunction`** is the service call, handed in by the page.
- **`dbObjectId`** goes into the dependency array, so the hook loads again when the page's id changes. The hook cannot tell that by looking at the function: the page makes a new one on every render. (The linter will point at the missing `dbLoaderFunction`; putting it in would load again on every render.)
- **`reload`** loads again without showing *Loading…*, for when the page wants fresh data while it is open (the polling timer below).

Both pages now read the same way:

```jsx
export default function ListPage() {
  const { listId } = useParams();
  const { dbObject: list, loading, error } =
    useLoadingFromDB(() => loadList(listId), listId);

  if (loading) return <p>Loading…</p>;
  if (error) return <p>{error}</p>;
  return <ToDoList list={list} />;
}

export default function Home() {
  const { dbObject: lists, loading, error } = useLoadingFromDB(loadMyLists);
  // ...
}
```

`dbObject: list` renames what the hook returns, so the rest of the page talks about a `list` again, not a `dbObject`.

A hook has two jobs, and reuse is only one of them. The other is that the page reads as what it is about. `useList` already did the second; `useLoadingFromDB` adds the first. If the general one reads too abstract to you, stay with the specific ones: that is a fine choice.

## A hook gets a function to call later, not the result of calling it now

`useLoadingFromDB` does not want the list. It wants a way to *get* the list, which it calls when it decides to: after the first render, and again when the id changes. So the page hands it a function, and there are three ways to write that:

```jsx
// right: an anonymous function that calls loadList(listId) when it is called
useLoadingFromDB(() => loadList(listId), listId);

// right: the same function, with a name
function loadCurrentList() {
  return loadList(listId);
}
useLoadingFromDB(() => loadCurrentList(), listId);

// right: a function with no parameters can be passed by its name alone
useLoadingFromDB(loadCurrentList, listId);

// wrong: calls loadList now, during the render, and passes on what it returns
useLoadingFromDB(loadList(listId), listId);
```

The last one runs the query on every render, and hands the hook a Promise where it expected a function. `loadList` needs a `listId`, so it cannot be passed by its name: the hook would call it with nothing. Wrap it in a function that knows the id, anonymous or named, and the hook can call that with nothing.

`loadCurrentList` without parentheses means *this function*; with them, *call it now*. JavaScript lets you skip the `() =>` only for functions that take no parameters, which is why `loadMyLists` in `Home` needs no wrapper. You will meet the same idea again in the next note: a setter given a function instead of a value.

## A hook returns data, never JSX

A custom hook returns values (state, and functions that change it), never JSX. `useList` does not know whether the list ends up in a `<ul>`, a MUI `Card`, or a count in the navigation bar; `ListPage` decides. That keeps the hook usable by any screen, the same way a service is usable by any hook.

When a hook starts returning `<p>Loading…</p>`, it has turned into a component with an odd name. Turn it into a component.

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
const { dbObject: list, loading, error, reload } =
  useLoadingFromDB(() => loadList(listId), listId);
useInterval(reload, 10_000);
```

`reload`, not `reload()`: the timer gets the function, and calls it every ten seconds.

This version is good enough to start with, but it restarts the timer on every render, because `reload` is a new function each time. [The useRef Hook](The-useRef-Hook.md#a-ref-keeps-the-latest-callback-without-restarting-the-timer) fixes that.

## What came up in the lecture

*Things that happened while this was coded live, rather than things that were planned.*

### The same bug is easier to find once the code is cut into named parts

The lecture started with a Bug Hunt: half the room got a page written as one long component, the other half the same page with its rows extracted into their own components. The bug was the same in both: the *Leave* button called `onShare`. In the long version, one person found it. A week earlier, an AI agent had written exactly that long version for me; it took five or six rounds of "I don't understand this, refactor it" before I could read it, and only then could I ask whether all that complexity was needed at all. Much of it was not.

### `useLoadingFromDB` was written because a TA pushed for it

The plan was to stop at `useList`. Konstantina asked for the general version, and we wrote it live. While I typed, it was pointed out that the hook no longer knew when to load again, which is how `dbObjectId` became its second parameter. One person types and the other sees the bugs: that is the argument for pair programming.

### A hook gets its own file, even when it is five lines long

One of you asked why each hook gets a file in `src/hooks/`. For the same reason components and services have their folders: when you need one, you know where to look, and you can see whether it exists already. A five-line file next to a 300-line component is fine; the file does not care how long it is, only that what is in it belongs together. One `databaseHooks.js` with all of them in it is also fine. Keeping a codebase in order is less like architecture than like cleaning your room.

## Exam Questions

### 1. What makes a function a custom hook? What changes if you rename `useList` to `getList`?

### 2. Why should a custom hook return data rather than JSX?

### 3. Write `useInterval(callback, milliseconds)`. What happens if you leave out the function that `useEffect` returns?

### 4. Give two reasons to extract a custom hook that only one component uses.

### 5. Why is `useLoadingFromDB(loadList(listId), listId)` wrong, and why does `useLoadingFromDB(loadMyLists)` work without `() =>`?

## References

- [Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks), react.dev
- David L. Parnas, [On the Criteria To Be Used in Decomposing Systems into Modules](https://dl.acm.org/doi/10.1145/361598.361623), *Communications of the ACM*, 1972: the paper behind "hide each decision likely to change"
