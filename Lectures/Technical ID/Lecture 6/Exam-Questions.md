# Exam Questions - Lecture 6: Efficient Backend Communication and Server-Side Code

## Conceptual Questions

### 1. What is the N+1 select problem and why is it important?

### 2. How do you solve the N+1 problem in Parse?

### 3. What is the difference between polling and event-driven (LiveQuery) approaches for real-time updates?

### 4. When should you run code on the server instead of the client?

## Code Analysis Questions

### 5. What's wrong with this useEffect for polling?
```js
useEffect(() => {
  const interval = setInterval(() => {
    fetchMessages();
  }, 5000);
}, []);
```
Hint: resource cleanup.


### 6. Explain what this cloud function does:
```js
Parse.Cloud.beforeSave("TodoItem", (request) => {
  const name = request.object.get("name");
  if (!name || name.trim().length === 0) {
    throw new Parse.Error(400, "Todo name cannot be empty");
  }
});
```

### 7. What do `select` and `exclude` do in Parse queries?
```js
query.select('title', 'completed');
// vs
query.exclude('description', 'attachments');
```

### 8. Explain this LiveQuery subscription:
```js
subscription.on('enter', (todo) => {
  console.log('Todo entered query:', todo.get('title'));
});
```

## Practical Questions

### 9. What is the difference between `afterSave` and `beforeSave` triggers?

### 10. What are WebSockets and why does LiveQuery use them?


