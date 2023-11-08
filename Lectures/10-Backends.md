# Backends

## Backend

- Defined in opposition to the front-end
- The server side in a *client-server* architecture


- Responsibilities
	- authentication 
	- session management
	- business logic and DB access
	- scheduled jobs (e.g., `cron`)
	- authorization


- Installing it
	- machine
	- security & firewall
	- DBMS
	- web server
	- API 
	- logging and analytics
	- backup system

We do not have time for that in this course: instead, we'll use a **low-code backend**
- common solutions for common backend problems
- alternatives
	- Firebase = proprietary & hosted by Google
	- Azure = Microsoft’s version 
	- **Parse Server** = open source & you can self host

### Parse Server
- node.js based
- startup => facebook => open source
- deployment
	- by yourself
	- on back4app

### Back4App Parse
- Database
- Authentication
- File storage
- APIS (Javascript, REST & GraphQL)
- Cloud functions
- Authorization


### A bit about APIs
- https://rickandmortyapi.com/ 
- you can see by example:
	- REST
	- GraphQL
- you test them with Postman
- you also test them with the help of the `fetch` API


### Using Parse Platform with Back4App in your Project

- Create an account on Back4App
- Find the right library, **install it**, and import it
	- installing: 
		- npm i --save 
		- commit package.json 
- 
- Then you can write code like the one below

```javascript
const Topic = Parse.Object.extend("Topic");
const topic = new Topic();

topic.set("name", "Backends");
topic.set("isDiscussed", false);

topic.save().then((topic) => {
	console.log("saved with id: " + topic.id);
}, (error) => {
	console.log(error.message);
})
```


- This is not REST api nor is it GraphQL
- So what is this?
- [Read upon it](https://docs.parseplatform.org/js/guide/#getting-started)
	- **create and save objects to the DB**
	- **model a relationship between two objects** (e.g, User and Topic)
	- **Save a [relationship between two objects](https://docs.parseplatform.org/js/guide/#saving-nested-objects) in the DB**  
	- **Query for a list of objects**
	- **Delete an object**
	- query for complex sets of interelated objectst (e.g. All topics of a given user)



# Pulling Updates vs. Event-Driven Updates

- Simplest way to update message in a chat
	- repeat
		- get all messages for conversation
		- sleep 1s

- More advanced version is with a publish-subscribe pattern
	- in Parse this is using Live Query 
	- declare a query
	- register event handlers for all kinds of events relative to that query
	- for react you have @parse/react and [`useParseQuery`](https://www.back4app.com/docs/react/real-time/react-hook-real-time)


