function revealWords(replaceWords, text) {
    let wordsArr = replaceWords.split(", ");

    for (const word of wordsArr) {
        text = text.replace("*".repeat(word.length), word);
    }
    console.log(text);
}

revealWords(
    "great",
    "softuni is ***** place for learning new programming languages"
);

revealWords(
    "great, learning",
    "softuni is ***** place for ******** new programming languages"
);
