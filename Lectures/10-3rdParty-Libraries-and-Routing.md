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
		- Every URL request is intercepted by the routing library




- What are the essential elements that a router library should cover? 
	- Mapping a route to a page
	- Intercepting navigation to a different page and doing the routing
	- Extracting parameters from a complex route (e.g. `/articles/id=4567`)


#### In class exercise
- Add an about page 
- Use `react-router-dom` to show the about page at `/about` and the main app at `/`
- *Advanced*: Implement your own home-made basic router (see the `window` events `load` and `hashchange` and the `window.location` property)

# Project Work
- Add routing to your project
