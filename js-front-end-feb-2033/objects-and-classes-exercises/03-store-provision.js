function storeProvision(stock, orderedStock) {
    let items = {};

    for (let i = 1; i <= stock.length; i++) {
        if (i % 2 !== 0) {
            items[stock[i - 1]] = Number(stock[i]);
        }
    }

    for (let i = 1; i <= orderedStock.length; i++) {
        if (i % 2 !== 0 && items.hasOwnProperty(orderedStock[i - 1])) {
            items[orderedStock[i - 1]] += Number(orderedStock[i]);
        } else if (i % 2 !== 0) {
            items[orderedStock[i - 1]] = Number(orderedStock[i]);
        }
    }

    Object.entries(items).forEach(([key, value]) => {
        console.log(`${key} -> ${value}`)
    });
}

storeProvision(
    ["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
    [
        "Flour",
        "44",
        "Oil",
        "12",
        "Pasta",
        "7",
        "Tomatoes",
        "70",
        "Bananas",
        "30",
    ]
);
