# Routing in React

## One page is getting crowded, and people expect URLs anyway

Our app shows every list on one page, and it is getting crowded. What people want is a page per list, and they want each page to have its own address:

- **a link** Ada can send Armin, that opens *Apartment* and nothing else;
- **a bookmark** that comes back to the same list tomorrow;
- **the back button**, taking them to where they just were.

The browser still loads one `index.html`. So the app itself has to notice every change of address, and draw the page that belongs to it. That is client-side routing.

## React does not route; a library does

React draws components, and has no idea what a URL is. Routing comes from a library that sits between the address bar and your components. When somebody clicks a link or presses *back*, it catches the navigation before the browser can ask the server for a new page, changes the address itself, and tells React which page to draw.

Which library? Look on npm and take the one everybody uses. Popularity is not a matter of taste here: it buys documentation, answers to the question you are about to search for, and many eyes on its bugs. For React, that is `react-router-dom`:

```bash
npm install react-router-dom
```

## Routing with `react-router-dom`

Everything below is from `todo-26`, or would fit into it.

### `BrowserRouter` wraps the app once, in `main.jsx`

```jsx
import { BrowserRouter } from "react-router-dom";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter basename={import.meta.env.BASE_URL}>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
```

It watches the address bar, and every component inside it can ask what the URL is. (`basename` is for [going live](#going-live-with-routes); leave it out and nothing changes on `localhost`.)

### `Routes` picks one `Route` per URL

At the end of `App`, after the login check, the app no longer returns one page. What it used to return, the lists and the forms, moves into its own component, `Home`, in `Home.jsx`. `App` keeps the state and the handlers, and passes them down as props. Then it returns the list of pages, each with the path it answers to:

```jsx
return (
  <Routes>
    <Route
      path="/"
      element={
        <Home
          lists={lists}
          memberships={memberships}
          onAddList={handleAddList}
          onShare={handleShare}
          onLeave={handleLeave}
          onLogout={handleLogout}
        />
      }
    />
    <Route path="/lists/:listId" element={<ListPage />} />
    <Route path="*" element={<Link to="/">No such page</Link>} />
  </Routes>
);
```

`element` is the JSX to draw for that path. `Home` gets everything it shows and everything it can do from `App`; `ListPage` needs nothing, because it reads its list from the URL. The `*` route catches every URL nothing else matched: a mistyped link gets an answer instead of an empty page.

A path matches the whole URL. `/lists/:listId` matches `/lists/Xk3v9QaB2c`, and not `/lists/Xk3v9QaB2c/edit`. (Older tutorials write `exact` and `component=`. That is React Router 5; since version 6 neither exists, and matching is exact by default.)

### `:listId` is a parameter, and `useParams` reads it

The part of the path after a colon is a placeholder. On `/lists/Xk3v9QaB2c`, `useParams()` gives `{ listId: "Xk3v9QaB2c" }`: the `objectId` of the list, straight from the database into the address bar. The page loads its own list:

```jsx
export default function ListPage() {
  const { listId } = useParams();

  const [list, setList] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadList() {
      try {
        setList(await new Parse.Query(List).get(listId));
      } catch (err) {
        // "Object not found": no such list, or its ACL does not let me read it
        setError(err.message);
      }
    }
    loadList();
  }, [listId]);

  return (
    <>
      <Link to="/">← All lists</Link>
      {error ? <p>{error}</p> : !list ? <p>Loading…</p> : <ToDoList list={list} />}
    </>
  );
}
```

The three states of remote data again: loading, error, the list. The error state matters more than it looks. Send somebody the link to a list that is not shared with them, and `get()` fails with *Object not found*. **A URL is not a permission**: anyone can type any address, and the ACL still decides what comes back.

> **In [todo-26](https://github.com/itu-tid/todo-26):** `git checkout week-06-routing` ([browse it](https://github.com/itu-tid/todo-26/tree/week-06-routing)). Look at `main.jsx` (`BrowserRouter`, with a `basename`, explained under *Going live with routes*), `App.jsx` (three routes, and the state and handlers it passes to `Home`), the new `Home.jsx` (lists by name, each a `Link` to `/lists/:listId`), and `ListPage.jsx`: `useParams` gives the `listId`, and `new Parse.Query(List).get(listId)` loads it. Open a list that is not yours, and the page shows the server's *Object not found*. A URL is not a permission; the ACL decides.

### `Link` changes the URL without asking the server; `<a>` reloads everything

On the home page, every list name is a link to its page:

```jsx
<Link to={`/lists/${item.id}`}>{item.get("name")}</Link>
```

It renders as an ordinary `<a>`, but a click changes the URL in the browser, and the router draws the new page. Nothing is fetched but the list. Write `<a href="/lists/…">` instead, and the browser asks the server for a new page: the whole app starts again from `index.html`, with every piece of state gone.

### `useNavigate` changes the URL from code

A link is for the user to click. When the *code* decides where to go, for instance to open a list right after creating it, ask for `navigate`:

```jsx
const navigate = useNavigate();

async function handleAddList(name) {
  // … create and save the list, as before …
  const savedList = await list.save();
  navigate(`/lists/${savedList.id}`);   // straight to the new list's page
}
```

(Not in `todo-26`. A good first thing to try on your own!)

### Nested routes share a layout, and `<Outlet>` marks where the child goes

Every page will want the same frame: the app's name, a link back to *My lists*, *Logout*. Instead of repeating it in each page, give the routes a parent with no path of its own:

```jsx
<Routes>
  <Route element={<Layout />}>
    <Route path="/" element={home} />
    <Route path="/lists/:listId" element={<ListPage />} />
  </Route>
</Routes>
```

```jsx
function Layout() {
  return (
    <>
      <header>
        <Link to="/">My lists</Link>
      </header>
      %%render your sidebar %%
      
      <Outlet />   {/* the matched child route renders here */}
      
    </>
  );
}
```

(Not in `todo-26` either. Worth doing the day you have a third page.)

### Search parameters, like `?show=open&style=minimal`, are read with `useSearchParams`

Some state belongs in the URL, so that a link carries it: which to-dos a list page shows, say. `/lists/Xk3v9QaB2c?show=open` shows only the open ones:

```jsx
const [searchParams, setSearchParams] = useSearchParams();
const onlyOpen = searchParams.get("show") === "open";
const visible = onlyOpen ? todos.filter((todo) => !todo.done) : todos;

// …
<button onClick={() => setSearchParams({ show: "open" })}>Only open</button>
```

### Pages only for logged-in users are a note of their own

`todo-26` still shows the login page to anybody who is not logged in, with the early return from week 5, before any route is drawn. Doing it per route is [Protecting Routes If Not Logged In](Protecting-Routes.md).

## Going live with routes

Publishing the app is in [Publishing Your App on GitHub Pages](../Tooling/Publishing-on-GitHub-Pages.md). Routes add two things to it.

### The router has to know the app lives under `/<repo>/` too

`base` in `vite.config.js` told Vite; `basename` tells the router, so that `/lists/abc` in your routes means `/<repo>/lists/abc` in the address bar:

```jsx
<BrowserRouter basename={import.meta.env.BASE_URL}>
```

`import.meta.env.BASE_URL` is that same `base`, so there is only one place to change it.

### A refresh asks the server, and GitHub Pages answers 404

Click from the home page to a list, and it works. Refresh, and GitHub answers with its 404 page.

The refresh asked the *server* for `/<repo>/lists/Xk3v9QaB2c`. The server has one page, `index.html`. The list page never existed anywhere but in the browser, where the router drew it. That is what client-side routing *is*, and you only really believe it once it has bitten you. Opening a link to a list from a chat message fails the same way.

The fix: make every unknown path load the app anyway, so the router gets to read the URL. Many hosts have a setting for that. GitHub Pages does not, but for any path it does not know it serves `404.html`. So the build copies `index.html` there:

```json
"build": "vite build && node -e \"require('fs').copyFileSync('dist/index.html', 'dist/404.html')\""
```

(`node` rather than `cp`, so that it works on Windows too.) The response still carries the status 404. Browsers do not care; a search engine would. The alternative is `HashRouter`: the URLs become `/<repo>/#/lists/Xk3v9QaB2c`, and the server never sees the part after the `#`. It works, and the URLs are uglier.

> **In [todo-26](https://github.com/itu-tid/todo-26):** `git checkout week-06` ([browse it](https://github.com/itu-tid/todo-26/tree/week-06)). Look at the `build` script in `package.json`. This is the app as it stood at the end of the lecture.

## Notes

### Other routers solve the same problems
- if you understand the concepts here you will have a much easier time understanding other similar libraries
- the problems described above are the same

## What came up in the lecture

Things that happened while this was coded live, rather than things that were planned.

### Keeping the current page in `useState` means writing your own router

A `page` state variable and conditional rendering would switch pages, and it is how a router starts. But `useState` knows nothing about the address bar. The back button, a link that opens one list, a refresh that lands where you were: each would have to be wired by hand. `react-router-dom` has already done that, so we take it.

## Read More
- [React Router Declarative Mode](https://reactrouter.com/start/declarative/installation) - the official documentation - note that there's also Data Mode and Framework mode that we didn't talk about


### Exam Questions

#### 1. Why does a single-page app need routing in the browser, when a classic website does not?

#### 2. What is the difference between `<Link>` and `<a>` in React Router? What happens to the app's state with each?

#### 3. Explain what this routing setup does, for the URLs `/`, `/lists/abc`, and `/lists/abc/edit`:
```jsx
<Routes>
  <Route element={<Layout />}>
    <Route path="/" element={home} />
    <Route path="/lists/:listId" element={<ListPage />} />
  </Route>
  <Route path="*" element={<NotFound />} />
</Routes>
```

#### 4. On `/lists/abc`, how does `ListPage` find out which list to show? And what does it show when the list exists, but is not shared with you?

#### 5. How would you read `show` from `/lists/abc?show=open`, and why keep it in the URL rather than in `useState`?

#### 6. Your app is on GitHub Pages. Clicking to `/lists/abc` works; refreshing that page gives a 404. Why, and how do you fix it?
