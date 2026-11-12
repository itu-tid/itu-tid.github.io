# Installing Your App on a Phone

Since week 6 your app has a public address, and you can open it on your phone (see [Publishing Your App on GitHub Pages](Publishing-on-GitHub-Pages.md#open-it-on-your-phone)). It works, but it is still a web page in a browser tab: an address bar on top, browser buttons at the bottom, and to find it again you have to find the tab.

Your projects (meal plans, grocery lists, households, record crates) are things people reach for on their phone, several times a day. This note makes the app installable: an icon on the home screen that opens full-screen, like an app from the store. An app that does this is called a **Progressive Web App** (PWA).

## An installable app is a website that describes itself to the phone

No app store, no Swift or Kotlin, no second codebase. The phone needs three things before it offers to install a website:

1. the site is served over **HTTPS**, which GitHub Pages already does;
2. the page links to a **web app manifest**, a small file that describes the app;
3. the manifest lists **icons** large enough for a home screen.

That is enough for Chrome on Android and for Safari on iOS. The rest of this note is what those three things mean, and what changes for your app once it runs without a browser around it.

## "Progressive" means each layer is optional

A PWA is not a different kind of app. It is your website, with layers added on top:

| layer | what it adds | what it takes |
|---|---|---|
| website | runs in a browser tab | what you have |
| **installable** | home-screen icon, own window | a manifest and icons |
| works offline | starts without a network | a service worker |
| app-like features | push notifications, badges | more APIs, and permission from the user |

A browser that does not support a layer still shows the website underneath, so nothing breaks. That is the *progressive* part: you go as far up as your app needs. For your projects, the second row is the one that matters.

## The idea is Apple's, the name is Google's, and the standard belongs to all the browsers

When the iPhone launched in 2007, it had no App Store: web apps in Safari were *the* way to build for it, and Safari's "Add to Home Screen" and its `apple-touch-icon` date from then. A year later the App Store opened, and native apps took over.

The idea came back in 2015, when Alex Russell, an engineer on Chrome, and the designer Frances Berriman named it *Progressive Web Apps*, and Google pushed it in Chrome and Android. The pieces it rests on, the manifest and the service worker, are W3C standards, written together by the browser makers. Apple followed slowly: service workers reached Safari in 2018, push notifications for installed web apps only in 2023.

That history is why installing works slightly differently on every phone, and why your app still carries one Apple-specific line next to the standard manifest.

## The manifest tells the phone the app's name, its icon, where it starts, and how it opens

The manifest is a JSON file, served next to your page. todo-26's:

```json
{
  "name": "To-do lists",
  "short_name": "To-do",
  "start_url": ".",
  "scope": ".",
  "display": "standalone",
  "background_color": "#f6f3ee",
  "theme_color": "#f6f3ee",
  "icons": [
    { "src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

- **`name`** is shown when installing; **`short_name`** goes under the icon, where there is room for about twelve characters.
- **`start_url`** is the page the icon opens; **`scope`** is the part of the site that belongs to the app; a link that leads outside it opens in a browser again.
- **`display: "standalone"`** is what removes the browser around the app. It is the line that makes it feel like an app.
- **`theme_color`** tints what the system draws around your app: the status bar, the title bar of the app's window, the address bar in Chrome on Android. **`background_color`** fills the screen for the moment before your app has drawn anything. Take both from your design system, so the app looks like itself from the first frame.
- **`icons`**: two square PNGs, 192 and 512 pixels. Keep the important part away from the edges, because Android cuts icons into circles or rounded squares.

The file's official name is the *Web Application Manifest*, not "PWA manifest". It describes a web app to the operating system, and it predates the term PWA; installing is simply what it is used for most.

## DevTools tells you whether your app is installable, and why not

On your laptop, open the published app in Chrome, then **DevTools → Application → Manifest**. Chrome shows the manifest as it understood it, the icons it found, and under **Installability** anything that stops the app from being installed, with the reason. A wrong path shows up here long before it shows up as "nothing happens" on a phone.

This is the step to insist on even when an agent writes the manifest for you: the agent cannot see whether the phone accepted it.

## On a phone, installing is hidden in the browser's menu

- **Android, Chrome:** the ⋮ menu → **Add to home screen**, then **Install**.
- **iPhone, Safari** (and other browsers since iOS 16.4): the Share button → **Add to Home Screen**.

The icon lands on the home screen, and tapping it opens the app with no address bar. Your data is all there: the installed app talks to the same backend, in the same way, as the browser tab did.

## Without a browser around it, your app has to take over six of the browser's jobs

In a tab, the browser does a lot for your app that you never had to think about. Standalone mode takes the browser away, and with it these jobs:

| the browser's job | gone in the installed app | what your app has to do |
|---|---|---|
| **back** | no back button, and on iOS often no way back at all | a way back on every screen |
| **reload** | no reload button | pull to refresh, or reload on return |
| **the address** | no address bar to copy a link from | a share button where sharing matters |
| **showing progress** | no loading bar while a page loads | its own loading state |
| **showing failure** | no "can't connect" page | its own failed state, with a way to retry |
| **leaving** | links to other sites take the user out of your app | treat outside links as a deliberate exit |

Install your group's app and use it for a day. Every time you reach for a browser button that is not there, write it down: that is your list of things to build.

### Every screen needs a way back, because the phone may not offer one

On iOS, an installed web app has no back button. A list page with no link back to the home page is a dead end: the only way out is to close the app. todo-26's `← All lists` link was a nicety in the browser; in the installed app it is the only exit. Android has a system back button, but users of both phones should find the same way out in your interface.

### Data other people change needs a way to reload: pull to refresh, or reload on return

If someone else adds an item to a shared list, the installed app does not show it until it loads the list again, and there is no reload button to press.

The usual answer is a gesture users already know from mail and social apps: pull the top of a list down, see a spinner, let go, and the list reloads. It belongs at the top of lists that show data other people change.

An even cheaper answer needs no gesture at all: reload when the user comes back to the app. People switch away from an installed app and back all the time, and the moment they return is exactly when the data is most likely to be stale. For a shared grocery list, that alone fixes most of the problem.

### A link worth sharing needs a share button, because there is no address bar to copy it from

In a tab, sharing a list means copying the URL. Installed, the URL is invisible. If your app's sharing works through links (an invitation, a recipe, a list), it needs a share button. Phones offer a system share sheet that web apps can open, so the button can hand the link to messages, mail or chat like any native app does.

### Loading and failure are yours to show, because the browser no longer shows them

The browser's loading bar and its "can't connect" page belonged to the tab. In the installed app, a slow request is a frozen screen and a failed one is a blank screen, unless your app shows otherwise. This is [The Three States of Remote Data](../React/The-Three-States-of-Remote-Data.md) again, and now no browser covers for a missing state.

### A link to another site is an exit from your app

A link that leads outside the app's scope opens in a browser, on top of or instead of your app. That is fine for "open the recipe's original page", and surprising for anything the user expected to stay inside. Decide for each outside link whether leaving is what the user wants.

## A service worker is what makes an app work offline, and you can skip it

Open the installed app in airplane mode, and you get the browser's "you are offline" page: the app's files come from the static host every time, and the host is out of reach.

A **service worker** is a script the browser runs in the background, between your app and the network. It can keep copies of the app's files, so that the app at least starts without a connection.

Even then, the app would start and show **no data**: your data lives on the backend, and the backend is on the network too. The app would be in the `failed` state from [The Three States of Remote Data](../React/The-Three-States-of-Remote-Data.md), and it had better say so. Real offline support (saving changes locally and sending them later) is a large piece of work, and not what your projects need. An installable app that needs a connection is already a big step up from a browser tab.

## Notes

- **The favicon is not the app icon.** The small icon in the browser tab comes from `<link rel="icon">` in `index.html`. Vite's starter template puts its own logo there, which is why so many student apps show a purple lightning bolt. Replace it with your app's icon.

## Exam Questions

### 1. What does a website need before a phone will offer to install it? Which of those does GitHub Pages already give you?

### 2. What does "progressive" mean in Progressive Web App?

### 3. Why does installing a web app work differently on an iPhone than on an Android phone?

### 4. Which of the browser's jobs does your app have to take over once it is installed? For three of them, say what your app has to do.

### 5. A service worker can make your app start without a network. Why would todo-26 still be of little use offline?

## Appendix: making todo-26 installable

> **In [todo-26](https://github.com/itu-tid/todo-26):** [pull request #2](https://github.com/itu-tid/todo-26/pull/2), live at <https://itu-tid.github.io/todo-26/>.

**Every path in the manifest is relative.** todo-26 is served at `https://itu-tid.github.io/todo-26/`, not at the root of the domain. A manifest saying `"start_url": "/"` would open the installed app on GitHub's root page. Paths in a manifest are resolved relative to the manifest itself, so `"."` means "the folder I am in", and the same file works on `localhost`, on GitHub Pages, and on a domain of your own. It is the same reason as `base` in week 6.

The pull request changes three things:

1. **`public/manifest.webmanifest`**, the manifest above. Vite copies everything in `public/` into the build unchanged, which is what a manifest and its icons need.
2. **`public/icons/icon-192.png` and `icon-512.png`**, exported as square PNGs.
3. **Three lines in the `<head>` of `index.html`:**

   ```html
   <link rel="manifest" href="/manifest.webmanifest" />
   <link rel="apple-touch-icon" href="/icons/icon-192.png" />
   <meta name="theme-color" content="#f6f3ee" />
   ```

   These paths start with `/`, because Vite rewrites the links in `index.html` with `base` when it builds: `dist/index.html` says `/todo-26/manifest.webmanifest`. The `apple-touch-icon` line is optional: Safari has read the manifest's icons since iOS 15.4, and the line only matters for older iPhones or a different icon on iOS.

For a service worker, the usual route with Vite is the [`vite-plugin-pwa`](https://vite-pwa-org.netlify.app/) package (read [Libraries](Libraries.md) before adding it).

## References

- [Making PWAs installable](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable), MDN
- [Web application manifest](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest), MDN
