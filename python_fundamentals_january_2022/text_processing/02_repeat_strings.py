text_data = input().split()

for word in text_data:
    res = word * len(word)
    print(f"{res}", end='')
