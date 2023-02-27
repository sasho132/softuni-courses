function oddEvenSum(num) {
    let numArray = Array.from(String(num));
    let oddSum = 0;
    let evenSum = 0;

    for (let i = 0; i < numArray.length; i++) {
        let currentNum = parseInt(numArray[i]);
        if (currentNum % 2 === 0) {
            evenSum += currentNum;
        } else {
            oddSum += currentNum;
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddEvenSum(1000435);
oddEvenSum(3495892137259234);
