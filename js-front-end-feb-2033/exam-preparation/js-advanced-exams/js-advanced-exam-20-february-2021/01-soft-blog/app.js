function solve(){
   const createBtn = document.querySelector('.btn');
   const postsSection = document.querySelector('.site-content > main:nth-child(1) > section:nth-child(1)');
   const archiveSection = document.querySelector('.archive-section > ol');

   const inputs = {
      creator: document.getElementById('creator'),
      title: document.getElementById('title'),
      category: document.getElementById('category'),
      content: document.getElementById('content'),
   }

   createBtn.addEventListener('click', addPost);

   function addPost(event) {
      event.preventDefault();

      Object.keys(inputs).forEach((key) => {
         if (inputs[key].value === '') {
            return;
         }
      })

      const article = elGenerator('article', null, postsSection);
      const title = elGenerator('h1', `${inputs.title.value}`, article);
      const category = elGenerator('p', null, article);
      category.innerHTML = `Category: <strong>${inputs.category.value}</strong>`;
      const creator = elGenerator('p', null, article);
      creator.innerHTML = `Creator: <strong>${inputs.creator.value}</strong>`;
      const content = elGenerator('p', `${inputs.content.value}`, article);
      const buttonsDiv = elGenerator('div', null, article, null, ['buttons']);
      const deleteBtn = elGenerator('button', 'Delete', buttonsDiv, null, ['btn', 'delete']);
      const archiveBtn = elGenerator('button', 'Archive', buttonsDiv, null, ['btn', 'archive']);

      Object.keys(inputs).forEach((key) => {
         inputs[key].value = '';
      })

      archiveBtn.addEventListener('click', archivePost);
      deleteBtn.addEventListener('click', deletePost);

      function archivePost() {
         const archiveList = document.querySelector('.archive-section > ol:nth-child(2)');
         let postTitle = this.parentNode.parentNode.querySelector('h1').textContent;
         const titleLi = elGenerator('li', postTitle, archiveList);
         let archiveItems = document.querySelectorAll('.archive-section > ol:nth-child(2) > li');
         archiveItems = Object.values(archiveItems).sort((a, b) => {
            if (a.textContent < b.textContent) {
               return -1;
             }
             if (a.textContent > b.textContent) {
               return 1;
             }
             return 0;
         })
         Object.values(archiveItems).forEach((el) => archiveList.appendChild(el));

         this.parentNode.parentNode.remove();
      }

      function deletePost() {
         this.parentNode.parentNode.remove();
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
