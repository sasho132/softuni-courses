function objConverter(jsonFile) {
    let person = JSON.parse(jsonFile);
    let entries = Object.entries(person);

    entries.forEach(([key, value]) => {
        console.log(`${key}: ${value}`);
    });
}

objConverter('{"name": "George", "age": 40, "town": "Sofia"}');
objConverter('{"name": "Peter", "age": 35, "town": "Plovdiv"}');
