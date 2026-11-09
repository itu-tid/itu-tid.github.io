
# Refactoring by Extracting Components

**Lesson:** refactoring is critical for having a codebase that is maintainable and pleasant to work with

#### Challenge: Compare the following equivalent versions of `Home` in todo-26

- They have **exactly the same behavior**: the same page, the same links and buttons
- Which of them is easier to read?

##### Version 1 — `git checkout week-08-service-layer`

```jsx
<h2>My lists</h2>
{lists.map((item) => (
  <div key={item.id}>
    <Link to={`/lists/${item.id}`}>{item.get("name")}</Link>
    <AddForm
      onAdd={(username) => onShare(item, username)}
      buttonLabel="Share with (username)"
    />
  </div>
))}

{memberships.length > 0 && <h2>Shared with me</h2>}
{memberships.map((membership) => (
  <p key={membership.id}>
    <Link to={`/lists/${membership.get("list").id}`}>
      {membership.get("list").get("name")}
    </Link>{" "}
    shared by{" "}
    {membership.get("list").get("owner")?.get("username") ?? "someone"}{" "}
    <button onClick={() => onLeave(membership)}>Leave</button>
  </p>
))}

<h3>List Manager</h3>
<AddForm onAdd={onAddList} buttonLabel="New list" />
<h3>Account</h3>
<button onClick={onLogout}>Logout</button>
```

##### Version 2 — `git checkout week-08-components`

```jsx
<h2>My lists</h2>
{lists.map((list) => (
  <MyListRow key={list.id} list={list} onShare={onShare} />
))}

{memberships.length > 0 && <h2>Shared with me</h2>}
{memberships.map((membership) => (
  <SharedListRow key={membership.id} membership={membership} onLeave={onLeave} />
))}

<h3>List Manager</h3>
<AddForm onAdd={onAddList} buttonLabel="New list" />
<h3>Account</h3>
<button onClick={onLogout}>Logout</button>
```

- Version 2 reads like the page: two headings, two kinds of row, a form, a button. Everything in it is at the same abstraction level, that of the page.
- Version 1 is at every level at once
	- the page: headings, sections
	- one row: a link, a form, a button
	- the data: `membership.get("list").get("owner")?.get("username")`, a pointer followed through a pointer
	- the text between the elements: `{" "}`

The details did not go away. They moved to [`SharedListRow`](Finding-the-Components.md#extracting-a-component-is-moving-jsx-out-and-naming-what-it-needs), where they are the whole point, and you read them only when the row is what you care about.

#### Principle: Code in a component should be at the same abstraction level

#### Advice: iterate. iterate. iterate
- there is no way to arrive to simple code without a lot of iteration

#### Advice 2: first make it work. then refactor it and make it nice
- you never get it right from the first time

<!-- TODO: This could be a good place for some fast-paced exercises that ask "which one do you prefer?", in the style of the UI style exercises. They could even use the students' own projects: by this point in the course, they all have enough examples. -->

## Where the State Goes

Extraction has a consequence. Split one component into three and some of them will need to agree about the same piece of state — which now belongs to none of them. The two patterns from [Component Communication](../React/Patterns-of-Component-Communication.md) (props down, callbacks up) are not enough on their own.

### sibling to sibling by "*lifting the state*"

Sometimes, you want the state of two components to always change together.

To do it, you _lift the state up_:
- remove state from both of them
- move it to their closest common parent, and then
- pass it down to them via props


This is a common thing you will do when writing React


**Example**: in the TODO list application, ensuring that one can't start two tasks in two different lists

### Sending a message from one component to the other

- also has to be done via the parent
- in our case, imagine that you want to move one of the tasks, from one list to the other
- the parent would have to know about all the lists and a given list will have to call a callback on the parent to decide to which list does one

**To read for next time**: [Sharing state between components](https://react.dev/learn/sharing-state-between-components)
- talks about lifting state with an example


### Exam Questions

#### 1. What does "lifting state up" mean in React?

#### 2. Why is this principle important: *"Code in a component should be at the same abstraction level"*?

## The same function, written twice

Components are not the only thing worth extracting. A common case: `const getCurrentUser = async () => …` defined once in `ProfileBar` and again in `Settings`, because both screens needed it and neither knew about the other.

Two copies of a function are two things to fix when the backend changes, and they drift silently — one gets a null check, the other does not. Pull it into a **custom hook** (`useCurrentUser`) and both screens call the same code.

The signal to watch for: you are about to write something you have a feeling you already wrote. You probably did.
