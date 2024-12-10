from queue import LifoQueue


def printMap(m):
    for row in m:
        print("".join([str(x) for x in row]))


def makeMap(lines):
    m = []
    for line in lines:
        m.append([int(c) for c in list(line.strip())])
    return m


def lookAround(stack, m, y, x):
    i = m[y][x]
    # look right (x + 1)
    new = x + 1
    if 0 <= new < len(m[y]):
        j = m[y][new]
        if j == i + 1:
            stack.put((y, new, j))
    # look down (y + 1)
    new = y + 1
    if 0 <= new < len(m):
        j = m[new][x]
        if j == i + 1:
            stack.put((new, x, j))
    # look left (x - 1)
    new = x - 1
    if 0 <= new < len(m[y]):
        j = m[y][new]
        if j == i + 1:
            stack.put((y, new, j))
    # look up (y - 1)
    new = y - 1
    if 0 <= new < len(m):
        j = m[new][x]
        if j == i + 1:
            stack.put((new, x, j))

    return stack


def getScore(m, y, x):
    stack = LifoQueue()
    dups = []
    score = 0

    stack.put((y, x, m[y][x]))

    while not stack.empty():
        y, x, c = stack.get()
        if c == 9:
            if (y, x) not in dups:
                score += 1
                dups.append((y, x))
        else:
            stack = lookAround(stack, m, y, x)

    return score


def solve(lines):
    trailheads = LifoQueue()
    score = 0
    m = makeMap(lines)

    for y, row in enumerate(m):
        for x, c in enumerate(row):
            if c == 0:
                trailheads.put((y, x, c))

    while not trailheads.empty():
        y, x, c = trailheads.get()

        i = getScore(m, y, x)
        score += i
    return score


def main():
    input_file = "input/d10.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines))


if __name__ == "__main__":
    main()
