function inventory(inventoryArr) {
    let heroes = [];

    for (let line of inventoryArr) {
        [heroName, level, items] = line.split(" / ");
        let hero = { Hero: heroName, level: Number(level), items: items };
        heroes.push(hero);
    }

    let sortedHeroes = heroes.sort(
        (a, b) => a.level - b.level
    );

    for (let h of sortedHeroes) {
        console.log(`Hero: ${h["Hero"]}`);
        console.log(`level => ${h["level"]}`);
        console.log(`items => ${h["items"]}`);
    }
}

inventory([
    "Isacc / 25 / Apple, GravityGun",
    "Derek / 12 / BarrelVest, DestructionSword",
    "Hes / 1 / Desolator, Sentinel, Antara",
]);

inventory([
    "Batman / 2 / Banana, Gun",
    "Superman / 18 / Sword",
    "Poppy / 28 / Sentinel, Antara",
]);
