text = input()

vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
filter_text = [x for x in text if x not in vowels]

filtered_text = "".join(filter_text)
print(filtered_text)
