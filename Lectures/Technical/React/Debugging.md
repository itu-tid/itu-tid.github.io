# Debugging

Three tools, roughly in the order you will reach for them: a `debugger;` statement, the React DevTools component tree, and a proper breakpoint in your editor.

## Your editor can pause code that is running in the browser

In VS Code, this takes a one-off configuration. (WebStorm and the other JetBrains editors do it without any of this — run the dev server, then attach a JavaScript Debug configuration to `http://localhost:5173`.)

1. Create the `.vscode` folder in your project
2. Add the following configuration in the `launch.json` file
```json
{
	"configurations": [
		{
			"type": "chrome",
			"request": "launch",
			"name": "Debug localhost in Chrome ",
			"url": "http://localhost:5173/",
			"webRoot": "${workspaceFolder}/src"
		}
	]
}
```
3. Set your breakpoints
4. Select from the menu: `Run -> Start Debuggging`

## `debugger;` is a real statement, and costs nothing when nobody is watching

`debugger;` is a real JavaScript statement, not a library call. Put it anywhere in your code: it does nothing while nobody is watching, and pauses execution the moment DevTools is open.

That makes it the cheapest breakpoint there is — and unlike a `console.log`, you cannot forget where you left it, because it stops the program and shows you.

## React DevTools lets you see state instead of printing it

The browser extension adds two panels that plain DevTools does not have:

- **Components** — the live component tree, with every component's props and state visible and editable. This is the only way to *see* state rather than print it, and it is what turns "the list did not update" into "the state changed but the key did not", which are different bugs.
- **Profiler** — which components re-rendered and why. Ignore this until something is slow; it answers a question you do not have yet.

## The stack frame you want is the topmost one in your own file

Most React errors name the component and the hook. Read the first three lines of the stack before changing anything: the frame you want is usually the topmost one that belongs to *your* file rather than to `react-dom`.
