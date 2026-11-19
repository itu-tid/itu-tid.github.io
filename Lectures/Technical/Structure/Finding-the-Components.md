# Finding the Components

You know how to write a component. The harder question is which ones to write, and the answer is not obvious from the code, because at that point everything is already one big `return`.

So answer it on the screen instead. Draw boxes around the parts of the running interface, and name each box. It works both ways round: on a screen you have not built yet, and on one that already runs and has grown hard to read.

## Start by drawing boxes on the app you can already see

Here is the home page of `todo-26`, as it runs after [Pulling Out the Service Layer](Pulling-Out-the-Service-Layer.md):

```
┌─ Home ────────────────────────────────────────────────┐
│ My lists                                              │
│ ┌─ MyListRow ───────────────────────────────────────┐ │
│ │ Groceries   ┌─ AddForm ─────────────────────────┐ │ │
│ │             │ [_______] [Share with (username)] │ │ │
│ │             └───────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────────┘ │
│ ┌─ MyListRow ───────────────────────────────────────┐ │
│ │ Exam prep   ┌─ AddForm ─────────────────────────┐ │ │
│ │             │ [_______] [Share with (username)] │ │ │
│ │             └───────────────────────────────────┘ │ │
│ └───────────────────────────────────────────────────┘ │
│                                                       │
│ Shared with me                                        │
│ ┌─ SharedListRow ───────────────────────────────────┐ │
│ │ Trip to Rome   shared by armin   [Leave]          │ │
│ └───────────────────────────────────────────────────┘ │
│                                                       │
│ List Manager                                          │
│ ┌─ AddForm ─────────────────────┐                     │
│ │ [__________] [New list]       │                     │
│ └───────────────────────────────┘                     │
│ Account                                               │
│ [Logout]                                              │
└───────────────────────────────────────────────────────┘
```

Boxes inside boxes give you the hierarchy for free:

```
Home
├── MyListRow        (one per list I own)
│   └── AddForm      (share it)
│       └── TextInput
├── SharedListRow    (one per list shared with me)
└── AddForm          (a new list)
    └── TextInput
```

The labels are your names for the boxes, not anything the user sees.

Notice what is *not* a box. The *My lists* heading, the *Logout* button and the *Leave* button are drawn but unnamed: each appears in exactly one place. **Draw a box when the same thing appears more than once.** `MyListRow` appears once per list, `SharedListRow` once per membership, and `AddForm` three times on this page alone, and once more on every list's page, for a new to-do.

That is the stopping rule, and you need one, because without it you can keep subdividing until every `<span>` is a component. *My lists* plus the rows under it would make a fine-sounding `MyLists` component, and it would be used exactly once. When you are unsure, leave it where it is: pulling a component out later is a five-minute job, and one you did not need is permanent clutter.

That is the whole exercise, and it takes two minutes on paper.

> **In todo-26:** `git checkout week-08-components`, and compare `Home.jsx` with the one in `week-08-service-layer`. The two rows moved out into `MyListRow.jsx` and `SharedListRow.jsx`; the rest of the page stayed where it was.

## Two boxes if either half would be useful on its own

It is not about how many parts the thing has. `AddForm` is a text input *and* a button, and it is rightly one box: a button with nothing to submit is useless, and a field with no way to submit it is useless. Two parts, one job.

So the test is: **would either half be useful on its own? If yes, make them two. If neither means anything without the other, they are one.**

Then name it as a **thing, not an action**. A component is something on the screen, so it gets a noun: `MyListRow`, `SharedListRow`, `AddForm`. Functions that *do* something get the verb: `handleShare`, `onLeave`. If you find yourself writing `ShareList` as a component, you have named the button's job rather than the thing on the page.

A name also has to fit every place the thing is used. The form began, in [Forms and Controlled Components](../React/Forms-and-Controlled-Components.md), as `NewTodoForm`. Then it started creating lists, and then sharing them, and `NewTodoForm` with `buttonLabel="Share with (username)"` was a lie. It is `AddForm` now: a form that adds whatever its caller says.

- `MyListRow` — draws one of my lists. One box.
- `SharedListRow` — draws one list somebody shared with me. One box.
- `AddForm` — an input and a button, neither any use without the other. Still one box.

### The common way to fail is welding the page's heading into a component that does not need it

`todo-26` still has one. `ToDoList` draws the to-dos and the form to add one, and, at the top, the page's title:

```jsx
export default function ToDoList({ list }) {
  let h1Style = { color: "deeppink", backgroundColor: "white" };
  // …
  return (
    <>
      <h1 style={h1Style}>{list.get("name")}</h1>
      {/* … the to-dos, and the AddForm … */}
    </>
  );
}
```

Want the list without the big pink title, say as a preview of the first few to-dos on the home page? Want a share button next to the title, on the list's page? You cannot have either, because they were glued together before anybody asked.

**Both halves would be useful alone, and that is the whole argument.** It is the exact opposite of `AddForm`, where neither half would be. Notice too that the name gave nothing away: `ToDoList` sounds like one thing, and it is one thing plus a heading.

The heading belongs to the page. Split, `ListPage` says what goes on it, and `ToDoList` draws only the list:

