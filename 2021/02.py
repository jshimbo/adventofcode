def main():
    input_file = 'input/02-input'
    lines = []
    with open(input_file) as fp:
        lines = [tuple(line.split()) for line in fp]

    # part 1
    moves = {}
    for cmd, v in lines:
        moves[cmd] = moves.get(cmd, 0) + int(v)
    answer1 = moves.get('forward') * \
        (moves.get('down') - moves.get('up'))

    # part 2
    aim = 0
    depth = 0
    fwd = 0
    for cmd, v in lines:
        if cmd == 'down':
            aim += int(v)
        if cmd == 'up':
            aim -= int(v)
        elif cmd == 'forward':
            fwd += int(v)
            depth += aim * int(v)
    answer2 = fwd * depth

    print('Answers:')
    print('  Part 1', answer1)
    print('  Part 2', answer2)


if __name__ == '__main__':
    main()
