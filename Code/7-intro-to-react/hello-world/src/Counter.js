import {useState} from "react";

export default function Counter({color, size}) {

    const [clicks, setClicks] = useState(0);

    function handleClick() {
        setClicks(clicks +1)
    }

    return (
        <div style={{backgroundColor: color}  }>

            <p>
                Button has been clicked <span style={
                        {fontSize: size}  }>{clicks}</span>
            </p>

            <button onClick={ handleClick }>Click me!</button>

        </div>
    );
}