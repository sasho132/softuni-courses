def odds_finder(numbers_list, max_or_min):
    odds = [x for x in numbers_list if x % 2 != 0]
    if len(odds) > 0:
        if max_or_min == "max":
            odd_max = max(odds)
            indices = [index for index, item in enumerate(numbers_list) if item == odd_max]
            return max(indices)

        elif max_or_min == "min":
            odd_min = min(odds)
            indices = [index for index, item in enumerate(numbers_list) if item == odd_min]
            return max(indices)
    else:
        return "No matches"


def evens_finder(numbers_list2, max_or_min):
    evens = [x for x in numbers_list2 if x % 2 == 0]
    if len(evens) > 0:
        if max_or_min == "max":
            even_max = max(evens)
            indices = [index for index, item in enumerate(numbers_list2) if item == even_max]
            return max(indices)
        elif max_or_min == "min":
            even_min = min(evens)
            indices = [index for index, item in enumerate(numbers_list2) if item == even_min]
            return max(indices)
    else:
        return "No matches"


def first(list_of_numbers, counter_first, odd_or_even):
    if odd_or_even == "odd":
        if counter_first > len(list_of_numbers):
            return "Invalid count"
        else:
            current_odds = [x for x in list_of_numbers if x % 2 != 0]
            if counter_first > len(current_odds):
                return current_odds
            else:
                return current_odds[:counter_first]
    elif odd_or_even == "even":
        if counter_first > len(list_of_numbers):
            return "Invalid count"
        else:
            current_evens = [x for x in list_of_numbers if x % 2 == 0]
            if counter_first > len(current_evens):
                return current_evens
            else:
                return current_evens[:counter_first]


def last(list_of_numbers1, counter_last, odd_or_even1):
    if odd_or_even1 == "odd":
        if counter_last > len(list_of_numbers1):
            return "Invalid count"
        else:
            current_odds1 = [x for x in list_of_numbers1 if x % 2 != 0]
            if counter_last > len(current_odds1):
                return current_odds1
            else:
                return current_odds1[- counter_last:]
    elif odd_or_even1 == "even":
        if counter_last > len(list_of_numbers1):
            return "Invalid count"
        else:
            current_evens1 = [x for x in list_of_numbers1 if x % 2 == 0]
            if counter_last > len(current_evens1):
                return current_evens1
            else:
                return current_evens1[- counter_last:]


numbers = list(map(int, input().split(" ")))

command = input()
while command != "end":
    command_list = command.split(" ")
    action = command_list[0]

    if action == "exchange":
        exchange_index = int(command_list[1])
        if 0 <= exchange_index < len(numbers):
            first_half = numbers[exchange_index + 1:]
            second_half = numbers[:exchange_index + 1]
            numbers = first_half + second_half
        else:
            print("Invalid index")

    elif action == "max":
        if command_list[1] == "odd":
            print(odds_finder(numbers, "max"))
        elif command_list[1] == "even":
            print(evens_finder(numbers, "max"))

    elif action == "min":
        if command_list[1] == "odd":
            print(odds_finder(numbers, "min"))
        elif command_list[1] == "even":
            print(evens_finder(numbers, "min"))

    elif action == "first":
        counter = int(command_list[1])
        if command_list[2] == "odd":
            print(first(numbers, counter, "odd"))
        elif command_list[2] == "even":
            print(first(numbers, counter, "even"))

    elif action == "last":
        counter = int(command_list[1])
        if command_list[2] == "odd":
            print(last(numbers, counter, "odd"))
        elif command_list[2] == "even":
            print(last(numbers, counter, "even"))

    command = input()

print(numbers)
