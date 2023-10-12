import {PackingList} from './PackingList.js'

function App() {

    let user = "TID Hacker"
    let date = Date();
    let titleStyle = {
        fontWeight: 100
    };

    return (
        <>
            <h1 className="fancyHeader">Hello {user}!</h1>
            <br/>
            <h3>Date: {date}</h3>
            <p>By the end of this lecture you'll be know about</p>
            <PackingList/>
        </>
    );
}

export default App;
