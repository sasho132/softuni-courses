class Laptop {
    constructor(info, quality) {
        this.info = info;
        this.isOn = false;
        this.quality = quality;
    }

    turnOn() {
        this.isOn = true;
        this.quality--;
    }

    turnOff() {
        this.isOn = false;
        this.quality--;
    }

    showInfo() {
        let jsonInfo = JSON.stringify(this.info);
        return jsonInfo;
    }

    get price() {
        let price = Number(800 - (this.info.age * 2) + (this.quality * 0.5));
        return price;
    }
    
}

let info = {producer: "Dell", age: 2, brand: "XPS"}
let laptop = new Laptop(info, 10)
laptop.turnOn()
console.log(laptop.showInfo())
laptop.turnOff()
console.log(laptop.quality)
laptop.turnOn()
console.log(laptop.isOn)
console.log(laptop.price)
