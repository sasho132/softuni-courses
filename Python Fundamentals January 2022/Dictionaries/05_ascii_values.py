list_of_chars = input().split(", ")

res = {word: ord(word) for word in list_of_chars}

print(res)
