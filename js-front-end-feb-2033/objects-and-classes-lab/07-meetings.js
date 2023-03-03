function meetings(meetingsArr) {
    let meetings = {};

    for (let str of meetingsArr) {
        let [weekday, name] = str.split(" ");

        if (meetings.hasOwnProperty(weekday)) {
            console.log(`Conflict on ${weekday}!`);
        } else {
            meetings[weekday] = name;
            console.log(`Scheduled for ${weekday}`);
        }
    }

    Object.entries(meetings).forEach(([key, value]) =>
        console.log(`${key} -> ${value}`)
    );
}

meetings(["Monday Peter", "Wednesday Bill", "Monday Tim", "Friday Tim"]);
// meetings([
//     "Friday Bob",
//     "Saturday Ted",
//     "Monday Bill",
//     "Monday John",
//     "Wednesday George",
// ]);
