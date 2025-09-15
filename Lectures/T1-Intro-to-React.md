
# React

React is a JavaScript **library** for building interactive **single page applications**. We will talk about what Single Page Applications are and how they work in a different lecture. For now, we want to be users of react so we'll start doing a very simple application in it and learn React on the way. 

## React is a ***component-based*** UI library 

### Components are **JS functions** that return JSX elements

[Example](https://react.dev/learn/your-first-component#defining-a-component) of a React component :

```js
export default function ToDoList() {
  return (
    <>
      <h1>Remember</h1>
      <ul>
        <li>Buy bread</li>
        <li>Buy milk</li>
      </ul>
    </>
  )
}

```

## JSX is a combination of JS and HTML

JSX is acronym for JavaScript + XML

### JSX is a **syntax extension** that provides template-like declarative UI description within JavaScript itself
- syntax extension for Javascript! 
- has the full power of JS inside of the {}
- template-like because it looks like other other front-end JS frameworks (e.g., [Vue templates](https://www.freecodecamp.org/news/reacts-jsx-vs-vue-s-templates-a-showdown-on-the-front-end-b00a70470409/)) and server-side rendering frameworks (e.g. Jinja for Flask, Moustache)
- HTML-like code within JavaScript
- JSX is **transpiled** to Javascript 

### JSX has a **stricter syntax than HTML**
#### A component can [only ever return a single JSX tag](https://react.dev/learn/writing-markup-with-jsx#1-return-a-single-root-element) 
Otherwise, you get an error.
Solution is to use a Fragment when you don't need an actual HTML element as parent

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
#### Tags must [always be closed](https://react.dev/learn/writing-markup-with-jsx#2-close-all-the-tags) 


### JSX converts most HTML and CSS attributes to camelCase 
#### HTML Event Handlers, e.g. `onclick` => `onClick`
#### CSS attributes, e.g. `background-color` => `backgroundColor`
#### Special JS keyword `class` becomes `className`

Two [minor exceptions](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things) from this rule.




## Interpolating JS in JSX

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

### A component is a function. Functions can be parameterized => Components  should be parameterizable

### Component parameters are called **props** in React
- the term very likely comes from properties

### Props are passed on normally as HTML attributes

- In the moment when the *props* are [passed to the component](https://react.dev/learn/passing-props-to-a-component#step-1-pass-props-to-the-child-component), they *look* like HTML attributes -- have the same syntax

### Props are used in the component definition as the `props` parameter 
- In the component definition the props are accessed as either
	- a single function parameter named `props`

### You can be more explicitit using a [destructured](https://react.dev/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component) dictionary in the component definition
- makes code easier to read and write


## Component State

### Every component can store local state 

Unlike the props, the state can be changed from within the component

### Local state is defined using the `useState` hook 

The `useState` hook: 
- takes an **initial** value
- returns **current value** and a **setter function**

See the [button with counter example](https://react.dev/learn#updating-the-screen) for a combination of state and events

### Note: Hooks are special React functions who's name starts with `use`



## Event Handling

### Interactive apps must handle events: click, type, mouse move, screen touch, etc. 

This is the main job of your UI app.


### Built-in components (e.g. `<button>`) support built-in events (e.g. `onClick`, etc.).

Associating event handlers with events is done with the attribute in curly brackets syntax, as above. (See [onClick example](https://react.dev/learn/responding-to-events#adding-event-handlers).)

#### WARNING: You must know the difference between calling a function and passing a reference to it! 
### Event handlers are defined inside components

### Handlers have usually names starting with `handle`... 

### **Event handlers always receive an event as argument**

The `event` argument details info about what just happened. 
- Sometimes you can ignore it, 
- Sometimes you inspect it to learn about the event (e.g. mouse position, element that was clicked, etc. )

### Events propagate (*bubble up*) the DOM tree

If you have an `onClick` handler on both a button and a containing div, both will be handled in sequence, from the inner one outwards. [See event propagation example](https://react.dev/learn/responding-to-events#event-propagation). 

- Sometimes you can change the behavior of the event by calling `stopPropagation` or `preventDefault` on the event object. [example of stop propagation](https://react.dev/learn/responding-to-events#stopping-propagation) and of [preventing default behavior](https://react.dev/learn/responding-to-events#preventing-default-behavior). 



## Connecting Inputs To State Via Event Handlers

The strange story of how you connect a state variable to the content of an input control in React: 

```js
import { useState } from 'react';

export default function InputExample () {
  const [answer, setAnswer] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();
    // do something with the answer 
    // ... 
  }

  function handleTextareaChange(e) {
    setAnswer(e.target.value);
  }

  return (
    <>
  
	  <form onSubmit={handleSubmit}>

		<textarea
          value={answer}
          onChange={handleTextareaChange}
          disabled={status === 'submitting'}
        />
        <br />
        
        <button disabled={answer.length === 0}>
          Submit
        </button>
      
      </form>
    </>
  );
}
```

This is called a `controlled component` because the form elements (i.e. `textarea` in our example, are controlled by the react prop). Should probably be *controlling* ...  



## Rendering Lists

Most applications sooner or later rely on lists of things that you want to process. 

### In React, to render lists you rely on `for` loops and  `array.map()`

### You must use a `key` attribute for every element in a list
- must be unique
- can be the database ID, UUID, or anything else unique
- important internally for React's rendering
- if you don't do this, your console will be full of 

Nice examples of rendering lists and filtering at: *Describing the UI* > [Rendering Lists](https://react.dev/learn/rendering-lists). Also nice exercises at the bottom of the page.




## Styling

CSS Styles can be defined in multiple ways

### In a separate file
This has the problem that it does not scale - at some point the various styles will conflict with each other.

### Inline as the example above
This is the least recommended

### As local variables, as they use in React Native 

e.g. [here](https://github.com/mircealungu/zeeguu-mobile/blob/master/screens/AllArticles.js)

### With the help of `styled-components` library

#### First you install the library `npm install -s styled-components`

#### Then you define styles with the `styled` function!
```js

// Create a Title component that'll render an <h1> tag with some styles
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: #BF4F74;
`;

// Create a Wrapper component that'll render a <section> tag with some styles
const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
`;

// Use Title and Wrapper like any other React component – except they're styled!
render(
  <Wrapper>
    <Title>
      Hello World!
    </Title>
  </Wrapper>
);
```

#### It's nicer to move components to their own file





## Conditional Rendering 

Often components need to display differently based on some state or prop. 

Three possible ways to render conditionally: 
1. If statements
1. The `conditional ? operator` 
1. When only one option is possible `logical && syntax` 

Note: 
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation. 

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*






## Reactive Programming 

When a state variable defined with `useState` changes with the help of the setter (and thus, not changing the variable directly!!) a redrawing of the whole component is triggered. 

This is *reactive programming*. And reactive programming is why React is called so. 

A bit like in Excel -- one of the classical reactive programming environments -- where when you change one cell, all the others who depend on it and only those are changed automatically. 

In React, the dependents are not formulas, but UIs. When a state variable or a prop changes, the library automatically redraws all the relevant UI elements, and only those. 


### The useEffect hook ...





## Coding Conventions

A few conventions 
- (naming) components are named with capital letters 
- (modularization): components are defined in their own files
- (modularization) To import a component one can use either *default* or *named* imports



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














