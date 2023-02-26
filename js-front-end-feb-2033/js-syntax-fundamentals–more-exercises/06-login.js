function login(arr) {
    let username = arr.shift();
    let reversedUsername = username.split("").reverse().join("");

    for (let i = 0; i <= 3; i++) {
        if (arr[i] === reversedUsername) {
            console.log(`User ${username} logged in.`);
            break;
        } else {
            if (i === 3) {
                console.log(`User ${username} blocked!`)
            } else {
                console.log("Incorrect password. Try again.");
            }
        }
    }
}

// login(['Acer','login','go','let me in','recA']);
// login(['momo','omom']);
login(['sunny','rainy','cloudy','sunny','not sunny']);