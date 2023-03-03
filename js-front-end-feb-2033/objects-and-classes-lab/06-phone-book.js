function phoneBook(arr) {
    let phoneBook = {};

    for (let index of arr) {
        let tokens = index.split(" ");
        let name = tokens[0];
        let phone = tokens[1];
        phoneBook[name] = phone;
    }

    Object.keys(phoneBook).forEach(key => {
        console.log(`${key} -> ${phoneBook[key]}`);
    })
}

phoneBook([
    "Tim 0834212554",
    "Peter 0877547887",
    "Bill 0896543112",
    "Tim 0876566344",
]);
