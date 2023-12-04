def solve2(lines):
    cards = {}
    num_cards = len(lines)

    for l in lines:
        subtotal = 0
        s = l.strip().split(":")
        y = s[0].split()
        card_number = int(y[1])
        z = s[1].split("|")
        winning_numbers = z[0].strip().split()
        my_numbers = z[1].strip().split()

        matches = 0
        for num in my_numbers:
            if num in winning_numbers:
                matches += 1

        cards[card_number] = {"matches": matches, "qty": 1}

    for k, v in cards.items():
        matches = v["matches"]
        n = k + 1
        while matches > 0:
            if n > num_cards:
                break
            else:
                cards[n]["qty"] += v["qty"]
                n += 1
                matches -= 1

    return sum([c.get("qty") for _, c in cards.items()])


def solve1(lines):
    total = 0

    for l in lines:
        subtotal = 0
        s = l.strip().split(":")
        y = s[0].split()
        z = s[1].split("|")
        winning_numbers = z[0].strip().split()
        my_numbers = z[1].strip().split()

        for num in my_numbers:
            if num in winning_numbers:
                if subtotal == 0:
                    subtotal = 1
                else:
                    subtotal *= 2
        total += subtotal

    return total


def main():
    input_file = "input/d04.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
