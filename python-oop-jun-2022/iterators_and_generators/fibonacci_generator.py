def fibonacci():

    current_num = 0
    previous_num = 1

    for i in range(2):
        yield i

    while True:
        result = current_num + previous_num
        yield result
        current_num = previous_num
        previous_num = result


generator = fibonacci()
for i in range(5):
    print(next(generator))

# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
