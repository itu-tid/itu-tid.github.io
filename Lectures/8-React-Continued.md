
## Render and Commit -- More on Reactive Programming with React
Source: [Render and Commit](https://react.dev/learn/render-and-commit)

Notes:
- the restaurant metaphor is not very useful

**What to understand**
- What triggers a component re-render? Change of state in that component
- Besides the re-rendered component, all it's children will also be re-rendered
- Multiple state changes might be batched in the same re-render
- Rendering is logical - react has a virtual DOM that it updates - then updates the real DOM only in those parts where this is necessary

## State Does Not Change Inside an Event Handler
Source: [State as a Snapshot](https://react.dev/learn/state-as-a-snapshot)

Notes:
- the snapshot metaphor I don't find very useful
- the first image that shows react updating the DOM tree is good
- the state is not changed immediately after you call the setter, but later when React does all the state changes. Try to understand the [examples](https://react.dev/learn/state-as-a-snapshot#state-over-time)!

## Queueing A Series of State Updates
Source: [docs](https://react.dev/learn/queueing-a-series-of-state-updates)

What to understand
- Updater Functions (cool concept, not needed often)
- Setting state does not change the variable in the existing render, but it will be changed in the  new render

## Updating Objects in State
Source: [Updating Objects in State](https://react.dev/learn/updating-objects-in-state)

What to understand
- you can't modify a state object - you have to use the setter and provide a new object instead
- modifying objects with the spread syntax
	![[spread-syntax.png]]
- updating nested objects is ... a little bit ugly
	![[nested-object-definition.png]]![[updating-nested-objects.png]]