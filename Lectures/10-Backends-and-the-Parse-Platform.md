# Backends and the Parse Platform

## Backends

- What is a backend?
	- Defined in opposition to the front-end
	- The server side in a ***client-server architecture***


- What are the responsibilities of the backend?
	- authentication (proving that a user is who they say they are)
	- session management
	- business logic and DB access
	- scheduled jobs (e.g., `cron`)
	- authorization (what can a user do)


- Deploying and implementing a traditional backend
	- machine installation!
	- operating system
	- security & firewall
	- DBMS
	- web server
	- API 
	- logging and analytics
	- backup system


- **Low-code backends**
	- Common solutions for common backend problems
	- Alternatives
		- Firebase = proprietary & hosted by Google
		- Azure = Microsoft’s version 
		- **Parse Server** = open source 


## Parse Platform

Our preferred low-code backend
- Implementation language
	- Node.js based
- History
	Startup => facebook => open source
- Functionality
	- Authentication
	- File storage
	- APIs (REST & GraphQL)
	- Javascript wrapper library
	- Cloud functions
	- Authorization


### Using Parse from Back4App

- Where is the Parse server?
	- On your own hardware
	- In your own cloud server
	- In somebody else's cloud server => back4app.com 


Steps to start working with the Back4App Parse deployment 
1. Create an account on Back4App
2. Install the `parse` library from npm
3. Initialize the global Parse object (see step 4 in the [back4app guide](https://www.back4app.com/docs/react/quickstart))
 
Then you can write code like the one below to save data to your database:

```javascript

import Parse from 'parse';

const Topic = Parse.Object.extend("Topic");
const topic = new Topic();

topic.set("name", "Backends");
topic.set("isDiscussed", false);

topic.save().then(
	(topicObject) => {
		console.log("saved with id: " + topicObject.id);
}, (error) => {
	console.log(error.message);
})
```

To understand in the code above:
- Creating a class for the object
- `save()` - sends the data to the server
- `save.then( (obj) => {...})` - save returns a *promise*





# JS Intermezzo: Async Programming and Promises

- What is [asynchronous programming](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)?
	- Technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs


- [What are Promises and how to Use Them?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises) 
	- Using the `then` syntax for promises
	- Using `await` with promises in `async` functions
	- How to chain two promises? 



# Using Parse - References

Reference Reading == *read as you need* 

Two *alternative documentation sources*
- The Back4App [React Quickstart Guide](https://www.back4app.com/docs/react/quickstart) <-- nicer we think
- The Parse.js [Getting Started Guide](https://docs.parseplatform.org/js/guide/#getting-started)

- [CRUD operations](https://www.back4app.com/docs/react/data-objects/react-crud-tutorial)
	- CRUD = **Create, Read, Update, and Delete objects to/from the DB**
- [Basic Data types](https://www.back4app.com/docs/react/data-objects/react-data-types)
- [Relationships](https://www.back4app.com/docs/react/data-objects/relationships)
	- **Model a relationship between two objects** (e.g, User and Topic)
- [Basic Queries](https://www.back4app.com/docs/react/data-objects/react-query)
	- **Query for a list of objects**

- [Query Cookbook](https://www.back4app.com/docs/react/data-objects/react-query-cookbook)
	- Filters
	- Query for complex sets of interelated objects (e.g. All topics of a given user)


## User Management with Parse
- [User Creation / Login](https://www.back4app.com/docs/react/working-with-users/sign-up-page-react)



## Individual Work
- Solve the [Sequencing Animations](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Sequencing_animationshttps://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Sequencing_animations) problem
- Mandatory reading:
	- [What are Promises and how to Use Them?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises) 


## Project Work
- Start saving and loading data to and from the database
