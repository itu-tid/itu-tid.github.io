## parent to child via props

## child to parent via callbacks

![[../../Pasted image 20250929145919.png]]

## sibling to sibling? 

Sometimes, you want the state of two components to always change together. 

### Lifting the state up
To do it, remove state from both of them, move it to their closest common parent, and then pass it down to them via props. 

This is known as _lifting state up,_ and it’s one of the most common things you will do writing React code.

Finally, pass the event handlers down so that the children can change the parent’s state <- example of **child-to-parent communication**!!! 

**Example**: in the TODO list application, ensuring that one can't start two tasks 

**To read for next time**: [Sharing state between components](https://react.dev/learn/sharing-state-between-components)
- talks about lifting state with an example

