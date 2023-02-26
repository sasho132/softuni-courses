function solve(x1, x2, y1, y2) {
    
    let firstCheck = Number.isInteger(Math.sqrt(((0 - x1) ** 2) + ((0 - y1) ** 2)));
    let secondCheck = Number.isInteger(Math.sqrt(((x2 - 0) ** 2) + ((y2 - 0) ** 2)));
    let thirdCheck = Number.isInteger(Math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)));
    
    if (firstCheck) {
        console.log(`{${x1}, ${y1}} to {${0}, ${0}} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {${0}, ${0}} is invalid`);
    }
 
    if (secondCheck) {
        console.log(`{${x2}, ${y2}} to {${0}, ${0}} is valid`);
    } else {
        console.log(`{${x2}, ${y2}} to {${0}, ${0}} is invalid`);
    }
 
    if (thirdCheck) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {s
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
}

solve(3, 0, 0, 4);
solve(2, 1, 1, 1);
