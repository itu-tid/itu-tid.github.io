# Publishing Your App on GitHub Pages

Until today the app has lived on `localhost:5173`, on your laptop, where nobody else can reach it. This note puts it on the internet, at an address anyone can open on their phone. It takes a few minutes, and you do it once; after that, publishing again is one command.

## The built app is a folder of plain files

`npm run dev` is for working: it rebuilds on every save. What you publish is the result of

```bash
npm run build
```

which writes a folder `dist/`: an `index.html`, and next to it the JavaScript and CSS that Vite bundled. 

No server code at all. Your backend is Parse, and it has been on the internet since week 4; only the frontend was on your laptop. So anything that can hand out files can host the app. `npm run preview` serves `dist/` locally, if you want to see the built version first.

## GitHub Pages hands out those files, from your repository, for free

Every public repository can have a site at `https://<owner>.github.io/<repo>/`. For your team, `<owner>` is the organisation. A free organisation gets Pages for **public** repositories only; a private one has its Pages settings greyed out.

## Vite has to know the app does not live at the root

The address ends in `/<repo>/`, not in `/`. By default Vite writes `/assets/index-….js` into `index.html`, and on GitHub Pages that path is wrong: the page loads, finds none of its scripts, and stays blank. Tell Vite, in `vite.config.js`:

```js
export default defineConfig({
  plugins: [react()],
  base: "/<repo>/",   // e.g. "/todo-26/"
})
```

The dev server moves with it: from now on it is `localhost:5173/<repo>/`.

## `gh-pages` publishes `dist/` to a branch of its own

Install the small tool that does the copying, as a development dependency:

```bash
npm install --save-dev gh-pages
```

Add a script to `package.json`:

```json
"deploy": "npm run build && gh-pages -d dist"
```

and run it:

```bash
npm run deploy
```

It builds, then pushes the contents of `dist/` to a branch called `gh-pages`, separate from your code. The first time, tell GitHub to serve that branch, in the **repository's** settings (the organisation has a *Settings* tab and a *Pages* page too, but that one is only about domains): **Settings → Pages → Build and deployment → Deploy from a branch → `gh-pages`, `/ (root)`**. The first deployment takes a minute or two; the Pages settings show the address when it is live.

From then on, every change goes out with `npm run deploy`.

## The Parse keys travel with the build, and that is fine

`.env.local` is git-ignored, so the keys are not in your repository. But the build reads them, and bakes them into the JavaScript it publishes. That is not a leak: the same keys were already in the browser of everybody who opened your app, as the `curl` in [Authentication and Authorization](../Backend/Authorization-and-ACL-in-Parse.md) showed. What protects your data is the ACLs and the class-level permissions, not the keys.

It does mean the build has to run where `.env.local` is, which is on your laptop. A teammate who deploys needs their own copy.

## Open it on your phone

Log in, and your lists are there: same backend, same data, a different device. From now on two people testing sharing can be two people, on two phones, and not two windows on one laptop.

> **In [todo-26](https://github.com/itu-tid/todo-26):** `git checkout week-06-deploy` ([browse it](https://github.com/itu-tid/todo-26/tree/week-06-deploy)). Look at `base` in `vite.config.js`, and the `deploy` script in `package.json`.

Once the app has routes, publishing needs two more things: the router has to know about `/<repo>/` too, and a refresh on any page but the first answers 404. Both are in [Routing in React](../Routing/Routing-in-React.md#going-live-with-routes).

## Exam Questions

### 1. Your app is built and published, and the page is blank. The browser's Network tab shows the JavaScript file failing with 404. What did you forget, and why does it matter on GitHub Pages?

### 2. The Parse keys are in a git-ignored `.env.local`, and yet they are in the published app. Is that a problem? What protects your data instead?
