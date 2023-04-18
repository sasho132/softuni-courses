window.addEventListener('load', solve);

function solve() {
    const furnitureList = document.getElementById('furniture-list');
    const totalPriceContainer = document.querySelector('.total-price');
    const addBtn = document.getElementById('add');
    let totalPrice = 0;

    const inputs = {
        model: document.getElementById('model'),
        year: document.getElementById('year'),
        description: document.getElementById('description'),
        price: document.getElementById('price'),
    }

    addBtn.addEventListener('click', addFurniture);

    function addFurniture(event) {
        event.preventDefault();

        for (let el in inputs) {
            if (inputs[el].value === '') {
                return;
            } else if (inputs.price.value <= 0 || inputs.year.value <= 0) {
                return;
            }
        }

        let currentData = {
            model: inputs.model.value,
            year: inputs.year.value,
            description: inputs.description.value,
            price: inputs.price.value,
        }

        const tr = elGenerator('tr', null, furnitureList, null, ['info']);
        const modelTd = elGenerator(
            'td',
            `${currentData.model}`,
            tr,
        );
        const priceTd = elGenerator(
            'td',
            `${Number(currentData.price).toFixed(2)}`,
            tr,
        );
        const buttonsTd = elGenerator('td', null, tr);
        const moreBtn = elGenerator(
            'button',
            'More Info',
            buttonsTd,
            null,
            ['moreBtn']
        );
        const buyBtn = elGenerator(
            'button',
            'Buy it',
            buttonsTd,
            null,
            ['buyBtn']
        );
        const hideTr = elGenerator('tr', null, furnitureList, null, ['hide']);
        const yearTd = elGenerator(
            'td',
            `Year: ${currentData.year}`,
            hideTr,
        );
        const descTd = elGenerator(
            'td',
            `Description: ${currentData.description}`,
            hideTr
        );
        descTd.setAttribute('colspan', '3');

        for (let el in inputs) {
            inputs[el].value = '';
        }

        moreBtn.addEventListener('click', moreInfo);
        buyBtn.addEventListener('click', buyFurniture);

        function moreInfo() {
            this.textContent = 'Less Info';
            hideTr.setAttribute('style', 'display: contents;');
            this.addEventListener('click', lessInfo);
        }

        function lessInfo() {
            this.textContent = 'More Info';
            hideTr.setAttribute('style', 'display: none;');
            this.addEventListener('click', moreInfo);
        }

        function buyFurniture() {
            let info = furnitureList.querySelector('.info');
            let hide = furnitureList.querySelector('.hide');

            totalPrice += Number(currentData.price);
            totalPriceContainer.textContent = totalPrice.toFixed(2);

            info.remove();
            hide.remove();
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
