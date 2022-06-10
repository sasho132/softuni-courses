def grocery_store(**kwargs):
    result = ''
    sorted_products = sorted(kwargs.items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))
    for items_tuple in sorted_products:
        items = items_tuple[0]
        values = items_tuple[1]
        result += f"{items}: {values}\n"
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
