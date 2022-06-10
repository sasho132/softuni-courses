def sorting_cheeses(**kwargs):
    result = ''
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in kwargs:
        name = tuple_[0]
        values = tuple_[-1]
        result += name + "\n"
        quantity = sorted(values, reverse=True)
        result += '\n'.join(map(str, quantity))
        result += '\n'
    return result
