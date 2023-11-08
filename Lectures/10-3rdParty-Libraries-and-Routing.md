


# Third Party Libraries

- What is the relationship between react, npm and Javascript? 
- How do you instal dependencies with `npm`? What do you do to make sure that your colleagues also know which dependency you are using? 
- When do you have to run `nmp install`?
- Do you add `node_modules` to version control? What's the principle there? 
- Why do we list dependencies in `packages.json`? 
- What is the meaning of the version numbers in `packages.json`? [How is semantic versioning used in npm?](https://docs.npmjs.com/about-semantic-versioning)
- Where to find 3rd party libraries? See:  https://www.npmjs.com

Live Demo Example 
- Adding a progress-bar from [`mui`](https://mui.com/material-ui/react-progress/)
- Also adding a toast? 



# Single Page Applications

#### What are Single Page Applications (SPAs)? 

#### Why are they useful? 

#### What's the relationship between the client-server architecture and SPAs?


# Routing

#### What is routing in web applications?
- Asking the server for the page at a given url
- Uploading content to the server at a given URL
- The routing is implemented on the server
	- parses the URL
	- calls the right program
	- generates the HTTP response
	- sends the response to the client

#### Where and how is routing done in Single Page Applications? 
- on the client side (in the browser; client = browser for you)
- how? 
	- the new URL request is intercepted by the Javascript library

#### What are the essential elements that a router library should cover? 
- mapping a page to a route
- intercepting the wish of the user to navigate to a different page and doing the routing on the client side
- 

In class exercise: 
- add an about page 
- use react-router to 

# Project Work
- Find out what's the difference between `react-router` and `react-router-dom`
- Add the right dependency to your project
- Implement basic routing for at least two of the screens


## Advanced Questions / To Think About

1. What happens when one sends a full url straight to the server? e.g. zeeguu.org/exercises? 