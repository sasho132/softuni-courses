text = input()
while text != "end":
    reversed_text = ''
    for i in reversed(text):
        reversed_text += i
    print(f"{text} = {reversed_text}")

    text = input()
