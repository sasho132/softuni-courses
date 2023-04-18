function solve(arr) {
    const targetValues = arr
        .shift()
        .split(' ')
        .map((el) => Number(el));

    for (let command of arr) {
        if (command === 'End') {
            break;
        }

        let [ action, ...data ] = command.split(' ');
        if (action === 'Shoot') {
            shoot(data);
        } else if (action === 'Add') {
            add(data);
        } else if (action === 'Strike') {
            strike(data);
        }
    }

    console.log(targetValues.join('|'));

    function shoot(data) {
        let [ index, power ] = [ Number(data[0]), Number(data[1]) ];
        if (targetValues[index] !== undefined) {
            targetValues[index] -= power;
            if (targetValues[index] <= 0) {
                targetValues.splice(index, 1);
            }
        }
    }

    function add(data) {
       let [ index, value ] = [ Number(data[0]), Number(data[1]) ];
        if (targetValues[index] !== undefined) {
            targetValues.splice(index, 0, value);
        } else {
            console.log("Invalid placement!");
        }
    }

    function strike(data) {
        let [ index, radius ] = [ Number(data[0]), Number(data[1]) ];
        if (
            targetValues[index] !== undefined &&
            targetValues[index - radius] !== undefined &&
            targetValues[index + radius] !== undefined
        ) {
            let indexFrom = index - radius;
            let indexTo = (radius * 2) + 1;
            targetValues.splice(indexFrom, indexTo);
        } else {
            console.log("Strike missed!");
        }
    }
}

// solve(["52 74 23 44 96 110",
// "Shoot 5 10",
// "Shoot 1 80",
// "Strike 2 1",
// "Add 22 3",
// "End"]);

solve(["1 2 3 4 5",
"Strike 0 1",
"End"])
