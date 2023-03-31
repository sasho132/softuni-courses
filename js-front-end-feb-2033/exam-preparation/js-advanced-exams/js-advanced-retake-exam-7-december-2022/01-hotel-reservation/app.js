window.addEventListener('load', solve);

function solve() {
    const formInputs = {
        firstName: document.getElementById('first-name'),
        lastName: document.getElementById('last-name'),
        dateIn: document.getElementById('date-in'),
        dateOut: document.getElementById('date-out'),
        peopleCount: document.getElementById('people-count')
    }

    const reservationData = {
        firstName: null,
        lastName: null,
        dateIn: null,
        dateOut: null,
        peopleCount: null
    }

    const infoList = document.querySelector('.info-list');
    const confirmList = document.querySelector('.confirm-list');
    const verificationContainer = document.getElementById('verification');
    const nextBtn = document.getElementById('next-btn');

    nextBtn.addEventListener('click', reservationInfo);

    function reservationInfo(event) {
        if (event) {
            event.preventDefault();
        }

        for (let input in formInputs) {
            if (formInputs[input].value === '' || dateValidation()) {
                return;
            }
        }

        for (let input in reservationData) {
            reservationData[input] = formInputs[input].value;
        }

        const li = document.createElement('li');
        li.classList.add('reservation-content');
        const article = document.createElement('article');
        const title = document.createElement('h3');
        const fromDateP = document.createElement('p');
        const toDateP = document.createElement('p');
        const peopleCountP = document.createElement('p');
        const editBtn = document.createElement('button');
        const continueBtn = document.createElement('button');

        title.textContent = `Name: ${formInputs.firstName.value} ${formInputs.lastName.value}`;
        fromDateP.textContent = `From date: ${formInputs.dateIn.value}`;
        toDateP.textContent = `To date: ${formInputs.dateOut.value}`;
        peopleCountP.textContent = `For ${formInputs.peopleCount.value} people`;
        editBtn.textContent = 'Edit';
        continueBtn.textContent = 'Continue';
        editBtn.classList.add('edit-btn');
        continueBtn.classList.add('continue-btn');

        article.appendChild(title);
        article.appendChild(fromDateP);
        article.appendChild(toDateP);
        article.appendChild(peopleCountP);
        li.appendChild(article);
        li.appendChild(editBtn);
        li.appendChild(continueBtn);
        infoList.appendChild(li);

        nextBtn.disabled = true;
        
        for (let input in formInputs) {
            formInputs[input].value = '';
        }

        editBtn.addEventListener('click', editReservation);
        continueBtn.addEventListener('click', readyReservation);
    }

    function editReservation() {
        for (let input in formInputs) {
            formInputs[input].value = reservationData[input];
        }
        nextBtn.disabled = false;
        const li = this.parentNode;
        li.remove();
    }

    function readyReservation() {
        const li = this.parentNode;
        const confirmBtn = document.createElement('button');
        const cancelBtn = document.createElement('button');
        confirmBtn.textContent = 'Confirm';
        cancelBtn.textContent = 'Cancel';
        confirmBtn.classList.add('confirm-btn');
        cancelBtn.classList.add('cancel-btn');

        confirmBtn.addEventListener('click', confirmReservation);
        cancelBtn.addEventListener('click', cancelReservation);

        li.appendChild(confirmBtn);
        li.appendChild(cancelBtn);
        confirmList.appendChild(li);
        
        const editBtn = confirmList.querySelector('.edit-btn');
        const continueBtn = confirmList.querySelector('.continue-btn');

        editBtn.remove();
        continueBtn.remove();
    }

    function confirmReservation() {
        const li = this.parentNode;
        li.remove();

        nextBtn.disabled = false;

        verificationContainer.classList.add('reservation-confirmed');
        verificationContainer.textContent = 'Confirmed.';
    }

    function cancelReservation() {
        const li = this.parentNode;
        li.remove();

        nextBtn.disabled = false;

        verificationContainer.classList.add('reservation-cancelled');
        verificationContainer.textContent = 'Cancelled.';
    }

    function dateValidation() {
        let firstDate = Number(formInputs.dateIn.value.split('-').join(''));
        let secondDate = Number(formInputs.dateOut.value.split('-').join(''));
        return firstDate > secondDate
    }
}
