# When Users Break Your App

Stories from [Zeeguu](https://zeeguu.org), a language-learning app, about inputs you did not think of as inputs, about how you find out that something broke, and about users who cost you money. This note is the problem; [Running Code Server-Side](../Backend/Running-Code-Server-Side.md) is the fix.

## Users find inputs you never thought of as inputs

Two stories from Zeeguu. The first is the one you expect; the second is the one worth learning from.

### Some users type extreme values on purpose

Zeeguu lets learners choose how many words they want to be learning at the same time. One user typed a 1 followed by fifty zeros into that box.

This is the familiar case. A field accepts a number, so someone tries the largest number they can type, out of curiosity rather than malice. The fix is the one you already know: validate the input, and decide what the largest sensible value is before a user decides it for you.

### Other users produce extreme values just by using the app a lot

The second story is more useful, because the user did nothing unusual.

When you click an article in the Zeeguu feed, the app also records which articles you scrolled past to get there, so it can learn which sources you keep ignoring. It sends that list to the server as a JSON array of ids, which the server stores in a database column that holds 4096 characters.

The feed loads 20 articles at a time. One user scrolled through roughly 80 pages, about 1,600 articles, and then clicked one. The list was about 12,700 characters long. The database refused it, the request failed, and the click was lost. The user clicked twice more and those were lost too.

Nobody typed anything extreme. The extreme value was built by *our* code, from ordinary behavior repeated more times than we had imagined. No form validation would have caught it, because there was no form.

## You find out only because the app reports its own errors

Nobody told us about the second story. We found out because Zeeguu sends its own errors to Sentry, an error-monitoring service.

### Your users will not tell you when things don't work

The user saw nothing: the click just did not register. If the app had not been reporting its own errors, the bug would still be there.

Error monitoring tools such as [Sentry](https://sentry.io) fix this. You add a few lines to your app:

```python
import sentry_sdk
sentry_sdk.init(dsn="https://...")
```

and from then on every unhandled exception is sent to a dashboard, along with the stack trace, the request, the browser and operating system, and the values of local variables. Sentry also works in the browser, for JavaScript errors that never reach your server at all.

For the story above, the Sentry report said, in one screen: this error, three times, on 5 October, from one person on Safari on a Mac, at this line of our code, with this SQL statement and these parameters. The 12,700-character list was right there in the parameters, which was the whole diagnosis. We did not have to reproduce the bug to understand it.

### Error reports, session recordings and your own logs answer different questions

Error monitoring answers *what broke*. Two other tools answer questions it cannot:

- **Session recording** (tools such as Contentsquare, formerly Hotjar, or Microsoft Clarity) records what users did on the page: where they clicked, how far they scrolled, where they hesitated. It answers *where do people get stuck*, which no error report shows, because getting stuck is not an error. It also records whatever is on the screen, so the same care about personal data applies, twice over.
- **Your own logs**: a table where your app writes the events you care about, such as "list shared", "translation requested", "item bought". It answers *what are people actually doing with the app*, in your own terms, and it is the only one of the three you fully control. The per-day translation limit below is such a log: to count a user's translations, you have to have written them down.

For a user study, the third is the most useful: you can count how often the feature you built is used, instead of asking.

## A limit has to be chosen, enforced on the server, and explained on the client

The fix for the second story, and for every value that grows with use.

### Anything that grows with use needs a limit you chose

List lengths, history, retries, upload sizes, session lengths: anything that grows each time the user does something will one day be bigger than you expected. "Nobody will scroll that far" is an assumption, and the code relies on it whether you wrote it down or not.

If you do not choose the limit, something else chooses it for you. Here it was a database column width, and it was enforced by crashing.

### Choose the limit from what the data is for

The scrolled-past list exists to detect sources a user skips. An article 1,500 cards above the click, flicked past in a fast scroll, says nothing about what the user wants. Keeping only the last 100 or so ids before the click keeps all of the meaning and fits the column with room to spare.

So the right limit came from asking what the data means, not from looking up how much the column can hold.

### Only a limit on the server holds

Capping the list in the web app would help. But the iOS and Android apps already installed on people's phones keep sending the old, uncapped lists until each user updates, which can take months. The client can be polite about limits; the server is the only place where a limit actually holds.

### The frontend explains a limit; the backend enforces it

Every limit therefore lives in two places, and each has a different job.

**The backend enforces.** It refuses whatever breaks the rule, from any client, in any version, including a script that never saw your form. It does not need to be friendly; it needs to be there.

**The frontend explains.** It is where the user meets the limit, so it is where the limit has to make sense:

- **before** they hit it: a field that says *0–100 words*, a counter that says *180/200*, a list that says *12 of 500 items*;
- **while** they approach it: a warning as the counter nears the end, not a surprise after pressing Save;
- **when** they hit it anyway: a message in the user's terms (*"A list can hold at most 500 items"*), not the server's (*"Error 142"*), and without throwing away what they typed.

A limit that only the backend knows feels like a bug to the user: the button worked yesterday, and today it silently does nothing. A limit that only the frontend knows is not a limit at all. So write it twice, with the same number, and when it changes, change both.

### Form validation is the frontend's half of a limit

Since week 2, todo-26's Add button is disabled while the field is empty: `disabled={text.length === 0}`. That is form validation, the smallest kind. The same form can explain the rest of its limits.

#### The browser checks simple rules by itself, and says so in its own words

HTML inputs take their rules as attributes, and the browser enforces them before the form is submitted:

```jsx
<input required maxLength={200} />           // not empty, at most 200 characters
<input type="email" required />              // looks like an email address
<input type="number" min={0} max={100} />    // a number within a range
```

It is free, and it works without any JavaScript. But the browser chooses the wording and the moment, and some rules are silent: `maxLength` just stops accepting keys, so the user does not learn why their typing stopped.

#### A controlled input can explain a limit before the user reaches it

Because the text is state ([Forms and Controlled Components](../React/Forms-and-Controlled-Components.md)), anything about it can be shown while the user types, and none of it needs new state:

```jsx
const MAX = 200;

<input value={text} onChange={(e) => setText(e.target.value)} maxLength={MAX} />
<small>{text.length}/{MAX}</small>
<button disabled={text.trim().length === 0}>Add</button>
```

The counter is derived from `text`, like the disabled button. It turns a silent `maxLength` into a limit the user can see coming.

#### An error shown on the first keystroke is stupid and anti-usability! 

"Not a valid email" appearing after the user typed one letter is not help: they were not finished. Show a field's error when the user leaves the field or presses submit, and from then on update it as they type, so that it disappears the moment the value becomes valid.

#### A failed save must not throw away what the user typed

todo-26's `AddForm` clears the field right after handing the text to `onAdd`, before anyone knows whether the save worked:

```jsx
onAdd(task);
setTask("");   // gone, even if the server refuses it a second later
```

When the server refuses (the list is full, the text too long), the user's input is already gone. Clear the field only after the save succeeded, and show the server's reason when it did not:

```jsx
try {
  await onAdd(task);
  setTask("");
} catch (error) {
  setError(error.message); // e.g. "A list can hold at most 500 to-dos"
}
```

The server's message is the backend's half of the limit reaching the user; [Running Code Server-Side](../Backend/Running-Code-Server-Side.md#a-toast-tells-the-user-what-the-server-refused-without-stopping-them) shows where it comes from.

## Some users cost you money, and some users are scripts

So far the extreme values were accidents. The next ones cost you money, or come from someone who never opened your form.

### Anything that costs you money per use needs a limit per user

Some of what your app does is free to you. Some is not. Zeeguu translates any word a learner taps, and every translation is a request to a paid translation service. One user tapping a thousand words a day is a learner; a script tapping a million is a bill. So Zeeguu limits **how many translations a user can ask for per day**. Nobody reading normally comes near the limit, and a runaway client or a misused account stops at it. The [next note](../Backend/Running-Code-Server-Side.md#a-secret-key-stays-on-the-server-and-the-app-asks-the-server-to-use-it) shows what such a limit looks like in code: about ten lines that count today's translations before calling the service.

The same holds for anything metered: AI calls, text messages, emails, storage, even your free tier's request count. For each one, decide what a heavy but honest user needs, and stop there.

### Creating an account is free, so somebody will create a million

Zeeguu also limits **how many accounts can be created from the same network address** in a given time. Without such a limit, a script can create accounts as fast as the server answers: to spam other users, to get around the per-user limits above (a fresh account has a fresh daily quota), or just to fill your database.

The common defenses, from cheapest to most annoying for honest users:

- a limit on sign-ups per IP address per hour;
- a confirmation email that has to be clicked before the account works;
- a CAPTCHA on the sign-up form.

### Your form adds one item at a time; a script adds a million

Look at your own app with these two in mind:

1. **How do you stop one user from creating a million to-dos (or dishes, or records) in their list?** Your form adds one at a time, but a script calls `save()` in a loop.
2. **How do you stop one person from creating a million accounts?** Your sign-up page is public, and so is the class that stores your users.

Neither has an answer on the client, for the reason in [Running Code Server-Side](../Backend/Running-Code-Server-Side.md#a-rule-belongs-on-the-server-if-it-must-hold-no-matter-what-the-user-does): the user controls the client. Both answers are a few lines of server code, in the next note.

## Exam Questions

### 1. A form field is validated to accept at most 1,000. Give an example of a value that still gets too large without any user typing it, and say where its limit should be enforced.

### 2. A bug causes a click to be silently ignored. The user does not complain. How would you find out it happened, and what would you need in the error report to fix it without reproducing it?

### 3. Error reports, session recordings and your own logs: which question does each answer?

### 4. Why is it not enough to cap the scrolled-past list in the web app, when the web app is the one that builds it?

### 5. How would you stop one user from creating a million to-dos, and one person from creating a million accounts? Why is neither possible on the client alone?
