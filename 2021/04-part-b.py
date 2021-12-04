def score_board(board):
    if not board:
        print("score_board() received empty board")
        return(False)

    sum = 0
    cols = range(len(board[0]))
    rows = range(len(board))
    for col in cols:
        for row in rows:
            number = board[row][col]
            if number != -1:
                sum += number

    return(sum)


def check_cols(board):
    for col in range(5):
        sum = 0
        for row in range(5):
            sum += board[row][col]
        if sum == -5:
            return(True)
    return(False)


def check_rows(board):
    for row in range(5):
        sum = 0
        for col in range(5):
            sum += board[row][col]
        if sum == -5:
            return(True)
    return(False)


def check_bingo(board):
    """
    Check one board for Bingo
    Return True if Bingo. Otherwise, return false
    """
    if board and (check_rows(board) or check_cols(board)):
        return(True)
    else:
        return(False)


def main():
    numbers = []
    boards = []
    input_file = "04-input"
    new_board = []
    last_winning_board = False
    score = 0

    with open(input_file) as fp:
        for line in fp:
            line = line.strip()

            if not numbers:
                # get bingo numbers
                num_strings = line.split(',')
                for n in num_strings:
                    numbers.append(int(n))
                continue

            if not line:
                # end of board (or bingo numbers)
                if new_board:
                    boards.append(new_board)
                    new_board = []
            else:
                new_line = []
                tmp_line = line.split()
                for s in tmp_line:
                    new_line.append(int(s))

                new_board.append(new_line)

    # In case last line of input is not blank
    if new_board:
        boards.append(new_board)

    # Run the bingo game
    # print(numbers)
    for number in numbers:
        # mark boards
        for board_num in range(len(boards)):
            board = boards[board_num]
            if board:
                # mark the board
                for row in range(5):
                    for col in range(5):
                        if board[row][col] == number:
                            # print("hit")
                            board[row][col] = -1
                if check_bingo(board):
                    last_winning_board = board
                    last_winning_num = number
                    # Burn winning board
                    boards[board_num] = False

    print("bingo!")
    print(last_winning_board)
    print("Last number = ", last_winning_num)
    score = score_board(last_winning_board)
    print("Prelim score = ", score)
    print("Final score = ", score * last_winning_num)


if __name__ == '__main__':
    main()
