function attachEventsListeners() {
    const daysInput = document.getElementById('days');
    const hoursInput = document.getElementById('hours');
    const minutesInput = document.getElementById('minutes');
    const secondsInput = document.getElementById('seconds');

    const daysBtn = document.getElementById('daysBtn');
    const hoursBtn = document.getElementById('hoursBtn');
    const minutesBtn = document.getElementById('minutesBtn');
    const secondsBtn = document.getElementById('secondsBtn');

    daysBtn.addEventListener('click', daysHandler);
    hoursBtn.addEventListener('click', hoursHandler);
    minutesBtn.addEventListener('click', minutesHandler);
    secondsBtn.addEventListener('click', secondsHandler);

    function daysHandler() {
        let hours = Number(daysInput.value) * 24;
        let minutes = Number(daysInput.value * 1440);
        let seconds = Number(daysInput.value * 86400 );

        hoursInput.value = hours;
        minutesInput.value = minutes;
        secondsInput.value = seconds;
    }

    function hoursHandler() {
        let days = Number(hoursInput.value) / 24;
        let minutes = Number(hoursInput.value * 60);
        let seconds = Number(hoursInput.value * 3600);

        daysInput.value = days;
        minutesInput.value = minutes;
        secondsInput.value = seconds;
    }

    function minutesHandler() {
        let days = Number(minutesInput.value) / 1440;
        let hours = Number(minutesInput.value / 60);
        let seconds = Number(minutesInput.value * 60);

        daysInput.value = days;
        hoursInput.value = hours;
        secondsInput.value = seconds;
    }

    function secondsHandler() {
        let days = Number(secondsInput.value / 86400);
        let hours = Number(secondsInput.value / 3600);
        let minutes = Number(secondsInput.value / 60);

        daysInput.value = days;
        hoursInput.value = hours;
        minutesInput.value = minutes;
    }
}