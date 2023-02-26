function wordsUpper(text) {
    let textUppercase = text.toUpperCase();
    let output = [];
    let matches = textUppercase.match(/[A-Za-z0-9]+/gm);

    matches.forEach((word) => {
        output.push(word);
    });

    console.log(output.join(", "));
}

wordsUpper("Hi, how are you?");
wordsUpper("hello");
