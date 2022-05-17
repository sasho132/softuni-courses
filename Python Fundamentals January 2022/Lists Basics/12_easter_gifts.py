gift_list = input().split(" ")

command = input()
while command != "No Money":
    command_list = list(command.split(" "))
    if "OutOfStock" in command:
        out_of_stock = command_list[1]
        for index, temp_gift in enumerate(gift_list):
            if temp_gift == out_of_stock:
                gift_list[index] = "None"

    elif "Required" in command_list:
        searched_index = int(command_list[2])
        given_gift = command_list[1]
        if 0 <= searched_index < len(gift_list):
            gift_list[searched_index] = given_gift

    elif "JustInCase" in command_list:
        in_case_gift = command_list[1]
        gift_list[-1] = in_case_gift

    command = input()

filtered_gifts = list(filter(lambda x: x != "None", gift_list))
print(" ".join(filtered_gifts))
