budget = float(input())
flour_price_for_one_kg = float(input())
pack_of_eggs_price = flour_price_for_one_kg * 0.75
price_for_one_l_milk = flour_price_for_one_kg + (flour_price_for_one_kg * 0.25)
milk_price_for_one_bread = price_for_one_l_milk / 4
price_for_one_bread = flour_price_for_one_kg + pack_of_eggs_price + milk_price_for_one_bread
number_of_breads = 0
number_of_colored_eggs = 0

while True:
    if budget - price_for_one_bread <= 0:
        break
    budget -= price_for_one_bread
    number_of_breads += 1
    number_of_colored_eggs += 3
    if number_of_breads % 3 == 0:
        number_of_colored_eggs -= number_of_breads - 2


print(f"You made {number_of_breads} loaves of Easter bread! Now you have {number_of_colored_eggs} eggs and {budget:.2f}BGN left.")
