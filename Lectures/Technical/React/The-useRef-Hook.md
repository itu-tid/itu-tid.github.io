# The `useRef` hook

A ref is a box that keeps a value across renders, without causing a render when it changes. The most common thing to keep in it is a DOM element, so that you can focus it, scroll to it or measure it. It can also hold a timer's id, or the latest version of a callback, as `useInterval` does in [Custom Hooks](Custom-Hooks.md#a-ref-keeps-the-latest-callback-without-restarting-the-timer).

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
