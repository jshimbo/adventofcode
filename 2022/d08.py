def scenicScore(forest, x_pos, y_pos):
    # Assume that x_pos and y_pos are not on the edges
    # print(x_pos, y_pos)
    height = len(forest)
    width = len(forest[0])

    tree_height = forest[x_pos][y_pos]

    score = 1  # one because we're multiplying

    # check down
    subtotal = 0
    x = x_pos
    for y in range(y_pos+1, height):
        subtotal += 1
        if tree_height <= forest[x][y]:
            break

    score *= subtotal

    # check up
    subtotal = 0
    x = x_pos
    for y in range(y_pos-1, -1, -1):
        subtotal += 1
        if tree_height <= forest[x][y]:
            break

    score *= subtotal

    # check right
    subtotal = 0
    y = y_pos
    for x in range(x_pos+1, width):
        subtotal += 1
        if tree_height <= forest[x][y]:
            break

    score *= subtotal

    # check left
    subtotal = 0
    y = y_pos
    for x in range(x_pos-1, -1, -1):
        subtotal += 1
        if tree_height <= forest[x][y]:
            break

    score *= subtotal

    return score


def checkClearance(forest, x_pos, y_pos):
    # Assume that x_pos and y_pos are not on the edges
    height = len(forest)
    width = len(forest[0])

    tree_height = forest[x_pos][y_pos]

    # check down
    x = x_pos
    nope = False
    for y in range(y_pos+1, height):
        if tree_height <= forest[x][y]:
            nope = True
            break
    if not nope:
        return True

    # check up
    x = x_pos
    nope = False
    for y in range(0, y_pos):
        if tree_height <= forest[x][y]:
            nope = True
            break
    if not nope:
        return True

    # check right
    y = y_pos
    nope = False
    for x in range(x_pos+1, width):
        if tree_height <= forest[x][y]:
            nope = True
            break
    if not nope:
        return True

    # check left
    y = y_pos
    nope = False
    for x in range(0, x_pos):
        if tree_height <= forest[x][y]:
            nope = True
            break
    if not nope:
        return True

    return False


def solve(forest, part):
    height = len(forest)
    width = len(forest[0])
    result = 0

    if part == 1:
        result += width * 2  # top and bottom rows
        result += (height - 2) * 2  # left and right edges

        for x in range(1, width-1):
            for y in range(1, height-1):
                if checkClearance(forest, x, y):
                    result += 1
    else:
        # part 2
        for x in range(1, width-1):
            for y in range(1, height-1):
                res = scenicScore(forest, x, y)
                if res > result:
                    result = res

    return result


def main():
    input_file = 'input/d08.txt'
    with open(input_file) as fp:
        lines = fp.read().splitlines()

    input_data = []
    for line in lines:
        input_data.append([int(x) for x in line])

    print("Part 1:", solve(forest=input_data, part=1))
    print("Part 2:", solve(forest=input_data, part=2))


if __name__ == '__main__':
    main()
