function wordsTracker(wordsArr) {
    let searched = wordsArr.shift().split(" ");
    let result = {};
    for (let word of searched) {
        result[word] = 0;
    }

    for (let i of wordsArr) {
        if (result.hasOwnProperty(i)) {
            result[i]++;
        }
    }

    let orderedWords = Object.entries(result)
        .sort(([, a], [, b]) => b - a)
        .reduce(
            (obj, [key, value]) => ({
                ...obj,
                [key]: value,
            }),
            {}
        );

    for ([key, value] of Object.entries(orderedWords)) {
        console.log(`${key} - ${value}`);
    }
}

// wordsTracker([
//     "this sentence",
//     "In",
//     "this",
//     "sentence",
//     "you",
//     "have",
//     "to",
//     "count",
//     "the",
//     "occurrences",
//     "of",
//     "the",
//     "words",
//     "this",
//     "and",
//     "sentence",
//     "because",
//     "this",
//     "is",
//     "your",
//     "task",
// ]);

wordsTracker([
    "is the",
    "first",
    "sentence",
    "Here",
    "is",
    "another",
    "the",
    "And",
    "finally",
    "the",
    "the",
    "sentence",
]);
