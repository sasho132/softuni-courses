card_deck = input().split()
shuffle_count = int(input())
current_card_deck = []

for shuffle in range(shuffle_count):
    half_deck = len(card_deck) // 2
    left_part = card_deck[:half_deck]
    right_part = card_deck[half_deck:]
    for card in range(len(left_part)):
        current_card_deck.append(left_part[card])
        current_card_deck.append((right_part[card]))
    card_deck = current_card_deck
    current_card_deck = []

print(card_deck)
