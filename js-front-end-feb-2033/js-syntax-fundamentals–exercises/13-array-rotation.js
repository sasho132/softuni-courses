function arrayRotation(numbersArray, num) {
    let resultArray = numbersArray;

    if (numbersArray.length === num) {
        resultArray = numbersArray;
    } else {
        for (let i = 1; i <= num; i++) {
            resultArray.push(resultArray.shift());
        }
    }
    console.log(resultArray.join(" "));
}

arrayRotation([51, 47, 32, 61, 21], 2);
arrayRotation([32, 21, 61, 1], 4);
arrayRotation([2, 4, 15, 31], 5);
