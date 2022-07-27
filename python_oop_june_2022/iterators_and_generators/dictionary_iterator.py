class dictionary_iter:
    def __init__(self, obj: dict) -> None:
        self.obj = list(obj.items())
        self.end = len(obj) - 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > self.end:
            raise StopIteration
        current_kvp = self.obj[self.idx]
        self.idx += 1
        return current_kvp


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
