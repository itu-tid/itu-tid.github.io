# Class Discussion Guide: Component Architecture

**Topic:** Semantic Component Extraction & React Architecture
**Duration:** 90 minutes
**Format:** Interactive discussion + live coding demo

---

## 📋 Learning Objectives

By the end of this session, students will:
1. Understand why component abstraction matters
2. Identify "div soup" and "class soup" in their code
3. Apply the 4 core principles (Tech Lead, Semantic, DRY, SLA)
4. Know how to extract semantic components
5. Understand Sprint 2 requirements

---

## 🎯 Session Outline

### Part 1: The Problem (20 minutes)

#### A. Opening Question (5 min)
**Ask the class:**
> "If I gave your code to a backend developer who doesn't know CSS, could they understand your component structure?"

**Have 2-3 students answer:**
- Most will say "probably not"
- This sets up the problem

#### B. Show Real Examples (10 min)

**Example 1: "The Yikes Example"** (from open source)
```tsx
<div className="w-16 h-16 rounded text-white bg-black py-1 px-2 m-1 text-sm md:w-32 md:h-32 md:rounded-md md:text-base lg:w-48 lg:h-48 lg:rounded-lg lg:text-lg">
  Yikes.
</div>
```

**Ask:** "What is this div? What does it do?"
- Students won't be able to tell
- Point out: 20+ classes, no semantic meaning

**Example 2: The Netlify Story**
> "Netlify's admin dashboard had **71 class names** on a single checkbox. It took 13 lines in the browser inspector."

**Ask:** "How do you think code review went for that?"
- Discuss: impossible to review
- Point out: even big companies make this mistake

**Example 3: Generic Pattern** (CSS-agnostic)
```tsx
<div className="container-wrapper">
  <section className="inner-content">
    <div className="avatar-box">
      <img src={user.avatar} />
    </div>
    <h2 className="user-name">{user.name}</h2>
    {/* 200 more lines... */}
  </section>
</div>
```

**Ask:** "What's wrong here?"
- Let students identify:
  - Generic names (container-wrapper?)
  - Can't tell what page this is
  - Everything in one component
  - Not reusable

#### C. The Technical Lead Scenario (5 min)

**Tell this story:**
> "Imagine I'm your tech lead. I don't care about Tailwind, CSS Modules, or whatever you're using. I'm reviewing your PR for security issues, data flow, and architecture.
>
> I open your Profile.tsx file. I see 275 lines of divs with classes. I can't understand what this page does without mentally parsing all the CSS.
>
> **I close the PR and request changes: 'Please refactor to use semantic components.'**"

**Ask:** "Is this fair?"
- Have students debate
- Consensus: Yes, it's fair. Code should be readable.

**The point:**
> "You're not writing code for the computer. You're writing it for the next developer."

---

### Part 2: The Solution (25 minutes)

#### A. Introduce the 4 Principles (10 min)

Write on board/slide:

**1. The Tech Lead Test**
> "Can a non-CSS person understand your structure?"

**2. The Semantic Naming Test**
> "If you can name it in 1-2 words, that should be the component name."

**3. The DRY Test**
> "Repeated 3+ times? Extract a component."

**4. The Single Level of Abstraction (SLA)**
> "Don't mix high-level components with low-level HTML."

**For each principle, ask:**
- "Does your current code pass this test?"
- Most will say no - that's okay!

#### B. Show Before/After (15 min)

**Before:**
```tsx
const Profile = () => {
  return (
    <div className="mx-auto flex w-full max-w-xl flex-col items-start gap-6 px-4 py-6">
      <section className="flex w-full flex-col items-center gap-2 p-6">
        <div className="size-24 rounded-3xl bg-neutral-300">
          <img src={user.avatarUrl} alt={user.name} />
        </div>
        <h2 className="text-2xl font-bold">{user.name}</h2>
        <div className="flex items-center">
          {[...Array(5)].map((_, i) => (
            <Star key={i} className="h-5 w-5 text-yellow-400" />
          ))}
        </div>
        {/* 200 more lines... */}
      </section>
    </div>
  );
};
```

**Ask class:**
1. "Can you tell what this page does?" (hard)
2. "How many lines is this component?" (275)
3. "Could you reuse any of this?" (no)
4. "Is it testable?" (no)

**After:**
```tsx
const Profile = () => {
  const { user, loading, error } = useUserProfile();

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;
  if (!user) return <NotFound />;

  return (
    <ProfileContainer>
      <ProfileHeader user={user} />
      <ProfileSections user={user} />
    </ProfileContainer>
  );
};
```

