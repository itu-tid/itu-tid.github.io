- Browsers expose the `beforeunload`event where you can do cleanup before page closes
- This includes a refresh


```js
useEffect(() => {
	const handleBeforeUnload = () => {
		// If there's an active timer, stop it to save the accumulated time
		if (activeElementId) {
			handleStopTimer(activeElementId);
		}
	};
	
	window.addEventListener("beforeunload", handleBeforeUnload);
	return () => window.removeEventListener("beforeunload", handleBeforeUnload);

}, [activeElementId]);
```

