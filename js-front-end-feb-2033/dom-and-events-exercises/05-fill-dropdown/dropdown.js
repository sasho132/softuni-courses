function addItem() {
    const itemText = document.getElementById("newItemText");
    const itemValue = document.getElementById("newItemValue");
    const menuSelector = document.getElementById("menu");
    let newOption = document.createElement("option");
    newOption.textContent = itemText.value;
    newOption.value = itemValue.value;
    menuSelector.appendChild(newOption);

    itemText.value = "";
    itemValue.value = "";
}