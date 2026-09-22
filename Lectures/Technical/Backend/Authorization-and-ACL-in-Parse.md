# Authentication and Authorization (in Parse)

Two words that sound alike and mean different things, which is why they belong in the same lecture:

- **Authentication** — proving that a user is who they say they are. *Who are you?*
- **Authorization** — deciding what that user is then allowed to do. *What are you allowed to touch?*

The first half of today gives your app accounts. The second half stops those accounts from reading each other's data. Neither half is worth much without the other: accounts that everyone can read through are theatre, and permissions with nobody to attach them to are unusable.

# Part 1: Authentication

## Parse gives you accounts, login and the current user without your writing any of it

The Javascript Parse SDK helps you manage user accounts and track the logged in user. `_User` is a class that already exists in your database, with `username`, `password` and `email` already on it, and with the password already being hashed for you.

### Signing up and logging in

```jsx
import { useState } from 'react';
import Parse from 'parse';

export default function AuthPage({ onAuthenticated }) {
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const [error, setError] = useState('');

	async function handleSignUp(e) {
		e.preventDefault();
		setError('');
		try {
			const user = new Parse.User();
			user.set('username', username);
			user.set('password', password);
			await user.signUp();
			onAuthenticated(user);
		} catch (err) {
			setError(err.message);
		}
	}

	async function handleLogin(e) {
		e.preventDefault();
		setError('');
		try {
			const user = await Parse.User.logIn(username, password);
			onAuthenticated(user);
		} catch (err) {
			setError(err.message);
		}
	}

	return (
		<div>
			<h1>Welcome</h1>
			{error && <p style={{ color: 'red' }}>{error}</p>}

			<form>
				<input
					type="text"
					placeholder="Username"
					value={username}
					onChange={(e) => setUsername(e.target.value)}
				/>
				<input
					type="password"
					placeholder="Password"
					value={password}
					onChange={(e) => setPassword(e.target.value)}
				/>
				<button onClick={handleSignUp}>Sign Up</button>
				<button onClick={handleLogin}>Log In</button>
			</form>
		</div>
	);
}
```

What happens:
- `user.signUp()` creates a new user, and logs them in
- `Parse.User.logIn()` logs in an existing one
- Both of them manage the session for you
- Log out with `await Parse.User.logOut()`

### Showing the login page, without a router

Both handlers finish by calling `onAuthenticated`. They do *not* navigate anywhere, because we have no router yet — that is week 6. We do not need one:

```jsx
function App() {
	const [user, setUser] = useState(Parse.User.current());

	if (!user) {
		return <AuthPage onAuthenticated={setUser} />;
	}

	return <ToDoList user={user} onLogOut={() => Parse.User.logOut().then(() => setUser(null))} />;
}
```

This is [conditional rendering](../React/Conditional-Rendering.md) again, in its whole-screen form: either the app, or the way in. A router will later give each of these its own URL, which is a real improvement — but notice that what a router adds here is *addressability*, not the gating. The gating is this `if`.

### Getting the current user

It would be silly if the user had to login every time they opened the app, so Parse stores the logged-in user in `localStorage` and hands them back to you:

```jsx
const currentUser = Parse.User.current();
if (currentUser) {
	// do stuff with the user
} else {
	// show the signup or login page
}
```

This is why `useState(Parse.User.current())` above is safe as a `useState` initializer while `fetchTodos()` was not: `current()` reads from `localStorage` and is synchronous. No network, no waiting, no third state.

### Logging out

```jsx
await Parse.User.logOut();
// Parse.User.current() is now null
```

### How the server knows it is still you

Open the developer tools right after logging in, and look in **Application → Local Storage**. Parse has stored the current user there, and inside it a `sessionToken`: a long random string that the server handed out when your password checked out.

The reason it exists: **HTTP is stateless.** The server forgets you the moment it has answered a request. So from now on every call your app makes carries that token, and the token is what proves who is calling. Your password was sent once, at login; the token is sent every time instead.

