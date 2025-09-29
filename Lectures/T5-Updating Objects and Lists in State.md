
## [Updating Objects in State](https://react.dev/learn/updating-objects-in-state)

Modifying an object is called **mutating an object**.

**What to understand**
- you don't mutate state objects in React because react does not *see* that
- **modifying objects** is *easiest* with the *spread syntax*: 
	![](./images/spread-syntax.png)
- updating nested objects is ... a little bit ugly
	![](./images/nested-object-definition.png)![](./images/updating-nested-objects.png)





## [Updating Arrays in State](https://react.dev/learn/updating-arrays-in-state)

Use spread syntax to create a copy of an array, e.g. `[...artists]`.


**What to understand**

- Once you have a copy, you can simply **add elements at the end**, e.g. 

```javascript
setArtists( 
	[ 
		...artists, // that contains all the old items  
		{ id: nextId++, name: name } // and one new item at the end  	
	]  
);
```

- or you can prepend the element to add it at the beginning

```javascript
setArtists([  
	{ id: nextId++, name: name },  
	...artists // Put old items at the end  
]);
```

- **Removing an element from an array**: `filter` (because filter *does not mutate the object* but returns a new one)

```javascript
setArtists(  
	artists.filter(a => a.id !== artist.id)  
);
```


- Replacing an element in the array can be done with `**map**` 
	- map = one of the most important functions in functional programming 
	- Google invented a whole new big data processing around it named MapReduce

```javascript
  function handleClick() {
    const nextShapes = shapes.map(shape => {
      if (shape.type === 'square') {
        return shape;
      } else {
        return {
          ...shape,
          y: shape.y + 50,
        };
      }
    });
    setShapes(nextShapes);
  }
```
 ( [example](https://codesandbox.io/s/s4vvyz?file=%2FApp.js&utm_medium=sandpack))

- Inserting an element  can be done with two uses of `slice`: 

```javascript
  function handleClick() {
    const insertAt = 1; // Could be any index
    const nextArtists = 
	[
      
      // Items before the insertion point:
      ...artists.slice(0, insertAt),
      
      // New item:
      { id: nextId++, name: name },
      
      // Items after the insertion point:
      ...artists.slice(insertAt)
    ];
    setArtists(nextArtists);
    setName('');
  }

```

- Sorting, reversing - `reverse`, `sort` -- they mutate the array. But it's ok if you copy the array first, and then mutate it the way you like

```
let reversedArtists = [...artists].reverse();
```


