# Field-Level Permissions, and the Two-Table Workaround

In [Authentication and Authorization (in Parse)](Authorization-and-ACL-in-Parse.md) every permission we set applied to a whole object. That is the only granularity Parse offers, and sooner or later you want less than that.

## ACL does not work at the field level

In Parse, **ACLs work at the object level, not at the field/column level**. You cannot make some fields public and other fields private within the same object.

The example that forces the issue:

- You want everyone to **see your to-do's task name** and done status (public read).
- But you want to **keep your time-tracking data private** (only you can read it).

One object, two audiences. There is no ACL that expresses it.

### Problem: you cannot set some fields private and some public

```js
// This does NOT work - you can't set different permissions per field
const todo = new TodoItem();
todo.set("text", "Write report");            // want this PUBLIC
todo.set("done", false);                     // want this PUBLIC
todo.set("totalTime", 3600000);              // want this PRIVATE
todo.set("currentSessionStart", new Date()); // want this PRIVATE

const acl = new Parse.ACL(currentUser);
acl.setPublicReadAccess(true); // This makes ALL fields public!
todo.setACL(acl);
```

The ACL is a property of the row, not of any column in it. `setPublicReadAccess(true)` opens every field at once, `totalTime` along with `text`.

### Solution: split the data into two tables with a 1-to-1 relationship

If the permissions differ, the objects differ. Put the public fields in one class and the private ones in another, and point the second at the first.

**Table 1: TodoItem (public)**

```js
const TodoItem = Parse.Object.extend("TodoItem");
const todo = new TodoItem();
todo.set("text", "Write report");
todo.set("done", false);
todo.set("owner", currentUser);

// Public read, owner write
const acl = new Parse.ACL(currentUser);
acl.setPublicReadAccess(true);
todo.setACL(acl);
await todo.save();
```

**Table 2: TodoTimeTracking (private)**

```js
const TodoTimeTracking = Parse.Object.extend("TodoTimeTracking");

const timeTracking = new TodoTimeTracking();

timeTracking.set("todoId", todo);  // Pointer to the TodoItem
timeTracking.set("totalTime", 3600000);
timeTracking.set("currentSessionStart", new Date());
timeTracking.set("owner", currentUser);

// Private - only owner can read and write
const acl = new Parse.ACL(currentUser);
timeTracking.setACL(acl);
await timeTracking.save();
```

The pointer is the same mechanism as any other one-to-one relationship — see [Relationships Between Object Classes](Relationships-Between-Object-Classes.md). What is new is the *reason* for the split: not that the data is a separate thing, but that it needs a separate ACL.

### Exam Questions

#### 1. Why can't ACLs be set at the field level, and what's the workaround?

#### 2. You split a to-do's private time-tracking into its own class. What stops another user reading it, given they can already read the `TodoItem` it points at?
