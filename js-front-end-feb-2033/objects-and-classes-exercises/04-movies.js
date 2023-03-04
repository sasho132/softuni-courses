function movies(arr) {
    let movies = [];

    for (let movie of arr) {
        let currentLine = movie.split(" ");
        let addMovieIndex = currentLine.findIndex((el) => el === "addMovie");
        let directedByIndex = currentLine.findIndex(
            (el) => el === "directedBy"
        );
        let onDateIndex = currentLine.findIndex((el) => el === "onDate");

        if (addMovieIndex >= 0) {
            currentMovie = {};
            currentLine.shift();
            currentMovie["name"] = currentLine.join(" ");
            movies.push(currentMovie);
        } else if (directedByIndex >= 0) {
            let movieName = currentLine.slice(0, directedByIndex).join(" ");
            let director = currentLine
                .slice(directedByIndex + 1, currentLine.length + 1)
                .join(" ");

            for (let m of movies) {
                if (m["name"] === movieName) {
                    m["director"] = director;
                }
            }
        } else if (onDateIndex >= 0) {
            let movieName = currentLine.slice(0, onDateIndex).join(" ");
            let onDate = currentLine
                .slice(onDateIndex + 1, currentLine.length + 1)
                .join(" ");

            for (let m of movies) {
                if (m["name"] === movieName) {
                    m["date"] = onDate;
                }
            }
        }
    }

    let filteredMovies = movies.filter(obj => Object.entries(obj).length === 3)

    filteredMovies.forEach(el => {
        console.log(JSON.stringify(el))
    });
}

movies([
    "addMovie Fast and Furious",
    "addMovie Godfather",
    "Inception directedBy Christopher Nolan",
    "Godfather directedBy Francis Ford Coppola",
    "Godfather onDate 29.07.2018",
    "Fast and Furious onDate 30.07.2018",
    "Batman onDate 01.08.2018",
    "Fast and Furious directedBy Rob Cohen",
]);
