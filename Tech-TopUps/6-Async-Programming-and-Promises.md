
# Async Programming and Promises

- What is [asynchronous programming](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)?
	- Technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs


- [What are Promises and how to Use Them?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises) 
	- Using the `then` syntax for promises
	- Using `await` with promises in `async` functions
	- How to chain two promises? 


Promises are often used when requesting something from a server, as in the following example:

```javascript 
function fetchMorty() {

	return fetch('https://rickandmortyapi.com/api/character/2')
		.then(response => response.json())
		.then(data => console.log(data))
		.catch(error => console.error(error));

}
```

Declaring the function to be async allows us to use the `await` keyword and makes the code easier to read:

```js
async function fetchMorty() {

	const response = await fetch('https://rickandmortyapi.com/api/character/2');
	const data = await response.json();
	console.log(data);
}
```

Surely, one needs to also handle exceptions: 

```js
async function fetchMorty() {
	try {
		const response = await fetch('https://rickandmortyapi.com/api/character/2');
		const data = await response.json();
		console.log(data);
	} catch (error) {
		console.error(error);
	}
}
```

## Individual Work
- Solve the [Sequencing Animations](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Sequencing_animations) problem
- Mandatory reading:
	- [What are Promises and how to Use Them?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises) 
