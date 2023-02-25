function solve(dayType, age) {
    let ticketPrice;

    if (0 <= age && age <= 18) {
        if (dayType === "Weekday") {
            ticketPrice = "12$";
        } else if (dayType === "Weekend") {
            ticketPrice = "15$";
        } else {
            ticketPrice = "5$";
        }
    } else if (18 <= age && age <= 64) {
        if (dayType === "Weekday") {
            ticketPrice = "18$";
        } else if (dayType === "Weekend") {
            ticketPrice = "20$";
        } else {
            ticketPrice = "12$";
        }
    } else if (64 <= age && age <= 122) {
        if (dayType === "Weekday") {
            ticketPrice = "12$";
        } else if (dayType === "Weekend") {
            ticketPrice = "15$";
        } else {
            ticketPrice = "10$";
        }
    } else {
        ticketPrice = "Error!";
    }

    console.log(ticketPrice)
}

solve("Weekday", 42);
solve("Holiday", -12);
solve("Holiday", 15);
