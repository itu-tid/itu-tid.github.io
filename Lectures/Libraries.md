
# Libraries


# You must add all the libraries on which you  depend to the `packages.js` 

Under the `dependencies` key.

### The libraries are normally  specified with their version number 

### Version numbers respect the [semantic versioning](https://docs.npmjs.com/about-semantic-versioning) convention
- major
- minor
- patch


# When you clone  a project, you always run `npm install` to install the required libraries

This is the way you can share your dependencies with your colleagues

# React creates a `pacakages.lock` file 
- this one you don't commit to the repo normally  - it's generated
- unless you want to ensure 100% replicability of all the dependencies 

# Locally the libraries you install are saved in the `node_modules` folder
- that one you NEVER want to commit to git 




# Questions to know

- How do you instal dependencies with `npm`? What do you do to make sure that your colleagues also use the same dependency that you are using?
- When do you have to run `nmp install`?
- What is the `node_modules` folder good for? Should you add it  to version control? Why or why not? 
- Why do we list dependencies in `packages.json`?
- What is the meaning of the version numbers in `packages.json`? 
- Why do we need `package-lock.json`? Do we commit it to GH?