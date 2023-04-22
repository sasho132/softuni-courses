function attachEvents() {
    const BASE_URL = "http://localhost:3030/jsonstore/tasks/";
    const cursesList = document.getElementById("list");
    const loadCursesBtn = document.getElementById("load-course");
    const addCurseBtn = document.getElementById("add-course");
    const editCurseBtn = document.getElementById("edit-course");

    const inputs = {
        curseName: document.getElementById("course-name"),
        curseType: document.getElementById("course-type"),
        description: document.getElementById("description"),
        teacherName: document.getElementById("teacher-name"),
    };

    loadCursesBtn.addEventListener("click", loadCurses);
    addCurseBtn.addEventListener("click", addCourse);

    function loadCurses() {
        editCurseBtn.disabled = true;
        cursesList.textContent = '';

        fetch(BASE_URL)
            .then((res) => res.json())
            .then((data) => {
                Object.values(data).forEach((obj) => {
                    let title = obj.title;
                    let type = obj.type;
                    let description = obj.description;
                    let teacher = obj.teacher;
                    let id = obj._id;

                    const divContainer = document.createElement("div");
                    divContainer.classList.add("container");
                    divContainer.id = id;
                    cursesList.appendChild(divContainer);
                    const taskTitle = document.createElement("h2");
                    taskTitle.textContent = `${title}`;
                    divContainer.appendChild(taskTitle);
                    const taskTeacher = document.createElement("h3");
                    taskTeacher.textContent = `${teacher}`;
                    divContainer.appendChild(taskTeacher);
                    const taskType = document.createElement("h3");
                    taskType.textContent = `${type}`;
                    divContainer.appendChild(taskType);
                    const taskDesc = document.createElement("h4");
                    taskDesc.textContent = `${description}`;
                    divContainer.appendChild(taskDesc);

                    const editBtn = document.createElement("button");
                    editBtn.textContent = "Edit Course";
                    editBtn.classList.add("edit-btn");
                    divContainer.appendChild(editBtn);
                    const finishBtn = document.createElement("button");
                    finishBtn.textContent = "Finish Course";
                    finishBtn.classList.add("finish-btn");
                    divContainer.appendChild(finishBtn);

                    editBtn.addEventListener('click', edit);
                    finishBtn.addEventListener('click', finish);

                    function edit() {
                        let id = this.parentNode.id;
                        let course = document.getElementById(id);
                
                        inputs.curseName.value = title;
                        inputs.curseType.value = type;
                        inputs.description.value = description;
                        inputs.teacherName.value = teacher;

                        addCurseBtn.disabled = true;
                        editCurseBtn.disabled = false;

                        editCurseBtn.addEventListener('click', editCourse);

                        course.remove();
                    }

                    function finish() {
                        let currentid = this.parentNode.id;
                        console.log(currentid);
                        fetch(`${BASE_URL}${currentid}`, {
                            method: 'DELETE'
                        })
                        .then(() => loadCurses())
                        .catch((err) => console.error(err));
                    }

                    function editCourse() {

                        let data = {
                            title: inputs.curseName.value,
                            type: inputs.curseType.value,
                            description: inputs.description.value,
                            teacher: inputs.teacherName.value,
                        };
                
                        fetch(`${BASE_URL}${id}`, {
                            method: "PUT",
                            body: JSON.stringify(data),
                        })
                            .then(() => loadCurses())
                            .then(() =>
                                Object.keys(inputs).forEach((el) => {
                                    inputs[el].value = "";
                                })
                            )
                            .then(() => addCurseBtn.disabled = false)
                            .catch((err) => console.error(err));
                    }
                });
            });
    }

    function addCourse() {
        for (let el in inputs) {
            if (inputs[el].value === "") {
                return;
            }
        }

        let validTypesList = ["Long", "Medium", "Short"];

        if (!validTypesList.includes(inputs.curseType.value)) {
            return;
        }

        let data = {
            title: inputs.curseName.value,
            type: inputs.curseType.value,
            description: inputs.description.value,
            teacher: inputs.teacherName.value,
        };

        fetch(BASE_URL, {
            method: "POST",
            body: JSON.stringify(data),
        })
            .then(() => loadCurses())
            .then(() =>
                Object.keys(inputs).forEach((el) => {
                    inputs[el].value = "";
                })
            )
            .catch((err) => console.error(err));
    }

    
}

attachEvents();
