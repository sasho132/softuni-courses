function characterInRange(char1, char2) {
    let fromChar = char1.codePointAt();
    let toChar = char2.codePointAt();
    let output = [];

    if (fromChar < toChar) {
        for (let i = fromChar + 1; i < toChar; i++) {
            output.push(String.fromCharCode(i));
        }
    } else {
        for (let i = toChar + 1; i < fromChar; i++) {
            output.push(String.fromCharCode(i));
        }
    }

    console.log(output.join(" "));
}

characterInRange("a", "d");
characterInRange("#", ":");
characterInRange("C", "#");
