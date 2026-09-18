# The Three States of Remote Data

Up to now, every component that had data simply had it. This note is about what happens to a component when its data lives somewhere else — on the far side of a network, fifty milliseconds away on a good day and several seconds from a bad train connection — and the answer is not "it waits", because components cannot wait. It renders anyway, and you have to decide what it renders.

## The synchronous case hid the pattern

Here is how the to-do list loaded its data when the data was in `localStorage`:

```jsx
let [todos, setTodos] = useState(loadTodos);
```

A `useState` initializer has to **return the value**. `loadTodos` could, because `localStorage.getItem` is synchronous: the data is already on the machine, so the line after the call has it.

Reading the data and having the data happen at the same instant. There is no in-between moment, so there is nothing to render during it, so the component has exactly one state: the data.

This is a special case, and it is the only one you have met so far. It stops being available the moment the data is on a server. `fetchTodos()` cannot be a `useState` initializer, because it does not return to-dos — it returns a promise, and React would put the promise in your state.

## A fetch has three states, and your component has to render all three

The initial state can now only be "nothing yet", and the data has to arrive later, which is why it arrives through an effect. And the arrival itself has to become state, because the component needs to render differently before and after it:

```jsx
function ToDoList() {
	const [todos, setTodos] = useState([]);
	const [status, setStatus] = useState("loading");

	useEffect(() => {
		async function load() {
			try {
				setTodos(await fetchTodos());
				setStatus("ready");
			} catch (error) {
				console.error(error);
				setStatus("failed");
			}
		}
		load();
	}, []);

	if (status === "loading") return <p>Loading your to-dos…</p>;
	if (status === "failed") return <p>Could not reach the server. Try again.</p>;

	return (
		<ul>
			{todos.map((todo) => (
				<li key={todo.id}>{todo.text}</li>
			))}
		</ul>
	);
}
```

**Loading, failed, ready.** Three screens, from one fetch.

The rendering itself is nothing new — it is the early-return form of [conditional rendering](Conditional-Rendering.md), which is why that note showed you three shapes and said the `if` was the one for whole-screen decisions. This is the screen it meant.

## `failed` is not the optional one

It is the one people leave out, because during development the server is on your own machine and it never fails.

Without it, a dead network looks exactly like an empty list. The user retries nothing, because as far as they can see nothing went wrong. A `catch` that only writes to the console is a bug with a comforting shape: you see the error while developing, and your users never do.

## The fourth state, and the bug it explains

A `ready` list can still have nothing in it, and *"you have no to-dos"* is a real screen that a real app needs. It is often the nicest screen in the app — the one that tells a new user what to do first.

So the states are really:

| state   | what it means              | what the user should see       |
| ------- | -------------------------- | ------------------------------ |
| loading | I have not heard back yet  | a skeleton, or a quiet message |
| failed  | I asked, and it went wrong | what went wrong, and a way to retry |
| empty   | I heard back: there is nothing | an invitation to add the first one |
| ready   | I heard back: here it is   | the data                       |

And now the bug in the to-do list has a name. The app already had an empty state:

```jsx
{todos.length === 0 ? <>Nothing to do</> : ( ... )}
```

When the data moved to a server, no loading state was added — so **the empty state impersonated the loading state**. `useState([])` gives an empty array, `length === 0` is true, and the screen cheerfully says *Nothing to do* when the truth is *I do not know yet*. Those are different things, and the user cannot tell them apart.

This is the general shape of the mistake: when a state is missing, some other state takes its place, and it is usually the one that looks most like success.

## What you render in each state is a design decision

`<p>Loading…</p>` is honest and takes a minute. A spinner is a rotating element in CSS, and there is nothing React-specific about it. Better than either, when you know the shape of what is coming, are **skeleton rows** — grey blocks the size of the real to-dos — because the layout does not jump when the data lands.

A spinner has a failure mode of its own: if the data usually arrives in 200ms, it appears and disappears before the eye resolves it, and the flicker reads as a glitch rather than as progress. Showing nothing for the first few hundred milliseconds often looks *faster* than showing a spinner immediately.

And for `failed`, the word "Retry" on a button is worth more than any amount of apology in the message. An error the user can do something about is a smaller error.

## You are going to write this again, and again

Every screen that fetches needs these states, which means the same pair of `useState` calls in every component that talks to the backend. Duplication that shows up in every component of a certain kind is usually telling you something, and later in the course we come back and do something about this one.

## Exam Questions

### 1. Why could `useState(loadTodos)` load the to-dos from `localStorage`, but cannot load them from a backend?

### 2. Name the three states a fetching component has, and say what the user sees in each.

### 3. This component fetches in a `useEffect` and starts with `useState([])`. What does the user see before the data arrives, and why is it wrong?

### 4. What is the difference between the `empty` state and the `loading` state, and what goes wrong when a component has only one of them?

### 5. Why is it not enough to `console.error` in the `catch`?
