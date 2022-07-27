class take_skip:
    def __init__(self, step, count) -> None:
        self.step = step
        self.count = count
        self.idx = 0 - step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        self.idx += self.step
        self.count -= 1
        return self.idx


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print(11 * '-')

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
