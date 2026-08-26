# React

React is a JavaScript **library** for building interactive **single page applications**. We will talk about what Single Page Applications are and how they work in a different lecture. For now, we want to be users of react so we'll start doing a very simple application in it and learn React on the way.

We build a to-do list as we go. Each section below is the smallest step that makes the
previous step's problem go away, so the page reads in the order the app needs — and each
one opens by saying what the app does at that point.

## React is a ***component-based*** UI library

### Everything in React is a component

### Components are **JS functions** that return JSX elements

[Example](https://react.dev/learn/your-first-component#defining-a-component) of a React component :

```js
export default function ToDoList() {
  const name = "Mircea";
  
  return (
    <>
      <h1>Remember {name}:</h1>
      <ul>
        <li>Buy bread</li>
        <li>Buy milk</li>
      </ul>
    </>
  )
}

```

## JSX is a combination of JS and HTML

**The app now.** The same heading, wrapped in a little markup — and the first surprise, because that markup is not quite HTML.

JSX is acronym for JavaScript + XML

### JSX is a **syntax extension** that provides template-like declarative UI description within JavaScript itself
- syntax extension for Javascript! 
- has the full power of JS inside of the {}
- template-like because it looks like other other front-end JS frameworks (e.g., [Vue templates](https://www.freecodecamp.org/news/reacts-jsx-vs-vue-s-templates-a-showdown-on-the-front-end-b00a70470409/)) and server-side rendering frameworks (e.g. Jinja for Flask, Moustache)
- HTML-like code within JavaScript
- JSX is **transpiled** to Javascript 

### JSX has a **stricter syntax than HTML**
#### A component can only ever return a single JSX tag 

Otherwise, [you get an error](https://react.dev/learn/writing-markup-with-jsx#1-return-a-single-root-element).

```js
// This won't work - multiple top-level elements
return (
  <h1>Title</h1>
  <p>Paragraph</p>
)

// This works but adds unnecessary <div>
return (
  <div>
    <h1>Title</h1>
    <p>Paragraph</p>
  </div>
)

// This works without extra DOM node
return (
  <>
    <h1>Title</h1>
    <p>Paragraph</p>
  </>
)
```
this is called  = a fragment. 

Solution is to use a Fragment when you don't need an actual HTML element as parent
#### Tags must [always be closed](https://react.dev/learn/writing-markup-with-jsx#2-close-all-the-tags) 

### JSX converts most HTML and CSS attributes to camelCase 
#### HTML event handlers, e.g. `onclick` becomes `onClick`
#### CSS attributes, e.g. `background-color` becomes `backgroundColor`
#### Special JS keyword `class` becomes `className`

Two [minor exceptions](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things) from this rule.




## Interpolating JS in JSX

**The app now.** The heading counts: *My To-Do (3)*. The number has to come from JavaScript, and it has to land inside the markup.

Curly brackets to escape JS inside JSX can be used in three ways
### As **inline inside of HTML text**

```js
return (
  <>
    <h1>Hello {user.firstName + user.LastName}</h1>
    <p>Today is: {todaysDate}</p>
  </>
);
```

### As **attributes immediately following the `=` sign**
```js
return (
  <img
    className="avatar"
    src={user.imageUrl}
  />
);

```

### Special case of attributes: **[double curlies](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx) for objects**
```js
export default function TodoList() {
  return (
    <ul style={{
		  backgroundColor: 'black',
	      color: 'pink'
	    }}>
      <li>Improve the videophone</li>
      <li>Prepare aeronautics lectures</li>
      <li>Work on the alcohol-fuelled engine</li>
    </ul>
  );
}

```

## Parameterizing Components

**The app now.** One `<TodoItem text="Buy milk" />`. Writing a second one by hand would mean copying the whole component, so it has to take its text from outside.

### A component is a function

Functions can be parameterized, so components should be parameterizable too.

### Component parameters are called **`props`** in React
- the term very likely comes from properties

### Props are passed on normally as HTML attributes

- In the moment when the *props* are [passed to the component](https://react.dev/learn/passing-props-to-a-component#step-1-pass-props-to-the-child-component), they *look* like HTML attributes -- have the same syntax

### Props are used in the component definition as the `props` parameter 
- In the component definition the props are accessed as either
	- a single function parameter named `props`

### You can be more explicit using a [destructured](https://react.dev/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component) dictionary in the component definition
- makes code easier to read and write


### With the `{children}` prop

Props pass **data** into a component. `children` passes **markup** into it — everything
written between the opening and closing tags.

Start without it. A panel that takes its content as an ordinary prop:

```jsx
function Panel({ title, text }) {
  return (
    <section className="panel">
      <h2>{title}</h2>
      <p>{text}</p>
    </section>
  );
}

<Panel title="Today" text="Nothing due." />
```

That works exactly as long as the content is one string. The moment you want a list inside
the panel, or a button, or another component, you are stuck: you cannot put a `<ul>` inside
a string. You would end up adding `items`, then `buttonLabel`, then `showIcon`, and the
panel would slowly learn about everything that might ever go in it.

`children` is the way out. The component stops describing its content and only describes
its *frame*:

```jsx
function Panel({ title, children }) {
  return (
    <section className="panel">
      <h2>{title}</h2>
      {children}
    </section>
  );
}
```

Now the same component takes anything:

```jsx
<Panel title="Today">
  <ul>
    <li>Buy milk</li>
    <li>Call the landlord</li>
  </ul>
</Panel>

<Panel title="Nothing due">
  <p>Enjoy the afternoon.</p>
  <button>Add something anyway</button>
</Panel>
```

Note what `Panel` does **not** know: that there is a list, that there is a button, that
either exists. It knows it has a title and a frame to draw around whatever it was handed.
That is the whole idea, and it is why almost every layout component you write — containers,
cards, modals, page wrappers — ends up taking `children`.

> **The rule of thumb.** If it is data the component needs to *use* — a title, a count, a
> user — make it a prop. If it is markup the component only needs to *place*, use
> `children`.

## Rendering Lists

**The app now.** Three items, drawn from an array rather than typed out. Which is the point: the array is the app, and the screen is a picture of it.

Most applications sooner or later rely on lists of things that you want to process. 

### In React, to render lists you rely on `for` loops and  `array.map()`

Our three hardcoded `<TodoItem />`s become one array and one `map`:

```jsx
const todos = ["Buy milk", "Call the landlord", "Book the dentist"];

function TodoList() {
  return (
    <ul>
      {todos.map((text, index) => (
        <TodoItem key={index} text={text} />
      ))}
    </ul>
  );
}
```

`map` turns an array of **strings** into an array of **JSX elements**, and React renders an
array of elements by rendering each one. That is the whole mechanism. Add a fourth string
to `todos` and a fourth row appears; nothing else has to change.

### You must use a `key` attribute for every element in a list
- must be unique **among its siblings**
- can be the database ID, UUID, or anything else stable
- it is how React tells the items apart between renders — without it, it cannot know
  whether you added a row, removed one, or reordered them
- if you don't do this, your console fills up with warnings

We are using the array **index** above, which is the thing every beginner reaches for and
which works perfectly — until items can be removed from the middle. Delete the first of
three, and the item that was index 1 becomes index 0: React sees "the thing with key 0
changed its text" rather than "the first thing is gone". Next week adds delete, you will
watch exactly that go wrong, and that is when we swap indexes for real IDs.

Nice examples of rendering lists and filtering at: *Describing the UI* > [Rendering Lists](https://react.dev/learn/rendering-lists). Also nice exercises at the bottom of the page.

## Event Handling

**The app now.** An **Add** button that does nothing at all. Making it do something is the next two sections.

### Interactive apps must handle events: click, type, mouse move, screen touch, etc. 

This is the main job of your UI app.

### Event handlers are defined inside components
### Handlers have usually names starting with `handle`... 
### Built-in components (e.g. `<button>`) support built-in events (e.g. `onClick`, etc.).

Associating event handlers with events is done with the attribute in curly brackets syntax, as above. (See [onClick example](https://react.dev/learn/responding-to-events#adding-event-handlers).)

Our button, doing nothing useful yet:

```jsx
function TodoList() {
  function handleAdd() {
    console.log("Add was clicked");
  }

  return (
    <>
      <ul>
        {todos.map((text, index) => <TodoItem key={index} text={text} />)}
      </ul>
      <button onClick={handleAdd}>Add</button>
    </>
  );
}
```

#### WARNING: You must know the difference between calling a function and passing it as a reference!

```jsx
<button onClick={handleAdd}>Add</button>     // ✅ hands React the function
<button onClick={handleAdd()}>Add</button>   // ❌ calls it now, hands React the result
```

The second one runs `handleAdd` while the component is *rendering*, before anybody has
clicked anything, and gives `onClick` whatever it returned — usually `undefined`. If your
handler fires once on load and never again, this is why.

### **Event handlers always receive an event as argument**

The `event` argument details info about what just happened. 
- Sometimes you can ignore it, 
- Sometimes you inspect it to learn about the event (e.g. mouse position, element that was clicked, etc. )

### Events propagate (*bubble up*) the DOM tree (advanced)

If you have an `onClick` handler on both a button and a containing div, both will be handled in sequence, from the inner one outwards. [See event propagation example](https://react.dev/learn/responding-to-events#event-propagation). 

- Sometimes you can change the behavior of the event by calling `stopPropagation` or `preventDefault` on the event object. [example of stop propagation](https://react.dev/learn/responding-to-events#stopping-propagation) and of [preventing default behavior](https://react.dev/learn/responding-to-events#preventing-default-behavior). 

## Component State

**The app now. This is the one to slow down for.** Add pushes a task onto the array — and nothing appears. The variable really did change; the screen simply does not care. That failure is the whole argument for state, and it is far more convincing having just watched it fail.

### Every component can store local state 

Unlike the props, the state can be changed from within the component.

First, the version that does **not** work — worth typing out, because the reason it fails
is the reason state exists:

```jsx
const SAMPLE_TASKS = ["Buy milk", "Call the landlord", "Book the dentist",
                      "Water the plants", "Reply to Mette"];

function randomTask() {
  return SAMPLE_TASKS[Math.floor(Math.random() * SAMPLE_TASKS.length)];
}

let todos = ["Buy milk"];          // ❌ an ordinary variable

function TodoList() {
  function handleAdd() {
    todos.push(randomTask());
    console.log(todos);            // the array really does grow — look at the console
  }
  // …and the screen never changes
}
```

The array grows. The console proves it. The screen ignores you completely, because nothing
told React that anything happened — it only re-runs your component when you ask it to, and
pushing onto a variable is not asking.

### Local state is defined using the `useState` hook 

The `useState` hook: 
- takes an **initial** value
- returns **current value** and a **setter function**

```jsx
import { useState } from "react";

function TodoList() {
  const [todos, setTodos] = useState(["Buy milk"]);

  function handleAdd() {
    setTodos([...todos, randomTask()]);   // a *new* array, not a push
  }

  return (
    <>
      <ul>
        {todos.map((text, index) => <TodoItem key={index} text={text} />)}
      </ul>
      <button onClick={handleAdd}>Add</button>
    </>
  );
}
```

Two things changed, and both matter:

- `todos` now comes from `useState`, so it survives between renders. A plain `let` inside
  the component would be created fresh every time React called the function.
- `setTodos` is given a **new array** — `[...todos, randomTask()]` — rather than the old
  one mutated. React decides whether to redraw by comparing what it was given with what it
  had; hand it the same array object back and it sees no change, even if the contents
  differ. `push` would have done exactly that.

See the [button with counter example](https://react.dev/learn#updating-the-screen) for a combination of state and events

### Note: Hooks are special React functions who's name starts with `use`

## Reactive Programming

**The app now.** It works: **Add** appends a random sample task and the list grows. The question left over is *why the screen redrew at all* — nobody told it to. 

When a state variable defined with `useState` changes with the help of the setter (and thus, not changing the variable directly!!) a redrawing of the whole component is triggered. 

This is *reactive programming*. And reactive programming is why React is called so. 

A bit like in Excel -- one of the classical reactive programming environments -- where when you change one cell, all the others who depend on it and only those are changed automatically. 

In React, the dependents are not formulas, but UIs. When a state variable or a prop changes, the library automatically redraws all the relevant UI elements, and only those. 

So the loop the app now runs is:

> you click **Add** → `handleAdd` calls `setTodos` with a new array → React notices the
> state it is holding is not the array it had → it calls `TodoList()` again → `map` builds
> one more `<TodoItem />` than last time → the new row appears.

Nobody wrote "add a row to the screen" anywhere. You changed the data and described what
the screen should look like for any data; React did the rest. That is the trade React asks
you to make, and everything else this term is a consequence of it.

Here is the whole thing, which is the app you leave the first lecture with:

```jsx
import { useState } from "react";

const SAMPLE_TASKS = ["Buy milk", "Call the landlord", "Book the dentist",
                      "Water the plants", "Reply to Mette"];

function randomTask() {
  return SAMPLE_TASKS[Math.floor(Math.random() * SAMPLE_TASKS.length)];
}

function TodoItem({ text }) {
  return <li className="todo-item">{text}</li>;
}

export default function TodoList() {
  const [todos, setTodos] = useState(["Buy milk"]);

  function handleAdd() {
    setTodos([...todos, randomTask()]);
  }

  return (
    <>
      <h1>My To-Do ({todos.length})</h1>
      <ul>
        {todos.map((text, index) => (
          <TodoItem key={index} text={text} />
        ))}
      </ul>
      <button onClick={handleAdd}>Add</button>
    </>
  );
}
```

Forty lines, and every idea in this note is in there somewhere.

# References

Read up from the [react.dev](https://react.dev) documentation site, the following: 

- Describing the UI
	- [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components)
	- [Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx)
	- [JS in JSX](https://react.dev/learn/javascript-in-jsx-with-curly-braces)
	- [Passing Props](https://react.dev/learn/passing-props-to-a-component)
	- [Conditional Rendering](https://react.dev/learn/conditional-rendering)
	- [Rendering Lists](https://react.dev/learn/rendering-lists)

- Adding Interactivity
	- [Responding to Events](https://react.dev/learn/responding-to-events) 
	- [State: A Component's Memory](https://react.dev/learn/state-a-components-memory)

# Exam Questions

### 1. What is JSX and how does it differ from HTML?

### 2. Explain the difference between props and state in React.

### 3. Why do we need to use a `key` attribute when rendering lists in React?

### 4. What is wrong with this component?
```js
function Greeting() {
  return (
    <h1>Hello</h1>
    <p>Welcome to React</p>
  )
}
```

---

By the end the app is deliberately silly: **Add** picks a task at random, because there is
nothing to type into yet. Next week there is, and that is where forms come in — along with
the first real bug, when deleting from the middle of the list shows you why keying by
position was never going to hold.
