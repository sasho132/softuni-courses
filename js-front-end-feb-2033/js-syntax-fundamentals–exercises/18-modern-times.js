function modernTimes(text) {
    let regex = /(?<=#)[A-Za-z]+/gm;
    let matches = text.match(regex);

    matches.forEach((word) => {
        console.log(`${word}`);
    });
}

modernTimes("Nowadays everyone uses # to tag a #special word in #socialMedia");
modernTimes(
    "The symbol # is known #variously in English-speaking #regions as the #number sign"
);
