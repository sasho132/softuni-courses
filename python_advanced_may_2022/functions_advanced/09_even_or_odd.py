def even_odd(*args):
    numbers = args[:len(args) - 1]
    command = args[-1]
    if command == 'even':
        return [x for x in numbers if x % 2 == 0]
    else:
        return [x for x in numbers if x % 2 != 0]
