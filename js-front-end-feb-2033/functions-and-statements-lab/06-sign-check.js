function signCheck(numOne, numTwo, numThree) {
    let result = (a, b, c) => a * b * c;

    if (result(numOne, numTwo, numThree) > 0) {
        console.log("Positive");
    } else {
        console.log("Negative");
    }
}

signCheck(5, 12, -15);
signCheck(-6, -12, 14);
signCheck(-1, -2, -3);
