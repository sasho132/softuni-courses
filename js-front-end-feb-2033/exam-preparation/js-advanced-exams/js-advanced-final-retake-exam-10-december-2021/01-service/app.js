window.addEventListener('load', solve);

function solve() {
    const inputs = {
        productType: document.getElementById('type-product'),
        description: document.getElementById('description'),
        clientName: document.getElementById('client-name'),
        clientPhone: document.getElementById('client-phone')
    }
    const receivedOrdersContainer = document.getElementById('received-orders');
    const completedOrdersContainer = document.getElementById('completed-orders');
    const sendFormBtn = document.querySelector('form > button');
    const clearBtn = document.querySelector('.clear-btn');
    sendFormBtn.addEventListener('click', sendForm);
    
    function sendForm(event) {
        event.preventDefault();

        for (let el in inputs) {
            if (inputs[el].value === '') {
                return;
            }
        }

        let repairData = {
            productType: inputs.productType.value,
            description: inputs.description.value,
            clientName: inputs.clientName.value,
            clientPhone: inputs.clientPhone.value
        }

        const divContainer = elGenerator(
            'div', 
            null, 
            receivedOrdersContainer, 
            null, 
            ['container']
        );
        const prodType = elGenerator(
            'h2', 
            `Product type for repair: ${repairData.productType}`,
            divContainer,
        );
        const clientInfo = elGenerator(
            'h3',
            `Client information: ${repairData.clientName}, ${repairData.clientPhone}`,
            divContainer
        );
        const problemDesc = elGenerator(
            'h4',
            `Description of the problem: ${repairData.description}`,
            divContainer
        );
        const startRepairBtn = elGenerator(
            'button',
            'Start repair',
            divContainer,
            null,
            ['start-btn']
        );
        const finishRepairBtn = elGenerator(
            'button',
            'Finish repair',
            divContainer,
            null,
            ['finish-btn']
        );

        finishRepairBtn.disabled = true;

        for (let el in inputs) {
            inputs[el].value = '';
        }

        startRepairBtn.addEventListener('click', () => {
            startRepairBtn.disabled = true;
            finishRepairBtn.disabled = false;
        });
        finishRepairBtn.addEventListener('click', completeRepair);

        function completeRepair() {
            completedOrdersContainer.appendChild(this.parentNode);

            clearBtn.addEventListener('click', clearRepairsList);

            startRepairBtn.remove();
            finishRepairBtn.remove();
        }

        function clearRepairsList() {
            let repairs = completedOrdersContainer.querySelectorAll('.container');

            for (let el of repairs) {
                el.remove();
            }
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