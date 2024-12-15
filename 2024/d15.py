import sys


def printMap(m):
    for row in m:
        print("".join([str(x) for x in row]))


def makeMap(lines):
    m = []
    for line in lines:
        m.append(list(line.strip()))
    return m


def scoreMap(map):
    y = 0
    x = 0
    score = 0
    for y, row in enumerate(map):
        for x, space in enumerate(row):
            if space == "O":
                score += y * 100 + x
    return score


def moveX(map, y, x, move, width):
    orig_x = x
    while map[y][x] != "#":
        x = (x + move) % width
        if map[y][x] == ".":
            map[y][x] = "O"
            x = orig_x + move
            map[y][x] = "@"
            map[y][orig_x] = "."
            break

    if map[y][x] == "#":
        x = orig_x

    return (map, x)


def moveY(map, y, x, move, height):
    orig_y = y
    while map[y][x] != "#":
        y = (y + move) % height
        if map[y][x] == ".":
            map[y][x] = "O"
            y = orig_y + move
            map[y][x] = "@"
            map[orig_y][x] = "."
            break

    if map[y][x] == "#":
        y = orig_y

    return (map, y)


def solve(lines, part):
    result = 0
    height = len(lines)
    width = len(lines[0])
    x = -1
    y = -1
    is_moves = False

    map = []
    raw_map = []
    for linenum, line in enumerate(lines):
        if len(line.strip()) == 0:
            is_moves = True
            map = makeMap(raw_map)
            # printMap(map)
        elif not is_moves:
            col = line.find("@")
            if col != -1:
                x = col
                y = linenum
            raw_map.append(line)
        else:
            # is_moves
            for move in list(line.strip()):
                if move == "^":
                    (map, y) = moveY(map, y, x, -1, height)
                elif move == ">":
                    (map, x) = moveX(map, y, x, 1, width)
                elif move == "v":
                    (map, y) = moveY(map, y, x, 1, height)
                elif move == "<":
                    (map, x) = moveX(map, y, x, -1, width)
                else:
                    print("ERROR")

    return scoreMap(map)


def main():
    if len(sys.argv) > 1:
        input_file = "input/d15-pre.txt"
    else:
        input_file = "input/d15.txt"

    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    # print("Answer to part 2:", solve(lines, part=2))


if __name__ == "__main__":
    main()
