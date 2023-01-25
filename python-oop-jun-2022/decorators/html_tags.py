def tags(type_of_data):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return f"<{type_of_data}>{result}</{type_of_data}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


@tags('h1')
def to_upper(text):
    return text.upper()


print(join_strings("Hello", " you!"))
print(to_upper('hello'))
