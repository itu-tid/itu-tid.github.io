# Patterns of Component Communication
## parent to child = via props

- parent can send information to the child via props

## child to parent = via callbacks
- child does not even know who the parent is (imagine a button, it does not know, and it should not know who uses it)
- but the parent will give it callbacks and it can call them, effectively communicating to the parent

![](../images/props-and-callbacks.png)

**Next**: once you extract components, two of them end up needing the same state, and neither owns it. That is *lifting state up*, and it is in [Refactoring by Extracting Components](../Structure/Refactoring-by-Extracting-Components.md) — because extraction is what creates the problem in the first place.


## Exam Questions

### 1. Explain the three patterns of component communication in React.


# Worked example: deleting an item

The to-do list is the clearest case there is, because the two halves genuinely live in different components.

`TodoList` owns the array. `TodoItem` draws one row — and the delete button belongs on the row, because that is where it makes sense to a user. But the row **cannot delete itself**: it does not own the list, and it has no way to reach it. All it can do is say *this one*, and let whoever owns the list decide what that means.

```jsx
function TodoList() {
  const [todos, setTodos] = useState([]);

  function handleRemove(id) {
    setTodos(todos.filter((t) => t.id !== id));
  }

  return (
    <ul>
      {todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} onRemove={handleRemove} />
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
- **Up, as a callback.** `TodoItem` is handed `onRemove` and calls it. It does not know what happens next, and that is the point: it is not deleting anything, it is *reporting a click*.

`TodoItem` knows nothing about `filter`, about the array, or even that a list exists. Drop it into a different app that also passes an `onRemove` and it works unchanged. That is what you get for keeping the arrow pointing one way.

### The mistake to avoid

The tempting shortcut is to pass `setTodos` down and let the row remove itself:

```jsx
<TodoItem todo={todo} todos={todos} setTodos={setTodos} />   // ❌
```

It works. It also means every row now knows the whole list, and the shape of it, and how deletion is implemented — so changing any of those means changing the row too. You have swapped one small prop for three, and gained a component that only works in this app.

**Hand down what the child needs to know, and a way to tell you something happened. Nothing else.**

