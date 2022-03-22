coffee_counter = 0
one_coffee_commands = ['coding', 'dog', 'cat', 'movie']
two_coffee_command = ['CODING', 'DOG', 'CAT', 'MOVIE']

command = input()
while command != 'END':
    if command in one_coffee_commands:
        coffee_counter += 1
    elif command in two_coffee_command:
        coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)
