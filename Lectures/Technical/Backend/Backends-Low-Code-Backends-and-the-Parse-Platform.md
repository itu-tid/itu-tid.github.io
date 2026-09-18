# Backends, Low-Code Backends, and the Parse Platform

Motivation: we want to be full-stack web developers :) But we don't have much time.

> **Read before the lecture:** [Async Programming and Promises](../../../TopUps/6-Async-Programming-and-Promises.md). Everything you ask a backend for arrives later, which in JavaScript means a **promise**. From the first `save()` onwards this lecture assumes you have met one, and knows the difference between `.then()`, `.catch()` and `await`.
>
> **Also before the lecture:** run `node --version` and make sure it says 20, 22 or 24. Parse 8 needs one of those, and on an older Node `npm install parse` quietly installs an old release instead of failing.

## What a backend is

### "Backend" only means something relative to a front-end
- **Front-end** -- code that runs in the user's browser and handles presentation and user interaction
- **Back-end** -- handles data processing, storage, and security

### Client-server is the arrangement, and the backend is the server half

The pair has a name, and it is older than the web: a ***client-server architecture***. 

The **client** runs on the user's machine and asks for things; the **server** runs somewhere else and answers.

![](../images/client-server-architecture.png)

The detail that matters is the one the picture shows and the phrase does not: **there are many clients and one server.** Nearly everything in the next three weeks follows from that asymmetry.

- **The server is the only shared thing**, so it is the only place where two users can meet. Sharing a to-do list is possible because there is one copy of it and both clients are talking to that copy.
- **The server is the only trusted thing.** Every client runs on somebody else's computer, in code they can read and change. Anything you need to be *true* *has to be enforced on the server* — which is next week's lecture in one sentence.
- **The server is far away.** Between the asking and the answering there is a network, and your interface has to have something to show meanwhile.


*Note:* Client / front-end are going to be used interchangeably in this course. 


### Backend Responsibilities: The backend takes care of everything the browser cannot be trusted with

