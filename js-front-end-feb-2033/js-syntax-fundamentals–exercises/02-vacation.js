function solve(group, groupType, dayOfWeek) {
    let singlePersonPrice = 0;
    let totalPrice = 0;

    if (groupType === "Students") {
        if (dayOfWeek === "Friday") {
            singlePersonPrice = 8.45;
        } else if (dayOfWeek === "Saturday") {
            singlePersonPrice = 9.80;
        } else if (dayOfWeek == "Sunday") {
            singlePersonPrice = 10.46;
        }
    } else if (groupType === "Business") {
        if (dayOfWeek === "Friday") {
            singlePersonPrice = 10.90;
        } else if (dayOfWeek === "Saturday") {
            singlePersonPrice = 15.6;
        } else if (dayOfWeek == "Sunday") {
            singlePersonPrice = 16;
        }
    } else if (groupType === "Regular") {
        if (dayOfWeek === "Friday") {
            singlePersonPrice = 15;
        } else if (dayOfWeek === "Saturday") {
            singlePersonPrice = 20;
        } else if (dayOfWeek == "Sunday") {
            singlePersonPrice = 22.5;
        }
    }

    totalPrice = singlePersonPrice * group;
    if (groupType === "Students" && group >= 30) {
        totalPrice -= totalPrice * 0.15;
    } else if (groupType === "Business" && group >= 100) {
        totalPrice -= singlePersonPrice * 10;
    } else if (groupType === "Regular" && group >= 10 && group <= 20) {
        totalPrice -= totalPrice * 0.05;
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

solve(30, "Students", "Sunday");
solve(40, "Regular", "Saturday");
