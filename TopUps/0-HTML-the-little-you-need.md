# HTML, the little you need

Two of you asked for this after the first lecture, and it was a fair thing to ask: the course assumed HTML without ever saying so. You need less of it than you might think — this whole page is the amount.

## An element is a tag, some content, and a closing tag

```html
<p>Buy milk</p>
```

`<p>` opens it, `</p>` closes it, and what sits between is the content. That is the entire shape, repeated for every element there is.

A few elements have no content and close themselves:

```html
<input />
<img src="cat.png" />
```

## Attributes go in the opening tag

```html
<input type="checkbox" checked />
<a href="https://itu.dk">the university</a>
```

`type`, `checked` and `href` are **attributes**: settings on the element, written `name="value"` in the opening tag. Some, like `checked`, are just present or absent.

## Elements nest, and the nesting is the structure

```html
<ul>
  <li>Buy milk</li>
  <li>Call the landlord</li>
</ul>
```

A list contains list items. Something inside something else is *part of* it, and that containment is the whole of HTML's structure — there is nothing else to it. It is also why the boxes in [Finding the Components](../Lectures/Technical/Structure/Finding-the-Components.md) work as a way of finding components: the boxes you draw on a screen are already the nesting.

## The tags this course actually uses

| tag | what it is |
|---|---|
| `<p>` | a paragraph of text |
| `<h1>` … `<h3>` | headings, largest first |
| `<div>` | a box with no meaning of its own — a container |
| `<span>` | the same, but inline, inside a line of text |
| `<ul>`, `<li>` | an unordered list, and one item in it |
| `<form>` | a group of inputs that can be submitted together |
| `<input>` | a field you type in, or a checkbox |
| `<button>` | a button |
| `<section>` | a box that *does* mean something: a part of the page |

That is close to the complete list. If you know these nine, nothing in this course will show you HTML you cannot read.

## Where JSX differs from HTML

This is the part worth reading even if you already knew all of the above, because it is where HTML knowledge quietly stops being correct.

**`class` becomes `className`.** `class` is a reserved word in JavaScript, and JSX is JavaScript.

```jsx
<div className="panel">…</div>
```

**Every element must be closed.** HTML forgives `<input>` and `<br>`; JSX does not. Write `<input />`.

**A component returns one element.** Two side by side is an error, which is what the empty tag `<>…</>` is for — it groups them without adding anything to the page.

**Curly braces escape into JavaScript.** `{todo.text}` puts a value in; `value={text}` puts one in an attribute. Anything inside `{}` is an expression, evaluated and dropped in place.

**Attribute names are camelCase.** `onclick` becomes `onClick`, `tabindex` becomes `tabIndex`.


## References

- [MDN: HTML basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Creating_the_content) — the same ground, at more length
- [React: Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx) — the differences above, from React's side
