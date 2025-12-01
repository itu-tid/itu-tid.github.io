# Exam Questions - Lecture 4: Backends and Parse Platform

## Conceptual Questions

### 1. What is the difference between front-end and back-end?

### 2. List at least 5 responsibilities of a backend.

### 3. What is Parse Platform and what does it provide?

### 4. What does CRUD stand for and what do each of the letters represent?

## Code Analysis Questions

### 5. Explain what this code does:
```js
const TodoItem = Parse.Object.extend("TodoItem");
const newItem = new TodoItem();
newItem.set("name", "Buy milk");
newItem.set("done", false);
await newItem.save();
```

### 6. What is wrong with this query pattern?
```js
const query = new Parse.Query("Post");
const posts = await query.find();

for (let post of posts) {
  const userQuery = new Parse.Query("User");
  const user = await userQuery.get(post.get("userId"));
  console.log(user.get("username"));
}
```

### 7. How do you get the currently logged-in user in Parse?

### 8. Explain the difference between Pointers and Relations in Parse.

## Practical Questions

### 9. How would you query all TodoItems where done is false, ordered by creation date?

### 10. Why are Join Tables often preferred over Parse Relations for many-to-many relationships?

### 11. What is the loading notification pattern and why is it important?
