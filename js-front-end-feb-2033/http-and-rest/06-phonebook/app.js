function attachEvents() {
    const phoneBookList = document.getElementById("phonebook");
    const loadBtn = document.getElementById("btnLoad");
    const createBtn = document.getElementById("btnCreate");
    const personInput = document.getElementById("person");
    const phoneInput = document.getElementById("phone");
    const BASE_URL = `http://localhost:3030/jsonstore/phonebook/`;

    loadBtn.addEventListener("click", loadContacts);
    createBtn.addEventListener("click", createContact);

    async function loadContacts() {
        try {
            const phoneBookData = await fetch(BASE_URL);
            const phoneBookContacts = await phoneBookData.json();
            phoneBookList.innerHTML = '';
            Object.values(phoneBookContacts).forEach((el) => {
                let person = el.person;
                let phone = el.phone;
                let li = document.createElement("li");
                let deleteBtn = document.createElement("button");
                deleteBtn.textContent = "Delete";
                deleteBtn.id = el._id;
                deleteBtn.addEventListener("click", deleteFromPhoneBook);
                li.textContent = `${person}: ${phone}`;
                li.appendChild(deleteBtn);
                phoneBookList.appendChild(li);
            });
        } catch (err) {
            console.log(err);
        }
    }

    function createContact() {
        let person = personInput.value;
        let phone = phoneInput.value;
        let htmlHeaders = {
            method: "post",
            body: JSON.stringify({ person, phone }),
        };
        fetch(BASE_URL, htmlHeaders)
            .then((res) => res.json())
            .then(personInput.value = "")
            .then(phoneInput.value = "")
            .then(loadContacts())
            .catch((err) => {
                console.log(err);
            })
    }

    function deleteFromPhoneBook() {
        const id = this.id;
        const httpHeaders = {
            method: "delete"
        };

        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then((res) => res.json())
            .then(loadContacts())
            .catch((err) => {
                console.log(err);
            })
    }
}

attachEvents();
