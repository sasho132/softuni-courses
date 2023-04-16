function solve(numbers) {
    let numArr = numbers.split(" ");

    let average =
        numArr.reduce(
            (a, b) =>
                Number(a) + Number(b), 0
        ) / numArr.length;
    
    let filteredNumbers = numArr.filter((el) => Number(el) > average);
    if (filteredNumbers.length === 0) {
        console.log('No');
    } else {
        filteredNumbers.sort((a, b) => b - a);
        filteredNumbers.length = 5;

        console.log(filteredNumbers.join(' '));
    }
}

// solve("10 20 30 40 50");
solve('5 2 3 4 -10 30 40 50 20 50 60 60 51');
// solve('1');
// solve('-1 -2 -3 -4 -5 -6');
