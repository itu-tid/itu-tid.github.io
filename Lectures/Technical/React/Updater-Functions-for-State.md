# Updater functions for state

> **You do not need this yet.** `setTodos([...todos, item])` is correct wherever you read the state and write it back in the same breath — adding, deleting, toggling. The updater form earns its keep only when the value you captured has gone stale: two setter calls in one handler, or a callback that fires later — a response arriving, a timer, a live query pushing a change.

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


## The other way the setter surprises you: editing what is already in state

Since week 2 you have been building new arrays and new objects rather than editing the ones you had:

```jsx
setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
```

Here is what that habit was protecting you from. This is the version people write when they are in a hurry:

```jsx
const copy = [...todos];                       // a new array...
copy.find((t) => t.id === id).done = true;     // ...holding the SAME objects
setTodos(copy);
```

The array is genuinely new, so React sees a change and re-renders, and the screen is right. **This code works**, which is the whole problem with it: nothing tells you off, so the habit survives.

What it did was reach into a to-do React was already holding and edit it where it lay. That costs you as soon as anything else is holding the same object:

- **Anything that kept the previous list** — an undo stack, or a comparison of before and after — is now holding a list whose contents changed underneath it. The past was rewritten.
- **Anything that skips work by comparing objects** — a memoised child, an effect with the item in its dependency array — sees the same object it saw last time and concludes nothing changed. The screen goes stale, and nothing looks wrong in your code.

React is built on the assumption that what you put in state is never edited afterwards. So:

**Treat everything already in state as read-only.** To change it, build the new version and hand *that* to the setter — which is what `map` with a spread has been doing all along.

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

### 4. This code gives the setter a brand-new array, the screen updates, and it is still wrong. Why?
```jsx
const copy = [...todos];
copy.find((t) => t.id === id).done = true;
setTodos(copy);
```
