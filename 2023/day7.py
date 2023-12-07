from input_manager import get_input
from collections import defaultdict

input = get_input(__file__)
part1 = True

bids = {line.split(" ")[0]: int(line.split(" ")[1]) for line in input}
# 0-6, representing high card to five of a kind respectively.
hand_types: dict[int, list[str]] = defaultdict(list)


# Process type of hand
for hand in bids.keys():
    cards: dict[str, int] = defaultdict(int)
    for card in hand:
        cards[card] += 1
    # Five of a kind
    if len(cards) == 1:
        hand_types[6].append(hand)
    elif len(cards) == 2:
        if 4 in cards.values():
            hand_types[5].append(hand)
        else:
            hand_types[4].append(hand)
    elif len(cards) == 3:
        if 3 in cards.values():
            hand_types[3].append(hand)
        else:
            hand_types[2].append(hand)
    elif len(cards) == 4:
        hand_types[1].append(hand)
    else:
        hand_types[0].append(hand)

card_map = {
    "A": 14,  # Cursed
    "K": 13,
    "Q": 12,
    "J": 11 if part1 else 1, 
    "T": 10,
    **{str(num): num for num in range(2, 10)},
}


def compare_cards(hand1: str, hand2: str) -> bool:
    # Return true if hand1 is better than hand2
    # Both of the hands would be of the same hand type
    # So we just need to compare their cards

    for card1, card2 in zip(hand1, hand2):
        if card_map[card1] == card_map[card2]:
            continue
        return card_map[card1] > card_map[card2]
    raise Exception()


ordered = []
# Ranks comparison
for hand_type in range(7):
    l = hand_types[hand_type]

    for i in range(len(l)):
        swapped = False
        for j in range(0, len(l) - i - 1):
            if compare_cards(l[j], l[j + 1]):
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            break
    ordered.extend(l)

score = 0
for i, hand in enumerate(ordered, start=1):
    score += i * bids[hand]

print(score)
