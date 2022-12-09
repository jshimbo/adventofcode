def solve(moves, knots):
    rope = []
    positions = set()

    for _ in range(knots):
        rope.append((0, 0))

    for move in moves:
        dir = move[0]
        steps = move[1]
        for _ in range(steps):
            # first move the head
            head = 0
            if dir == 'U':
                rope[head] = (rope[head][0], rope[head][1]+1)
            elif dir == 'D':
                rope[head] = (rope[head][0], rope[head][1]-1)
            elif dir == 'R':
                rope[head] = (rope[head][0]+1, rope[head][1])
            else:  # Left
                rope[head] = (rope[head][0]-1, rope[head][1])

            # update tail(s)
            for head in range(knots-1):
                tail = head + 1

                deltaX = rope[head][0] - rope[tail][0]
                deltaY = rope[head][1] - rope[tail][1]

                if deltaX > 1:
                    if deltaY > 1:
                        rope[tail] = (rope[tail][0]+1, rope[tail][1]+1)
                    elif deltaY < -1:
                        rope[tail] = (rope[tail][0]+1, rope[tail][1]-1)
                    else:
                        rope[tail] = (rope[tail][0]+1, rope[head][1])
                elif deltaX < -1:
                    if deltaY > 1:
                        rope[tail] = (rope[tail][0]-1, rope[tail][1]+1)
                    elif deltaY < -1:
                        rope[tail] = (rope[tail][0]-1, rope[tail][1]-1)
                    else:
                        rope[tail] = (rope[tail][0]-1, rope[head][1])
                elif deltaY > 1:
                    rope[tail] = (rope[head][0], rope[tail][1]+1)
                elif deltaY < -1:
                    rope[tail] = (rope[head][0], rope[tail][1]-1)

                if tail == (knots-1) and not rope[tail] in positions:
                    positions.add(rope[tail])

    return len(positions)


def main():
    input_file = 'input/d09-pre'
    input_file = 'input/d09.txt'

    lines = []
    with open(input_file) as f:
        for line in f:
            s = line.strip().split(' ')
            lines.append((s[0], int(s[1])))

    # print(lines)
    print("Part 1:", solve(moves=lines, knots=2))
    print("Part 2:", solve(moves=lines, knots=10))


if __name__ == '__main__':
    main()
