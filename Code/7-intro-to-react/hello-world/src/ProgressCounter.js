import {useEffect} from 'react';

export function ProgressCounter({topics}) {

    const discussedTopics = topics.filter(each => each.isDiscussed);
    const discussedCount = discussedTopics.length;

    useEffect(
        () => {
            console.log("every render!");
            document.title = "Course Progress " + discussedCount;
        }
    );


    return (
        <div>
            Discussed: {discussedCount}
        </div>
    )
}