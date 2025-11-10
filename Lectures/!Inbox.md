- talk about configuration and envvars 
- 
- to put this somewhere, ## It's *components all the way down*
- Most basic components: e.g. buttons
- Most elaborate component: full web page or mobile screen -- probably when we talk about folder structure
- this comes from the beginning of T1- hooks and effects - but does not belong there.
	- [The JSON namespace in the browser](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
	- [localStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) includes the global object `localStorage` and the methods `setItem` and `getItem` which both *work on strings*
- questions to know
	- - What is the relationship between react, npm and Javascript?



Two types of logic inside React components:

1. **Rendering code** => a transformation from props & state into JSX. This is *purely functional code*  -- for the same props and state it will always return the same JSX. 
2. **Event handlers** => functions that do things -- change state, submit HTTP POST request, navigate to another screen, interact directly with the DOM (e.g. change page title)



- What happens if you forget to mention the dependency in the dependencies array but you still refer to it inside of the effect function? 