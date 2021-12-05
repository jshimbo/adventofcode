def scan_board(board):
    count = 0
    for row in board:
        row_range = range(len(row))
        for y in row_range:
            if row[y] > 1:
                count += 1
    return count


def print_board(board):
    for row in board:
        new_row = ""
        for x in row:
            if x < 1:
                new_row += '.'
            else:
                new_row += str(x)
        print(new_row)

    print("=end of board=")
    return


def init_board(board, size):
    """
    create square array filled with zeros
    """
    for x in range(size):
        # create row
        new_row = []

        for y in range(size):
            new_row.append(0)

        board.append(new_row)
    print("board has ", len(board), " rows")
    return


def main():
    input_file = "05-input"
    board_size = 1000
    board = []
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    init_board(board, board_size)
    # print_board(board)

    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            if line:
                coords = line.split(" -> ")
                tmp = coords[0].split(',')
                x1 = int(tmp[0])
                y1 = int(tmp[1])
                tmp = coords[1].split(',')
                x2 = int(tmp[0])
                y2 = int(tmp[1])

                if x1 == x2:
                    # Vertical
                    # Point vector down (increasing y)
                    if y1 > y2:
                        # Swap
                        y1, y2 = y2, y1

                    col_range = range(y1, y2+1)
                    for y in col_range:
                        board[y][x1] += 1
                elif y1 == y2:
                    # Horizontal
                    # Point vector to the right (increasing x)
                    if x1 > x2:
                        # swap
                        x1, x2 = x2, x1

                    row_range = range(x1, x2+1)
                    for x in row_range:
                        board[y1][x] += 1
                else:
                    # 45 degrees diagonal, per instructions
                    # Make vector point down (increasing y)
                    if y1 > y2:
                        # swap begin and end
                        x1, x2 = x2, x1
                        y1, y2 = y2, y1

                    x = x1
                    col_range = range(y1, y2+1)
                    for y in col_range:
                        board[y][x] += 1
                        if x2 > x1:
                            x += 1
                        else:
                            x -= 1

    # print_board(board)
    count = scan_board(board)
    print("Count is ", count)


if __name__ == '__main__':
    main()