Two things worth being precise about:

- The token is **not encrypted**. It is random, and meaningless to anyone who does not have the database. What protects it on its way to the server is **HTTPS**, which encrypts the whole connection.
- Whoever has it, *is you*. Copy it out of this browser into another one, and the server cannot tell the difference. This is called **session hijacking**, and it is why `logOut()` does not merely delete the token from your browser: it destroys the session **on the server**, so the copied token stops working too.

# Part 2: Authorization

## Motivation

##### **Why can you not keep the Parse API keys perfectly secret?**
- Remember the architectural diagram from the beginning of the course? bundle.js is sent to the browser...
- The JavaScript code of your web application can be inspected by another web programmer.

###### See it, rather than take my word for it

Open your own to-do app, open the developer tools on the **Network** tab, and tick a checkbox. One request appears. Click it, and look at what your app sent:

```
POST https://parseapi.back4app.com/parse/classes/TodoItem/AbC123xY

{"done":true, "_method":"PUT",
 "_ApplicationId":"YOUR_APP_ID",
 "_JavaScriptKey":"YOUR_JS_KEY",
 "_SessionToken":"r:aBcD1234..."}
```

There they are. Not hidden in the bundle, not obfuscated — **written in plain text in the body of every single request**, by your own code, because the server has no other way of knowing who is calling.

Anybody who can open your app can read them. That is not a bug in Parse, and there is no setting that fixes it: a key that the browser must send is a key the browser's owner can read.

Now look at the two credentials in there, because the difference between them is this entire lecture:

- `_ApplicationId` and `_JavaScriptKey` say **which application is calling**. Every visitor has them. They identify your app, and they prove nothing about the person using it.
- `_SessionToken` appeared when you logged in an hour ago. It says **who is calling**. It is yours, it is secret, and it is the only thing in this request that the server can use to tell you from anybody else.

Everything we build today hangs off that second line. The keys cannot protect anything, so the protection has to be attached to the user.

And two more things are visible in that same request, both of which matter shortly: the **class name** (`TodoItem`) and the **object id** — so a stranger now knows what your tables are called, and can address individual rows in them.

##### **What happens if I access your repository and find your AppID and JSKey?**
- Read info that is not meant for me
- Delete useful information
- Store my movie collection in your tables
- etc.

That is - **only if you have made your tables public**
- When we created the DB we were asked about access control and we agreed to make everything public because we're working on an MVP.
- Now it's time to harden the security of our database


## What can we do if the API keys can't be made secret?

Use access control in such a way that even with the keys, no harm can be done. Parse gives you three layers, and we take them from the most concrete to the coarsest:

1. **Object level** — who can read and write *this row* (ACLs)
2. **Class level** — who can touch *this table* at all (class-level permissions)
3. **Schema level** — who can create *new tables* (client class creation)

## 1. Object-Level Permissions: Access Control Lists

### See the problem first

Open your app in two windows side by side: a normal one and an incognito one. Their local storage is separate, so you can be logged in as two different users at once. Log in as Ada on the left, as Anka on the right.

Ada creates a to-do. Refresh Anka's window: **Anka can see it.** Every user sees every to-do, because nothing in the database says whose it is or who may read it.

### The fix: an ACL on every object

An **Access Control List** is attached to one object, and says who may do what to it. They allow you to set **fine-grained permissions** for every row in your table. Usually they are **created at the same time** as the object.

```js
export const createTodoItem = async (text) => {
	const currentUser = Parse.User.current();

	const item = new TodoItem();
	item.set("text", text);
	item.set("done", false);

	item.setACL(new Parse.ACL(currentUser)); // ← only the creator can read and write

	const result = await item.save();
	return toPlainObject(result);
};
```

Ada creates another to-do, Anka refreshes, and this one does not appear.

