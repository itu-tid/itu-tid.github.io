# Code Quality Sprint - Comprehensive Plan

**When:** After functionality is complete (Sprint 3 or later)
**Duration:** 1-2 weeks
**Focus:** Professional code quality, not new features

---

## 🎯 Why a Code Quality Sprint?

**The Problem:**
Students have been focused on "making it work" for 2 sprints. Now their code:
- ✅ Works functionally
- ❌ Hard to read
- ❌ Hard to maintain
- ❌ Not ready for portfolios or code reviews

**The Solution:**
A dedicated sprint to refactor and polish, focusing on:
1. **Component Architecture** (readability)
2. **Error Handling** (robustness)
3. **Code Organization** (maintainability)
4. **Git & Documentation** (professionalism)

**The Goal:**
Transform "student projects" into "portfolio-ready code."

---

## 📋 Code Quality Sprint Overview

### Option 1: 1-Week Intensive
**Best for:** Limited time, hit the essentials
- 2 class sessions (90 min each)
- Focus: Component architecture + Error handling
- Students fix most obvious issues

### Option 2: 2-Week Comprehensive
**Best for:** More thorough improvement
- 4 class sessions (90 min each)
- Cover all 4 quality aspects
- Students do deeper refactoring

---

## 📚 The 4 Pillars of Code Quality

### 1. Component Architecture & Readability (40% of grade)
**Topics:**
- Semantic component naming
- Eliminating inline styles
- Consistent styling approach
- File organization

**Materials you have:**
- ✅ LESSON_PLAN_ONE_WEEK.md
- ✅ COMPONENT_EXTRACTION_CHEATSHEET.md
- ✅ CASE_STUDY_TODO_APP.md

**Session focus:** Make code readable by non-CSS experts

---

### 2. Error Handling & Robustness (30% of grade)
**Topics:**
- Try-catch blocks
- Loading states
- Error states
- User feedback
- Defensive programming

**Common issues in student code:**
```jsx
// ❌ BAD - No error handling
const [data, setData] = useState(null);

useEffect(() => {
  fetchData().then(setData);
}, []);

return <div>{data.name}</div>;  // Crashes if data is null!
```

```jsx
// ✅ GOOD - Proper error handling
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
  setLoading(true);
  fetchData()
    .then(setData)
    .catch(setError)
    .finally(() => setLoading(false));
}, []);

if (loading) return <LoadingSpinner />;
if (error) return <ErrorMessage error={error} />;
if (!data) return <NotFound />;

return <div>{data.name}</div>;
```

**What to cover:**
1. Always handle loading states
2. Always handle error states
3. Always validate data exists before using
4. Show user-friendly error messages
5. Log errors for debugging

---

