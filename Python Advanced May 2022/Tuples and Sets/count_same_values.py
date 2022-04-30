numbers = [float(el) for el in input().split()]
numbers_dict = {}

for num in numbers:
    if num not in numbers_dict:
        numbers_dict[num] = 0
    numbers_dict[num] += 1
    
for tp in numbers_dict.items():
    print(f"{tp[0]} - {tp[1]} times")
    