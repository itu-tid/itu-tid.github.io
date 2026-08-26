# Lesson Plan: Component Architecture & React Best Practices

**Course Module:** React Component Design & Refactoring
**Duration:** 4 weeks (Sprint 2)
**Target:** Web development students with basic React knowledge
**Prerequisites:** React fundamentals, JSX, props, state

---

## 📋 Module Overview

### Learning Objectives

By the end of this module, students will be able to:
1. **Identify** poor component architecture patterns ("div soup", "class soup")
2. **Apply** the 4 core principles: Tech Lead Test, Semantic Naming, DRY, Single Level of Abstraction
3. **Extract** semantic components from monolithic page files
4. **Organize** component libraries with proper file structure
5. **Use** styled-components (or CSS approach) consistently and semantically
6. **Document** component APIs and refactoring decisions
7. **Review** code with architectural focus, not just functionality

### Assessment

- **Sprint 2 Project:** 120 points (see rubric in SPRINT_2_ASSIGNMENT.md)
- **Class Participation:** 10 points
- **Peer Code Review:** 10 points
- **Total:** 140 points

---

## 📅 Weekly Schedule

| Week | Focus | Sessions | Deliverable |
|------|-------|----------|-------------|
| **Week 1** | Understanding the Problem | 2 sessions | Layout components extracted |
| **Week 2** | Component Extraction | 2 sessions | UI primitives + domain components |
| **Week 3** | Refactoring Practice | 2 sessions | All pages refactored |
| **Week 4** | Documentation & Polish | 1 session + demos | Documentation + presentations |

---

## 📚 Materials Distribution Schedule

### Before Week 1
**Post to LMS:**
- [ ] This LESSON_PLAN.md (instructor guide)
- [ ] SPRINT_2_ASSIGNMENT.md (full assignment)
- [ ] Announcement: "Important Sprint 2 changes - please read assignment before class"

### During Week 1, Session 1
**Distribute:**
- [ ] COMPONENT_EXTRACTION_GUIDE.md
- [ ] COMPONENT_EXTRACTION_CHEATSHEET.md (printable PDF if possible)

### During Week 1, Session 2
**Share:**
- [ ] CASE_STUDY_TODO_APP.md
- [ ] Link to external articles (Semantic JSX, etc.)

### Week 2-4
**As needed:**
- Example component files
- Code review templates
- Individual feedback documents

---

## 🗓️ Detailed Session Plans

---

## Week 1: Understanding the Problem

### Session 1: "What's Wrong with Our Code?" (90 minutes)

**Materials Needed:**
- CLASS_DISCUSSION_GUIDE.md (your script)
- Projector for live coding
- Student Sprint 1 code reviews (anonymized)

#### Part 1: Opening & Context (15 min)

**1.1 Hook with Real Scenario (5 min)**
```
"Imagine you're interviewing for a React position. The interviewer
asks to review your portfolio code. They open your Profile.tsx file
and see 275 lines of divs with classes everywhere. What do you think
happens next?"

[Get student responses]

"Today we're learning why this matters and how to fix it."
```

**1.2 Learning Objectives (5 min)**
- Write on board:
  1. Identify component architecture problems
  2. Learn 4 core principles
  3. Extract semantic components
  4. Apply to your Sprint 1 code

**1.3 Sprint 2 Overview (5 min)**
- Briefly overview SPRINT_2_ASSIGNMENT.md
- Timeline: 4 weeks
- Deliverables: Refactored code + documentation
- "This is not busy work - this is how professionals code"

#### Part 2: The Problem (25 min)

**Follow CLASS_DISCUSSION_GUIDE.md sections:**
- Show "The Yikes Example" from open source
- Tell the Netlify 71-class checkbox story
- Present the Technical Lead scenario
- Debate: "Is this feedback fair?"

**Key Message:**
> "You're not writing code for the computer. You're writing it for the next developer."

**Activity (10 min):**
- Show anonymized examples from Sprint 1 reviews
- Ask: "Can you tell what this page does without running it?"
- Most will say no - that's the problem!

#### Part 3: The 4 Principles (30 min)

**3.1 Introduce Principles (10 min)**
Write on board with examples:

