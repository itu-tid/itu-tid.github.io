
# The useRef hook

Allows you to get hold of a DOM element and manipulate it 

## Example: Automatically focusing a given element on first render

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
## Canonical use of the `useRef` hook
1. Import `useRef`
2. Declare a ref object (i.e. `inputRef`) - initialize it with null, it's fine
3. Pass your object as the `ref` attribute to the desired DOM element
4. Refer to the DOM object by using the `current` property 


## Other Examples of  manipulating the DOM 
- scrolling to a given node
- getting the dimensions of a given DOM node
- keeping track of a timer (see the TODO list application)

## Notes

### Optional chaining to prevent errors

The optional chaining (`?.`) prevents errors if the element isn't mounted yet.

```js
	  useEffect(() => {
	    inputRef.current?.focus()
	  }, [])
```

#### The reference is persisted between renders

#### State changes of the referenced element are not observed by React

# Read More

- [useRef in the react documentation](https://react.dev/learn/manipulating-the-dom-with-refs)
- Nice example of [controlling a video player component](https://react.dev/learn/synchronizing-with-effects#step-1-declare-an-effect)
	- you need to interact with the video element in the DOM 
	- the DOM has already a powerful implementation of 
	- get a reference to the relevant DOM element
	- call the `start` and `stop` methods 
