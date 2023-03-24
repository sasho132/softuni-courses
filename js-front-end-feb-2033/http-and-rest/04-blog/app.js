function attachEvents() {
    const loadPostsBtn = document.getElementById('btnLoadPosts');
    const postSelection = document.getElementById('posts');
    const viewPostsBtn = document.getElementById('btnViewPost');
    const postTitle = document.getElementById('post-title');
    const postBody = document.getElementById('post-body');
    const postCommentsList = document.getElementById('post-comments');
    const BASE_URL = `http://localhost:3030/jsonstore/blog/`;

    loadPostsBtn.addEventListener('click', loadPosts);

    async function loadPosts() {
        try {
            const postsData = await fetch(`${BASE_URL}posts`);
            const posts = await postsData.json();

            Object.values(posts).forEach((post) => {
                let newOption = document.createElement('option');
                newOption.value = post.id;
                newOption.textContent = post.title;
                postSelection.appendChild(newOption);
            })

            viewPostsBtn.addEventListener('click', viewPost);

            async function viewPost() {
                let postId = document.querySelector('#posts').value;
                let currentPost = Object.values(posts).find((el) => el.id === postId);
                postTitle.textContent = currentPost.title;
                postBody.textContent = currentPost.body;

                const allPostsData = await fetch(`${BASE_URL}comments`);
                const allPosts = await allPostsData.json();
                postCommentsList.innerHTML = '';

                let filteredPosts = Object.values(allPosts).filter((el) => {
                    return el.postId === currentPost.id;
                });
                Object.values(filteredPosts).forEach((el) => {
                    let newLi = document.createElement('li');
                    newLi.id = el.id;
                    newLi.textContent = el.text;
                    postCommentsList.appendChild(newLi);
                })
            }

            
        } catch (err) {
            console.log(err);
        }
    }
}

attachEvents();