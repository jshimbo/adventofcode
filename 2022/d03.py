def scoreItems(duplicates):
    score = 0
    for c in duplicates:
        if c.isupper():
            score += ord(c) - ord("A") + 27
        else:
            score += ord(c) - ord("a") + 1
    return score


def solve1(lines):
    score = 0
    for l in lines:
        pocket = set()
        bag_size = len(l)
        pocket_size = int(bag_size/2)
        duplicates = set()
        for i in range(bag_size):
            bag_item = l[i]
            if i < pocket_size:
                pocket.add(bag_item)
            elif bag_item in pocket:
                if not bag_item in duplicates:
                    duplicates.add(bag_item)

        # print(bag_size, pocket_size, pocket, duplicates)
        score += scoreItems(duplicates)

    return score


def solve2(lines):
    score = 0
    count = 0
    bags = []
    badges = set()
    for l in lines:
        bag = set()
        for bag_item in l:
            bag.add(bag_item)
        bags.append(bag)

        count += 1
        if count == 3:  # one-offset because we just incremented
            badges = badges.union(bags[0].intersection(bags[1], bags[2]))
            score += scoreItems(badges)
            # reinitialize variables
            count = 0
            bags = []
            badges = set()

    return score


def main():
    # filename = "input/d03-pre"
    filename = "input/d03"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve1(lines))
    print("Part 2:", solve2(lines))


if __name__ == '__main__':
    main()
