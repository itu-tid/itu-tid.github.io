# Updater functions for state

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