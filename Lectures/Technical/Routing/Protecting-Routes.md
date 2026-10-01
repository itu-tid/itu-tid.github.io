# Protecting Routes If Not Logged In

It follows on from [Routing in React](Routing-in-React.md), and uses the login from [Authentication and Authorization](../Backend/Authorization-and-ACL-in-Parse.md).

## todo-26 already protects every page, with one early return

Open `/lists/Xk3v9QaB2c` while logged out, and `todo-26` shows the login page. No route is involved. `App` checks before it draws any route at all:

```jsx
const [user, setUser] = useState(Parse.User.current());

// …

if (!user) {
  return <AuthPage onAuthenticated={handleAuthenticated} />;
}

return (
  <Routes>
    {/* … every page of the app … */}
  </Routes>
);
```

The address bar still says `/lists/Xk3v9QaB2c`. Log in, `handleAuthenticated` sets `user`, `App` draws again, the router reads the same URL, and the list appears: the page Armin asked for, after the login he needed for it.

That is enough as long as *every* page needs a login. This note is for the day one does not: a landing page that says what the app is for, an *About*, a sign-up page with an address of its own that you can link to.

## A check inside every page repeats itself, and protects no data

The first idea is to let each page check for itself:

```jsx
export default function ListPage({ user }) {
  if (!user) {
    return <p>Please log in.</p>;
  }
  // …
}
```

Every protected page repeats the same lines, and the day somebody forgets them in one page, nobody notices.

Nobody notices, because nothing leaks. A page that forgot its check asks Parse for the list, and Parse answers *Object not found*: a visitor's request carries no user, and the list's ACL names only Ada and Armin. **Protecting a route is about what the user sees, not about who may read what.** It decides that a visitor gets the login page instead of an error. The ACL, on the server, is still the only thing that keeps the data safe. It is the same lesson as [a URL is not a permission](Routing-in-React.md#listid-is-a-parameter-and-useparams-reads-it), the other way round: hiding a page is not a permission either.

So the check belongs in one place. There are two good places for it.

## Two sets of routes: one for visitors, one for logged-in users

Grow the early return into routes of its own. A visitor gets the pages anybody may see, and the login page for every other address:

```jsx
if (!user) {
  return (
    <Routes>
      <Route path="/about" element={<About />} />
      <Route path="*" element={<AuthPage onAuthenticated={handleAuthenticated} />} />
    </Routes>
  );
}

return (
  <Routes>
    <Route path="/" element={<Home /* … */ />} />
    <Route path="/lists/:listId" element={<ListPage />} />
    <Route path="*" element={<Link to="/">No such page</Link>} />
  </Routes>
);
```

`*` draws the login page *at* whatever address the visitor asked for, without moving them anywhere. So it keeps what the early return was good at: after logging in, the same URL draws the page they wanted.

This fits when nearly every page needs a login, which is most apps in this course. The visitors' set stays short, and reading it tells you exactly what a stranger can see.

## A wrapper component guards one route at a time

When the protected pages are the few, wrap each of them instead:

```jsx
import { Navigate, useLocation } from "react-router-dom";

export default function RequireAuth({ user, children }) {
  const location = useLocation();

  if (!user) {
    // remember where they were going, so the login can send them back
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }

  return children;
}
```

`children` is whatever the route puts between `<RequireAuth>` and `</RequireAuth>`: the page, when somebody is logged in. Otherwise `<Navigate>` sends the visitor to `/login`. It is the [`useNavigate`](Routing-in-React.md#usenavigate-changes-the-url-from-code) of the previous note, in the form of a component. `replace` swaps the address instead of adding to the history, so *back* does not land on the protected page, only to be sent to the login again.

The early return goes, and every page gets a route of its own, the login page included:

```jsx
<Routes>
  <Route path="/about" element={<About />} />
  <Route path="/login" element={<AuthPage onAuthenticated={handleAuthenticated} />} />
  <Route
    path="/lists/:listId"
    element={
      <RequireAuth user={user}>
        <ListPage />
      </RequireAuth>
    }
  />
</Routes>
```

Unlike the two sets of routes, the visitor has really moved, to `/login`. Bringing them back is the login's job, and `from` tells it where to:

```jsx
const navigate = useNavigate();
const location = useLocation();

function handleAuthenticated(loggedInUser) {
  setUser(loggedInUser);
  navigate(location.state?.from ?? "/", { replace: true });
}
```

### `RequireAuth` gets the user as a prop, because `Parse.User.current()` is not state

It is tempting to write `Parse.User.current()` inside `RequireAuth` and save the prop. But logging in does not draw anything again: only a change of state does. That is why `todo-26` keeps `user` in a `useState` in `App`, and sets it in `handleAuthenticated`. Pass that state down, and the wrapper redraws the moment somebody logs in or out.

## Exam Questions

### 1. One page of your app forgot its login check. Can a visitor now read your users' lists? What does decide that?

### 2. When would you protect routes with two sets of routes, and when with a `RequireAuth` wrapper?

### 3. Why does `RequireAuth` take `user` as a prop, instead of calling `Parse.User.current()` itself?

### 4. What does `replace` change in `<Navigate to="/login" replace />`? What goes wrong with the *back* button without it?
