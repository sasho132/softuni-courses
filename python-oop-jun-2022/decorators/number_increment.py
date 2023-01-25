def number_increment(numbers):

    def increase():
        result = [n + 1 for n in numbers]
        return result

    return increase()


print(number_increment([1, 2, 3]))
