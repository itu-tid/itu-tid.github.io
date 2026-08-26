# Exam Structure

## On the day

- **Demo** — 5–7 minutes, maximum.
- **Mini presentation** — 5–7 minutes: corrections or completions to the report, late
  changes to the code, and lessons learned. Late changes matter: realistically we will
  not have looked at the code more than a week before the oral exams, so anything you
  fixed or finished after submission is worth naming.
- **Group discussion** — 10 to 30 minutes.
- **Individual examination** — 15 minutes.
- **Feedback.**

The individual examination is where the course's deal is settled: you may have used AI
as much as you liked, and you own every line when we meet.

## Giving the demo

Five to seven minutes is short, and the failure modes are consistent — these came out of
watching previous cohorts present:

- **Open with a slide that says what the idea is.** Thirty seconds of "here is who this
  is for and what it does" before anything moves on screen.
- **Have real data in the system.** An app demoed with `asdf` and `test test` looks
  unfinished whatever the code is like.
- **Have a story, and rehearse it.** Not a feature tour — one path through the app that
  a real person would actually take. Steve Jobs' keynotes and Google's product demos are
  worth watching for exactly this.
- **Reset your state before you start.** The profile you have been developing against is
  full of debris. Clear it, or make a clean account.

## What you get asked

**About your code**
- Where is *this particular feature* implemented?
- What does *this code* do?
- How could *this code* be written better?
- This bug we just saw in the app — where would you start fixing it?
- *This piece of code* — when is it called?
- This feature — how is it modelled in the database?
- Which part of the code did you write yourself, and are most proud of?

**About your UI design**
- What are the limitations of the design on *this particular* screen?
- Which visual design principles are used on *this particular* screen?

**About design process**
- How do you organise a usability test?
- How do you prioritise what a usability test finds?

**About application architecture**
- What kinds of computation need to run *on the server*? How do you do that in Parse?
- What is the N+1 select problem, and how do you avoid it in Parse?

**React**
- How is routing implemented in React?
- How do you protect a route so it is not available to a user who is not logged in?
- What are hooks, and why? Which are the most used, and how do they work?
- How do you run code when a component is created?
- How can you reuse code with a custom hook? Do you have an example from your codebase?

**Parse**
- How do you model a one-to-many relationship in Parse? An example from your project?
- How do you secure your application's data in Parse?

Every note in [`Lectures/Technical/`](Lectures/Technical) also ends with its own
**Exam Questions** section. Those test the material; the ones above test *your project*.
