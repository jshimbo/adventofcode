def print_board(m):
    """Print board in AoC style"""
    print("")
    s = ''
    for row in m:
        s = ("".join([str(c) for c in row]))
        print(s)
    return


def print_board_space(m):
    """Print board with spaces so we can see 10s"""
    print("")
    s = ''
    for row in m:
        s = (" ".join([str(c) for c in row]))
        print(s)
    return


def new_matrix(n):
    """Unused but keep for reference"""
    global width
    global height
    row = [n] * width
    return row * height


def inc_mat_item(m, y, x):
    """Increment one item in matrix"""
    global width
    global height

    if 0 <= y < height and 0 <= x < width:
        if m[y][x] != 10:
            # Ignore 10 because it needs to flash
            m[y][x] += 1

    return m


def mat_trim(m):
    """Count and reset flashed cells"""
    global flashes
    for row, i in enumerate(m):
        for col, j in enumerate(i):
            if m[row][col] > 9:
                m[row][col] = 0
                flashes += 1
    return m


def matix_contains(m, elem):
    """Look for value in matrix"""
    for row, i in enumerate(m):
        try:
            col = i.index(elem)
        except ValueError:
            continue
        return row, col
    return -1, -1


def fallout(board):
    """Process flashes and secondary fallout"""
    done = False
    while not done:
        # Check for 10, because a unit can flash once per step
        # Once flashed it will be greater than 10 until
        #   the trim operation
        y, x = matix_contains(board, 10)
        if y == -1 or x == -1:
            done = True
        else:
            board[y][x] += 1
            # left and right
            inc_mat_item(board, y, x - 1)
            inc_mat_item(board, y, x + 1)
            # above
            y2 = y - 1
            inc_mat_item(board, y2, x - 1)
            inc_mat_item(board, y2, x)
            inc_mat_item(board, y2, x + 1)
            # below
            y2 = y + 1
            inc_mat_item(board, y2, x - 1)
            inc_mat_item(board, y2, x)
            inc_mat_item(board, y2, x + 1)

    # Reset units that flashed
    result = mat_trim(board)
    return result


def increment(m):
    for row, i in enumerate(m):
        for col, j in enumerate(i):
            m[row][col] += 1
    return m


def part1(board, steps):
    global flashes
    flashes = 0
    for step in range(steps):
        board = increment(board)
        board = fallout(board)
    print_board(board)
    return flashes


def part2(board):
    global flashes
    flashes = 0
    prev_flashes = flashes
    step = 0
    all_flashed = False

    while not all_flashed:
        board = increment(board)
        board = fallout(board)
        if (flashes - prev_flashes) == (height * width):
            all_flashed = True
        prev_flashes = flashes
        step += 1

    print("All flashed at step", step)
    print_board(board)
    return step


width = 0
height = 0
flashes = 0


def main():
    global width
    global height
    global flashes

    input_file = "input/11-input"
    steps = 100

    board = []
    for line in open(input_file).readlines():
        l = list(map(int, line.strip()))
        if len(l) > 0:
            board.append(l)

    width = len(board[0])
    height = len(board)
    print("Board is", width, "X", height)
    answer1 = part1(board, steps)

    # reset the board for part 2
    board = []
    for line in open(input_file).readlines():
        l = list(map(int, line.strip()))
        if len(l) > 0:
            board.append(l)
    answer2 = part2(board)

    print("Answers")
    print("  Part 1:", answer1)
    print("  Part 2:", answer2)


if __name__ == '__main__':
    main()
