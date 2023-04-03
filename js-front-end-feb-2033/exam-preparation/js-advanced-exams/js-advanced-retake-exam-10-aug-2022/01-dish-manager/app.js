window.addEventListener("load", solve);

function solve() {
  const inProgressList = document.getElementById('in-progress');
  const finishedList = document.getElementById('finished');
  const progressCounterSpan = document.getElementById('progress-count');
  const submitBtn = document.getElementById('form-btn');
  const clearBtn = document.getElementById('clear-btn');

  const formInputs = {
    firstName: document.getElementById('first-name'),
    lastName: document.getElementById('last-name'),
    age: document.getElementById('age'),
    gender: document.getElementById('genderSelect'),
    taskDesc: document.getElementById('task')
  }

  const taskData = {
    firstName: null,
    lastName: null,
    age: null,
    gender: null,
    taskDesc: null
  }

  let progressCounter = Number(progressCounterSpan.textContent);

  submitBtn.addEventListener('click', addTask);

  function addTask(event) {
    event.preventDefault();

    let validateInputs = Object.values(formInputs).every((el) => el.value !== '');
    console.log(validateInputs);
    if (!validateInputs) {
      return;
    }

    for (let key in taskData) {
      taskData[key] = formInputs[key].value;
    }

    const li = document.createElement('li');
    li.classList.add('each-line');
    const article = document.createElement('article');
    const titleP = document.createElement('h4');
    titleP.textContent = `${taskData.firstName} ${taskData.lastName}`;
    const ageAndGenderP = document.createElement('p');
    ageAndGenderP.textContent = `${taskData.gender}, ${taskData.age}`;
    const descP = document.createElement('p');
    descP.textContent = `Dish description: ${taskData.taskDesc}`;
    const editBtn = document.createElement('button');
    editBtn.classList.add('edit-btn');
    editBtn.textContent = 'Edit';
    const completeBtn = document.createElement('button');
    completeBtn.classList.add('complete-btn');
    completeBtn.textContent = 'Mark as complete';
    
    article.appendChild(titleP);
    article.appendChild(ageAndGenderP);
    article.appendChild(descP);
    li.appendChild(article);
    li.appendChild(editBtn);
    li.appendChild(completeBtn);
    inProgressList.appendChild(li);

    progressCounter++;
    progressCounterSpan.textContent = progressCounter;

    for (let el in formInputs) {
      formInputs[el].value = '';
    }

    editBtn.addEventListener('click', editTask);
    completeBtn.addEventListener('click', confirmTask);
  }

  function editTask() {
    for (let input in formInputs) {
      formInputs[input].value = taskData[input];
    }

    progressCounter--;
    progressCounterSpan.textContent = progressCounter;

    let li = inProgressList.querySelector('.each-line');
    li.remove();
  }

  function confirmTask() {
    let li = inProgressList.querySelector('.each-line');
    finishedList.appendChild(li);

    progressCounter--;
    progressCounterSpan.textContent = progressCounter;

    clearBtn.addEventListener('click', () => finishedList.innerHTML = '');

    let editBtn = finishedList.querySelector('.edit-btn');
    let completeBtn = finishedList.querySelector('.complete-btn');
    editBtn.remove();
    completeBtn.remove();
  }
}
