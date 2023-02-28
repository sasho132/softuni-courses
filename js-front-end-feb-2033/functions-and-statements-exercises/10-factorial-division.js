function factorialDivision(num1, num2) {
    function factorialize(n) {
        if (n < 0) return -1;
        else if (n == 0) return 1;
        else {
            return n * factorialize(n - 1);
        }
    }

    let division = (a, b) => a / b;

    console.log(division(factorialize(num1), factorialize(num2)).toFixed(2));
}

factorialDivision(5, 2);
factorialDivision(6, 2);
