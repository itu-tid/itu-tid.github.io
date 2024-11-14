
# Steps Towards Full-Stack Development: Costs, Efficiency, Code that Must Run on the Server


## Being Aware of Costs

Back4App, the hosted service of Parse costs money. You are using a free tier, but you must realize that this is a cloud-based solution. For cloud-based solutions one has to pay. 

Consequently, a free tier will have limitations. The limitations of the Back4App server ensure that you do not put too much pressure on the server. 

The image below shows the prices and limitations of the Back4App various plans. 

![](images/parse-server-plans.png)

In particular for the free tier, you have limited:
- number of requests
- data transfer
- data storage

### How does the fact that you are using a backend-as-a-service impact your application? 

The answer is: you have to be smart about resource usage. 

Case Study: MathsCamp -- looking at the networking tab... why might we need to improve the interaction of this 

![](images/maths-camp-lots-of-requests.png)

## Using Queries the Smart Way

If you have limited requests it makes sense to get as much data from the DB in one go, as opposed to run multiple queries. 

This is not a problem only for backends-as-a-service - this is a general problem. If you are not smart about querying your backend you will end up with a slow application. 

### What is the N+1 Select Problem? 

This is one of the most popular ways of using a DB wrongly. 
You send a query, get n objects back, and then for every one of those objects, you send another query to get more information. 

In general it's slow.
In the particular case of cloud-hosted-parse, this is also stupid because you're running out of requests. 

How to solve it? Get all the data at once by *joining* the corresponding tables. 

And in Parse?

### How to update elements ? 

#### Polling: The low-tech way
- set a timer
- when the timer expires, request the data again from the server; redisplay if needed

#### Event-Driven Approaches: The Advanced Way
- allow the server to send you events when something in your query has changed
- update only when something has actually changed



## Code That Does not Run on the Client

One of the nice things is that with Parse we did not have to implement a server. 

All the code runs on the client side until now. `Parse.Query`, `Parse.Object` - they're APIs that run in the context of our Application. 

However, for some things, we will need a server.

### For what kinds of computations do we need to write code that *runs on the server*?
- complex calculations on the server side that would be too expensive to run on the client side
- statistics that might involve the data of all the users (e.g., average rating of all the movies in the database; one does not want send all that data to the client; it is good to do the calculations on the server)
- calling 3rd party APIs (especially those that require a secret API key that can't be hardcoded in the Javascript)
- making a check before a user writes something to the database or updating some other metadata after a write is done.

To think about: Examples of computational tasks from your own project that 

### Cloud Functions in Parse

In Parse, cloud functions are
- defined on the server that are run in the context of the server
- called from the JS client by name with parameters

Example of cloud function called from the client: 
```js
const params = {movie: "Oh Brother, Where Art Thou?"};
const ratings = await Parse.Cloud.run("totalCounters", params);
```

Such a function assumes that on the server the implementation of the `averageStars` is present. A possible implementation could be: 

```js
Parse.Cloud.define("averageStars", async (request) => {

	const query = new Parse.Query("Review");	
	query. equalTo ("movie", request.params.movie);
	
	const results = await query. find();

	let sum = 0;
	for (let i = 0; i < results.length; ++i) {
		sum += results [i].get ("stars");
	} 

	return sum / results.length;
});
```

Observe in the function implementation the following:
- we can still use the `Parse.Query` API
- the params sent from the client are stored in the `request.params`
- the function is defined as `async` so it's returning a promise

To declare cloud functions in Parse one has to go to the `Dashboard`> `Cloud Code` and add it to the `main.js` file under the `cloud` folder. (see [example](https://www.back4app.com/docs/get-started/cloud-functions)). Once declared, you have to use the `Deploy` button at the bottom of the editor. 


**How can you automatically run a function on the server before a user makes a write to the database?**
- the `beforeSave` method of `Parse.Cloud`, e.g.

```js
Parse.Cloud.beforeSave ("Review", (request) => {

	const comment = request.object.get ("comment");
	
	if (comment. length > 140) {
		// Truncate and add a ...
		request. object. set ("comment", comment.substring (0, 137) +
		" ...");
	}
});
```

To think about:
- what does the above code do? 
- how could a user abuse your system if you don't implement the above code?
- if you check for comment length in JS in the UI of your application... why would you still have to check right before saving a review also on the server?


**How can you define a function that is automatically called *after* a user makes a write to the database?**

```js
Parse. Cloud.afterSave ("Comment", (request) => {

	const query = new Parse.Query ("Post");
	
	query.get(request.object.get("post").id)
		•then (function (post) { post.increment ("comments");
			return post.save ( );
		})
	
	.catch (function (error) {
	
	console.error ("Got an error " + error.code + " : " error .message);
	
	});

});
```
What does the above code do? 
