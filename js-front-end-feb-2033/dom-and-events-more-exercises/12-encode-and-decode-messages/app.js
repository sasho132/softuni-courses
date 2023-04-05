function encodeAndDecodeMessages() {
    const messageContainer = document.querySelector(
        "#main > div:nth-child(1) > textarea:nth-child(2)"
    );
    const encodedMessageContainer = document.querySelector(
        "#main > div:nth-child(2) > textarea:nth-child(2)"
    );
    const encodeBtn = document.querySelector(
        "#main > div:nth-child(1) > button:nth-child(3)"
    );
    const decodeBtn = document.querySelector(
        "#main > div:nth-child(2) > button:nth-child(3)"
    );

    encodeBtn.addEventListener("click", encodeMessage);
    decodeBtn.addEventListener("click", decodeMessage);

    function encodeMessage() {
        const message = Array.from(messageContainer.value);
        let result = [];
        for (let el of message) {
            let currentCode = el.charCodeAt(0) + 1;
            let currentElement = String.fromCharCode(currentCode);
            result.push(currentElement); 
        }
        messageContainer.value = '';
        encodedMessageContainer.value = result.join('');
    }

    function decodeMessage() {
        const message = Array.from(encodedMessageContainer.value);
        let result = [];
        for (let el of message) {
            let currentCode = el.charCodeAt(0) - 1;
            let currentElement = String.fromCharCode(currentCode);
            result.push(currentElement); 
        }
        encodedMessageContainer.value = result.join('');
    }
}
