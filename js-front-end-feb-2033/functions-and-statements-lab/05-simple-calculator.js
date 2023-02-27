function calculator(numOne, numTwo, operator) {
    let multiply = (a, b) => a * b;
    let divide = (a, b) => a / b;
    let add = (a, b) => a + b;
    let subtract = (a, b) => a - b;

    switch (operator) {
        case "multiply":
            console.log(multiply(numOne, numTwo));
            break;
        case "divide":
            console.log(divide(numOne, numTwo));
            break;
        case "add":
            console.log(add(numOne, numTwo));
            break;
        case "subtract":
            console.log(subtract(numOne, numTwo));
            break;
    }
}

calculator(5, 5, "multiply");
calculator(40, 8, "divide");
calculator(12, 19, "add");
calculator(50, 13, "subtract");
