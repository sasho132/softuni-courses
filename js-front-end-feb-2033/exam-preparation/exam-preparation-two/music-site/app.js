window.addEventListener("load", solve);

function solve() {
    const genre = document.getElementById("genre");
    const name = document.getElementById("name");
    const author = document.getElementById("author");
    const date = document.getElementById("date");
    const addBtn = document.getElementById("add-btn");
    const allHitsContainer = document.querySelector(".all-hits-container");

    addBtn.addEventListener("click", addSong);

    function addSong(e) {
        e.preventDefault();
        if (
            genre.value === "" ||
            name.value === "" ||
            author.value === "" ||
            date.value === ""
        ) {
            return;
        }

        let infoGenre = genre.value;
        let infoName = name.value;
        let infoAuthor = author.value;
        let infoDate = date.value;

        let hitsInfo = document.createElement("div");
        hitsInfo.classList.add("hits-info");
        
        hitsInfo.innerHTML = `<img src="./static/img/img.png">
        <h2>Genre: ${infoGenre}</h2>
        <h2>Name: ${infoName}</h2>
        <h2>Author: ${infoAuthor}</h2>
        <h3>Date: ${infoDate}</h3>
        <button class="save-btn">Save song</button>
        <button class="like-btn">Like song</button>
        <button class="delete-btn">Delete</button>`;
        let likeBtn = hitsInfo.querySelector('.like-btn');
        let saveBtn = hitsInfo.querySelector('.save-btn');
        let deleteBtn = hitsInfo.querySelector('.delete-btn');
        likeBtn.addEventListener("click", likeSong);
        saveBtn.addEventListener("click", saveSong);
        deleteBtn.addEventListener("click", deleteSong);
        allHitsContainer.appendChild(hitsInfo);
        
        genre.value = "";
        name.value = "";
        author.value = "";
        date.value = "";

        function likeSong(e) {
            const likesDiv = document.querySelector(".likes");
            let totalLikesP = likesDiv.children[0];
            let splitText = totalLikesP.textContent.split(": ");
            let likes = Number(splitText[1]);
            likes++;
            totalLikesP.textContent = splitText[0] + ": " + likes;

            e.currentTarget.disabled = true;
        }

        function saveSong() {
            const savedContainer = document.querySelector(".saved-container");
            savedContainer.appendChild(hitsInfo);
            saveBtn.remove();
            likeBtn.remove();
            allHitsContainer.removeChild(hitsInfo);
        }

        function deleteSong() {
            hitsInfo.remove();
        }
    }
}