**But the old one still does.** An ACL is set on an object when it is saved; it does not reach back to objects saved before your code changed. The to-dos created without an ACL are still readable and writable by everybody, and will stay so until you give them one. You will meet this in your own project, as old test data that behaves differently from new data.

##### Who can ACL permissions apply to?
  - Public
  - Specific users
  - Roles

##### Privileges per object
  - Read - can retrieve/query this object
  - Write - can update or delete this object

### `new Parse.ACL(user)` is shorthand 
```js
	const acl = new Parse.ACL();
	acl.setReadAccess(currentUser, true);
	acl.setWriteAccess(currentUser, true);
	item.setACL(acl);
	
	// is equivalent to
	
	const acl = new Parse.ACL(currentUser);
	item.setACL(acl);
```

### More examples
###### User creates a private note

In the following example, a logged in user, creates a private note and ensures that it is only himself that can access that note:

```js
const Counter = Parse.Object.extend("Counter");
const privateCounter = new Counter();
privateCounter.set("name", "Times Checked Twitter");
privateCounter.set("count", 42);
privateCounter.setACL(
	new Parse.ACL(Parse.User.current()));
privateCounter.save();
```

###### Read for public but write only for owner
It is sometimes desirable that an object can be **read by other users**, but just **can not be written by them**. For such a case the `Parse.ACL` object offers the `setPublicReadAccess(true)` method call:
```js
const Post = Parse.Object.extend("Post");
const publicPost = new Post();
publicPost.set("content", "I love technical interaction design");
publicPost.setACL(new Parse.ACL(Parse.User.current()));
publicPost.setPublicReadAccess(true);
publicPost.save();
```
Access control lists can be modified every time an object is saved.

### Sharing, and public read

###### Sharing with another user

```js
  const acl = new Parse.ACL(currentUser); // owner has full access
  acl.setReadAccess(otherUser, true);   // other user can read
  acl.setWriteAccess(otherUser, true);  // other user can write
```
###### Public read - owner write
```js
  const acl = new Parse.ACL(currentUser); // owner has full access
  acl.setPublicReadAccess(true);  // anyone can read
```
## 2. Class-Level Permissions

ACLs decide *which rows* a user can open. Class-level permissions sit in front of them and decide whether a user may touch the class *at all*.

For every class you choose who has access and with which privileges.

###### Who has access can be specified with multiple levels of granularity
  - Public (anyone, even unauthenticated)
  - Authenticated users (requiresAuthentication)
  - Specific users
  - Roles

###### Privileges for the entire class
 - Get - retrieve individual objects by ID
 - Find - query for objects
 - Create - create new objects
 - Update - modify existing objects
 - Delete - delete objects
 - Add Fields - add new fields to the schema

The image below shows the Parse UI for setting Class-level permissions
![](../images/class-level-permissions-in-parse.png)

### Try it: only logged-in users may create to-dos

Somebody without an account has no business creating to-dos. In the dashboard, open the class-level permissions of `TodoItem` and require authentication for **Create**. Then log out, and try to save a to-do: the server refuses.

One toggle, and one layer of the lecture becomes visible. Class level says who may knock; the ACL says which rows open.

### The exception: `_User`

Every other class tightens. One class cannot: **`_User` must keep Create public**, because signing up *is* creating a user, and the person signing up is by definition not logged in yet.

What must not stay public on `_User` is everything else. By default a user can only modify their own user object, but user objects can be read by anyone — so with the keys from your bundle, a stranger could list every account in your app. Turn **Find** off for the public in the `_User` class-level permissions. Create stays open; the rest does not.

<!-- TODO before Thursday: check on Back4App exactly which _User CLP columns can be turned off without breaking login and Parse.User.current(). -->

## 3. Restricting Class Creation

Surely, not all users should be allowed to create classes either!

Under `App Settings > Server Settings > Client Class Creation` you can specify if your expect users to be allowed to create new classes in your database. Very handy in week one, when saving to a class that does not exist yet simply creates it. Very dangerous in production, where anyone with your keys can do the same. Turn it off.

