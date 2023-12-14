ROCK = "O"
SPACE = "."
# CUBE = "#"


def printBoard(board):
    row_num = len(board)
    for row in board:
        print(f"{''.join(row)} {row_num:2}")
        row_num -= 1


def scoreBoard(board):
    score = 0
    multiplier = len(board)
    for row in board:
        score += sum(c == ROCK for c in row) * multiplier
        multiplier -= 1

    return score


def tiltBoard(board):
    for y in range(1, len(board)):
        for x in range(len(board[y])):
            move_rock = False
            if board[y][x] == ROCK:
                for y2 in range(y - 1, -1, -1):
                    if board[y2][x] == SPACE:
                        move_rock = True
                        destination = y2
                    else:
                        break
                if move_rock:
                    board[y][x] = SPACE
                    board[destination][x] = ROCK

    return board


def solve(lines, part):
    total = 0
    board = []

    for l in lines:
        row = [c for c in l.strip()]
        board.append(row)

    board = tiltBoard(board)
    # printBoard(board)

    total += scoreBoard(board)

    return total


def main():
    input_file = "input/d14.txt"
    with open(input_file) as f:
        lines = f.readlines()

    print("Answer to part 1:", solve(lines, part=1))
    # print("Answer to part 1:", solve(lines, part=2))


if __name__ == "__main__":
    main()
