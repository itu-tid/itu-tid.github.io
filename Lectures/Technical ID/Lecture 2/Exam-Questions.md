# Exam Questions - Lecture 2: Advanced React Patterns

## Conceptual Questions

### 1. What does "lifting state up" mean in React?

### 2. Explain the three patterns of component communication in React.

### 3. Why should you avoid mutating state objects directly in React?

### 4. What is the purpose of the useRef hook?

## Code Analysis Questions

### 5. What will be displayed after clicking the "+3" button?
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

### 6. How would you add a new item to the beginning of this array in state?
```js
const [artists, setArtists] = useState([
  { id: 1, name: "Picasso" },
  { id: 2, name: "Monet" }
]);
```

### 7. How would you remove an item with id=2 from the previous artists array?

### 8. What does this code do and why use optional chaining?
```js
const inputRef = useRef(null);

useEffect(() => {
  inputRef.current?.focus();
}, []);

return <input ref={inputRef} />;
```

## Practical Questions

### 9. How would you update a nested object in state?
Given:
```js
const [person, setPerson] = useState({
  name: "Alice",
  address: {
    city: "Copenhagen",
    country: "Denmark"
  }
});
```
Update only the city to "Aarhus".

### 10. Why is this principle important: *"Code in a component should be at the same abstraction level"*?

### 11. When would you use an updater function vs. passing a direct value to setState?