### 3. Code Organization & Best Practices (20% of grade)
**Topics:**
- Consistent naming conventions
- DRY principle (Don't Repeat Yourself)
- Magic numbers/strings
- Dead code removal
- Console.log cleanup

**Common issues:**
```jsx
// ❌ BAD - Magic numbers, repetition
if (user.age > 18) { /* ... */ }
if (product.price > 100) { /* ... */ }
if (user.age > 18) { /* ... */ }  // Repeated!

// ✅ GOOD - Constants, reusable
const ADULT_AGE = 18;
const EXPENSIVE_THRESHOLD = 100;

const isAdult = (user) => user.age >= ADULT_AGE;
const isExpensive = (product) => product.price > EXPENSIVE_THRESHOLD;

if (isAdult(user)) { /* ... */ }
if (isExpensive(product)) { /* ... */ }
```

**What to cover:**
1. Extract magic numbers to constants
2. Remove unused imports/variables/functions
3. Remove console.log statements
4. Consistent naming (camelCase vs snake_case)
5. Group related code together

---

### 4. Git Hygiene & Documentation (10% of grade)
**Topics:**
- Meaningful commit messages
- README quality
- Code comments (when needed)
- API documentation
- Setup instructions

**Common issues:**
```bash
# ❌ BAD commit messages
git commit -m "fix"
git commit -m "update"
git commit -m "asdf"
git commit -m "final final final"

# ✅ GOOD commit messages
git commit -m "Fix login form validation for empty email"
git commit -m "Add loading state to profile fetch"
git commit -m "Refactor Button component to use variants"
```

**README checklist:**
- [ ] Project description (what it does)
- [ ] Technologies used
- [ ] Setup instructions
- [ ] How to run locally
- [ ] Environment variables needed
- [ ] Features list
- [ ] Screenshots (nice to have)

---

## 📅 Week-by-Week Plans

---

## OPTION 1: 1-Week Code Quality Sprint

**Use when:** Limited time, hit essentials

### Monday Session 1: Component Architecture + Error Handling (90 min)

#### Part 1: Component Architecture (45 min)
- Use LESSON_PLAN_ONE_WEEK.md Session 1
- Focus on semantic naming and consistency
- Show case study examples

**Key Message:**
"Your code works, but can anyone else read it?"

#### Part 2: Error Handling (45 min)

**Show the problem:**
```jsx
// Many students do this
const Profile = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser().then(setUser);
  }, []);

  return <div>{user.name}</div>;  // Crash!
};
```

**Show the fix:**
```jsx
const Profile = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetchUser()
      .then(setUser)
      .catch(setError)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;
  if (!user) return <NotFound />;

  return <div>{user.name}</div>;
};
```

**Live code this pattern!**

**Assignment for Wednesday:**
- [ ] Audit code for missing error handling
- [ ] Audit code for inline styles/naming issues

---

### Wednesday Session 2: Refactoring Workshop (90 min)

#### Part 1: Component Refactoring (45 min)
- Use LESSON_PLAN_ONE_WEEK.md Session 2
- Live refactor inline styles
- Student practice time

#### Part 2: Error Handling Implementation (45 min)
- Pick a student component without error handling
- Add loading/error states live
- Student practice adding to their code

**Assignment for week:**
- [ ] Fix all inline styles
- [ ] Add error handling to all data fetching
- [ ] Remove console.logs
- [ ] Write basic REFACTORING.md

---

### Deliverables (Due Sunday)

**Required improvements:**
1. **Component Architecture (40 pts)**
   - [ ] Zero inline styles
   - [ ] Semantic component names
   - [ ] Consistent styling approach

2. **Error Handling (30 pts)**
   - [ ] All fetches have try-catch or .catch()
   - [ ] All data components have loading states
   - [ ] User-friendly error messages shown

3. **Code Cleanup (20 pts)**
   - [ ] No console.log statements
   - [ ] No unused imports/variables
   - [ ] No commented-out code

4. **Documentation (10 pts)**
   - [ ] REFACTORING.md with examples
   - [ ] Updated README with setup instructions

**Total: 100 points**

---

## OPTION 2: 2-Week Code Quality Sprint

**Use when:** More time, deeper improvements

### Week 1: Architecture & Error Handling

**Monday Session 1: Component Architecture (90 min)**
- Follow LESSON_PLAN_ONE_WEEK.md Session 1
- Homework: Audit code for issues

**Wednesday Session 2: Error Handling Deep Dive (90 min)**

**Topics:**
1. Loading states everywhere (15 min)
2. Error boundaries in React (20 min)
3. User feedback patterns (15 min)
4. Defensive programming (20 min)
5. Student practice (20 min)

**Error Boundary Example:**
```jsx
// ErrorBoundary.jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <App />
</ErrorBoundary>
```

**Assignment:**
- [ ] Add error handling to all data fetching
- [ ] Add loading states everywhere
- [ ] Fix component architecture issues

---

### Week 2: Code Organization & Polish

**Monday Session 3: Code Organization (90 min)**

**Part 1: Dead Code & Console Cleanup (20 min)**
```bash
# Find console.logs
grep -r "console.log" src/

# Find unused imports (ESLint can help)
npm run lint
```

**Part 2: Magic Numbers & Constants (20 min)**
```jsx
// ❌ BAD
if (user.age >= 18) { /* ... */ }
setTimeout(() => { /* ... */ }, 5000);
if (price > 100) { /* ... */ }

// ✅ GOOD
const ADULT_AGE = 18;
const DEBOUNCE_DELAY = 5000;
const EXPENSIVE_THRESHOLD = 100;

if (user.age >= ADULT_AGE) { /* ... */ }
setTimeout(() => { /* ... */ }, DEBOUNCE_DELAY);
if (price > EXPENSIVE_THRESHOLD) { /* ... */ }
```

**Part 3: DRY Principle (20 min)**
Show repeated code and extract to functions/components

**Part 4: Student Work (30 min)**
- Clean up their code
- Extract constants
- Remove dead code

**Assignment:**
- [ ] Remove all console.logs
- [ ] Extract magic numbers to constants
- [ ] Remove unused code
- [ ] Check ESLint warnings

---

**Wednesday Session 4: Git & Documentation (90 min)**

**Part 1: Git Best Practices (30 min)**

**Good commit messages:**
```
Format: <type>: <description>

Types:
- feat: New feature
- fix: Bug fix
- refactor: Code restructuring
- docs: Documentation
- style: Formatting, missing semi-colons
- test: Adding tests

Examples:
feat: Add user profile page
fix: Resolve login form validation bug
refactor: Extract Button component for reusability
docs: Update README with setup instructions
```

**Show git history:**
```bash
# Bad
git log --oneline
a1b2c3d fix
b2c3d4e update
c3d4e5f final

# Good
git log --oneline
a1b2c3d feat: Add error handling to profile fetch
b2c3d4e refactor: Extract TaskInput styled component
c3d4e5f docs: Add environment variables to README
```

**Part 2: README Workshop (30 min)**

**Template:**
```markdown
# Project Name

Brief description of what your app does.

## Technologies Used
- React 18
- styled-components
- React Router
- Parse Server

## Setup Instructions

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation
\`\`\`bash
git clone <repo-url>
cd project-name
npm install
\`\`\`

### Environment Variables
Create a `.env` file:
\`\`\`
VITE_API_URL=your_api_url
VITE_APP_ID=your_app_id
\`\`\`

### Running Locally
\`\`\`bash
npm run dev
\`\`\`

Open http://localhost:5173

## Features
- User authentication
- Profile management
- Job listings
- Real-time updates

## Screenshots
[Optional]

## Known Issues
- [List any known bugs]

## Future Improvements
- [What you'd add next]
```

**Part 3: Student Work (30 min)**
- Write their README
- Review recent commits
- Improve commit messages going forward

**Final Assignment:**
- [ ] Complete README
- [ ] Clean commit history (if needed, rebase/squash)
- [ ] Final code review self-check
- [ ] Submit refactored code

---

### Week 2 Deliverables (Due Sunday)

**All Week 1 requirements PLUS:**

5. **Code Organization (10 pts)**
   - [ ] No magic numbers (extracted to constants)
   - [ ] No dead code
   - [ ] No console.logs
   - [ ] ESLint clean

6. **Git Hygiene (5 pts)**
   - [ ] Meaningful commit messages from now on
   - [ ] Clean git history

7. **Documentation (5 pts)**
   - [ ] Complete README with setup instructions
   - [ ] Environment variables documented
   - [ ] Features list

**Total: 120 points**

---

## 📊 Grading Rubric

### 1-Week Sprint (100 points)

| Category | Points | Criteria |
|----------|--------|----------|
| Component Architecture | 40 | Zero inline styles, semantic names, consistency |
| Error Handling | 30 | Loading + error states, try-catch blocks |
| Code Cleanup | 20 | No console.logs, no unused code |
| Documentation | 10 | REFACTORING.md complete |

### 2-Week Sprint (120 points)

| Category | Points | Criteria |
|----------|--------|----------|
| Component Architecture | 40 | Zero inline styles, semantic names, consistency |
| Error Handling | 30 | Loading + error states, error boundaries |
| Code Cleanup | 20 | No console.logs, no unused code |
| Code Organization | 10 | Constants extracted, DRY principle |
| Git Hygiene | 5 | Meaningful commits |
| Documentation | 15 | README + REFACTORING.md |

---

## 📝 Self-Assessment Checklist

**Give this to students before submission:**

### Component Architecture
- [ ] I searched for `style={{` and got 0 results
- [ ] All my styled-components/CSS classes have semantic names
- [ ] I use one styling approach consistently
- [ ] No generic names like "Container" or "Wrapper" alone

### Error Handling
- [ ] All my data fetching has try-catch or .catch()
- [ ] All components that fetch data show loading states
- [ ] All components show user-friendly error messages
- [ ] I validate data exists before using it (null checks)

### Code Quality
- [ ] I removed all console.log statements
- [ ] I removed all commented-out code
- [ ] I removed all unused imports/variables
- [ ] ESLint shows no errors or warnings

### Organization (2-week only)
- [ ] I extracted magic numbers to named constants
- [ ] I removed duplicate code where possible
- [ ] My code follows consistent naming conventions

### Documentation
- [ ] I wrote REFACTORING.md with before/after examples
- [ ] My README has setup instructions
- [ ] My README lists all environment variables
- [ ] My recent commit messages are meaningful (2-week only)

---

## 🎯 Class Session Templates

### Session Template: Error Handling Deep Dive

**Objective:** Students understand and implement proper error handling

#### 1. Show the Pain (10 min)
```jsx
// Demo: App crashes when API fails
const BadProfile = () => {
  const [user, setUser] = useState(null);
  useEffect(() => {
    fetchUser().then(setUser);  // What if this fails?
  }, []);
  return <div>{user.name}</div>;  // Crash!
};
```

- Run this live
- Show it crash
- Point out: "This is half your projects right now"

#### 2. The Pattern (20 min)
```jsx
// The 3-state pattern
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

// Always handle all 3 states
if (loading) return <LoadingSpinner />;
if (error) return <ErrorMessage error={error} />;
if (!data) return <NotFound />;
```

**Write on board:**
```
3 States Pattern:
1. Loading (waiting for data)
2. Error (something went wrong)
3. Success (got data)

ALWAYS handle all 3!
```

#### 3. Common Scenarios (20 min)

**Scenario 1: Fetch on mount**
```jsx
useEffect(() => {
  setLoading(true);
  fetchData()
    .then(setData)
    .catch(setError)
    .finally(() => setLoading(false));
}, []);
```

**Scenario 2: Fetch on button click**
```jsx
const handleSubmit = async () => {
  setLoading(true);
  setError(null);
  try {
    const result = await submitForm(data);
    setSuccess(true);
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
};
```

**Scenario 3: Multiple fetches**
```jsx
useEffect(() => {
  setLoading(true);
  Promise.all([
    fetchUser(),
    fetchPosts(),
    fetchComments()
  ])
    .then(([user, posts, comments]) => {
      setUser(user);
      setPosts(posts);
      setComments(comments);
    })
    .catch(setError)
    .finally(() => setLoading(false));
}, []);
```

#### 4. Student Practice (30 min)
"Find ONE fetch in your code that doesn't handle errors. Add the 3-state pattern to it."

Walk around and help!

#### 5. Show & Tell (10 min)
2-3 students show what they added

---

### Session Template: Code Cleanup Workshop

**Objective:** Clean, professional code

#### 1. The Smell Test (15 min)
"Let's find code smells in your projects"

**Search exercises:**
```bash
# Find console.logs
grep -rn "console.log" src/

# Find TODO comments
grep -rn "TODO" src/

# Find commented code
grep -rn "^[[:space:]]*\/\/" src/ | head -20
```

**Show class results:**
"We found 47 console.logs across all projects!"

#### 2. Cleanup Categories (20 min)

**Category 1: Debug statements**
```jsx
// ❌ Delete these
console.log('user:', user);
console.log('!!!!!!');
console.log('test');
```

**Category 2: Commented code**
```jsx
// ❌ Delete these
// const oldFunction = () => {
//   return something;
// };

// useEffect(() => {
//   // old approach
// }, []);
```

**Category 3: Magic numbers**
```jsx
// ❌ BAD
if (age > 18) { }
setTimeout(() => {}, 5000);

// ✅ GOOD
const ADULT_AGE = 18;
const DEBOUNCE_DELAY = 5000;

if (age > ADULT_AGE) { }
setTimeout(() => {}, DEBOUNCE_DELAY);
```

#### 3. ESLint Introduction (15 min)
```bash
npm run lint
```

Show common warnings:
- Unused variables
- Unused imports
- Missing dependencies in useEffect
- etc.

"Fix the easy ones, document the hard ones"

#### 4. Student Cleanup Sprint (30 min)
"You have 30 minutes. Clean your code!"

Checklist:
- [ ] Remove all console.logs
- [ ] Delete commented code
- [ ] Fix ESLint warnings (easy ones)
- [ ] Extract at least 3 magic numbers

#### 5. Before/After (10 min)
Show metrics:
- Console.logs: 47 → 2
- ESLint warnings: 123 → 45
- Magic numbers: 31 → 8

"Progress! Keep going this week!"

---

## 🆘 Office Hours Guide

### What Students Bring

**Common questions:**
1. "How do I name this component?"
2. "Where should error handling go?"
3. "Is this the right pattern?"
4. "How do I fix this ESLint error?"

### Quick Helps

**Naming components (5 min):**
- Ask: "What does it DO?"
- That's the name
- Examples on hand

**Error handling (10 min):**
- Show the 3-state pattern
- Help them implement it
- Test that it works

**ESLint errors (variable time):**
- Some are quick fixes
- Some need discussion
- Some can be ignored (document why)

---

## 📈 Success Metrics

### You know it worked if:
- [ ] Students submit code with 0 inline styles
- [ ] All data fetching has error handling
- [ ] Console is clean (no logs)
- [ ] READMEs are complete
- [ ] Students understand WHY this matters

### Red flags:
- Students don't submit anything
- Minimal changes made
- "This is busywork" complaints
- No understanding of principles

---

## 💡 Teaching Tips

### Frame It Right
❌ "Your code is bad"
✅ "Your code works! Now let's make it professional"

❌ "This is required"
✅ "This is what companies look for in code reviews"

❌ "Fix everything"
✅ "Fix the highest-impact issues"

### Set Expectations
- This is about **polish**, not **functionality**
- It's okay if not everything is perfect
- Focus on the most obvious issues first
- Something is better than nothing

### Celebrate Progress
- "You removed 30 console.logs? Awesome!"
- "Your error handling is much better!"
- "This component name is way clearer!"
- Share good examples publicly

---

## ✅ Final Checklist

### Week Before Sprint
- [ ] Review student code for common issues
- [ ] Prepare 3-4 anonymized examples
- [ ] Set up office hours
- [ ] Choose 1-week or 2-week format

### Session Prep
- [ ] Review session plan
- [ ] Test live coding examples
- [ ] Have backup examples ready

### During Sprint
- [ ] Be available for questions
- [ ] Monitor progress
- [ ] Adjust pace as needed

### After Sprint
- [ ] Grade using rubric
- [ ] Provide specific feedback
- [ ] Document what worked/didn't

---

## 🎯 The Win

**If students leave understanding:**
- "Code readability matters"
- "Error handling makes apps robust"
- "Cleanup is part of professional development"
- "This makes my portfolio better"

**You've succeeded! 🎉**
