function aliquotSum(num) {
    let sum = 0;
    for (let i = 1; i < num; i++) {
        if (num % i == 0) {
            sum += i;
        }
    }

    if (sum === num) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.");
    }
}

aliquotSum(6);
aliquotSum(28);
aliquotSum(1236498);
