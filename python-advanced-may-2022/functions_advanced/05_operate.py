from functools import reduce


def operate(operator, *args):
    result = 0
    if operator == '+':
        result = reduce(lambda x, y: x + y, args)
    elif operator == '-':
        result = reduce(lambda x, y: x - y, args)
    elif operator == '*':
        result = reduce(lambda x, y: x * y, args)
    elif operator == '/':
        result = reduce(lambda x, y: x / y, args)
    return result
