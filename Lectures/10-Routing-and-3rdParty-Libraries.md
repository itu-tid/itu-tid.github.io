# Routing in Web Applications

- What is routing in web applications?

- Where is routing traditionally implemented in web applications?
	- On the server side
		- server parses the URL
		- then, depending on the server type
			- static = simply returns the right page
			- dynamic = calls the right program, which
				- generates the HTTP response
				- returns it to the server
				- server sends the response forward to the client


- However, when you have a single page application? 
	- The whole point is that you don't want to go to the server for the pages, but generate them locally
	- The easiest way is to serve the whole application at a static url (e.g. mirceastodoapp) and do not use routing and pages anymore
	- Why would that be bad? Discuss
	- So if this is bad, how do we implement routing in Single Page Applications? 
		- On the client side (i.e. browser)
		- Every URL request is intercepted by the our SPA


- What are the **essential elements** that a router for a single page application should do? 
	- **Mapping a route to a page** (in react this is going to be a component)
	- **Extracting parameters from a complex** route (e.g. `www.sharenow.com/cars?id=4567`) 
	- Route nested routes (e.g. `www.sharenow.com/cars/new-arrivals`)
	- Provide a default route mapping (What do you display when no route matches?)



## Routing in React

- Is Routing the responsibility of React?
	- You'd think so... but, nope. React does not care. 
	- React is responsible with the rendering of components
	- Routing has to be implemented by a 3rd party library


- How would a 3rd party library work? 
	- **Intercepting the intent of navigating to a different page** and rendering the corresponding page 
	- How can it intercept? 

- How to find a routing library? 
	- Look on `npm`
	- Choose the most popular
	- Why is this a good idea? 
		- popularity is proportional to support
		- *many eyes catch all the bugs*

## In class coding using `react-router-dom` 

- Create an About page as a React component
- Use `react-router-dom@6` to show the about page at `/about` and the main app at `/`

1. Declare the routes
```javascript
import {Routes , Route } from "react-router-dom" 
import {BrowserRouter} from "react-router-dom"
import Home from "./components/Home/Home" 
import About from "./components/About/About" 
function App(){ 
   return ( 
      <div> 
      <BrowserRouter>
	        <Routes> 
	            <Route path="/" element={<Home/> } /> 
	            <Route path="/about" element={<About/> } /> 
	       </Routes> 
       </BrowserRouter>
    </div> 
)} 
export default App
```

Use `Link` components 

```javascript
import React from 'react'; 
import { Link } from 'react-router-dom';  
const Header = () => { 
    return ( 
        <div className="App"> 
             <Link to="/" >  Home  </Link> 
             <Link to="/about" >  About </Link> 
        </div> 
    ); 
};
```

Sometimes you need to programmatically change the url:


```js
import React from "react" 
import {useNavigate} from "react-router-dom" 
  
export default function Profile() { 
   let navigate = useNavigate() 
   return ( 
	   <div> 
	         <h2> This is profile </h2> 
	         <button> onClick ={()=>{ navigate("/about")}}> Login 
	         </button> 
	   </div> 
	);
```

Note:
- Do not use anchor tags instead of `<Link>` components because using anchor tags would not allow applications to remain Single Page Application ( SPA). HTML tag would trigger a page reload or page refresh when clicked. 

Note 2:
- However, what happens if the user does a reload on your `/about` page? The request will go the server. However, we only have an `index.html` on the server, we do not have an about! 
- The solution in this kind of situations is that normally, the web host will redirect all the page-not-found to the `index.html` such that tis' still the react app that gets to handle the request. And the react app will parse the url of the page, and handle it again.
- We'll talk more about servers and deployment later in the course. 

https://reactrouter.com/en/main/hooks/use-params




# Third Party Libraries


- What is the relationship between react, npm and Javascript?
	- could be cool to get a VM; and show them how you compile, and how you host? 
	- but that's for later
- How do you instal dependencies with `npm`? What do you do to make sure that your colleagues also use the same dependency that you are using?
- When do you have to run `nmp install`?
- What is the `node_modules` folder good for? Should you add it  to version control? Why or why not? 
- Why do we list dependencies in `packages.json`?
- What is the meaning of the version numbers in `packages.json`? [What is semantic versioning?](https://docs.npmjs.com/about-semantic-versioning)
- Why do we need `package-lock.json`? Do we commit it to GH?





# Project Work
- Start working on the main pages in your project
- Add routing to your project by using `react-router-dom`
