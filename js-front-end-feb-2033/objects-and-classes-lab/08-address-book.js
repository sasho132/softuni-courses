function addressBook(namesArr) {
    let addressBook = {};

    for (let str of namesArr) {
        let [name, address] = str.split(":");
        addressBook[name] = address;
    }

    let orderedAddressBook = Object.keys(addressBook).sort().reduce(
        (obj, key) => { 
          obj[key] = addressBook[key]; 
          return obj;
        }, 
        {}
      );
    // let orderedAddressBook = Object.entries(addressBook)
    //     .sort((a, b) => a[0].localeCompare(b[0]));

    Object.entries(orderedAddressBook).forEach(([name, address]) =>
        console.log(`${name} -> ${address}`)    
    );
}

addressBook([
    "Tim:Doe Crossing",
    "Bill:Nelson Place",
    "Peter:Carlyle Ave",
    "Bill:Ornery Rd",
]);
