def checkNumber(board, number):
    row = number["y"]
    col = number["x"]
    digits = ""

    max_y = len(board)
    max_x = len(board[0])

    valid_number = False

    while col < max_x and board[row][col].isdigit():
        digits += board[row][col]

        # scan for symbol
        for y in [row - 1, row, row + 1]:
            for x in [col - 1, col, col + 1]:
                if x >= 0 and x < max_x and y >= 0 and y < max_y:
                    if not board[y][x].isdigit() and board[y][x] != ".":
                        valid_number = True

        col += 1

    if valid_number:
        result = int(digits)
    else:
        result = 0

    return result


def getNumbers(board):
    answer = []

    for row_num, row in enumerate(board):
        x = 0
        max_x = len(row)
        in_number = False

        while x < max_x:
            c = row[x]
            if c.isdigit():
                if x == 0 or not in_number:
                    in_number = True
                    answer.append({"y": row_num, "x": x})
            else:
                in_number = False
            x += 1

    return answer


def solve1(board):
    total = 0

    numbers = getNumbers(board)

    for number in numbers:
        total += checkNumber(board, number)

    return total


def createBoard(lines):
    board = []
    for l in lines:
        l = l.strip()
        row = [c for c in l]
        board.append(row)
    return board


def main():
    input_file = "input/d03.txt"
    with open(input_file) as f:
        lines = f.readlines()

    board = createBoard(lines)

    print("Answer to part 1:", solve1(board))
    # print("Answer to part 2:", solve2(lines))


if __name__ == "__main__":
    main()
