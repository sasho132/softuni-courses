function solve() {
    const output = document.getElementById("output");
    const input = document.getElementById("input");
    let text = Array.from(input.value.split("."));

    let chunkSize = 3;
    for (let i = 0; i < text.length; i += chunkSize) {
        let chunk = text.slice(i, i + chunkSize).filter((el) => el !== "").join(".");
        if (chunk.length > 0) {
          let p = document.createElement("p");
        chunk += ".";
        p.textContent = chunk;
        output.appendChild(p);
        }      
    }
    input.value = "";
}
