# One-Week Intensive: Component Architecture Refactoring

**Duration:** 1 week (Sprint 2)
**Class Sessions:** 2 sessions (90 min each)
**Focus:** High-impact refactoring essentials

---

## 🎯 Week Overview

**Reality Check:** We only have 1 week, so we're focusing on the **highest-impact changes** that make code readable and professional.

### Learning Objectives (Prioritized)

Students will be able to:
1. ✅ **Identify** component architecture problems (div soup, class soup)
2. ✅ **Apply** semantic naming to components
3. ✅ **Extract** the most problematic patterns from their code
4. ✅ **Eliminate** inline styles and inconsistent patterns
5. ✅ **Document** what they changed and why

### What We're NOT Covering (Save for Later)
- ❌ Building complete design systems
- ❌ Advanced composition patterns
- ❌ Comprehensive component libraries
- ❌ Performance optimization
- ❌ Testing strategies

---

## 📅 One-Week Schedule

| Day | Activity | Duration | Deliverable |
|-----|----------|----------|-------------|
| **Monday** | Session 1: The Problem & Principles | 90 min | Read materials |
| **Tuesday** | - | - | Identify issues in code |
| **Wednesday** | Session 2: Refactoring Workshop | 90 min | Start refactoring |
| **Thu-Fri** | Office hours + work time | 4 hours | Refactor code |
| **Saturday** | - | - | Final submission |
| **Next Monday** | Quick presentations (optional) | 30 min | 2-min demos |

---

## 📚 Materials Distribution

### Before Monday Session
**Post to LMS:**
- [ ] SPRINT_2_ASSIGNMENT_ONE_WEEK.md (simplified version)
- [ ] Announcement: "Important 1-week intensive on component architecture"

### During Monday Session
**Distribute:**
- [ ] COMPONENT_EXTRACTION_CHEATSHEET.md (essential!)
- [ ] CASE_STUDY_TODO_APP.md

### After Monday Session
**Optional reading:**
- [ ] COMPONENT_EXTRACTION_GUIDE.md (for those who want depth)

---

## 📖 Session 1: "Why Your Code is Hard to Read" (90 minutes)

**Monday - Focus: Understanding & Motivation**

### Materials Needed
- Projector
- CLASS_DISCUSSION_GUIDE.md (your script)
- Anonymized student code examples from Sprint 1
- CASE_STUDY_TODO_APP.md

---

### Part 1: The Wake-Up Call (20 min)

#### 1.1 Opening Hook (5 min)
```
"Show of hands: Who has written code that works perfectly,
but when you read it a week later, you can't understand it?"

[Most hands go up]

"That's what we're fixing this week. Not functionality - READABILITY."
```

**The Scenario:**
> "You're in a job interview. They ask to review your portfolio code.
> They open your Profile.tsx: 275 lines, divs everywhere, classes everywhere.
>
> Interviewer: 'Walk me through this structure.'
> You: '...umm...'
>
> Interview over."

#### 1.2 Real Examples (10 min)

**Show 3 quick examples:**

1. **"The Yikes Example"** (from open source)
   ```jsx
   <div className="w-16 h-16 rounded text-white bg-black py-1 px-2 m-1
                   text-sm md:w-32 md:h-32 md:rounded-md md:text-base">
     Yikes.
   </div>
   ```
   **Ask:** "What is this div?"
   **Answer:** Nobody knows!

2. **Netlify's 71 Classes**
   - Production code from Netlify
   - Single checkbox: 71 class names, 13 lines
   - Even professionals make this mistake

3. **Your Student Code** (anonymized)
   ```jsx
   <div className="mx-auto flex w-full max-w-xl flex-col items-start gap-6 px-4 py-6">
     <section className="flex w-full flex-col items-center gap-2 p-6">
   ```
   **Ask:** "What page is this? What's the structure?"
   **Point:** Can't tell without reading every class

#### 1.3 The Core Problem (5 min)

