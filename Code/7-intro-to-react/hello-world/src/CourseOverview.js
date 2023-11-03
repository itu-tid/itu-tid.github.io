import {useState} from 'react';
import {TopicsList} from "./TopicsList";
import {ProgressCounter} from "./ProgressCounter";
import {useEffect} from "react";

export function CourseOverview() {

    const [topics, setTopics] =
        useState([]);

    // run on every change to the topics variable
    useEffect(() => {
        if (topics.length > 0) {
            localStorage.setItem("topics", JSON.stringify(topics));
        }
    }, [topics]);

    // run on the first render
    useEffect(() => {
        setTopics(JSON.parse(localStorage.getItem("topics")));
    }, []);

    // run on every render
    useEffect(() => {
        // setTopics(JSON.parse(localStorage.getItem("topics")));
        console.log("a new render");
    });


    useEffect(() => {
        let interval = setInterval(() => {
            console.log("hello")
        }, 1000)

        return () => {
            clearInterval(interval) // clear the interval in the returning function
        }
    }, [])

    return (
        <>
            <TopicsList topics={topics} setTopics={setTopics}/>
            <ProgressCounter topics={topics}/>
        </>
    )
}