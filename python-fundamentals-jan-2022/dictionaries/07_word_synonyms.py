synonyms_dict = {}

number = int(input())

for w in range(number):
    word = input()
    synonym = input()

    if word not in synonyms_dict:
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for current_word in synonyms_dict:
    print(f"{current_word} - {', '.join(synonyms_dict[current_word])}")
