function bitcoinMining(shiftArr) {
    let bitcoinInLv = 11949.16;
    let goldPriceForGram = 67.51;
    let totalAmount = 0;
    let firstBitcoinDay = 0;
    let boughtBitcoins = 0;

    for (let i = 0; i < shiftArr.length; i++) {
        let goldForDay = shiftArr[i];
        if ((i + 1) % 3 === 0) {
            goldForDay -= goldForDay * 0.3;
        }
        let moneyForDay = goldForDay * goldPriceForGram;

        totalAmount += moneyForDay;
        if (totalAmount >= bitcoinInLv) {
            while (totalAmount >= bitcoinInLv) {
                totalAmount -= bitcoinInLv;
                boughtBitcoins++;
                if (firstBitcoinDay === 0) {
                    firstBitcoinDay = i + 1;
                }
            }
        }
    }

    console.log(`Bought bitcoins: ${boughtBitcoins}`);
    if (firstBitcoinDay > 0) {
        console.log(`Day of the first purchased bitcoin: ${firstBitcoinDay}`);
    }
    console.log(`Left money: ${totalAmount.toFixed(2)} lv.`);
}

bitcoinMining([100, 200, 300]);
bitcoinMining([50, 100]);
bitcoinMining([3124.15, 504.212, 2511.124]);