Write on board:
```
PROBLEM: Code optimized for computers, not humans

Your code works ✅
Your code is unreadable ❌

In real jobs:
- Code is read 10x more than written
- Code reviews happen daily
- Team members need to understand your code
- Future you needs to understand past you
```

---

### Part 2: The 3 Essential Principles (20 min)

**Simplified from 4 to 3 for one week:**

#### Principle 1: The Tech Lead Test (7 min)
> "Can someone who doesn't know your CSS framework understand your structure?"

**Bad:**
```jsx
<div className="container-wrapper">
  <div className="inner-section">
    <div className="content-box">
```
**Can you tell what this is?** NO.

**Good:**
```jsx
<ProfileContainer>
  <ProfileHeader>
    <ProfileInfo>
```
**Can you tell what this is?** YES!

**The Rule:**
"If it requires CSS knowledge to understand structure, it's wrong."

#### Principle 2: Semantic Naming (7 min)
> "If you can name it in 1-2 words, that should be the component name."

**Examples on board:**
```
❌ Bad Names:
- Container, Wrapper, Box, Div
- Component1, Component2
- BlueButton (describes appearance)
- div className="profile-info"

✅ Good Names:
- ProfileContainer, ProfileHeader
- JobCard, ExperienceEntry
- PrimaryButton (describes purpose)
- <ProfileInfo> (styled component)
```

**The Rule:**
"Name by PURPOSE, not appearance or generic type."

#### Principle 3: No Inline Styles (6 min)
> "Pick ONE styling approach and stick with it everywhere."

**Bad (inconsistent):**
```jsx
// Some styled-components
<AuthContainer>
  <Title>Login</Title>

  // Suddenly inline styles!
  <div style={{ marginTop: '15px', textAlign: 'center' }}>
    Click here
  </div>
</AuthContainer>
```

**Good (consistent):**
```jsx
<AuthContainer>
  <Title>Login</Title>
  <ToggleSection>
    Click here
  </ToggleSection>
</AuthContainer>
```

**The Rule:**
"If you're using styled-components, use them EVERYWHERE. If CSS Modules, use them EVERYWHERE. No mixing!"

---

### Part 3: Case Study - Real Code (25 min)

**Use CASE_STUDY_TODO_APP.md**

#### 3.1 Show What's Good (5 min)
```jsx
// LoginPage.jsx - THIS is the pattern we want
import { AuthContainer, Title, Form, Input, Button } from "./LoginPage.styles";

<AuthContainer>
  <Title>Log In</Title>
  <Form onSubmit={handleSubmit}>
    <Input placeholder="Username" />
    <Button type="submit">Log In</Button>
  </Form>
</AuthContainer>
```

**Point out:**
- Clear semantic names
- No generic divs
- Easy to understand structure

#### 3.2 Show 2 Problems (15 min)

