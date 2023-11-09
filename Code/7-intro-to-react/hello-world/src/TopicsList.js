import {useState, useRef, useEffect} from 'react';
import Parse from 'parse';


const CHECKBOX = "✔"
const NOT_CHECKED = "x"


function TopicsList({topics, setTopics}) {

    const [newTopic, setNewTopic] = useState("");
    const inputRef = useRef(null);

    useEffect(() => {
        inputRef.current.focus();
        console.dir(inputRef.current);
    }, []);


    function saveNewTopicToDB(topicName, discussedState) {
        const Topic = Parse.Object.extend("Topic");
        const topic = new Topic();

        topic.set("name", topicName);
        topic.set("isDiscussed", false);

        const successFunction = (topic) => {
            console.log("saved with id: " + topic.id);
        };
        const errorFunction = (error) => {
            console.log(error.message);
        };

        const savePromise = topic.save();
        savePromise.then(successFunction, errorFunction);

    }

    async function asyncSaveNewTopicToDB(topicName, discussedState) {
        const Topic = Parse.Object.extend("Topic");
        const topic = new Topic();

        topic.set("name", topicName);
        topic.set("isDiscussed", false);

        try {
            let savedObject = await topic.save();
            console.log("saved with id: " + savedObject.id);

        } catch (error) {
            console.log(error.message);
        }
    }

    function handleSubmit(e) {

        e.preventDefault();

        setTopics([
            {topic: newTopic, isDiscussed: false},
            ...topics
        ])

        asyncSaveNewTopicToDB(newTopic, false);
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