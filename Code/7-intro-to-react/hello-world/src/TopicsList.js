import {useState} from 'react';

const CHECKBOX = "✔"
const NOT_CHECKED = "x"


function TopicsList() {

    const [topics, setTopics] =
        useState([
            {topic: "State", isDiscussed: true},
            {topic: "Components", isDiscussed: true},
            {topic: "JSX", isDiscussed: true},
            {topic: "Conditional Rendering", isDiscussed: true},
            {topic: "Rendering Lists", isDiscussed: false},
        ]);

    const [newTopic, setNewTopic] = useState("")
    const [discussedCount, isDiscussedCount] = useState(4);

    function handleSubmit(e) {
        e.preventDefault();
        setTopics([
            {topic: newTopic, isDiscussed: false},
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
                    <Item name={each.topic} isDiscussed={each.isDiscussed} deleteElementFunction={deleteItem}/>
                </>)}
            </ul>

            <div>
                Didcussed: {discussedCount}
            </div>
        </div>
    )
}

function ItemA({name, isDiscussed}) {

    return (
        <li>
            {name} {isDiscussed && CHECKBOX}
        </li>
    )
}


function ItemB({name, isDiscussed}) {

    let checkboxString = ""
    if (isDiscussed) {
        checkboxString = CHECKBOX
    }

    return (
        <li>
            {name} {checkboxString}
        </li>
    )
}

function Item({name, isDiscussed, deleteElementFunction}) {


    function handleDeletePress(e) {
        deleteElementFunction(name);
    }


    return (
        <li>
            {name} {isDiscussed ? CHECKBOX : NOT_CHECKED}
            <button onClick={handleDeletePress}>Delete</button>
        </li>
    )
}

export {TopicsList}