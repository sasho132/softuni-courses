factor = int(input())
count = int(input())
number_list = []
current_multiplayer = factor

for i in range(count):
    if current_multiplayer % factor == 0:
        number_list.append(current_multiplayer)
    current_multiplayer += factor

print(number_list)
