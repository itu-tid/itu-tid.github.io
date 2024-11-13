# Styling

## Separate the style for a component in a separate file
Do not use inline styling. This promotes the separation of concerns.


## Do not hardcode colors ad hoc 
Separate the definition of your colors in a colors file. This allows reuse. And keeps the unity of the design if the same colors are used across the application. 


# Javascript

## Favor named functions to lambda expressions when possible
This increases the readability of the code

# React

## Extract repetitive patterns into a separate components
e.g. the two patterns below are too repetitive; they should be factored out in a separate component
<img width="778" alt="image" src="https://github.com/user-attachments/assets/c0417216-c537-474b-b64e-9c039a2f86e6">
<img width="822" alt="image" src="https://github.com/user-attachments/assets/85b15686-71c7-4dcd-9203-36a6877634e4">
