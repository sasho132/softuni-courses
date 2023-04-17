function solve(arr) {
    let num = arr.shift();
    let plantsData = {};

    for (let i = 0; i < num; i++) {
        let [ plant, rarity ] = arr.shift().split('<->');
        plantsData[plant] = {rarity: rarity, rating: []};
    }

    for (let i = 0; i < arr.length; i++) {
        let currentCommand = arr[i];
        if (currentCommand === 'Exhibition') {
            break;
        }

        let [ action, data ] = currentCommand.split(': ');
        if (action === 'Rate') {
            let [ plant, rating ] = data.split(' - ');
            if (!plantsData.hasOwnProperty(plant)) {
                console.log('error');
            } else {
                plantsData[plant].rating.push(Number(rating));
            }
        } else if (action === 'Update') {
            let [ plant, newRarity ] = data.split(' - ');
            if (!plantsData.hasOwnProperty(plant)) {
                console.log('error');
            } else {
                plantsData[plant].rarity = newRarity;
            }
        } else if (action === 'Reset') {
            let plant = data;
            if (!plantsData.hasOwnProperty(plant)) {
                console.log('error');
            } else {
                plantsData[plant].rating = [];
            }
        }
    }

    console.log('Plants for the exhibition:');
    for (let el in plantsData) {
        let plantName = el;
        let rarity = plantsData[el].rarity;
        let averageRating = 0;
        if (plantsData[el].rating.length) {
            averageRating = plantsData[el].rating.reduce(
            (a, b) => a + b, 0
            ) / plantsData[el].rating.length;
        }

        console.log(`- ${plantName}; Rarity: ${rarity}; Rating: ${averageRating.toFixed(2)}`);
    }
}

solve(["3",
"Arnoldii<->4",
"Woodii<->7",
"Welwitschia<->2",
"Rate: Woodii - 10",
"Rate: Welwitschia - 7",
"Rate: Arnoldii - 3",
"Rate: Woodii - 5",
"Update: Woodii - 5",
"Reset: Arnoldii",
"Exhibition"]);

// solve(["2",
// "Candelabra<->10",
// "Oahu<->10",
// "Rate: Oahu - 7",
// "Rate: Candelabra - 6",
// "Exhibition"]);

