function search() {
   const input = document.getElementById('searchText');
   const result = document.getElementById('result');
   const townsList = document.querySelectorAll('#towns li');
   let matches = 0;

   for (let town of townsList) {
      if (town.textContent.includes(input.value)) {
         town.style.fontStyle = "bold|underline";
         matches++; 
      }
   }

   result.textContent = `${matches} matches found`;
}
