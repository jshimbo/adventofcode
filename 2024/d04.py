import re


def makeMap(lines):
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m


def printMap(m):
    for row in m:
        print("".join(row))


def rotateMap(m):
    transposed = list(zip(*m))
    return [list(reversed(row)) for row in transposed]


def makeMask(s):
    # make matrix with string in diagonal
    width = len(s)  # matrix is square

    target = list(s)
    mask = []

    for y in range(width):
        mask.append([])
        for x in range(width):
            if x == y:
                mask[y].append(target[x])
            else:
                mask[y].append(" ")

    return mask


def matrixMatch(map, mask, y0, x0):
    # overlay mask on mastrix and check for match
    for y in range(len(mask)):
        for x in range(len(mask[0])):
            y2 = y + y0
            x2 = x + x0
            if (
                y2 >= len(map)
                or x2 >= len(map[0])
                or (mask[y][x] != " " and mask[y][x] != map[y2][x2])
            ):
                return 0
    return 1


def findXmas(m, target, mask1, mask2):
    score = 0
    for y, row in enumerate(m):
        if target:
            s = "".join(row)
            part1 = re.findall(target, s)
            part2 = re.findall(target[::-1], s)
            score += len(part1) + len(part2)
        for x in range(len(row)):
            score += matrixMatch(m, mask1, y, x)
            score += matrixMatch(m, mask2, y, x)
    return score


def solve(lines, part):
    m = makeMap(lines)
    score = 0

    if part == 1:
        target_string = "XMAS"
        mask1 = makeMask(target_string)
        mask2 = makeMask(target_string[::-1])
        score = findXmas(m, target_string, mask1, mask2)
        mr = rotateMap(m)
        score += findXmas(mr, target_string, mask1, mask2)
    else:
        mask1 = []
        mask2 = []
        s = "M S"
        mask1.append(list(s))
        mask2.append(list(reversed(list(s))))
        s = " A "
        mask1.append(list(s))
        mask2.append(list(s))
        s = "M S"
        mask1.append(list(s))
        mask2.append(list(reversed(list(s))))
        # Skip searching for "XMAS" string
        score = findXmas(m, None, mask1, mask2)
        mr = rotateMap(m)
        score += findXmas(mr, None, mask1, mask2)

    return score


def main():
    input_file = "input/d04.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    print("Answer to part 2:", solve(lines, part=2))


if __name__ == "__main__":
    main()
