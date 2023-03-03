function numberModification(num) {
    let myFunc = (num) => Number(num);
    let intArr = Array.from(String(num), myFunc);
    let average = intArr.reduce((a, b) => a + b, 0) / intArr.length;

    while (average < 5) {
        average = intArr.reduce((a, b) => a + b, 0) / intArr.length;
        if (average > 5) {
            break;
        }
        intArr.push(9);
    }

    console.log(intArr.join(""));
}

numberModification(101);
numberModification(5835);