1. Authentication (proving that a user is who they say they are)
2. Authorization (checking what a user is allowed to do)
3. Session management (tracking a user across requests, so they don't log in again on every click -- this is a result of HTTP being a stateless protocol)
4. Business logic and DB access (because it's the one central place, as per above)
5. Scheduled jobs (e.g., `cron`, backups, etc.)
6. API endpoints / request handling (since the backend receives and responds to requests)
7. Data validation (ensuring incoming data is correct/safe)

### A traditional backend needs that you configure many pieces of infrastructure before writing even a line of your own code

1. **Machine** setup (or create a VM with a cloud provider)
2. **Operating system** installation & configuration
3. Security & **firewall** configuration
4. **Database** management system (DBMS)
5. **Web server** -- application that listens to HTTP requests and serves pages to clients (e.g. nginx, apache2)
6. **Application server** -- runtime environment in which your application will be executed
7. **Logging, monitoring & analytics** -- supper essential for a service that has to be available non-stop
8. **Backup** system

Note that none of the eight is on the previous list. That list was about *responsibilities*; this one is about the *machinery* you would have to assemble before you could discharge a single one of them.

## Low-code backends and Backends-as-a-service
### A low-code backend hands you (some of) the eight responsibilities already built

The responsibilities arrive already assembled, and what you get is a **pre-built solution** for the needs that every application has, so that the only code you write is the code particular to your application domain. 

**Low-code** says how much you have to write to implement your backend. 

### Backend-as-a-service (BaaS) gives you a low-code backend with the infrastructure also pre-built 

**As-a-service** says that it is somebody else that owns the infrastructure. All you are responsible with is writing the application. 

### The two are independent and can be combined

- **Parse Platform** is **a low-code backend**. 
	- Open-source software
	- You rent a virtual machine in the cloud and install it there, or you run it on your own laptop while you are developing
	- You pay a fixed price for renting the VM 
	- Or you pay electricity for the machine in your basement / data center
- **Firebase** is a **backend-as-a-service**. 
	- Proprietary, hosted by Google
	- Renting it is the only way to have it - you pay for the usage of the firebase backend
	- However, open source alternatives exist
- **Back4App** is **backend-as-a-service** that comes with Parse pre-installed on it. 
	- Somebody else running the low-code backend you could have run yourself
	- You don't have to rent a VM
	- You just pay for the usage of the backend 

### The code you write that communicates with a Parse server, does not care whether the server is hosted on your own VM or is a service hosted by somebody else

The only thing that your code needs to know is that there's a Parse backend. And what's the URL where it can communicate with that backend. 

### It will be the same with any kind of backend. The frontend talks to a given IP address or URL. 

That backend can be running on your local machine, then you connect to `localhost:1337` e.g., or `127.0.0.1:1337`. Or you can connect to a staging server. Or to the main server. 


## Parse as a low-code backend

### Is open source
Now. It started as a startup, got bought by Facebook, and is now opened again

### The Parse server is implemented in Node
Implemented in JS. And as we've discussed in the past, you can run JS in the browser, or on any machine with the help of the `node` Javascript interpreter that does not need a browser.

### Parse has an answer for every line of the requirements of a backend 

| The backend is responsible with ... | Parse gives you                                                                          |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| Authentication                      | `Parse.User` — signup, login, sessions (*next week*)                                     |
| Authorization                       | class-level permissions and ACLs (*next week*)                                           |
| Session management                  | completely free (handled by the SDK, and remembered across page reloads)                 |
| Business logic and DB access        | the JavaScript SDK — the subject of today                                                |
| Scheduled jobs                      | cloud jobs                                                                               |
| API endpoints                       | REST and GraphQL, generated from your classes (although not needed when you use the SDK) |
| Data validation                     | cloud code triggers (*week 11*)                                                          |

And two more that were never on the list, because the browser never had them to lose: 
- **file storage**, and 
- an interactive **dashboard** for looking at and editing your database


### For your frontend/client code, Parse provides you with an easy to use Javascript SDK

SDK
- stands for (software development kit)
- is a library that makes it easy for you to communicate from the frontend to the backend
- without this SDK, you would have to communicate with the backend with the HTTP protocol, and that's more clumsy

Everything you do to Parse goes through the JavaScript SDK. There are also SDKs for other languages than JS (Kotlin for Android, Swift for iOS, etc.). 

*Note:* The full documentation of the SDK is in the [Parse.js Javascript Guide](https://docs.parseplatform.org/js/guide/#saving-objects). Use it as reference -- that is, search for things as you need them. Don't read it as a book. 



## Making our TODO app save tasks in a  real database instead of localStorage


### Creating the backend for our app on Back4App
1. Create an account on Back4App
2. Create a app for your react application in Back4App (this is the backend of your application)
3. Somewhere in settings find `APP_ID` and `JAVASCRIPT_KEY` and `PARSE_SERVER_URL` and save them for later

### Installing the Javascript SDK so we can use it from React

```bash
npm install parse@8.6.0 events
npm list parse
```

Check what the second command prints. It should say **`parse@8.6.0`** — the version we use in the course. Asking for the version by name is what keeps everyone on the same one: with a bare `npm install parse`, `npm` is free to hand you an older release instead.

`parse` is the SDK. `events` is a library that Parse needs in order to run in the browser; without it, `Parse.initialize()` fails with `Emitter is not a constructor`.

That failure has a shape you will meet again: `npm run build` **succeeds**, with at most a warning in the output. The app only dies when someone loads it. A green build is not evidence that anything works.

### Initializing the connection to the backend 

We put the following lines as early in the application as possible, e.g., in `App.jsx`. 

```js
import Parse from 'parse';

Parse.serverURL = "https://parseapi.back4app.com/"; // your PARSE_SERVER_URL
Parse.initialize("YOUR_APP_ID", "YOUR_JAVASCRIPT_KEY");
```

The initialization configures your react application to connect to
	- the server (`Parse.serverURL`)
	- the corresponding app (`YOUR_APP_ID`), because there might be multiple apps on the server

### Creating and Saving An Object to the Database

```js
import Parse from 'parse';

// This next line is super advanced - it creates a Class! 
// How we do know, look on the next line, we create an object of that class there! 
const TodoItem = Parse.Object.extend("TodoItem");
const newItem = new TodoItem();

newItem.set("text", "Call the landlord");
newItem.set("done", false);

newItem.save()
	.then(onSuccessfulSave)
	.catch(onError);

function onSuccessfulSave(savedItem) {
	alert("saved a todo with id: " + savedItem.id);
}

function onError(error) {
	alert(error.message);
}
```

Steps:
1. `Parse.Object.extend("TodoItem")` creates a class for the object
2. `save()` - sends the data to the server
3. `save()` returns a *promise*: `.then()` runs if it worked, `.catch()` runs if it did not

This code does not float somewhere in the component: it goes **in the event handler** — the function that already runs when the user submits the form. Adding a to-do is something the user *does*, and the save is part of doing it.

The callback is called `onSuccessfulSave` rather than `onSave` on purpose: `save` in the app means the button the user pressed, and `save()` here means the round trip to the database. `onSuccessfulSave` also says the thing that matters about it — it runs only if the database said yes.

#### Classes created with `Parse.Object.extend`  correspond to tables in the database 

Thus in JS you create an object of that class and when you save it it gets automatically saved in the database. 

#### If a class created with ``Parse.Object.extend`` does not exist in the database, it is automatically created

The `TodoItem` class is automatically created in the database if it didn't exist. This behavior can be turned off, and we *will* turn off next week. You will see why. 

#### The promise can be written also with anonymous functions 
The two functions are given names on purpose. Written inline it is the same code, and that is the form you will meet often, especially in the examples, tutorials, and AI-generated code. 

```js
newItem.save()
	.then((savedItem) => alert("saved a todo with id: " + savedItem.id))
	.catch((error) => alert(error.message));
```

Names make it easier to read. Compare the above once more with the code below: 

```js
newItem.save()
	.then(onSuccessfulSave)
	.catch(onError);

function onSuccessfulSave(savedItem) {
	alert("saved a todo with id: " + savedItem.id);
}

function onError(error) {
	alert(error.message);
}
```

### Reading Objects from the Database

The simplest type of query 
- is created **for a specific class** 
- given some **some constraints**
- then **executed with `find()`**

```js
const TodoItem = Parse.Object.extend("TodoItem");

// we are creating a query object for objects of type TodoItem
const query = new Parse.Query(TodoItem);

query.equalTo("done", false);
query.ascending("createdAt");

// await 
const results = await query.find();

for (const item of results) {
	console.log(item.id + " - " + item.get("text"));
}
```


`find()` returns a promise as well. From here on we use `await` rather than `.then()`, because the code then reads in the order in which it happens.

> **`await` and `.then()` are the same promise, handled two ways.**
> `.then(f)` says *when the answer arrives, call `f` with it* — and the lines after it run immediately, before `f` ever does.
> `await` says *stop here until the answer arrives, then carry on with it in hand* — so the next line is the next thing that happens.
>
> Nothing changes on the network; what changes is whether your code reads top to bottom or is cut into callbacks. The price of `await` is that it is only allowed inside a function marked `async`, which is why `async` starts appearing on our handlers below.



References:
- [Query Constraints](https://docs.parseplatform.org/js/guide/#query-constraints)
- [Queries on Strings](https://docs.parseplatform.org/js/guide/#queries-on-string-values)



### Putting the snippets into the app

You already have a working app. It has a list, a form, a checkbox and a delete button, and at the bottom of `ToDoList.jsx` it has this:

```jsx
useEffect(() => {
	localStorage.setItem("todos", JSON.stringify(todos));
}, [todos]);
```

One line, and everything is saved. Whenever anything about any to-do changes, the entire array is serialized and written again.

#### The whole-array write is the first thing that has to go

With `localStorage` that line is free. It is the same machine, the list is a few kilobytes, and nobody notices.

Now put a network in the middle. Ticking one checkbox would upload every to-do you own. Two people editing the same list would overwrite each other wholesale, because each of them is writing the entire list as they last saw it. And there is no operation in the database for *replace everything*; there are operations for one object at a time.

So the single effect that wrote everything becomes **one call per change**:

| User action      | In the database            |
| ---------------- | -------------------------- |
| adds a to-do     | create one object          |
| ticks a checkbox | save one object            |
| presses Delete   | destroy one object         |
| opens the page   | find all the objects, once |

This is not a Parse rule. It is what having a backend means.

We now go through that table one row at a time. All four end up in the same file, `ToDoList.jsx`, in the handlers that are already there.

#### Creating: in the handler that adds a to-do

```jsx
const TodoItem = Parse.Object.extend("TodoItem");

async function handleAdd(newTask) {
	const item = new TodoItem();
	item.set("text", newTask);
	item.set("done", false);
	const saved = await item.save();

	setTodos([...todos, { id: saved.id, text: saved.get("text"), done: saved.get("done") }]);
}
```

Two things happen, and the order matters: **first the database, then the state**. If the save fails, the to-do never appears on the screen — which is the truth.

What `save()` gives back is a Parse object, and the component has been working with plain `{ id, text, done }` all along, so we unpack it on the way into the state. 

**Note:** that `id` is the one thing that is not a field: it lives on the object itself, not behind `get()`.

#### Reading: once, when the page opens

Reading already happened once, when the component mounted — but it happened *while* it mounted:

```jsx
let [todos, setTodos] = useState(loadTodos);   // reads localStorage, synchronously
```

`localStorage` could answer inside that line. A database cannot: `find()` hands back a promise, and `useState` needs a value now. So the read moves out of the initial state and into an effect that runs once, after the first render:

```jsx
useEffect(() => {
	async function load() {
		const query = new Parse.Query(TodoItem);
		query.ascending("createdAt");
		const results = await query.find();

		setTodos(results.map((each) => ({
			id: each.id,
			text: each.get("text"),
			done: each.get("done"),
		})));
	}
	load();
}, []);
```

The empty `[]` is essential: it says *run this once, when the component first appears*. Without it the effect would run after every change to `todos` — and since it ends by setting `todos`, each load would trigger the next one.

Notice what the state now starts as: `useState([])`, an empty list. Not because the list is empty, but because we do not know yet. We will come back to that.

##### Why the `async` function *inside* the effect, and not `useEffect(async () => ...)`

Because React reads whatever an effect returns as its **cleanup function** — the thing to call when the component goes away. An `async` function always returns a promise, so React would be handed a promise where it expects a function.

So the asynchronous work goes into a function declared inside the effect; the effect calls it and returns nothing. It looks like a workaround, and it is one, but it is the standard one — you will see it in every codebase that fetches.

#### Updating: only the field that changed

Ticking a checkbox means changing one field of one row. We do **not** need to download the row first:

```jsx
async function handleToggle(id) {
	const todo = todos.find((each) => each.id === id);

	const item = TodoItem.createWithoutData(id);
	item.set("done", !todo.done);
	await item.save();

	setTodos(todos.map((each) => (each.id === id ? { ...each, done: !each.done } : each)));
}
```

`createWithoutData(id)` deserves the objection: **why don't we look the object up first?**

The obvious version is this, and it works:

```js
const item = await new Parse.Query(TodoItem).get(id);   // ask the server for the to-do
item.set("done", done);
await item.save();                                      // ask it again, to change one field
```

Two round trips, and the first one downloads a to-do we already have on screen only to throw it away.


#### A Parse object is not a *copy of a row* but rather a handle to a row.

The intuition tells us that a Parse object is a *copy of a row*. It is not. It is a handle to a row. A reference to it. 

An object is a **handle to a row** — and a handle needs only the id. `createWithoutData(id)` builds one out of thin air, and `save()` sends only the fields you actually changed, so what crosses the network is `{done: true}` and an id.

#### Deleting: the same handle, destroyed

To destroy a row you need to know *which* row, and nothing else:

```jsx
async function handleDelete(idToDelete) {
	const item = TodoItem.createWithoutData(idToDelete);
	await item.destroy();

	setTodos(todos.filter((each) => each.id !== idToDelete));
}
```

#### The four of them, in one file

```jsx
import { useState, useEffect } from "react";
import Parse from "parse";

const TodoItem = Parse.Object.extend("TodoItem");

export default function ToDoList({ firstName }) {
	const [todos, setTodos] = useState([]);

	useEffect(() => {
		async function load() {
			const query = new Parse.Query(TodoItem);
			query.ascending("createdAt");
			const results = await query.find();

			setTodos(results.map((each) => ({
				id: each.id,
				text: each.get("text"),
				done: each.get("done"),
			})));
		}
		load();
	}, []);

	async function handleAdd(newTask) {
		const item = new TodoItem();
		item.set("text", newTask);
		item.set("done", false);
		const saved = await item.save();

		setTodos([...todos, { id: saved.id, text: saved.get("text"), done: saved.get("done") }]);
	}

	async function handleToggle(id) {
		const todo = todos.find((each) => each.id === id);

		const item = TodoItem.createWithoutData(id);
		item.set("done", !todo.done);
		await item.save();

		setTodos(todos.map((each) => (each.id === id ? { ...each, done: !each.done } : each)));
	}

	async function handleDelete(idToDelete) {
		const item = TodoItem.createWithoutData(idToDelete);
		await item.destroy();

		setTodos(todos.filter((each) => each.id !== idToDelete));
	}

	// ... the JSX is unchanged
}
```

The `useEffect` that used to synchronize the app with `localStorage` is gone, because there is nothing left for it to synchronize. Every handler does the same two things in the same order: **change the database, then change the state**.

The app now works against a real database, and two people opening it see the same list.

#### What we have just written has a name: CRUD

Four operations, and between them they are most of what any application does to its data:

| CRUD       | The user...           | In Parse                                            |
| ---------- | --------------------- | --------------------------------------------------- |
| **C**reate | adds a to-do          | `new TodoItem()`, `set()`, `save()`                 |
| **R**ead   | opens the page        | `new Parse.Query(TodoItem)`, `find()`               |
| **U**pdate | ticks a checkbox      | `createWithoutData(id)`, `set()`, `save()`          |
| **D**elete | presses Delete        | `createWithoutData(id)`, `destroy()`                |

You will meet the acronym in documentation, in job ads, and in the exam. It is worth noticing how little there is to it: you have now written all four, and the rest of the course is mostly about doing them *safely*, and against [more than one class at a time](Relationships-Between-Object-Classes.md) (both next week), and *efficiently* (the week after).

## Code organization

Look at the one file above once more. `TodoItem` is set up there, the three-line unpacking of a Parse object into `{ id, text, done }` appears twice, and the component that draws a list of to-dos is also the component that knows a field is called `"text"`. It works, and it is already getting hard to read — and this is one class and four operations.

So, instead of calling Parse directly from our UI components, we put those calls in their own file — a **service layer**.

Without one, a component both renders the UI *and* talks to the database, which are two responsibilities (see the **Single Responsibility Principle**, in the further reading). Components get longer, and the same four lines of Parse setup get copied into every one of them:

```js
// in the component - messy, and about to be duplicated in the next component
const TodoItem = Parse.Object.extend("TodoItem");
const item = new TodoItem();
item.set("text", text);
item.set("done", false);
await item.save();
```

With a service layer the component says what it wants:

```js
// in the component - clean, simple
await createTodo(text);
```

Our services folder starts with a single file, `src/services/todoService.js`:

```js
import Parse from "parse";

const TodoItem = Parse.Object.extend("TodoItem");

// React is happier with plain JS objects than with Parse objects,
// and this is also where we unify the treatment of `id` with the other fields
function toPlainObject(parseObject) {
	return {
		id: parseObject.id,
		text: parseObject.get("text"),
		done: parseObject.get("done"),
	};
}

export async function fetchTodos() {
	const query = new Parse.Query(TodoItem);
	query.ascending("createdAt");   // oldest first
	const results = await query.find();
	return results.map(toPlainObject);
}

export async function createTodo(text) {
	const item = new TodoItem();
	item.set("text", text);
	item.set("done", false);
	return toPlainObject(await item.save());
}

export async function setTodoDone(id, done) {
	const item = TodoItem.createWithoutData(id);
	item.set("done", done);
	return toPlainObject(await item.save());
}

export async function deleteTodo(id) {
	const item = TodoItem.createWithoutData(id);
	await item.destroy();
}
```

`toPlainObject` is the only place in the whole app that knows a field is called `"text"`. Everywhere else, a to-do is `{ id, text, done }` — the same shape it had when it lived in `localStorage`, which is why the components barely change.

`createWithoutData(id)` is the same handle-to-a-row trick we used in the handlers above: `setTodoDone` and `deleteTodo` never read the row they are about to change.

### And the component

The component keeps exactly the shape it had a page ago. What changes is that no line of it mentions Parse any more — each handler says *what it wants*, and the service says how:

```jsx
import { useState, useEffect } from "react";
import { fetchTodos, createTodo, setTodoDone, deleteTodo } from "../services/todoService";

export default function ToDoList({ firstName }) {
	const [todos, setTodos] = useState([]);

	useEffect(() => {
		async function load() {
			setTodos(await fetchTodos());
		}
		load();
	}, []);

	async function handleAdd(newTask) {
		const created = await createTodo(newTask);
		setTodos([...todos, created]);
	}

	async function handleDelete(idToDelete) {
		await deleteTodo(idToDelete);
		setTodos(todos.filter((each) => each.id !== idToDelete));
	}

	async function handleToggle(id) {
		const todo = todos.find((t) => t.id === id);
		await setTodoDone(id, !todo.done);
		setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
	}

	// ... the JSX is unchanged
}
```

Same two things in the same order as before — **change the database, then change the state** — but a handler is now three lines you can read at a glance, and `"text"`, `"done"` and `TodoItem` appear in exactly one file in the whole app.

The version above is not finished: it assumes the data arrives. What a component has to show while it has not arrived — and when it never does — is [The Three States of Remote Data](../React/The-Three-States-of-Remote-Data.md), which every component you write from here on will need.


## Exam Questions

### 1. What is the difference between front-end and back-end?

### 2. List at least 5 responsibilities of a backend.

### 3. What is Parse Platform and what does it provide?

### 4. What does CRUD stand for and what do each of the letters represent?

### 5. Explain what this code does:
```js
const TodoItem = Parse.Object.extend("TodoItem");
const newItem = new TodoItem();
newItem.set("text", "Buy milk");
newItem.set("done", false);
await newItem.save();
```

### 6. Once the to-dos live on a server, this one line has to become several separate calls. For each thing the user can do in the app, name the database operation that replaces it.
```jsx
useEffect(() => {
  localStorage.setItem("todos", JSON.stringify(todos));
}, [todos]);
```

### 7. What are two benefits of placing this code in a separate service file rather than directly in a React component?
```js
export async function fetchTodos() {
  const query = new Parse.Query(TodoItem);
  query.ascending("createdAt");
  const results = await query.find();
  return results.map(toPlainObject);
}
```

### 8. How would you query all TodoItems where done is false, ordered by creation date?



## References

The documentation on ParsePlatform.org
- [Getting Started Guide](https://docs.parseplatform.org/js/guide/#getting-started) - extensive reference for everything ParseJS


<!-- Staff notes, hidden from the published page and the chapter.
History
- Sep '26 - Restructured. Authentication moved out to the Authorization note (auth + authz belong together).
            The lecture is now "replace localStorage with a real DB", worked on todo-26 rather than on GameScore.
            Service layer moved here from the Authorization note, since the need arises here.
            Modeling appears only where relationships appear. Arrays and Parse.Relation demoted to warnings.
            Vite detour deleted: `npm install parse events` + a bare `import Parse from 'parse'` works in dev
            and in a production build (verified against parse 8.6.0 / vite 7.3.6).
- Oct '25 - Improved structure - made the page more stand-alone - less external references
- Nov '24 - better organized the references
To do
- Nov '24 - spend more time discussing the Relationships
- Sep '26 - todo-26 still needs the matching commit: `npm install parse@8.6.0 events`, per-item CRUD in the component, the three states.
- Sep '26 - demo each snippet twice: first in the `node` REPL against the backend (so they see they can test without the UI), then moved into the React app. Worth doing for create and read; implied after that.
- Sep '26 - the service layer at the end is the time-permitting tail. If time runs short, stop after CRUD-in-one-file and do the refactoring next time. Do not start the account creation instead - the pain has to be felt before the refactoring lands.
- Sep '26 - mail the students before the lecture: check `node --version`, install Node 20/22/24.
-->
