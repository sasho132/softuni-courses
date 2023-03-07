function catalogue(prodArr) {
    let catalogue = {};

    for (let prod of prodArr) {
        let firstLetter = prod[0];
        let [prodName, prodQuantity] = prod.split(" : ");
        if (!catalogue.hasOwnProperty(firstLetter)) {
            catalogue[firstLetter] = {};
        }
        catalogue[firstLetter][prodName] = prodQuantity;
    }

    let sortedCatalogue = Object.keys(catalogue)
        .sort()
        .reduce((objEntries, key) => {
            objEntries[key] = catalogue[key];
            return objEntries;
        }, {});

    for (let [key, value] of Object.entries(sortedCatalogue)) {
        console.log(`${key}`);
        Object.keys(value)
            .sort((a, b) => {
                let nameA = a.toUpperCase(); // ignore upper and lowercase
                let nameB = b.toUpperCase(); // ignore upper and lowercase
                if (nameA < nameB) {
                    return -1;
                }
                if (nameA > nameB) {
                    return 1;
                }

                // names must be equal
                return 0;
            })
            .forEach((k) => {
                console.log(`  ${k}: ${value[k]}`);
            });
    }
}

catalogue([
    "Appricot : 20.4",
    "Fridge : 1500",
    "TV : 1499",
    "Deodorant : 10",
    "Boiler : 300",
    "Apple : 1.25",
    "Anti-Bug Spray : 15",
    "T-Shirt : 10",
]);

// catalogue(["Omlet : 5.4", "Shirt : 15", "Cake : 59"]);
