function focused() {
    let inputFields = document.querySelectorAll("input");
    let inputFieldsArr = Array.from(inputFields);

    for (let field of inputFieldsArr) {
        field.addEventListener("focus", function () {
            field.parentElement.classList.add("focused");
        });
        field.addEventListener("blur", function () {
            field.parentElement.classList.remove("focused");
        });
    }
}
