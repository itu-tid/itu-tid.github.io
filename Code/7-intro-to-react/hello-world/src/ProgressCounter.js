export function ProgressCounter({topics}) {

    const discussedTopics = topics.filter(each => each.isDiscussed);
    const discussedCount = discussedTopics.length;

    return (
        <div>
            Discussed: {discussedCount}
        </div>
    )
}