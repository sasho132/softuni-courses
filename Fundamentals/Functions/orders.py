def order_calculate(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2

    total_price = price * quantity
    return total_price


product_type = input()
quantity_of_product = int(input())
order_price = order_calculate(product_type, quantity_of_product)
print(f"{order_price:.2f}")