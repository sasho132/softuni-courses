function attachEvents() {
    const loadBtn = document.getElementById("loadBooks");
    const tableBody = document.querySelector(
        "body > table:nth-child(2) > tbody:nth-child(2)"
    );
    const BASE_URL = `http://localhost:3030/jsonstore/collections/books/`;
    const formTitle = document.querySelector("#form > h3:nth-child(1)");
    const titleInput = document.querySelector("#form > input:nth-child(3)");
    const authorInput = document.querySelector("#form > input:nth-child(5)");
    const submitBtn = document.querySelector("#form > button:nth-child(6)");
    let allBooks = {};

    loadBtn.addEventListener("click", loadBooks);
    submitBtn.addEventListener("click", submitBook);

    async function loadBooks() {
        try {
            const getBooks = await fetch(BASE_URL);
            const booksData = await getBooks.json();
            allBooks = booksData;

            tableBody.innerHTML = "";

            Object.entries(booksData).forEach((book) => {
                let author = book[1].author;
                let title = book[1].title;
                let id = book[0];
                let tr = document.createElement("tr");
                let titleTd = document.createElement("td");
                titleTd.textContent = title;
                let authorTd = document.createElement("td");
                authorTd.textContent = author;
                let buttonsTd = document.createElement("td");
                let editBtn = document.createElement("button");
                editBtn.textContent = "Edit";
                editBtn.id = id;
                let deleteBtn = document.createElement("button");
                deleteBtn.textContent = "Delete";
                deleteBtn.id = id;
                buttonsTd.append(editBtn, deleteBtn);
                tr.append(titleTd, authorTd, buttonsTd);
                editBtn.addEventListener("click", editBook);
                deleteBtn.addEventListener("click", deleteBook);

                tableBody.appendChild(tr);
            });
        } catch (err) {
            console.log(err);
        }
    }

    function editBook() {
        formTitle.textContent = "Edit FORM";
        submitBtn.textContent = "Save";
        currentBookId = this.id;
        titleInput.value = allBooks[currentBookId].title;
        authorInput.value = allBooks[currentBookId].author;
    }

    function deleteBook() {
        const currentBookId = this.id;
        const httpHeaders = {
            method: "delete",
        };

        fetch(`${BASE_URL}${currentBookId}`, httpHeaders)
            .then((res) => res.json())
            .then(loadBooks())
            .catch((err) => {
                console.log(err);
            });
    }

    function submitBook() {
        let url = BASE_URL;
        let author = authorInput.value;
        let title = titleInput.value;
        let httpHeaders = {
            method: "post",
            body: JSON.stringify({ author, title }),
        };
        if (formTitle.textContent === "Edit FORM") {
            httpHeaders.method = "put";
            url += currentBookId;
        }
        fetch(url, httpHeaders)
            .then((res) => res.json)
            .then((authorInput.value = ""))
            .then((titleInput.value = ""))
            .then(loadBooks())
            .catch((err) => {
                console.log(err);
            });
    }
}

attachEvents();
