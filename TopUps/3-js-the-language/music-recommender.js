const SEPARATOR = " >>>> "

let good_songs = [
    {title: "Yellow Submarine", band: "The Beatles", seconds: 200},
    {title: "Smells like Teen Spirit", band: "Nirvana", seconds: 400},
    {title: "Paint It Black", band: "Rolling Stones", seconds: 200},
    {title: "Shake It Off", band: "Taylor Swift", seconds: 350}
]

function printSongNicely(song) {
    console.log(song.band + SEPARATOR + song.title)
}

let printOnlyTitle = function (song) {
    console.log(song.title);
}

let printOnlyTitleForever = function onlyTitle(song) {
    console.log(song.title);
    onlyTitle(song);
}

// for (let i = 0; i< good_songs.length; i++ ) {
//     printSongNicely(good_songs[i])
// }

function printSongsNicely(list_of_songs) {
    for (let song of list_of_songs) {
        printSongNicely(song)
    }

}

function longSongs(listOfSongs, minimum_duration) {
    let result = listOfSongs.filter(function (song) {
        return song.seconds > minimum_duration
    });
    return result;
}

let long_songs = longSongs(good_songs, 300)
printSongsNicely(long_songs)

/*
Stuff that you should try at home:
- create a function that converts the list of songs to use "duration" as a key instead of "seconds"
- create a function that adds a new song at the end of the existing list
- create a function that adds a new song, but returns a different list
 */