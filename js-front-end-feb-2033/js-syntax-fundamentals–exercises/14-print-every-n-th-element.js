function printElement(arr, num) {
    let output = [];
    for (let i = 0; i < arr.length; i += num) {
        output.push(arr[i]);
    }
    return output;
}

printElement(["5", "20", "31", "4", "20"], 2);
printElement(["dsa", "asd", "test", "tset"], 2);
printElement(["1", "2", "3", "4", "5"], 6);
