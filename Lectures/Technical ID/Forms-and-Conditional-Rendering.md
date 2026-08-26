# Forms and Conditional Rendering

Last week the app could only add whatever it felt like — the button reached into a
list of sample tasks and picked one at random. This week you type the task yourself,
which means React has to own the input, and the screen has to change shape depending
on what is in it.

## Connecting Inputs To State Via Event Handlers

The strange story of how you connect a state variable to the content of an input control in React: 

```js
import { useState } from 'react';

export default function InputExample () {
  const [answer, setAnswer] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();
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
          disabled={status === 'submitting'}
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

### This is called a `controlled component` 
- because the form elements (i.e. `textarea` in our example, are controlled by the react prop). Should probably be *controlling* ...  

## Conditional Rendering 

Often components need to display differently based on some state or prop. 

Three possible ways to render conditionally: 
1. If statements
1. The `conditional ? operator` 
1. When only one option is possible `logical && syntax` 

Note: 
- you can [conditionally return null](https://react.dev/learn/conditional-rendering#conditionally-returning-nothing-with-null) if you don't want to display a given component in some situation. 

Read and see examples at: *Describing the UI > [Conditional Rendering](https://react.dev/learn/conditional-rendering)*


# References

- *Describing the UI* > [Conditional Rendering](https://react.dev/learn/conditional-rendering)
- *Adding Interactivity* > [Reacting to Input with State](https://react.dev/learn/reacting-to-input-with-state)


## Exam Questions

### 1. What is a controlled component in React?
