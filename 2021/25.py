import sys


def make_moves(cukes, moves, dir):
    if not moves:
        return cukes

    height = len(cukes)
    width = len(cukes[0])
    right_edge = width - 1
    lower_edge = height - 1

    if dir == 'right':
        for move in moves:
            x = move[0]
            x2 = 0 if x == right_edge else (x + 1)
            y = move[1]
            cukes[y][x] = '.'
            cukes[y][x2] = '>'
    elif dir == 'down':
        for move in moves:
            x = move[0]
            y = move[1]
            y2 = 0 if y == lower_edge else (y + 1)
            cukes[y][x] = '.'
            cukes[y2][x] = 'v'
    else:
        print("Bad direction in make_moves()")
        sys.exit()

    return cukes


def get_moves(cukes, dir):
    height = len(cukes)
    width = len(cukes[0])
    right_edge = width - 1
    lower_edge = height - 1

    moves = []

    if dir == 'down':
        for y, row in enumerate(cukes):
            for x, c in enumerate(row):
                if c == 'v':
                    y2 = 0 if y == lower_edge else y + 1
                    if cukes[y2][x] == '.':
                        moves.append((x, y))
    elif dir == 'right':
        for y, row in enumerate(cukes):
            for x, c in enumerate(row):
                if c == '>':
                    x2 = 0 if x == right_edge else x + 1
                    if cukes[y][x2] == '.':
                        moves.append((x, y))
    else:
        print("Bad direction in get_moves()")
        sys.exit()
    return moves


def print_board(b):
    """Print board in AoC style"""
    s = ''
    for row in b:
        s = ("".join([c for c in row]))
        print(s)
    print("")
    return


def main():
    input_file = "input/25-input"

    lines = open(input_file if len(sys.argv) <
                 2 else sys.argv[1], encoding="utf-8").readlines()

    board = []
    for line in lines:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        board.append(row)

    # print_board(board)

    count = 0
    moves_r = moves_d = [True]
    while moves_r or moves_d:
        moves_r = get_moves(board, 'right')
        board = make_moves(board, moves_r, 'right')
        moves_d = get_moves(board, 'down')
        board = make_moves(board, moves_d, 'down')
        count += 1

    # print_board(board)
    print("Answer is", count)


if __name__ == "__main__":
    main()
