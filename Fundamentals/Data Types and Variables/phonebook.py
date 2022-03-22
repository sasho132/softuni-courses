def search_name(phonebook_dict, counter):
    for _ in range(counter):
        searched_name = input()
        if searched_name in phonebook_dict:
            print(f"{searched_name} -> {phonebook_dict[searched_name]}")
        else:
            print(f"Contact {searched_name} does not exist.")


phonebook = {}

line = input().split("-")
while True:
    if line[0].isdigit():
        # counter == int(line[0])
        search_name(phonebook, int(line[0]))
        break
    name = line[0]
    phone = line[1]
    phonebook[name] = phone

    line = input().split("-")
