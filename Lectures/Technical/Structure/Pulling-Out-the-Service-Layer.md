# Pulling Out the Service Layer

It works on the `todo-26` app as it stands after [Routing in React](../Routing/Routing-in-React.md). You will not write a single new query in this note. Every query is already there; it only moves.

> **In todo-26:** `git checkout week-06-routing` is where this note starts, and `git checkout week-08-service-layer` is where it ends. `git diff week-06-routing week-08-service-layer -- src` shows every line that moved.

## Every component in todo-26 knows how Parse works

Count the files in `src/` that `import Parse from "parse"`: `App.jsx`, `ToDoList.jsx`, `ListPage.jsx`, `AuthPage.jsx`. Half of the eight components. And `Home`, which does not import it, still calls `item.get("name")` on a Parse object it was handed.

The clearest case is sharing a list. Here is what `App` runs when somebody clicks *Share*:

```jsx
async function handleShare(list, username) {
  try {
    const friend = await new Parse.Query(Parse.User)
      .equalTo("username", username)
      .first();

    if (!friend) {
      alert("No user with that name");
      return;
    }

    const acl = list.getACL() ?? new Parse.ACL(Parse.User.current());
    acl.setReadAccess(friend, true);
    list.setACL(acl);

    const todos = await new Parse.Query(TodoItem).equalTo("list", list).find();
    todos.forEach((todo) => todo.setACL(acl));

    const member = new ListMember();
    member.set("list", list);
    member.set("user", friend);
    // … the member's own ACL …

    await Parse.Object.saveAll([list, ...todos, member]);

    alert(`Shared ${list.get("name")} with ${username}`);
  } catch (error) {
    alert(error.message);
  }
}
```

Forty lines in a click handler, and only the two `alert`s are about the screen. The rest is about ACLs, pointers and which rows to save together. `App` is the component that decides which page to draw, and it also knows that sharing a list means rewriting the ACL of every to-do in it.

Nothing is broken. It worked when each of you wrote it alone. It stops working when four people share the code: the one changing how the home page looks and the one fixing a sharing bug are editing the same function.

## A component says *what* should happen; a service says *how*

This is the principle from the [Component Extraction Cheat Sheet](Component-Extraction-Cheatsheet.md), one level up: **code in a component should be at the same abstraction level.** A click handler that reads "share this list with this user, then tell the user it worked" is at one level. One that builds queries and ACLs between those two steps is at three.

So the *how* goes into a **service**: a plain JavaScript module of `async` functions, named in the language of the app rather than the language of the database. `shareList(list, username)`, not `saveAllWithAcl(...)`. The component calls it and handles the outcome.

The services live in their own folder, as in [Code Organization](Code-Organization.md):

```
src/
├── services/
│   ├── parse.js          ← Parse.initialize, and nothing else
│   ├── authService.js    ← signUp, logIn, logOut, currentUser
│   ├── listService.js    ← loadMyLists, loadSharedWithMe, loadList, addList, shareList, leaveList
│   └── todoService.js    ← loadTodos, addTodo, deleteTodo, setDone
├── App.jsx
├── ToDoList.jsx
└── …
```

One service per kind of thing the app handles, which in todo-26 is one per Parse class, give or take: users, lists, to-dos.

## The service knows nothing about React; the state stays in the component

Here is `todoService.js`, every line of it moved out of `ToDoList.jsx`:

```js
import Parse from "./parse.js";

const TodoItem = Parse.Object.extend("TodoItem");

// may the current user change this object? asks its ACL
export function canWrite(parseObject) {
  const acl = parseObject.getACL();
  if (!acl) return true; // no ACL at all: everybody may write

  const user = Parse.User.current();
  return acl.getPublicWriteAccess() || acl.getWriteAccess(user);
}

// a row from the database, as the components want to see it
function toTodo(item) {
  return {
    id: item.id,
    text: item.get("text"),
    done: item.get("done"),
    canWrite: canWrite(item),
  };
}

export async function loadTodos(list) {
  const results = await new Parse.Query(TodoItem)
    .equalTo("list", list)
    .ascending("createdAt")
    .find();

  return results.map(toTodo);
}

export async function addTodo(list, text) {
  const item = new TodoItem();
  item.set("text", text);
  item.set("done", false);
  item.set("list", list);

  // the to-do follows its list: whoever may read the list may read the to-do
  item.setACL(list.getACL());

  return toTodo(await item.save());
}

export async function deleteTodo(id) {
  // we only have the id, so we build a stand-in object pointing at that row
  await TodoItem.createWithoutData(id).destroy();
}

export async function setDone(id, done) {
  const item = TodoItem.createWithoutData(id);
  item.set("done", done);
  await item.save();
}
```

No `useState`, no JSX, no `alert`. It takes arguments, talks to the server, and returns data or throws. You could call it from a test, from a script, or from a different UI altogether.

