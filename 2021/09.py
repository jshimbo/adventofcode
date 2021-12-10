def get_basin(lines, coord):
    # Are we on the field of play?
    x, y = coord
    if not x in range(len(lines[0])) or not y in range(len(lines)):
        return 0

    # Is spot marked or is this a peak?
    i = lines[y][x]
    if i == -1 or i == 9:
        return 0

    # else

    result = 1  # score it
    lines[y][x] = -1  # mark map

    # check up, down, left, right
    result += get_basin(lines, (x, y-1))
    result += get_basin(lines, (x, y+1))
    result += get_basin(lines, (x-1, y))
    result += get_basin(lines, (x+1, y))

    return result


def part2(lines, suspects):
    basins = []

    for suspect in suspects:
        basins.append(get_basin(lines, suspect))

    basins.sort()
    basins.reverse()
    result = 1  # because we're multiplying
    for x in basins[0:3]:
        result *= x

    return result


def part1(lines, suspects):

    height = len(lines)

    # check vertical neighbors
    risk_level = 0
    for x, y in suspects:
        i = lines[y][x]
        if y == 0:
            if i < lines[y+1][x]:
                risk_level += 1 + i
        elif y == (height - 1):
            if i < lines[y-1][x]:
                risk_level += 1 + i
        else:
            if i < lines[y-1][x] and i < lines[y+1][x]:
                risk_level += 1 + i

    return risk_level


def get_suspects(lines):
    suspects = []

    width = len(lines[0])

    # check horizontal neighbors
    y = 0
    for line in lines:
        for x in range(width):
            i = line[x]
            if x == 0:
                if i < line[x+1]:
                    suspects.append((x, y))
            elif x == (width - 1):
                if i < line[x-1]:
                    suspects.append((x, y))
            else:
                if i < line[x-1] and i < line[x+1]:
                    suspects.append((x, y))
        y += 1
    return(suspects)


def main():
    answer1 = 0
    answer2 = 0

    input_file = 'input/09-input'

    lines = []
    with open(input_file) as fp:
        for line in fp:
            lines.append(list(map(int, list(line.strip()))))

    suspects = get_suspects(lines)

    answer1 = part1(lines, suspects)
    answer2 = part2(lines, suspects)

    print("Answers:")
    print("  Part 1", answer1)
    print("  Part 2", answer2)


if __name__ == '__main__':
    main()
