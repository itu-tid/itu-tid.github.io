import {useEffect, useState} from "react";

export default function Counter({name, color, size}) {

    const [clicks, setClicks] = useState(0);

    useEffect(() => {
            document.title = "Counter: "+ clicks;
            localStorage.setItem(name, JSON.stringify(clicks));
    }, [clicks]);


    function handleClick() {
        setClicks(clicks + 1);
    }

    return (
        <div style={{backgroundColor: color}  }>

            <p>
                {name} <span style={{fontSize: size}  }>{clicks}</span>
            </p>

            <button onClick={ handleClick }>Increase</button>

        </div>
    );
}