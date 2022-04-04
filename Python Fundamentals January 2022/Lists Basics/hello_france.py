item_prices_list = input().split("|")
budget = int(input())
train_ticket = 150
buying_list = []
final_list = []
profit = 0

for temp_value in item_prices_list:
    current_item = temp_value.split("->")
    for index, item in enumerate(current_item):
        if 'Clothes' in item and 50 >= float(current_item[index + 1]) or \
                'Shoes' in item and 35 >= float(current_item[index + 1]) or \
                'Accessories' in item and 20.50 >= float(current_item[index + 1]):
            if budget - float(current_item[index + 1]) >= 0:
                budget -= float(current_item[index + 1])
                buying_list.append(float(current_item[index + 1]))
            else:
                continue
        current_item = []

for sell in buying_list:
    current_sum = float(sell) + (float(sell) * 0.40)
    budget += current_sum
    profit += current_sum - sell
    final_list.append(current_sum)

for temp_item in final_list:
    print(f"{temp_item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
