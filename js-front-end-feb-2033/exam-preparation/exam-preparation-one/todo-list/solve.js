function attachEvents() {}
  const addTaskBtn = document.getElementById('add-button');
  const loadTaskBtn = document.getElementById('load-button');
  const taskListContainer = document.getElementById('todo-list');
  const titleInput = document.getElementById('title');
  const BASE_URL = `http://localhost:3030/jsonstore/tasks/`;

  loadTaskBtn.addEventListener('click', loadTasks);
  addTaskBtn.addEventListener('click', addTask);

  function loadTasks(event) {
    if (event) {
      event.preventDefault();
    }
    taskListContainer.innerHTML = '';
    fetch(BASE_URL)
      .then((res) => res.json())
      .then((data) => {
        Object.values(data).forEach(({_id, name}) => {
          const li = document.createElement('li');
          const span = document.createElement('span');
          const removeBtn = document.createElement('button');
          const editBtn = document.createElement('button');
          
          li.id = _id;
          span.textContent = name;
          removeBtn.textContent = 'Remove';
          editBtn.textContent = 'Edit';

          removeBtn.addEventListener('click', removeTask);
          editBtn.addEventListener('click', editTask);

          li.append(span, removeBtn, editBtn);
          taskListContainer.appendChild(li);
        })
      })
      .catch((err) => {
        console.log(err);
      })
  }

  function removeTask(event) {
    const id = event.currentTarget.parentNode.id;
    const httpHeaders = {
      method: 'DELETE'
    }

    fetch(`${BASE_URL}${id}`, httpHeaders)
      .then(() => loadTasks())
      .catch((err) => {
        console.error(err);
      })
  }

  function editTask(event) {
    const li = event.currentTarget.parentNode;
    const [span, _removeBtn, editBtn] = Array.from(li.children);
    const input = document.createElement('input');
    input.value = span.textContent;
    li.prepend(input);
    span.remove();
    editBtn.remove();
    const submitBtn = document.createElement('button');
    submitBtn.textContent = 'Submit';
    submitBtn.addEventListener('click', submitTask);
    li.append(submitBtn);    
  }

  function submitTask(event) {
    const taskId = event.currentTarget.parentNode.id;
    const [ input ] = Array.from(event.currentTarget.parentNode.children);
    const name = input.value;
    const httpHeaders = {
      method: 'PATCH',
      body: JSON.stringify({ name })
    }

    fetch(`${BASE_URL}${taskId}`, httpHeaders)
      .then(() => loadTasks())
      .catch((err) => {
        console.error(err);
      })
  }

  function addTask(event) {
    if (event) {
      event.preventDefault();
    }
    const name = titleInput.value;
    const httpHeaders = {
      method: 'POST',
      body: JSON.stringify({ name })
    }
    fetch(BASE_URL, httpHeaders)
      .then(() => loadTasks())
      .then(() => titleInput.value = '')
      .catch((err) => {
        console.error(err);
      })
  }

attachEvents();
