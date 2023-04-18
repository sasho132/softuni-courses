function solve(arr) {
    const numberOfCars = Number(arr.shift());
    let cars = {};

    for (let i = 0; i < numberOfCars; i++) {
        let [ car, mileage, fuel ] = arr.shift().split('|');
        cars[car] = {mileage: Number(mileage), fuel: Number(fuel)};
    }

    for (let el of arr) {
        if (el === 'Stop') {
            break;
        }

        let currentData = el.split(' : ');
        let action = currentData.shift();

        if (action === 'Drive') {
            driveCar(currentData);
        } else if (action === 'Refuel') {
            refuelCar(currentData);
        } else if (action === 'Revert') {
            revertCar(currentData);
        }
    }

    Object.keys(cars).forEach((car) => {
        let mileage = cars[car].mileage;
        let fuel = cars[car].fuel;
        console.log(`${car} -> Mileage: ${mileage} kms, Fuel in the tank: ${fuel} lt.`)
    });

    function driveCar(data) {
        let [ car, distance, fuel ] = [ data[0], Number(data[1]), Number(data[2]) ];

        if (cars[car].fuel < fuel) {
            console.log('Not enough fuel to make that ride');
        } else {
            cars[car].mileage += distance;
            cars[car].fuel -= fuel;
            console.log(
                `${car} driven for ${distance} kilometers. ${fuel} liters of fuel consumed.`
            );
            if (cars[car].mileage >= 100000) {
                delete cars[car];
                console.log(`Time to sell the ${car}!`);
            }
        }
    }

    function refuelCar(data) {
        let [ car, fuel ] = [ data[0], Number(data[1]) ];

        let maximumTankCapacity = 75;
        if ((cars[car].fuel + fuel) > maximumTankCapacity) {
            fuel = maximumTankCapacity - cars[car].fuel;
        }

        cars[car].fuel += fuel;
        console.log(`${car} refueled with ${fuel} liters`);
    }

    function revertCar(data) {
        let [ car, kilometers ] = [ data[0], Number(data[1]) ];
        let minimumMileage = 10000;
        if ((cars[car].mileage - kilometers) < minimumMileage) {
            cars[car].mileage = minimumMileage;
        } else {
            cars[car].mileage -= kilometers;
            console.log(`${car} mileage decreased by ${kilometers} kilometers`);
        }
    }
}

// solve([
//     '3',
//     'Audi A6|38000|62',
//     'Mercedes CLS|11000|35',
//     'Volkswagen Passat CC|45678|5',
//     'Drive : Audi A6 : 543 : 47',
//     'Drive : Mercedes CLS : 94 : 11',
//     'Drive : Volkswagen Passat CC : 69 : 8',
//     'Refuel : Audi A6 : 50',
//     'Revert : Mercedes CLS : 500',
//     'Revert : Audi A6 : 30000',
//     'Stop'
//   ]);

solve([
    '4',
    'Lamborghini Veneno|11111|74',
    'Bugatti Veyron|12345|67',
    'Koenigsegg CCXR|67890|12',
    'Aston Martin Valkryie|99900|50',
    'Drive : Koenigsegg CCXR : 382 : 82',
    'Drive : Aston Martin Valkryie : 99 : 23',
    'Drive : Aston Martin Valkryie : 2 : 1',
    'Refuel : Lamborghini Veneno : 40',
    'Revert : Bugatti Veyron : 2000',
    'Stop'
]);