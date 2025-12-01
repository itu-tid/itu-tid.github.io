# Exam Questions - Lecture 5: Authorization and Access Control

## Conceptual Questions

### 1. Why can't Parse API keys be kept secret in a web application?

### 2. What is the difference between authentication and authorization?

### 3. What are the three methods of access control in Parse?

### 4. What is an ACL and at what level does it operate?

## Code Analysis Questions

### 5. Explain what this code does:
```js
const privateNote = new Note();
privateNote.set("content", "My secret");
privateNote.setACL(new Parse.ACL(Parse.User.current()));
await privateNote.save();
```

### 6. How would you make an object publicly readable but only writable by the owner?

### 7. What's the problem with this code if we only validate name length on the client?
```js
// Client-side validation
if (name.length > 200) {
  alert("Name too long!");
  return;
}
await todoItem.save();
```

### 8. What are two benefits of placing this code in a separate service file rather than directly in a React component?
```js
export async function fetchTodosByCategory(category) {
  const query = new Parse.Query(TodoItem);
  query.equalTo("category", category);
  query.equalTo("userId", Parse.User.current());
  const results = await query.find();
  return results.map(todoItemToPlainObject);
}
```

## Practical Questions

### 9. What are the two types of roles in Parse and how do they differ?

### 10. Why can't ACLs be set at the field level, and what's the workaround?


