function loadingBar(num) {
    let loading = [];

    if (num === 100) {
        console.log("100% Complete!");
    } else {
        for (let i = 0; i < 10; i++) {
            let ready = num / 10;
            if (i < ready) {
                loading.push("%");
            } else {
                loading.push(".");
            }
        }
        console.log(`${num}% [${loading.join("")}]`);
        console.log("Still loading...");
    }
}

loadingBar(30);
loadingBar(50);
loadingBar(100);
