# Sprint 2 Assignment: Component Architecture Refactoring

## 🎯 Objective

Refactor your Sprint 1 codebase to use **semantic component architecture** that is readable, maintainable, and follows React best practices.

**This assignment applies to ALL teams** regardless of CSS approach (Tailwind, CSS Modules, styled-components, vanilla CSS).

---

## 📋 Background: The Problem

### Review Feedback Summary

Your Sprint 1 code review identified a critical architectural issue:

**❌ Lack of Semantic Component Abstraction**

This means:
- Code structure is hard to understand without deep CSS knowledge
- Components are not reusable
- Pages mix high-level and low-level abstractions
- File lengths are excessive (200+ lines)
- Code is difficult to review and maintain

### Example of the Problem

**Your code probably looks like this:**
```tsx
// ❌ What is this div? What does this page do?
<div className="mx-auto flex w-full max-w-xl flex-col items-start gap-6 px-4 py-6">
  <section className="flex w-full flex-col items-center gap-2 p-6">
    <div className="size-24 rounded-3xl bg-neutral-300">
      <img src={user.avatar} />
    </div>
    <h2 className="text-2xl font-bold">{user.name}</h2>
    {/* 200 more lines... */}
  </section>
</div>
```

**It should look like this:**
```tsx
// ✅ Clear, semantic, reviewable
<ProfileContainer>
  <ProfileHeader>
    <Avatar user={user} />
    <UserName>{user.name}</UserName>
  </ProfileHeader>
  <ProfileSections user={user} />
</ProfileContainer>
```

---

## 📚 Required Reading

