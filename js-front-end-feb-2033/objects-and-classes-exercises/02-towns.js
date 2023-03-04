function towns(townsArr) {
    for (let town of townsArr) {
        let townInfo = town.split(" | ");
        let townsData = {};
        townsData["town"] = townInfo[0];
        townsData["latitude"] = Number(townInfo[1]).toFixed(2);
        townsData["longitude"] = Number(townInfo[2]).toFixed(2);
        console.log(townsData);
    } 
}

towns(["Sofia | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
