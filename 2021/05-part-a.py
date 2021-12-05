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
    start = [0, 0]
    finish = [0, 0]

    init_board(board, board_size)
    # print_board(board)

    with open(input_file) as fp:
        for line in fp:
            line = line.strip()
            if line:
                coords = line.split(" -> ")
                tmp = coords[0].split(',')
                start[0] = int(tmp[0])
                start[1] = int(tmp[1])
                tmp = coords[1].split(',')
                finish[0] = int(tmp[0])
                finish[1] = int(tmp[1])

                # print("start coords: ", start)
                # print("end coords ", finish)

                if start[0] == finish[0]:
                    # vertical = True
                    x = start[0]
                    if start[1] < finish[1]:
                        y1 = start[1]
                        y2 = finish[1]
                    else:
                        y1 = finish[1]
                        y2 = start[1]

                    col_range = range(y1, y2+1)
                    for y in col_range:
                        board[y][x] += 1
                elif start[1] == finish[1]:
                    # horizontal
                    y = start[1]
                    if start[0] < finish[0]:
                        x1 = start[0]
                        x2 = finish[0]
                    else:
                        x1 = finish[0]
                        x2 = start[0]

                    row_range = range(x1, x2+1)
                    for x in row_range:
                        board[y][x] += 1

    # print_board(board)
    count = scan_board(board)
    print("Count is ", count)


if __name__ == '__main__':
    main()
