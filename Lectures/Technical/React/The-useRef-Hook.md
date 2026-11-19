# The `useRef` hook

A ref is a box that keeps a value across renders, without causing a render when it changes. The most common thing to keep in it is a DOM element, so that you can focus it, scroll to it or measure it. It can also hold a timer's id, or the latest version of a callback, as `useInterval` does [below](#a-ref-keeps-the-latest-callback-without-restarting-the-timer).

## A ref hands you the real DOM element, for what React does not do: focus, scroll, measure

```js
import {useRef, useEffect} from 'react'

const InputRefExample = () => {

	  const inputRef = useRef(null);
  
	  useEffect(() => {
	    inputRef.current?.focus()
	  }, [])
  
	  return(
	    <div>
	      <input ref={inputRef} />
	      <button>
			Submit
		  </button>
	    </div>
	  )
	}
	
export default inputRefExample
```
### `ref={inputRef}` attaches the element, and `inputRef.current` is the element
1. Import `useRef`
2. Declare a ref object (i.e. `inputRef`) - initialize it with null, it's fine
3. Pass your object as the `ref` attribute to the desired DOM element
4. Refer to the DOM object by using the `current` property


### Scrolling to an element and measuring it work the same way
- scrolling to a given node
- getting the dimensions of a given DOM node
- keeping track of a timer (see the TODO list application)

### `?.` guards against a ref whose element is not on screen yet

The optional chaining (`?.`) prevents errors if the element isn't mounted yet.

```js
useEffect(() => {
  inputRef.current?.focus();
}, []);
```

## A ref keeps the latest callback without restarting the timer

[Custom Hooks](Custom-Hooks.md#a-polling-timer-belongs-in-a-hook-because-its-cleanup-is-easy-to-forget) wrote `useInterval` with the callback in the effect's dependency array:

```jsx
export function useInterval(callback, milliseconds) {
  useEffect(() => {
    const id = setInterval(callback, milliseconds);
    return () => clearInterval(id);
  }, [callback, milliseconds]);
}

// in ListPage
useInterval(reload, 10_000);
```

That version has a problem you only see in use. `reload` is created inside a function that runs on every render, so it is a **new function on every render**. It is in the dependency array, so every render clears the timer and starts a new one. Type into the form on that page, and each keystroke restarts the ten seconds: the list never reloads while you type.

Take `callback` out of the dependencies, and the opposite happens: the timer keeps the `reload` from the first render forever, with the state of the first render in it. That is the stale state of [The Render Loop and Stale State](The-Render-Loop-and-Stale-State.md#each-render-sees-its-own-copy-of-the-state), in a timer.

What the hook needs is a place to keep **the latest callback, without restarting the timer when it changes**: a value that survives renders, and whose change does not cause one. That is a ref:

```jsx
import { useEffect, useRef } from "react";

export function useInterval(callback, milliseconds) {
  const latestCallback = useRef(callback);

  // after every render, remember the newest callback; the timer is not touched
  useEffect(() => {
    latestCallback.current = callback;
  });

  // the timer starts once, and always calls whatever callback is newest
  useEffect(() => {
    const id = setInterval(() => latestCallback.current(), milliseconds);
    return () => clearInterval(id);
  }, [milliseconds]);
}
```

`ListPage` still writes `useInterval(reload, 10_000)`. All of this is inside the hook, which is the point of a hook: the tricky part has one home.

State would not work here. Setting state causes a render, and the render makes a new `reload`, which would set the state again.

## Read More

- [useRef in the react documentation](https://react.dev/learn/manipulating-the-dom-with-refs)
- Nice example of [controlling a video player component](https://react.dev/learn/synchronizing-with-effects#step-1-declare-an-effect)
	- you need to interact with the video element in the DOM
	- the DOM has already a powerful implementation of
	- get a reference to the relevant DOM element
	- call the `start` and `stop` methods


### Exam Questions

#### 1. What is the purpose of the useRef hook?

#### 2. What does this code do and why use optional chaining?
```js
const inputRef = useRef(null);

useEffect(() => {
  inputRef.current?.focus();
}, []);

return <input ref={inputRef} />;
```

#### 3. Why does `useInterval` keep the callback in a ref instead of putting it in the effect's dependency array? Why would state not work instead of the ref?
