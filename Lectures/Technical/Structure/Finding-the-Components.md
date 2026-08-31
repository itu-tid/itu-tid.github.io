# Finding the Components

You know how to write a component. The harder question is which ones to write — and the answer is not obvious from the code, because at that point everything is already one big `return`.

So answer it on the screen instead. Draw boxes around the parts of the running interface, and name each box. It works both ways round: on a screen you have not built yet, and on one that already runs and has grown hard to read.

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

The labels are your names for the boxes, not anything the user sees. Boxes inside boxes give you the hierarchy for free.

Notice what is *not* a box. The **Add** button and the **×** are drawn but unnamed: each appears in one place, inside one component, and nobody else needs them. **Draw a box when the thing repeats, or when something else will want it.** That is the stopping rule, and without one you can keep subdividing until every `<span>` is a component.

That is the whole exercise, and it takes two minutes on paper.

## A box earns its name if you can say what it does without "and"

The same test as for a function, with one refinement that matters: **say out loud what it draws. If the honest description needs an "and", it is two boxes — whatever you decided to call it.**

The name you chose will not catch you out, because you chose it. `ToDoPanel`, below, has no "and" in it and is still two components; described honestly it is *a to-do heading and a general-purpose container*, and there is the "and".

And name it as a **thing, not an action**. A component is something on the screen, so it gets a noun: `TodoList`, `TodoItem`, `NewTodoForm`. Functions that *do* something get the verb — `handleAdd`, `handleRemove`. If you find yourself writing `AddTodo` as a component, you have named the button's job rather than the thing on the page.

- `TodoItem` — draws one to-do. One box.
- `TodoList` — draws all of them. One box.
- `TodoListAndForm` — draws every to-do *and* collects a new one. Two boxes, and this one admits it in the name.

The commonest way to fail that test is to weld a **domain** component to a **layout** one — something that knows about to-dos *and* accepts arbitrary content:

```jsx
function ToDoPanel({ firstName, children }) { // two components
  return (
    <>
      <h1>To Do List for {firstName}</h1>
      <div className="panel">{children}</div>
    </>
  );
}
```

Neither half can be used without the other. Want the heading somewhere without a panel? Want a panel around something that is not a to-do list? You cannot have either, because they were glued together before anybody asked.

**Those two questions are the test.** Ask them of anything you suspect: *can I use this half without that half?* Two noes means two components.

Split, each half is usable on its own, and the caller says what it wants:

```jsx
function Panel({ children }) {
  return <div className="panel">{children}</div>;
}

// and at the call site — whatever goes between the tags arrives as `children`
<Panel>
  <h1>To Do List for {firstName}</h1>
  <TodoList todos={todos} />
</Panel>
```

Two boxes on the drawing, two components in the file.

Two other signals, both visible on the drawing rather than in the code:

**It repeats.** `TodoItem` appears once per to-do. Anything you would draw more than once is a component, because otherwise you will copy the markup and then have to remember to change every copy.

**It matches the data.** Notice that the tree above looks like the array it renders: a list of things, and a thing. When the component hierarchy and the data have the same shape, the code is usually easy; when they disagree, something is being forced.

## Extracting a component is moving JSX out and naming what it needs

Here is the form before anything is pulled out of it — the `<input>` from [Forms and Controlled Components](../React/Forms-and-Controlled-Components.md), sitting inline:

```jsx
function NewTodoForm({ onAdd }) {
  const [text, setText] = useState("");

  return (
    <input
      className="text-input"
      value={text}
      onChange={(e) => setText(e.target.value)}
      placeholder="What needs doing?"
    />
  );
}
```

`value` and `onChange` are ordinary props, so nothing stops you putting that input inside a component of your own. **Everything the moved JSX referenced from outside itself has to become a prop** — here the value, the change handler, and the placeholder:

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

One line inside `TextInput` does more than move: `onChange={(e) => onChange(e.target.value)}` unwraps the event and passes up a plain string. Write `onChange={onChange}` instead and the parent gets an event object where it expected text — the commonest way an extraction like this goes wrong.

The state stays where it was; `TextInput` has none of its own:

```jsx
function NewTodoForm({ onAdd }) {
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

(The submit button and `handleSubmit` are still there in the real component — left out here so that the extraction is the only change on the page.)

`useState` did not move into `TextInput`. If it had, `NewTodoForm` would have no idea what was typed, and could never clear the field or add the task. `TextInput` displays what it is given and reports what happened; it remembers nothing between renders.

Two things improved, and neither is about saving typing.

**The parent stopped touching `e.target.value`.** `TextInput` unwraps the event and hands up a plain string, so `NewTodoForm` can pass `setText` directly. The parent now works in the language of the app — a piece of text — instead of the language of the DOM.

**There is one place to change how inputs look.** The `className`, and anything you add later, lives here rather than in every screen that happens to need typing.

And look at the shape of it: `TextInput` takes the value it should show, and a way to report that something changed. Exactly what the raw `<input>` takes. The pattern travelled up a level without changing, so the word travels with it: a **controlled component** is any component whose important state is held by its parent — exactly as a [controlled input](../React/Forms-and-Controlled-Components.md) is an input whose value is held by the component around it.

## Do not build the whole static version first

React's [Thinking in React](https://react.dev/learn/thinking-in-react) presents the boxes as step one of five, and the next step is *build the whole static version first, with no state at all, then add interactivity*.

That advice assumes you are starting from a design with nothing built yet. You are not: your app already runs, and it will keep running all term. So treat the five steps as a description of a finished thought rather than a way of working. What you will actually do — repeatedly — is notice that a `return` has grown too long to read, box up the part that has its own name, and pull it out.

Steps three to five are about deciding where state should live. We get there a different way, by moving state when it hurts: [Refactoring by Extracting Components](Refactoring-by-Extracting-Components.md). The drawing is the part worth keeping.


## References

- [Thinking in React](https://react.dev/learn/thinking-in-react) — the five steps, of which the first is the one worth keeping
- [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components) — once a component has its own name it usually wants its own file

## Exam Questions

### 1. How do you decide what should be its own component?

### 2. What is wrong with a component that renders a to-do heading *and* accepts arbitrary `children`?

### 3. `TextInput` holds no state of its own. Why not, and what would break if it did?
