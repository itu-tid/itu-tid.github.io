# Finding the Components

You know how to write a component. The harder question is which ones to write — and the answer is not obvious from the code, because at that point everything is already one big `return`.

So do it on the screen instead, before you touch the editor. Draw boxes around the parts of the interface, and name each box.

## The to-do, boxed

```
┌─ TodoApp ─────────────────────────────┐
│                                       │
│  ┌─ AddTodo ─────────────────────┐    │
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
├── AddTodo
│   └── TextInput
└── TodoList
    └── TodoItem   (one per to-do)
```

That is the whole exercise, and it takes two minutes on paper. It is worth doing precisely because it is not a coding activity — you are looking at what the thing *is*, not at what you have already typed.

## What earns a box

The same test as for a function: **it does one thing, and you can name it without using "and".**

- `TodoItem` — draws one to-do. ✅
- `TodoList` — draws all of them. ✅
- `TodoListAndForm` — two things, wearing a raincoat. ❌ Two boxes.

Two other signals, both visible on the drawing rather than in the code:

**It repeats.** `TodoItem` appears once per to-do. Anything you would draw more than once is a component, because otherwise you will copy the markup and then have to remember to change every copy.

**It matches the data.** Notice that the tree above looks like the array it renders: a list of things, and a thing. When the component hierarchy and the data have the same shape, the code is usually easy; when they disagree, something is being forced.

## What not to take from this

React's [Thinking in React](https://react.dev/learn/thinking-in-react) presents the boxes as step one of five, and the next step is *build the whole static version first, with no state at all, then add interactivity*.

Treat that as a description of a finished thought rather than a way of working. Nobody builds an entire inert interface and then goes back to bring it to life, and you certainly will not once your app already runs. What you will do — repeatedly, all term — is notice that a `return` has grown too long to read, box up the part that has its own name, and pull it out.

The drawing is worth keeping. The five-step ceremony around it is not.
