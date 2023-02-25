function sameNumbers(num) {
    let numAsString = num.toString();
    let sumDigits = 0;
    let result = true;
    let firstChar = numAsString[0];

    for (const number of numAsString) {
        if (number !== firstChar) {
            result = false;
        }
        sumDigits += Number(number);
    }

    console.log(result);
    console.log(sumDigits);
}

sameNumbers(2222222);
sameNumbers(1234);
