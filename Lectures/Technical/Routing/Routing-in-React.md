# Routing in React

### On a classic website, every URL is a page the server sends
- On the server side

### A single-page app draws its pages in the browser, so routing moves there too
- You don't want to go to the server for the pages, but generate them locally
- So the routing has to be done on the client side

### Without URLs, users lose links, bookmarks and the back button
- Usability principle? (conventions that are familiar to the user)
- Deep linking
- Browser functionality


### The app intercepts every navigation and draws the matching page
- On the client side (i.e. in the browser)
- Every URL request is intercepted by the our SPA


## React does not route; a library does

#### React only renders
- You'd think so... but, nope. React does not care
- React is responsible with the rendering of components
- Routing has to be implemented by a 3rd party library

#### A router intercepts the intent to navigate
- **Intercepting the intent of navigating to a different page** and rendering the corresponding page
- How can it intercept?

#### Pick the popular library: popularity buys support
- Look on `npm`
- Choose the most popular
- Why is this a good idea?
	- popularity is proportional to support
	- *many eyes catch all the bugs*

## Routing with `react-router-dom`

### `BrowserRouter` wraps the app, and `Routes` picks one `Route` per URL

- Install `react-router-dom` via npm/yarn
- Wrap the app with `<BrowserRouter>`
- Use `<Routes>` and `<Route>` to define routes

```js
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}
```

### `Link` changes the URL without asking the server; `<a>` reloads everything

- Use `<Link>` for client-side navigation (avoids full page reloads)
- This is as opposite to `<a>` elements - who go to the server and trigger a full page re-render

```javascript
import React from 'react'; 
import { Link } from 'react-router-dom';  
const Header = () => { 
    return ( 
        <div className="App"> 
             <Link to="/" >  Home  </Link> 
             <Link to="/about" >  About </Link> 
             <a href="/about">dont' use this!</a>
        </div> 
    ); 
};
```

### `useNavigate` changes the URL from code

- Use the `useNavigate` hook for programmatic navigation
```js
import React from "react" 
import {useNavigate} from "react-router-dom" 
  
export default function Profile() { 
   let navigate = useNavigate() 
   return ( 
	   <div> 
	         <h2> Go to profile </h2> 
	         <button onClick={()=>{ navigate("/about")}}> About 
	         </button> 
	   </div> 
	);
```


### A `:name` in a path is a parameter, and `useParams` reads it

- Sometimes you want to pass parameters to the url, e.g. ``/users/:id``
- Use `:param` in the path to define dynamic segments
```js
// Route definition
<Route path="/users/:userId" element={<UserProfile />} />
```

- Access the parameter with `useParams` hook
```js
// Accessing the parameter
function UserProfile() {
  const { userId } = useParams();
  return <div>User ID: {userId}</div>;
}

```

