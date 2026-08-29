# Updater functions for state

> **You will not need this in week 2.** `setTodos([...todos, item])` is correct wherever
> you are reading the state and writing it back in the same breath — adding, deleting,
> toggling. The updater form earns its keep only when the value you captured has gone
> stale: two setter calls in one handler, or a callback that fires later — a response
> arriving, a timer, a live query pushing a change. That is why this note sits with the
> backend material rather than with `useState`.

State can be updated with either **updater functions** like in the first button below or by calling the setter function with an actual value, the second button below. One increments with three the value of the state var. The other with one.  

```js
  export defult function Counter() {
  
    const [number, setNumber] = useState(0)
  
	  return (
	    <>
	      <button onClick={() => {
	        
	        // updater function that takes a callback
	        // all the ones below are the same
	        // the name of the vaiable does not matter!
	        setNumber(x => x + 1);
	        setNumber(n => n + 1);	        
	        setNumber(number => number + 1);	
	      }}>+3</button>
	      
	      <button onClick={() => {
	        
	        // direct update of variable
	        // although you call it three times,  value is incremented with 1!
	        setNumber(number + 1);
	        setNumber(number + 1);
	        setNumber(number + 1);
	      }}>+1</button>	      
	    </>
    }

```
**Updater Function** vs. **Calling with Actual Value**
- difference is between passing a callback and an actual value to the react state updater
- the updater will do this work at a later point, we don't control when that happens



## Why would you use this
- [Queueing A Series of State Updates](https://react.dev/learn/queueing-a-series-of-state-updates)
- When a lambda function risks capturing a stale state


## Exam Questions

### 1. What will happen when the button is clicked three times?
```js
function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
    setCount(count + 1);
    setCount(count + 1);
  }

  return <button onClick={handleClick}>{count}</button>;
}
```

### 2. What will be displayed after clicking the "+3" button?
```js
function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <button onClick={() => {
      setNumber(n => n + 1);
      setNumber(n => n + 1);
      setNumber(n => n + 1);
    }}>+3: {number}</button>
  );
}
```

### 3. When would you use an updater function vs. passing a direct value to setState?
