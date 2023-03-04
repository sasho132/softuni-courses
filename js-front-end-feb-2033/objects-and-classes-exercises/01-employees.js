function employees(names) {
    let employees = {};

    names.forEach((el) => {
        employees[el] = String(el).length;
    });

    Object.entries(employees).forEach(([name, number]) => {
        console.log(`Name: ${name} -- Personal Number: ${number}`);
    });
}

employees([
    "Silas Butler",
    "Adnaan Buckley",
    "Juan Peterson",
    "Brendan Villarreal",
]);

employees(["Samuel Jackson", "Will Smith", "Bruce Willis", "Tom Holland"]);
