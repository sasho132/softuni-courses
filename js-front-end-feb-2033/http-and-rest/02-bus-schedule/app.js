function solve() {
    const arriveBtn = document.getElementById("arrive");
    const departBtn = document.getElementById("depart");
    const BASE_URL = "http://localhost:3030/jsonstore/bus/schedule/";
    const infoContainer = document.querySelector(".info");

    let stopName = "";
    let nextStop = "depot";

    async function depart() {
        try {
            const stopInfoData = await fetch(`${BASE_URL}${nextStop}`);
            const stopInfo = await stopInfoData.json();
            stopName = stopInfo.name;
            nextStop = stopInfo.next;
            infoContainer.textContent = `Next stop ${stopName}`;

            departBtn.disabled = true;
            arriveBtn.disabled = false;
        } catch (err) {
            infoContainer.textContent = "Error";
            departBtn.disabled = true;
            arriveBtn.disabled = true;
        }
    }

    async function arrive() {
        infoContainer.textContent = `Arriving in ${stopName}`;
        
        departBtn.disabled = false;
        arriveBtn.disabled = true;
    }

    return {
        depart,
        arrive,
    };
}

let result = solve();
