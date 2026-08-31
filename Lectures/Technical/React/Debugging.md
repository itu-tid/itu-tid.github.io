# Setting breakpoints in VSCode

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

# Using the Browser DevTools

- You can add `debugger;` statements directly in your code
- If Developer Tools is open, you'll get a breakpoint

- `debugger;` is a real JavaScript statement, not a library call. It does nothing when nobody is watching and pauses execution the moment DevTools is open, which makes it the cheapest breakpoint there is: you can commit it by accident, but you cannot forget where you put it the way you forget a `console.log`.

# React DevTools

The browser extension adds two panels that plain DevTools does not have:

- **Components** — the live component tree, with every component's props and state visible and editable. This is the only way to *see* state rather than print it, and it is what turns "the list did not update" into "the state changed but the key did not", which are different bugs.
- **Profiler** — which components re-rendered and why. Ignore this until something is slow; it answers a question you do not have yet.

# Reading an error before reacting to it

Most React errors name the component and the hook. Read the first three lines of the stack before changing anything: the frame you want is usually the topmost one that belongs to *your* file rather than to `react-dom`.
