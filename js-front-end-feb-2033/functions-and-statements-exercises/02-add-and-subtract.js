function sumAndSubtract(num1, num2, num3) {
    let sum = (a, b) => a + b;
    let subtract = (a, b) => a - b;
    let result = subtract(sum(num1, num2), num3);

    return result;
}

console.log(sumAndSubtract(23, 6, 10));
console.log(sumAndSubtract(1, 17, 30));
console.log(sumAndSubtract(42, 58, 100));
