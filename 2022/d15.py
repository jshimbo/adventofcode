import re


def mergeChords(input):
    result = []

    chords = sorted(input)

    current = None

    for chord in chords:
        if not current:
            current = chord
            continue

        (head, tail) = current
        (head2, tail2) = chord

        if tail < head2:
            result.append(current)
            current = chord
            continue
        else:
            if head > head2:
                head = head2
            if tail < tail2:
                tail = tail2
            current = (head, tail)

    result.append(current)

    return result


def getChords(board, y):
    result = []

    # if beacon at this position, return False
    for sensor in board:
        sx = sensor["sensor"][0]
        sy = sensor["sensor"][1]
        d = sensor["distance"]

        delta = abs(sy - y)

        # formula for the chord is: 2 * (d - delta) + 1
        x = d - delta
        if x == 0:
            result.append((sx, sx))
        elif x > 0:
            x1 = sx - x
            x2 = sx + x
            result.append((x1, x2))

    return result


def solve(lines, part):

    board = []

    for line in lines:
        l = line.split(':')
        s = re.findall(r'\d+', l[0])
        sx = int(s[0])
        sy = int(s[1])
        s = re.findall(r'\d+', l[1])
        bx = int(s[0])
        by = int(s[1])

        distance = abs(bx - sx) + abs(by - sy)

        s = {"sensor": (sx, sy),
             "beacon": (bx, by),
             "distance": distance}

        board.append(s)

    if part == 1:
        y = 2000000

        chords = getChords(board, y)

        chords = mergeChords(chords)

        result = 0
        for c in chords:
            (head, tail) = c
            result += tail - head
    else:  # part 2
        result = None
        for y in range(4000001):
            if (y % 500000) == 0:
                print(y)

            chords = getChords(board, y)

            chords = mergeChords(chords)

            if len(chords) > 1:
                print("y =", y, ":", chords)
                (begin, end) = chords[1]
                x = begin-1
                m = 4000000
                result = m * x + y
                break

    return result


def main():
    filename = "input/d15.txt"
    with open(filename) as f:
        lines = f.read().splitlines()

    print("Part 1:", solve(lines=lines, part=1))
    print("Part 2:", solve(lines=lines, part=2))


if __name__ == '__main__':
    main()
