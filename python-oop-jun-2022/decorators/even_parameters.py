def even_parameters(func_ref):
    def wrapper(*args):
        for ar in args:
            if not isinstance(ar, int) or ar % 2 != 0:
                return "Please use only even numbers!"

        return func_ref(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(add(2, 4))
print(add("Peter", 1))

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
