function solve() {
    const selection = document.getElementById("selectMenuTo");
    const convertBtn = document.querySelector(
        "#container > button:nth-child(8)"
    );
    const decimalInput = document.getElementById('input');
    const resultContainer = document.getElementById("result");
    const binaryOption = document.createElement("option");
    const hexadecimalOption = document.createElement("option");

    binaryOption.value = "binary";
    binaryOption.textContent = "Binary";
    hexadecimalOption.value = "hexadecimal";
    hexadecimalOption.textContent = "Hexadecimal";

    selection.appendChild(binaryOption);
    selection.appendChild(hexadecimalOption);

    convertBtn.addEventListener("click", convert);

    function convert() {
        if (selection.value === "binary") {
            let decimal = decimalInput.value;
            let binary = '';
            while (decimal > 0) {
                if (decimal % 2 == 1) {
                    binary = "1" + binary;
                } else {
                    binary = "0" + binary;
                }
                decimal = Math.floor(decimal / 2);
            }
            return resultContainer.value = binary;
        } else if (selection.value === 'hexadecimal') {
            let decimal = Number(decimalInput.value);
            let result = decimal.toString(16).toUpperCase();
            return resultContainer.value = result;
        }
    }
}
