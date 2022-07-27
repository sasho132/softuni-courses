class vowels:
    def __init__(self, text) -> None:
        self.text = text
        self.i = 0
        self.end = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            current_char = self.text[self.i]
            self.i += 1
            if current_char in 'AEIOUaeiou':
                return current_char
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
