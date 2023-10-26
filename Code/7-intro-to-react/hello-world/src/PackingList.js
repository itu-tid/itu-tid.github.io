import {useState} from 'react';

const CHECKBOX = "✔"
const NOT_CHECKED = "x"


function PackingList() {

    const [topics, setTopics] =
        useState([
            {topic: "Components", isPacked: true},
            {topic: "JSX", isPacked: true},
            {topic: "Conditional Rendering", isPacked: true},
            {topic: "Rendering Lists", isPacked: false},
        ]);

    const [newTopic, setNewTopic] = useState("")

    function handleSubmit(e) {
        e.preventDefault();
        setTopics([
            {topic: newTopic, isPacked: false},
            ...topics
        ])
    }

    function deleteItem(topicName) {
        let newList = topics.filter(e => e.topic !== topicName);
        setTopics(newList)
    }

    function handleNewTopicChange(e) {
        setNewTopic(e.target.value);
    }

    console.log("component was called");

    return (
        <div>
            <form>
                <input onChange={handleNewTopicChange} value={newTopic} type="text"/>
                <button onClick={handleSubmit} type="submit">Add</button>
            </form>
            <ul>
                {topics.map(each => <>
                    <Item name={each.topic} isPacked={each.isPacked} deleteElementFunction={deleteItem}/>
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

function Item({name, isPacked, deleteElementFunction}) {


    function handleDeletePress(e) {
        deleteElementFunction(name);
    }


    return (
        <li>
            {name} {isPacked ? CHECKBOX : NOT_CHECKED}
            <button onClick={handleDeletePress}>Delete</button>
        </li>
    )
}

export {PackingList}