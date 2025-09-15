
# React Hooks 

## Special React functions for "hooking into" the framework
### Their name starts with `use`

Most popular: 
- `useState` -- to allow you to define state
- `useEffect` -- to allow you to handle side effects (see below)
- `useRef` -- an object that can be persisted across renderings but is not state (see below)
### Called at the top of the component
### Can be called from another hook or directly from a component
### Can NOT be called from within a conditional expression or nested functions



# [useEffect](https://react.dev/learn/synchronizing-with-effects#step-1-declare-an-effect) for handling Effects

## When *as a side effect of changing state* you must to do something else besides re-render

IMO, In Mircea's Opinion: this should be called useReactive -- because defines a reactive relationship. 

### Side effect in functional programming = anything besides the calculation

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



## Side Effect Examples in React
In the context of React, the main responsibility of a component function is to... render JSX. 
Anything besides that is considered a side-effect. 

Examples of such side effects that you'll encounter in React are: 

- When a ChatRoom component must connect to the server to download the corresponding info
- When you want to change the title of the page based on the state in a component 
- When you want to save something to database based on some changes in the component state

In conclusion...

> **Side Effects in React = actions that a functional component does besides rendering the component.**

The goal of side effects then is to synchronize your component with some system outside of React. 

## Declaring Side Effects 
Remember that React is *reactive programming*, so it's all about updating dependencies when state changes (remember, Excel, the par excellence and most popular example of Reactive programming is all about updating cell dependencies). This is why, React expects you to use a special function called `useEffect` if you want to perform side effects when state changes. The function takes two arguments
- what to do as a side effect
- when to execute the side effect -- and by this React means: which state variable should change for the side effect to be executed.

The following is the most basic example possible of a component that changes the title of a window when the state changes:

```js

import { useEffect } from 'react';

export default function Counter({color, size}) {  
  
    const [clicks, setClicks] = useState(0);  
  
    useEffect(() => {  
        localStorage.setItem("clicks", clicks);
    }, [clicks]);

// ...
```

Note that the first argument of `useEffect` is a lambda function (arrow function). And the second argument is an array. You could run an effect when more than one state variable and then the (side-)effect would be run on any of those variables changing. 

Let us assume that our counters have names. In that case we would have to think about how to save the information for a specific counter, and also save it when either the counter changes, or the name of the counter changes. Try to do this on your own. When you're done compare it with the following 

```bash
git clone git@github.com:itu-tid/code-examples.git 
git checkout named_counter
```

Do you have it? 


## Special Case: Empty dependencies list

**Important**: If you call an effect with an **empty dependencies list**, **it is only run once, on mount!**

Why would you want to run something only on mount? What kind of things would you want to do? Initialization. Sometimes there's special initializations that you want to have when a component is first time rendered. 

Let us imagine that we would want to not initialize our counters always with a zero, but rather, load that data from localStorage. It's a little database, that we should benefit from. The following code pattern solves this. Make sure you understand it. 

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

To play with the code, you can run in the repo above:

```
git checkout named_counters_from_local_storage
```

In the upcoming lectures you will learn how to load things from the database and you will see that the patterns are going to be the same. 

## A very special case: no dependencies 

A very special case of calling `useEffect` is with no second argument: 

```javascript
function MyComponent() {  

	useEffect(() => {  
		console.log("every render!")
	});  
	return <div />;  
}
```

**Every time the component renders, React updates the screen and then runs the code inside useEffect.** 

This is not normally used, except for debugging in my experience. 


## Releasing Resources on Component Unmount
This is ugly and won't be necessary often. But it pushes your understanding of JS syntax... and it's something that you'll need to do also in other components. Indeed, sometimes a component allocates a resource in the initialization and that resource has to be de-allocated in the component *destruction*. 

Examples of such resources could be:
- a reference to a timer
- a connection to a database
- etc.

If your effect allocates a resource that must be deallocated, do that by returning a *cleanup function*
- The syntax is ***UGLY***: **an arrow function that does the connection, and then returns another function that does the disconnect** 

![](images/effect-with-cleanup-function.png)

And  example of resource that needs to be released: a timer!

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


**Note:** During development, React runs the useEffect twice on mount

Why? if your code works in this situation, it means you're cleaning up nicely; and that's good! if not, then you have to figure out why and make it work.






# Backmatter
To try out: 
- What happens if you forget to mention the dependency in the dependencies array but you still refer to it inside of the effect function? 
