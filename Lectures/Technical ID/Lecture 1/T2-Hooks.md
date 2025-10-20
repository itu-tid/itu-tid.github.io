
# React Hooks 

## Special React functions for "hooking into" the framework
### Their name starts with `use`

Most popular: 
- `useState` -- to allow you to define state
- `useEffect` -- to allow you to handle side effects (see below)
- `useRef` -- an object that can be persisted across renderings but is not state (see below)
### Called at the top of the component
### Can be called from another hook or directly from a component
### Can NOT be called from within a conditional expression or nested functions
- would throw off the internal implementation
- react does not compile your code if you try to 

