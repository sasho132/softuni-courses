def existing_item(catalog, searched_item):
    if searched_item in catalog:
        return True
    else:
        return False


def combine(catalog, first_item, second_item):
    first_item = catalog.index(first_item)
    catalog.insert(first_item + 1, second_item)
    return catalog


journal = input().split(", ")

command = input().split(" - ")
while command[0] != "Craft!":
    action = command[0]
    if action == "Collect":
        item = command[1]
        if not existing_item(journal, item):
            journal.append(item)

    elif action == "Drop":
        item = command[1]
        if existing_item(journal, item):
            journal.remove(item)

    elif action == "Combine Items":
        combine_items = command[1].split(":")
        old_item = combine_items[0]
        new_item = combine_items[1]
        if existing_item(journal, old_item):
            current_combine = combine(journal, old_item, new_item)

    elif action == "Renew":
        item = command[1]
        if existing_item(journal, item):
            journal.remove(item)
            journal.append(item)

    command = input().split(" - ")

print(", ".join(journal))
