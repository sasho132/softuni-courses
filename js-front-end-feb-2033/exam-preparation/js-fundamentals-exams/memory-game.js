function solve(arr) {
    let elements = arr.shift().split(' ');

    let win = false;
    let numberOfTurns = 0;
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 'end') {
            break;
        }
        numberOfTurns++;

        let currentIndexes = arr[i].split(' ');
        let firstIndex = Number(currentIndexes[0]);
        let secondIndex = Number(currentIndexes[1]);

        if (
            elements[firstIndex] === undefined || 
            elements[secondIndex] === undefined || 
            firstIndex === secondIndex
            ) {
                let half = Math.ceil(elements.length / 2);
                let elementsToAdd = [`-${numberOfTurns}a`, `-${numberOfTurns}a`];
                elements.splice(half, 0, ...elementsToAdd);
                console.log("Invalid input! Adding additional elements to the board");
        } else if (elements[firstIndex] === elements[secondIndex]) {
            let currentMatch = elements[firstIndex];
            let removeValFromIndex = [firstIndex, secondIndex];
            elements = elements.filter((_value, index) => {
                return !removeValFromIndex.includes(index);
            })
            // elements.splice(firstIndex, 1);
            // elements.splice(secondIndex, 1);
            console.log(`Congrats! You have found matching elements - ${currentMatch}!`);
        } else if (elements[firstIndex] !== elements[secondIndex]) {
            console.log('Try again!');
        }

        if (elements.length === 0) {
            win = true;
            break;
        }
    }

    if (win) {
        console.log(`You have won in ${numberOfTurns} turns!`);
    } else {
        console.log('Sorry you lose :(');
        console.log(`${elements.join(' ')}`);
    }
}

// solve([
//     '1 1 2 2 3 3 4 4 5 5',
//     '1 0',
//     '-1 0',
//     '1 0',
//     '1 0',
//     '1 0', 
//     'end'
// ])

// solve(['a 2 4 a 2 4',
// '0 3',
// '0 2',
// '0 1',
// '0 1',
// 'end'
// ])

solve(['a 2 4 a 2 4', 
'4 0',
'0 2',
'0 1',
'0 1', 
'end'
])