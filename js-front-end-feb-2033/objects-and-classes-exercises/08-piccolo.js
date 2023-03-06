function piccolo(arr) {
    let cars = {};

    for (let i = 0; i < arr.length; i++) {
        [action, carLicense] = arr[i].split(", ");
        cars[carLicense] = action;
    }

    let carsInParking = Object.entries(cars)
        .filter(([, v]) => v === "IN")
        .sort();

    if (Object.entries(carsInParking).length === 0) {
        console.log("Parking Lot is Empty");
    } else {
        carsInParking.forEach(([k]) => console.log(k));
    }
}

piccolo([
    "IN, CA2844AA",
    "IN, CA1234TA",
    "OUT, CA2844AA",
    "IN, CA9999TT",
    "IN, CA2866HI",
    "OUT, CA1234TA",
    "IN, CA2844AA",
    "OUT, CA2866HI",
    "IN, CA9876HH",
    "IN, CA2822UU",
]);

piccolo(["IN, CA2844AA", "IN, CA1234TA", "OUT, CA2844AA", "OUT, CA1234TA"]);
