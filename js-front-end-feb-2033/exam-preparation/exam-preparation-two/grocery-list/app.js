function attachEvents() {
    const loadProductsBtn = document.getElementById('load-product');
    const addProductBtn = document.getElementById('add-product');
    const updateProductBtn = document.getElementById('update-product');
    const tBody = document.getElementById('tbody');
    const productInput = document.getElementById('product');
    const countInput = document.getElementById('count');
    const priceInput = document.getElementById('price');
    const BASE_URL = 'http://localhost:3030/jsonstore/grocery/';

    loadProductsBtn.addEventListener('click', loadProducts);
    addProductBtn.addEventListener('click', addProduct);

    function loadProducts(event) {
        if (event) {
            event.preventDefault();
        }
        tBody.innerHTML = '';
        fetch(BASE_URL)
            .then((res) => res.json())
            .then((data) => {
                Object.values(data).forEach(({ _id, count, price, product}) => {
                    const tr = document.createElement('tr');
                    tr.id = _id;
                    const productTd = document.createElement('td');
                    productTd.classList.add('name');
                    productTd.textContent = product;
                    const productCountTd = document.createElement('td');
                    productCountTd.classList.add('count-product');
                    productCountTd.textContent = count;
                    const productPriceTd = document.createElement('td');
                    productPriceTd.classList.add('product-price');
                    productPriceTd.textContent = price;
                    const buttonsTd = document.createElement('td');
                    buttonsTd.classList.add('btn');

                    const updateBtn = document.createElement('button');
                    updateBtn.classList.add('update');
                    updateBtn.textContent = 'Update';
                    const deleteBtn = document.createElement('button');
                    deleteBtn.classList.add('delete');
                    deleteBtn.textContent = 'Delete';

                    deleteBtn.addEventListener('click', deleteProduct);
                    updateBtn.addEventListener('click', updateProduct);

                    buttonsTd.append(updateBtn, deleteBtn);
                    tr.append(productTd, productCountTd, productPriceTd, buttonsTd);
                    tBody.appendChild(tr);
                })
            })
            .catch((err) => {
                console.error(err);
            })
    }

    function addProduct(event) {
        if (event) {
            event.preventDefault();
        }

        const count = countInput.value;
        const price = priceInput.value;
        const product = productInput.value;

        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ count, price, product })
        }

        fetch(BASE_URL, httpHeaders)
            .then(() => loadProducts())
            .then(() => productInput.value = '')
            .then(() => countInput.value = '')
            .then(() => priceInput.value = '')
            .catch((err) => {
                console.error(err);
            })
    }

    function deleteProduct(event) {
        if (event) {
            event.preventDefault();
        }

        const id = event.currentTarget.parentNode.parentNode.id;
        httpHeaders = {
            method: 'DELETE'
        }

        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadProducts())
            .catch((err) => {
                console.error(err);
            })
    }

    function updateProduct(event) {
        if (event) {
            event.preventDefault();
        }

        updateProductBtn.disabled = false;
        addProductBtn.disabled = true;
        const trParentNode = event.currentTarget.parentNode.parentNode;
        const [ product, count, price, _btn ] = Array.from(trParentNode.children);

        productInput.value = product.textContent;
        countInput.value = count.textContent;
        priceInput.value = price.textContent;

        updateProductBtn.addEventListener('click', () => {
            const id = trParentNode.id;
            const count = countInput.value;
            const price = priceInput.value;
            const product = productInput.value;
            const httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({ count, price, product })
            }
            fetch(`${BASE_URL}${id}`, httpHeaders)
                .then(() => loadProducts())
                .then(() => productInput.value = '')
                .then(() => countInput.value = '')
                .then(() => priceInput.value = '')
                .catch((err) => {
                    console.error(err);
                })
        })
    }
}


attachEvents();
