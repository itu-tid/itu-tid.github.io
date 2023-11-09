# Routing in React

#### What is routing in web applications?
- Asking the server for the page at a given url
- Uploading content to the server at a given URL
- The routing is implemented on the server
	- parses the URL
	- calls the right program
	- generates the HTTP response
	- sends the response to the client

#### Where and how is routing done in Single Page Applications? 
- On the client side (i.e. browser)
- How? 
	- Every URL request is intercepted by the routing library

#### What are the essential elements that a router library should cover? 
- Mapping a route to a page
- Intercepting the wish of the user to navigate to a different page and doing the routing
- Enabling the programmer to parse route parameters 


#### In class exercise
- Add an about page 
- Use react-router-dom to show the about page at `/about` and the main app at `/`
- *Advanced*: Implement your own home-made basic router (see the `window` events `load` and `hashchange` and the `window.location` property)

# Project Work
- Add routing to your project
