list_of_num_strings = input().split()
list_of_integers = []
list_of_strings = []
numbers_left = []
number = int(input())

for num in list_of_num_strings:
    list_of_integers.append(int(num))

for current_number in range(number):
    list_of_integers.remove(min(list_of_integers))

for string in list_of_integers:
    list_of_strings.append(str(string))

print(", ".join(list_of_strings))