```jsx
// in ListPage
<>
  <h1>{list.get("name")}</h1>
  <ToDoList key={list.id} list={list} />
</>
```

Two boxes on the drawing, two components in the file. This one is left for you: in `todo-26` it is a two-line pull request.

Two other signals, both visible on the drawing rather than in the code:

**It repeats.** `MyListRow` appears once per list. Anything you would draw more than once is a component.

**It matches the data.** Notice that the two kinds of row are the two kinds of thing `App` loads: `lists`, rows of the `List` class, and `memberships`, rows of `ListMember`. One component per kind of row. When the component hierarchy and the data have the same shape, the code is usually easy; when they disagree, something is being forced. Try drawing one `ListRow` for both, and it fills up with `if (membership)`.

## Extracting a component is moving JSX out and naming what it needs

Here is `Home` with the shared lists still inline:

```jsx
{memberships.map((membership) => (
  <p key={membership.id}>
    <Link to={`/lists/${membership.get("list").id}`}>
      {membership.get("list").get("name")}
    </Link>{" "}
    shared by{" "}
    {membership.get("list").get("owner")?.get("username") ?? "someone"}{" "}
    <button onClick={() => onLeave(membership)}>Leave</button>
  </p>
))}
```

Cut the `<p>` out, and look at what it uses that it did not define itself: `membership`, from the `map`, and `onLeave`, from `Home`'s props. **Everything the moved JSX referenced from outside itself has to become a prop.**

```jsx
export default function SharedListRow({ membership, onLeave }) {
  const list = membership.get("list");

  return (
    <p>
      <Link to={`/lists/${list.id}`}>{list.get("name")}</Link>{" "}
      shared by {list.get("owner")?.get("username") ?? "someone"}{" "}
      <button onClick={() => onLeave(membership)}>Leave</button>
    </p>
  );
}
```

The `key` stays behind. It is for the `map`, which tells one row from the next, not for the row:

```jsx
{memberships.map((membership) => (
  <SharedListRow key={membership.id} membership={membership} onLeave={onLeave} />
))}
```

Once it had a name of its own, `membership.get("list")`, said three times, became one `const`. That kind of small tidying is easier once the code is in a box of its own, where you can see all of it at once.

### A component around an input takes what the input takes

The same move works one level down. `AddForm` used to hold its `<input>` inline, as in [Forms and Controlled Components](../React/Forms-and-Controlled-Components.md):

```jsx
function AddForm({ onAdd, buttonLabel = "Add New Task" }) {
  const [task, setTask] = useState("");
  // …
  return (
    <form onSubmit={onButtonClick}>
      <input type="text" value={task} onChange={(e) => setTask(e.target.value)} />
      <button type="submit" disabled={task.length === 0}>{buttonLabel}</button>
    </form>
  );
}
```

The `<input>` references the value and the change handler, so those become props:

```jsx
export default function TextInput({ value, onChange }) {
  return (
    <input
      type="text"
      value={value}
      onChange={(event) => onChange(event.target.value)}
    />
  );
}
```

One line inside `TextInput` does more than move: `onChange={(event) => onChange(event.target.value)}` unwraps the event and passes up a plain string. Write `onChange={onChange}` instead and the parent gets an event object where it expected text. That is the commonest way an extraction like this goes wrong.

The state stays where it was; `TextInput` has none of its own:

```jsx
<TextInput value={task} onChange={setTask} />
```

`useState` did not move into `TextInput`. If it had, `AddForm` would have no idea what was typed, and could never clear the field or submit the task. `TextInput` displays what it is given and reports what happened; it remembers nothing between renders.

Two things improved, and neither is about saving typing.

**The parent stopped touching `event.target.value`.** `TextInput` unwraps the event and hands up a plain string, so `AddForm` can pass `setTask` directly. The parent now works in the language of the app instead of the language of the DOM.

**There is one place to change how inputs look.** A `className`, a placeholder, anything you add later, lives here rather than in every screen that happens to need typing.

And look at the shape of it: `TextInput` takes the value it should show, and a way to report that something changed. Exactly what the raw `<input>` takes, under the same names. The pattern travelled up a level without changing, so the word travels with it: a **controlled component** is any component whose important state is held by its parent, exactly as a [controlled input](../React/Forms-and-Controlled-Components.md) is an input whose value is held by the component around it.

## Exam Questions

### 1. `AddForm` holds an input and a button and is one component. `ToDoList` holds the list's heading and its to-dos and should be two. What is the difference?

### 2. What is wrong with a component that renders a to-do heading *and* accepts arbitrary `children`?

### 3. `TextInput` holds no state of its own. Why not, and what would break if it did?

### 4. Why does todo-26's home page have a `SharedListRow` component, but no `MyLists` component?


## References

- [Thinking in React](https://react.dev/learn/thinking-in-react) — the five steps, of which the first is the one worth keeping
- [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components) — once a component has its own name it usually wants its own file

**Next**: deciding *where the state lives* once you have pulled components out is its own problem, and extraction is what creates it: lifting state up, in [Extracting Components and Where the State Goes](../React/Extracting-Components-and-Where-the-State-Goes.md#siblings-share-state-through-a-parent-of-both).
