def for_all_characters(a, b):
    characters_string = ""

    for char in range(ord(a) + 1, ord(b)):
        character = chr(char)
        characters_string += character
        characters_string += " "

    return characters_string


first_character = input()
second_character = input()
result = for_all_characters(first_character, second_character)
print(result)
