function toggle() {
    const description = document.getElementById("extra");
    const bn = document.getElementsByClassName("button")[0];
    if (description.style.display === "none") {
        description.style.display = "block";
        bn.textContent = "Less";
    } else {
        description.style.display = "none";
        bn.textContent = "More"
    }
}