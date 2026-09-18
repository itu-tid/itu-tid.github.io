# Backends and Low-Code Backends

Motivation: we want to be full-stack web developers :) But we don't have much time.

> **Read before the lecture:** [Async Programming and Promises](../../../TopUps/6-Async-Programming-and-Promises.md). Everything you ask a backend for arrives later, which in JavaScript means a **promise**. From the first `save()` onwards this lecture assumes you have met one, and knows the difference between `.then()`, `.catch()` and `await`.
>
> **Also before the lecture:** run `node --version` and make sure it says 20, 22 or 24. Parse 8 needs one of those, and on an older Node `npm install parse` quietly installs an old release instead of failing.

## What a backend is

### "Backend" only means something relative to a front-end
- **Front-end** -- code that runs in the user's browser and handles presentation and user interaction
- **Back-end** -- handles data processing, storage, and security

### Client-server is the arrangement, and the backend is the server half

The pair has a name, and it is older than the web: a ***client-server architecture***. 

The **client** runs on the user's machine and asks for things; the **server** runs somewhere else and answers.

![](../images/client-server-architecture.png)

The detail that matters is the one the picture shows and the phrase does not: **there are many clients and one server.** Nearly everything in the next three weeks follows from that asymmetry.

- **The server is the only shared thing**, so it is the only place where two users can meet. Sharing a to-do list is possible because there is one copy of it and both clients are talking to that copy.
- **The server is the only trusted thing.** Every client runs on somebody else's computer, in code they can read and change. Anything you need to be *true* *has to be enforced on the server* — which is next week's lecture in one sentence.
- **The server is far away.** Between the asking and the answering there is a network, and your interface has to have something to show meanwhile.


*Note:* Client / front-end are going to be used interchangeably in this course. 


### Backend Responsibilities: The backend takes care of everything the browser cannot be trusted with

1. Authentication (proving that a user is who they say they are)
2. Authorization (checking what a user is allowed to do)
3. Session management (tracking a user across requests, so they don't log in again on every click -- this is a result of HTTP being a stateless protocol)
4. Business logic and DB access (because it's the one central place, as per above)
5. Scheduled jobs (e.g., `cron`, backups, etc.)
6. API endpoints / request handling (since the backend receives and responds to requests)
7. Data validation (ensuring incoming data is correct/safe)

### Infrastructure: A traditional backend needs that you configure many pieces of infrastructure before writing even a line of your own code

1. **Machine** setup (or create a VM with a cloud provider)
2. **Operating system** installation & configuration
3. Security & **firewall** configuration
4. **Database** management system (DBMS)
5. **Web server** -- application that listens to HTTP requests and serves pages to clients (e.g. nginx, apache2)
6. **Application server** -- runtime environment in which your application will be executed
7. **Logging, monitoring & analytics** -- supper essential for a service that has to be available non-stop
8. **Backup** system

Note that none of the eight is on the previous list. That list was about *responsibilities*; this one is about the *machinery* you would have to assemble before you could discharge a single one of them.

## Low-code backends and Backends-as-a-service
### A low-code backend hands you (some of) the eight responsibilities already built

The responsibilities arrive already assembled, and what you get is a **pre-built solution** for the needs that every application has, so that the only code you write is the code particular to your application domain. 

**Low-code** says how much you have to write to implement your backend. 

### Backend-as-a-service (BaaS) gives you a low-code backend with the infrastructure also pre-built 

**As-a-service** says that it is somebody else that owns the infrastructure. All you are responsible with is writing the application. 

### The two are independent and can be combined

- **Parse Platform** is **a low-code backend**. 
	- Open-source software
	- You rent a virtual machine in the cloud and install it there, or you run it on your own laptop while you are developing
	- You pay a fixed price for renting the VM 
	- Or you pay electricity for the machine in your basement / data center
- **Firebase** is a **backend-as-a-service**. 
	- Proprietary, hosted by Google
	- Renting it is the only way to have it - you pay for the usage of the firebase backend
	- However, open source alternatives exist
- **Back4App** is **backend-as-a-service** that comes with Parse pre-installed on it. 
	- Somebody else running the low-code backend you could have run yourself
	- You don't have to rent a VM
	- You just pay for the usage of the backend 

### The code you write that communicates with a Parse server, does not care whether the server is hosted on your own VM or is a service hosted by somebody else

The only thing that your code needs to know is that there's a Parse backend. And what's the URL where it can communicate with that backend. 

### It will be the same with any kind of backend. The frontend talks to a given IP address or URL. 

That backend can be running on your local machine, then you connect to `localhost:1337` e.g., or `127.0.0.1:1337`. Or you can connect to a staging server. Or to the main server. 


## Parse as a low-code backend

### Is open source
Now. It started as a startup, got bought by Facebook, and is now opened again

### The Parse server is implemented in Node
Implemented in JS. And as we've discussed in the past, you can run JS in the browser, or on any machine with the help of the `node` Javascript interpreter that does not need a browser.

### Parse has an answer for every line of the requirements of a backend 

| The backend is responsible with ... | Parse gives you                                                                          |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| Authentication                      | `Parse.User` — signup, login, sessions (*next week*)                                     |
| Authorization                       | class-level permissions and ACLs (*next week*)                                           |
| Session management                  | completely free (handled by the SDK, and remembered across page reloads)                 |
| Business logic and DB access        | the JavaScript SDK — the subject of today                                                |
| Scheduled jobs                      | cloud jobs                                                                               |
| API endpoints                       | REST and GraphQL, generated from your classes (although not needed when you use the SDK) |
| Data validation                     | cloud code triggers (*week 11*)                                                          |

And two more that were never on the list, because the browser never had them to lose: 
- **file storage**, and 
- an interactive **dashboard** for looking at and editing your database


### For your frontend/client code, Parse provides you with an easy to use Javascript SDK

SDK
- stands for (software development kit)
- is a library that makes it easy for you to communicate from the frontend to the backend
- without this SDK, you would have to communicate with the backend with the HTTP protocol, and that's more clumsy

Everything you do to Parse goes through the JavaScript SDK. There are also SDKs for other languages than JS (Kotlin for Android, Swift for iOS, etc.). 

*Note:* The full documentation of the SDK is in the [Parse.js Javascript Guide](https://docs.parseplatform.org/js/guide/#saving-objects). Use it as reference -- that is, search for things as you need them. Don't read it as a book.

Everything above is what a backend *is*. What it looks like to actually put one
under an app you have already written is the next note:
[Replacing localStorage with a Real Database](Backends-Low-Code-Backends-and-the-Parse-Platform.md).

## Exam Questions

### 1. What is the difference between front-end and back-end?

### 2. List at least 5 responsibilities of a backend.

### 3. What is Parse Platform and what does it provide?
