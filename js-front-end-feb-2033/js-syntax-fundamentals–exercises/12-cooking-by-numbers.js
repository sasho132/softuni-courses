function cookingByNumbers(strNumber, ...actions) {
    let number = Number(strNumber);

    for (const action of actions) {
        if (action === "chop") {
            number /= 2;
        } else if (action === "dice") {
            number = Math.sqrt(number);
        } else if (action === "spice") {
            number += 1;
        } else if (action === "bake") {
            number *= 3;
        } else if (action === "fillet") {
            number -= number * 0.2;
        }
        console.log(number);
    }
}

cookingByNumbers("32", "chop", "chop", "chop", "chop", "chop");
cookingByNumbers("9", "dice", "spice", "chop", "bake", "fillet");
