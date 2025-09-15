

# [Using `useRef` for manipulating DOM elements](https://react.dev/learn/manipulating-the-dom-with-refs)

Sometimes you want to manipulate the DOM in ways that React does not help you to. E.g. 
- ***automatically focusing a given element*** when a component is first time rendered.  
- scrolling to a given node
- getting the dimensions of a given DOM node


The `useRef` hook returns an object with one property: `current`. 
It is persisted between renders. 


Example of **automatically focusing a given element on first render**: 
1. import `useRef`
2. declare a ref object (i.e. `inputRef`)
3. pass your object as the `ref` attribute to the desired DOM element

```js
import {useRef, useEffect} from 'react'

const InputRefExample = () => {

	  const inputRef = useRef(null);
  
	  useEffect(() => {
	    inputRef.current.focus()
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


Nice example: [controlling a video player component](https://react.dev/learn/synchronizing-with-effects#step-1-declare-an-effect)
- you need to interact with the video element in the DOM 
- get a reference to the relevant DOM element
- call the `start` and `stop` methods 
