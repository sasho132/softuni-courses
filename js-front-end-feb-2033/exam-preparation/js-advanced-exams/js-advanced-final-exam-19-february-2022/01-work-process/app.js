function solve() {
    const tBody = document.getElementById('tbody');
    const addWorkerBtn = document.getElementById('add-worker');
    const budgetSum = document.getElementById('sum');
    let budgetTotal = 0;
    const inputs = {
        firstName: document.getElementById('fname'),
        lastName: document.getElementById('lname'),
        email: document.getElementById('email'),
        birth: document.getElementById('birth'),
        position: document.getElementById('position'),
        salary: document.getElementById('salary')
    }

    addWorkerBtn.addEventListener('click', addWorker);

    function addWorker(event) {
        event.preventDefault();

        for (let el in inputs) {
            if (inputs[el].value === '') {
                return;
            }
        }

        currentWorkerData = {
            firstName: inputs.firstName.value,
            lastName: inputs.lastName.value,
            email: inputs.email.value,
            birth: inputs.birth.value,
            position: inputs.position.value,
            salary: inputs.salary.value
        }

        const tr = elGenerator('tr', null, tBody);
        const fName = elGenerator('td', `${currentWorkerData.firstName}`, tr);
        const lName = elGenerator('td', `${currentWorkerData.lastName}`, tr);
        const email = elGenerator('td', `${currentWorkerData.email}`, tr);
        const birth = elGenerator('td', `${currentWorkerData.birth}`, tr);
        const position = elGenerator('td', `${currentWorkerData.position}`, tr);
        const salary = elGenerator('td', `${currentWorkerData.salary}`, tr);
        const buttons = elGenerator('td', null, tr);
        const firedBtn = elGenerator('button', 'Fired', buttons, null, ['fired']);
        buttons.appendChild(document.createTextNode(" "));
        const editBtn = elGenerator('button', 'Edit', buttons, null, ['edit']);
        
        for (let el in inputs) {
            inputs[el].value = '';
        }

        budgetTotal += Number(currentWorkerData.salary);
        budgetSum.textContent = budgetTotal.toFixed(2);

        editBtn.addEventListener('click', editWorker);
        firedBtn.addEventListener('click', fireWorker);

        function fireWorker() {
            budgetTotal -= Number(currentWorkerData.salary);
            budgetSum.textContent = budgetTotal.toFixed(2);

            let elForRemove = this.parentNode.parentNode;
            elForRemove.remove();
        }
        
        function editWorker() {
            for (let el in inputs) {
                inputs[el].value = currentWorkerData[el];
            }

            budgetTotal -= Number(currentWorkerData.salary);
            budgetSum.textContent = budgetTotal.toFixed(2);

            let elForRemove = this.parentNode.parentNode;
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
solve()