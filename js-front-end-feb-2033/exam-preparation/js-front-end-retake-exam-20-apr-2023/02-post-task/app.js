window.addEventListener("load", solve);

function solve() {
  const publishBtn = document.getElementById('publish-btn');
  const reviewList = document.getElementById('review-list');
  const publishedList = document.getElementById('published-list');

  const inputs = {
    taskTitle: document.getElementById('task-title'),
    taskCategory: document.getElementById('task-category'),
    taskContent: document.getElementById('task-content')
  }

  publishBtn.addEventListener('click', publishTask);

  function publishTask() {
    for (let el in inputs) {
        if (inputs[el].value === '') {
            return;
        }
    }

    let currentData = {
        taskTitle: inputs.taskTitle.value,
        taskCategory: inputs.taskCategory.value,
        taskContent: inputs.taskContent.value
    }

    const li = document.createElement('li');
    li.classList.add('rpost');
    reviewList.appendChild(li);
    const article = document.createElement('article');
    li.appendChild(article);
    const title = document.createElement('h4');
    title.textContent = `${currentData.taskTitle}`;
    article.appendChild(title);
    const category = document.createElement('p');
    category.textContent = `Category: ${currentData.taskCategory}`;
    article.appendChild(category);
    const content = document.createElement('p');
    content.textContent = `Content: ${currentData.taskContent}`;
    article.appendChild(content);
    
    const editBtn = document.createElement('button');
    editBtn.textContent = 'Edit';
    let editBtnClasses = ['action-btn', 'edit'];
    editBtn.classList.add(...editBtnClasses);
    li.appendChild(editBtn);
    const postBtn = document.createElement('button');
    postBtn.textContent = 'Post';
    let postBtnClasses = ['action-btn', 'post'];
    postBtn.classList.add(...postBtnClasses);
    li.appendChild(postBtn);

    for (let el in inputs) {
        inputs[el].value = '';
    }

    editBtn.addEventListener('click', editTask);
    postBtn.addEventListener('click', postTask);

    function editTask() {
        Object.keys(inputs).forEach((el) => {
            inputs[el].value = currentData[el];
        });

        this.parentNode.remove();
    }

    function postTask() {
        let li = this.parentNode;
        publishedList.appendChild(li);

        let editBtn = publishedList.querySelector('.edit');
        let postBtn = publishedList.querySelector('.post');
        
        editBtn.remove();
        postBtn.remove();
    }
  }

  

}