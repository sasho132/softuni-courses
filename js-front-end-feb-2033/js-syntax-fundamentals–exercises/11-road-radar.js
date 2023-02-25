function roadRadar(speed, area) {
    let speedLimit;
    let status;
    let difference;

    switch (area) {
        case "motorway":
            speedLimit = 130;
            break;
        case "interstate":
            speedLimit = 90;
            break;
        case "city":
            speedLimit = 50;
            break;
        case "residential":
            speedLimit = 20;
            break;
    }

    if (speed <= speedLimit) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    } else {
        difference = speed - speedLimit;
        if (speed > speedLimit && speed <= speedLimit + 20) {
            status = "speeding";
        } else if (speed > speedLimit &&  speed <= speedLimit + 40) {
            status = "excessive speeding";
        } else {
            status = "reckless driving";
        }
        console.log(
            `The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`
        );
    }
}

roadRadar(40, "city");
roadRadar(21, "residential");
roadRadar(120, "interstate");
roadRadar(200, "motorway");
