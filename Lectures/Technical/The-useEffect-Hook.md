# Side effects in programming 

## Concept coming from functional programming
## Side effect = anything besides the main calculation needed for the result

Refers to anything that a function does not serve the purpose of computing the result. Conceptually the following function is free of side-effects:
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


# Side Effects in React with `useEffect`

### In the context of React, the main responsibility of a component function is to... render JSX.  

### => Anything besides that is considered a side-effect
- actions that a functional component does besides rendering the component.
- what could they be? 
	- updating the DOM
	- saving things to the DB
	- we'll see a few examples later
	
### Goal: synchronize your component with **some system outside of React**


## Defining side effects in React is done with the `useEffect` hook with two arguments

The most basic example possible of a component that changes the title of a window when the state changes

```js

import { useEffect } from 'react';

export default function Counter({color, size}) {  
  
    const [clicks, setClicks] = useState(0);  
  
    useEffect(() => {  
        localStorage.setItem("clicks", clicks);
    }, [clicks]);

// ...
```

#### Arg 1: What is the side effect: often a lambda function

#### Arg 2: When to execute the side effect
The second argument is an array that contains one or more state variables
The (side-)effect would be run on any of those variables changing.

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

#### Defining some DOM event handlers

```js
useEffect(() => {  
  window.addEventListener("scroll", handleScroll, true);  
}, [articles]);
```

## useEffect as one of the mechanisms of *reactive programming*

### Reactive programming = you express your program logic as a network of dependencies between variables

#### Excel, the *par excellence* and most popular example of Reactive programming 

- is all about updating cell dependencies

#### React is also *reactive*, so it's all about updating dependencies when state changes

#### Besides updating variables react also updates the UI when the state changes



# Special Case of `useEffect`: Empty dependencies list

### If you call an effect with an **empty dependencies list**, **it is only run once, on component mount!**

##### Why would you want to run something only on mount? What kind of things would you want to do? 

- Initialization.  Sometimes there's special initializations that you want to have when a component is first time rendered. 



##### If you had a TODO list app, you might want to load counters from the DB 

LocalStorage is actually a little database, that we should benefit from.
The following code pattern solves this: 

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

There are two further cases — a cleanup function that runs when the component unmounts,
and an effect with no dependency list at all. Neither is much use against local storage,
and both are needed the moment an effect talks to a live backend: one to close a
subscription, the other as a warning. They live in
*Backend III · [useEffect Against a Live Backend](useEffect-Against-a-Live-Backend.md)*.


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
