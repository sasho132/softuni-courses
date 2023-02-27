function passValidator(pass) {
    let lengthValidation = true;
    let symbolsValidation = true;
    let digitCount = 0;

    if (pass.length < 6 || pass.length > 10) {
        lengthValidation = false;
    }

    for (const symbol of pass) {
        let symbolNum = symbol.charCodeAt(0);
        if (
            symbolNum < 48 || symbolNum > 57 && 
            symbolNum < 65 || symbolNum > 90 &&
            symbolNum < 97 || symbolNum > 122
            
        ) { 
            symbolsValidation = false;
        }

        if (symbolNum >= 48 && symbolNum <= 57) {
            digitCount++;
        }
    }

    if (lengthValidation === false) {
        console.log("Password must be between 6 and 10 characters");
    }
    if (symbolsValidation === false) {
        console.log("Password must consist only of letters and digits");
    }
    if (digitCount < 2) {
        console.log("Password must have at least 2 digits");
    }
    if (lengthValidation && symbolsValidation && digitCount >= 2) {
        console.log("Password is valid");
    }
}

passValidator("logIn");
passValidator("MyPass123");
passValidator("Pa$s$s");
