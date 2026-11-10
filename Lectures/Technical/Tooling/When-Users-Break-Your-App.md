# When Users Break Your App

Two stories from [Zeeguu](https://zeeguu.org), a language-learning app, and what they say about inputs you did not think of as inputs, and about how you find out that something broke.

## Some users type extreme values on purpose

Zeeguu lets learners choose how many words they want to be learning at the same time. One user typed a 1 followed by fifty zeros into that box.

This is the familiar case. A field accepts a number, so someone tries the largest number they can type, out of curiosity rather than malice. The fix is the one you already know: validate the input, and decide what the largest sensible value is before a user decides it for you.

## Other users produce extreme values just by using the app a lot

The second story is more useful, because the user did nothing unusual.

When you click an article in the Zeeguu feed, the app also records which articles you scrolled past to get there, so it can learn which sources you keep ignoring. It sends that list to the server as a JSON array of ids, which the server stores in a database column that holds 4096 characters.

The feed loads 20 articles at a time. One user scrolled through roughly 80 pages, about 1,600 articles, and then clicked one. The list was about 12,700 characters long. The database refused it, the request failed, and the click was lost. The user clicked twice more and those were lost too.

Nobody typed anything extreme. The extreme value was built by *our* code, from ordinary behavior repeated more times than we had imagined. No form validation would have caught it, because there was no form.

## Anything that grows with use needs a limit you chose

List lengths, history, retries, upload sizes, session lengths: anything that grows each time the user does something will one day be bigger than you expected. "Nobody will scroll that far" is an assumption, and the code relies on it whether you wrote it down or not.

If you do not choose the limit, something else chooses it for you. Here it was a database column width, and it was enforced by crashing.

## Choose the limit from what the data is for

The scrolled-past list exists to detect sources a user skips. An article 1,500 cards above the click, flicked past in a fast scroll, says nothing about what the user wants. Keeping only the last 100 or so ids before the click keeps all of the meaning and fits the column with room to spare.

So the right limit came from asking what the data means, not from looking up how much the column can hold.

## Enforce the limit on the server

Capping the list in the web app would help. But the iOS and Android apps already installed on people's phones keep sending the old, uncapped lists until each user updates, which can take months. The client can be polite about limits; the server is the only place where a limit actually holds.

## Your users will not tell you

The user saw nothing: the click just did not register. If the app had not been reporting its own errors, the bug would still be there.

Error monitoring tools such as [Sentry](https://sentry.io) fix this. You add a few lines to your app:

```python
import sentry_sdk
sentry_sdk.init(dsn="https://...")
```

and from then on every unhandled exception is sent to a dashboard, along with the stack trace, the request, the browser and operating system, and the values of local variables. Sentry also works in the browser, for JavaScript errors that never reach your server at all.

For the story above, the Sentry report said, in one screen: this error, three times, on 5 October, from one person on Safari on a Mac, at this line of our code, with this SQL statement and these parameters. The 12,700-character list was right there in the parameters, which was the whole diagnosis. We did not have to reproduce the bug to understand it.

## A report nobody reads is the same as no report

A dashboard helps only if someone looks at it. Configure it to send an email or a chat message when a *new* kind of error appears, so the first occurrence reaches a person instead of sitting in a list.

Error reports are also user data. The report above contained a user id, an approximate location and part of that person's reading history. Scrub what you do not need before it leaves your server, and be careful whom you show the dashboard to.

## Exam Questions

### 1. A form field is validated to accept at most 1,000. Give an example of a value that still gets too large without any user typing it, and say where its limit should be enforced.

### 2. Why is it not enough to cap the scrolled-past list in the web app, when the web app is the one that builds it?

### 3. A bug causes a click to be silently ignored. The user does not complain. How would you find out it happened, and what would you need in the error report to fix it without reproducing it?
