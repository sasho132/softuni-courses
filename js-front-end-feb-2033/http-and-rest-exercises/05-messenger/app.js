function attachEvents() {
    const refreshBtn = document.getElementById("refresh");
    const submitBtn = document.getElementById("submit");
    const messageArea = document.getElementById('messages');
    const messageAuthor = document.querySelector('#controls > div:nth-child(1) > input:nth-child(2)');
    const messageBody = document.querySelector('#controls > div:nth-child(2) > input:nth-child(2)');
    const BASE_URL = `http://localhost:3030/jsonstore/messenger`;

    refreshBtn.addEventListener("click", getMessages);
    submitBtn.addEventListener('click', postMessage);
    
    function postMessage() {
        messageArea.value = '';
        let author = messageAuthor.value;
        let content = messageBody.value;
        let httpHeaders = {
            method: 'post',
            body: JSON.stringify({ author, content }),
        }
        fetch(BASE_URL, httpHeaders)
            .then((res) => res.json())
            .then(messageAuthor.value = '')
            .then(messageBody.value = '')
            .then(getMessages)
    }

    async function getMessages() {
        try {
            const messagesData = await fetch(`${BASE_URL}`);
            const messages = await messagesData.json();
            let messageData = '';
            Object.values(messages).forEach((message) => {
                messageData += `${message.author}: ${message.content}\n`;
            })
            messageArea.value = messageData.trim();

        } catch (err) {
            console.log(err);
        }
    }
}

attachEvents();
