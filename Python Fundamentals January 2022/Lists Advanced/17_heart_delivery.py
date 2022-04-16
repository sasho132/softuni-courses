def houses_jump(houses, index):
    if houses[index] <= 0:
        return print(f"Place {index} already had Valentine's day.")
    else:
        houses[index] -= 2
        if houses[index] <= 0:
            return print(f"Place {index} has Valentine's day.")
        return houses


def failed_houses(houses):
    failed = [int(house) for house in houses if house > 0]
    return len(failed)


neighborhood = [int(house) for house in input().split("@")]
cupid_index = 0

cupid_jump = input().split()
while cupid_jump[0] != "Love!":
    jump_length = int(cupid_jump[1])
    if cupid_index + jump_length >= len(neighborhood):
        cupid_index = 0
    else:
        cupid_index += jump_length
    current_jump = houses_jump(neighborhood, cupid_index)

    cupid_jump = input().split()
print(f"Cupid's last position was {cupid_index}.")
if failed_houses(neighborhood):
    print(f"Cupid has failed {failed_houses(neighborhood)} places.")
else:
    print("Mission was successful.")
