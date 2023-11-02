import {useState} from 'react';
import {TopicsList} from "./TopicsList";
import {ProgressCounter} from "./ProgressCounter";

export function CourseOverview() {

    const [topics, setTopics] =
        useState([
            {topic: "Effects", isDiscussed: false},
            {topic: "State", isDiscussed: true},
            {topic: "Components", isDiscussed: false},
            {topic: "JSX", isDiscussed: true},
            {topic: "Conditional Rendering", isDiscussed: true},
            {topic: "Rendering Lists", isDiscussed: false},
        ]);

    return (
        <>
            <TopicsList topics={topics} setTopics={setTopics}/>
            <ProgressCounter topics={topics}/>
        </>
    )
}