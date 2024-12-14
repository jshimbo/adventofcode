import re
from math import prod


def printMap(m, s):
    print_it = False
    for row in m:
        line = "".join(row)
        if s in line:
            print_it = True
            break

    if print_it:
        for row in m:
            print("".join(row))

    return print_it


def printPoints(points, width, height, sec):
    result = -1
    m = []
    for _ in range(height):
        m.append([" "] * width)

    midx = width // 2
    midy = height // 2
    for key in points:
        (x, y) = key
        if x != midx and y != midy:
            m[y][x] = "^"

    if printMap(m, "^^^^^^^^^^"):
        result = sec + 1
    else:
        result = -1

    return result


def makeVectors(lines):
    v = []
    for line in lines:
        data = re.findall(r"p=(-*\d+),(-*\d+) v=(-*\d+),(-*\d+)", line)
        (x, y, dx, dy) = data[0]
        v.append((int(x), int(y), int(dx), int(dy)))
    return v


def coalesce(vectors, width, height):
    points = {}
    midx = width // 2
    midy = height // 2
    for vector in vectors:
        (x, y, _, _) = vector
        if y != midy and x != midx:
            points[(x, y)] = points.get((x, y), 0) + 1

    return points


def tally(vectors, width, height):
    scores = [0, 0, 0, 0]
    midx = width // 2
    midy = height // 2
    for vector in vectors:
        (x, y, _, _) = vector
        if y != midy and x != midx:
            index = 2 * (y > midy) + (x > midx)
            scores[index] += 1

    # return scores[0] * scores[1] * scores[2] * scores[3]
    return prod(scores[:4])


def solve(lines, part):
    result = -1
    width = 101
    height = 103

    if part == 1:
        seconds = 100
    else:
        seconds = 10000

    vectors = makeVectors(lines)

    for sec in range(seconds):
        for i, vector in enumerate(vectors):
            (x, y, dx, dy) = vector
            x = (x + dx) % width
            y = (y + dy) % height
            vectors[i] = (x, y, dx, dy)

        if part == 2:
            points = coalesce(vectors, width, height)
            result = printPoints(points, width, height, sec)
            if result >= 0:
                break

    if part == 1:
        result = tally(vectors, width, height)

    return result


def main():
    input_file = "input/d14.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    print("Answer to part 2:", solve(lines, part=2))


if __name__ == "__main__":
    main()
