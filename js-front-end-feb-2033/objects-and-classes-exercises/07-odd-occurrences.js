function oddOccurrences(text) {
    let textArr = text.split(" ");
    let stringsObj = {};

    for (let word of textArr) {
        let currentWord = word.toLowerCase(0);
        if (stringsObj.hasOwnProperty(currentWord)) {
            stringsObj[currentWord] += 1;
        } else {
            stringsObj[currentWord] = 1;
        }
    }

    let occStrings = Object.entries(stringsObj).filter(([, v]) => v % 2 !== 0);
    let result = [];
    occStrings.forEach(([k,]) => result.push(k));
    console.log(result.join(" "));
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
oddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');