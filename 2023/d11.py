def printSpace(space):
    for row in space:
        print("".join(row))


def listGalaxies(space):
    galaxies = []

    for y, row in enumerate(space):
        for x, c in enumerate(row):
            if c != ".":
                galaxies.append((x, y))

    return galaxies


def getDistance(g1, g2, empty_rows, empty_columns, expansion_factor=1):
    # base distance
    distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    # add expansion
    empty = 0
    for x in range(*sorted([g1[0], g2[0]])):
        if x in empty_columns:
            empty += 1

    for y in range(*sorted([g1[1], g2[1]])):
        if y in empty_rows:
            empty += 1

    distance += empty * max(expansion_factor - 1, 1)

    return distance


def solve(lines, expansion_factor):
    total = 0
    space = []
    empty_rows = []
    empty_columns = []

    for i, l in enumerate(lines):
        row = list(l.strip())
        if all(c == "." for c in row):
            empty_rows.append(i)
        space.append(row)

    # expand columns
    empty_bools = [c == "." for c in space[0]]
    for row in space[1:]:
        empty_bools = [c and (row[i] == ".") for i, c in enumerate(empty_bools)]

    for i, c in enumerate(empty_bools):
        if c:
            empty_columns.append(i)

    galaxies = listGalaxies(space)
    num_pairs = 0

    for i1, g1 in enumerate(galaxies[:-1]):
        for g2 in galaxies[i1 + 1 :]:
            num_pairs += 1
            total += getDistance(g1, g2, empty_rows, empty_columns, expansion_factor)

    return total


def main():
    input_file = "input/d11.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, expansion_factor=1))
    print("Answer to part 2:", solve(lines, expansion_factor=1000000))


if __name__ == "__main__":
    main()
