def makeLists(lines):
    antennas = {}

    for y, line in enumerate(lines):
        line = line.strip()
        for x, c in enumerate(line):
            if c != ".":
                if c not in antennas:
                    antennas[c] = [(y, x)]
                else:
                    antennas[c].append((y, x))

    return antennas


def getAntinodes(a, b):
    (y1, x1) = a
    (y2, x2) = b

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if x1 < x2:
        an1_x = x1 - dx
        an2_x = x2 + dx
    else:
        an1_x = x1 + dx
        an2_x = x2 - dx

    if y1 < y2:
        an1_y = y1 - dy
        an2_y = y2 + dy
    else:
        an1_y = y1 + dy
        an2_y = y2 - dy

    return [(an1_y, an1_x), (an2_y, an2_x)]


def solve(lines):
    total = 0
    dup_list = []
    antennas = makeLists(lines)

    ymax = len(lines) - 1
    xmax = len(lines[0].strip()) - 1

    for _, list in antennas.items():
        for i, coord in enumerate(list):
            for j in range(i + 1, len(list)):
                antinodes = getAntinodes(coord, list[j])
                for an in antinodes:
                    (y, x) = an
                    if 0 <= x <= xmax and 0 <= y <= ymax and not an in dup_list:
                        total += 1
                        dup_list.append(an)

    return total


def main():
    input_file = "input/d08.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines))


if __name__ == "__main__":
    main()
