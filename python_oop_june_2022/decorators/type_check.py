def type_check(type_of_data):
    def decorator(func_ref):
        def wrapper(*args):
            for ar in args:
                if not isinstance(ar, type_of_data):
                    return "Bad Type"
            return func_ref(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2

@type_check(str)
def first_letter(word):
    return word[0]

print(times2(2))
print(times2('Not A Number'))


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))