function listOfNames(namesArr) {
    let output = "";
    let sortedNames = namesArr.sort((a, b) => (a.localeCompare(b)));

    for (let i = 0; i < sortedNames.length; i++) {
        output += `${i + 1}.${sortedNames[i]}\n`;
    }

    console.log(output);
}

listOfNames(["John", "Bob", "Christina", "Ema"]);
