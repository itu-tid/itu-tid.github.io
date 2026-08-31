
# Async Programming and Promises

- What is [asynchronous programming](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)?
	- Technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs


- [What are Promises and how to Use Them?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)
	- Using the `then` syntax for promises
	- Using `await` with promises in `async` functions
	- How to chain two promises?


Promises are often used when requesting something from a server, as in the following example:

```js 
const RM_API="https://rickandmortyapi.com/api";

function fetchMorty() {
	return fetch(RM_API+'/character/2')
		.then(response => response.json())
		.then(data => console.log(data))
		.catch(error => console.error(error));

}
```

Declaring the function to be async allows us to use the `await` keyword and makes the code easier to read:

```js
const RM_API="https://rickandmortyapi.com/api"

async function fetchMorty() {
	const response = await fetch(RM_API+'/character/2');
	const data = await response.json();
	console.log(data);
}
```

Surely, one needs to also handle exceptions:

```js
async function fetchMorty() {
	try {
		const response = await fetch(RM_API+'/character/2');
		const data = await response.json();
		console.log(data);
	} catch (error) {
		console.error(error);
	}
}
```

# Individual Work
- Solve the [Sequencing Animations](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Sequencing_animations) problem

# References
- [What are Promises and how to Use Them?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises) -- an overview at *mdn* (Mozila Developer Network)
- [Video discussion](https://www.youtube.com/watch?v=li7FzDHYZpc) about how to transform a `Promise.then()` into `async/await` call



# `await` or `.then()` — does it matter for speed?

Only when you have several calls in a row, and then it depends on whether they have to happen in order.

**Serial** — each call needs the previous one's answer. No difference between the two: both wait, because you have no choice but to wait.

**Parallel** — the calls are independent. Now it matters, because awaiting each in turn makes them queue up for no reason:

```js
const user = await getUser();      // waits
const todos = await getTodos();    // then waits again — for nothing
```

Start them both, then wait for both:

```js
const [user, todos] = await Promise.all([getUser(), getTodos()]);
```

`Promise.all` when the calls do not depend on each other is the part worth remembering. There is a [long StackOverflow discussion](https://stackoverflow.com/questions/54495711/async-await-vs-then-which-is-the-best-for-performance/54497100#54497100) if you want the detail.
