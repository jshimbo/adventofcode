# Day 22: Monkey Map

def takeStep(map, pos, facing):
    (x, y) = pos

    if facing == 3:  # right
        y2 = y
        x2 = x + 1
        if x2 >= len(map[y2]):
            x2 = 0
    elif facing == 9:  # left
        y2 = y
        x2 = x - 1
        if x2 < 0:
            x2 = len(map[y2]) - 1
    elif facing == 6:  # down
        x2 = x
        y2 = y + 1
        if y2 >= len(map) or x >= len(map[y2]):
            y2 = y
            while x < len(map[y2]):
                y2 -= 1
                if y2 < 0:
                    break
            y2 += 1  # fix overshoot
    else:  # up
        x2 = x
        y2 = y - 1
        if y2 < 0 or x >= len(map[y2]):
            y2 = y
            while x < len(map[y2]):
                y2 += 1
                if y2 >= len(map):
                    break
            y2 -= 1  # fix overshoot

    assert not (x != x2 and y != y2)

    return (x2, y2)


def makeMove(map, pos, steps, facing):

    (x, y) = pos
    (x2, y2) = (x, y)

    history = []
    history.append(pos)

    stop = False
    for i in range(steps):
        if stop:
            break

        last_pos = (x2, y2)
        (x2, y2) = takeStep(map, last_pos, facing)

        if map[y2][x2] == '.':
            history.append((x2, y2))

        elif map[y2][x2] == '#':
            stop = True
            (x2, y2) = history.pop()

        else:
            while map[y2][x2] == ' ':
                (x2, y2) = takeStep(map, (x2, y2), facing)
            if map[y2][x2] == '#':
                stop = True
                (x2, y2) = history.pop()

    return (x2, y2)


def getMove(path, ptr):
    i = ptr
    move = []

    s = ""

    pathlen = len(path)
    while i < pathlen:
        if path[i].isdigit():
            s += path[i]
            i += 1
        else:
            break

    moves = int(s)
    if i < pathlen:
        turn = path[i]
    else:
        turn = 0
    ptr = i+1
    return (moves, turn, ptr)


def findOrigin(map):
    y = 0
    x = 0
    line = map[0]
    for c in line:
        if c == '.':
            return (x, y)
        x += 1

    return False


def solve(paper_map, path):
    result = 0
    map = []
    path = path.strip()

    # digitize the map
    for line in paper_map.splitlines():
        map.append(line)

    facing = 3  # three o'clock
    pos = findOrigin(map)

    ptr = 0
    while ptr < len(path):
        (steps, turn, ptr) = getMove(path, ptr)

        pos = makeMove(map, pos, steps, facing)
        if turn == 'R':
            facing = (facing + 3) % 12
        elif turn == 'L':
            facing = (facing - 3 + 12) % 12
        else:  # turn == 0
            break

    if facing == 3:
        face_value = 0
    elif facing == 6:
        face_value = 1
    elif facing == 9:
        face_value = 2
    else:
        face_value = 3

    (x, y) = pos
    result = 4 * (x+1) + 1000 * (y+1) + face_value

    return result


def main():
    # filename = "input/d22-pre"
    filename = "input/d22.txt"
    with open(filename) as f:
        parts = f.read().split("\n\n")

    print("Part 1:", solve(paper_map=parts[0], path=parts[1]))


if __name__ == '__main__':
    main()
