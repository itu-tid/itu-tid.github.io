# Forms and Conditional Rendering

Last week the app could only add whatever it felt like — the button reached into a list of sample tasks and picked one at random. This week you type the task yourself, which means React has to own the input, and the screen has to change shape depending on what is in it.

Two topics in one note, because they arrive together: the moment you can add items you can also remove them, and the moment the list can be empty the screen needs to say something other than nothing.

## Connecting Inputs To State Via Event Handlers

The strange story of how you connect a state variable to the content of an input control in React:

```js
import { useState } from 'react';

export default function InputExample () {
  const [answer, setAnswer] = useState('');

  async function handleSubmit(e) {
    
    e.preventDefault(); // prevent sending the page to the server. we're a single page application. we'll see more about that later.
    
    // do something with the answer 
    // ... 
  }

  function handleTextareaChange(e) {
    setAnswer(e.target.value);
  }

  return (
    <>
  
	  <form onSubmit={handleSubmit}>

		<textarea
          value={answer}
          onChange={handleTextareaChange}
        />
        <br />
        
        <button disabled={answer.length === 0}>
          Submit
        </button>
      
      </form>
    </>
  );
}
```

Notice `disabled={answer.length === 0}`: the button's state is *derived* from the answer, not stored separately. Nothing has to remember to switch it on and off — it is a function of the state, recomputed on every render. That is the pattern to reach for whenever you catch yourself about to add a second piece of state that is really about the first.

### This is called a `controlled component` 
- because the form elements (i.e. the `textarea` in our example) are controlled by the React state. Should probably be *controlling component* ...

The input has no memory of its own. It shows what state says, and every keystroke goes back through the setter — so there is exactly one place where the truth lives, and the screen cannot disagree with the app.

## Conditional Rendering 

Often components need to display differently based on some state or prop.

The moment a list can be added to and deleted from, it can also be **empty** — and an empty `<ul>` on screen looks like a bug rather than an achievement. That is the first place you need this:

```jsx
{todos.length === 0 && <p>Nothing to do. Enjoy the afternoon.</p>}
```

Three possible ways to render conditionally:

**1. An `if`, before the `return`** — best when whole branches differ:

```jsx
function TodoItem({ text, done }) {
  if (done) {
    return <li className="done"><s>{text}</s></li>;
  }
  return <li>{text}</li>;
}
```

**2. The `? :` operator**, inside the JSX — best when only a small part changes:

```jsx
<li>{done ? <s>{text}</s> : text}</li>
```

**3. `&&`**, when there is nothing to show in the other case:

```jsx
{todos.length === 0 && <p>Nothing to do. Enjoy the afternoon.</p>}
```

A warning about that last one. `&&` returns its **left** side when the left side is falsy — so `{todos.length && <p>…</p>}` renders a literal **0** on the page when the list is empty, because `0` is falsy but is still something React will happily display. Compare explicitly (`=== 0`, `> 0`) and the problem disappears.

Note:
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation.

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*


# References

- *Describing the UI* > [Conditional Rendering](https://react.dev/learn/conditional-rendering)
- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)


## Exam Questions

### 1. What is a controlled component in React?
