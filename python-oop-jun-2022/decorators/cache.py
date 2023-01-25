def cache(func_ref):
    memo = {}

    def wrapper(number):
        if number in memo:
            return memo[number]
        result = func_ref(number)
        memo[number] = result
        return result

    wrapper.log = memo
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)