**Ask class:**
1. "Can you tell what this page does?" (YES - profile page!)
2. "How many lines?" (15 vs 275)
3. "Could you reuse components?" (YES)
4. "Is it testable?" (YES - each component separately)

**Show the extracted components:**
```tsx
// components/layout/ProfileContainer.tsx
export const ProfileContainer = ({ children }: { children: ReactNode }) => {
  return (
    <div className="mx-auto flex w-full max-w-xl flex-col items-start gap-6 px-4 py-6">
      {children}
    </div>
  );
};

// components/profile/ProfileHeader.tsx
export const ProfileHeader = ({ user }: { user: UserProfile }) => {
  return (
    <header className="flex w-full flex-col items-center gap-2 p-6">
      <Avatar user={user} />
      <UserName>{user.name}</UserName>
      <StarRating rating={user.rating} />
    </header>
  );
};
```

**Point out:**
- Styling is hidden in component files
- Page shows structure clearly
- Each component < 100 lines
- Reusable everywhere

---

### Part 3: Live Coding Demo (30 minutes)

#### A. Choose a Real Example (5 min)

**Pick one of these:**
1. Button component (simple, good for beginners)
2. Card component (medium complexity)
3. List item component (shows patterns)

**For this example, let's use Button:**

#### B. Identify the Problem (5 min)

**Show repeated pattern in student code:**
```tsx
// Appears 10 times in their codebase
<button className="rounded-xl bg-neutral-200 px-4 py-2 hover:bg-neutral-300">
  Share
</button>

<button className="rounded-xl bg-neutral-200 px-4 py-2 hover:bg-neutral-300">
  Message
</button>

<button className="rounded-xl bg-green-500 px-4 py-2 hover:bg-green-600">
  Apply
</button>
```

**Ask:** "What's wrong here?"
- Students identify: repeated classes, copy-paste, not DRY

#### C. Extract Step-by-Step (20 min)

**Step 1: Identify variations**
```
What varies?
- Background color (neutral vs green)
- Hover color
- Text content

What stays same?
- Border radius
- Padding
- Text color
```

**Step 2: Create component file**
```tsx
// components/ui/Button.tsx
interface ButtonProps {
  variant?: 'secondary' | 'primary';
  children: ReactNode;
  onClick?: () => void;
}

export const Button = ({
  variant = 'secondary',
  children,
  onClick
}: ButtonProps) => {
  // TODO: implement
};
```

**Ask students:** "How do we handle the color variations?"

**Step 3: Implement variants**
```tsx
export const Button = ({ variant = 'secondary', children, onClick }: ButtonProps) => {
  const variantClasses = {
    secondary: 'bg-neutral-200 hover:bg-neutral-300',
    primary: 'bg-green-500 hover:bg-green-600 text-white'
  };

  return (
    <button
      className={`rounded-xl px-4 py-2 ${variantClasses[variant]}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```

**Step 4: Refactor usage**
```tsx
// Before: 3 separate buttons with repeated classes
<button className="rounded-xl bg-neutral-200 px-4 py-2 hover:bg-neutral-300">Share</button>
<button className="rounded-xl bg-neutral-200 px-4 py-2 hover:bg-neutral-300">Message</button>
<button className="rounded-xl bg-green-500 px-4 py-2 hover:bg-green-600">Apply</button>

// After: Clean, reusable components
<Button variant="secondary">Share</Button>
<Button variant="secondary">Message</Button>
<Button variant="primary">Apply</Button>
```

**Ask:** "What have we gained?"
- Let students list benefits:
  - Reusable
  - Consistent styling
  - Single source of truth
  - Easy to change (one place)
  - Testable
  - Clear intent

---

### Part 4: Student Exercise (10 minutes)

#### Hands-On Practice

**Give students this code:**
```tsx
<div className="flex items-center rounded bg-white shadow-md overflow-hidden mt-10">
  <img src={job.imageUrl} className="h-32 w-32 object-cover" />
  <div className="px-6 py-4">
    <h3 className="text-lg font-semibold">{job.title}</h3>
    <p className="text-sm text-gray-600">{job.location}</p>
  </div>
</div>
```

**Ask them to:**
1. Name this component (2 min thinking)
2. What props would it need? (2 min)
3. What file structure? (2 min)

**Have students share answers:**
- Good names: `JobCard`, `JobListItem`, `JobPreview`
- Bad names: `Card`, `Item`, `Component`

**Show solution:**
```tsx
// components/jobs/JobCard.tsx
interface JobCardProps {
  job: Job;
}

