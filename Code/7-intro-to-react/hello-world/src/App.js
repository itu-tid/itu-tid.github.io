import {CourseOverview} from "./CourseOverview";
import {Link} from 'react-router-dom';

function App() {

    let user = "TID Hacker"
    let date = Date();
    let titleStyle = {
        fontWeight: 100
    };

    return (
        <>
            <h1 className="fancyHeader">Hello {user}!</h1>
            <Link to="about">About</Link> |

            <br/>
            <h3>Date: {date}</h3>
            <p>By the end of this lecture you'll be know about</p>

            <CourseOverview/>
        </>
    );
}

export default App;
