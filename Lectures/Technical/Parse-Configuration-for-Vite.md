# Parse SDK Configuration for Vite

If you're using the Parse SDK with Vite, you need to update your `vite.config.js` file to avoid runtime errors.

## The Problem

You may encounter this error when importing Parse:

```
Uncaught TypeError: Super expression must either be null or a function
```

This happens because Vite doesn't handle Parse's class inheritance correctly by default.

## The Solution

Update your `vite.config.js` to redirect Parse imports to the pre-built distribution.


```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  
  // Tell Vite that when we refer to "parse" we talk about the minified version
  resolve: {
    alias: {
      parse: "parse/dist/parse.min.js",
    },
  }
})
```

- **`resolve.alias`**: Redirects `import Parse from "parse"` to use the pre-built minified version

## One other performance configuration

While you're at it, also add the `optimizeDeps` key to tell Vite to load parse at dev server startup for faster performance during development. 
```js

export default defineConfig({
  plugins: [react()],
  
  // Tell Vite that when we refer to "parse" we talk about the minified version
  resolve: {
    alias: {
      parse: "parse/dist/parse.min.js",
    },
    
  // Beter performance during development 
  optimizeDeps: {
    include: ["parse"],
  },
  }
})

```

**See example here:** [https://github.com/itu-tid/todo-25/blob/main/vite.config.js](https://github.com/itu-tid/todo-25/blob/main/vite.config.js)

