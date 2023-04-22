function solve(arr) {
    let horses = arr.shift().split('|');

    for (let command of arr) {
        if (command === 'Finish') {
            break;
        }

        let currentData = command.split(' ');
        let action = currentData.shift();

        if (action === 'Retake') {
            retake(currentData);
        } else if (action === 'Trouble') {
            trouble(currentData);
        } else if (action === 'Rage') {
            rage(currentData);
        } else if (action === 'Miracle') {
            miracle();
        }
    }

    let winner = horses[horses.length - 1];
    console.log(horses.join('->'));
    console.log(`The winner is: ${winner}`);

    function retake(data) {
        let [ firstHorseName, secondHorseName ] = [data[0], data[1]];
        let firstHorseIndex = horses.indexOf(firstHorseName);
        let secondHorseIndex = horses.indexOf(secondHorseName);
        
        if (firstHorseIndex < secondHorseIndex) {
            [horses[firstHorseIndex], horses[secondHorseIndex]] = [horses[secondHorseIndex], horses[firstHorseIndex]];
            console.log(`${firstHorseName} retakes ${secondHorseName}.`);
        }
        
    }

    function trouble(data) {
        let horseName = data[0];
        let horseIndex = horses.indexOf(horseName);
        if (horseIndex !== 0) {
            horses.splice(horseIndex, 1);
            horses.splice(horseIndex - 1, 0, horseName);
            console.log(`Trouble for ${horseName} - drops one position.`);
        }
    }

    function rage(data) {
        let horseName = data[0];
        let horseIndex = horses.indexOf(horseName);
        if (horseIndex !== horses.length - 1) {
            if ((horseIndex + 2) < horses.length) {
                horses.splice(horseIndex, 1);
                horses.splice(horseIndex + 2, 0, horseName);
            } else {
                horses.splice(horseIndex, 1);
                horses.push(horseName);
            }
        }
        console.log(`${horseName} rages 2 positions ahead.`);

    }


    function miracle() {
        let horseIndex = 0;
        let horseName = horses[0];

        horses.splice(horseIndex, 1);
        horses.push(horseName);
        
        console.log(`What a miracle - ${horseName} becomes first.`);
    }
}

solve(['Bella|Alexia|Sugar',
'Retake Alexia Sugar',
'Rage Alexia',
'Trouble Bella',
'Finish']);

// solve(['Onyx|Domino|Sugar|Fiona',
// 'Trouble Onyx',
// 'Retake Onyx Sugar',
// 'Rage Domino',
// 'Miracle',
// 'Finish']);

// solve(['Fancy|Lilly',
// 'Retake Lilly Fancy',
// 'Trouble Lilly',
// 'Trouble Lilly',
// 'Finish',
// 'Rage Lilly']);

