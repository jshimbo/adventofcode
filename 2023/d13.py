def checkRowMirror(y, pattern):
    top = y - 1
    bottom = y
    max_y = len(pattern)

    for _ in range(y):
        top -= 1
        bottom += 1
        if top < 0 or bottom >= max_y:
            return y
        if pattern[top] != pattern[bottom]:
            break

    return 0


def analyzeRows(pattern):
    result = 0
    prev_row = ""

    for y, row in enumerate(pattern):
        if prev_row == row:
            result = checkRowMirror(y, pattern)
            if result > 0:
                return result
        prev_row = row

    return -1


def processPattern(pattern, part):
    # look for horizontal mirror
    result = analyzeRows(pattern)
    if result > 0:
        return result * 100

    # look for vertical mirror by rotating the matrix clockwise
    columns = []
    for x in range(len(pattern[0])):
        col = ""
        for y in range(len(pattern)):
            col += pattern[y][x]
        columns.append(col)

    # same code as above
    result = analyzeRows(columns)
    if result > 0:
        return result

    return -1


def solve(lines, part):
    total = 0
    pattern_lines = []

    for l in lines:
        if len(l) > 2:
            pattern_lines.append(l.strip())
        else:
            total += processPattern(pattern_lines, part)
            pattern_lines.clear()

    # last pattern
    total += processPattern(pattern_lines, part)

    return total


def main():
    input_file = "input/d13.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    # print("Answer to part 1:", solve(lines, part=2))


if __name__ == "__main__":
    main()
