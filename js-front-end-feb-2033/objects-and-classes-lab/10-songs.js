function songs(songsArr) {
    let numberOfSongs = songsArr.shift();
    let songs = [];
    let songType = songsArr.pop();

    class Song {
        constructor(type, name, time) {
            this.type = type;
            this.name = name;
            this.time = time;
        }
    }

    for (let currentSong of songsArr) {
        let [type, name, time] = currentSong.split("_");
        let song = new Song(type, name, time);
        songs.push(song);
    }

    if (songType === "all") {
        songs.forEach((s) => console.log(s.name));
    } else {
        let sortedSongs = songs.filter((s) => s.type === songType);
        sortedSongs.forEach((s) => console.log(s.name));
    }
}

songs([
    3,
    "favourite_DownTown_3:14",
    "favourite_Kiss_4:16",
    "favourite_Smooth Criminal_4:01",
    "favourite",
]);
