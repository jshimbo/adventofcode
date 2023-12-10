from functools import cmp_to_key

# hand types
HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
THREE = 3
FULL_HOUSE = 4
FOUR = 5
FIVE = 6


def compareCards(a, b):
    alphabet = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "T": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "2": 0,
    }
    result = 0
    if alphabet[a] < alphabet[b]:
        result = -1
    elif alphabet[a] > alphabet[b]:
        result = 1
    return result


def compareHands(a, b):
    left = list(a["cards"])
    right = list(b["cards"])

    n = len(left)
    i = 0
    result = 0
    while i < n:
        result = compareCards(left[i], right[i])
        if result != 0:
            break
        i += 1

    return result


def collateCards(hand):
    bins = {}

    cards = list(hand["cards"])
    for c in cards:
        try:
            bins[c] += 1
        except KeyError:
            bins[c] = 1

    return bins


def classify_hand(hand):
    card_list = collateCards(hand)

    # five of a kind
    num_pairs = 0
    has_three = False
    for c in card_list:
        if card_list[c] == 5:
            return FIVE
        elif card_list[c] == 4:
            return FOUR
        elif card_list[c] == 3:
            # Full house or three of a kind
            has_three = True
        elif card_list[c] == 2:
            # One or two pairs
            num_pairs += 1

    if has_three:
        if num_pairs == 1:
            return FULL_HOUSE
        else:
            return THREE
    elif num_pairs == 2:
        return TWO_PAIR
    elif num_pairs == 1:
        return PAIR
    else:
        return HIGH_CARD


def solve1(lines):
    total = 1

    hands = []

    results = [
        [],  # High card
        [],  # One pair
        [],  # Two pairs
        [],  # Three of a kind
        [],  # Full House
        [],  # Four of a kind
        [],  # Five of a kind
    ]

    for line in lines:
        h = line.split()
        hands.append({"cards": h[0], "bid": int(h[1])})

    for hand in hands:
        hand_type = classify_hand(hand)
        results[hand_type].append(hand)

    sorted_hands = []
    for v in results:
        if len(v) > 0:
            res = sorted(v, key=cmp_to_key(compareHands))
            for r in res:
                sorted_hands.append(r)

    i = 1
    total = 0
    for hand in sorted_hands:
        total += i * hand["bid"]
        i += 1

    return total


def main():
    input_file = "input/d07.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    # print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
