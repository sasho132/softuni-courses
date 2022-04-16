number_of_electrons = int(input())
shells = list()
shells_counter = 1

while True:
    current_electrons = 2 * shells_counter ** 2
    if number_of_electrons - current_electrons <= 0:
        if number_of_electrons > 0:
            shells.append(number_of_electrons)
        break
    shells.append(current_electrons)
    number_of_electrons -= current_electrons
    shells_counter += 1

print(shells)
