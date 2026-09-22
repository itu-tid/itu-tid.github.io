# Code Organization

- If you implement a reusable component, put it in a /components folder
- Put screens in the /pages (or /screens) folder
- When you have more than one component to implement a bigger one, group them in a folder
- If you use styled components keep the associated style file adjacent to each component



## A folder structure to start from

### Separate Pages and Reusable Components 

My favorite way of organizing
- **pages**  -- One file per page/view
- **components** -- Reusable UI components
- **services** -- API/backend logic
- **utilities** -- a catch all for things that we don't know where to put yet

```bash
  src/
  ├── assets/       
  ├── pages/              
  │   ├── LoginPage.jsx
  │   └── HomePage.jsx
  ├── components/         
  │   ├── TodoList/    
  │   │   ├── TodoList.jsx
  │   │   ├── TodoItem.jsx
  ├── services/           
  │   ├── authService.js
  │   └── todoService.js
  ├── constants/
  ├── utilities/
  └── App.jsx

```

Also, refactor, refactor, refactor. When you find a better organization, go with that.
