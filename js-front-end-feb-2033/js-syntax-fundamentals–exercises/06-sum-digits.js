function sumDigits(num) {
    let totalSum = 0;
    let numString = num.toString();

    for (const number of numString) {
        totalSum += Number(number);
    }

    console.log(totalSum);
}

sumDigits(245678);
sumDigits(97561);
sumDigits(543);