```
1. Tech Lead Test
   Can non-CSS person understand structure?
   ❌ <div className="mx-auto flex...">
   ✅ <ProfileContainer>

2. Semantic Naming Test
   Can you name it in 1-2 words?
   ❌ Container, Wrapper, Div
   ✅ ProfileHeader, JobCard

3. DRY Test
   Repeated 3+ times?
   ❌ Copy-paste same classes
   ✅ Extract component

4. Single Level of Abstraction
   Don't mix high/low levels
   ❌ <Header /> + <div className="...">
   ✅ <Header /> + <ProfileContent />
```

**3.2 Check Current Code (10 min)**
- "Take 5 minutes: Open your Sprint 1 code"
- "Apply each test to one of your pages"
- "How many tests does it fail?"
- Share results (show of hands)

**3.3 Before/After Preview (10 min)**
- Show the 275-line vs 68-line example from guide
- Point out clear hierarchy in refactored version
- "This is our goal for Sprint 2"

#### Part 4: Getting Started (20 min)

**4.1 Distribute Materials**
- COMPONENT_EXTRACTION_GUIDE.md
- COMPONENT_EXTRACTION_CHEATSHEET.md

**4.2 Reading Assignment**
"Before next class (Wednesday):"
- [ ] Read COMPONENT_EXTRACTION_GUIDE sections 1-3
- [ ] Read CHEATSHEET completely
- [ ] Identify 3 issues in your Sprint 1 code
- [ ] Bring questions to next class

**4.3 First Steps Assignment**
"Due Sunday (Week 1):"
- [ ] Extract ONE layout component (container)
- [ ] Use it in at least one page
- [ ] Push to GitHub
- [ ] Short write-up: What you extracted and why

#### Part 5: Q&A (Remaining time)

Common questions to address:
- "What if I use CSS Modules instead of Tailwind?"
  → Principles apply to all approaches
- "How small should components be?"
  → No hard rule, but < 150 lines
- "What about performance?"
  → Components are just functions, no overhead

**Homework Checklist:**
- [ ] Read COMPONENT_EXTRACTION_GUIDE sections 1-3
- [ ] Read CHEATSHEET
- [ ] Identify 3 issues in your code
- [ ] Extract ONE layout component
- [ ] Push to GitHub by Sunday

---

### Session 2: "Component Extraction Workshop" (90 minutes)

**Materials Needed:**
- CASE_STUDY_TODO_APP.md
- Live coding setup
- Student code examples (anonymized)

#### Part 1: Review & Questions (15 min)

**1.1 Homework Review (10 min)**
- "Who extracted a layout component?"
- Show 2-3 student examples
- Quick feedback on naming, structure

**1.2 Address Reading Questions (5 min)**
- Common confusions from guide
- Clarify any principles

#### Part 2: Case Study Analysis (30 min)

**Follow CASE_STUDY_TODO_APP.md:**

**2.1 Show What's Working (10 min)**
- LoginPage example with semantic components
- "This is the pattern we want"
- Point out: AuthContainer, Title, Form, Input, Button

**2.2 Show What Needs Work (20 min)**
Present 3 issues from case study:
1. **Inline styles mixed with styled-components** (Issue 1)
   - Show the problem
   - Show the solution
   - Discuss: Why is consistency important?

2. **Plain HTML elements** (Issue 4)
   - Plain `<input>` and `<button>`
   - Refactored to `<TaskInput>` and `<AddButton>`
   - Discuss: Semantic naming benefits

3. **Complex inline JSX** (Issue 5)
   - 20 lines of item markup
   - Extract to `<TodoListItem>` component
   - Discuss: Single Responsibility Principle

**Key Takeaway:**
"Even when using styled-components, you can still have architecture problems. Consistency is everything."

#### Part 3: Live Coding Demo (35 min)

**Choose one of these based on student needs:**

**Option A: Button Component (Simple)**
Good for students struggling with basics
- Show repeated button pattern
- Extract with variants
- Add props interface
- Demo usage

**Option B: Card Component (Medium)**
Good for average class
- Show repeated card layout
- Extract with composition
- Add polymorphic 'as' prop
- Demo in multiple contexts

**Option C: List Component (Advanced)**
Good for advanced students
- Show repeated list pattern
- Extract with render props
- Add TypeScript generics
- Demo with different item types

