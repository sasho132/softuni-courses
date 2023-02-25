function solve(num1, num2) {
    let result = [];
    let totalSum = 0;

    for (let i = num1; i <= num2; i++) {
        totalSum += i;
        result.push(i);
    }

    console.log(result.join(" "));
    console.log(`Sum: ${totalSum}`);
}

solve(5, 10);
solve(0, 26);
solve(50, 60);
