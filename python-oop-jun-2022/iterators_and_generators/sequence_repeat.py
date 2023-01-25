class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            if self.index > len(self.sequence) - 1:
                self.index = 0
            char = self.sequence[self.index]

            self.index += 1
            self.number -= 1
            return char
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
