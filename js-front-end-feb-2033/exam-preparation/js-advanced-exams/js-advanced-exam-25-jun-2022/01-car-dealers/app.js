window.addEventListener("load", solve);

function solve() {
  const tBody = document.getElementById('table-body');
  const carsList = document.getElementById('cars-list');
  const profit = document.getElementById('profit');
  const publishBtn = document.getElementById('publish');
  let totalProfit = 0;

  const inputs = {
    make: document.getElementById('make'),
    model: document.getElementById('model'),
    year: document.getElementById('year'),
    fuel: document.getElementById('fuel'),
    originalCost: document.getElementById('original-cost'),
    sellingPrice: document.getElementById('selling-price')
  }

  publishBtn.addEventListener('click', publishCar);

  function publishCar(event) {
    event.preventDefault();

    if (!validateInputs()) {
      return;
    }

    const carData = {
      make: inputs.make.value,
      model: inputs.model.value,
      year: inputs.year.value,
      fuel: inputs.fuel.value,
      originalCost: inputs.originalCost.value,
      sellingPrice: inputs.sellingPrice.value
    }

    clearInputs();

    const tr = createElement('tr', null, tBody, null, ['row']);
    const makeTd = createElement('td', `${carData.make}`, tr);
    const modelTd = createElement('td', `${carData.model}`, tr);
    const yearTd = createElement('td', `${carData.year}`, tr);
    const fuelTd = createElement('td', `${carData.fuel}`, tr);
    const originalCostTd = createElement('td', `${carData.originalCost}`, tr);
    const sellingPriceTd = createElement('td', `${carData.sellingPrice}`, tr);
    const buttonsTd = createElement('td', null, tr);
    const editBtn = createElement('button', 'Edit', buttonsTd, null, ['action-btn', 'edit']);
    const sellBtn = createElement('button', 'Sell', buttonsTd, null, ['action-btn', 'sell']);

    editBtn.addEventListener('click', editCar);
    sellBtn.addEventListener('click', sellCar);

    function sellCar() {
      let sellingMoneyDifference = Number(carData.sellingPrice) - Number(carData.originalCost);
      const li = createElement('li', null, carsList, null, ['each-list']);
      const makeSpan = createElement('span', `${carData.make} ${carData.model}`, li);
      const yearSpan = createElement('span', `${carData.year}`, li);
      const differenceSpan = createElement('span', `${sellingMoneyDifference}`, li);
  
      totalProfit += sellingMoneyDifference;
      profit.textContent = totalProfit.toFixed(2);
  
      let tr = this.parentNode.parentNode;
      tr.remove();
    }
  
    function editCar() {
      Object.keys(inputs).map((key) => {
        inputs[key].value = carData[key];
      })
  
      let tr = this.parentNode.parentNode;
      tr.remove();
    }
  }

  function createElement(type, content, parentNode, id, classes, attributes, useInnerHtml) {
    const htmlElement = document.createElement(type);

    if (content && useInnerHtml) {
		htmlElement.innerHTML = content;
	} else {
		if (content && type !== 'input') {
			htmlElement.textContent = content;
		}
		if (content && type === 'input') {
	        htmlElement.value = content;
	    }
	}

    if (id) {
        htmlElement.id = id;
    }

    //['list', 'item']
    if (classes) {
        htmlElement.classList.add(...classes);
    }

    if (parentNode) {
        parentNode.appendChild(htmlElement);
    }

    // { src: 'link-to-image', href: 'link-to-site', type: checkbox, ... }
    if (attributes) {
        attributes.forEach((key) => htmlElement.setAttribute(key, attributes[key]));
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
    if (Number(inputs.originalCost.value) > Number(inputs.sellingPrice.value)) {
      result = false;
    }
    return result;
  }

  function clearInputs() {
    Object.keys(inputs).map((key) => {
      inputs[key].value = '';
    })
  }
}
