
## React

React is a JavaScript library for building interactive user interfaces.


## Components

React is a *component-based* UI library. 

Every UI element in React is either a component or is composed of nested components.

Components are 
- reusable UI elements
- functions that return markup
- nested all the way down
	- From small, e.g. buttons, to large, e.g. full web page or mobile screens

Conventions: 
- (naming) components are named with capital letters 
- (modularization): unless they are very small and related, components should be defined in their own files. 
- (modularization) To import a component one can use either *default* or *named* imports.

[Example](https://react.dev/learn/your-first-component#defining-a-component) of a React component 


## JSX

JSX is 
- A markup syntax used in React to ease definition of UIs
- A combination of JS and HTML
- A stricter syntax than HTML
	- A component can [only ever return a single JSX tag](https://react.dev/learn/writing-markup-with-jsx#1-return-a-single-root-element) 
	- Tags must [always be closed](https://react.dev/learn/writing-markup-with-jsx#2-close-all-the-tags) 

JSX converts [most HTML and CSS attributes to camelCase](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things) 
- `onclick` => `onClick`
- `background-color` => `backgroundColor`

Notes: 
- Similar approaches for other front-end JS frameworks (e.g., [Vue templates](https://www.freecodecamp.org/news/reacts-jsx-vs-vue-s-templates-a-showdown-on-the-front-end-b00a70470409/)) and server-side rendering frameworks (e.g. Jinja for Flask).
- JSX is transpiled to Javascript ... it represents *syntactic sugar* 


## Styles

CSS Styles can be defined 
- in a separate file, or 
- inline or as local variables (see example in Interpolating JS)

Warning: Use `className` instead of class (e.g. `<img className="avatar" />`) because `class` is reserved keyword in JS. 



## Interpolating JS in JSX

Curly brackets to escape JS inside JSX can be used in three ways

1. As **text inside a component**

```
return (
  <>
    <h1>{"Hello" + user.firstName + user.LastName}</h1>
    <p>Today is: {todaysDate}</p>
  </>
);
```

2. As **attributes immediately following the `=` sign**
```
return (
  <img
    className="avatar"
    src={user.imageUrl}
  />
);

```

3. Special case of attributes: **[double curlies](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-double-curlies-css-and-other-objects-in-jsx) for objects**
```
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


## Conditional Rendering 

Often components need to display differently based on some state or prop. E.g. checking done items in a list as in the [example](https://react.dev/learn/conditional-rendering#conditionally-returning-jsx) from *Describing the UI > Conditionally Rendering JSX*. 

Three possible ways to render conditionally: 

- If statements
- The `conditional ? operator` 
- When only one option is possible `logical && syntax` 

Note: 
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation. 

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*


## Rendering Lists

Most applications sooner or later rely on lists of things that you want to process. 

In React, to render lists: 
- You rely on `for` loops and array `map()`
- You must use a `key` attribute for every element in a list
	- must be unique
	- can be the database ID, UUID, or anything else unique
	- important internally for React's rendering

Nice examples of rendering lists and filtering at: *Describing the UI* > [Rendering Lists](https://react.dev/learn/rendering-lists). Also nice exercises at the bottom of the page.


## Parameterizing Components

- A component is a drawing function => It should be parameterizable
- In the moment when the props are [passed to the component](https://react.dev/learn/passing-props-to-a-component#step-1-pass-props-to-the-child-component), they *look* like HTML attributes -- have the same syntax
- In the component definition the parameters are collected in a single function parameter named `props` but one can [destructuring notation instead](https://react.dev/learn/passing-props-to-a-component#step-2-read-props-inside-the-child-component)

Note: A special kind of prop is the `children` prop that, when used inside of a component definition refers to the JSX contained in the component. [Read and see example](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children)

When a prop is changed, the component is also redrawn (reactive programming). See the [clock example](https://react.dev/learn/passing-props-to-a-component#how-props-change-over-time)

See the example from: [Sharing data between components](https://react.dev/learn#sharing-data-between-components)
- moving the state up is also calling *lifting the state*


## Component State

A component might need to store local state. 

In React, state is: 
- defined with `useState` that is a function defined in the `react` package
- hidden inside each component 

See the [example](https://react.dev/learn#updating-the-screen) and note:
- `useState` 
	- takes an initial value
	- returns current value and setter
- the component 
	- returns the definition of it's representation 
- the `onClick` is the camelcase version of the event handler name from HTML (`onclick`)
- observe how we link an event handler with a JSX element

When a state variable defined with `useState` changes with the help of the setter (and thus, not changing the variable name!), a redrawing of the component is triggered. This is reactive programming. A bit like in Excel where when you change one cell, all the others who depend on it and only those are changed automatically. Here, the dependents are not formulas, but UIs. When a state variable or a prop changes, the library automatically redraws all the relevant UI elements, and only those. 



## Example Application

[TODO List Application with React](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_components)
- requires input... that we didn't discuss yet


# References
- Describing the UI > Writing Markup with JSX
- 


## Designing with Components

One possible process: 
- Breaking the UI in a component hierarchy
- 



- Reactive programming - as opposed to declarative programming
	- [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state) (from react.dev)




- [Updating Objects in State](https://react.dev/learn/updating-objects-in-state)
- [Updating Arrays in State](https://react.dev/learn/updating-arrays-in-state)

- UI Patterns
	- Rendering a list of elements 




# To Think About

- What is the relation between JSX and React? 
- 


# Project work 👬
- Start converting the HTML prototype to React
- 



