# Component Extraction Cheat Sheet

## 🚦 Quick Decision Tree

```
Is this JSX block hard to understand?
├─ YES → Can you describe it in 1-2 words?
│  ├─ YES → Extract component with that name
│  └─ NO → Break it into smaller logical pieces
│
└─ NO → Is it repeated 3+ times?
   ├─ YES → Extract reusable component
   └─ NO → Keep as is (don't over-abstract)
```

---

## ❌ vs ✅ Quick Examples

### Layout Components

```tsx
// ❌ Bad - What is this div?
<div className="mx-auto flex w-full max-w-xl flex-col gap-6 px-4 py-6">

// ✅ Good - Clear semantic name
<ProfileContainer>
```

### Domain Components

```tsx
// ❌ Bad - Implementation details everywhere
<section className="flex w-full flex-col items-center gap-2 p-6">
  <div className="size-24 rounded-3xl bg-neutral-300">
    <img src={user.avatar} />
  </div>
  <h2>{user.name}</h2>
</section>

// ✅ Good - Semantic hierarchy
<ProfileHeader>
  <Avatar user={user} />
  <UserName>{user.name}</UserName>
</ProfileHeader>
```

### Repeated Patterns

```tsx
// ❌ Bad - Copy-pasted 10 times
<button className="rounded-xl bg-neutral-200 px-4 py-2 hover:bg-neutral-300">
  Click me
</button>

// ✅ Good - Reusable component
<Button variant="secondary">Click me</Button>
```

---

## 🎯 The 4 Tests

| Test | Question | Example |
|------|----------|---------|
| **Tech Lead Test** | Can non-CSS person understand structure? | `<ProfileHeader>` ✅ vs `<div className="...">` ❌ |
| **Semantic Test** | Can you name it in 1-2 words? | `<JobCard>` ✅ vs `<Component1>` ❌ |
| **DRY Test** | Is pattern repeated 3+ times? | Extract if yes |
| **SLA Test** | Is everything at same abstraction level? | Mix `<Header>` and `<div className="...">` = ❌ |

---

## 📋 Step-by-Step Process

### 1. Identify Sections
```tsx
// Draw boxes around logical groups
┌─────────────────────┐
│ Header Area         │ → ProfileHeader
├─────────────────────┤
│ About Section       │ → ProfileSection
├─────────────────────┤
│ Experience List     │ → ExperienceList
│  ├─ Experience Item │ → ExperienceEntry
│  └─ Experience Item │ → ExperienceEntry
└─────────────────────┘
```

### 2. Name Components
- Use **nouns**: `Button`, `Card`, `Avatar`
- Be **specific**: `ProfileHeader` not `Header`
- Show **purpose**: `PrimaryButton` not `BlueButton`
- Use **domain terms**: `JobListing` not `Item`

### 3. Create Component Files
```
components/
├── ui/             ← Reusable primitives
│   ├── Button.tsx
│   └── Avatar.tsx
├── layout/         ← Layout containers
│   └── PageContainer.tsx
└── [domain]/       ← Domain components
    └── ProfileHeader.tsx
```

### 4. Extract Props
```tsx
// Identify what varies
<Button
  variant="primary"    // Style variation
  size="large"         // Size variation
  onClick={handleClick} // Behavior
>
  Click me             // Content
</Button>
```

### 5. Refactor Page
```tsx
// Before: 275 lines of mixed HTML/CSS
const Profile = () => {
  return <div className="...">...</div>
}

// After: 60 lines of semantic components
const Profile = () => {
  return (
    <ProfileContainer>
      <ProfileHeader user={user} />
      <ProfileSections user={user} />
    </ProfileContainer>
  );
};
```

---

## 🔧 Component Templates

### Layout Component
```tsx
interface ContainerProps {
  children: ReactNode;
}

export const Container = ({ children }: ContainerProps) => {
  return (
    <div className="[your-layout-classes]">
      {children}
    </div>
  );
};
```

### UI Component (with variants)
```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'small' | 'medium' | 'large';
  children: ReactNode;
  onClick?: () => void;
}

export const Button = ({
  variant = 'primary',
  size = 'medium',
  children,
  onClick
}: ButtonProps) => {
  return (
    <button className={getButtonClasses(variant, size)} onClick={onClick}>
      {children}
    </button>
  );
};
```

### List Component
```tsx
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => ReactNode;
  emptyMessage?: string;
}

export const List = <T extends { id: string }>({
  items,
  renderItem,
  emptyMessage = "No items"
}: ListProps<T>) => {
  if (items.length === 0) return <p>{emptyMessage}</p>;

  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{renderItem(item)}</li>
      ))}
    </ul>
  );
};
```

### Polymorphic Component (semantic flexibility)
```tsx
interface CardProps {
  children: ReactNode;
  as?: 'div' | 'article' | 'section';
}

export const Card = ({ children, as: Element = 'div' }: CardProps) => {
  return (
    <Element className="rounded-lg border p-4">
      {children}
    </Element>
  );
};

// Usage
<Card as="article">...</Card>
```

---

## ⚠️ Common Mistakes

| Mistake | Why Bad | Fix |
|---------|---------|-----|
| `<div className="container">` everywhere | Meaningless name | `<ProfileContainer>`, `<JobContainer>` |
| `Component1`, `Component2` | No semantic meaning | Name by purpose |
| 50-line component inline | Hard to read/test | Extract to file |
| 15 props | Too coupled | Break into smaller components |
| `<BlueButton>` | Names appearance | `<PrimaryButton>` (names purpose) |
| Mixing `<Header>` with `<div className="...">` | Mixed abstraction | Keep consistent level |

---

## 📊 Before/After Metrics

**Good refactoring achieves:**
- ✅ 50-70% line reduction in page files
- ✅ No component > 150 lines
- ✅ 3-5 reusable components per page
- ✅ Clear component hierarchy (3-4 levels max)
- ✅ Reviewable without CSS knowledge

---

## 🎓 Sprint Assignment Quick Checklist

- [ ] Identify all pages in your app
- [ ] For each page, list the semantic sections
- [ ] Name each section as a component
- [ ] Extract layout components (containers, wrappers)
- [ ] Extract UI primitives (buttons, avatars, cards)
- [ ] Extract domain components (profile header, job card)
- [ ] Refactor pages to use components
- [ ] Test: Can someone unfamiliar with your CSS understand structure?
- [ ] Document components with JSDoc
- [ ] Create Storybook stories (bonus)

---

## 💡 Pro Tips

1. **Start with layout** - Extract containers first
2. **Then UI primitives** - Buttons, avatars, inputs
3. **Finally domain** - Profile headers, job cards
4. **Use TypeScript** - Props interfaces catch errors
5. **Write README** - Explain component usage
6. **Keep it simple** - Don't over-engineer

---

## 🆘 When Stuck

**Ask yourself:**
1. What does this component DO? (name it that)
2. Is someone seeing this for first time confused? (extract)
3. Would I copy-paste this elsewhere? (extract)
4. Can I test this alone? (if no, extract)

**The Golden Rule:**
> "Code is read 10x more than it's written. Optimize for reading."

---

## 📚 Quick Links

- [Full Guide](./COMPONENT_EXTRACTION_GUIDE.md)
- [Semantic JSX Article](https://mxb.dev/blog/semantic-jsx/)
- [React Docs: Composition](https://react.dev/learn/passing-props-to-a-component)
