function solve(arr) {
    const number = Number(arr.shift());
    const assignees = {};
    const points = {
        "ToDo": 0,
        "In Progress": 0,
        "Code Review": 0,
        "Done": 0,
    };

    for (let i = 0; i < number; i++) {
        let [assignee, taskId, title, status, estimatedPoints] = arr
            .shift()
            .split(":");
        if (!assignees.hasOwnProperty(assignee)) {
            assignees[assignee] = [];
        }
        assignees[assignee] = [{ taskId, title, status, estimatedPoints }];
        points[status] += Number(estimatedPoints);
    }

    for (let currentLine of arr) {
        let currentData = currentLine.split(':');
        let action = currentData.shift();

        switch(action) {
            case 'Add New':
                addNew(currentData);
                break;
            case 'Change Status':
                changeStatus(currentData);
                break;
            case 'Remove Task':
                removeTask(currentData);
                break;
        }
    }

    function addNew(data) {
        let [ assignee, taskId, title, status, estimatedPoints ] = data;
        if (!assignees.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
        } else {
            assignees[assignee].push({ taskId, title, status, estimatedPoints });
            points[status] += Number(estimatedPoints);
        }
    }

    function changeStatus(data) {
        let [ assignee, taskId, newStatus ] = data;
        if (!assignees.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
        } else {
            let task = assignees[assignee].find(task => task.taskId === taskId);
            if (!task) {
                console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
            } else {
                let taskStatus = task.status;
                let taskPoints = Number(task.estimatedPoints);
                points[taskStatus] -= taskPoints;
                taskStatus = newStatus;
                points[taskStatus] += taskPoints;
            }
        }
    }

    function removeTask(data) {
        let [ assignee, index ] = data;
        if (!assignees.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
        } else {
            let taskIndex = Number(index) - 1;
            if (assignees[assignee][taskIndex] === undefined) {
                console.log("Index is out of range!");
            } else {
                let task = assignees[assignee][taskIndex];
                points[task.status] -= Number(task.estimatedPoints);
                assignees[assignee].splice(taskIndex, 1);
            }
        }
    }
    
    console.log(`ToDo: ${points['ToDo']}pts`);
    console.log(`In Progress: ${points['In Progress']}pts`);
    console.log(`Code Review: ${points['Code Review']}pts`);
    console.log(`Done Points: ${points['Done']}pts`);

    let doneTaskPoints = points['Done'];
    let otherTaskPoints = points['ToDo'] + points['In Progress'] + points['Code Review'];

    if (doneTaskPoints >= otherTaskPoints) {
        console.log('Sprint was successful!');
    } else {
        console.log('Sprint was unsuccessful...')
    }
}

solve([
    "5",
    "Kiril:BOP-1209:Fix Minor Bug:ToDo:3",
    "Mariya:BOP-1210:Fix Major Bug:In Progress:3",
    "Peter:BOP-1211:POC:Code Review:5",
    "Georgi:BOP-1212:Investigation Task:Done:2",
    "Mariya:BOP-1213:New Account Page:In Progress:13",
    "Add New:Kiril:BOP-1217:Add Info Page:In Progress:5",
    "Change Status:Peter:BOP-1290:ToDo",
    "Remove Task:Mariya:1",
    "Remove Task:Joro:1",
]);

// solve([
//     "4",
//     "Kiril:BOP-1213:Fix Typo:Done:1",
//     "Peter:BOP-1214:New Products Page:In Progress:2",
//     "Mariya:BOP-1215:Setup Routing:ToDo:8",
//     "Georgi:BOP-1216:Add Business Card:Code Review:3",
//     "Add New:Sam:BOP-1237:Testing Home Page:Done:3",
//     "Change Status:Georgi:BOP-1216:Done",
//     "Change Status:Will:BOP-1212:In Progress",
//     "Remove Task:Georgi:3",
//     "Change Status:Mariya:BOP-1215:Done",
// ]);
