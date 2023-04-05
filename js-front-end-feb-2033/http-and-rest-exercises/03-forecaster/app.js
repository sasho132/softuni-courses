function attachEvents() {
    const BASE_URL = "http://localhost:3030/jsonstore/forecaster/";
    const locationInput = document.getElementById("location");
    const forecastContainer = document.getElementById("forecast");
    const currentForecastContainer = document.getElementById("current");
    const upcomingForecastContainer = document.getElementById("upcoming");
    const getWeatherBtn = document.getElementById("submit");

    getWeatherBtn.addEventListener("click", getWeather);

    async function getWeather() {
        try {
            const locationsData = await fetch(`${BASE_URL}locations`);
            const locations = await locationsData.json();
            let searchedLocation = locations.find(
                (el) => el.name === locationInput.value
            );
            const cityCode = searchedLocation.code;
            const todayForecastData = await fetch(
                `${BASE_URL}today/${cityCode}`
            );
            const today = await todayForecastData.json();
            let conditionSymbol = getWeatherIcon(today.forecast.condition);
            let currentConditionDiv = document.createElement("div");
            currentConditionDiv.classList.add("forecasts");
            currentConditionDiv.innerHTML = `
            <span class="condition symbol">${conditionSymbol}</span>
            <span class="condition">
                <span class="forecast-data">${today.name}</span>
                <span class="forecast-data">${today.forecast.low}&#176;/${today.forecast.high}&#176</span>
                <span class="forecast-data">${today.forecast.condition}</span>
            </span>
            `;
            currentForecastContainer.appendChild(currentConditionDiv);

            const upcomingForecastData = await fetch(
                `${BASE_URL}upcoming/${cityCode}`
            );
            const upcoming = await upcomingForecastData.json();
            let upcomingConditionDiv = document.createElement("div");
            upcomingConditionDiv.classList.add("forecast-info");

            for (let day of upcoming.forecast) {
                let upcomingConditionSymbol = getWeatherIcon(day.condition);
                upcomingConditionDiv.innerHTML += `
                <span class="upcoming">
                    <span class="condition symbol">${upcomingConditionSymbol}</span>
                    <span class="forecast-data">${day.low}&#176;/${day.high}&#176</span>
                    <span class="forecast-data">${day.condition}</span>
                </span>
                `;
            }
            upcomingForecastContainer.appendChild(upcomingConditionDiv);

            forecastContainer.style.display = "block";

            function getWeatherIcon(condition) {
                if (condition === "Sunny") {
                    return "&#x2600;";
                } else if (condition === "Partly sunny") {
                    return "&#x26C5;";
                } else if (condition === "Overcast") {
                    return "&#x2601;";
                } else if (condition === "Rain") {
                    return "&#x2614;";
                }
            }

        } catch (err) {
            forecastContainer.style.display = 'block';
            forecastContainer.textContent = 'Error';
        }
    }
}

attachEvents();
