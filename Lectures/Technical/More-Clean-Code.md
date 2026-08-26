# Clean Code Questions - With Examples From Your Projects

## Example #1

```js
function App() {  
  const ChatOverviewHeader = "Chats";  
  return (  
    <Router>  
      <Routes>  
        <Route path="/" element={<ChatOverview title={ChatOverviewHeader} />} /> 
        <Route path="/contactspopup" element={<PopUpContactPage />} />  
        <Route path="/contacts" element={<Contacts />} />  
		<Route path="/contactsPopUp" element={<PopUpContactPage />} />          
        <Route path="/userlogin" element={<UserLogin />} />  
      </Routes>  
    </Router>  
  );  
}
```
- Is the `title` defined where it should be?
- What is the difference between `ChatOverviewHeader` and  `ChatOverview`? Is there something about the naming conventions that is off here? 
- Is there a problem with the route definitions? 

### Rules
#### Define parameters and constants as close as possible to where they are used
#### Use a code styling convention. 
- CamelCase is for class names
- Constants and variables are lowerCase
- Sometimes constants can also be ALL_UPERCASE 
#### Follow a naming convention also for your URLs
Choose either all lowercase or camelcase


## Example #2

```js
// In ChatOverview.js
return (  
  <div>  
    <Topbar />  
    <ColumnContainer>  
      <ChatComponent isPopupVisible={isPopupVisible}/>  
    </ColumnContainer>  
  </div>  
);

// In ChatComponent.js
const ChatComponent = () => {  

// ... 

return (  
  <div>  
    <ChatContainer>  
      <NamebarTop />  
      <StyledMessageBubble>
      // ...
```
### Rules
#### Remove unused code and props


## Example 3

Q: What is the problem with the following code? 
```js
return (  
  <div>  
    <Topbar />  
    <ColumnContainer>  
      <Sidebar />  
      <SideOverview title= "Contacts" />  
              <SelectContact isVisible={isPopupVisible} onClose={togglePopup}/>  
              <BlurredComponent isBlurred={isPopupVisible}> <ChatComponent/>  
              </BlurredComponent>  
    </ColumnContainer>  
  </div>  
);

const ColumnContainer = styled.div`  
  display: flex;  width: 100vw;`;  
  
const BlurredComponent = styled.div`  
  filter: ${({ isBlurred }) => (isBlurred ? 'blur(2px)' : 'none')}; `;
  
```
### Rules
#### Use an automatic code formatter
It will make code more readable. 

#### If a style is used in multiple components, factor it out
E.g. in the project above, `ColumnContainer` is defined  four times, always the same way.





