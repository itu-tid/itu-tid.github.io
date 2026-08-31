# Finding the Components

You know how to write a component. The harder question is which ones to write — and the answer is not obvious from the code, because at that point everything is already one big `return`.

So do it on the screen instead, before you touch the editor. Draw boxes around the parts of the interface, and name each box.

## Start by drawing boxes on the app you can already see

```
┌─ TodoApp ─────────────────────────────┐
│                                       │
│  ┌─ NewTodoForm ─────────────────┐    │
│  │  ┌─ TextInput ─────────┐      │    │
│  │  │ What needs doing?   │ [Add]│    │
│  │  └─────────────────────┘      │    │
│  └───────────────────────────────┘    │
│                                       │
│  ┌─ TodoList ────────────────────┐    │
│  │  ┌─ TodoItem ──────────────┐  │    │
│  │  │ Buy milk            [×] │  │    │
│  │  └─────────────────────────┘  │    │
│  │  ┌─ TodoItem ──────────────┐  │    │
│  │  │ Call the landlord   [×] │  │    │
│  │  └─────────────────────────┘  │    │
│  └───────────────────────────────┘    │
│                                       │
└───────────────────────────────────────┘
```

Boxes inside boxes give you the hierarchy for free:

```
TodoApp
├── NewTodoForm
│   └── TextInput
└── TodoList
    └── TodoItem   (one per to-do)
```

That is the whole exercise, and it takes two minutes on paper. Do it away from the editor: you are looking at what the thing *is*, not at what you have already typed.

## A box earns its name if you can say what it does without "and"

The same test as for a function: **it does one thing, and you can name it without using "and".**

And name it as a **thing, not an action**. A component is something on the screen, so it gets a noun: `TodoList`, `TodoItem`, `NewTodoForm`. Functions that *do* something get the verb — `handleAdd`, `handleRemove`. If you find yourself writing `AddTodo` as a component, you have named the button's job rather than the thing on the page.

- `TodoItem` — draws one to-do. ✅
- `TodoList` — draws all of them. ✅
- `TodoListAndForm` — two things, wearing a raincoat. ❌ Two boxes.

The commonest way to fail that test is to weld a **domain** component to a **layout** one — something that knows about to-dos *and* accepts arbitrary content:

```jsx
function ToDoPanel({ firstName, children }) {      // ❌ two components
  return (
    <>
      <h1>To Do List for {firstName}</h1>
      <div className="panel">{children}</div>
    </>
  );
}
```

Neither half can be used without the other. Want the heading somewhere without a panel? Want a panel around something that is not a to-do list? You cannot have either, because they were glued together before anybody asked. Two boxes on the drawing, two components in the file.

Two other signals, both visible on the drawing rather than in the code:

**It repeats.** `TodoItem` appears once per to-do. Anything you would draw more than once is a component, because otherwise you will copy the markup and then have to remember to change every copy.

**It matches the data.** Notice that the tree above looks like the array it renders: a list of things, and a thing. When the component hierarchy and the data have the same shape, the code is usually easy; when they disagree, something is being forced.

## Extracting a component is moving JSX out and naming what it needs

`value` and `onChange` are ordinary props, so nothing stops you putting that input inside a component of your own:

```jsx
function TextInput({ value, onChange, placeholder }) {
  return (
    <input
      className="text-input"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
    />
  );
}
```

The state stays where it was — `TextInput` has none of its own:

```jsx
function NewTodoForm() {
  const [text, setText] = useState("");

  return (
    <TextInput
      value={text}
      onChange={setText}
      placeholder="What needs doing?"
    />
  );
}
```

`useState` did not move into `TextInput`. If it had, `NewTodoForm` would have no idea what was typed, and could never clear the field or add the task. `TextInput` displays what it is given and reports what happened; it remembers nothing between renders.

Two things improved, and neither is about saving typing.

**The caller stopped touching `e.target.value`.** `TextInput` unwraps the event and hands up a plain string, so `NewTodoForm` can pass `setText` directly. The parent now works in the language of the app — a piece of text — instead of the language of the DOM.

**There is one place to change how inputs look.** The `className`, and anything you add later, lives here rather than in every screen that happens to need typing.

And look at the shape of it: `TextInput` takes the value it should show, and a way to report that something changed. Exactly what the raw `<input>` takes. The pattern travelled up a level without changing — which is why React reuses the word, and calls *any* component whose important state is held by its parent a controlled one.

## Do not build the whole static version first

React's [Thinking in React](https://react.dev/learn/thinking-in-react) presents the boxes as step one of five, and the next step is *build the whole static version first, with no state at all, then add interactivity*.

Treat that as a description of a finished thought rather than a way of working. Nobody builds an entire inert interface and then goes back to bring it to life, and you certainly will not once your app already runs. What you will do — repeatedly, all term — is notice that a `return` has grown too long to read, box up the part that has its own name, and pull it out.

The drawing is worth keeping. The five-step ceremony around it is not.


## References

- [Thinking in React](https://react.dev/learn/thinking-in-react) — the five steps, of which the first is the one worth keeping
- [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components) — once a component has its own name it usually wants its own file

## Exam Questions

### 1. How do you decide what should be its own component?

### 2. What is wrong with a component that renders a to-do heading *and* accepts arbitrary `children`?

### 3. `TextInput` holds no state of its own. Why not, and what would break if it did?
