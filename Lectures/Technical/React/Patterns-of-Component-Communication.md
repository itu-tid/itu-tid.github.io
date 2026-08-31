# Patterns of Component Communication

Components are arranged in a tree, and information has to travel along it. There are only two directions, and they use different mechanisms.

## Data goes down, as props

The parent hands the child what it needs to draw itself. Data goes down.

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
