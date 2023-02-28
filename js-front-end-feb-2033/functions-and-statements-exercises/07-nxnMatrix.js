function nxnMatrix(num) {
    let output = [];

    for (let i = 0; i < num; i++) {
        output.push([]);
        for (let j = 0; j < num; j++) {
            output[i][j] = num;
        }
    }

    for (const row of output) {
        console.log(`${row.join(" ")}`);
    }
}

nxnMatrix(3);
nxnMatrix(7);
nxnMatrix(2);
