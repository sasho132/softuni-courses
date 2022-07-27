def genrange(start, end):
    num = start
    while num <= end:
        yield num
        num += 1


print(list(genrange(1, 10)))
