function pianist(collectionArr) {
    let numberOfPieces = collectionArr.shift();
    let ownedPieces = collectionArr.slice(0, numberOfPieces);
    let piecesData = collectionArr.slice(numberOfPieces, collectionArr.length);
    let pieces = {};

    for (const p of ownedPieces) {
        let [piece, composer, key] = p.split("|");
        pieces[piece] = { composer, key };
    }

    let lineIndex = 0;
    while (piecesData[lineIndex] !== "Stop") {
        let data = piecesData[lineIndex].split("|");
        let action = data.shift();
        if (action === "Add") {
            console.log(addPiece(data));
        } else if (action === "Remove") {
            console.log(removePiece(data));
        } else if (action === "ChangeKey") {
            console.log(changePieceKey(data));
        }

        lineIndex++;
    }

    for (const piece in pieces) {
        let [composer, key] = [pieces[piece].composer, pieces[piece].key];
        console.log(`${piece} -> Composer: ${composer}, Key: ${key}`);
    }

    function addPiece(data) {
        let [piece, composer, key] = [data[0], data[1], data[2]];
        if (pieces.hasOwnProperty(piece)) {
            return `${piece} is already in the collection!`;
        } else {
            pieces[piece] = { composer, key };
            return `${piece} by ${composer} in ${key} added to the collection!`;
        }
    }

    function removePiece(data) {
        let piece = data;
        if (pieces.hasOwnProperty(piece)) {
            delete pieces[piece];
            return `Successfully removed ${piece}!`;
        } else {
            return `Invalid operation! ${piece} does not exist in the collection.`;
        }
    }

    function changePieceKey(data) {
        let [piece, newKey] = [data[0], data[1]];
        if (pieces.hasOwnProperty(piece)) {
            pieces[piece]["key"] = newKey;
            return `Changed the key of ${piece} to ${newKey}!`;
        } else {
            return `Invalid operation! ${piece} does not exist in the collection.`;
        }
    }
}

pianist([
    "3",
    "Fur Elise|Beethoven|A Minor",
    "Moonlight Sonata|Beethoven|C# Minor",
    "Clair de Lune|Debussy|C# Minor",
    "Add|Sonata No.2|Chopin|B Minor",
    "Add|Hungarian Rhapsody No.2|Liszt|C# Minor",
    "Add|Fur Elise|Beethoven|C# Minor",
    "Remove|Clair de Lune",
    "ChangeKey|Moonlight Sonata|C# Major",
    "Stop",
]);
