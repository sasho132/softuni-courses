products = {}

command = input()
while command != "statistics":
    get_products = command.split(": ")
    key = get_products[0]
    value = int(get_products[1])

    if key not in products:
        products[key] = 0
    products[key] += value

    command = input()

print("Products in stock:")

for item, quantity in products.items():
    print(f"- {item}: {quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
