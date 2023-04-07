function solve() {
    const mailsList = document.getElementById('list');
    const sentList = document.querySelector('.sent-list');
    const deleteMailList = document.querySelector('.delete-list');
    const addMailBtn = document.getElementById('add');
    const resetMailBtn = document.getElementById('reset');

    const inputs = {
        recipient: document.getElementById('recipientName'),
        title: document.getElementById('title'),
        message: document.getElementById('message')
    }

    addMailBtn.addEventListener('click', addMail);
    resetMailBtn.addEventListener('click', resetInputs);

    function addMail(event) {
        event.preventDefault();

        if (!validateInputs()) {
            return;
        }

        const currentMail = {
            recipient: inputs.recipient.value,
            title: inputs.title.value,
            message: inputs.message.value
        }

        const li = elGenerator('li', null, mailsList);
        const title = elGenerator('h4', `Title: ${currentMail.title}`, li);
        const recipientName = elGenerator(
            'h4', 
            `Recipient Name: ${currentMail.recipient}`,
            li
        );
        const messageSpan = elGenerator('span', `${currentMail.message}`, li);
        const listActionDiv = elGenerator('div', null, li, 'list-action');
        const sendBtn = elGenerator('button', `Send`, listActionDiv, 'send');
        sendBtn.setAttribute('type', 'submit');
        const deleteBtn = elGenerator('button', 'Delete', listActionDiv, 'delete');
        deleteBtn.setAttribute('type', 'submit');
        
        resetInputs();

        sendBtn.addEventListener('click', sendMail);
        deleteBtn.addEventListener('click', deleteMail);

        function sendMail(event) {
            event.preventDefault();

            const sentMailsLi = elGenerator('li', null, sentList);
            const recipientSpan = elGenerator('span', `To: ${currentMail.recipient}`, sentMailsLi);
            const titleSpan = elGenerator(
                'span', 
                `Title: ${currentMail.title}`, 
                sentMailsLi
            );
            const btnDiv = elGenerator('div', null, sentMailsLi, null, ['btn']);
            const deleteMailBtn = elGenerator('button', `Delete`, btnDiv, null, ['delete']);
            deleteMailBtn.setAttribute('type', 'submit');
            deleteMailBtn.addEventListener('click', deleteMail);
            
            let toRemoveNode = event.currentTarget.parentNode.parentNode;
            toRemoveNode.remove();
        }

        function deleteMail(event) {
            event.preventDefault();
            event.currentTarget.parentNode.parentNode.remove();

            const deleteMailsLi = elGenerator('li', null, deleteMailList);
            const deleteRecipientSpan = elGenerator(
                'span', 
                `To: ${currentMail.recipient}`,
                deleteMailsLi
            );
            const deleteTitleSpan = elGenerator(
                'span',
                `Title: ${currentMail.title}`,
                deleteMailsLi
            );
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

    function validateInputs() {
        let result = true;
        for (let input in inputs) {
          if (inputs[input].value === '' || inputs[input].value.trim() === '') {
            result = false;
          }
        }
        return result;
    }

    function resetInputs() {
        Object.keys(inputs).map((key) => {
            inputs[key].value = '';
        })
    }
}
solve()