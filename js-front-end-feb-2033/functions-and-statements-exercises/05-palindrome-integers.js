function palindromeInt(arr) {
    for (const num of arr) {
        let validator = true;
        let currentNum = String(num);
        let reversedNum = String(num).split("").reverse().join("");
        for (let i = 0; i < currentNum.length; i++) {
            if (currentNum[i] !== reversedNum[i]) {
                validator = false;
                break;
            }
        }
        if (validator) {
            console.log(true);
        } else {
            console.log(false);
        }
    }
}

palindromeInt([123, 323, 421, 121]);
palindromeInt([32, 2, 232, 1010]);