> **In [todo-26](https://github.com/itu-tid/todo-26):** `git checkout week-06-routing`. Look at `main.jsx` (`BrowserRouter`, with a `basename`, explained under *Going live*), `App.jsx` (the home page shows lists by name, each a `Link` to `/lists/:listId`, plus a `*` route for anything else), and the new `ListPage.jsx`: `useParams` gives the `listId`, and `new Parse.Query(List).get(listId)` loads it. Open a list that is not yours, and the page shows the server's *Object not found*. A URL is not a permission; the ACL decides.

### A route matches the whole URL, unless you say otherwise

`<Route path="/about" …>` matches `/about`, and not `/about/team`. To give a whole group of URLs one component, nest routes under it (next section), or end the path with `/*`.

Older tutorials write `exact` and `component=`. That is React Router 5; since version 6 neither exists, and matching is exact by default.

### Nested routes share a layout, and `<Outlet>` marks where the child goes

Most often than not, you will want to have nested routes.

- you can define them inside of each other
- you can use the `<Outlet>` element to render the children elements inside of the layout of the main


```js
// Parent route
<Route path="/dashboard" element={<DashboardLayout />}>
  <Route index element={<DashboardHome />} />
  <Route path="stats" element={<DashboardStats />} />
</Route>

// DashboardLayout.jsx
function DashboardLayout() {
  return (
    <div>
	  <title> The greatest dashboard </title>
      <Sidebar />
      <Outlet /> {/* Child routes render here */}
    </div>
  );
}
```
- Note the `index` - that this is what gets rendered inside of the `<Outlet>`


### A protected route sends whoever is not logged in elsewhere

- How to protect routes (e.g., redirect unauthenticated users).
- Use `<Navigate>` for redirects
- Create wrapper component for auth checks


```js
// Define a wrapper component
function PrivateRoute({ children }) {
  const isAuthenticated = checkAuth(); // Your auth logic
  return isAuthenticated ? children : <Navigate to="/login" />;
}

// Usage
<Route
  path="/profile"
  element={
    <PrivateRoute>
      <Profile />
    </PrivateRoute>
  }
/>

```
### Search parameters, like `?sort=name`, are read with `useSearchParams`

- Search params are query strings that can exist appended at the end of your URL, e.g.
```
/dashboard?sort=name&filter=active
/profile?tab=settings
/products?page=2&category=electronics
```

- To access them from within the appropriate component you have to use the `useSearchParams` hook

```jsx
import { useSearchParams } from 'react-router-dom';

function DashboardHome() {
  const [searchParams, setSearchParams] = useSearchParams();
  
  const sort = searchParams.get('sort'); // 'name'
  const filter = searchParams.get('filter'); // 'active'
  
}
```

### A `*` route catches every URL nothing else matched

- Use a wildcard route (*) to catch all unmatched paths
```js
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="*" element={<NotFound />} />
</Routes>

```
### A bigger example: a top bar everywhere, a sidebar in one section

#### App.js
```js
import { Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar';
import About from './components/About';
import MainLayout from './components/MainLayout';
import Feed from './components/Feed';
import Profile from './components/Profile';

function App() {
  return (
    <>
      {/* Top navigation (shared everywhere) */}
      <NavBar />

      {/* Routes */}
      <Routes>
        <Route path="/about" element={<About />} />
        <Route path="/main" element={<MainLayout />}>
          <Route path="feed" element={<Feed />} />
          <Route path="profile" element={<Profile />} />
        </Route>
      </Routes>
    </>
  );
}
```

#### NavBar.js - top navigation

```js
import { Link } from 'react-router-dom';

export default function NavBar() {
  return (
    <nav style={{ background: '#333', color: 'white', padding: '10px' }}>
      <ul style={{ display: 'flex', gap: '20px', listStyle: 'none' }}>
        <li><Link to="/about" style={{ color: 'white' }}>About</Link></li>
        <li><Link to="/main/feed" style={{ color: 'white' }}>Feed</Link></li>
        <li><Link to="/main/profile" style={{ color: 'white' }}>Profile</Link></li>
      </ul>
    </nav>
  );
}

```

or better yet, using the `NavLink` from the framework you can do:

```js
import { NavLink } from 'react-router-dom';

export default function NavBar() {
  return (
    <nav style={{ background: '#333', color: 'white', padding: '10px' }}>
      <ul style={{ display: 'flex', gap: '20px', listStyle: 'none' }}>
        <li><NavLink to="/about" style={{ color: 'white' }}>About</NavLink></li>
        <li><NavLink to="/main/feed" style={{ color: 'white' }}>Feed</NavLink></li>
        <li><NavLink to="/main/profile" style={{ color: 'white' }}>Profile</NavLink></li>
      </ul>
    </nav>
  );
}
```

and add the following CSS:
```css
.active {
  font-weight: bold;
  text-decoration: underline;
}
```

because the framework (`react-router-dom`) automatically adds the `.active` class to the link that matches the current URL.

#### MainLayout.js - the sidebar

```js
import { Outlet } from 'react-router-dom';

export default function MainLayout() {
  return (
    <div style={{ display: 'flex' }}>
      {/* Sidebar (shared for /main/* routes) */}
      <div style={{ width: '200px', background: '#f0f0f0', padding: '10px' }}>
        <h3>Main Menu</h3>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li><a href="/main/feed">Feed</a></li>
          <li><a href="/main/profile">Profile</a></li>
        </ul>
      </div>

      {/* Dynamic content for child routes */}
      <div style={{ flex: 1, padding: '20px' }}>
        <Outlet />  {/* Feed or Profile renders here */}
      </div>
    </div>
  );
}

```

Note: you can also use the `NavLink` here to highlight the currently selected element

#### About.js 

```js
export default function About() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>About Us</h1>
      <p>This is a standalone page with only the top navigation.</p>
    </div>
  );
}
```

#### Feed.js and Child.js

```js
// Feed.js
export default function Feed() {
  return <h2>Your Feed Content</h2>;
}

// Profile.js
export default function Profile() {
  return <h2>Your Profile Content</h2>;
}

```


## Going live

### GitHub Pages serves the built app, once you tell it where the app lives

After `npm run build`, the app is a folder of plain files in `dist/`. Any host that serves files can serve it, and GitHub Pages is free and already has your repository.

- **The app does not live at the root.** It lives at `https://<org>.github.io/<repo>/`. Tell Vite, in `vite.config.js`: `base: "/<repo>/"`. Without it the page is blank, because every script and stylesheet is looked for in the wrong place.
- **Tell the router too:** `<BrowserRouter basename={import.meta.env.BASE_URL}>`. `BASE_URL` is that same `base`, so the routes live under `/<repo>/` as well.
- **Publish:** `npm install --save-dev gh-pages`, add a script `"deploy": "npm run build && gh-pages -d dist"`, and run `npm run deploy`. Then on GitHub: **Settings → Pages → Branch: `gh-pages`**. A free organisation can do this for public repositories only.
- The build runs on your laptop, so the Parse keys from `.env.local` end up in the published files. They are in every visitor's browser anyway: that is what the `curl` in [Authentication and Authorization](../Backend/Authorization-and-ACL-in-Parse.md) showed.

> **In [todo-26](https://github.com/itu-tid/todo-26):** `git checkout week-06-deploy`. Look at `base` in `vite.config.js`, and the `deploy` script in `package.json`.

### A refresh asks the server, and GitHub Pages answers 404

Click from the home page to a list, and it works. Refresh, and GitHub answers with its 404 page.

The refresh asked the *server* for `/<repo>/lists/Xk3v9QaB2c`. The server has one page, `index.html`. The list page never existed anywhere but in the browser, where the router drew it. That is what client-side routing *is*, and you only really believe it once it has bitten you. Opening a link to a list from a chat message fails the same way.

The fix: make every unknown path load the app anyway, so the router gets to read the URL. Many hosts have a setting for that. GitHub Pages does not, but for any path it does not know it serves `404.html`. So the build copies `index.html` there:

```json
"build": "vite build && node -e \"require('fs').copyFileSync('dist/index.html', 'dist/404.html')\""
```

(`node` rather than `cp`, so that it works on Windows too.) The response still carries the status 404. Browsers do not care; a search engine would. The alternative is `HashRouter`: the URLs become `/<repo>/#/lists/Xk3v9QaB2c`, and the server never sees the part after the `#`. It works, and the URLs are uglier.

> **In [todo-26](https://github.com/itu-tid/todo-26):** `git checkout week-06`. Look at the `build` script in `package.json`. This is the app as it stood at the end of the lecture.

## Notes

### Other routers solve the same problems
- if you understand the concepts here you will have a much easier time understanding other similar libraries
- the problems described above are the same


## Read More
- [React Router Declarative Mode](https://reactrouter.com/start/declarative/installation) - the official documentation - note that there's also Data Mode and Framework mode that we didn't talk about


### Exam Questions

#### 1. Why is client-side routing necessary in SPAs?

#### 2. What is the difference between `<Link>` and `<a>` tags in React Router?

#### 3. Explain what this routing setup does:
```js
<Routes>
  <Route path="/dashboard" element={<DashboardLayout />}>
    <Route index element={<DashboardHome />} />
    <Route path="stats" element={<DashboardStats />} />
  </Route>
</Routes>
```

#### 4. What does this protected route component do?
```js
function PrivateRoute({ children }) {
  const isAuthenticated = checkAuth();
  return isAuthenticated ? children : <Navigate to="/login" />;
}
```

#### 5. How do you access URL parameters in React Router?
```js
// Route: <Route path="/users/:userId" element={<UserProfile />} />
// URL: /users/123
```

#### 6. How do you access query string parameters?
```js
// URL: /dashboard?sort=name&filter=active
```

#### 7. What happens if a user reloads the page on `/about` in an SPA?
