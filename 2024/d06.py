def printBoard(board):
    for row in board:
        print(row)


def solve1(lines):
    steps = 1
    board = []
    curx = 0
    cury = 0

    for line in lines:
        board.append(list(line.strip()))

    for y, row in enumerate(board):
        try:
            x = row.index("^")
        except ValueError:
            continue
        curx = x
        cury = y
        break

    max_y = len(board)
    max_x = len(board[0])

    dir = 0  # north, east, south, west

    while 0 <= cury < max_y and 0 <= curx < max_x:
        space = board[cury][curx]
        if space == ".":
            steps += 1
            board[cury][curx] = "X"
        elif space == "#":
            # Obstacle. Backup and turn.
            if dir == 0:
                cury += 1
            elif dir == 1:
                curx -= 1
            elif dir == 2:
                cury -= 1
            else:
                curx += 1

            dir = (dir + 1) % 4  # turn

        if dir == 0:
            cury -= 1
        elif dir == 1:
            curx += 1
        elif dir == 2:
            cury += 1
        else:
            curx -= 1

    return steps


def main():
    input_file = "input/d06.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve1(lines))


if __name__ == "__main__":
    main()
