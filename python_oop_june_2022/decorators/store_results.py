def store_results(func_ref):
    def wrapper(*args):
        with open('./result.txt', 'a') as file:
            result = func_ref(*args)
            file.write(f"Function {func_ref.__name__} was add called. Result: {result}\n")

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
