function solve() {
   const productsAddBtn = Array.from(document.querySelectorAll('.add-product'));
   let result = document.querySelector('.shopping-cart > textarea:nth-child(5)');
   let productsInCart = new Set();
   let totalPrice = 0; 
   const checkout = document.querySelector('.checkout');
   checkout.addEventListener("click", getSummary);
   
   productsAddBtn.map((btn) => btn.addEventListener("click", addProduct));

   function addProduct(e) {
      const currentProduct = e.currentTarget.parentElement.parentElement;

      let currentProductName = currentProduct.querySelector('.product-title')
         .textContent;
      let currentProductPrice = currentProduct.querySelector('.product-line-price')
         .textContent;
      productsInCart.add(currentProductName);
      totalPrice += Number(currentProductPrice);
      result.value += `Added ${currentProductName} for ${currentProductPrice} to the cart.\n`;
   }

   function getSummary(e) {
      productsAddBtn.map((btn) => btn.disabled = true);
      checkout.disabled = true;
      let listOfProducts = Array.from(productsInCart).join(', ');
      result.value += `You bought ${listOfProducts} for ${totalPrice.toFixed(2)}.`
   }
}
