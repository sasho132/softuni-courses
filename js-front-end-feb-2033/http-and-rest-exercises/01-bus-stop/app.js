function getInfo() {
    const stopName = document.getElementById('stopName');
    const busesList = document.getElementById('buses');
    const inputId = document.getElementById('stopId');
    const BASE_URL = "http://localhost:3030/jsonstore/bus/businfo/"
    const stopId = inputId.value;

    busesList.innerHTML = '';
    fetch(`${BASE_URL}${stopId}`)
        .then((res) => res.json())
        .then((busInfo) => {
            const { name, buses } = busInfo;
            stopName.textContent = name;

            Object.entries(buses).forEach((busNum) => {
                let li = document.createElement('li');
                li.textContent = `Bus ${busNum[0]} arrives in ${busNum[1]} minutes`;
                busesList.appendChild(li);
            })
        })
        .catch((err) => {
            stopName.textContent = 'Error';
        })

}