function circleArea(num) {
    let argType = typeof num;
    let result;
    if (argType !== 'number') {
        console.log(
            `We can not calculate the circle area, because we receive a ${argType}.`
        );
    } else {
        result = Math.pow(num, 2) * Math.PI;
        console.log(result.toFixed(2));
    }
}

circleArea(5);
circleArea("name");
