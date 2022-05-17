number = int(input())
opening_bracket_counter = 0
closing_bracket_counter = 0
bracket = ""


for i in range(0, number):
    current_command = input()
    if current_command == "(":
        opening_bracket_counter += 1
        bracket = current_command
    elif bracket == "(" and current_command == ")":
        closing_bracket_counter += 1
        bracket = ""

if opening_bracket_counter == closing_bracket_counter and opening_bracket_counter != 0 and closing_bracket_counter != 0:
    print('BALANCED')
else:
    print('UNBALANCED')
    