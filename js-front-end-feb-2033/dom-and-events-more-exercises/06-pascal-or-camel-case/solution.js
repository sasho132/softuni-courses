function solve() {
    let input = document.getElementById("text").value.split(", ");
    let currentCase = document.getElementById("naming-convention").value;
    let result = document.getElementById("result");

    let arr = input[0].split(" ");
    let toLower = arr.map((el) => el.toLowerCase(0));
    let convertStr = toLower.map(
        (el) => el.charAt(0).toUpperCase() + el.slice(1)
    );
    let convertToStr = convertStr.join("");

    if (currentCase === "Camel Case") {
        let resultStr =
            convertToStr.charAt(0).toLowerCase() + convertToStr.slice(1);
        result.textContent = resultStr;
    } else if (currentCase === "Pascal Case") {
      result.textContent = convertToStr;
    } else {
      result.textContent = "Error!";
    }
}
