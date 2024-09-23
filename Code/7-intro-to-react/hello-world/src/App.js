import Counter  from "./Counter";
import {useState} from "react";

function App() {

    const [color, setColor] = useState("lightBlue");

    return (
        <div>
            <h1 >
                Hi from React
            </h1>

            <br />

            <Counter color={color} size={"24pt"}/>

            <Counter color={color} size={"14pt"} />

            <button onClick={
                    () => {setColor("yellow")}}
                    type="submit">Change Color</button>

        </div>
    );
}

export default App;
