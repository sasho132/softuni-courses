window.addEventListener("load", solve);

function solve() {
    const firstName = document.getElementById("first-name");
    const lastName = document.getElementById("last-name");
    const age = document.getElementById("age");
    const storyTitle = document.getElementById("story-title");
    const genre = document.getElementById("genre");
    const storyText = document.getElementById("story");
    const publishButton = document.getElementById("form-btn");
    const previewList = document.getElementById("preview-list");

    publishButton.addEventListener("click", publish);

    function publish(e) {
        if (
            firstName.value === '' ||
            lastName.value === '' ||
            age.value === '' ||
            storyTitle.value === '' ||
            storyText.value === ''
        ) {
            return;
        }

        const storyInfo = document.createElement("li");
        storyInfo.classList.add("story-info");
        const storyArticle = document.createElement("article");
        storyInfo.appendChild(storyArticle);
        previewList.appendChild(storyInfo);

        let nameP = document.createElement("h4");
        let ageP = document.createElement("p");
        let titleP = document.createElement("p");
        let genreP = document.createElement("p");
        let textP = document.createElement("p");
        let saveBtn = document.createElement("button");
        let editBtn = document.createElement("button");
        let deleteBtn = document.createElement("button");
        saveBtn.classList.add("save-btn");
        editBtn.classList.add("edit-btn");
        deleteBtn.classList.add("delete-btn");

        storyArticle.appendChild(nameP);
        storyArticle.appendChild(ageP);
        storyArticle.appendChild(titleP);
        storyArticle.appendChild(genreP);
        storyArticle.appendChild(textP);

        storyInfo.appendChild(saveBtn);
        storyInfo.appendChild(editBtn);
        storyInfo.appendChild(deleteBtn);

        nameP.textContent = `Name: ${firstName.value} ${lastName.value}`;
        ageP.textContent = `Age: ${age.value}`;
        titleP.textContent = `Title: ${storyTitle.value}`;
        genreP.textContent = `Genre: ${genre.value}`;
        textP.textContent = storyText.value;
        saveBtn.textContent = "Save Story";
        editBtn.textContent = "Edit Story";
        deleteBtn.textContent = "Delete Story";

        let infoFirstName = firstName.value;
        let infoLastName = lastName.value;
        let infoAge = age.value;
        let infoTitle = storyTitle.value;
        let infoGenre = genre.value;
        let infoText = storyText.value;

        e.currentTarget.disabled = true;
        firstName.value = "";
        lastName.value = "";
        storyTitle.value = "";
        age.value = "";
        storyText.value = "";

        saveBtn.addEventListener("click", saveStory);
        editBtn.addEventListener("click", editStory);
        deleteBtn.addEventListener("click", deleteStory);

        function saveStory() {
            const message = document.createElement("h1");
            message.textContent = "Your scary story is saved!";
            const mainDiv = document.getElementById("main");
            const wrapperDiv = document.querySelector(".form-wrapper");
            const sideWrapper = document.querySelector("#side-wrapper");
            mainDiv.removeChild(wrapperDiv);
            mainDiv.removeChild(sideWrapper);
            mainDiv.appendChild(message);
        }

        function editStory() {
            firstName.value = infoFirstName;
            lastName.value = infoLastName;
            age.value = infoAge;
            storyTitle.value = infoTitle;
            genre.value = infoGenre;
            storyText.value = infoText;
            publishButton.disabled = false;

            previewList.removeChild(storyInfo);
        }

        function deleteStory() {
            publishButton.disabled = false;
            previewList.removeChild(storyInfo);
        }
    }
}
