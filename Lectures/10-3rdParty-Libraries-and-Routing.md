# Third Party Libraries


- What is the relationship between react, npm and Javascript?
- How do you instal dependencies with `npm`? What do you do to make sure that your colleagues also know which dependency you are using?
- When do you have to run `nmp install`?
- Do you add `node_modules` to version control? What's the principle there?
- Why do we list dependencies in `packages.json`?
- What is the meaning of the version numbers in `packages.json`? [How is semantic versioning used in npm?](https://docs.npmjs.com/about-semantic-versioning)
- Why do we need package-lock.json? Do we commit it to GH?
- Finding libraries on [https://www.npmjs.com](https://www.npmjs.com/)

Live Demo Example

- Adding a progress-bar from [`mui`](https://mui.com/material-ui/react-progress/)
- Also adding a toast?



# Routing in React


- What is routing in web applications?
	- Associating a page with a given url 



- Where is routing traditionally implemented in web applications?
	- On the server side
	- Steps done by the server: 
		- parses the URL
		- calls the right program
			- generates the HTTP response
		- sends the response to the client



- Where and how is routing done in Single Page Applications? 
	- On the client side (i.e. browser)
	- How? 
		- Every URL request is intercepted by the *routing library*



- Is Routing the responsibility of React?
	- nope. React is responsible with the rendering of components
	- Routing has to be implemented by a 3rd party library



- What are the **essential elements** that a router library should cover? 
	- **Mapping a route to a page**
	- **Intercepting navigation to a different page** and doing the routing
	- **Extracting parameters from a complex** route (e.g. `www.sharenow.com/cars?id=4567`) 
	- Nested routes (e.g. `www.sharenow.com/cars/new-arrivals`)


#### In class coding

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

```javascript
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
- Do not use anchor tags instead of `<Link>` components because using anchor tags would not allow applications to remain Single Page Application ( SPA). HTML anchor tag would trigger a page reload or page refresh when clicked. 



https://reactrouter.com/en/main/hooks/use-params



# Project Work
- Add routing to your project by using `react-router-dom`
