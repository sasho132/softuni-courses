class custom_range:
    def __init__(self, start, end) -> None:
        self.i = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            i = self.i
            self.i += 1
            return i
        raise StopIteration()


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
