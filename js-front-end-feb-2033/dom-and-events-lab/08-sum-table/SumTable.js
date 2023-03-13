function sumTable() {
    let columns = document.querySelectorAll("tr td:nth-child(2)");
    let totalSum = 0;
    for (let el of columns) {
        totalSum += Number(el.textContent);
    }
    
    let sumElement = document.getElementById("sum").textContent = totalSum;
    return sumElement;
}