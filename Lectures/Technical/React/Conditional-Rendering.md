# Conditional Rendering

A component returns JSX. Which JSX it returns can depend on what is in state, or on what it was handed as props — so the screen changes shape rather than only changing its contents.

You need this the moment the app can be in more than one situation, which is sooner than it sounds. A to-do list that can be added to and deleted from can also be **empty**, and an empty `<ul>` on screen looks like a bug rather than an achievement:

```jsx
{todos.length === 0 && <p>Nothing to do. Enjoy the afternoon.</p>}
```

There are three ways to write one, and to see what actually differs between them it is worth writing the *same* thing three times. Here is a to-do row that should look different once it is done.

**1. An `if`, before the `return`** — when the two versions are different enough to be worth reading separately:

```jsx
function TodoItem({ text, done }) {
  if (done) {
    return <li className="done"><s>{text}</s></li>;
  }
  return <li>{text}</li>;
}
```

**2. The `? :` operator**, inside the JSX — when only a small part changes, and repeating the whole `<li>` would hide how little that is:

```jsx
function TodoItem({ text, done }) {
  return <li className={done ? "done" : ""}>{done ? <s>{text}</s> : text}</li>;
}
```

**3. `&&`** — when there is genuinely nothing to show in the other case, so a `? :` would end in an awkward `: null`:

```jsx
function TodoItem({ text, done }) {
  return (
    <li>
      {text} {done && <span aria-label="done">✓</span>}
    </li>
  );
}
```

They are not three styles of the same thing. `if` and `? :` both answer *which of these two*, and `&&` answers *is there anything here at all* — which is why the empty-list message above is written with `&&` and could not sensibly be written any other way.

A warning about that last one. `&&` returns its **left** side when the left side is falsy — so `{todos.length && <p>…</p>}` renders a literal **0** on the page when the list is empty, because `0` is falsy but is still something React will happily display. Compare explicitly (`=== 0`, `> 0`) and the problem disappears.

Note:
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation.

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*


# References

- *Describing the UI* > [Conditional Rendering](https://react.dev/learn/conditional-rendering)


## Exam Questions

### 1. Give the three ways of rendering conditionally, and say when you would reach for each.

### 2. `{todos.length && <p>Nothing to do</p>}` puts a `0` on the screen. Why, and how do you fix it?

### 3. Which of the three cannot express an *else*, and what does that tell you about when to use it?