`ToDoList` keeps its `todos` state, and keeps deciding what to do with the answer:

```jsx
import {
  loadTodos,
  addTodo,
  deleteTodo,
  setDone,
  canWrite,
} from "./services/todoService.js";

export default function ToDoList({ list }) {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    loadTodos(list)
      .then(setTodos)
      .catch((error) => alert(error.message));
  }, [list]);

  async function handleAdd(text) {
    try {
      const todo = await addTodo(list, text);
      setTodos([...todos, todo]);
    } catch (error) {
      alert(error.message);
    }
  }

  async function handleDelete(id) {
    try {
      await deleteTodo(id);
      setTodos(todos.filter((each) => each.id !== id));
    } catch (error) {
      alert(error.message);
    }
  }

  async function handleToggle(id) {
    const todo = todos.find((each) => each.id === id);
    try {
      await setDone(id, !todo.done);
      setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
    } catch (error) {
      alert(error.message);
    }
  }

  // … the same JSX as before …
}
```

Each handler now has the same three beats: ask the service, update the state, or tell the user it failed. You can read it without knowing what Parse is.

## The service throws; the component decides how to tell the user

Look at what happened to the two `alert`s in `handleShare`. The service cannot call `alert`. It does not know whether it is running behind a button, a form with an error line, or a test. So where the old code alerted and returned, the service throws:

```js
// listService.js
export async function shareList(list, username) {
  const friend = await new Parse.Query(Parse.User)
    .equalTo("username", username)
    .first(); // undefined if nobody has that username

  if (!friend) {
    throw new Error("No user with that name");
  }

  // … the ACLs, the ListMember row, the saveAll: moved here unchanged …
}
```

and `App` is left with the part that is about the screen:

```jsx
async function handleShare(list, username) {
  try {
    await shareList(list, username);
    alert(`Shared ${list.get("name")} with ${username}`);
  } catch (error) {
    alert(error.message);
  }
}
```

The user sees exactly what they saw before. That is the test of a refactoring: **the behaviour does not change, only where the code lives.**

## Move one function at a time, and click through the app after each move

Do not move everything in one sitting and then find out what broke. Move one function, run the app, try the thing it does, commit. Then the next.

A good order is from the leaves inwards:

1. `parse.js`: move `Parse.initialize` and the credentials check out of `App.jsx`. Every other service imports `Parse` from here, so it is always initialised first.
2. `ListPage`'s single query becomes `loadList(listId)`. One function, easy to check.
3. `ToDoList`'s four operations become `todoService.js`, as above.
4. `AuthPage`'s sign-up and login, and `App`'s logout, become `authService.js`.
5. `App`'s lists, sharing and leaving become `listService.js`, with `shareList` last, because it is the biggest.

Each step is one branch and one pull request, which is what [Collaboration with Git-Flow](../Tooling/Collaboration-with-Git-Flow.md) is for. A reviewer can check "this moved, and nothing else changed" in a two-minute diff. Nobody can check that in a diff that touches every file.

## When it is done, only `services/` imports Parse

There is a one-line check that the job is finished:

```bash
grep -rl 'from "parse"' src
```

It should print `src/services/parse.js` and nothing else. If a component still shows up, it still knows how the database works.

It is not quite the whole story. `Home` never imports Parse and still calls `membership.get("list").get("owner")?.get("username")`, because `App` hands it Parse objects. The to-dos do not have this problem: `toTodo` turns each one into a plain `{ id, text, done, canWrite }` before any component sees it. Doing the same for lists, a `toList` in `listService.js`, is the natural next step, and the one to take when a component needs to know *why* a field might be missing.

## The payoff is a single place to change when the backend does

If Back4App doubles its prices and your group moves to another backend, which files change? Before: every component. After: the files in `services/`. The components ask for `loadTodos(list)` and get an array of plain objects; they do not care who answered.

The more everyday payoff is in the team. One person reshapes the home page, another fixes a sharing bug, and their pull requests touch different files.

With the queries gone, what is left in the components is only the screen, and the next question is whether the screen is cut into the right components: [Finding the Components](Finding-the-Components.md).

## Exam Questions

### 1. What is a service layer, and what does it take out of a React component?

### 2. A service function finds that the username does not exist. Why should it throw rather than call `alert`?

### 3. Your group moves from Parse to another backend. Which files change, if the service layer was pulled out properly? Which change if it was not?

### 4. How can you check, after a refactoring, that the behaviour of the app did not change?

## References

- [Martin Fowler — Service Layer](https://martinfowler.com/eaaCatalog/serviceLayer.html) — the pattern, from *Patterns of Enterprise Application Architecture*
- [Reusing Logic with Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) — once the service exists, a `useTodos(list)` hook can wrap it together with the state
