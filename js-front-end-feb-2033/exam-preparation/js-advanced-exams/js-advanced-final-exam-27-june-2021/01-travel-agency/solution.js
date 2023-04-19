window.addEventListener('load', solution);

function solution() {
  const infoPreview = document.getElementById('infoPreview');
  const blockContainer = document.getElementById('block');
  const submitBtn = document.getElementById('submitBTN');
  const editBtn = document.getElementById('editBTN');
  const continueBtn = document.getElementById('continueBTN');


  const inputs = {
    name: document.getElementById('fname'),
    email: document.getElementById('email'),
    phone: document.getElementById('phone'),
    address: document.getElementById('address'),
    code: document.getElementById('code')
  }

  submitBtn.addEventListener('click', addReservation);

  function addReservation(event) {
    event.preventDefault();

    if (inputs.name.value === '' || inputs.email.value === '') {
      return;
    }

    this.disabled = true;
    editBtn.disabled = false;
    continueBtn.disabled = false;

    let currentData = {
      name: inputs.name.value,
      email: inputs.email.value,
      phone: inputs.phone.value,
      address: inputs.address.value,
      code: inputs.code.value
    }

    const nameLi = elGenerator('li', `Full Name: ${currentData.name}`, infoPreview);
    const emailLi = elGenerator('li', `Email: ${currentData.email}`, infoPreview);
    const phoneLi = elGenerator('li', `Phone Number: ${currentData.phone}`, infoPreview);
    const addressLi = elGenerator('li', `Address: ${currentData.address}`, infoPreview);
    const codeLi = elGenerator('li', `Postal Code: ${currentData.code}`, infoPreview);

    for (let el in inputs) {
      inputs[el].value = '';
    }

    editBtn.addEventListener('click', editReservation);
    continueBtn.addEventListener('click', continueReservation);

    function continueReservation(event) {
      event.preventDefault();

      blockContainer.textContent = '';
      const doneMessage = elGenerator('h3', 'Thank you for your reservation!', blockContainer);
    }

    function editReservation(event) {
      event.preventDefault();

      infoPreview.textContent = '';

      Object.keys(inputs).forEach((key) => {
        inputs[key].value = currentData[key];
      })

      this.disabled = true;
      continueBtn.disabled = true;
      submitBtn.disabled = false;
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
}
