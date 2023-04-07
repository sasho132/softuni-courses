window.addEventListener("load", solve);

function solve() {
    const reviewList = document.getElementById("review-list");
    const publishedList = document.getElementById('published-list');
    const clearBtn = document.getElementById('clear-btn');
    const publishBtn = document.getElementById("publish-btn");

    const inputs = {
      title: document.getElementById('post-title'),
      category: document.getElementById('post-category'),
      content: document.getElementById('post-content')
    }

    publishBtn.addEventListener("click", publishPost);

    function publishPost() {
        if (!validateInputs()) {
          return;
        }

        currentPostData = {
          title: inputs.title.value,
          category: inputs.category.value,
          content: inputs.content.value
        }

        const li = elGenerator('li', null, reviewList, null, ['rpost']);
        const article = elGenerator('article', null, li);
        const header = elGenerator('h4', `${currentPostData.title}`, article);
        const categoryP = elGenerator('p', `Category: ${currentPostData.category}`, article);
        const contentP = elGenerator('p', `Content: ${currentPostData.content}`, article);
        const editBtn = elGenerator('button', 'Edit', li, null, ['action-btn', 'edit']);
        const approveBtn = elGenerator(
          'button', 
          'Approve', 
          li, 
          null, 
          ['action-btn', 'approve']
        );

        Object.keys(inputs).map((key) => {
          inputs[key].value = '';
        })

        editBtn.addEventListener('click', editPost);
        approveBtn.addEventListener('click', approvePost);

        function approvePost() {
          let li = this.parentNode;
          publishedList.appendChild(li);

          let editBtn = publishedList.querySelector('.edit');
          let approveBtn = publishedList.querySelector('.approve');

          editBtn.remove();
          approveBtn.remove();

          clearBtn.addEventListener('click', () => {
            publishedList.innerHTML = '';
          })
        }

        function editPost() {
          Object.keys(inputs).map((key) => {
            inputs[key].value = currentPostData[key];
          })

          let toDeleteItem = this.parentNode;
          toDeleteItem.remove();
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
}
