
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





# [useEffect](https://react.dev/learn/synchronizing-with-effects#step-1-declare-an-effect) - The Most Important Hook to Understand


# Side Effects in React

### In the context of React, the main responsibility of a component function is to... render JSX.  

### => Anything besides that is considered a side-effect
- actions that a functional component does besides rendering the component.
- what could they be? 
	- updating the DOM
	- saving things to the DB
	
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
  return () => {  
    window.removeEventListener("scroll", handleScroll, true);  
  };  
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

##### If you had a counter app, you might want to load counters from the DB 

LocalStorage is actually a little database, that we should benefit from.
The following code pattern solves this: 

```js
export default function Counter({name, color, size}) {  
  
    const [clicks, setClicks] = useState(undefined);  
  
    useEffect(()=>{  
        try {  
            let stored_counter = Number(localStorage.getItem(name));  
            setClicks(stored_counter);  
        } catch (e) {  
            setClicks(0);  
        }  
    }, []);  
  
    useEffect(() => {  
        if (clicks !== undefined) {  
            localStorage.setItem(name, JSON.stringify(clicks));  
        }  
    }, [clicks]);
```

In the upcoming lectures you will learn how to load things from the database and you will see that the patterns are going to be the same. 

### **Important:** During development, React runs the useEffect twice on mount

Why? if your code works in this situation, it means you're cleaning up nicely; and that's good!

if not, then you have to figure out why and cleanup correctly.



## Releasing Resources on Component Unmount

### This is ugly and won't be necessary often. But it pushes your understanding of JS syntax... 

It's something that you'll need to do also in other components. 

### Sometimes a component allocates a resource in the initialization and that resource has to be de-allocated in the component *destruction*. 

Examples of such resources could be:
- a reference to a timer - that executes an action every second
- a connection to a database 

### If your effect allocates a resource that must be deallocated, do that by returning a *cleanup function* from useEffect

#### The syntax is ***UGLY***: **an arrow function that does the connection, and then returns another function that does the disconnect** 

![](images/effect-with-cleanup-function.png)

#### And  example of resource that needs to be released: a timer

```javascript
useEffect(() => {
  setInterval(() => {console.log("hello")},1000)
}, [])
```

The correct way of handling it: 
```javascript
useEffect(() => {
  let interval = setInterval(() => {console.log("hello")}, 1000)

  return () => {
    clearInterval(interval) // clear the interval in the returning function
  }
}, [])
```


# Second special case of `useEffect`: no second argument at all!

A very special case of calling `useEffect` is with no second argument: 
```javascript
function MyComponent() {  

	useEffect(() => {  
		console.log("every render!")
	});  
	return <div />;  
}
```

## **Every time the component renders, React updates the screen and then runs the code inside useEffect.** 

## This is not normally used, except for debugging in my experience. 

## This is the fastest way to run out of cloud credits when you'll connect to the DB later in the course




