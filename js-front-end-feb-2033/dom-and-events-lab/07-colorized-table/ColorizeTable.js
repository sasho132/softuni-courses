function colorize() {
    let oddRows = document.querySelectorAll("tr:nth-child(even)");

    Object.values(oddRows).map((td) => td.style.backgroundColor = "teal");
    return;
}