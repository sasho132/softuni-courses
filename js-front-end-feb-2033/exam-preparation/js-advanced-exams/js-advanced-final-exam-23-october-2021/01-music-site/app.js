window.addEventListener('load', solve);

function solve() {
    const addBtn = document.getElementById('add-btn');
    const allHitsContainer = document.querySelector('.all-hits-container');
    const likesContainer = document.querySelector('.likes > p:nth-child(1)');
    const savedSongsContainer = document.querySelector('.saved-container');
    let likesCounter = 0;

    const inputs = {
        genre: document.getElementById('genre'),
        name: document.getElementById('name'),
        author: document.getElementById('author'),
        date: document.getElementById('date')
    }

    addBtn.addEventListener('click', addSong);

    function addSong(event) {
        event.preventDefault();

        for (let el in inputs) {
            if (inputs[el].value === '') {
                return;
            }
        }

        let currentData = {
            genre: inputs.genre.value,
            name: inputs.name.value,
            author: inputs.author.value,
            date: inputs.date.value
        }

        const songDiv = elGenerator(
            'div',
            null,
            allHitsContainer,
            null,
            ['hits-info']
        );
        const songImg = elGenerator('img', null, songDiv);
        songImg.setAttribute('src', './static/img/img.png');
        const songGenre = elGenerator('h2', `Genre: ${currentData.genre}`, songDiv);
        const songName = elGenerator('h2', `Name: ${currentData.name}`, songDiv);
        const songAuthor = elGenerator('h2', `Author: ${currentData.author}`, songDiv);
        const songDate = elGenerator('h3', `Date: ${currentData.date}`, songDiv);
        const saveBtn = elGenerator(
            'button',
            'Save song',
            songDiv,
            null,
            ['save-btn']
        );
        const likeBtn = elGenerator(
            'button',
            'Like song',
            songDiv,
            null,
            ['like-btn']
        );
        const deleteBtn = elGenerator(
            'button',
            'Delete',
            songDiv,
            null,
            ['delete-btn']
        );

        for (let el in inputs) {
            inputs[el].value = '';
        }

        likeBtn.addEventListener('click', likeSong);
        saveBtn.addEventListener('click', saveSong);
        deleteBtn.addEventListener('click', deleteSong);

        function saveSong() {
            savedSongsContainer.appendChild(this.parentNode);

            let likeBtn = savedSongsContainer.querySelector('.like-btn');
            let saveBtn = savedSongsContainer.querySelector('.save-btn');

            likeBtn.remove();
            saveBtn.remove();
        }

        function likeSong() {
            likesCounter++;
            likesContainer.textContent = `Total Likes: ${likesCounter}`;
            this.disabled = true;
        }

        function deleteSong() {
            let elForDelete = this.parentNode;
            likesCounter--;
            likesContainer.textContent = `Total Likes: ${likesCounter}`;
            elForDelete.remove();
        }
    }

    function elGenerator(type, content, parent, id, classes) {
        const htmlElement = document.createElement(type);
        if (content && type !== "input") {
            htmlElement.textContent = content;
        }
    
        if (content && type === "input") {
            htmlElement.value = content;
        }
    
        if (id) {
            htmlElement.id = id;
        }
    
        if (classes) {
            htmlElement.classList.add(...classes);
        }
    
        if (parent) {
            parent.appendChild(htmlElement);
        }
    
        return htmlElement;
    }
}