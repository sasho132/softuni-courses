function editElement(htmlElement, textToReplace, replacer) {
    let elText = htmlElement.textContent;

    while (elText.includes(textToReplace)) {
        elText = elText.replace(textToReplace, replacer);
    }

    htmlElement.textContent = elText;
}