## Combining the three

The methods above should be combined together to strengthen the DB access for your application.

![](../images/parse-server-access-control.png)

In practice, there's no real reason to have any public tables. If it's a public list of objects, they can be hardcoded in the application.

## Roles, in one sentence

If your design has **named groups of users that are reused** across many objects — a family, a team, the moderators — look up **roles**: a role is an object that holds users, and you can put a role into an ACL instead of listing the users one by one. For one-off sharing with a person or two, putting them in the ACL directly is simpler.

<details>
<summary>More on roles, for when your project needs them</summary>

###### Role-Based Access
```js
  const acl = new Parse.ACL(currentUser);
  acl.setRoleReadAccess("TeamMembers", true);
  acl.setRoleWriteAccess("TeamMembers", true); 
```
###### Two types of roles
###### **Application-level roles** (Moderators, Admins, Premium Users)
- Created manually in Parse Dashboard or via Cloud Code
- Managed by the app administrators, not end users
- Public read of the role is normal - users should see who the moderators are

###### **User-created roles** (e.g. Family, MyTeam, ProjectX)
- Created programmatically by regular users from the app
- Each user manages their own teams
- Private - no reason for others to see them

```js
  // Say user creates a "TeamMembers" role
  
  const roleACL = new Parse.ACL(currentUser);
  
  const role = new Parse.Role("TeamMembers", roleACL);

  // Later our user can add other users to this role
  role.getUsers().add(user1);

  await role.save();
```

</details>

## The query is a convenience; the ACL is the security

Next, in [Relationships Between Object Classes](Relationships-Between-Object-Classes.md), we give every to-do an owner and query for "only mine" explicitly. That query is useful. It is not what protects anybody: a filter like `equalTo("owner", …)` is something *our* client chooses to send, and nothing obliges anyone else to send it. They do not even need your client: `npm install parse`, twenty lines of Node, and the App ID and JavaScript key they read out of the bundle you shipped them. Then they run whatever query they like — and what stops them is the ACL, on the server.

## Field-level permissions

An ACL covers a whole object, so it cannot make one field public and another private. When you need that — a to-do whose text is shared but whose time-tracking is not — the data has to be split across two classes. That is week 12's subject: [Field-Level Permissions, and the Two-Table Workaround](Field-Level-Permissions.md).

## Reading
From the ParsePlatform.org Guide:
- [Class-level Permissions](https://docs.parseplatform.org/js/guide/#class-level-permissions)
- [Object-level Access Control](https://docs.parseplatform.org/js/guide/#object-level-access-control)


### Exam Questions

#### 1. Why can't Parse API keys be kept secret in a web application?

#### 2. What is the difference between authentication and authorization?

#### 3. HTTP is stateless. How does the server know, on your tenth request, that it is still you? What happens if someone copies that thing into their own browser?

#### 4. What are the three layers of access control in Parse, and what does each one protect?

#### 5. What is an ACL and at what level does it operate?

#### 6. Explain what this code does:
```js
const privateNote = new Note();
privateNote.set("content", "My secret");
privateNote.setACL(new Parse.ACL(Parse.User.current()));
await privateNote.save();
```

#### 7. How would you make an object publicly readable but only writable by the owner?

#### 8. User B, logged in, can see a to-do that user A created. Give every reason that could be the case.

#### 9. Why must the `_User` class keep Create public, when every other class should not?

#### 10. What's the problem with this code if we only validate the length on the client?
```js
// Client-side validation
if (text.length > 200) {
  alert("Too long!");
  return;
}
await todoItem.save();
```

#### 11. This query returns only the current user's to-dos. Explain why it is nevertheless not a security measure, and what is.
```js
const query = new Parse.Query(TodoItem);
query.equalTo("owner", Parse.User.current());
const results = await query.find();
```

#### 12. When would you reach for a role instead of listing users in an ACL?
