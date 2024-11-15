# Clean Code

To make your code more maintainable, and your life easier, here are some rules that we want you to follow in TID. This is a living document, so as we discover new rules we add them here.





# General

## Avoid copy-pasting code that you don't understand

Why?
- The code will become a *big ball of mud and bugs* if you just add stuff in there that was generated without you understanding it. 
- You upset the code reviewers...

As a rule of thumb, code generation is useful as a reminder of something that you knew before, something that you understand and just forgot. 

How do we know that it's generated code?
- your code is using class components -- which is archaic
- your code is using redundant comments -- no human would waste time to belabor the obvious
- your code is using unnecessary specifications -- e.g. `z-index: 1000` in a project where `z-index` is never used elsewhere





# Styling

## Separate the style for a component in a separate file
- Do not use inline styling. 
- This promotes the separation of concerns and reusability. 


## Do not hardcode colors ad hoc 
Separate the definition of your colors in a colors file. This allows reuse. And keeps the unity of the design if the same colors are used across the application. 



# Javascript - The Language

## Favor named functions to lambda expressions when possible
This increases the readability of the code


# React

## Keep components small
- examples 
- counter-example: show 

## Extract repetitive patterns into a separate components
e.g. the two patterns below are too repetitive; they should be factored out in a separate component
<img width="778" alt="image" src="https://github.com/user-attachments/assets/c0417216-c537-474b-b64e-9c039a2f86e6">
<img width="822" alt="image" src="https://github.com/user-attachments/assets/85b15686-71c7-4dcd-9203-36a6877634e4">
