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


def makeSpace(lines):
    space = []

    for l in lines:
        row = list(l.strip())
        if all(c == "." for c in row):
            # make a copy before appending
            space.append(list(row))
        space.append(row)

    # expand columns
    empty_bools = [c == "." for c in space[0]]
    for row in space[1:]:
        empty_bools = [c and (row[i] == ".") for i, c in enumerate(empty_bools)]

    empty_col_nums = []
    for i, c in enumerate(empty_bools):
        if c:
            empty_col_nums.append(i)

    empty_col_nums.reverse()

    for row in space:
        for i in empty_col_nums:
            row.insert(i, ".")

    return space


def solve1(lines):
    total = 0
    space = makeSpace(lines)

    galaxies = listGalaxies(space)

    for i1, g1 in enumerate(galaxies[:-1]):
        for i2, g2 in enumerate(galaxies[i1 + 1 :]):
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return total


def main():
    input_file = "input/d11.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))
    # print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