**Live Coding Steps (any option):**
1. Identify the pattern (5 min)
2. Name the component (2 min)
3. Create component file (3 min)
4. Create styles file (10 min)
5. Refactor usage (10 min)
6. Test and review (5 min)

**Encourage questions throughout!**

#### Part 4: Team Exercise (25 min)

**4.1 Form Teams (2 min)**
- Groups of 2-3 students
- Mixed skill levels if possible

**4.2 Exercise Instructions (3 min)**
"Choose ONE component from your Sprint 1 code:"
- Something repeated 3+ times
- OR something with unclear purpose
- OR something with mixed styling approaches

**4.3 Team Work (15 min)**
Each team should:
1. Identify the problem (2 min)
2. Name the component (2 min)
3. Sketch the refactoring (5 min)
4. Prepare to present (6 min)

**Walk around and help teams!**

**4.4 Quick Presentations (5 min)**
- 2-3 teams present (1-2 min each)
- Class feedback
- You provide guidance

#### Part 5: Week 1 Deliverable & Next Steps (Remaining)

**Due by End of Week 1 (Sunday):**
- [ ] Extract 3 layout components
  - Page container
  - Section container
  - Header/footer wrapper
- [ ] Use them in at least 2 pages
- [ ] Push to GitHub
- [ ] Document in REFACTORING.md (start file)

**Reading for Week 2:**
- [ ] COMPONENT_EXTRACTION_GUIDE sections 4-6
- [ ] Review CASE_STUDY Issues 2, 3, 6
- [ ] Optional: Semantic JSX article

**Office Hours:**
- Tuesday 2-4pm
- Thursday 10am-12pm
- Bring specific components you're stuck on

---

## Week 2: Component Extraction Practice

### Session 3: "UI Primitives & Design Systems" (90 minutes)

**Materials Needed:**
- Examples of design systems (show Airbnb, Shopify, Material-UI)
- Component template files
- Students' Week 1 submissions

#### Part 1: Week 1 Feedback (15 min)

**1.1 Show Good Examples (10 min)**
- Display 3-4 excellent layout components from students
- Highlight what makes them good:
  - Clear semantic names
  - Appropriate abstraction level
  - Reusability
  - Clean code

**1.2 Common Issues (5 min)**
Address patterns you saw:
- Generic names (Container1, Wrapper)
- Over-abstraction (too many props)
- Under-abstraction (not reusable)

#### Part 2: Design System Thinking (20 min)

**2.1 What is a Design System? (10 min)**
- Show examples: Material-UI, Chakra UI, Ant Design
- Components organized by purpose
- Consistent props interfaces
- Theme integration

**2.2 UI Primitives vs Domain Components (10 min)**

Draw on board:
```
Component Hierarchy

UI Primitives (Reusable everywhere)
├── Button (variants: primary, secondary, danger)
├── Input (variants: text, email, password)
├── Avatar (sizes: small, medium, large)
├── Card
└── Badge

Domain Components (Business-specific)
├── ProfileHeader
├── JobCard
├── ExperienceEntry
└── FeedbackList

Layout Components (Structure)
├── PageContainer
├── ContentSection
└── Grid
```

**Discussion:**
"What UI primitives do YOU need in your app?"

#### Part 3: Building a Button Component (30 min)

**Live coding: Creating a reusable Button**

**3.1 Identify Requirements (5 min)**
- Survey student codebases: "How many buttons do you have?"
- "What variations? Colors? Sizes? States?"
- List on board:
  - Variants: primary, secondary, danger
  - Sizes: small, medium, large
  - States: default, hover, disabled, loading

**3.2 Create Component (20 min)**

**Step-by-step live code:**

```tsx
// Button.tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  children: ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  loading?: boolean;
}

export const Button = ({
  variant = 'primary',
  size = 'medium',
  children,
  onClick,
  disabled = false,
  loading = false
}: ButtonProps) => {
  return (
    <StyledButton
      variant={variant}
      size={size}
      onClick={onClick}
      disabled={disabled || loading}
    >
      {loading ? 'Loading...' : children}
    </StyledButton>
  );
};
```

