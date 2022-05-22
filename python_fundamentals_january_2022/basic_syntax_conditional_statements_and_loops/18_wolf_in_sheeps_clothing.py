text = input()
sheep_list = text.split(", ")
wolf_is_the_closest_animal = False
wolf_count = 0

for index, animal in enumerate(reversed(sheep_list)):
    if animal == 'wolf':
        if index == 0:
            wolf_is_the_closest_animal = True
        else:
            wolf_count = index

if wolf_is_the_closest_animal:
    print('Please go away and stop eating my sheep')
else:
    print(f"Oi! Sheep number {wolf_count}! You are about to be eaten by a wolf!")
    