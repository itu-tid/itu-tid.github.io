# Exam Questions - Lecture 3: Web Architecture and Routing

## Conceptual Questions

### 1. Describe the three generations of web application architectures.

### 2. What is a Single Page Application (SPA) and what are its characteristics?

### 3. Why is client-side routing necessary in SPAs?

### 4. What is the difference between `<Link>` and `<a>` tags in React Router?

## Code Analysis Questions

### 5. Explain what this routing setup does:
```js
<Routes>
  <Route path="/dashboard" element={<DashboardLayout />}>
    <Route index element={<DashboardHome />} />
    <Route path="stats" element={<DashboardStats />} />
  </Route>
</Routes>
```

### 6. What does this protected route component do?
```js
function PrivateRoute({ children }) {
  const isAuthenticated = checkAuth();
  return isAuthenticated ? children : <Navigate to="/login" />;
}
```

### 7. How do you access URL parameters in React Router?
```js
// Route: <Route path="/users/:userId" element={<UserProfile />} />
// URL: /users/123
```

### 8. How do you access query string parameters?
```js
// URL: /dashboard?sort=name&filter=active
```

## Git Flow Questions

### 9. Describe the three types of branches used in the course's Git Flow model.

### 10. Why should `node_modules` be in `.gitignore`?

### 11. What happens if a user reloads the page on `/about` in an SPA?
