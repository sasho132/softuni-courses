function spiceMustFlow(startingYield) {
    let totalAmount = 0;
    let totalDays = 0;

    let yield = startingYield;

    while (yield >= 100) {
        totalDays += 1;
        totalAmount += yield;
        yield -= 10;
        totalAmount -= 26;
    }

    if (totalAmount - 26 >= 0) {
        totalAmount -= 26;
    }
    
    console.log(totalDays);
    console.log(totalAmount);
}

spiceMustFlow(111);
spiceMustFlow(450);