export const JobCard = ({ job }: JobCardProps) => {
  return (
    <article className="flex items-center rounded bg-white shadow-md overflow-hidden mt-10">
      <JobImage src={job.imageUrl} alt={job.title} />
      <JobInfo title={job.title} location={job.location} />
    </article>
  );
};
```

---

### Part 5: Sprint 2 Introduction (5 minutes)

#### Requirements Overview

**Hand out SPRINT_2_ASSIGNMENT.md**

**Summarize key points:**
1. **Extract components** from all your pages
   - Layout components
   - UI primitives
   - Domain components

2. **Use semantic naming** throughout

3. **Organize in folders**
   - `components/layout/`
   - `components/ui/`
   - `components/[domain]/`

4. **Document your work**
   - COMPONENTS.md
   - REFACTORING.md

5. **Metrics to achieve:**
   - Pages < 100 lines
   - Components < 150 lines
   - 50-70% code reduction

**Timeline:**
- Week 1: Layout components
- Week 2: UI primitives + domain
- Week 3: Refactor + document

---

### Part 6: Q&A (10 minutes)

#### Common Questions

**Q: "How do I know when to extract a component?"**
A: Use the 4 tests. If it fails any test, consider extraction.

**Q: "Can I use @apply with Tailwind?"**
A: Yes, but component extraction is better. Components are reusable in React, @apply is just CSS.

**Q: "What if my component needs many props?"**
A: If > 8 props, consider breaking into smaller components or using composition.

**Q: "Do I need to extract everything?"**
A: No. If it's < 10 lines and used once, keep it inline.

**Q: "What about styled-components users?"**
A: Same principles! Extract semantic components, even with styled-components.

**Q: "How small should components be?"**
A: No hard rule, but aim for < 150 lines. If larger, probably doing too much.

---

## 🎯 Key Messages to Emphasize

1. **"Code is read 10x more than it's written"**
   - Optimize for reading

2. **"Think in components, not in divs"**
   - React is component-based, use it that way

3. **"Name by purpose, not appearance"**
   - `PrimaryButton` not `BlueButton`

4. **"This is how professionals write React"**
   - These are industry standards

5. **"CSS framework doesn't matter"**
   - Principles apply to Tailwind, CSS Modules, styled-components, everything

---

## 📊 Assessment Checkpoint

**Quick poll at end:**
- "Raise hand if you understand why component extraction matters"
- "Raise hand if you know how to start Sprint 2"
- "Raise hand if you have questions"

**Look for:**
- Most students should raise hands for first two
- Some questions are good - shows engagement

---

## 📚 Materials to Share

**After class, post to LMS/Slack:**
1. COMPONENT_EXTRACTION_GUIDE.md
2. COMPONENT_EXTRACTION_CHEATSHEET.md
3. SPRINT_2_ASSIGNMENT.md
4. Link to Semantic JSX article
5. Office hours schedule

---

## 💡 Teaching Tips

### If Class is Quiet:
- Call on specific students
- Ask for examples from their code
- Do think-pair-share activities

### If Running Over Time:
- Skip the live coding, show completed version
- Make exercise homework
- Cut Q&A to 5 minutes

### If Students Don't Get It:
- Use more examples
- Draw component trees on board
- Show their actual code (anonymized)

### If Students Are Defensive:
- Emphasize: "This is how I learned too"
- Show: "Even big companies (Netlify) made these mistakes"
- Frame as: "Level up your skills" not "your code is bad"

---

## 🎓 Follow-Up Actions

### Immediately After Class:
- [ ] Post all materials to LMS
- [ ] Create Slack channels (#sprint-2-help, #component-examples)
- [ ] Schedule office hours
- [ ] Announce TA pairing sessions

### During Sprint 2:
- [ ] Review student progress weekly
- [ ] Share good examples in #component-examples
- [ ] Host mid-sprint check-in session
- [ ] Provide individual feedback as needed

### Before Demo Day:
- [ ] Review all submissions
- [ ] Prepare feedback for each team
- [ ] Select exemplary examples to showcase
- [ ] Prepare Sprint 3 based on results

---

## 📈 Success Metrics

**This session is successful if:**
- Students understand the "why" behind component extraction
- Students can apply the 4 principles
- Students know how to start Sprint 2
- Students are motivated (not defensive)
- Office hours get booked

**Red flags:**
- Most students look confused
- Defensive reactions ("but my code works!")
- No questions (means they're lost or don't care)
- Office hours stay empty

---

## 🔄 Iteration Notes

**After teaching, reflect:**
- What examples worked best?
- Where did students struggle?
- What questions came up?
- How to improve for next time?

**Update this guide based on experience.**

---

Good luck with the session! Remember: You're teaching them **professional software engineering**, not just React. This is valuable career preparation.
