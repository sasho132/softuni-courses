function attachGradientEvents() {
    const resultDiv = document.getElementById('result');
    const gradient = document.getElementById('gradient');
    gradient.addEventListener('mousemove', gradientMove);
    gradient.addEventListener('mouseout', gradientOut);

    function gradientMove(event) {
        let power = event.offsetX / (event.target.clientWidth - 1);
        power = Math.trunc(power * 100);
        resultDiv.textContent = power + "%";
    }

    function gradientOut(event) {
        resultDiv.textContent = "";
    }
}