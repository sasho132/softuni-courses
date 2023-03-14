function create(words) {
   let contentContainer = document.getElementById("content");

   for (let word of words) {
      let divContainer = document.createElement("div");
      let p = document.createElement("p");
      let node = document.createTextNode(word);
      p.appendChild(node);
      p.style.display = "none";
      divContainer.appendChild(p);

      divContainer.addEventListener("click", function(e) {
         e.target.children[0].style.display = "";
      })
      contentContainer.appendChild(divContainer);
   }
}
