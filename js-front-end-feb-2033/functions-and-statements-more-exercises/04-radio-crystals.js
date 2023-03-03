function radioCrystals(arr) {
    let finalThickness = arr.shift();

    let cut = (a) => a / 4;
    let lap = (a) => a - a * 0.2;
    let grind = (a) => a - 20;
    let etch = (a) => a - 2;
    let xRay = (a) => a + 1;
    let transporting = (a) => Math.floor(a);

    for (let i = 0; i < arr.length; i++) {
        let chunk = arr[i];
        console.log(`Processing chunk ${chunk} microns`);
        let cutCounter = 0;
        while (cut(chunk) >= finalThickness) {
            chunk = cut(chunk);
            cutCounter++;
        }
        if (cutCounter > 0) {
            console.log(`Cut x${cutCounter}`);
            chunk = transporting(chunk);
            console.log("Transporting and washing");
        }        

        let lapCounter = 0;
        while (lap(chunk) >= finalThickness) {
            chunk = lap(chunk);
            lapCounter++;
        }
        if (lapCounter > 0) {
            console.log(`Lap x${lapCounter}`);
            chunk = transporting(chunk);
            console.log("Transporting and washing");
        }

        let grindCounter = 0;
        while (grind(chunk) >= finalThickness) {
            chunk = grind(chunk);
            grindCounter++;
        }
        if (grindCounter > 0) {
            console.log(`Grind x${grindCounter}`);
            chunk = transporting(chunk);
            console.log("Transporting and washing");
        }

        let etchCounter = 0;
        while (chunk > finalThickness) {
            chunk = etch(chunk);
            etchCounter++;
        }
        if (etchCounter > 0) {
            console.log(`Etch x${etchCounter}`);
            chunk = transporting(chunk);
            console.log("Transporting and washing");
        }

        if (chunk < finalThickness) {
            let xRayCounter = 0;
            while (chunk < finalThickness) {
                chunk = xRay(chunk);
                xRayCounter++;
            }
            console.log(`X-ray x${xRayCounter}`);
        }

        console.log(`Finished crystal ${chunk} microns`);
    }
}

radioCrystals([1375, 50000]);
radioCrystals([1000, 4000, 8100]);