# Protecting routes if a user is not logged in 

### Example: How to improve the code below? 
```js
// App.js 
// ... 
return (  
    <Routes>  
      <Route path="/" element={<Login />} />  
      <Route path="/event-detail/:eventId" element={<EventDetail />} />     </Routes>  
);

// EventDetailPage.js 
const EventDetailPage = () => {  

	// ... 
  
    const currentUser = Parse.User.current();  

	// ... 
	
    if (!currentUser) {  
        return (  
            <div className="error-container">  
                <p>Error: User not logged in.</p>  
            </div>  
        );  
    }
    
```
## With a Higher-Order Component

Creating another React component named `RequireAuth` that redirects to the Login page if the user is not logged in. 
```js
import Parse from "./services/Parse";  
import Login from "./pages/LoginPage";  
  
export default function RequireAuth({children}) {  
    const currentUser = Parse.User.current();  
    
    if (!currentUser) {  
        return <Login />;  
    }  
  
    return children;  
}
```
This component can be then used in the router like this:

```js
	// ... 
	<Route path="/event-detail/:eventId" element={  
	  <RequireAuth>  
		  <EventDetail />
	  </RequireAuth>}  
	/>
```

## With Two Different Routers

```js
// inside App.js or wherever you do your routing
const currentUser = Parse.User.current();  

if (!currentUser) {  
  // return simplified version of routing
  return (  
	  <Routes>  
		<Route path="/" element={<Login />} />  
		<Route path="/signup" element={<SignUpPage />} />
		
		<Route path="*" element={<Navigate to="/" />} />  
	  </Routes>  
  )  
}

// Return the routing for when the a user is logged in
return (  
	<Routes>  
	  <Route path="/home" element={<HomePage />} />  
	  <Route path="/create-event" element={<CreateEvent />} />  
	  <Route path="/event-detail/:eventId" element={<EventDetail />} /> 
	</Routes>  
);
```
