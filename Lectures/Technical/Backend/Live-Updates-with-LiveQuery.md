# Live Updates with LiveQuery

> **Optional.** Not covered in class. [Efficient Communication with the Backend](Efficient-Communication-with-the-Backend.md#push-lets-the-server-announce-a-change-and-is-worth-it-only-when-seconds-matter) explains when push is worth it; this note shows how to add it to the to-do list, with Parse on Back4App.

## LiveQuery has to be switched on in Back4App, and the client told where it is

In *App Settings → Server Settings → Server URL and Live Query*, turn on the Back4App subdomain and Live Query, and tick the classes to watch (here `TodoItem`). Then, next to `Parse.serverURL` in `parse.js`, tell the client where the LiveQuery server is:

```js
Parse.liveQueryServerURL = "wss://<your-subdomain>.b4a.io";
```

## The subscription belongs in the service, next to `loadTodos`

The service gives the components the same plain to-dos that `toTodo` makes, so `ToDoList` never sees a Parse object:

```js
// todoService.js
export async function subscribeToTodos(list, { onAdd, onChange, onRemove }) {
  const subscription = await new Parse.Query(TodoItem)
    .equalTo("list", list)
    .subscribe();

  subscription.on("create", (item) => onAdd(toTodo(item)));
  subscription.on("update", (item) => onChange(toTodo(item)));
  subscription.on("delete", (item) => onRemove(item.id));

  return subscription;
}
```

## The component subscribes in an effect and unsubscribes in its cleanup

```js
// ToDoList.jsx
useEffect(() => {
  const subscribing = subscribeToTodos(list, {
    onAdd: (todo) => setTodos((todos) => [...todos, todo]),
    onChange: (todo) =>
      setTodos((todos) => todos.map((t) => (t.id === todo.id ? todo : t))),
    onRemove: (id) => setTodos((todos) => todos.filter((t) => t.id !== id)),
  });

  // subscribing is a promise: unsubscribe once it has resolved
  return () => subscribing.then((subscription) => subscription.unsubscribe());
}, [list]);
```

The callbacks use [updater functions](../React/The-Render-Loop-and-Stale-State.md): they run long after the effect, when the `todos` it captured are out of date.

## The server also sends you your own changes

Once the list is subscribed, `handleAdd`, `handleDelete` and `handleToggle` should only talk to the server and leave `setTodos` to the subscription. Otherwise each new to-do shows up twice: once from `handleAdd`, once from the `create` event.

## LiveQuery follows the ACLs

A friend who cannot read a list gets no events for it, so sharing works as it already does.

See [Live Queries](https://docs.parseplatform.org/js/guide/#live-queries) in the Parse guide.
