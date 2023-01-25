words = input().split(" ")

words_dict = {}

for word in words:
    lower_cases = word.lower()

    if lower_cases not in words_dict:
        words_dict[lower_cases] = 0
    words_dict[lower_cases] += 1

for key, value in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")
