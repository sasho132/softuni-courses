async function attachEvents() {
    const submitBtn = document.getElementById("submit");
    const tableBody = document.querySelector("#results > tbody:nth-child(2)");
    const BASE_URL = `http://localhost:3030/jsonstore/collections/students`;

    const firstNameInput = document.querySelector(".inputs > input:nth-child(1)");
    const lastNameInput = document.querySelector(".inputs > input:nth-child(2)");
    const facultyNumberInput = document.querySelector(".inputs > input:nth-child(3)");
    const gradeInput = document.querySelector(".inputs > input:nth-child(4)");

    submitBtn.addEventListener("click", submitStudent);

    try {
        let studentsData = await fetch(BASE_URL);
        let students = await studentsData.json();
        tableBody.innerHTML = "";
        Object.values(students).forEach((el) => {
            const firstName = el.firstName;
            const lastName = el.lastName;
            const facultyNumber = el.facultyNumber;
            const grade = el.grade;

            let tableRow = document.createElement("tr");
            let firstNameTd = document.createElement("td");
            firstNameTd.textContent = firstName;
            let lastNameTd = document.createElement("td");
            lastNameTd.textContent = lastName;
            let facultyNumberTd = document.createElement("td");
            facultyNumberTd.textContent = facultyNumber;
            let gradeTd = document.createElement("td");
            gradeTd.textContent = grade;

            tableRow.append(firstNameTd, lastNameTd, facultyNumberTd, gradeTd);
            tableBody.appendChild(tableRow);
        });
    } catch (err) {
        console.log(err);
    }

    function submitStudent() {
        let firstName = firstNameInput.value;
        let lastName = lastNameInput.value;
        let facultyNumber = facultyNumberInput.value;
        let grade = gradeInput.value;

        if (
            firstName === "" ||
            lastName === "" ||
            facultyNumber === "" ||
            grade === ""
        ) {
            return;
        }

        let htmlHeaders = {
            method: "post",
            body: JSON.stringify({
                firstName,
                lastName,
                facultyNumber,
                grade,
            }),
        };
        fetch(BASE_URL, htmlHeaders)
            .then((res) => res.json())
            .then((firstNameInput.value = ""))
            .then((lastNameInput.value = ""))
            .then((facultyNumberInput.value = ""))
            .then((gradeInput.value = ""))
            .catch((err) => {
                console.log(err);
            });
    }
}

attachEvents();
