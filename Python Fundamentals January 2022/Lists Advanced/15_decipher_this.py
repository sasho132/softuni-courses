import re

text = input().split(" ")

for current_string in text:
    filtered = re.split('(\d+)', current_string)
    current_letter = chr(int(filtered[1]))
    filtered[1] = current_letter
    temp_word = filtered[1] + filtered[2]
    word_list = list(temp_word)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    result = "".join(word_list)
    print(result, end=" ")
