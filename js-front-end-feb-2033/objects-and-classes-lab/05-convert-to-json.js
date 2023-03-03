function jsonConverter(name, lastName, hairColor) {
    let person = {
        name,
        lastName,
        hairColor,
    };

    console.log(JSON.stringify(person));
}

jsonConverter("George", "Jones", "Brown");
jsonConverter("Peter", "Smith", "Blond");
