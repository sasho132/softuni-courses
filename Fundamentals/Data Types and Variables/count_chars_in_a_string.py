text = input().split(" ")

text_dict = {}

for word in text:
    for char in word:
        if char not in text_dict:
            text_dict[char] = 0
        text_dict[char] += 1

for key, value in text_dict.items():
    print(f"{key} -> {value}")
