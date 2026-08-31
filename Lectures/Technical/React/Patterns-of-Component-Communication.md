# Patterns of Component Communication

Components are arranged in a tree, and information has to travel along it. There are only two directions, and they use different mechanisms.

## A to-do has to become an object before any of this works

Last week a to-do was a **string**, and the list was drawn straight from it:

```jsx
const [todos, setTodos] = useState(["Buy milk", "Call the landlord"]);
```

That is enough right up until something can be removed. To delete one row you have to say *which* row, and a string cannot say — two people can both put "Buy milk" on the list, and [the index is not an answer either](Intro-to-React.md#every-item-needs-a-key), because the index of everything after the deleted row changes.

So each to-do becomes an object carrying its own name:

```jsx
const [todos, setTodos] = useState([]);   // each one is { id, text, done }

function handleAdd(text) {
  setTodos([...todos, { id: crypto.randomUUID(), text, done: false }]);
}
```

`crypto.randomUUID()` is built into the browser and needs no library. A counter that goes up by one works just as well.

**The id is made once, when the to-do is made** — not worked out while rendering. That is the whole point of it: a key has to name the *same* item on every render, and anything computed at render time is a new answer each time. This is the one place in the course where deriving a value instead of storing it is the wrong move.

That `handleAdd` is also the missing half of the form from [Forms and Controlled Components](Forms-and-Controlled-Components.md). The form calls `onAdd(text)` with a string, because typing a name is all a form knows how to do; turning that string into a to-do is the list's job, and this is where it happens:

```jsx
<NewTodoForm onAdd={handleAdd} />
```

## Data goes down, as props

The parent hands the child what it needs to draw itself — for a row, the `todo` object above. Data goes down.

## Events come back up, as callbacks

The child does not know who its parent is — and should not. Imagine a button: it has no idea who put it there, and it would be a worse button if it did.

What it does have is a function it was handed. Calling it is how the child says *something happened*, without knowing or caring what that means:

```jsx
function TodoList() {
  const [todos, setTodos] = useState([]);

  function handleRemove(id) {
    setTodos(todos.filter((t) => t.id !== id));
  }

  return (
    <ul>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}          // down: what to draw
          onRemove={handleRemove}   // up: a way to report a click
        />
      ))}
    </ul>
  );
}

function TodoItem({ todo, onRemove }) {
  return (
    <li>
      {todo.text}
      <button onClick={() => onRemove(todo.id)}>×</button>
    </li>
  );
}
```

Read the two directions:

- **Down, as props.** `TodoList` hands each row its `todo` — the data it needs to draw.
- **Up, as a callback.** `TodoItem` is handed `onRemove` and calls it. It does not know what happens next: it is not deleting anything, it is *reporting a click*.

`TodoItem` knows nothing about `filter`, about the array, or even that a list exists. Drop it into an app that archives items instead of deleting them, passing the same `onRemove`, and it works unchanged. That is what you get for keeping the arrow pointing one way.

## Passing `setTodos` down gives every row power over the whole list

The tempting shortcut is to pass `setTodos` down and let the row remove itself:

```jsx
<TodoItem todo={todo} todos={todos} setTodos={setTodos} />   // do not do this
```

It works. It also means every row now knows the whole list, and the shape of it, and how deletion is implemented — so changing any of those means changing the row too. You have swapped one small prop for three, and gained a component that only works in this app.

**Hand down what the child needs to know, and a way to tell you something happened. Nothing else.**

**Next**: once you extract components, two of them end up needing the same state, and neither owns it. That is *lifting state up*, and it is in [Refactoring by Extracting Components](../Structure/Refactoring-by-Extracting-Components.md) — because extraction is what creates the problem in the first place.


## Exam Questions

### 1. What are the two directions information travels between components, and what carries each?

### 2. `TodoItem` has a delete button but cannot delete anything. Why is that the right arrangement?

### 3. What goes wrong if you pass `setTodos` to every row instead of an `onRemove` callback?

### 4. Last week a to-do was a string. Why can the list not stay that way once rows can be deleted?

### 5. Why is a to-do's `id` created in `handleAdd` rather than worked out while rendering? Everywhere else the course tells you to derive rather than store.
