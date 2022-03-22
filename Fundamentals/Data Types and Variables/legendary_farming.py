key_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}

searched_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}

is_obtained = False

while not is_obtained:
    data_line = input().split(" ")
    # using list() slicing to obtain list(items) and list(quantities)
    quantity, items = data_line[0::2], data_line[1::2]
    # convert items() in lower cases
    items = [x.lower() for x in items]
    # map quantity() in integers
    quantity = list(map(int, quantity))
    for current_item, current_value in zip(items, quantity):
        if current_item in searched_items:
            searched_items[current_item] += current_value
            if searched_items[current_item] >= 250:
                searched_items[current_item] -= 250
                print(f"{key_items[current_item]} obtained!")
                is_obtained = True
                break
        else:
            if current_item not in junk_items:
                junk_items[current_item] = 0
            junk_items[current_item] += current_value

for item, quantity in searched_items.items():
    print(f"{item}: {quantity}")

for material, value in junk_items.items():
    print(f"{material}: {value}")
