import {useState, useRef, useEffect} from 'react';

const CHECKBOX = "✔"
const NOT_CHECKED = "x"


function TopicsList({topics, setTopics}) {

    const [newTopic, setNewTopic] = useState("");
    const inputRef = useRef(null);

    useEffect(() => {
        inputRef.current.focus();
        console.dir(inputRef.current);
    }, []);

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


    return (
        <div>
            <form>
                <input ref={inputRef} onChange={handleNewTopicChange} value={newTopic} type="text"/>
                <button onClick={handleSubmit} type="submit">Add</button>
            </form>
            <ul>
                {topics.map((each) =>
                    <Item key={each.topic}
                          name={each.topic}
                          isDiscussed={each.isDiscussed}
                          deleteElementFunction={deleteItem}/>
                )}
            </ul>


        </div>
    )
}

function Item({name, isDiscussed, deleteElementFunction}) {


    function handleDeletePress() {
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