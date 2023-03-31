function shoppingList(shoppingData) {
    let groceries = shoppingData.shift().split("!");

    const urgent = (item) => {
        if (!groceries.includes(item)) {
            return groceries.unshift(item);
        }
    };

    const unnecessary = (item) => {
        if (groceries.includes(item)) {
            let itemIndex = groceries.indexOf(item);
            return groceries.splice(itemIndex, 1);
        }
    };

    const correct = (oldItem, newItem) => {
        if (groceries.includes(oldItem)) {
            let itemIndex = groceries.indexOf(oldItem);
            return groceries.splice(itemIndex, 1, newItem);
        }
    };

    const rearrange = (item) => {
        if (groceries.includes(item)) {
            let itemIndex = groceries.indexOf(item);
            groceries.splice(itemIndex, 1);
            return groceries.push(item)
        }
    };

    let index = 0;
    while (shoppingData[index] !== "Go Shopping!") {
        let line = shoppingData[index].split(" ");
        let action = line.shift();
        let item = line[0];
        if (action === "Urgent") {
            urgent(item);
        } else if (action === "Unnecessary") {
            unnecessary(item);
        } else if (action === "Correct") {
            let oldItem = item;
            let newItem = line[1];
            correct(oldItem, newItem);
        } else if (action === "Rearrange") {
            rearrange(item);
        }

        index++;
    }

    console.log(groceries.join(", "));
}

// shoppingList((["Tomatoes!Potatoes!Bread",
// "Unnecessary Milk",
// "Urgent Tomatoes",
// "Go Shopping!"])
// )

shoppingList([
    "Milk!Pepper!Salt!Water!Banana",
    "Urgent Salt",
    "Unnecessary Grapes",
    "Correct Pepper Onion",
    "Rearrange T",
    "Correct Tomatoes Potatoes",
    "Go Shopping!",
]);
