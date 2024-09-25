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

            <Counter name={"Push Ups"} color={color} size={"24pt"}/>

            <Counter name={"Glasses of Water"} color={color} size={"14pt"} />

            <button onClick={
                    () => {setColor("yellow")}}
                    type="submit">Change Color</button>

        </div>
    );
}

export default App;