```tsx
// Button.styles.ts (for styled-components)
export const StyledButton = styled.button<ButtonProps>`
  padding: ${props => {
    const sizes = {
      small: '0.5rem 1rem',
      medium: '0.75rem 1.5rem',
      large: '1rem 2rem'
    };
    return sizes[props.size];
  }};

  background: ${props => {
    const variants = {
      primary: props.theme.colors.primary,
      secondary: props.theme.colors.secondary,
      danger: props.theme.colors.danger
    };
    return variants[props.variant];
  }};

  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s;

  &:hover:not(:disabled) {
    opacity: 0.9;
    transform: translateY(-1px);
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`;
```

**3.3 Usage Examples (5 min)**
```tsx
// Show how clean the usage becomes
<Button variant="primary" onClick={handleApply}>Apply Now</Button>
<Button variant="secondary" size="small">Cancel</Button>
<Button variant="danger" loading={isDeleting}>Delete</Button>
```

#### Part 4: Student Practice (20 min)

**4.1 Individual Exercise (15 min)**
"Create ONE UI primitive from your app:"
- Choose: Avatar, Card, Input, Badge, or another common element
- Create component file
- Create styles file
- Add TypeScript props
- Test with different variations

**Walk around and help!**

**4.2 Pair Share (5 min)**
- Find a partner
- Show your component
- Explain: What variations did you support?
- Get feedback

#### Part 5: Week 2 Goals (Remaining)

**Due by Mid-Week 2 (Wednesday):**
- [ ] Create 5 UI primitive components:
  - Button (required)
  - Input (required)
  - Avatar or Card (required)
  - 2 others from your app
- [ ] Organize in `components/ui/` folder
- [ ] Document each in COMPONENTS.md
- [ ] Use in at least 2 pages each

**Checkpoint Review:**
- Wednesday: I'll review your UI components
- Provide feedback before you build domain components
- Fix any issues early

---

### Session 4: "Domain Components & Composition" (90 minutes)

**Materials Needed:**
- Student UI components from Wednesday checkpoint
- Examples of good composition patterns
- Refactoring exercises

#### Part 1: UI Components Review (15 min)

**1.1 Showcase (10 min)**
- Show 3-4 excellent UI components
- Highlight:
  - Good prop interfaces
  - Variants support
  - TypeScript usage
  - Documentation

**1.2 Quick Fixes (5 min)**
- Common issues you saw
- How to improve for next iteration

#### Part 2: Domain Components Concept (20 min)

**2.1 UI vs Domain Components (10 min)**

```
UI Components (Generic)
- Can be used in ANY app
- No business logic
- Pure presentation
Examples: Button, Input, Card, Avatar

Domain Components (Business-Specific)
- Specific to YOUR app
- May contain business logic
- Compose UI components
Examples: ProfileHeader, JobCard, CheckoutForm
```

**2.2 Composition Pattern (10 min)**

Show hierarchy:
```tsx
// Domain component USES UI components
<ProfileHeader>
  <Avatar user={user} />          {/* UI component */}
  <UserName>{user.name}</UserName> {/* UI component */}
  <Button variant="primary">      {/* UI component */}
    Edit Profile
  </Button>
</ProfileHeader>
```

**Key Principle:**
"Domain components are the glue between UI primitives and your business logic."

#### Part 3: Building ProfileHeader (25 min)

**Live coding: Domain component example**

**3.1 Analyze Requirements (5 min)**
- What goes in a profile header?
- What data does it need?
- What actions are available?
- Draw on board

**3.2 Build Component (15 min)**

```tsx
// ProfileHeader.tsx
import { Avatar } from '@/components/ui/Avatar';
import { Button } from '@/components/ui/Button';
import { StarRating } from '@/components/ui/StarRating';
import * as S from './ProfileHeader.styles';

interface ProfileHeaderProps {
  user: UserProfile;
  onEdit?: () => void;
  onMessage?: () => void;
}

export const ProfileHeader = ({
  user,
  onEdit,
  onMessage
}: ProfileHeaderProps) => {
  return (
    <S.Header>
      <S.AvatarSection>
        <Avatar src={user.avatarUrl} alt={user.name} size="large" />
      </S.AvatarSection>

      <S.InfoSection>
        <S.UserName>{user.name}</S.UserName>
        <StarRating rating={user.rating} />
        <S.Metadata>
          <S.Role>{user.role}</S.Role>
          <S.JoinDate>Joined {formatDate(user.joinedDate)}</S.JoinDate>
        </S.Metadata>
      </S.InfoSection>

      <S.Actions>
        {onEdit && (
          <Button variant="secondary" onClick={onEdit}>
            Edit
          </Button>
        )}
        {onMessage && (
          <Button variant="primary" onClick={onMessage}>
            Message
          </Button>
        )}
      </S.Actions>
    </S.Header>
  );
};
```

**3.3 Show Usage (5 min)**
```tsx
// Clean page component!
<ProfileContainer>
  <ProfileHeader
    user={user}
    onEdit={handleEdit}
    onMessage={handleMessage}
  />
  <ProfileContent>
    {/* ... */}
  </ProfileContent>
</ProfileContainer>
```

**Point out:**
- Semantic structure
- Composition of UI components
- Props interface clearly documents behavior
- Optional actions (onEdit, onMessage)

#### Part 4: Refactoring Exercise (25 min)

**4.1 Choose Example (5 min)**
Pick a problematic component from student code (anonymized)
- Show the "before" - complex, unclear structure
- Discuss: What's wrong? What would you name these parts?

**4.2 Group Refactoring (15 min)**
- Break into teams
- Each team refactors the same component
- Different approaches OK!

**4.3 Compare Solutions (5 min)**
- Show 2-3 team solutions
- Discuss trade-offs
- There's often no "one right answer"

#### Part 5: Week 2 Deliverables (Remaining)

**Due by End of Week 2 (Sunday):**
- [ ] Create 5-8 domain components specific to your app
  - Example: ProfileHeader, JobCard, ExperienceEntry, etc.
  - Use UI components inside them
  - Add TypeScript interfaces
- [ ] Refactor at least 3 pages to use new components
- [ ] Update COMPONENTS.md documentation
- [ ] Push to GitHub

**Reading for Week 3:**
- [ ] Review entire COMPONENT_EXTRACTION_GUIDE
- [ ] Read CASE_STUDY issues 4 and 5
- [ ] Review your Sprint 1 code with fresh eyes

**Checkpoint:**
- I'll review progress mid-week 3
- Should see significant line reduction in pages
- Pages should be mostly composition, minimal logic

---

## Week 3: Refactoring & Polish

### Session 5: "Page Refactoring Workshop" (90 minutes)

**Materials Needed:**
- Students' Week 2 components
- Refactoring checklist
- Before/after metrics template

#### Part 1: Progress Check (15 min)

**1.1 Metrics Review (10 min)**
"Let's see your progress:"
- "Open your main page file (Profile, Jobs, etc.)"
- "How many lines NOW vs Sprint 1?"
- Share results - celebrate improvements!

**Target metrics:**
- Sprint 1: 200-300 lines
- Now: 60-100 lines
- Reduction: 50-70%

**1.2 Common Struggles (5 min)**
- What's been hard?
- Where are you stuck?
- Address quick questions

#### Part 2: Single Level of Abstraction (20 min)

**2.1 The SLA Principle (10 min)**

Bad example:
```tsx
<ProfilePage>
  <Header />                                    {/* High level */}
  <div className="flex gap-4">                  {/* Low level */}
    <div className="w-1/3 bg-gray-100 p-4">   {/* Low level */}
      <p className="font-bold">Name</p>         {/* Low level */}
      <p>{user.name}</p>
    </div>
  </div>
  <Footer />                                    {/* High level */}
</ProfilePage>
```

Good example:
```tsx
<ProfilePage>
  <Header />
  <ProfileContent>
    <ProfileSection title="Name" value={user.name} />
    <ProfileSection title="Email" value={user.email} />
  </ProfileContent>
  <Footer />
</ProfilePage>
```

**Question:** "Can you read the structure without knowing CSS?"

**2.2 Student Code Review (10 min)**
- Show 2 anonymized student examples
- One with mixed levels
- One with consistent level
- Class discusses which is clearer

#### Part 3: Live Refactoring (30 min)

**Choose a complex page from student code (with permission):**

**3.1 Audit Current State (5 min)**
- How many lines?
- How many divs/spans?
- How many inline styles?
- What's the structure?

**3.2 Identify Sections (5 min)**
- Draw boxes around logical groups
- Name each section
- List what components we need

**3.3 Refactor Live (15 min)**
- Create missing components
- Replace sections with semantic names
- Show before/after line count
- Demonstrate improved readability

**3.4 Measure Results (5 min)**
```
Before:
- 285 lines
- 43 divs
- 12 inline styles
- Structure unclear

After:
- 72 lines
- 0 divs (all semantic components)
- 0 inline styles
- Structure crystal clear

Improvement: 75% reduction
```

#### Part 4: Student Refactoring Sprint (20 min)

**4.1 Pick Your Worst Page (2 min)**
"Open your most complex page file"
"The one you're embarrassed to show"
"We're fixing it TODAY"

**4.2 Individual Work (15 min)**
Students refactor with your help:
1. Identify sections (3 min)
2. Create/extract components (10 min)
3. Measure improvement (2 min)

**Walk around - hands-on help!**

**4.3 Share Victories (3 min)**
- "Who reduced their page by 50%+?"
- Quick show & tell
- Celebrate!

#### Part 5: Week 3 Goals (Remaining)

**Due by End of Week 3 (Sunday):**
- [ ] ALL pages refactored (< 100 lines each)
- [ ] NO inline styles anywhere
- [ ] Consistent abstraction levels
- [ ] Complete COMPONENTS.md
- [ ] Complete REFACTORING.md with metrics
- [ ] All code pushed to GitHub

**Final checklist to run:**
- [ ] Run ESLint - no errors
- [ ] Run TypeScript check - no errors
- [ ] Test all functionality - nothing broken
- [ ] Check git status - everything committed

---

### Session 6: "Documentation & Code Review" (90 minutes)

**Materials Needed:**
- Documentation templates
- Code review checklist
- Peer review assignments

#### Part 1: Documentation Workshop (30 min)

**1.1 Why Document? (5 min)**
- Future you will forget
- Team members need guidance
- Portfolio reviewers want context

**1.2 COMPONENTS.md Template (15 min)**

Show good example:
```markdown
# Component Library

## UI Components

### Button
**Purpose:** Reusable button with variants
**File:** `components/ui/Button.tsx`
**Props:**
- `variant`: 'primary' | 'secondary' | 'danger'
- `size`: 'small' | 'medium' | 'large'
- `onClick`: Click handler
- `disabled`: Disable button

**Usage:**
\`\`\`tsx
<Button variant="primary" onClick={handleSubmit}>
  Submit
</Button>
\`\`\`
```

**1.3 Student Practice (10 min)**
- Document 2 of your components
- Use the template
- Include usage examples

#### Part 2: REFACTORING.md (20 min)

**2.1 What to Include (5 min)**
- Before/after metrics
- What changed and why
- Challenges faced
- Lessons learned

**2.2 Template & Example (10 min)**
```markdown
# Refactoring Report

## Metrics

### Profile.tsx
- **Before:** 275 lines
- **After:** 68 lines
- **Reduction:** 75%

### Components Created
- Layout: 3 components
- UI: 6 components
- Domain: 8 components

## Major Changes

### 1. Extracted Layout Components
Created `ProfileContainer` to replace repeated layout pattern...

### 2. Created Button System
Identified 23 buttons across the app...

## Challenges

The hardest part was...

## Lessons Learned

I now understand that...
```

**2.3 Student Work (5 min)**
- Start your REFACTORING.md
- Fill in metrics
- Outline major changes

#### Part 3: Peer Code Review (35 min)

**3.1 Assign Partners (5 min)**
- Pair students up
- Exchange GitHub repo links
- Clone partner's code

**3.2 Code Review Checklist (5 min)**

Distribute checklist:
```
Peer Review Checklist

Component Abstraction:
- [ ] Pages < 100 lines
- [ ] Components < 150 lines
- [ ] Clear semantic names
- [ ] Proper file organization

Consistency:
- [ ] No inline styles (style={{}})
- [ ] Consistent CSS approach
- [ ] All styling in designated files
- [ ] Proper TypeScript types

Abstraction Level:
- [ ] Single level per page
- [ ] No mixing high/low components
- [ ] Clear component hierarchy

Documentation:
- [ ] COMPONENTS.md present
- [ ] REFACTORING.md with metrics
- [ ] Component usage examples

Code Quality:
- [ ] No console errors
- [ ] No ESLint warnings
- [ ] Functionality works
- [ ] Git history clean
```

**3.3 Review Time (20 min)**
- Students review partner's code
- Fill out checklist
- Write 3 positives, 2 improvements
- Be constructive!

**3.4 Share Feedback (5 min)**
- Partners share findings
- Discuss improvements
- Thank each other

#### Part 4: Final Week Prep (Remaining)

**Week 4 Schedule:**
- **Monday:** Office hours for final questions
- **Wednesday:** Final submission deadline
- **Friday:** Presentations (5 min each)

**Final Submission Requirements:**
- [ ] All code pushed to GitHub
- [ ] COMPONENTS.md complete
- [ ] REFACTORING.md complete
- [ ] README updated
- [ ] Demo prepared (5 min)

**Presentation Structure (5 min):**
1. Show before code (1 min)
2. Show after code (1 min)
3. Metrics & improvements (2 min)
4. Key lesson learned (1 min)

**Extra Credit Opportunities:**
- Storybook setup (+10 pts)
- Component tests (+10 pts)
- Design system docs (+5 pts)
- Accessibility audit (+5 pts)

---

## Week 4: Presentations & Wrap-up

### Session 7: "Sprint 2 Demos" (90 minutes)

**Materials Needed:**
- Projector for presentations
- Grading rubric
- Feedback forms

#### Structure

**Format:** 5 minutes per team
- 3 min presentation
- 2 min Q&A from class

**Order:** Alphabetical or volunteer basis

**Your Role:**
- Take notes for grading
- Ask clarifying questions
- Highlight exceptional work
- Provide constructive feedback

**After Each Demo:**
- Class gives one positive comment
- You provide one improvement suggestion
- Next team prepares

#### Celebration
- Acknowledge most improved
- Best component design
- Best documentation
- Most creative solution

---

## 📊 Grading & Assessment

### Sprint 2 Grading (120 points)

Use rubric from SPRINT_2_ASSIGNMENT.md:

| Category | Points | Quick Check |
|----------|--------|-------------|
| Component Extraction | 40 | Layout + UI + Domain |
| Semantic Naming | 15 | Clear, purposeful names |
| File Organization | 10 | Proper structure, sizes |
| TypeScript Props | 10 | Interfaces, no any |
| Abstraction Level | 10 | Consistent hierarchy |
| Documentation | 10 | COMPONENTS.md complete |
| Code Quality | 5 | No errors |
| Refactoring Analysis | 10 | REFACTORING.md |
| Presentation | 10 | Clear, prepared |

### Participation (10 points)
- Attended all sessions: 6 pts
- Engaged in discussions: 2 pts
- Helped peers: 2 pts

### Peer Review (10 points)
- Completed review: 5 pts
- Constructive feedback: 5 pts

---

## 🆘 Support Structure

### Office Hours

**Weekly Schedule:**
- **Tuesday:** 2-4pm (in-person)
- **Thursday:** 10am-12pm (zoom)

**What to Bring:**
- Specific component you're stuck on
- Error messages
- Questions about principles

**Book via:** [Calendar link or Slack]

### Slack Channels

Create these channels:
- `#sprint-2-help` - General questions
- `#component-examples` - Share good examples
- `#pair-programming` - Find coding buddies

**Response time:** 24 hours max

### TA Support

If you have TAs:
- **TA Pairing Sessions:** 30 min slots
- **Code Review Help:** Async via GitHub comments
- **Office Hours:** Additional weekly slots

---

## 📈 Success Metrics

### Individual Student Success

Student is successful if they:
- [ ] Reduce page files by 50%+
- [ ] Create 10+ reusable components
- [ ] No inline styles remaining
- [ ] Clear component documentation
- [ ] Can articulate the 4 principles

### Class Success

Module is successful if:
- [ ] 80%+ students pass (85+/100)
- [ ] Average metrics show 50%+ code reduction
- [ ] Students can peer review architecture
- [ ] Positive feedback on post-module survey
- [ ] Code quality improves in Sprint 3

---

## 🔄 Iteration & Improvement

### After Module Completion

**Collect Feedback:**
- [ ] Student survey
- [ ] What worked well?
- [ ] What was confusing?
- [ ] What should change?

**Review Results:**
- [ ] Analyze grade distribution
- [ ] Identify common struggles
- [ ] Note questions that came up repeatedly
- [ ] Check time allocation (was it enough?)

**Update Materials:**
- [ ] Improve unclear sections
- [ ] Add more examples where needed
- [ ] Adjust timeline if needed
- [ ] Update this lesson plan

---

## 📝 Quick Reference: Weekly Checklist

### Week 1
- [ ] Session 1: Introduction & principles
- [ ] Session 2: Case study & demo
- [ ] Distribute: Guide + Cheatsheet
- [ ] Monitor: Layout components submission

### Week 2
- [ ] Session 3: UI primitives
- [ ] Session 4: Domain components
- [ ] Checkpoint: Review UI components
- [ ] Monitor: Component progress

### Week 3
- [ ] Session 5: Page refactoring
- [ ] Session 6: Documentation & peer review
- [ ] Monitor: All pages refactored
- [ ] Reminder: Final submission due

### Week 4
- [ ] Office hours for questions
- [ ] Final submission deadline
- [ ] Session 7: Presentations
- [ ] Grading & feedback

---

## 💡 Teaching Tips

### If Students Struggle With...

**Component naming:**
- Use the "1-2 word test"
- Ask "What does this DO?"
- Avoid appearance-based names

**Knowing when to extract:**
- Use the DRY test (3+ times)
- Use the line count test (> 150 lines)
- Use the "can you name it" test

**Styling consistency:**
- Show the pattern once, enforce everywhere
- Code review catches issues
- Peer pressure helps compliance

**Understanding SLA:**
- Draw hierarchy diagrams
- Use real examples from their code
- Compare to building floors (don't mix basement with penthouse)

### If You're Running Behind...

**Compress Week 2:**
- Combine sessions 3 & 4
- Do faster demos
- More homework, less in-class

**Extend Timeline:**
- Add extra week if possible
- Move presentations to Week 5
- More office hours

**Prioritize Core Content:**
- Must cover: 4 principles, extraction, naming
- Can skip: Advanced patterns, extra exercises
- Focus on getting basic refactoring done

### If Students Excel...

**Advanced Topics:**
- Compound components pattern
- Render props
- Custom hooks extraction
- Design tokens
- Component testing
- Storybook setup

**Extra Challenges:**
- Build a component library
- Create design system docs
- Performance optimization
- Accessibility audit

---

## 📚 Instructor Preparation Checklist

### Before Week 1
- [ ] Read all 5 teaching documents
- [ ] Review Sprint 1 student code
- [ ] Prepare anonymized examples
- [ ] Set up office hours calendar
- [ ] Create Slack channels
- [ ] Test all live coding examples

### Before Each Session
- [ ] Review session plan
- [ ] Prepare live coding environment
- [ ] Queue up examples
- [ ] Test projector/screen sharing
- [ ] Have backup plans ready

### During Module
- [ ] Monitor student progress
- [ ] Respond to Slack within 24h
- [ ] Review checkpoint submissions
- [ ] Adjust pace as needed
- [ ] Collect questions for FAQ

### After Module
- [ ] Grade all submissions
- [ ] Provide individual feedback
- [ ] Collect module feedback
- [ ] Update materials
- [ ] Document lessons learned

---

## 🎯 Learning Outcomes Alignment

This module teaches:

**Technical Skills:**
- Component architecture
- Semantic HTML/JSX
- styled-components best practices
- TypeScript interfaces
- File organization

**Soft Skills:**
- Code review
- Technical writing (documentation)
- Peer feedback
- Refactoring existing code
- Presenting technical work

**Professional Skills:**
- Industry standards
- Maintainable code practices
- Team collaboration
- Portfolio quality code

---

## ✅ Final Thoughts

**Remember:**
- This is tough love - students may be defensive initially
- Frame as career preparation, not criticism
- Celebrate progress, no matter how small
- The patterns will click at different times for different students
- Office hours are crucial - make time available
- This is a foundational skill they'll use forever

**Your goal:**
Teach students to write code that **humans can read and maintain**, not just code that runs.

---

**Good luck! You've got comprehensive materials and a clear plan. You've got this! 🎉**
