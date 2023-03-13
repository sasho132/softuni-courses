function extractText() {
    let items = document.querySelectorAll("ul#items li");
    let textarea = document.querySelector("#result");

    // items.forEach((item) => textarea.value += item.textContent + "\n");
    for (let item of items) {
        textarea.value += item.textContent + "\n";
    }
}