**Problem 1: Mixing Inline Styles** (Case Study Issue #1)
```jsx
// ❌ BAD - Inconsistent!
<Form onSubmit={handleSubmit}>
  <Input />
  <Button>Submit</Button>
</Form>

<div style={{ textAlign: "center", marginTop: "15px" }}>
  Click here
</div>
```

**Show the fix:**
```jsx
// ✅ GOOD - Consistent!
<Form onSubmit={handleSubmit}>
  <Input />
  <Button>Submit</Button>
</Form>

<ToggleSection>
  Click here
</ToggleSection>
```

**Problem 2: Plain HTML in Component Code** (Case Study Issue #4)
```jsx
// ❌ BAD - Plain HTML mixed with styled-components
<TodoList>
  {items.map(item => ...)}
</TodoList>

<input type="text" onChange={...} value={input} />
<button onClick={handleAdd}>Add</button>
```

**Show the fix:**
```jsx
// ✅ GOOD - Everything styled
<TodoList>
  {items.map(item => ...)}
</TodoList>

<AddTaskSection>
  <TaskInput onChange={...} value={input} />
  <AddButton onClick={handleAdd}>Add</AddButton>
</AddTaskSection>
```

#### 3.3 Key Takeaway (5 min)
"Even when using good tools like styled-components, you can still write messy code. **Consistency is everything.**"

---

### Part 4: Your Assignment (20 min)

#### 4.1 The Challenge (5 min)

**Show the metrics goal:**
```
Your Goal This Week:

1. Eliminate ALL inline styles (style={{}})
2. Create semantic names for ALL styling
3. Consistent approach throughout
4. Document what you changed

You DON'T need to:
❌ Build a complete design system
❌ Extract every possible component
❌ Achieve perfect architecture

You DO need to:
✅ Fix the most obvious problems
✅ Make code readable
✅ Be consistent
```

#### 4.2 Step-by-Step Plan (10 min)

Write on board:
```
STEP 1 (Tuesday): Audit Your Code
- Find all inline styles (search for "style={{")
- Find all plain HTML (input, button, div, etc.)
- Find all generic names (Container, Wrapper)
- List them in a document

STEP 2 (Wednesday in class): Learn Patterns
- We'll do live refactoring
- You'll see exactly how to fix issues

STEP 3 (Wed-Fri): Refactor Your Code
- For styled-components users: Create styled components
- For CSS Module users: Use className consistently
- For Tailwind users: Extract semantic components
- Replace inline styles
- Replace plain HTML
- Use semantic names

STEP 4 (Saturday): Document
- Write REFACTORING.md
- What did you change?
- Why is it better?
- What did you learn?
```

#### 4.3 Deliverables (5 min)

**Due Saturday (End of Week):**
```
Required:
1. Code Changes:
   - NO inline styles (style={{}}) anywhere
   - NO plain HTML mixed with styled components
   - Semantic names for all styling
   - Consistent approach throughout

2. Documentation (REFACTORING.md):
   - Before/after code snippets (3 examples)
   - What changed and why
   - Lessons learned (2-3 sentences)

3. All code pushed to GitHub

Grading (100 points):
- Consistency (40 pts) - One styling approach everywhere
- Semantic Naming (30 pts) - Clear, purposeful names
- No Inline Styles (20 pts) - All style={{}} removed
- Documentation (10 pts) - REFACTORING.md complete
```

---

### Part 5: Tuesday Homework (5 min)

**Assign for tomorrow:**
- [ ] Read COMPONENT_EXTRACTION_CHEATSHEET.md (8 pages)
- [ ] Audit your code (find all inline styles, plain HTML, generic names)
- [ ] Bring your audit to Wednesday session
- [ ] Come with specific questions

**Optional reading:**
- COMPONENT_EXTRACTION_GUIDE.md (if you want deeper understanding)
- CASE_STUDY_TODO_APP.md (review all 6 issues)

---

## 📖 Session 2: "Refactoring Workshop" (90 minutes)

**Wednesday - Focus: Hands-On Fixing**

### Materials Needed
- Student code audits from Tuesday
- Live coding setup
- CASE_STUDY_TODO_APP.md examples ready

---

### Part 1: Audit Review (15 min)

#### 1.1 Share Findings (10 min)
"What did you find in your code audit?"

Poll the class:
- "How many inline styles did you find?" (write numbers on board)
- "How many plain HTML elements mixed with styled components?"
- "How many generic names (Container, Wrapper, Div)?"

**Typical results:**
- Inline styles: 10-30 per student
- Plain HTML: 20-50 instances
- Generic names: 5-15

**The Point:**
"These aren't errors - your code works! But they make code hard to read and maintain."

#### 1.2 Prioritize Fixes (5 min)
"You can't fix everything perfectly in one week. Priority order:"
```
1. FIRST: Eliminate ALL inline styles
   - Easiest to find (search for "style={{")
   - Biggest readability impact
   - Clear right/wrong

2. SECOND: Fix plain HTML mixed with components
   - Consistency is key
   - If using styled-components, style EVERYTHING
   - If using CSS Modules, className EVERYTHING

3. THIRD: Improve names
   - Change generic to semantic
   - Takes more thought
   - Do what you can
```

---

### Part 2: Live Refactoring - Issue #1 (20 min)

**Fix inline styles → styled components**

#### 2.1 Show the Problem (5 min)
```jsx
// Real student code (anonymized)
export default function RemoveButton({ onClick }) {
  return (
    <a
      href="#"
      onClick={onClick}
      style={{
        color: "#a2a2a2cf",
        fontSize: "xx-small",
        marginLeft: "2em",
        textDecoration: "none",
      }}
    >
      (remove)
    </a>
  );
}
```

**Ask class:** "What's wrong here?"
- All styling inline
- Using <a> tag incorrectly
- Not reusable
- Can't theme
- Hard to change later

#### 2.2 Refactor Live (12 min)

**For styled-components users:**
```jsx
// STEP 1: Create styled component
// RemoveButton.styles.js (NEW FILE)
import styled from "styled-components";

export const StyledRemoveButton = styled.button`
  background: none;
  border: none;
  color: rgba(162, 162, 162, 0.81);
  font-size: 0.625rem;
  margin-left: 2rem;
  text-decoration: none;
  cursor: pointer;
  padding: 0;

  &:hover {
    color: red;
    text-decoration: underline;
  }
`;

// STEP 2: Use it
// RemoveButton.jsx
import { StyledRemoveButton } from "./RemoveButton.styles";

export default function RemoveButton({ onClick }) {
  return (
    <StyledRemoveButton onClick={onClick}>
      (remove)
    </StyledRemoveButton>
  );
}
```

**For CSS Modules users:**
```css
/* RemoveButton.module.css (NEW FILE) */
.removeButton {
  background: none;
  border: none;
  color: rgba(162, 162, 162, 0.81);
  font-size: 0.625rem;
  margin-left: 2rem;
  text-decoration: none;
  cursor: pointer;
  padding: 0;
}

.removeButton:hover {
  color: red;
  text-decoration: underline;
}
```

```jsx
// RemoveButton.jsx
import styles from "./RemoveButton.module.css";

export default function RemoveButton({ onClick }) {
  return (
    <button className={styles.removeButton} onClick={onClick}>
      (remove)
    </button>
  );
}
```

#### 2.3 Point Out Improvements (3 min)
What got better:
- ✅ No inline styles
- ✅ Proper semantic HTML (<button> not <a>)
- ✅ Added hover state (easy now!)
- ✅ Consistent with rest of codebase
- ✅ Easier to change later
- ✅ Can add theme colors if needed

---

### Part 3: Live Refactoring - Issue #2 (20 min)

**Fix plain HTML mixed with styled components**

#### 3.1 Show the Problem (5 min)
```jsx
// From TodoList.jsx
return (
  <>
    <Wrapper>
      <Title>{name}</Title>
    </Wrapper>

    <ul>
      {list.map(item => ...)}
    </ul>

    {/* Plain HTML! */}
    <input
      type="text"
      onChange={handleInputChange}
      value={input}
    />
    <button onClick={handleAddClick}>Add</button>
  </>
);
```

**Ask:** "What's inconsistent here?"
- Top uses styled components (Wrapper, Title)
- Bottom uses plain HTML (input, button)

#### 3.2 Refactor Live (12 min)

**Styled-components version:**
```jsx
// ToDoList.styles.js - Add these
export const TodoList = styled.ul`
  list-style: none;
  padding: 0;
  margin: 1rem 0;
`;

export const AddTaskSection = styled.div`
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
`;

export const TaskInput = styled.input`
  flex: 1;
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;

  &:focus {
    outline: none;
    border-color: #4CAF50;
  }
`;

export const AddButton = styled.button`
  padding: 0.75rem 1.5rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  &:hover {
    background-color: #45a049;
  }
`;

// ToDoList.jsx - Use them
import { TodoList, AddTaskSection, TaskInput, AddButton } from "./ToDoList.styles";

return (
  <>
    <Wrapper>
      <Title>{name}</Title>
    </Wrapper>

    <TodoList>
      {list.map(item => ...)}
    </TodoList>

    <AddTaskSection>
      <TaskInput
        type="text"
        onChange={handleInputChange}
        value={input}
      />
      <AddButton onClick={handleAddClick}>Add</AddButton>
    </AddTaskSection>
  </>
);
```

#### 3.3 Point Out Pattern (3 min)
"Notice the pattern:"
1. Plain HTML → Styled component
2. Semantic name (TaskInput, not Input1)
3. Hover/focus states added
4. Consistent throughout file

"This is what you need to do everywhere!"

---

### Part 4: Student Practice (30 min)

#### 4.1 Individual Work (25 min)

**Assignment:**
"Pick ONE of your inline styles or plain HTML elements. Refactor it RIGHT NOW using the pattern we just showed."

**Options:**
- A button with inline styles → Styled button
- A plain input → Styled input
- A div with inline styles → Semantic component

**You walk around and help!**

**Look for:**
- Correct file structure (.styles.js or .module.css)
- Semantic names
- Proper import/export
- Works correctly

#### 4.2 Quick Shares (5 min)
- 2-3 students show what they did
- Class gives feedback
- You highlight good decisions

---

### Part 5: Week Plan & Wrap-Up (5 min)

#### Work Plan for Rest of Week

**Wednesday evening:**
- [ ] Fix 5 inline styles using today's pattern
- [ ] Push to GitHub

**Thursday (Office hours available):**
- [ ] Fix remaining inline styles
- [ ] Start on plain HTML elements
- [ ] Push progress

**Friday:**
- [ ] Finish all refactoring
- [ ] Test everything still works
- [ ] Write REFACTORING.md

**Saturday:**
- [ ] Final review
- [ ] Submit to GitHub
- [ ] Sleep!

**Office Hours:**
- Thursday: 2-4pm
- Friday: 10am-12pm
- Bring specific code you're stuck on

---

## 🆘 Office Hours (Thursday & Friday)

### Thursday 2-4pm & Friday 10am-12pm

**Format:** Drop-in, first-come-first-served

**Bring:**
- Specific component you're struggling with
- Error messages if stuck
- Questions about patterns

**Common help needed:**
1. "How do I name this component?"
2. "How do I structure my .styles.js file?"
3. "Is this consistent enough?"
4. "How do I handle this complex inline style?"

**Your role:**
- Quick code review
- Naming suggestions
- Pattern clarification
- Encouragement!

---

## 📊 Simplified Grading (100 points)

### Grading Checklist

**Consistency (40 points)**
- [ ] ONE styling approach used throughout (20 pts)
- [ ] No mixing styled-components + inline styles (10 pts)
- [ ] No mixing CSS modules + inline styles (10 pts)

**No Inline Styles (20 points)**
- [ ] Zero `style={{}}` in codebase (search confirms) (20 pts)
- Partial credit: -2 pts per remaining inline style (max -20)

**Semantic Naming (30 points)**
- [ ] Styled components have clear names (15 pts)
- [ ] No generic names (Container, Wrapper alone) (10 pts)
- [ ] Names describe purpose not appearance (5 pts)

**Documentation (10 points)**
- [ ] REFACTORING.md exists (3 pts)
- [ ] Has 3 before/after examples (4 pts)
- [ ] Explains what changed and why (3 pts)

### Quick Grading Process

**15 minutes per student:**
1. Search for `style={{` (should be 0 results) - 2 min
2. Review 3 components for naming - 5 min
3. Check consistency of approach - 3 min
4. Read REFACTORING.md - 5 min

---

## 📝 Simplified Assignment Document

### What Students Need to Do

**Due: Saturday (End of Week)**

#### Step 1: Find & Fix Inline Styles
- Search your codebase for `style={{`
- Convert each one to your styling approach:
  - Styled-components → Create styled component
  - CSS Modules → Create class in .module.css
  - Tailwind → Extract to semantic component
- Push changes

#### Step 2: Fix Plain HTML
- Find plain `<input>`, `<button>`, `<div>` mixed with styled code
- Style them consistently
- Use semantic names
- Push changes

#### Step 3: Improve Names
- Change generic names to semantic:
  - `Container` → `ProfileContainer`
  - `Wrapper` → `ContentSection`
  - `div className="..."` → `<StyledComponent>`
- Push changes

#### Step 4: Document
Create `REFACTORING.md`:
```markdown
# Refactoring Report

## Changes Made

### 1. Eliminated Inline Styles
**Before:**
\`\`\`jsx
<a onClick={...} style={{ color: "#aaa", fontSize: "small" }}>
  remove
</a>
\`\`\`

**After:**
\`\`\`jsx
<RemoveButton onClick={...}>remove</RemoveButton>
\`\`\`

**Why better:** Consistent with styled-components, reusable, themeable

### 2. [Add 2 more examples]

## Lessons Learned
- I learned that consistency matters more than perfection
- Using semantic names makes code immediately readable
- Future me will thank present me for this cleanup
```

---

## 🎯 Success Metrics (Realistic for 1 Week)

### Must Achieve:
- [ ] Zero inline styles (`style={{}}`)
- [ ] Consistent styling approach
- [ ] Basic semantic naming

### Nice to Have:
- [ ] All components well-named
- [ ] Good file organization
- [ ] Comprehensive documentation

### Don't Stress About:
- Perfect component extraction
- Complete design system
- Every possible improvement

**The Goal:**
"Make your code readable by someone who doesn't know your CSS framework."

---

## 💡 Teaching Tips for 1-Week Sprint

### Keep It Simple
- Focus on 3 principles, not 4
- Show pattern, have them repeat
- Don't get into advanced topics

### Be Realistic
- This is "good enough" not "perfect"
- High-impact changes only
- Something is better than nothing

### Encourage Progress
- "You fixed 10 inline styles? Great!"
- "Your naming is much clearer now!"
- "This is already way more readable!"

### Common Student Concerns

**"I don't have time to fix everything!"**
→ "Fix the obvious stuff. That's 80% of the benefit."

**"What if I break something?"**
→ "Test as you go. Small changes, test, commit. Repeat."

**"This feels like busywork."**
→ "This is literally what code reviews check in real jobs. It matters."

**"My code worked before."**
→ "Yes! And now it works AND is readable. That's the goal."

---

## ✅ Instructor Week Checklist

### Before Monday
- [ ] Read CLASS_DISCUSSION_GUIDE
- [ ] Prepare 2-3 anonymized examples
- [ ] Test live coding setup
- [ ] Print CHEATSHEETs (optional)

### Monday Session
- [ ] Teach Session 1 (90 min)
- [ ] Distribute CHEATSHEET + CASE_STUDY
- [ ] Assign Tuesday homework

### Tuesday
- [ ] Monitor Slack for questions
- [ ] Review student audits if shared

### Wednesday Session
- [ ] Teach Session 2 (90 min)
- [ ] Live refactor 2 examples
- [ ] Help students during practice time

### Thursday
- [ ] Office hours 2-4pm
- [ ] Help with specific issues

### Friday
- [ ] Office hours 10am-12pm
- [ ] Last push of encouragement

### Saturday
- [ ] Deadline - students submit
- [ ] No work for you!

### Sunday-Monday
- [ ] Grade submissions (15 min each)
- [ ] Provide brief feedback
- [ ] Prepare for next week

---

## 🎉 Final Thoughts

**This is a 1-week sprint, not a semester.**

**Realistic Goals:**
- ✅ Eliminate obvious problems (inline styles)
- ✅ Introduce semantic naming concept
- ✅ Push for consistency
- ✅ Plant seeds for future improvement

**Not Goals:**
- ❌ Perfect architecture
- ❌ Complete component libraries
- ❌ Design system mastery

**The Win:**
If students leave understanding "consistency and readability matter," you've succeeded.

**Your materials are ready. Just follow this plan. You've got this! 💪**
