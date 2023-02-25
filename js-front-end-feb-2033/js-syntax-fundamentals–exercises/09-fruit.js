function solve(fruitType, weight, price) {
    let weightInKilograms = weight / 1000;
    let moneyNeed = weightInKilograms * price;
    console.log(
        `I need $${moneyNeed.toFixed(2)} to buy ${weightInKilograms.toFixed(
            2
        )} kilograms ${fruitType}.`
    );
}

solve("orange", 2500, 1.8);
solve("apple", 1563, 2.35);
