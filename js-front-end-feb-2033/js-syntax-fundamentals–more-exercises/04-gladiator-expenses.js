function gladiatorExpenses(
    lostFightsCount,
    helmetPrice,
    swordPrice,
    shieldPrice,
    armorPrice
) {
    let expensesOutput = 0;
    let shieldBreakCounter = 0;

    for (let i = 1; i <= lostFightsCount; i++) {
        if (i % 2 === 0 && i % 3 === 0) {
            expensesOutput += shieldPrice;
            if ((shieldBreakCounter + 1) % 2 === 0) {
                expensesOutput += armorPrice;
            }
            shieldBreakCounter++;
            expensesOutput += helmetPrice;
            expensesOutput += swordPrice;
        } else if (i % 2 === 0) {
            expensesOutput += helmetPrice;
        } else if (i % 3 === 0) {
            expensesOutput += swordPrice;
        }
    }

    console.log(`Gladiator expenses: ${expensesOutput.toFixed(2)} aureus`);
}

gladiatorExpenses(7, 2, 3, 4, 5);
gladiatorExpenses(23, 12.5, 21.5, 40, 200);
