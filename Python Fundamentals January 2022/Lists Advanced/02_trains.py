train = [0] * int(input())

command = input().split(" ")
while command[0] != "End":
    if command[0] == "add":
        number_of_people = int(command[1])
        train[-1] += number_of_people
    elif command[0] == "insert":
        wagon = int(command[1])
        number_of_people = int(command[2])
        train[wagon] += number_of_people
    elif command[0] == "leave":
        wagon = int(command[1])
        number_of_people = int(command[2])
        train[wagon] -= number_of_people
    command = input().split(" ")

print(train)
