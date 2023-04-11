window.addEventListener("load", solve);

function solve() {
    const tasksSection = document.getElementById("tasks-section");
    const totalSprintPoints = document.getElementById("total-sprint-points");
    const taskIdContainer = document.getElementById('task-id');
    const createTaskBtn = document.getElementById("create-task-btn");
    const deleteTaskBtn = document.getElementById("delete-task-btn");

    let totalPoints = 0;
    let taskNumber = 0;

    let estimationPoints = {};

    const inputs = {
        title: document.getElementById("title"),
        description: document.getElementById("description"),
        label: document.getElementById("label"),
        points: document.getElementById("points"),
        assignee: document.getElementById("assignee"),
    };

    createTaskBtn.addEventListener("click", createTask);

    function createTask(event) {
        event.preventDefault();

        for (let input in inputs) {
            if (inputs[input].value === "") {
                return;
            }
        }

        taskNumber++;

        const currentTask = {
            title: inputs.title.value,
            description: inputs.description.value,
            label: inputs.label.value,
            points: inputs.points.value,
            assignee: inputs.assignee.value,
        };

        const taskData = {
            feature: { name: "Feature", icon: "⊡", class: "feature" },
            lowPriorityBug: {
                name: "Low Priority Bug",
                icon: "☉",
                class: "low-priority",
            },
            highPriorityBug: {
                name: "High Priority Bug",
                icon: "⚠",
                class: "high-priority",
            },
        };

        let taskId = `task-${taskNumber}`;
        estimationPoints[taskId] = currentTask.points;
        let icon;
        let labelName;
        for (let el in taskData) {
            if (taskData[el].name === currentTask.label) {
                icon = taskData[el].icon;
                labelName = taskData[el].class;
            }
        }

        const article = elGenerator(
            "article",
            null,
            tasksSection,
            taskId,
            ["task-card"]
        );
        const labelDiv = elGenerator(
            "div",
            `${currentTask.label} ${icon}`,
            article,
            null,
            ["task-card-label", `${labelName}`]
        );
        const title = elGenerator("h3", `${currentTask.title}`, article, null, [
            "task-card-title",
        ]);
        const descP = elGenerator(
            "p",
            `${currentTask.description}`,
            article,
            null,
            ["task-card-description"]
        );
        const pointsDiv = elGenerator(
            "div",
            `Estimated at ${currentTask.points} pts`,
            article,
            null,
            ["task-card-points"]
        );
        const assigneeDiv = elGenerator(
            "div",
            `Assigned to: ${currentTask.assignee}`,
            article,
            null,
            ["task-card-assignee"]
        );
        const actionsDiv = elGenerator("div", null, article, null, [
            "task-card-actions",
        ]);
        const deleteBtn = elGenerator("button", "Delete", actionsDiv);

        totalPoints += Number(currentTask.points);
        totalSprintPoints.textContent = `Total Points ${totalPoints}pts`;
        taskNumber++;
        deleteTaskBtn.disabled = true;
        Object.keys(inputs).map((key) => {
            inputs[key].value = "";
        });

        deleteBtn.addEventListener('click', deleteTask);

        function deleteTask() {
            for (let el in inputs) {
                inputs[el].value = currentTask[el];
                inputs[el].disabled = true;
            }
            deleteTaskBtn.disabled = false;
            createTaskBtn.disabled = true;
            taskIdContainer.value = taskId;

            deleteTaskBtn.addEventListener('click', deleteTaskConfirm);
        }

        function deleteTaskConfirm() {
            for (let el in inputs) {
                inputs[el].value = '';
                inputs[el].disabled = false;
            }
            let id = taskIdContainer.value;
            let elForRemove = document.getElementById(id);
            totalPoints -= Number(estimationPoints[id]);
            totalSprintPoints.textContent = `Total Points ${totalPoints}pts`;
            createTaskBtn.disabled = false;
            deleteTaskBtn.disabled = true;

            elForRemove.remove();
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
