function attachEventsListeners() {
    const inputDistance = document.getElementById('inputDistance');
    const outputDistance = document.getElementById('outputDistance');
    const convertBtn = document.getElementById('convert');

    const inputUnits = document.getElementById('inputUnits');
    const outputUnits = document.getElementById('outputUnits');

    convertBtn.addEventListener('click', calculateDistance);

    function calculateDistance() {
        let result = 0;
        let inputToMeters = 0;
        let distance = Number(inputDistance.value);

        switch (inputUnits.value) {
            case "km":
                inputToMeters = distance * 1000;
                break;
            case "m":
                inputToMeters = distance;
                break;
            case "cm":
                inputToMeters = distance * 0.01;
                break;
            case "mm":
                inputToMeters = distance * 0.001;
                break;
            case "mi":
                inputToMeters = distance * 1609.34;
                break;
            case "yrd":
                inputToMeters = distance * 0.9144;
                break;
            case "ft":
                inputToMeters = distance * 0.3048;
                break;
            case "in":
                inputToMeters = distance * 0.0254;
                break;
        }

        console.log(inputToMeters);

        switch (outputUnits.value) {
            case "km":
                result = inputToMeters / 1000;
                break;
            case "m":
                result = inputToMeters;
                break;
            case "cm":
                result = inputToMeters / 0.01;
                break;
            case "mm":
                result = inputToMeters / 0.001;
                break;
            case "mi":
                result = inputToMeters / 1609.34;
                break;
            case "yrd":
                result = inputToMeters / 0.9144;
                break;
            case "ft":
                result = inputToMeters / 0.3048;
                break;
            case "in":
                result = inputToMeters / 0.0254;
                break;
        }

        outputDistance.value = result;
    }
}