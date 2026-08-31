# Conditional Rendering

A component returns JSX. Which JSX it returns can depend on what is in state, or on what it was handed as props — so the screen changes shape rather than only changing its contents.

You need this the moment the app can be in more than one situation, which is sooner than it sounds. A to-do list that can be added to and deleted from can also be **empty**, and an empty `<ul>` on screen looks like a bug rather than an achievement. So the list needs to say something else when there is nothing in it.

There are three ways to write that. Here they all are on the same condition, because writing the same thing three times is the only way to see what differs between the forms rather than between the examples.

**1. An `if`, before the `return`** — the one you already know from every other language you have written. Best when the two versions are different enough to be worth reading separately:

```jsx
function TodoList({ todos }) {

  if (todos.length === 0) {
    return <p>Nothing to do. Enjoy the afternoon.</p>;
  }

  return (
    <ul>
      {todos.map((todo) => <TodoItem key={todo.id} todo={todo} />)}
    </ul>
  );
}
```

**2. The `? : ` operator**, inside the JSX — when the surrounding markup is shared and repeating it would hide how little actually changes:

```jsx
function TodoList({ todos }) {
  return (
    <section>
      <h2>Today</h2>
      {todos.length === 0
        ? <p>Nothing to do. Enjoy the afternoon.</p>
        : <ul>{todos.map((todo) => <TodoItem key={todo.id} todo={todo} />)}</ul>}
    </section>
  );
}
```

**3. `&&`** — when there is genuinely nothing to show in the other case:

```jsx
function TodoList({ todos }) {
  return (
    <section>
      {todos.length === 0 && <p>Nothing to do. Enjoy the afternoon.</p>}
      <ul>{todos.map((todo) => <TodoItem key={todo.id} todo={todo} />)}</ul>
    </section>
  );
}
```

The first two **choose between two things** — you get the message *or* the list. The third **adds a thing, or does not** — the `<ul>` is always rendered, and it happens to be invisible when empty.

So they are not three styles of one thing. `if` and `? :` answer *which of these two*; `&&` answers *is there anything here at all*. Reach for `&&` when a `? :` would have to end in an awkward `: null`.

A warning about that last one. `&&` returns its **left** side when the left side is falsy — so `{todos.length && <p>…</p>}` renders a literal **0** on the page when the list is empty, because `0` is falsy but is still something React will happily display. Compare explicitly (`=== 0`, `> 0`) and the problem disappears.

Note:
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation.

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*


## References

- *Describing the UI* > [Conditional Rendering](https://react.dev/learn/conditional-rendering)


## Exam Questions

### 1. Give the three ways of rendering conditionally, and say when you would reach for each.

### 2. `{todos.length && <p>Nothing to do</p>}` puts a `0` on the screen. Why, and how do you fix it?

### 3. Which of the three cannot express an *else*, and what does that tell you about when to use it?
