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


