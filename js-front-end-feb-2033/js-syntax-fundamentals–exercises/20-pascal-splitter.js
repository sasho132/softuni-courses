function pascalSplitter(text) {
    let output = text.split(/(?=[A-Z])/).join(", ");
    console.log(output);
}

pascalSplitter("SplitMeIfYouCanHaHaYouCantOrYouCan");
pascalSplitter("HoldTheDoor");
pascalSplitter("ThisIsSoAnnoyingToDo");
