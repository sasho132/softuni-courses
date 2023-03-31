window.addEventListener("load", solve);

function solve() {
    const inputs = {
        firstName: document.getElementById("first-name"),
        lastName: document.getElementById("last-name"),
        peopleCount: document.getElementById("people-count"),
        fromDate: document.getElementById("from-date"),
        daysCount: document.getElementById("days-count"),
    };

    const ticketInfo = {
        firstName: null,
        lastName: null,
        peopleCount: null,
        fromDate: null,
        daysCount: null,
    }

    const bodyContainer = document.getElementById('body');
    const mainContainer = document.getElementById('main');
    const ticketInfoList = document.querySelector(".ticket-info-list");
    const nextBtn = document.getElementById("next-btn");
    const confirmTicketList = document.querySelector(
        ".confirm-ticket"
    );
    const formContainer = document.querySelector(".container-text > form:nth-child(1)");

    nextBtn.addEventListener("click", previewTicket);

    function previewTicket(event) {
        if (event) {
            event.preventDefault();
        }

        for (let input in inputs) {
            if (inputs[input].value === '') {
                return;
            }
        }

        Object.keys(ticketInfo).forEach((el) => {
            ticketInfo[el] = inputs[el].value;
        })

        const li = createElement("li", null, ticketInfoList, null, ["ticket"]);
        const article = createElement("article", null, li);
        const title = createElement(
            "h3",
            `Name: ${inputs.firstName.value} ${inputs.lastName.value}`,
            article
        );
        const formDateP = createElement("p", `From date: ${inputs.fromDate.value}`, article);
        const daysCountP = createElement("p", `For ${inputs.daysCount.value} days`, article);
        const peopleCountP = createElement("p",
            `For ${inputs.peopleCount.value} people`,
            article
        );
        const editBtn = createElement("button", "Edit", li, null, ["edit-btn"]);
        const continueBtn = createElement("button", "Continue", li, null, ["continue-btn"]);

        editBtn.addEventListener('click', editTicket);
        continueBtn.addEventListener('click', readyToConfirmTicket);

        nextBtn.disabled = true;
        formContainer.reset();
    }

    function editTicket() {
        for (let key in inputs) {
            inputs[key].value = ticketInfo[key];
        }

        ticketInfoList.innerHTML = '';
        nextBtn.disabled = false;
    }

    function readyToConfirmTicket() {
        const ticketRef = this.parentNode;
        ticketRef.classList.replace('ticket', 'ticket-content');
        confirmTicketList.appendChild(ticketRef);

        const editBtn = confirmTicketList.querySelector('.edit-btn');
        const continueBtn = confirmTicketList.querySelector('.continue-btn');

        const confirmBtn = createElement('button', 'Confirm', confirmTicketList, 
        null, ['confirm-btn']);
        const cancelBtn = createElement('button', 'Cancel', confirmTicketList, 
        null, ['cancel-btn']);
        
        confirmBtn.addEventListener('click', confirmTicket);
        cancelBtn.addEventListener('click', cancelTicket);
        
        editBtn.remove();
        continueBtn.remove();
    }

    function cancelTicket(event) {
        nextBtn.disabled = false;
        const li = event.currentTarget.parentNode;
        li.remove();
    }

    function confirmTicket() {
        mainContainer.remove();

        const title = createElement('h1', "Thank you, have a nice day!", 
            bodyContainer, "thank-you");

        const backBtn = createElement('button', 'Back', bodyContainer, 'back-btn');
        backBtn.addEventListener('click', () => location.reload());  
    }

    function createElement(
        type,
        content,
        parentNode,
        id,
        classes,
        attributes,
        useInnerHtml
    ) {
        const htmlElement = document.createElement(type);

        if (content && useInnerHtml) {
            htmlElement.innerHTML = content;
        } else {
            if (content && type !== "input") {
                htmlElement.textContent = content;
            }
        }

        if (id) {
            htmlElement.id = id;
        }

        if (classes) {
            htmlElement.classList.add(...classes);
        }

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        if (attributes) {
            attributes.forEach((key) =>
                htmlElement.setAttribute(key, attributes[key])
            );
        }

        return htmlElement;
    }
}
