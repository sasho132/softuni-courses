function solve() {
    document.querySelector("#searchBtn").addEventListener("click", onClick);

    function onClick() {
        const searchInCells = Array.from(
            document.querySelectorAll(".container > tbody > tr > td")
        );
        const input = document.getElementById("searchField");
        let searched = input.value;
        console.log(searched);

        searchInCells.map((el) => {
            if (el.textContent.includes(searched)) {
                const row = el.parentElement;
                row.setAttribute("class", "select");
            }
        });

        input.value = "";
    }
}
