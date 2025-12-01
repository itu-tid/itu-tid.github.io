# Exam Questions - Lecture 1: Introduction to React

## Conceptual Questions

### 1. What is JSX and how does it differ from HTML?

### 2. Explain the difference between props and state in React.

### 3. What is a controlled component in React?

### 4. Why do we need to use a `key` attribute when rendering lists in React?

## Code Analysis Questions

### 5. What will happen when the button is clicked three times?
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

### 6. What is wrong with this component?
```js
function Greeting() {
  return (
    <h1>Hello</h1>
    <p>Welcome to React</p>
  )
}
```

### 7. Explain what this useEffect does:
```js
useEffect(() => {
  localStorage.setItem("clicks", clicks);
}, [clicks]);
```

## Practical Questions

### 8. What is the difference between these two useEffect calls?
```js
// Version A
useEffect(() => {
  console.log("Effect A");
}, []);

// Version B
useEffect(() => {
  console.log("Effect B");
});
```

### 9. When would you use a cleanup function in useEffect?

### 10. What are the rules for using React hooks?
