elements = input().split(" ")
searched_products = input().split(" ")
products = {}


for e in range(0, len(elements), 2):
    key = elements[e]
    value = elements[e + 1]
    products[key] = int(value)

for current_product in searched_products:
    if current_product in products:
        print(f"We have {products[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
