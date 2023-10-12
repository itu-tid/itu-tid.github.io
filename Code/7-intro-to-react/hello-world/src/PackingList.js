import {useState} from 'react';

const CHECKBOX = "✔"
const NOT_CHECKED = "x"


function PackingList() {

    let topics = [
        {topic: "Components", isPacked: true},
        {topic: "JSX", isPacked: true},
        {topic: "Conditional Rendering", isPacked: true},
        {topic: "Rendering Lists", isPacked: false},
    ]

    const [newTopic, setNewTopic] = useState("...")

    function handleSubmit(e) {
        e.preventDefault();
    }

    function handleNewTopicChange(e) {
        setNewTopic(e.target.value);
    }

    return (
        <div>
            <form>
                <input onChange={handleNewTopicChange} value={newTopic} type="text"/>
                <button onClick={handleSubmit} type="submit">Add</button>
            </form>
            <ul>
                {topics.map(each => <>
                    <Item name={each.topic} isPacked={each.isPacked}/>
                </>)}
            </ul>
        </div>
    )
}

function ItemA({name, isPacked}) {

    return (
        <li>
            {name} {isPacked && CHECKBOX}
        </li>
    )
}


function ItemB({name, isPacked}) {

    let checkboxString = ""
    if (isPacked) {
        checkboxString = CHECKBOX
    }

    return (
        <li>
            {name} {checkboxString}
        </li>
    )
}

function Item({name, isPacked}) {

    const [clicks, setClicks] = useState(0);

    function handleDeletePress(e) {
        // clicks += 1
        setClicks(clicks + 1)
    }

    // if (clicks > 2) {
    //     return null;
    // }

    return (
        <li>
            {name} {isPacked ? CHECKBOX : NOT_CHECKED}
            <button onClick={handleDeletePress}>Delete ({clicks})</button>
        </li>
    )
}

export {PackingList}