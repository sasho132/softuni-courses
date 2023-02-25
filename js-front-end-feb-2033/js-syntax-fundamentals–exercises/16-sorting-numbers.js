function sortingNumbers(arr) {
    let output = [];

    let sortedArr = [...arr].sort((a, b) => {
        return a - b;
    });

    for (let i = 1; i < arr.length + 1; i++) {
        if (i % 2 !== 0) {
            output.push(sortedArr.shift()); 
        } else {
            output.push(sortedArr.pop());
        }
    }

    return output;
}

// [-3, 65, 1, 63, 3, 56, 18, 52, 31, 48]

sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);