**Before starting:**
1. Read [COMPONENT_EXTRACTION_GUIDE.md](./COMPONENT_EXTRACTION_GUIDE.md) (30 min)
2. Read [COMPONENT_EXTRACTION_CHEATSHEET.md](./COMPONENT_EXTRACTION_CHEATSHEET.md) (10 min)
3. Review [Semantic JSX Article](https://mxb.dev/blog/semantic-jsx/) (15 min)

**Total prep time:** ~1 hour

---

## 🎯 Requirements

### 1. Component Extraction (40 points)

You must extract components from your existing pages:

#### A. Layout Components (10 points)
Create reusable layout containers:
- Page-level containers
- Section containers
- Content wrappers

**Example:**
```tsx
// components/layout/ProfileContainer.tsx
// components/layout/PageContainer.tsx
// components/layout/ContentSection.tsx
```

#### B. UI Primitives (15 points)
Extract reusable UI elements:
- Buttons (with variants)
- Avatars
- Cards
- Icons with consistent styling
- Form inputs
- Any repeated UI patterns (3+ occurrences)

**Example:**
```tsx
// components/ui/Button.tsx
// components/ui/Avatar.tsx
// components/ui/Card.tsx
```

#### C. Domain Components (15 points)
Extract domain-specific components:
- Page headers
- List items
- Sections with specific business logic
- Any component specific to your app domain

**Example:**
```tsx
// components/profile/ProfileHeader.tsx
// components/profile/ExperienceEntry.tsx
// components/jobs/JobCard.tsx
```

---

### 2. Semantic Naming (15 points)

All components must have **clear semantic names**:

✅ **Good names:**
- `ProfileHeader`
- `JobCard`
- `ExperienceList`
- `PrimaryButton`
- `UserAvatar`

❌ **Bad names:**
- `Component1`
- `Container` (too generic)
- `BlueButton` (describes appearance, not purpose)
- `Div`
- `Section1`

**Grading criteria:**
- Component names communicate intent (not implementation)
- Consistent naming convention
- Appropriate specificity (not too generic, not too specific)

---

### 3. File Organization (10 points)

Create proper folder structure:

```
src/
├── components/
│   ├── layout/              # Generic layout components
│   │   ├── ProfileContainer.tsx
│   │   ├── PageContainer.tsx
│   │   └── ContentSection.tsx
│   │
│   ├── ui/                  # Reusable UI primitives
│   │   ├── Button.tsx
│   │   ├── Avatar.tsx
│   │   ├── Card.tsx
│   │   └── StarRating.tsx
│   │
│   └── [your-domain]/       # Domain-specific components
│       ├── ProfileHeader.tsx
│       ├── JobCard.tsx
│       └── ExperienceEntry.tsx
│
└── pages/
    ├── Profile.tsx          # Should be < 100 lines
    ├── JobPage.tsx
    └── ...
```

**Grading criteria:**
- Logical folder structure
- No component > 150 lines
- Page files < 100 lines (after refactoring)
- Clear separation: layout / ui / domain

---

### 4. TypeScript Props (10 points)

All components must have proper TypeScript interfaces:

```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  children: ReactNode;
  onClick?: () => void;
  disabled?: boolean;
}

export const Button = ({
  variant = 'primary',
  size = 'medium',
  children,
  onClick,
  disabled = false
}: ButtonProps) => {
  // Implementation
};
```

**Grading criteria:**
- All props typed with interfaces
- Appropriate use of optional props
- Default values provided
- No `any` types

---

### 5. Single Level of Abstraction (10 points)

Your page components must maintain **consistent abstraction levels**:

❌ **Bad (mixed levels):**
```tsx
<ProfilePage>
  <Header />                                    {/* High-level */}
  <div className="flex gap-4">                  {/* Low-level */}
    <div className="w-1/3 bg-gray-100 p-4">   {/* Low-level */}
      <p>{user.name}</p>
    </div>
  </div>
  <Footer />                                    {/* High-level */}
</ProfilePage>
```

✅ **Good (consistent level):**
```tsx
<ProfilePage>
  <Header />
  <ProfileContent>
    <ProfileSection title="About" content={user.about} />
    <ProfileSection title="Skills" content={user.skills} />
  </ProfileContent>
  <Footer />
</ProfilePage>
```

**Grading criteria:**
- All JSX at same conceptual level
- No mixing of component names and raw HTML with styling
- Clear component hierarchy (3-4 levels max)

---

### 6. Documentation (10 points)

Create a `COMPONENTS.md` file documenting your components:

```markdown
# Component Library

## Layout Components

### ProfileContainer
**Purpose:** Main container for profile pages
**Props:** `children`
**Usage:**
\`\`\`tsx
<ProfileContainer>
  <ProfileHeader />
</ProfileContainer>
\`\`\`

## UI Components

### Button
**Purpose:** Reusable button with variants
**Props:**
- `variant`: 'primary' | 'secondary' | 'danger'
- `size`: 'small' | 'medium' | 'large'
- `onClick`: Click handler
**Usage:**
\`\`\`tsx
<Button variant="primary" onClick={handleClick}>
  Click me
</Button>
\`\`\`
```

---

### 7. Code Quality (5 points)

- No console warnings
- No ESLint errors
- Consistent code formatting
- Removed unused imports/variables
- Proper naming conventions throughout

---

## 🚫 Common Mistakes to Avoid

| Mistake | Penalty | Fix |
|---------|---------|-----|
| Component > 150 lines | -5 pts | Break into smaller components |
| Page file > 100 lines | -5 pts | Extract more components |
| Generic names (`Container`, `Component1`) | -3 pts each | Use semantic names |
| No TypeScript props | -10 pts | Add proper interfaces |
| Mixed abstraction levels | -5 pts | Maintain consistent level |
| No folder structure | -10 pts | Organize properly |
| Missing documentation | -10 pts | Create COMPONENTS.md |

---

## 📝 Deliverables

### 1. Refactored Code (70 points)
All requirements above implemented in your repository.

### 2. Documentation (10 points)
- `COMPONENTS.md` with all component documentation
- Updated README with new architecture

### 3. Before/After Comparison (10 points)
Create `REFACTORING.md` with:
- Before: Screenshot or snippet of old code (1-2 examples)
- After: Screenshot or snippet of refactored code
- Metrics: Lines of code before/after for each page
- Explanation: What changed and why it's better

**Example metrics:**
```markdown
## Refactoring Metrics

### Profile.tsx
- **Before:** 275 lines
- **After:** 68 lines
- **Reduction:** 75%

### Components Created
- Layout: 3 components
- UI: 6 components
- Domain: 8 components
- Total: 17 components
```

### 4. Demo (10 points)
- 5-minute presentation in class
- Show before/after code side-by-side
- Explain your component hierarchy
- Demonstrate one extracted component

---

## 📅 Timeline

| Milestone | Due Date | Deliverable |
|-----------|----------|-------------|
| **Week 1** | [Date] | File structure + layout components |
| **Week 2** | [Date] | UI primitives + domain components |
| **Week 3** | [Date] | Refactor pages + documentation |
| **Sprint 2 Demo** | [Date] | Final submission + presentation |

---

## 💡 Tips for Success

1. **Start with layout** - Extract containers first
2. **Identify patterns** - Look for repeated code
3. **Name clearly** - If you can't name it, it's not clear enough
4. **Keep it simple** - Don't over-engineer
5. **Test as you go** - Make sure nothing breaks
6. **Ask for help** - Office hours available

---

## 🆘 Getting Help

### Office Hours
- **When:** Tuesday 2-4pm, Thursday 10am-12pm
- **Where:** [Location/Zoom link]
- **What to bring:** Specific components you're stuck on

### Slack Channel
- `#sprint-2-help` for questions
- `#component-examples` for sharing good examples

### Pair Programming Sessions
Sign up for 30-min sessions with TA

---

## 🎯 Grading Rubric

| Category | Points | Criteria |
|----------|--------|----------|
| **Component Extraction** | 40 | Layout (10) + UI (15) + Domain (15) |
| **Semantic Naming** | 15 | Clear, purposeful names |
| **File Organization** | 10 | Proper structure, file sizes |
| **TypeScript Props** | 10 | Proper interfaces, no `any` |
| **Abstraction Level** | 10 | Consistent hierarchy |
| **Documentation** | 10 | Complete COMPONENTS.md |
| **Code Quality** | 5 | Clean, no errors |
| **Before/After Analysis** | 10 | REFACTORING.md with metrics |
| **Demo Presentation** | 10 | Clear explanation of changes |
| **TOTAL** | **120** | Extra credit possible |

### Grade Scale
- **A (100-120pts):** Excellent refactoring, exemplary component design
- **B (85-99pts):** Good refactoring, meets all requirements
- **C (70-84pts):** Adequate refactoring, some issues remain
- **D (60-69pts):** Minimal refactoring, significant issues
- **F (<60pts):** Incomplete or no meaningful refactoring

---

## 🌟 Extra Credit Opportunities (+20 points max)

1. **Storybook Integration** (+10 pts)
   - Set up Storybook
   - Create stories for all UI components
   - Document variants and states

2. **Component Tests** (+10 pts)
   - Write unit tests for 5+ components
   - Use React Testing Library
   - Achieve >70% coverage on components

3. **Design System Documentation** (+5 pts)
   - Create visual guide of all components
   - Document design tokens (colors, spacing)
   - Show component variants

4. **Accessibility Audit** (+5 pts)
   - Run accessibility checker (axe, WAVE)
   - Fix all issues
   - Document accessibility features

---

## 📚 Resources

### Official Documentation
- [React: Thinking in Components](https://react.dev/learn/thinking-in-react)
- [TypeScript: Component Props](https://react-typescript-cheatsheet.netlify.app/docs/basic/getting-started/basic_type_example)

### Articles
- [Semantic JSX by Max Böck](https://mxb.dev/blog/semantic-jsx/)
- [React Component Design Principles](https://namastedev.com/blog/react-component-design-principles/)

### Videos
- [Kent C. Dodds: React Component Patterns](https://www.youtube.com/watch?v=7GC0CLF_P-s)
- [Jack Herrington: Bulletproof React Components](https://www.youtube.com/watch?v=qd0I8YK-xJg)

---

## ✅ Self-Check Before Submission

- [ ] All pages < 100 lines
- [ ] No component > 150 lines
- [ ] Components organized in proper folders
- [ ] All components have TypeScript interfaces
- [ ] Component names are semantic and clear
- [ ] Single level of abstraction maintained
- [ ] COMPONENTS.md created and complete
- [ ] REFACTORING.md with metrics
- [ ] No console errors or warnings
- [ ] Code formatted and cleaned
- [ ] Demo presentation prepared

---

## 🎓 Learning Outcomes

By completing this assignment, you will:
- ✅ Understand component-driven architecture
- ✅ Write maintainable, reviewable React code
- ✅ Apply single responsibility principle
- ✅ Create reusable component libraries
- ✅ Use TypeScript effectively with React
- ✅ Document code professionally
- ✅ Think in terms of abstraction levels

**This is how professional React development is done.** Master these skills and you'll be prepared for industry.

---

## 🚀 Ready to Start?

1. Read the required materials
2. Audit your current code
3. Create your component plan
4. Start refactoring!

**Good luck! Remember: Code for humans, not computers.**
