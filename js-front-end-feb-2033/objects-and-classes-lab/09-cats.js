function cats(catsArr) {
    let cats = [];

    class Cats {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    for (let currentCat of catsArr) {
        let catInfo = currentCat.split(" ");
        let name, age;
        [name, age] = [catInfo[0], catInfo[1]];
        cats.push(new Cats(name, age));
    }

    cats.forEach((cat) => cat.meow());
}

cats(["Mellow 2", "Tom 5"]);
