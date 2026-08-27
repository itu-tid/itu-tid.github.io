# Working as a Team

How the four of you are expected to divide the project, and what we are looking at when
we watch you do it. Assessment itself lives in the [syllabus](syllabus.html) — this page
is about the working arrangement, not the marking.

## Divide by functionality, not by technology

Each of you takes a slice of what the app *does* and builds all of it: the interface, the
state behind it, and the queries under that. A slice might be a screen, a feature, or a
capability — sharing, time-tracking, whichever your app actually has. Some apps have four
obvious pieces and some have three; what matters is that the cut is vertical.

What we do not want is the cut going the other way — one person doing the CSS, another
the React, another the Parse. It is an efficient way to build one app and a poor way to
learn four people's worth of React, and it collapses at the exam, where you are asked
about your project rather than about your layer of it.

## Everyone leaves fingerprints

Every member should have substantial code in the repository that is identifiably theirs,
and `git blame` is how we check. It is a blunt instrument, so treat it as the floor
rather than the definition:

- It says nothing about understanding. Code an agent wrote and you pasted blames to you
  just the same, and the exam is where that comes apart.
- It is noisy. A reformat, a merge, or whoever does the final integration pass can
  reassign whole files.
- And it must not stop you touching each other's code. Improving somebody's component is
  the point; a group where everyone stays in their own files is failing differently.

Two failure modes, and we look for both:

- **Somebody not coding.** Usually not laziness — usually somebody who fell behind in
  the second week and never found a way back in. Notice it in the first month, not the last.
- **Somebody coding everything.** More common, and more damaging, because it looks like
  the project is going well right up until the exam.

If you are the strongest programmer in the group, that is a job rather than a licence:
**do not carry the project, carry the others.** Pair with whoever is stuck, review their
pull request instead of rewriting it, and let them push the thing they wrote.

## More is not better

A **small app built well beats a big one built roughly**. The
required core is small on purpose — owner → lists → items, sharing at the list level —
and every extra feature has to earn its place against the population you chose.

One more screen does not impress us. What we want to see is that you understood the
ideas. If you have done the core well *and* built more, that is genuinely good, and we
will say so — but the order matters. Go slowly and do a good job.

## Own the code, whoever wrote it

At the exam we will point at code and ask you to explain what it does and why it is
shaped that way. **It does not matter whether you typed it.** Code written by a
teammate, and code written by an agent, are the same problem: it is in your project, so
it is yours to defend.

Your own code you should understand in detail — where the state lives, when the effect
runs, what happens if the query returns nothing. Everyone else's you should understand
well enough to say what it is for and how it fits.

This is the oldest rule in the course and the reason the rest of it is arranged the way
it is. Use AI as much as you like. Just make sure that when we point at a line, you can
tell us why it is there.

## Practical habits that make this work

- **Review each other's pull requests** rather than merging your own. Ten minutes of
  reading somebody else's code is the cheapest way to know what is in your project.
- **Rotate who does the awkward parts** — the data model, the deploy, the bug nobody
  wants. Those are the parts that get asked about.
- **Dogfood the app together.** You will find the problems your tests do not, and it
  keeps everyone in contact with the whole thing rather than their own screen.
