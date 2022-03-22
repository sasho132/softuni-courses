orders_dict = {}

line = input()
while line != 'buy':
    command = line.split(" ")
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if name not in orders_dict:
        orders_dict[name] = [price, quantity]
    else:
        for index, cur_value in enumerate(orders_dict[name]):
            if index == 0:
                if price != cur_value:
                    orders_dict[name][index] = price
            elif index == 1:
                orders_dict[name][index] += quantity
    line = input()

for key, value in orders_dict.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")
    