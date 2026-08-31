# React

React is a JavaScript **library** for building interactive **single page applications**. We will talk about what Single Page Applications are and how they work in a different lecture. For now, we want to be users of react so we'll start doing a very simple application in it and learn React on the way.

We build a to-do list as we go. Each section below is the smallest step that makes the previous step's problem go away, so the page reads in the order the app needs — and each one opens by saying what the app does at that point.

## React is a ***component-based*** UI library

### Everything in React is a component

A button is a component. A list row is a component. So is the whole page. You build a screen by nesting small ones inside bigger ones, and there is no other unit — no templates, no partials, no widgets.

### Components are **JS functions** that return JSX elements

[Example](https://react.dev/learn/your-first-component#defining-a-component) of a React component :

```jsx
export default function TodoList() {
  return (
    <>
      <h1>My To-Do</h1>
      <ul>
        <li>Buy milk</li>
      </ul>
    </>
  );
}
```

A plain JavaScript function, returning something that looks like HTML. The name is capitalised — React uses that to tell your components apart from built-in tags like `<ul>`, so `todoList` would not work.

## JSX is a combination of JS and HTML

**The app now.** The same heading, wrapped in a little markup — and the first surprise, because that markup is not quite HTML.

JSX is acronym for JavaScript + XML

### A syntax extension for JavaScript

It lets you describe a UI declaratively, inside the language itself, rather than in a separate template file.

- syntax extension for Javascript!
- has the full power of JS inside of the {}
- template-like because it looks like other front-end JS frameworks (e.g., [Vue templates](https://www.freecodecamp.org/news/reacts-jsx-vs-vue-s-templates-a-showdown-on-the-front-end-b00a70470409/)) and server-side rendering frameworks (e.g. Jinja for Flask, Moustache)
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
);

// This works but adds unnecessary <div>
return (
  <div>
    <h1>Title</h1>
    <p>Paragraph</p>
  </div>
);

// This works without extra DOM node
return (
  <>
    <h1>Title</h1>
    <p>Paragraph</p>
  </>
);
```
`<>…</>` is called a **fragment**: a wrapper that groups elements without adding anything to the page. Use it whenever you need a single parent but do not want a real `<div>` in the output.
#### Tags must [always be closed](https://react.dev/learn/writing-markup-with-jsx#2-close-all-the-tags) 

### JSX converts most HTML and CSS attributes to camelCase 
#### HTML event handlers, e.g. `onclick` becomes `onClick`
#### CSS attributes, e.g. `background-color` becomes `backgroundColor`
#### Special JS keyword `class` becomes `className`

Two [minor exceptions](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things) from this rule.




## Interpolating JS in JSX

**The app now.** The heading counts: *My To-Do (3)*. The number has to come from JavaScript, and it has to land inside the markup.

Curly brackets to escape JS inside JSX can be used in three ways
### Inside text

```js
return (
  <>
    <h1>Hello {user.firstName + " " + user.lastName}</h1>
    <p>Today is: {todaysDate}</p>
  </>
);
```

### As an attribute value
```js
return (
  <img
    className="avatar"
    src={user.imageUrl}
  />
);

```

### Double curlies, for objects

An object *inside* the braces — so `{{ }}`, which is one pair for the JS and one for the object. See [double curlies](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx).
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

### Parameters are called `props`
- the term very likely comes from properties

### Passed like HTML attributes

- In the moment when the *props* are [passed to the component](https://react.dev/learn/passing-props-to-a-component#step-1-pass-props-to-the-child-component), they *look* like HTML attributes -- have the same syntax

### They arrive as one object
- In the component definition the props are accessed as either
	- a single function parameter named `props`
	- a destructured dictionary

### Or destructure them

Naming the props you expect in the signature itself — [destructuring](https://react.dev/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component) — makes the component easier to read and to write.

Here is our to-do row, written both ways:

```jsx
// the props object, whole
function TodoItem(props) {
  return <li className="todo-item">{props.text}</li>;
}

// destructured — the version we will use from here on
function TodoItem({ text }) {
  return <li className="todo-item">{text}</li>;
}
```

Both are the same component. The second says, in its own signature, exactly which props it expects — so you can tell what it needs without reading the body. Used like this:

```jsx
<TodoItem text="Buy milk" />
<TodoItem text="Call the landlord" />
```

Which is already tedious for two items, and impossible for a list that changes while the app is running. That is the next section.


### With the `{children}` prop

Props pass **data** into a component. `children` passes **markup** into it — everything written between the opening and closing tags.

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

That works exactly as long as the content is one string. The moment you want a list inside the panel, or a button, or another component, you are stuck: you cannot put a `<ul>` inside a string. You would end up adding `items`, then `buttonLabel`, then `showIcon`, and the panel would slowly learn about everything that might ever go in it.

`children` is the way out. The component stops describing its content and only describes its *frame*:

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

Note what `Panel` does **not** know: that there is a list, that there is a button, that either exists. It knows it has a title and a frame to draw around whatever it was handed. That is the whole idea, and it is why almost every layout component you write — containers, cards, modals, page wrappers — ends up taking `children`.

> **The rule of thumb.** If it is data the component needs to *use* — a title, a count, a
> user — make it a prop. If it is markup the component only needs to *place*, use
> `children`.

## Rendering Lists

**The app now.** Three items, drawn from an array rather than typed out. Which is the point: the array is the app, and the screen is a picture of it.

Most applications sooner or later rely on lists of things that you want to process.

### Lists are rendered with `array.map()`

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

`map` turns an array of **strings** into an array of **JSX elements**, and React renders an array of elements by rendering each one. That is the whole mechanism. Add a fourth string to `todos` and a fourth row appears; nothing else has to change.

### Every item needs a `key`
- must be unique **among its siblings**
- can be the database ID, UUID, or anything else stable
- it is how React tells the items apart between renders — without it, it cannot know whether you added a row, removed one, or reordered them
- if you don't do this, your console fills up with warnings

We are using the array **index** above, which is the thing every beginner reaches for and which works perfectly — until items can be removed from the middle. Delete the first of three, and the item that was index 1 becomes index 0: React sees "the thing with key 0 changed its text" rather than "the first thing is gone". Next week adds delete, you will watch exactly that go wrong, and that is when we swap indexes for real IDs.

Nice examples of rendering lists and filtering at: *Describing the UI* > [Rendering Lists](https://react.dev/learn/rendering-lists). Also nice exercises at the bottom of the page.

## Event Handling

**The app now.** An **Add** button that does nothing at all. Making it do something is the next two sections.

### Interactive apps handle events

Click, type, mouse move, touch. Responding to these is the main job of a UI.

### Event handlers are defined inside components
### Handlers usually have names starting with `handle`
### Built-in elements come with built-in events

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

#### Passing a function, not calling it

```jsx
<button onClick={handleAdd}>Add</button>     // ✅ hands React the function
<button onClick={handleAdd()}>Add</button>   // ❌ calls it now, hands React the result
```

The second one runs `handleAdd` while the component is *rendering*, before anybody has clicked anything, and gives `onClick` whatever it returned — usually `undefined`. If your handler fires once on load and never again, this is why.

### Handlers receive an event object

The `event` argument details info about what just happened.
- Sometimes you can ignore it,
- Sometimes you inspect it to learn about the event (e.g. mouse position, element that was clicked, etc. )


<!-- lecture 1 stopped here; state and bubbling opened lecture 2 -->

### Events bubble up the DOM tree

If you have an `onClick` handler on both a button and a containing div, both will be handled in sequence, from the inner one outwards.

You will meet this for real next week, the moment each row gets a delete button:

```jsx
<li onClick={() => toggleDone(id)}>
  {text}
  <button onClick={() => remove(id)}>×</button>
</li>
```

Click the **×** and *both* handlers fire — the button's, then the row's — so the item is deleted and the row you just deleted is also toggled. `e.stopPropagation()` inside the delete handler is the fix, and it is much easier to remember once you have watched it happen. [See event propagation example](https://react.dev/learn/responding-to-events#event-propagation).

- Sometimes you can change the behavior of the event by calling `stopPropagation` or `preventDefault` on the event object. [example of stop propagation](https://react.dev/learn/responding-to-events#stopping-propagation) and of [preventing default behavior](https://react.dev/learn/responding-to-events#preventing-default-behavior).

## Component State

**The app now. This is the one to slow down for.** Add pushes a task onto the array — and nothing appears. The variable really did change; the screen simply does not care. That failure is the whole argument for state, and it is far more convincing having just watched it fail.

### Every component can store local state 

The difference from props is **ownership**. Props arrive from the parent and the component may only read them; state belongs to the component itself, which is the only thing that can change it. Props are what you were given; state is what you keep.

First, the version that does **not** work — worth typing out, because the reason it fails is the reason state exists:

```jsx
const SAMPLE_TASKS = [
	"Buy milk", 
	"Call the landlord", 
	"Book the dentist",
    "Water the plants", 
    "Reply to Mette"];

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

The array grows. The console proves it. The screen ignores you completely, because nothing told React that anything happened — it only re-runs your component when you ask it to, and pushing onto a variable is not asking.

### State comes from `useState`

The `useState` hook:
- takes an **initial** value
- returns **current value** and a **setter function** (returns from where? you get it from React! React gave you this setter! It baked an observer inside of it! So now if you change the state with its help, it will know that the state has changed! Let's see what does this imply)

```jsx

// We are importing the useState function from React
import { useState } from "react";

function TodoList() {
  const [todos, setTodos] = useState(["Buy milk"]);

  function handleAdd() {
    setTodos([...todos, randomTask()]);   
    // a *new* array, not a push
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

1. `todos` now comes from `useState`, so React is the one holding it. The broken version above did survive — a variable outside the component persists perfectly well — but nothing connected it to the screen. Had we moved that `let` *inside* the component it would have been worse still, created fresh on every call.
- `setTodos` is given a **new array** — `[...todos, randomTask()]` — rather than the old one mutated. **React decides whether to redraw by comparing what it was given with what it** **had**; hand it the same array object back and it sees no change, even if the contents differ. `push` would have done exactly that.

*Optional*: See the [button with counter example](https://react.dev/learn#updating-the-screen) for a combination of state and events

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

Nobody wrote "add a row to the screen" anywhere. You changed the data and described what the screen should look like for any data; React did the rest. That is the trade React asks you to make, and everything else this term is a consequence of it.

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


And deliberately silly: **Add** picks a task at random, because there is nothing to type into yet. Next week there is, and that is where forms come in — along with the first real bug, when deleting from the middle of the list shows you why keying by position was never going to hold.

# References

Read up from the [react.dev](https://react.dev) documentation site, the following:

- Describing the UI
	- [Importing and Exporting Components](https://react.dev/learn/importing-and-exporting-components)
	- [Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx)
	- [JS in JSX](https://react.dev/learn/javascript-in-jsx-with-curly-braces)
	- [Passing Props](https://react.dev/learn/passing-props-to-a-component)
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
  );
}
```

### 5. What is *reactive* about programming in React?

### 6. You push a new item onto an array and the screen does not change. Why not, and what do you do instead?

### 7. Why should you avoid mutating state objects and arrays directly in React? 