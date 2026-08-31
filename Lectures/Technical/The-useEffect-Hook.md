# Side effects in programming 

## Concept coming from functional programming

Functional programming - a powerful way of programming that is one of the main paradigms (ways of thinking):
1. imperative
2. functional
3. declarative

## Side effect = anything besides the main calculation needed for the result

### A pure function is a function that does one thing, and one thing only

Conceptually the following function is free of side-effects:
```js

function square(i) {
	return i*i;
}
```

however, if the function does something else than it's main goal, we call that a side effect.

```js
function square (i) {
	localStorage.setItem("square", i*i);
	return i*i;
}
```

in the above case, the `LocalStorage.setItem` saves the value of the counter to `LocalStorage`, a mini key-value store that's available for every web application inside of the browser.

That was not the main purpose of the function. It was a side effect.


# Side Effects in React with `useEffect`

### In the context of React, the main responsibility of every component function is to... render JSX.  

### => Anything besides that is considered a side-effect
- actions that a functional component does besides rendering the component.
- what could they be?
	- updating the DOM
	- saving things to the DB
	- we'll see a few examples later
	
**A fair objection: is *reading* a side effect?** In the functional-programming tradition, no — nothing changes, so nothing is affected. But it does make the function **impure**: its result depends on something other than its arguments, so two identical calls can return different things, and React can no longer assume that rendering the same props twice gives the same JSX.

React sidesteps the argument by framing it differently, and the framing is the useful part:

### Goal: synchronize your component with **some system outside of React**

Reading and writing are both synchronisation. `localStorage`, the document title, a timer, a backend — anything React does not control is *outside*, and keeping your component in step with it is what effects are for.


## Defining side effects in React is done with the `useEffect` hook with two arguments

useEffect allows us to "hook into" the React implementation, and capture the moment when a state variable is updated. We can decide to do something in such a situation. E.g., below, a component that changes the title of the browser window when the state of a variable changes:

```jsx
import { useState, useEffect } from "react";

export default function TodoList() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  // …
}
```

Read it as a sentence: **whenever `todos` changes, write it to local storage.** You never call that function yourself. You state the dependency, and React runs it at the right moment — which is the same bargain as `map`: describe the relationship, let React do the work.

`JSON.stringify` is there because local storage only holds **strings**. Hand it an array and you get back `"[object Object]"` on the next load, which is a confusing ten minutes if you have not been warned.

#### Arg 1: What the side effect should do is defined by a  function
- most of the times defined in-place as anonymous arrow function
- but can just as well be a named function

#### Arg 2: When to execute the side effect? 
The second argument is an array that contains one or more state variables The (side-)effect would be run on any of those variables changing.

### Examples of using `useEffect`
#### Changing the title of the page based on the state in a component 

```js 
useEffect(() => {  
  window.title = "Saved Articles";  
}, [articles]);
```
#### Interacting with the DOM in some way

```js
useEffect(() => {  
  if (errorMessage) {  
    scrollToTop();  
  }  
}, [errorMessage]);
```
- another example would be saving something to local storage as in the example above

#### Updating some state when a prop or a state changes

e.g.
```js
useEffect(() => {  
  setQuickFeedbackModal(false);  
  setOpenFeedback(false);  
  setHasProvidedQuickFeedback(false);  
}, [exerciseBookmarks]);
```
IMO, In Mircea's Opinion: this should be called useReactive -- because defines a reactive relationship.

## useEffect as one of the mechanisms of *reactive programming*

You met this last week with `useState`: change the data, and React works out what the screen should look like — see [Reactive Programming](Intro-to-React.md#reactive-programming).

`useEffect` is the same idea pointed outwards. `useState` keeps the *screen* in step with your data; `useEffect` keeps *everything else* in step with it. Same dependency, same automatic re-run, different destination.


# Special Case of `useEffect`: Empty dependencies list

### If you call an effect with an **empty dependencies list**, **it is only run once, on component mount!**

**Mount** is React's word for a component appearing for the first time — its first render, when it goes from not being on screen to being on screen. The opposite is **unmount**, when it is taken off again. A component mounts once and can then re-render any number of times.

An empty dependency list says *nothing to depend on*, so there is never a later change to react to, so it runs at mount and never again.

##### Why would you want to run something only on mount? What kind of things would you want to do? 

- Initialization.  Often there's special initializations that you want to have when a component is first time rendered - at least the top level component in your program - the screen -- it needs to remember the state from last time. In our case, it would be good if we could have our page remember



##### If you had a TODO list app, you might want to load counters from the DB 

LocalStorage is actually a little database, that we should benefit from. The following code pattern solves this:

```js
function saveList(key, list) {
	localStorage.setItem(key, JSON.stringify(list)); 
 } 

function loadList(key) { 
	const data = localStorage.getItem(key); 
	return data ? JSON.parse(data) : []; 
}
```

In the upcoming lectures you will learn how to load things from the database and you will see that the patterns are going to be the same.

### **Important:** During development, React runs the useEffect twice on mount

Why? if your code works in this situation, it means you're cleaning up nicely; and that's good!

if not, then you have to figure out why and cleanup correctly.


# Two more shapes of `useEffect`, later

There are two further cases — a cleanup function that runs when the component unmounts, and an effect with no dependency list at all. Neither is much use against local storage, and both are needed the moment an effect talks to a live backend: one to close a subscription, the other as a warning. They live in *Backend III · [useEffect Against a Live Backend](useEffect-Against-a-Live-Backend.md)*.


## Exam Questions

### 1. Explain what this useEffect does:
```js
useEffect(() => {
  localStorage.setItem("clicks", clicks);
}, [clicks]);
```

### 2. What is the difference between these two useEffect calls?
```js
// Version A
useEffect(() => {
  console.log("Effect A");
}, []);

// Version B
useEffect(() => {
  console.log("Effect B");
});
```
