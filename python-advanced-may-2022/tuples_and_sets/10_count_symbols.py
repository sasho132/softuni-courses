text = input()
characters_dict = {}

for el in text:
    if el not in characters_dict:
        characters_dict[el] = 0
    characters_dict[el] += 1

sorted_characters = sorted(characters_dict)
for current_element in sorted_characters:
    print(f"{current_element}: {characters_dict[current_element]} time/s")
