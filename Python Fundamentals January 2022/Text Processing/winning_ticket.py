def side_check(side, valid_symbols):
    symbol = ''
    counter = 0
    for char in side:
        if char not in valid_symbols:
            if counter >= 6:
                break
            counter = 0
            symbol = char
        else:
            symbol = char
            counter += 1
    return symbol, counter


def ticket_validator(ticket):
    valid_symbols = '@#$^'
    left_half = ticket[:10]
    right_half = ticket[10:]

    if len(ticket) != 20:
        print("invalid ticket")
    elif ticket[0] * 20 == ticket and ticket[0] in valid_symbols:
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
    else:
        # index[0] = special_symbol and index[1] = counter
        left_side = side_check(left_half, valid_symbols)
        right_side = side_check(right_half, valid_symbols)

        data_side = ''
        if left_side > right_side:
            data_side = right_side
        else:
            data_side = left_side

        special_symbol = data_side[0]
        symbol_counter = data_side[1]

        if symbol_counter < 6 or special_symbol not in valid_symbols:
            print(f'ticket "{ticket}" - no match')
        else:
            print(f'ticket "{ticket}" - {symbol_counter}{special_symbol}')


tickets_data = (input().split(","))
tickets = [x.strip() for x in tickets_data]

for current_ticket in tickets:
    ticket_validator(current_ticket)
