# Styling React Components

Where the CSS goes, once there are components to attach it to. Read alongside [Basics of CSS](../../../TopUps/1-Basics-of-CSS.md); this is the React-specific half, and the CSS exercise is where you put it to work.

## Styling

CSS Styles can be defined in multiple ways

### In a separate file
This has the problem that it does not scale - at some point the various styles will conflict with each other.

### Inline as the example above
This is the least recommended

### As local variables, as they use in React Native 

e.g. [here](https://github.com/mircealungu/zeeguu-mobile/blob/master/screens/AllArticles.js)

### With the help of `styled-components` library

#### First you install the library `npm install -s styled-components`

#### Then you define styles with the `styled` function!
```js

// Create a Title component that'll render an <h1> tag with some styles
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: #BF4F74;
`;

// Create a Wrapper component that'll render a <section> tag with some styles
const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
`;

// Use Title and Wrapper like any other React component – except they're styled!
render(
  <Wrapper>
    <Title>
      Hello World!
    </Title>
  </Wrapper>
);
```
#### Move components to their own file

#### Benefits of `styled-components`
##### Benefit 1: automatic CSS scoping
- the `Wrapper` and `Title` styles only apply to our title above
##### Benefit 2: automatic delete of CSS
- deleting the component deletes the style
- otherwise, in a huge CSS file you end up with a lot of dead code
