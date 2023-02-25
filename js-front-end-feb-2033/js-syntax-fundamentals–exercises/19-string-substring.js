function stringSubstring(searchedWord, text) {
    let lowerText = text.toLowerCase().split(" ");
    let lowerWord = searchedWord.toLowerCase();
    let found = false;

    for (const word of lowerText) {
        if (word === lowerWord) {
            found = true;
            break;
        }
    }

    if (found) {
        console.log(searchedWord);
    } else {
        console.log(`${searchedWord} not found!`);
    }
}

stringSubstring("javascript", "JavaScript is the best programming language");
stringSubstring("python", "JavaScript is the best programming language");
