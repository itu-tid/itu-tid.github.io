
# CSS 

Originally CSS for styling; HTML for content. Thought out to really separate programming from styling. In practice, it's very hard to separate the two. 

I've always Googled stuff. And these days you can ask ChatGPT. And that's fine. However, both when Googling, and especially when ChatGPT-ing, you must understand, in order to select the best solution. 

# Seems simple. Why bother?

Quite a complicated concept if you look at the [number of questions on StackOverflow](https://stackoverflow.com/tags) (compared with Java half the questions... also daily)

[Most asked question](https://stackoverflow.com/questions/1014861/is-there-a-css-parent-selector) - what do we learn from the discussion? 
- pseudo-classes 
- ever evolving (look at the [date](https://drafts.csswg.org/selectors-4/#relational) of the referred Draft)
- different browsers have different implementations (e.g. implementation of [:has](https://caniuse.com/css-has))
- functional (!) pseudo-selector

# CSS Selectors

To Read
- [What is a selector? ](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#what_is_a_selector)
- [How to apply the same style to a list of selectors?](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#selector_lists)
- What happens when a selector is invalid? What happens when a selector from a list is invalid?

You **must** know: 
- [Type, class, and id selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors)
- [Attribute Selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Attribute_selectors)
- [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) certain states (e.g. a:hover, input:checked, [p:first-child:first-letter](https://css-tricks.com/snippets/css/drop-caps/))
- [Combinators](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Combinators), most important: `article>p` and `article p` (direct child vs any recursively contained child)
- [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements), e.g. [::after](https://developer.mozilla.org/en-US/docs/Web/CSS/::after) , [::backdrop](https://developer.mozilla.org/en-US/docs/Web/CSS/::backdrop) , [::selection](https://developer.mozilla.org/en-US/docs/Web/CSS/::selection) , p::first-line

A nice [Demo](https://www.w3schools.com/cssref/trysel.php) of selectors in action

To read:  [selector reference](https://www.w3schools.com/cssref/css_selectors.php)

You should know:
- What is the difference between the `class1 class2` and `class1>class2` selectors?
- How to style specially an item that has the property `is-selected`, e.g. `<li is-selected>Home</li>`?
- Which is correct: `element [property]` and `element[property]`?

## Exercise
- Do the [Selectors Tasks](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Selectors_Tasks) from mdn
- Install WebStorm (or use VSCode) and do the tasks in this exercise, and all the following ones locally, instead of on the website

# Cascade, Inheritance, and Specificity 

To Read: [article](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)

The **cascade** is an algorithm that defines how user agents combine property values originating from different sources: browser stylesheet, [user-defined stylesheet](https://www.thoughtco.com/user-style-sheet-3469931) (an old concept that does not make sense these days), and website author stylesheet. Author stylesheet has precedence. 

To Read: [What is specificity in CSS and what is more specific: a class selector or an element selector?](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#specificity)
- Play with the example

To Read: [What is inheritance?](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#inheritance)
- Play with the see example

To answer: 
- What has higher priority: the style for an element or for a class? But a class or an id? 

## Exercise
- Do the [Inheritance tasks](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_tasks) from mdn

# **The Box Model**

Everything in CSS has a box around it.

A block box in CSS has: content area, padding, [margin](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#margin), border: 

![](../Lectures/images/css-box.png)

Two box models:
1. [Standard Box Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#the_standard_css_box_model): padding & border is added to the width & height
2. [Border-Box Model](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#the_alternative_css_box_model): content area width = width - padding & border

To think about: which do you prefer? 

When specifying [length dimensions](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#numbers_lengths_and_percentages) you can use either absolute units (e.g. 10px) or relative units (e.g. 10em, 10rem, 100vh, 100vw)

Note: using rem instead of em is more accessible because it's relative to the user's font size in the browser or OS. 

## Exercise
- Do the [box model tasks](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Box_Model_Tasks) from mdn



# Flow Layouts

Depending on the type, there are several types of outer display types. In what's called the  [Normal flow](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flow_layout/Block_and_inline_layout_in_normal_flow) elements with the corresponding 
- **display: inline** -- layout horizontally (e.g. words in a paragraph).
- **display: block** -- layout vertically (e.g. paragraphs)
- **display: [inline-block](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/The_box_model#using_display_inline-block)** -- layout block inside, and horizontally in the context


## In Flow and Out of Flow

See: [article]((https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flow_layout/In_flow_and_out_of_flow))

- Out of flow items create their own mini-layout (a new **formatting context**)
- Out of flow items:
	- [floated](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Floats#display_flow-root) items - originally for floating images inside text; later used for all kinds of layout hacks; now returned back to original 
	- elements  with `position: absolute`  


See the demo of: [Positioning elements](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
- What is the difference between static, relative and absolute? 


## Exercise

Implement a CSS layout for a website that provides translations from French to English. It should add the translation above the original text as in the figure below. 

![](../Lectures/images/inline-block-example.png)
Start from the following HTML, and define the required CSS.

```
<html>
	<p>
	Zoom demande à ses salariés de <span class="trans"><span class="eng">to return face-to-face</span><span class="fr">revenir en présentiel</span></span>
	</p>
	
	<p>
	En 2020, les revenus de l’entreprise <span class="trans"><span class="eng">had more than tripled</span><span class="fr">avaient plus que triplé</span></span> ; ils ont même continué d’augmenter en 2021, d’environ 55 %. Mais la progression a fortement ralenti l’année dernière : dans la période post-pandémie, la société de vidéo conférence a vu ses bénéfices chuter.
	</p>
	
</html>
```

